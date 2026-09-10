# Google AI 모델별 무료 사용 한도 및 주요 용도

> **기준**: 일일 요청 한도(RPD) 기준 내림차순 정렬 및 모델별 핵심 활용 목적 요약

---

## 📌 주요 용어 및 약어 안내

| 약어 / 용어 | 원어 (Full Name) | 쉬운 설명 |
| :--- | :--- | :--- |
| **RPD** | **R**equests **P**er **D**ay | **하루(24시간) 동안 API를 호출할 수 있는 최대 횟수**입니다. |
| **RPM** | **R**equests **P**er **M**inute | **1분 동안 API를 호출할 수 있는 최대 횟수**입니다. |
| **TPM** | **T**okens **P**er **M**inute | **1분 동안 처리 가능한 토큰(글자/단어 단위) 총량**입니다. (질문 입력 + 모델 답변 + 사고 과정 포함) |
| **단위 (K / M)** | Kilo / Million | **K = 1,000 (천)** / **M = 1,000,000 (백만)** <br> *(예: 250K = 25만 토큰, 1M = 100만 토큰)* |
| **Unlimited** | 무제한 | 일일/분당 횟수 제한 없이 자유롭게 호출 가능함을 의미합니다. |

---

## 1. 모델별 Rate Limits 및 주요 용도 (무료 사용량 많은 순)

