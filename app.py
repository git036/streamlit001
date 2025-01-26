import streamlit as st
import datetime
import pandas as pd
import matplotlib.pylab as plt

st.title('アプリ')
st.caption('テストアプリです')


col1, col2 = st.columns(2)

with col1:

    st.subheader('自己紹介')
    st.text('Pythonに関する情報をYouTubeで')

    code = '''
    import streamlit as st

    st.title('サプーアプリ')

    '''


    st.code(code, language='python')

    with st.form(key='profile_form'):
        name = st.text_input('名前')
        address = st.text_input('住所')

        age_category = st.selectbox('年齢層',('子供(18歳未満)','大人(18歳以上)'))

        gender_category = st.radio('性別',('男','女'))

        hobby = st.multiselect('趣味',('スポーツ','読書','プログラミング','アニメ','釣り','料理'))

        mail_subscribe = st.checkbox('メールマガジン購読')

        height = st.slider('身長',min_value=100, max_value=230)

        start_date = st.date_input('開始日', datetime.date(2025,1,1))

        color = st.color_picker('テーマカラー','#00F900')

        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')

        if submit_btn:
            st.text(f'ようこそ！{name}さん！{address}に送りました')
            st.text(f'年齢層: {age_category}')
            st.text(f'性別: {gender_category}')
            st.text(f'趣味:{",".join(hobby)}')

with col2:
    df = pd.read_csv('data.csv', index_col='月')
    st.dataframe(df)
    st.table(df)
    st.line_chart(df)
    st.bar_chart(df['2021年'])
    fig, ax = plt.subplots()
    ax.plot(df.index, df['2021年'])
    ax.set_title('matplotlib graph')
    st.pyplot(fig)
