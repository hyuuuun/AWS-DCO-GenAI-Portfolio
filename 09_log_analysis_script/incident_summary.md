# 📋 교육용 DCO 로그 분석 보고서 (Incident Summary)

- **분석 시각**: 2026-07-19
- **대상 로그 파일**: `sample_dco_log.txt`
- **총 로그 수**: 140 줄

## 1. 심각도별(Severity) 발생 현황
| 심각도 (Severity) | 빈도수 (Counts) | 비율 |
| --- | --- | --- |
| INFO | 135 | 96.4% |
| WARNING | 3 | 2.1% |
| ERROR | 2 | 1.4% |

## 2. 이벤트별(Event) 발생 현황
| 이벤트명 (Event) | 빈도수 (Counts) |
| --- | --- |
| Normal heartbeat | 125 |
| Ticket opened | 3 |
| Ticket escalated | 3 |
| Maintenance completed | 3 |
| Fan Alert | 1 |
| Temperature warning | 1 |
| SSD failure warning | 1 |
| CRC error 증가 | 1 |
| Link Down | 1 |
| Link Up | 1 |

## 3. WARNING 또는 CRITICAL 등급 로그 세부 목록
총 3개의 이슈 로그가 식별되었습니다.

| 시간 | 장비명 | 심각도 | 이벤트 | 상세 메시지 |
| --- | --- | --- | --- | --- |
| 2026-07-03 01:05:00 | `DEMO_CORE_SW_02` | **WARNING** | Fan Alert | Fan module 2 RPM dropped to 15% (Below threshold 20%). IP: 198.51.100.2 |
| 2026-07-03 02:05:00 | `EDU_SRV_R04_N12` | **WARNING** | Temperature warning | Chassis temperature reached 42C (Threshold: 40C). IP: 192.0.2.12 |
| 2026-07-03 03:05:00 | `SAMPLE_TOR_SW_01` | **WARNING** | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |

## 4. 장애 및 에스컬레이션 주요 이벤트 요약
DCO 인턴십 직무 이해를 위한 핵심 키워드(CRC_ERROR, LINK_DOWN, TICKET_ESCALATED) 기반 수집 결과입니다.

| 시간 | 구분 | 장비명 | 이벤트명 | 세부 메시지 |
| --- | --- | --- | --- | --- |
| 2026-07-03 01:10:00 | `TICKET_ESCALATED` | `DEMO_CORE_SW_02` | Ticket escalated | Ticket EDU-TKT-2026-0001 escalated to Local Infrastructure Team. |
| 2026-07-03 02:15:00 | `TICKET_ESCALATED` | `EDU_SRV_R04_N12` | Ticket escalated | Ticket EDU-TKT-2026-0002 escalated to DCO Hardware Support. |
| 2026-07-03 03:05:00 | `CRC_ERROR` | `SAMPLE_TOR_SW_01` | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |
| 2026-07-03 03:06:00 | `LINK_DOWN` | `SAMPLE_TOR_SW_01` | Link Down | Interface Gi0/1 status changed to DOWN. Connection to server lost. |
| 2026-07-03 03:12:00 | `TICKET_ESCALATED` | `SAMPLE_TOR_SW_01` | Ticket escalated | Ticket EDU-TKT-2026-0003 escalated to Onsite Cabling Team. |
| 2026-07-03 03:30:00 | `CRC_ERROR` | `SAMPLE_TOR_SW_01` | Normal heartbeat | System status is healthy. Interface Gi0/1 running with 0 CRC errors. IP: 192.0.2.1 |

---
*참고: 본 보고서는 학습용 샘플 데이터를 기반으로 가공된 교육 전용 분석 결과입니다. 실제 프로덕션 서버 정보는 담겨있지 않습니다.*