| 순위 | 모델명 | 카테고리 | RPD (일일 요청 수) | TPM (분당 토큰 수) | RPM (분당 요청 수) | 주요 용도 |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Gemini 2.5 Flash Native Audio Dialog** | Live API | **Unlimited** | 1M (1,000,000) | Unlimited | 실시간 음성 대화 및 양방향 오디오 스트리밍 상호작용 |
| 2 | **Gemini 3 Flash Live** | Live API | **Unlimited** | 65K (65,000) | Unlimited | 실시간 초저지연 멀티모달 상호작용 및 라이브 스트리밍 |
| 3 | **Gemini 3.5 Live Translate** | Live API | **Unlimited** | 20K (20,000) | Unlimited | 실시간 다국어 음성/텍스트 동시 통역 및 번역 |
| 4 | **Gemini 3.5 Transcribe Live** | Live API | **Unlimited** | 20K (20,000) | Unlimited | 실시간 오디오 스트리밍 음성 인식(STT) 및 자막 생성 |
| 5 | **Gemma 4 26B** | Other models | **14.4K (14,400)** | 16K | 30 | 고성능 오픈 가중치 경량 언어 모델 (추론, 텍스트 분석, 온프레미스) |
| 6 | **Gemma 4 31B** | Other models | **14.4K (14,400)** | 16K | 30 | 대규모 오픈 가중치 언어 모델 (복잡한 텍스트 작업 및 코딩 보조) |
| 7 | **Gemini Embedding 1** | Other models | **1,000** | 30K | 100 | 텍스트 임베딩 생성 (RAG 검색 증강, 시맨틱 검색, 문서 분류) |
| 8 | **Gemini Embedding 2** | Other models | **1,000** | 30K | 100 | 고차원 텍스트/멀티모달 임베딩 및 유사도 벡터 검색 |
| 9 | **Gemini 3.1 Flash Lite** | Text-out models | **500** | 250K | 15 | 경량화된 초고속 텍스트 처리 및 대규모 일괄(Batch) 분석 |
| 10 | **Gemini 3.5 Flash Lite** | Text-out models | **500** | 250K | 15 | 최신 경량 고효율 텍스트 생성, 요약 및 일상 대화 |
| 11 | **Antigravity** | Agents | **100** | 100K | 60 | 자율 에이전트 작업 실행, 워크플로우 자동화 및 툴 연동 |
| 12 | **Gemini 3.5 Transcribe** | Live API | **25** | 10K | 3 | 오디오 파일 일괄 음성 인식(STT) 및 스크립트 변환 |
| 13 | **Gemini 2.5 Flash Lite** | Text-out models | **20** | 250K | 10 | 초저비용 고속 텍스트 생성 및 데이터 파싱/분석 |
| 14 | **Gemini 2.5 Flash** | Text-out models | **20** | 250K | 5 | 범용 고속 멀티모달 분석, 요약 및 질의응답 |
| 15 | **Gemini 3 Flash** | Text-out models | **20** | 250K | 5 | 차세대 범용 멀티모달 추론 및 고속 텍스트 생성 |
| 16 | **Gemini 3.5 Flash** | Text-out models | **20** | 250K | 5 | 성능과 속도의 균형을 맞춘 주력 범용 텍스트/멀티모달 작업 |
| 17 | **Gemini 3.6 Flash** | Text-out models | **20** | 250K | 5 | 고도화된 코딩 및 구조적 데이터 처리용 Flash 모델 |
| 18 | **Gemini 3.7 Flash** | Text-out models | **20** | 250K | 5 | 복합 추론 및 하이브리드 사고(Thinking) 처리 지원 모델 |
| 19 | **Gemini 3.8 Flash** | Text-out models | **20** | 250K | 5 | 최신 고성능 범용 Flash 모델 (복합 추론 및 다국어 지원) |
| 20 | **Gemini Robotics ER 2 Preview** | Other models | **20** | 250K | 5 | 로보틱스 제어, 환경 인지(Embodied Reasoning) 및 공간 분석 |
| 21 | **Gemini 2.5 Flash TTS** | Multi-modal | **10** | 10K | 3 | 텍스트-음성 변환 (고품질 음성 합성, TTS) |
| 22 | **Gemini 3.1 Flash TTS** | Multi-modal | **10** | 10K | 3 | 감정 표현 및 자연스러운 음색의 실시간 음성 합성 |
| 23 | **Computer Use Preview** | Other models | **0** | 0 | 0 | 화면 인식 및 마우스/키보드 자동 조작 에이전트 |
| 24 | **Deep Research Pro Preview** | Agents | **0** | 0 | 0 | 다단계 웹 탐색 및 심층 리서치/보고서 작성 에이전트 |
| 25 | **Gemini 2 Flash** | Text-out models | **0** | 0 | 0 | 이전 세대 표준 고속 멀티모달 텍스트 생성 모델 |
| 26 | **Gemini 2 Flash Lite** | Text-out models | **0** | 0 | 0 | 이전 세대 초경량 고속 텍스트 처리 모델 |
| 27 | **Gemini 2.5 Pro** | Text-out models | **0** | 0 | 0 | 고난도 추론, 코딩 및 심층 문서 분석용 고성능 모델 |
| 28 | **Gemini 2.5 Pro TTS** | Multi-modal | **0** | 0 | 0 | 전문 음성 콘텐츠 제작용 스튜디오급 고품질 음성 합성 |
| 29 | **Gemini 3.1 Pro** | Text-out models | **0** | 0 | 0 | 복합 다단계 추론, 수학/코딩 및 논리 분석 플래그십 모델 |
| 30 | **Gemini Omni 1.1 Flash** | Multi-modal | **0** | 0 | 0 | 통합 옴니채널 멀티모달(시각+청각+텍스트) 실시간 처리 |
| 31 | **Gemini Omni Flash** | Multi-modal | **0** | 0 | 0 | 올인원 실시간 멀티모달 입출력 처리 모델 |
| 32 | **Lyria 3 Clip** | Multi-modal | **0** | 0 | 0 | 짧은 오디오 클립 및 배경음악 생성 |
| 33 | **Lyria 3 Pro** | Multi-modal | **0** | 0 | 0 | 전문가용 고품질 음악 작곡 및 오디오 사운드트랙 생성 |
| 34 | **Nano Banana (Gemini 2.5 Flash Preview Image)** | Multi-modal | **0** | 0 | 0 | 이미지 생성 및 시각 자료 합성 프리뷰 |
| 35 | **Nano Banana 2 (Gemini 3.1 Flash Image)** | Multi-modal | **0** | 0 | 0 | 고해상도 이미지 고속 생성 및 스타일 변환 |
| 36 | **Nano Banana 2 Lite (Gemini 3.1 Flash Lite Image)** | Multi-modal | **0** | 0 | 0 | 경량화된 빠른 이미지 생성 및 편집 |
| 37 | **Nano Banana Pro (Gemini 3 Pro Image)** | Multi-modal | **0** | 0 | 0 | 전문가급 고품질 비주얼/이미지 생성 및 세밀 편집 |
| 38 | **Veo 3 Fast Generate** | Multi-modal | **0** | - | 0 | 고속 비디오/동영상 생성 및 클립 렌더링 |
| 39 | **Veo 3 Generate** | Multi-modal | **0** | - | 0 | 고화질 시네마틱 동영상 생성 및 애니메이션 제작 |
| 40 | **Veo 3 Lite Generate** | Multi-modal | **0** | - | 0 | 경량화된 비디오 생성 및 짧은 모션 그래픽 제작 |

---

## 2. 부가 도구 (Grounding Tools) 무료 한도 및 주요 용도

| 구분 | 적용 모델 | 일일 한도 (RPD) | 주요 용도 |
| :--- | :--- | :---: | :--- |
| **Search Grounding** | Gemini 2, Gemini 2.5, Default | **1.5K (1,500)** | 구글 실시간 웹 검색 결과를 답변에 주입하여 최신 정보 제공 및 환각(Hallucination) 방지 |
| **Map Grounding** | Gemini 2 Flash, 2.5 Flash, 2.5 Flash Lite, 3.1 Flash Lite, 3.1 Flash TTS, 3.5 Flash Lite, 3.5 Transcribe, Deep Research Pro Preview, Computer Use Preview, Robotics ER 2 Preview | **500** | 구글 지도 DB를 연동하여 위치, 장소 평점, 영업 시간, 경로 등 지리 정보 검증 및 질의응답 |
| **한도 없음 / 비활성 (0)** | Gemini 3 (Search), Gemini 2.5 Pro, Gemini 3 Flash, Gemini 3.1 Pro, Gemini 3.5 Flash ~ 3.8 Flash (Map) | **0** | 무료 티어 내 해당 그라운딩 도구 미지원 또는 유료 계정 연동 필요 |
