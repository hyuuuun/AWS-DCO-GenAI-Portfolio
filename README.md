# AWS DCO 인턴십 직무 이해를 위한 생성형 AI 활용 포트폴리오

공개된 DCO(Data Center Operations) 직무 맥락과 교육용 샘플 데이터를 바탕으로 기초 용어, 로그 분석, 사건 문서화, Ticket 우선순위 판단과 교대 인수인계를 학습한 결과물입니다.

> **EDUCATIONAL SAMPLE DATA**
>
> 이 저장소의 로그, 장비명, IP 주소, Ticket과 사건은 모두 교육용 샘플입니다. 실제 AWS 내부 시스템, 운영 로그, 장비 또는 내부 절차를 포함하지 않습니다.

## 프로젝트 소개

이 프로젝트에서는 생성형 AI를 최종 답을 대신 만드는 도구가 아니라 학습과 검토를 돕는 보조 도구로 사용했습니다.

- DCO 직무 용어와 협업 맥락 정리
- 교육용 로그를 Python으로 파싱하고 사건별로 요약
- CRC Error와 Link Down 사건의 시간 흐름 분석
- 로그에서 확인된 사실, 가능한 원인과 미확인 정보 구분
- 교육용 Incident Report 작성
- 여러 Ticket의 영향과 상태를 비교하여 우선순위 판단
- 다음 담당자를 위한 Shift Handover Memo 작성
- AI 결과를 원본 로그와 다시 비교하고 오류 수정

## 학습 흐름

```text
교육용 샘플 로그
→ Python 로그 요약
→ CRC Error·Link Down 사건 분석
→ 교육용 Incident Report
→ 멀티 Ticket 우선순위 판단
→ Shift Handover Memo
```

## 주요 학습 및 수행 내용

| 영역 | 수행 내용 | 대표 결과물 |
|---|---|---|
| 협업 역량 정리 | 개인의 강점과 DCO 직무의 협업 상황 연결 | [DCO 직무 협업 유형 리포트](02_dco_profile/dco_collaboration_profil.md) |
| DCO 기초 용어 | Rack, Server, Ticket, SLA, SOP, NIC, ToR Switch 등의 개념 정리 | [DCO 인프라 용어 사전](01_dco_glossary/dco_infra_terms.md) |
| 교육용 문서 자동화 | 샘플 Ticket과 로그 확인용 체크리스트 작성 | [샘플 Ticket](06_cli_file_automation/sample_ticket.md), [랙 확인 체크리스트](06_cli_file_automation/rack_checklist.md) |
| 다중 로그 분석 | 여러 서버 로그에서 CRC Error와 Link Down 이벤트를 구분하는 Python 코드 작성 | [다중 로그 분석 코드](07_log_analysis_script2/analyze_logs.py) |
| 로그 요약 | 심각도와 이벤트를 집계하고 주요 사건을 Markdown으로 출력 | [로그 분석기](09_log_analysis_script/analyzer.py), [분석 결과](09_log_analysis_script/incident_summary.md) |
| 사건 분석 | CRC Error 증가부터 Link Down, 조치와 복구까지 시간순으로 분석 | [CRC Error·Link Down 분석](10_incident_analysis/crc_linkdown_analysis.md) |
| Incident 문서화 | 장비, Ticket, 사건 흐름, 사실, 추정과 미확인 정보를 보고서로 정리 | [교육용 Incident Report](11_incident_report/dco_incident_report.md) |
| Ticket 우선순위 | 현재 영향, 반복 여부, 영향 범위, 복구 상태와 Ticket 상태를 함께 비교 | [Ticket 우선순위 Matrix](12_ticket_triage_handover/ticket_priority_matrix.md), [CSV](12_ticket_triage_handover/ticket_priority_matrix.csv) |
| 교대 인수인계 | Open·Monitoring·Resolved Ticket과 다음 확인 사항을 전달 문서로 구성 | [Shift Handover Memo](12_ticket_triage_handover/shift_handover.md) |

## 대표 분석 사례

### CRC Error·Link Down 사건

- 샘플 장비: `SAMPLE_TOR_SW_01`
- 인터페이스: `Gi0/1`
- 교육용 Ticket: `EDU-TKT-2026-0003`
- 분석 구간: 2026-07-03 03:05~03:30
- 확인된 흐름: CRC 오류 카운터 증가 → Link Down → Ticket 생성·Escalation → 패치 코드 교체 및 커넥터 청소 → Link Up → 정상 상태 기록
- 분석 원칙: 조치 후 복구는 사실이지만, 현재 로그만으로 최초 원인을 하나로 확정하지 않음

### Ticket 우선순위와 Handover

- 교대 기준 시점: 2026-07-10 07:55
- 교육용 판단 순서: `0202 → 0201 → 0203 → 0204`
- 1순위 판단: `0202`는 서비스 중단은 기록되지 않았지만 Feed A 경고가 지속되고 정상 이중 전원이 복구되지 않았으며 관련 샘플 서버가 6대로 표시됨
- 판단 원칙: Severity만 보지 않고 현재 영향, 반복·지속, 영향 범위, 복구 여부, Ticket 상태와 부족한 정보를 함께 검토
- 주의 사항: 우선순위는 로그에 적힌 사실이 아니라 주어진 시점과 기준에 따른 교육용 판단

## 직무 역량과 연결되는 경험

