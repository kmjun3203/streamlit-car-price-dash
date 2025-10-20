import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def load_data(path='./data/Car_Purchasing_Data.csv'):
    return pd.read_csv(path)


def run_eda():
    df = load_data()

    st.header('탐색적 데이터 분석 (EDA)')
    st.write('데이터셋의 기본 구조와 주요 통계, 상관관계를 확인할 수 있습니다.')

    # 상단 KPI 카드
    col1, col2, col3, col4 = st.columns(4)
    col1.metric('행 수', f'{df.shape[0]}')
    col2.metric('열 수', f'{df.shape[1]}')
    col3.metric('평균 구매액', f"${int(df['Car Purchase Amount'].mean()):,}")
    col4.metric('최대 구매액', f"${int(df['Car Purchase Amount'].max()):,}")

    st.markdown('---')

    # 데이터와 기본 통계
    view = st.radio('보기 옵션', ['데이터프레임', '기본 통계'])
    if view == '데이터프레임':
        st.dataframe(df)
    else:
        st.dataframe(df.describe())

    st.markdown('---')

    # 컬럼의 min/max
    st.subheader('컬럼 범위 확인')
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    select_choice = st.selectbox('컬럼을 선택하세요.', numeric_cols)
    st.info(f'{select_choice} 은 {df[select_choice].min():,} 부터 {df[select_choice].max():,} 까지 있습니다.')

    # 상관관계 분석
    st.subheader('상관관계 분석')
    multi_menu = numeric_cols
    choice_list = st.multiselect('컬럼을 2개 이상 선택하세요', multi_menu, default=['Age', 'Annual Salary', 'Car Purchase Amount'])
    if len(choice_list) >= 2:
        corr = df[choice_list].corr()
        st.dataframe(corr.style.background_gradient(cmap='coolwarm'))

        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sns.heatmap(corr, vmax=1, vmin=-1, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f', ax=ax1)
        st.pyplot(fig1)

    st.markdown('---')

    # Pair plot (시간이 걸릴 수 있으니 선택적으로 렌더링)
    st.subheader('Pair Plot (선택적)')
    if st.checkbox('Pair Plot 그리기 (계산 비용이 있을 수 있음)'):
        pair_vars = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
        pair_vars = [v for v in pair_vars if v in df.columns]
        if pair_vars:
            fig2 = sns.pairplot(data=df[pair_vars])
            st.pyplot(fig2)
        else:
            st.warning('Pair plot에 사용할 컬럼이 없습니다.')
