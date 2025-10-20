# streamlit-50-startups

## 프로젝트 소개
스타트업의 재무 데이터를 기반으로 수익(Profit)을 예측하는 Streamlit 앱입니다. 데이터 탐색(EDA), 머신러닝 예측, 시각화 기능을 제공합니다.

## 주요 기능
- **Home**: 앱 소개, 데이터 샘플 미리보기, 데이터 다운로드
- **EDA**: 데이터 요약, 결측치/자료형, 상관관계 히트맵, 산점도, 박스플롯, 페어플롯 등 다양한 탐색적 분석
- **ML**: 머신러닝 모델을 통한 수익 예측 (예: 선형회귀)

## 폴더/파일 구조
- `app.py` : 메인 앱 진입점 (Streamlit)
- `app_home.py` : 홈 화면 구성
- `app_eda.py` : EDA(탐색적 데이터 분석) 화면
- `app_ml.py` : 머신러닝 예측 화면
- `data/50_Startups.csv` : 분석/예측에 사용되는 원본 데이터
- `requirements.txt` : 필요 패키지 목록

## 데이터 설명
`data/50_Startups.csv`에는 R&D, 관리비, 마케팅비, 지역(State), 수익(Profit) 정보가 포함되어 있습니다.

## 실행 방법
1. 필수 패키지 설치
	```bash
	pip install -r requirements.txt
	```
2. 앱 실행
	```bash
	streamlit run app.py
	```
3. 웹 브라우저에서 안내된 주소로 접속

## 필요 패키지
`requirements.txt` 참고 (주요 패키지: streamlit, pandas, numpy, matplotlib, seaborn, scikit-learn, koreanize-matplotlib 등)

## 참고
- EDA/ML 기능은 각 탭에서 확인 가능
- 데이터 파일 경로/구조가 변경되면 코드 내 경로도 함께 수정 필요