| 역량 | 프로젝트에서 수행한 활동 | 현재 수준과 보완점 |
|---|---|---|
| 문제 해결 | 사건을 시간순으로 정리하고 가능한 원인과 추가 확인 정보를 구분 | 기초 분석 단계이며 네트워크·하드웨어 원리 보충 필요 |
| Python | 텍스트 로그 파싱, 심각도·이벤트 집계와 Markdown 결과 생성 | 기본 파일 처리와 조건 분류 경험, 예외 처리와 테스트 보완 필요 |
| 문서화 | 체크리스트, Incident Report와 Handover Memo 작성 | 교육용 문서 구조 경험, 실제 조직 양식과 운영 절차 경험은 없음 |
| 우선순위 판단 | 네 Ticket의 영향, 반복, 범위와 복구 상태 비교 | 주어진 샘플 기준 판단이며 다양한 사례 연습 필요 |
| 협업·보고 | 다음 담당자가 확인할 사실, 미확인 정보와 후속 확인 항목 정리 | 글로 정리하는 기초 경험, 구두 브리핑 연습 필요 |
| Git·GitHub | 차시별 파일과 분석 결과를 저장소 구조로 관리 | 기본 버전관리 경험, 커밋 단위와 설명 품질 개선 필요 |

## 사용 도구

| 도구 | 활용 내용 |
|---|---|
| 생성형 AI(OpenAI Codex) | 문서 구조화, 코드와 보고서 초안 작성, 로컬 파일 검토 보조 |
| Python | 교육용 로그 파싱, 심각도·이벤트 집계와 결과 파일 생성 |
| PowerShell·`rg` | 파일 탐색, 사건 구간 검색과 결과 교차검증 |
| VS Code | Markdown, Python, CSV와 로그 파일 확인 및 편집 |
| Git·GitHub | 산출물 버전관리와 포트폴리오 구성 |
| Markdown·CSV | 분석 결과, 우선순위 Matrix와 인수인계 내용 표현 |

## 생성형 AI 활용 및 검증 원칙

- AI의 답변은 검토가 필요한 초안으로 사용했습니다.
- 장비명, 시간, Ticket ID, 상태와 사건 수치를 원본 로그와 비교했습니다.
- 로그에서 직접 확인한 내용은 사실로, 가능한 설명은 추정으로 구분했습니다.
- 로그만으로 확인할 수 없는 Root Cause는 확정하지 않았습니다.
- Ticket 우선순위는 여러 기준을 비교한 교육용 판단으로 명시했습니다.
- AI가 “CRC 오류 154건 증가”로 오해할 수 있는 표현을 원본에 맞게 “CRC 오류 카운터가 154까지 증가”로 수정했습니다.
- Excel에서 한글 CSV가 깨지는 문제를 확인하고 UTF-8 BOM 인코딩을 적용한 뒤 행과 열을 다시 검증했습니다.
- 실제 계정정보, 고객정보, 장비정보, Ticket 또는 AWS 내부정보를 사용하지 않았습니다.

## 배운 점

- AI가 결과를 빠르게 생성하더라도 원본 자료와 비교하는 검증이 필요합니다.
- 로그 분석에서는 확인된 사실, 가능한 추정과 미확인 정보를 분리해야 합니다.
- 장애가 복구되었다는 사실만으로 정확한 Root Cause가 확인된 것은 아닙니다.
- Severity는 사건의 심각도이고 Priority는 무엇을 먼저 확인할 것인지 정한 순서입니다.
- Ticket 우선순위는 서비스 영향, 반복·지속, 영향 범위, 복구 여부와 현재 상태를 함께 고려해야 합니다.
- Incident Report는 사건의 흐름과 조치 결과를 다른 사람이 이해할 수 있게 정리해야 합니다.
- Handover Memo에는 진행 중인 상황, 부족한 정보와 다음 확인 사항이 포함되어야 합니다.
- 코드와 문서뿐 아니라 AI를 사용한 목적과 직접 검증·수정한 내용도 기록해야 합니다.

## 저장소 구조

```text
AWS-DCO-GenAI-Portfolio/
├─ 01_dco_glossary/              # DCO 인프라 용어
├─ 02_dco_profile/               # 협업 유형 리포트
├─ 06_cli_file_automation/       # 교육용 Ticket·체크리스트
├─ 07_log_analysis_script2/      # 다중 서버 로그 분석
├─ 09_log_analysis_script/       # Python 로그 분석과 요약
├─ 10_incident_analysis/         # CRC Error·Link Down 사건 분석
├─ 11_incident_report/           # 교육용 Incident Report
└─ 12_ticket_triage_handover/    # Ticket 우선순위와 Handover
```

## 프로젝트 범위와 제한

이 저장소는 DCO 인턴십 직무를 이해하기 위한 학습형 포트폴리오입니다.

- 실제 AWS DCO 업무 수행 능력을 증명하는 자료가 아닙니다.
- 실제 데이터센터 근무 또는 장비 운영 경험을 나타내지 않습니다.
- 실제 데이터센터 운영 절차나 내부 SOP를 포함하지 않습니다.
- 실제 장애 대응, 장비 교체 또는 운영 자동화를 수행하지 않았습니다.
- 공개 직무 맥락과 교육용 샘플 데이터를 이용한 학습 결과만 포함합니다.
