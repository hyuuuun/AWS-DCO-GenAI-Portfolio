# -*- coding: utf-8 -*-
"""
DCO(Data Center Operations) 교육용 로그 분석기 (Python 초보자용)
- 이 스크립트는 외부 라이브러리(패키지) 없이 파이썬 표준 기능만 사용합니다.
- 비전공자도 한 줄씩 읽으며 쉽게 이해할 수 있도록 상세한 주석이 작성되어 있습니다.
"""

# 입력 파일명과 출력 파일명을 변수로 지정합니다.
INPUT_FILE_NAME = "sample_dco_log.txt"
OUTPUT_FILE_NAME = "incident_summary.md"

def analyze_dco_logs():
    # 1. 분석을 위해 필요한 데이터 저장소(변수)들을 준비합니다.
    total_lines = 0                   # 전체 로그 라인 수
    severity_counts = {}              # 심각도별 개수를 저장할 딕셔너리 (예: {"INFO": 5, "WARNING": 2})
    event_counts = {}                 # 이벤트별 개수를 저장할 딕셔너리 (예: {"Normal heartbeat": 10})
    warning_or_critical_logs = []     # WARNING 또는 CRITICAL 등급의 로그를 담을 리스트
    key_events_summary = []           # CRC error, Link Down, Ticket escalated 관련 주요 로그 요약

    # 2. 로그 파일을 안전하게 열어서 한 줄씩 읽어옵니다.
    try:
        # 'with open' 구문을 사용하면 작업이 끝난 후 파일이 자동으로 닫힙니다.
        # 인코딩 오류 방지를 위해 utf-8을 설정해 줍니다.
        with open(INPUT_FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                # 줄 바꿈 문자(\n)와 양쪽 공백을 제거합니다.
                cleaned_line = line.strip()
                
                # 빈 줄은 건너뜁니다.
                if not cleaned_line:
                    continue
                
                # 전체 라인 수 증가
                total_lines += 1
                
                # 각 줄은 ' | ' 문자열로 구분되어 있습니다. 이를 쪼개어 각각 변수에 담아줍니다.
                # 예: timestamp | device | severity | event | message
                parts = [part.strip() for part in cleaned_line.split("|")]
                
                # 형식이 맞지 않는 줄은 무시하거나 에러를 방지합니다. (정상 로그는 5개 구역으로 구성됨)
                if len(parts) < 5:
                    continue
                
                timestamp = parts[0]
                device = parts[1]
                severity = parts[2]
                event = parts[3]
                message = parts[4]
                
                # --- [분석 1] 심각도(Severity) 카운트 ---
                # 딕셔너리에 이미 해당 심각도가 존재하면 +1, 없으면 새로 만들며 1을 대입합니다.
                if severity in severity_counts:
                    severity_counts[severity] += 1
                else:
                    severity_counts[severity] = 1
                    
                # --- [분석 2] 이벤트(Event) 카운트 ---
                if event in event_counts:
                    event_counts[event] += 1
                else:
                    event_counts[event] = 1
                
                # --- [분석 3] WARNING 또는 CRITICAL 등급 로그 목록 수집 ---
                # 심각도가 WARNING이거나 CRITICAL인 경우 별도 목록에 저장합니다.
                if severity == "WARNING" or severity == "CRITICAL":
                    warning_or_critical_logs.append({
                        "timestamp": timestamp,
                        "device": device,
                        "severity": severity,
                        "event": event,
                        "message": message,
                        "raw": cleaned_line
                    })
                
                # --- [분석 4] CRC_ERROR, LINK_DOWN, TICKET_ESCALATED 포함 여부 확인 ---
                # 대소문자나 언어 표현 차이에 유연하게 대응하기 위해, 텍스트를 대문자로 바꾼 후 키워드를 비교합니다.
                # 예: 'CRC error 증가' 에는 'CRC'가 포함되고, 'Link Down'에는 'LINK'와 'DOWN'이 포함됩니다.
                upper_event = event.upper()
                upper_msg = message.upper()
                
                is_crc = ("CRC" in upper_event) or ("CRC" in upper_msg)
                is_link_down = ("LINK DOWN" in upper_event) or ("LINK DOWN" in upper_msg) or ("LINK" in upper_event and "DOWN" in upper_event)
                is_escalated = ("ESCALATED" in upper_event) or ("ESCALATED" in upper_msg)
                
                if is_crc or is_link_down or is_escalated:
                    # 어떤 유형인지 분류해서 태그를 붙여줍니다.
                    category = []
                    if is_crc: category.append("CRC_ERROR")
                    if is_link_down: category.append("LINK_DOWN")
                    if is_escalated: category.append("TICKET_ESCALATED")
                    
                    key_events_summary.append({
                        "categories": category,
                        "timestamp": timestamp,
                        "device": device,
                        "severity": severity,
                        "event": event,
                        "message": message
                    })

    except FileNotFoundError:
        print(f"오류: 입력 파일인 '{INPUT_FILE_NAME}'을 찾을 수 없습니다.")
        print("현재 디렉토리에 로그 파일이 존재하지 않는 것 같습니다. 먼저 파일을 생성해 주세요.")
        return
    except Exception as e:
        print(f"분석 중 예상치 못한 오류가 발생했습니다: {e}")
        return

    # 3. 분석한 결과를 incident_summary.md 파일에 마크다운 형식으로 예쁘게 기록합니다.
    try:
        with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as out_file:
            out_file.write("# 📋 교육용 DCO 로그 분석 보고서 (Incident Summary)\n\n")
            out_file.write(f"- **분석 시각**: 2026-07-19\n")
            out_file.write(f"- **대상 로그 파일**: `{INPUT_FILE_NAME}`\n")
            out_file.write(f"- **총 로그 수**: {total_lines} 줄\n\n")
            
            # --- 심각도 분포 기록 ---
            out_file.write("## 1. 심각도별(Severity) 발생 현황\n")
            out_file.write("| 심각도 (Severity) | 빈도수 (Counts) | 비율 |\n")
            out_file.write("| --- | --- | --- |\n")
            # 내림차순 정렬하여 보여줍니다.
            for sev, count in sorted(severity_counts.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / total_lines) * 100
                out_file.write(f"| {sev} | {count} | {percentage:.1f}% |\n")
            out_file.write("\n")
            
            # --- 이벤트 유형 분포 기록 ---
            out_file.write("## 2. 이벤트별(Event) 발생 현황\n")
            out_file.write("| 이벤트명 (Event) | 빈도수 (Counts) |\n")
            out_file.write("| --- | --- |\n")
            # 빈도수가 높은 것부터 정렬하여 상위 목록을 보여줍니다.
            for evt, count in sorted(event_counts.items(), key=lambda x: x[1], reverse=True):
                out_file.write(f"| {evt} | {count} |\n")
            out_file.write("\n")
            
            # --- WARNING / CRITICAL 로그 목록 기록 ---
            out_file.write("## 3. WARNING 또는 CRITICAL 등급 로그 세부 목록\n")
            if not warning_or_critical_logs:
                out_file.write("*해당 등급의 로그가 발견되지 않았습니다.*\n\n")
            else:
                out_file.write(f"총 {len(warning_or_critical_logs)}개의 이슈 로그가 식별되었습니다.\n\n")
                out_file.write("| 시간 | 장비명 | 심각도 | 이벤트 | 상세 메시지 |\n")
                out_file.write("| --- | --- | --- | --- | --- |\n")
                for item in warning_or_critical_logs:
                    out_file.write(f"| {item['timestamp']} | `{item['device']}` | **{item['severity']}** | {item['event']} | {item['message']} |\n")
                out_file.write("\n")
                
            # --- 주요 이벤트(CRC, LINK DOWN, ESCALATED) 요약 기록 ---
            out_file.write("## 4. 장애 및 에스컬레이션 주요 이벤트 요약\n")
            out_file.write("DCO 인턴십 직무 이해를 위한 핵심 키워드(CRC_ERROR, LINK_DOWN, TICKET_ESCALATED) 기반 수집 결과입니다.\n\n")
            if not key_events_summary:
                out_file.write("*관련 중요 이벤트가 발견되지 않았습니다.*\n")
            else:
                out_file.write("| 시간 | 구분 | 장비명 | 이벤트명 | 세부 메시지 |\n")
                out_file.write("| --- | --- | --- | --- | --- |\n")
                for item in key_events_summary:
                    cat_str = ", ".join(item['categories'])
                    out_file.write(f"| {item['timestamp']} | `{cat_str}` | `{item['device']}` | {item['event']} | {item['message']} |\n")
            out_file.write("\n")
            out_file.write("---\n")
            out_file.write("*참고: 본 보고서는 학습용 샘플 데이터를 기반으로 가공된 교육 전용 분석 결과입니다. 실제 프로덕션 서버 정보는 담겨있지 않습니다.*\n")
            
        print(f"성공: 분석 결과가 '{OUTPUT_FILE_NAME}' 파일로 저장되었습니다!")
        
    except Exception as e:
        print(f"보고서 파일 작성 중 오류가 발생했습니다: {e}")

# 스크립트가 직접 실행되는 경우 분석 함수를 호출합니다.
if __name__ == "__main__":
    analyze_dco_logs()
