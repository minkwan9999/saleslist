# 「온라인 사업 아이디어」 60개 — Hacker News · Indie Hackers 2026 조사

- 조사일: 2026-10-13
- 대상: Google Sheet 「온라인 사업 아이디어」의 재미나이 탭 1–30위, 클로드 탭 1–30위
- 출처: news.ycombinator.com, indiehackers.com (도메인 제한 검색)

## 조사 방법과 한계

- 이 환경에서는 HN API(hn.algolia.com, firebaseio)와 indiehackers.com 직접 접속이 네트워크 정책으로 막혀 있습니다. 그래서 **두 도메인으로 범위를 제한한 웹 검색**으로 조사했습니다. 그 결과 점수(points)와 댓글 수는 확보하지 못했습니다.
- 대부분 한국 특화 아이디어라서 **해외 유사 주제**(예: 카카오 CS 봇 → WhatsApp·이커머스 CS 봇)로 바꿔 검색했습니다. 아이디어 60개를 35개 주제로 묶었습니다.
- **HN 날짜 추정:** HN 글 번호는 시간순으로 늘어납니다. 2026년 10월 채용 글이 49,922,569번이고, 2025년 12월 글이 약 46,26x,xxx번입니다. 따라서 **약 4,645만 번 이후 글을 2026년 글**로 봤습니다. 아래에서 "(2026)"이라고 쓴 HN 글은 이 기준으로 추정한 것입니다.
- IH의 MRR(월 반복 매출)은 대부분 창업자가 **스스로 밝힌 수치**입니다. 실제로 한 글에서 주장한 $2.5K MRR이, Stripe와 연동해 검증하는 TrustMRR에서는 $1,131로 확인됐습니다([IH](https://www.indiehackers.com/post/how-i-built-a-reddit-marketing-tool-to-30k-mrr-in-4-months-with-0-spent-on-marketing-470f39b763)). 수치는 방향을 보는 참고용으로만 보세요.

### 신호 등급

| 등급 | 의미 |
|---|---|
| 🔴 포화 | 2026년 HN·IH에 신규 출시가 많거나 대형 경쟁자가 있음. 한국 현지화 말고는 차별점이 약함 |
| 🟡 신호 있음 | 수요나 유료 결제 사례가 있지만 경쟁이 아직 정리되지 않음 |
| 🟢 공백 | HN·IH에 제품이 거의 없음. 이 커뮤니티가 다루지 않는 시장일 수 있으므로 다른 채널에서 검증해야 함 |
| ⚪ 데이터 없음 | 관련 글을 찾지 못함 |

---

## 핵심 요약

1. **2026년 해외 포화 영역 (7개 군):** AI 계약서 검토, PII 마스킹, 음성 받아쓰기, SNS 예약 게시, GEO/AEO 진단, 문서 → 데이터 추출, AI SDR(콜드메일). 2026년에만 HN Show HN 출시가 각각 여러 건입니다. 한국판으로 들어가려면 경쟁력은 **네이버·카카오·한국 법령·한국 양식 같은 현지화**뿐이라고 봐야 합니다.
2. **커뮤니티 공백 = 클로드 탭의 제조 품질 툴(6–18위):** GRR/MSA, SPC, FMEA, PPAP, 8D, 교정 관리, CSR 관리 모두 HN·IH에 제품이 거의 없습니다. 이것은 "수요가 없다"는 뜻이 아니라 **인디 해커 경쟁자가 적다**는 신호입니다. HN에는 "웹 기반이고 '문의하세요' 가격이 없는 소규모 제조용 소프트웨어가 없다"는 불만 글이 있습니다([HN 43164863](https://news.ycombinator.com/item?id=43164863)). 2026년 IH 비교 글은 산업 현장 SOP 도구 10개 중 "8개는 아무도 안 여는 위키"라고 평가했습니다([IH](https://www.indiehackers.com/post/best-sop-software-2026-i-tested-10-tools-to-document-an-industrial-plant-onboarding-process-8-are-glorified-wikis-nobody-opens-2f4d2c5afb)).
3. **수익화 근거가 있는 쪽:** AI 지원 챗봇(AskAI 약 $40K MRR), 이력서(Rezi $330K+ MRR), SNS 예약(Postiz 약 $120K/월), 숏폼 생성(Autoshorts $31K MRR, 오래된 수치). 모두 포화 시장의 상위 사례입니다.
4. **수익화가 약하다는 근거:** MCP 서버(사용자 7천 명 중 유료 1명), Product Hunt 광고($5,000 지출에 유료 고객 0명), Reddit 페인포인트 분석(Achiv 7개월 만에 $130 MRR), ViralHunt(2026년 8월 $87 MRR).

---

## 재미나이 탭 (1–30위)

| # | 아이디어 | 신호 | HN·IH 2026 근거 |
|---|---|---|---|
| 1 | 로컬 AEO/SEO 최적화 에이전트 | 🔴 | 2026년 GEO 도구 출시가 많음: [Argeo](https://news.ycombinator.com/item?id=47077314), [Potatometer](https://news.ycombinator.com/item?id=47070663), [Ask HN: ChatGPT는 어떤 사이트를 추천하나](https://news.ycombinator.com/item?id=46907123), IH "[Best 15 AEO Tools in 2026](https://www.indiehackers.com/post/best-15-aeo-tools-in-2026-tested-ranked-6c6b9fa2c2)". **소상공인 특화 제품은 찾지 못함**. 네이버 플레이스·AI 브리핑 대응은 해외에 없는 영역 |
| 2 | 카카오톡 CS·구매 유도 에이전트 | 🟡 | [AskAI](https://www.indiehackers.com/post/tech/bootstrapping-to-40k-mrr-after-his-vc-backed-startup-failed-LF1CwRs1vL3oVLcuoIoE) 약 $40K MRR, 이탈률 9%→3%. WhatsApp 봇 [Worvi](https://www.indiehackers.com/post/worvi-whatsapp-ai-bot-launching-on-product-hunt-tomorrow-2cb5e41eeb)는 €89 일회 결제. 해외는 포화이고, 카카오 채널 연동이 차별점 |
| 3 | 세무·지원금 매칭 | ⚪ | 관련 글 없음 |
| 4 | 숏폼 대본·트렌드 툴 | 🔴 | [Autoshorts $31K MRR](https://www.indiehackers.com/post/faceless-short-maker-tool-makes-30k-mrr-33bb0ca91b)(약 2년 전 수치). 교훈: 사람들은 범용 영상 툴이 아니라 "얼굴 안 나오는 틱톡" 같은 **구체적 문제**로 검색함 |
| 5 | 마이크로 인플루언서 매칭·성과 예측 | 🟡 | 도구들이 초기 단계이고 "[디스커버리 도구가 비싸다](https://www.indiehackers.com/post/where-do-you-look-for-micro-influencers-4c586b95eb)"는 불만이 있음. 스크래핑 데이터 유출 사고([HN](https://news.ycombinator.com/item?id=19962790))로 개인정보 리스크 존재 |
| 6 | 계약서 독소조항 감지 | 🔴 | 2026년 Show HN 3건: [AI Contract Reviewer](https://news.ycombinator.com/item?id=46613943), [ContractShield](https://news.ycombinator.com/item?id=46851996), [Lawgmented](https://news.ycombinator.com/item?id=46946237). IH에는 [ClearSign](https://www.indiehackers.com/post/launched-clearsign-today-ai-contract-review-for-freelancers-691a635e95), [$39 리뷰어](https://www.indiehackers.com/post/i-built-a-39-ai-contract-reviewer-so-freelancers-stop-signing-bad-client-contracts-4128d0188f) 등. 자체 측정 정확도 75–85%이고, "깨끗하다고 했는데 놓친 조항" 때문에 생기는 **잘못된 안심**이 핵심 리스크 |
| 7 | 오피스 상권 점심 메뉴 수집 봇 | ⚪ | 약 10년 전 [Ask HN 점심 앱](https://news.ycombinator.com/item?id=9616275)뿐. 유사 사례로 투표 앱 [Simple Poll](https://www.indiehackers.com/post/how-wilhelm-klopp-built-simple-poll-one-of-the-most-popular-slack-apps-876c0ebcd9)이 60만 워크스페이스에 설치됨 |
| 8 | 와디즈·텀블벅 경쟁 분석 | ⚪ | [BackerTracker](https://news.ycombinator.com/item?id=11422598), Kicktraq 같은 오래된 사례만 있고 2026년 글 없음 |
| 9 | 팝업스토어 방명록·리뷰 분석 | 🟡 | [Wyapy](https://news.ycombinator.com/item?id=45645685)(2025): QR 피드백 수집 후 AI 요약, 지역 식당·소매점 대상. [qrfeedback.app](https://news.ycombinator.com/item?id=42392614) |
| 10 | GitHub 기반 이력서 윤문 | 🔴 | [Rezi $330K+ MRR](https://www.indiehackers.com/ideas), [JadeAI](https://news.ycombinator.com/item?id=47145873)(2026, 오픈소스), [Devfol.io](https://news.ycombinator.com/item?id=43491840) |
| 11 | 체험단 모집·검증 | 🟡 | 5번과 같은 시장. 허위 팔로워 탐지 신호(팔로워 급증, 좋아요/팔로워 비율)는 [HN 스레드](https://news.ycombinator.com/item?id=15457074) 참고 |
| 12 | 사내 위키 기반 온보딩 챗봇 | 🔴 | [DanswerBot](https://news.ycombinator.com/item?id=37677473)(현 Onyx, 오픈소스), [Genie](https://news.ycombinator.com/item?id=43946346), 2026년 [Channels SDK](https://news.ycombinator.com/item?id=49198583)(Slack·Teams 에이전트) |
| 13 | 상표 등록 가능성 분석 | ⚪ | 관련 글 없음(검색 결과가 모두 AI 검색 가시성 도구였음) |
| 14 | 한국형 B2B 리드 발굴·콜드메일 | 🔴 | 2026년 [FounderSDR](https://news.ycombinator.com/item?id=47112610)(월 $299~), AiSDR 월 $900, [Leaddrop](https://www.indiehackers.com/product/leaddrop-lead-generation)(2026년 3월 출시, 월 $49). IH 리뷰: "[완전 자동 AI 방식은 이미 소진 중](https://www.indiehackers.com/post/best-ai-sdr-for-b2b-saas-in-2026-i-reviewed-8-of-them-the-pure-ai-approach-is-already-burning-out-68aae34afb)" |
| 15 | 보도자료 작성·기자 배포 | 🔴 | IH의 2026년 보도자료 관련 글은 대부분 배포 대행 광고성 글. "보도자료는 죽었고 개인화 피칭이 낫다"는 주장도 있음. [Press Hunt](https://www.indiehackers.com/product/press-hunt/revenue)(기자 50만 명 DB) |
| 16 | 학원 학부모 알림·수납 봇 | ⚪ | SaaS 사례 없음. 2026년 HN 맥락: [튜터링 회사가 "AI 쓰라"며 폐업](https://news.ycombinator.com/item?id=49831690), [Khanmigo 2년 실험](https://news.ycombinator.com/item?id=49972419) → 사교육 가격 압박 |
| 17 | 전월세 등기부등본 분석 | ⚪ | 임대차 특화 글 없음 |
| 18 | 주류 재고·발주 예측 | 🟡 | 2026년 [Open Source Barware](https://news.ycombinator.com/item?id=48837809)(무료, GPLv3), [Kitted](https://news.ycombinator.com/item?id=47744611)(바코드 재고). 무료 오픈소스가 생겨 가격 압박 있음. 발주 예측 기능을 가진 인디 제품은 없음 |
| 19 | 팟캐스트 → 블로그 변환 | 🔴 | [Podsqueeze $6.5K MRR](https://www.indiehackers.com/post/reaching-6-5k-mrr-with-saas-for-podcasts-in-2-months-47fb4410ad)(출시 2개월, 오래된 수치), RepostAI(2026년 3월) |
| 20 | 중고거래 크로스리스팅·시세 | 🔴(해외) | Vendoo, List Perfectly, PrimeLister, Flyp 등 [포화](https://www.indiehackers.com/post/5-cross-listing-tools-for-scaling-a-reselling-side-hustle-8HlM2W0byVnrV1NaEYzy). 단, 당근·번개장터는 해외 도구가 지원하지 않음 |
| 21 | 프리랜서 단가 산정·견적서 | 🟡 | [Syntaks](https://news.ycombinator.com/item?id=46540811)(2025년 말, 업워크 제안서), 무료 계산기 다수. IH: 실제 시급을 계산해 보니 €8였다는 글이 공감을 얻음 |
| 22 | 회식 투표·정산 봇 | ⚪ | 2026년 관련 글 없음 |
| 23 | 자영업 커뮤니티 민심 분석 | 🟡 | Reddit 페인포인트 분석: [Achiv](https://www.indiehackers.com/product/achiv) 월 $29, 7개월 만에 $130 MRR. Reddit 마케팅 도구는 [$30K MRR 주장](https://www.indiehackers.com/post/how-i-built-a-reddit-marketing-tool-to-30k-mrr-in-4-months-with-0-spent-on-marketing-470f39b763). **"분석"보다 "마케팅·리드" 쪽이 돈이 됨** |
| 24 | K팝 팝업·생일카페 캘린더 | 🟢 | K팝 특화 글 없음. 유사 사례로 [보유 음악 기반 페스티벌 추천](https://news.ycombinator.com/item?id=46934190)(2026) |
| 25 | 무인 스터디카페 문의 봇 | 🟡 | 2번과 같음. 음성 접수 대행 모델은 고객당 [$300–800 MRR](https://www.indiehackers.com/post/building-a-profitable-ai-voice-saas-agency-300-800-mrr-per-client-frAbgO1yQMfHOFFtY3gE) |
| 26 | 공모주 일정·배정 알림 | ⚪ | 서비스 사례 없음(2026 OpenAI·Anthropic IPO 뉴스 토론만) |
| 27 | 아파트 실거래가 저평가 진단 | ⚪ | 2026년 사례 없음. 과거 [Lofty AI](https://news.ycombinator.com/item?id=20697449). Zestimate 오차 논란 → 추정 정확도가 핵심 리스크 |
| 28 | 크리에이터 협찬 메일 분류 | 🟢 | 크리에이터 특화 인박스 도구 없음. 범용 SaneBox, [MailSense](https://news.ycombinator.com/item?id=41905716). 스폰서를 찾아주는 [Sponsorstream](https://news.ycombinator.com/item?id=40130085)은 반대 방향 |
| 29 | 반려동물 유치원 알림장 생성 | ⚪ | 데이케어용 글 없음(소비자용 AI 펫 사진 앱만 있음) |
| 30 | 공모전 팀원 매칭 | 🟡(약) | [HackBud](https://news.ycombinator.com/item?id=41900501)는 사용자 수 부풀리기 지적을 받음. 2026년 [HackathonHub](https://news.ycombinator.com/item?id=48373023). 매칭은 보통 행사 자체 기능으로 해결됨 |

## 클로드 탭 (1–30위)

| # | 아이디어 | 신호 | HN·IH 2026 근거 |
|---|---|---|---|
| 1 | 거래명세서·발주서 → 엑셀/ERP | 🔴(범용) | 2026년 [Pdfpull](https://news.ycombinator.com/item?id=46718771)(규칙 기반, 무료 티어), [ParsePoint](https://news.ycombinator.com/item?id=44480818)(2025), [재무 PDF 추출](https://news.ycombinator.com/item?id=44445222). 시트 분석과 같은 결론: **범용은 포화, 이카운트·더존 양식 수직 특화만 여지 있음** |
| 2 | 스마트스토어·카카오 문의 답변 초안 | 🟡 | 재미나이 2번과 같음 |
| 3 | 한국형 GEO 진단 | 🔴 | 재미나이 1번과 같음. 무료 진단기(GEOScore, Potatometer)가 많아 **진단만으로는 과금이 어려움** |
| 4 | 한국어 상품 홍보 영상 음성 | ⚪ | TTS 발음 특화 사례 없음. 경쟁사 가격: Retell·Vapi·ElevenLabs 분당 $0.10–0.30. AI 보이스오버 데스크톱 앱 [$3K MRR](https://www.indiehackers.com/post/i-got-tired-of-opening-15-ai-websites-every-time-i-made-a-youtube-video-so-i-built-one-desktop-app-instead-RLiDX8cq3wSjA8eV0KsN) |
| 5 | 한국어 음성 입력 | 🔴🔴 | 2026년 가장 포화된 영역: [BetterWispr](https://news.ycombinator.com/item?id=50042333)(2026년 10월), [FreeFlow](https://news.ycombinator.com/item?id=47411467), [Voquill](https://news.ycombinator.com/item?id=47236677), [SpeechOS](https://news.ycombinator.com/item?id=46707409), [로컬 iOS 앱](https://news.ycombinator.com/item?id=47088339), [Wispr Flow 대안 질문](https://news.ycombinator.com/item?id=49809670). 대부분 **무료 오픈소스**. 시트의 "난이도 높음" 판단을 뒷받침함 |
| 6 | MSA 확장(GRR·편의·선형성) 계산기 | 🟢 | HN·IH에 관련 제품 없음 |
| 7 | 검사성적서 자동 생성 + Cpk | 🟢 | 관련 제품 없음 |
| 8 | 품질 5대 툴 입문 전자책·강의 | ⚪ | 관련 글 없음(콘텐츠 상품이라 이 커뮤니티 범위 밖) |
| 9 | 관리계획서·FMEA 초안 | 🟢 | 관련 제품 없음. HN의 의료기기 맥락: FMEA는 설계가 있어야 평가할 수 있음 |
| 10 | 8D 보고서 도우미 | 🟢 | 관련 제품 없음 |
| 11 | PPAP 누락 점검 | 🟢 | 관련 제품 없음 |
| 12 | 측정기 교정·만료 알림 | 🟢 | 관련 제품 없음 |
| 13 | SPC 관리도 판정 | 🟢 | 관련 제품 없음 |
| 14 | 고객사 요구서류(CSR) 트래커 | 🟢 | 관련 제품 없음 |
| 15 | 작업표준서(SOP) 생성기 | 🟡 | 2026년 IH 비교: [10개 중 8개는 위키에 불과](https://www.indiehackers.com/post/best-sop-software-2026-i-tested-10-tools-to-document-an-industrial-plant-onboarding-process-8-are-glorified-wikis-nobody-opens-2f4d2c5afb). 1위 Clypp(영상 기반), Scribe(화면 녹화). 현장 작업자용 SOP는 비어 있음 |
| 16 | 부품 견적 원가 산출 | 🟡 | 2025년 12월 HN "[What are you working on](https://news.ycombinator.com/item?id=46264491)"에 판금 공장용 CAD → 즉시 견적 SaaS 등장. 경쟁: OSH Cut, Protolabs. 배경 글: [The Factory's Quote is the Product](https://news.ycombinator.com/item?id=44561652) |
| 17 | Product Hunt 한국어 큐레이션 뉴스레터 | 🟡(약) | [Tiny Startups](https://news.ycombinator.com/item?id=44162008)(구독자 약 2만, 유료 노출로 월 $5.6K). [PH 광고 $5,000 → 유료 고객 0명](https://www.indiehackers.com/post/we-spent-5000-on-a-product-hunt-ad-here-are-the-numbers-5d7a663cc5). 시트의 "수익화 어려움" 판단과 일치 |
| 18 | 도면 풍선·검사항목표 자동화 | 🟢 | 완성된 엔드투엔드 인디 제품 없음. 인접 사례로 건설 도면 AI [InspectMind (YC W24)](https://news.ycombinator.com/item?id=46219386). IH에 [9년 전 같은 아이디어 글](https://www.indiehackers.com/post/how-to-make-a-engineering-drawing-inspection-ballooning-application-6adbfaf049) 있음 |
| 19 | 스마트스토어·쿠팡 정산 대조 | 🟡 | IH [Shopify 정산 대조 도구 검증 글](https://www.indiehackers.com/post/validating-a-shopify-payout-reconciliation-tool-honest-feedback-wanted-not-promoting-40556ee64d): A2X·Synder는 회계사용이고 월 $70+. 창업자는 $9 사전판매로 검증 중. **"회계사 아닌 셀러용 저가판"이라는 틈은 해외에도 있음** |
| 20 | 공공데이터·법령 MCP 서버 | 🟡(약) | [MCP 구독 출시](https://www.indiehackers.com/post/shipped-the-mcp-subscription-last-week-first-paying-customer-the-same-day-tp5xj8lRNnSGEO1sMuH2): 사용자 약 7천 명 중 월 $9 유료 1명. "MCP는 쉽게 복제되니 API에 과금하라"([HN](https://news.ycombinator.com/item?id=44016336)). 시트의 "수익 약함" 판단과 일치 |
| 21 | 불량 사진 → 부적합 보고서 | 🟢 | 관련 제품 없음 |
| 22 | 중대재해·산안 자가점검 | 🟡 | IH: [석유·가스 안전감사 도구, 주 경쟁자는 엑셀](https://www.indiehackers.com/post/i-built-a-simple-safety-audit-tool-for-oil-gas-contractors-then-realized-my-main-competitor-is-excel-KhuDWyAtE6bStqAHISRb). 대형 경쟁사는 SafetyCulture(좌석당 과금) |
| 23 | 한국어 PII 마스킹 | 🔴 | 2026년 Show HN 다수: [Veil](https://news.ycombinator.com/item?id=47675579), [Privacy Mask](https://news.ycombinator.com/item?id=47362497), [Phi-Redactor](https://news.ycombinator.com/item?id=47170744), [로컬 데이터 비식별화](https://news.ycombinator.com/item?id=48579589). 대부분 오픈소스(시트 판단과 일치). 한국어 개체명 인식은 여지 있음 |
| 24 | 협력사 탄소(PCF) 제출 | ⚪ | 관련 글 없음 |
| 25 | 오픈마켓 주문 → 송장 변환 | ⚪ | 별도 조사 안 함(우선순위 낮음) |
| 26 | 소상공인 계약서·견적서 생성기 | 🟡 | 재미나이 6·21번 참고 |
| 27 | 정부지원사업 매칭 | ⚪ | 재미나이 3번과 같음 |
| 28 | 소상공인 비용 자동분류 | 🟡 | 덴마크 AI 기장 [Northstone ~$2.8K MRR](https://www.indiehackers.com/post/2-8k-mrr-looking-for-a-technical-partner-3e41b660b5)(사람이 최종 승인), 스페인 Aikount |
| 29 | SNS 예약 게시 | 🔴 | [Postiz 약 $120K/월](https://www.indiehackers.com/product/postiz-2/revenue), [PostFast $6.3K MRR](https://www.indiehackers.com/post/tech/carving-out-a-6-3k-mrr-niche-in-a-saturated-market-y1bbTHkoRJmfJzMEmPsT), 2026년 [TryPost](https://news.ycombinator.com/item?id=48271283), [ViralHunt](https://www.indiehackers.com/product/viralhunt) 2026년 8월 $87 MRR. 시트의 "경쟁 과다" 판단과 일치 |
| 30 | 종합소득세 증빙 분류 | 🟡 | 28번과 같음(세무사법 리스크는 한국 고유) |

---

## 시트 판단과 비교

- **커뮤니티 데이터가 시트 판단을 뒷받침한 것:** 클로드 5위 음성 입력(난이도·경쟁), 17위 PH 뉴스레터(수익화 어려움), 20위 MCP(수익 약함), 23위 PII(오픈소스 존재), 29위 SNS 예약(경쟁 과다), 1위 문서 변환(범용은 포화).
- **시트보다 경쟁이 심한 것:** 재미나이 6위 계약서 검토(2026년 Show HN만 3건), 14위 리드 발굴, 10위 이력서, 12위 사내 챗봇.
- **커뮤니티 공백 → 다른 채널에서 검증 필요:** 클로드 6–14·18·21위(제조 품질). HN·IH에는 근거가 없으므로 **국내 품질 실무자 카페·LinkedIn·IATF 관련 커뮤니티**에서 수요를 확인해야 합니다.

## 다음 단계 제안

1. 제조 품질 군(🟢)은 해외 B2B 리뷰 사이트(G2, Capterra)와 국내 실무자 커뮤니티로 2차 검증합니다.
2. 🔴 영역 중 계속 검토할 아이디어는 "한국 현지화가 경쟁력이 되는가"(네이버·카카오 API 접근성, 한국 법령·양식)만 따로 확인합니다.
3. HN 점수·댓글 수가 필요하면, hn.algolia.com과 indiehackers.com 접속이 허용된 환경에서 HN Algolia API로 다시 수집합니다.
