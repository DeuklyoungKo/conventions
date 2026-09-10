# xAI (Grok) 모델별 스펙, Rate Limits 및 주요 용도 요약

> **기준**: xAI 공식 문서([docs.x.ai](https://docs.x.ai)) 기준 모델 라인업, 티어별 호출 한도(Rate Limits), 주요 용도 및 그라운딩 도구 요약

---

## 1. 모델별 상세 스펙 및 주요 용도

| 순위 | 모델명 (API Identifier) | 카테고리 | 컨텍스트 윈도우 | Tier 0 RPS | Tier 0 TPM | 주요 용도 및 특징 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | **Grok 4.6** (`grok-4.6`) | Flagship (주력) | 최대 1M | 3 | 10M | xAI 최고 지능의 최신 플래그십 모델. 복합 추론, 심층 코딩, 대규모 문서 분석 및 범용 멀티모달 대화 |
| 2 | **Grok 4.5** (`grok-4.5`) | Flagship | 128K ~ 500K | 3 | 10M | 고성능 텍스트 추론, 아키텍처 설계 및 프로그래밍 작업 전반 |
| 3 | **Grok 4.20 Reasoning** (`grok-4.20-reasoning`) | Reasoning (추론) | 128K | 3 | 10M | 명시적 사고(Thinking) 프로세스를 수행하는 고난도 수학, 알고리즘, 시스템 설계 전용 모델 |
| 4 | **Grok 4.20 Non-Reasoning** (`grok-4.20-non-reasoning`) | General | 128K | 3 | 10M | 빠른 응답 속도와 엄격한 지시 준수(Instruction Following), 정형 데이터(JSON) 추출 최적화 |
| 5 | **Grok Build 0.1** (`grok-build-0.1`) | Coding Agent | 128K | 3 | 10M | 자율 에이전트 코딩 세션 및 리포지토리 파일 수정/빌드/리팩토링 특화 모델 |
| 6 | **Grok 4.1 Fast** (`grok-4.1-fast`) | Fast / Routing | 128K | 5+ | 10M | 초저지연·고처리량 지원 챗봇, 실시간 데이터 라우팅 및 1차 응답 분류 모델 |
| 7 | **Grok 4.3** (`grok-4.3`) | Real-time Search | 128K | 3 | 10M | 실시간 X(구 Twitter) 데이터 검색 및 소셜 트렌드 분석 연계에 최적화된 모델 |
| 8 | **Grok 3** (`grok-3`) | General | 131K (131,072) | 3 | 10M | 범용 고성능 3세대 언어 모델. 벤치마크 기반 논리 분석 및 일반 업무 처리 |
| 9 | **Grok 3 Mini** (`grok-3-mini`) | Lightweight / Fast | 131K (131,072) | 5+ | 10M | 초저비용·고효율 경량 모델. 빠른 추론, 단순 코딩 질의, 대용량 배치 처리 |
| 10 | **Grok Imagine Image 2.0** (`grok-imagine-image`) | Multi-modal (Image) | - | 1~2 | - | 고해상도 비주얼 이미지 생성, 스타일 변환 및 디자인 에셋 합성 |
| 11 | **Grok Imagine Video 1.5** (`grok-imagine-video`) | Multi-modal (Video) | - | 1 | - | 짧은 애니메이션 영상 및 고품질 모션 비디오 클립 생성 |
| 12 | **Grok Voice API** (`grok-voice`) | Multi-modal (Audio) | - | 실시간 스트림 | - | 초저지연 양방향 음성 대화 및 자연스러운 음성 합성(TTS/STT) |
| 13 | **Grok-2** (`grok-2-1212`) | Legacy / Stable | 131K (131,072) | 3 | 10M | 2세대 범용 언어 모델 (이전 안정화 버전 유지보수용) |
| 14 | **Grok-2 Vision** (`grok-2-vision-1212`) | Legacy / Vision | 131K (131,072) | 3 | 10M | 2세대 시각 모델. 이미지 질의응답, 문서 OCR 및 시각 데이터 해석 |

---

## 2. xAI Rate Limit 티어 구조 (누적 결제액 기준)

xAI는 분당/초당 요청 한도를 누적 사용 금액(Cumulative Spend)에 따라 영구적으로 상향하는 티어 시스템을 사용합니다.

| 티어 (Tier) | 누적 결제 조건 | 기본 RPS (초당 요청 수) | 기본 TPM (분당 토큰 수) | 대상 및 특징 |
| :---: | :---: | :---: | :---: | :--- |
| **Tier 0** | **$0 (기본)** | **3 RPS** | **10M TPM** | 계정 생성 기본 티어. 무료 크레딧 사용 및 초기 개발/테스트에 적합 |
| **Tier 1** | $50 이상 | 10 RPS | 20M TPM | 초기 서비스 출시 및 소규모 상용 트래픽 처리 |
| **Tier 2** | $250 이상 | 25 RPS | 50M TPM | 중소규모 프로덕션 서비스 |
| **Tier 3** | $1,000 이상 | 50 RPS | 100M TPM | 대규모 트래픽 및 엔터프라이즈 워크플로우 |
| **Tier 4** | $5,000 이상 | 100+ RPS | 200M+ TPM | 대규모 동시 요청 및 배치 처리 |
| **Enterprise** | 별도 협의 | 맞춤 한도 설정 | 맞춤 한도 설정 | 전용 인프라 및 SLA 보장 |

> 📌 **참고**:
> - TPM 한도에는 **프롬프트 입력 토큰(텍스트/이미지/오디오), 생성 출력 토큰, 추론 모델의 Reasoning 토큰, 캐시된 토큰**이 모두 포함됩니다.
> - 한도 초과 시 `HTTP 429 Too Many Requests`가 발생하므로 지수 백오프(Exponential Backoff) 구현이 권장됩니다.

---

## 3. 부가 도구 (Grounding Tools & Extensions)

| 도구명 (Tool) | 지원 모델 | 과금 방식 / 한도 | 주요 기능 및 용도 |
| :--- | :--- | :---: | :--- |
| **X Search (소셜 그라운딩)** | Grok 4.x, Grok 3 계열 | 호출 건당 과금 | 실시간 X(Twitter) 포스트, 트렌드, 최신 이슈 검색 및 여론/반응 분석 |
| **Web Search Grounding** | 전 모델 지원 | 호출 건당 과금 | 실시간 구글/웹 검색 결과를 프롬프트에 자동 주입하여 최신 정보 제공 및 환각 방지 |
| **Code Execution (코드 인터프리터)** | Grok 4.x, Grok Build, Grok 3 | 기본 기능 포함 | 격리된 샌드박스 환경에서 파이썬 코드를 실행하여 수학 계산, 데이터 분석 및 코드 검증 |
| **Collections (RAG 문서 검색)** | Grok 전 모델 | 벡터 DB/문서 기반 | 개발자가 업로드한 커스텀 문서 집합에 대해 시맨틱 검색 수행 후 답변 생성 |

---

## 4. 과금 체계 및 무료 크레딧 안내

- **무료 크레딧**: xAI 콘솔([console.x.ai](https://console.x.ai)) 신규 등록 및 베타 참여 시 월간 $25 상당의 무료 API 크레딧 제공
- **입출력 토큰 과금 (예시 기준)**:
  - **Grok 4.6**: 입력 $2.00 / 1M 토큰, 출력 $6.00 / 1M 토큰 (캐시 입력: $0.50 / 1M 토큰)
  - **Grok 3**: 입력 $3.00 / 1M 토큰, 출력 $15.00 / 1M 토큰
  - **Grok 3 Mini**: 입력 $0.30 / 1M 토큰, 출력 $0.50 / 1M 토큰
  - **Batch API**: 비동기 배치 요청 시 50% 할인 혜택 적용
