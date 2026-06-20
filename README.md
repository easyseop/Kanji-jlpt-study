# 일본어 한자 공부 (JLPT N5 · N4 · N3)

JLPT **N5(79) · N4(166) · N3(367) = 612자**를 담은 일본어 한자 학습 웹앱.
빌드 도구 없이 **단일 `index.html` 하나만** 열면 바로 동작합니다.

## 기능
- **목록**: 등급 필터(전체/N5/N4/N3) · `모두/즐겨찾기/미암기` 필터 · 검색(한자·뜻·읽기·영어)
- **상세**: 기본정보(의미/음독/훈독) → 한자 모양 해설(어원) → 음독 상세 → 훈독 상세, 대표단어는 후리가나+한국어. 이전/다음 이동(←/→), 획순(KanjiVG, 온라인 시)
- **카드**: 플래시카드(탭하면 뒤집기, ✓외움/✗모름 → 진도 반영)
- **퀴즈**: 4지선다(뜻/읽기), 필터별 출제
- **학습 진도**: 즐겨찾기·암기 체크를 브라우저(localStorage)에 저장 · 진도바
- **발음 듣기**(TTS, ja-JP) · **다크 모드**
- **PWA**: 홈 화면에 설치 가능 · 오프라인 동작(한 번 본 화면/획순은 캐시되어 인터넷 없어도 열림)

## 바로 보기 / 배포
- 로컬: `index.html` 더블클릭
- GitHub Pages: **Settings → Pages → Source: main / (root)** → `https://<계정>.github.io/<레포>/`

## 데이터 출처 & 라이선스
- 읽기·획수·JLPT 등급·영어 의미: 공개 데이터셋 [davidluzgouveia/kanji-data](https://github.com/davidluzgouveia/kanji-data) (KANJIDIC2/JMdict 기반, EDRDG)
- 한국어 훈음·어원 해설·예시 번역: 직접 작성
- 획순 SVG: [KanjiVG](https://github.com/KanjiVG/kanjivg) (CC BY-SA, 런타임 로드)

## 빌드 (콘텐츠 갱신 시)
데이터를 수정하면 아래로 `index.html`을 재생성합니다.

```bash
python3 build.py   # facts.json + ko.py(훈음) + rich.py(상세) -> index.html
```

- `ko.py` : 612자 한국어 훈음
- `rich.py` : 어원 해설 + 대표단어 상세 (612자 전체 완료)
- `tips.py` : 한자별 암기 꿀팁(연상법)
- `facts.json` : 공개 데이터에서 추출한 읽기/획수/등급/영어뜻
- `template.html` : UI 템플릿(`/*__DATA__*/` 자리에 데이터 주입). PWA용 manifest/아이콘 링크와 서비스워커 등록 포함
- `manifest.webmanifest` / `sw.js` : PWA 설정(설치 정보)·서비스워커(오프라인 캐시). **앱을 고치면 `sw.js`의 `CACHE` 버전을 올려야** 사용자에게 갱신이 반영됨
- `make_icons.py` : PWA 아이콘(`icon-192/512`, `icon-maskable-512`, `apple-touch-icon`) 생성. `pip install Pillow` 후 `python3 make_icons.py`

## 진행 현황
- [x] 612자 기본 정보(음/훈/획수/훈음/영어뜻)
- [x] 학습 기능(즐겨찾기/암기/카드/퀴즈/진도/다크/TTS/획순)
- [x] 한자별 암기 꿀팁(연상법)
- [x] 어원·대표단어 상세: 612 / 612 완료 (N5·N4·N3)

