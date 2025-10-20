import streamlit as st
import joblib
import pandas as pd
from pathlib import Path


@st.cache_resource
def load_model(path='./model/regressor.pkl'):
    model_path = Path(path)
    if not model_path.exists():
        return None
    return joblib.load(model_path)


def run_ml():
    st.header('구매 금액 예측기')
    st.write('개인 정보를 입력하면 학습된 모델로 자동차 구매 금액을 예측합니다.')

    with st.form('predict_form'):
        gender = st.selectbox('성별', ['여자', '남자'])
        gender_data = 0 if gender == '여자' else 1

        age = st.number_input('나이', min_value=18, max_value=100, value=30)
        salary = st.number_input('연봉 ($)', min_value=0, value=50000, step=1000)
        debt = st.number_input('카드빚 ($)', min_value=0, value=1000, step=100)
        worth = st.number_input('자산 ($)', min_value=0, value=20000, step=1000)

        submitted = st.form_submit_button('예측하기')

    if submitted:
        model = load_model()
        if model is None:
            st.error('모델이 존재하지 않습니다. 먼저 `model/regressor.pkl` 파일이 있는지 확인하세요.')
            return

        new_data = pd.DataFrame([{
            'Gender': gender_data,
            'Age': age,
            'Annual Salary': salary,
            'Credit Card Debt': debt,
            'Net Worth': worth
        }])

        try:
            y_pred = model.predict(new_data)
        except Exception as e:
            st.error(f'예측 중 오류가 발생했습니다: {e}')
            return

        amount = float(y_pred[0])
        if amount <= 0:
            st.warning('예측된 구매 금액이 유효하지 않습니다.')
        else:
            st.success('예측 완료')
            price = f"${amount:,.0f}"
            st.write(f'예측된 구매 금액: **{price}**')
            st.info('모델 결과는 참고용입니다. 실제 구매 결정 시 더 많은 정보를 고려하세요.')

        



