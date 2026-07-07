# [교육용 샘플 데이터 사용]

## EDU-TICKET-SAMPLE-001

* **티켓 ID**: EDU-TICKET-SAMPLE-001
* **발생 시간**: 2026-07-07T15:00:00+09:00 (SAMPLE_TIME)
* **샘플 장비명**: SAMPLE_TOR_SW_01
* **이벤트**: CRC Error Increase followed by Link Down Event
* **심각도**: SAMPLE_SEV_2 (Medium-High)
* **관찰 내용**: 
  - SAMPLE_TOR_SW_01 장비의 Interface Ethernet1/1에서 CRC 에러 카운트가 지속적으로 증가하는 현상이 감지되었습니다.
  - CRC 에러 누적 이후 해당 인터페이스가 Link Down 상태로 천이되었습니다.
  - SAMPLE_LOG_LINE_01: `Jul  7 15:00:05 SAMPLE_TOR_SW_01 %ETHPORT-5-IF_DOWN_LINK_FAILURE: Interface Ethernet1/1 is down (Link failure)`
* **Escalation 필요 여부**: 필요 (샘플 기준에 따라 추가 분석을 위해 L2 엔지니어 또는 벤더 기술 지원팀으로의 SAMPLE_ESCALATION 검토 요망)
* **보안 주의사항**:
  - 본 티켓은 교육용 샘플 데이터이므로 실제 IP 주소, 장비 시리얼 번호, 실제 자산 정보 등을 포함해서는 안 됩니다.
  - 모든 장비명 및 식별자에는 `SAMPLE_` 또는 `EDU_` 접두어만을 사용하십시오.
