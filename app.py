import streamlit as st
from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml


def main():
    # 페이지 설정: 타이틀, 아이콘, 와이드 레이아웃
    st.set_page_config(page_title='자동차 구매 금액 예측', page_icon='🚗', layout='wide')

    # 사이드바: 로고 및 메뉴
    with st.sidebar:
        st.image('./image/car3.jpg', use_container_width=True)
        st.title('자동차 가격 대시보드')
        st.write('탐색적 데이터 분석(EDA)과 구매 금액 예측을 제공합니다.')
        st.markdown('---')
        menu = ['Home', 'EDA', 'ML']
        choice = st.radio('메뉴', menu)

    # 메인 컨텐츠 라우팅
    if choice == 'Home':
        run_home()
    elif choice == 'EDA':
        run_eda()
    elif choice == 'ML':
        run_ml()


if __name__ == '__main__':
    main()