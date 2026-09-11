# OpenAI API 티어별 사용 제한 및 Free(Tier 0) 안내

결제 수단 등록 여부 및 누적 충전 금액에 따른 OpenAI API의 티어 체계, 지원 모델, 속도/사용 제한(Rate Limits) 가이드입니다.

---

### 1. OpenAI API 계정 티어(Tier) 개요

| 티어 (Tier) | 승급 조건 (자격 요건) | 월간 사용 상한 (Usage Cap) | 비고 |
| :--- | :--- | :--- | :--- |
| **Free (Tier 0)** | 허용 국가 내 신규 계정 가입 ($0) | $100 / month | 기본 잔액 $0 (체험 크레딧 미지급) |
| **Tier 1** | 누적 결제액 $5 이상 (선불 충전) | $100 / month | 최신 모델 전체 개방, 제한 대폭 완화 |
| **Tier 2** | 누적 $50 결제 + 첫 결제 후 7일 경과 | $500 / month | - |
| **Tier 3** | 누적 $100 결제 + 첫 결제 후 7일 경과 | $1,000 / month | - |
| **Tier 4** | 누적 $250 결제 + 첫 결제 후 14일 경과 | $5,000 / month | - |
| **Tier 5** | 누적 $1,000 결제 + 첫 결제 후 30일 경과 | $200,000 / month | 최고 자동 승급 등급 |

---

### 2. Free (Tier 0) vs Tier 1 모델별 지원 현황 및 속도 제한 비교

> **주의**: Free(Tier 0)는 계정 잔액이 $0인 상태에서는 API 호출 시 `insufficient_quota` (잔액 부족) 오류가 발생합니다. 바우처/프로모션 크레딧이 등록된 상태이거나 유효 잔액이 있는 경우에 한해 아래 Free 리밋이 적용됩니다.

| 구분 | 모델명 (Model ID) | Free (Tier 0) 지원 여부 | Free 리밋 (RPM / RPD / TPM) | Tier 1 리밋 (최소 $5 충전 시) | 비고 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **경량 모델** | `gpt-4o-mini` | **지원** | 3 RPM / 200 RPD / 40,000 TPM | 500 RPM / 10,000 RPD / 200,000 TPM | 저지연·경량 기본 권장 모델 |
| **추론 모델** | `o3-mini` / `o1-mini` | **미지원** | 호출 불가 (Access Denied) | 500 RPM / 10,000 RPD / 100,000 TPM | 복잡한 코딩·추론 특화 (Tier 1 이상) |
| **플래그십 모델** | `gpt-4o` | **미지원** | 호출 불가 (Access Denied) | 500 RPM / 10,000 RPD / 30,000 TPM | 고성능 멀티모달 플래그십 (Tier 1 이상) |
| **임베딩 모델** | `text-embedding-3-small` | **지원** | 3 RPM / 200 RPD / 40,000 TPM | 500 RPM / 10,000 RPD / 1,000,000 TPM | 시맨틱 검색 및 RAG 파이프라인용 |
| **임베딩 모델** | `text-embedding-3-large` | **지원** | 3 RPM / 200 RPD / 40,000 TPM | 500 RPM / 10,000 RPD / 1,000,000 TPM | 고차원 임베딩 생성용 |
| **레거시 모델** | `gpt-3.5-turbo` | **지원** | 3 RPM / 200 RPD / 40,000 TPM | 500 RPM / 10,000 RPD / 60,000 TPM | 구형 레거시 모델 |
| **음성/오디오** | `whisper-1` / `tts-1` | **미지원** | 호출 불가 | 500 RPM / 10,000 RPD | 음성 인식(STT) 및 합성(TTS) (Tier 1 이상) |

---

### 3. 주요 정책 수정 및 유의사항

1. **신규 가입 무료 크레딧($5) 미지급**
   * 과거 신규 가입자에게 제공되던 $5 상당의 체험 크레딧(3개월 유효) 프로모션은 어뷰징 방지 정책에 따라 **전면 폐지**되었습니다.
   * 현재 신규 생성된 계정의 기본 잔액은 **$0**이며, 별도의 유료 결제(Credit Top-up) 없이는 실제 API 요청이 거부(`429 insufficient_quota`)됩니다.

2. **추론 및 플래그십 모델 접근 권한 제한**
   * `o3-mini`, `o1-mini`, `gpt-4o` 등의 추론형 및 고성능 플래그십 모델은 Free 티어에서 호출할 수 없습니다.
   * 개발 및 테스트를 위해 해당 모델을 사용하려면 최소 **Tier 1** 진입이 필요합니다.

3. **속도 제한 (Rate Limits) 메커니즘**
   * Free 티어 적용 시 분당 요청 수(RPM 3), 일일 요청 수(RPD 200)의 강한 쓰로틀링이 적용되어 병렬 처리 및 반복 테스트 시 `429 Too Many Requests (Rate limit reached)`가 빈번히 발생합니다.
   * API 호출 시 응답 헤더(`x-ratelimit-remaining-requests`, `x-ratelimit-reset-requests`)를 모니터링하고, 지수 백오프(Exponential Backoff with Jitter) 로직 구현이 필수적입니다.

4. **Tier 1 승급 절차 및 권장 설정**
   * **승급 조건**: OpenAI Platform(`platform.openai.com`)의 Billing 설정에서 결제 수단 등록 후 **최소 $5 이상 선불 충전(Credit Top-up)** 시 대기 시간 없이 즉시 승급됩니다.
   * **승급 혜택**: `gpt-4o-mini`, `o3-mini`, `gpt-4o` 등 전체 모델 카탈로그 개방, RPM이 3에서 500으로 대폭 상향되며 실서비스 및 개발 테스트가 원활해집니다.