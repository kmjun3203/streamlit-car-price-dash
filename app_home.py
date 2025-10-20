import streamlit as st


def run_home():
        # Hero 영역
        st.markdown("""
        <div style='display:flex; align-items:center; gap:20px'>
            <div style='flex:1'>
                <h2 style='margin:0'>자동차 구매 금액 예측 & 데이터 분석</h2>
                <p style='color: #6c757d; margin-top:6px'>
                    이 앱은 자동차 구매 데이터의 탐색적 분석(EDA)과 머신러닝 기반 구매 금액 예측을 제공합니다.
                </p>
            </div>
            <div style='width:260px'>
                <img src='./image/car3.jpg' style='width:100%; border-radius:8px' />
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('---')

        # 핵심 기능 카드
        cols = st.columns(3)
        cols[0].metric('데이터 건수', '1000+', delta=None)
        cols[1].metric('모델', '선형회귀', delta=None)
        cols[2].metric('목표', 'Car Purchase Amount', delta=None)

        st.write('### 사용된 데이터')
        st.info('데이터는 공개 데이터셋 Car_Purchasing_Data.csv를 사용하였으며, 연령, 연봉, 카드빚, 자산 등의 피처를 포함합니다.')

        with st.expander('데이터셋, 전처리 및 모델 요약 보기'):
                st.markdown('- 피처: Gender, Age, Annual Salary, Credit Card Debt, Net Worth')
                st.markdown('- 모델: 학습된 회귀모델을 사용하여 구매 금액을 예측')
                st.markdown('- 사용법: 사이드바에서 EDA 또는 ML을 선택해보세요')

