import streamlit as st
import pandas as pd

def convert_text_to_hyperlink(row):
    if row['心得'] == '尚未繳交':
        return '<span>尚未繳交</span>'
    else:
        return '<a href="{}">{}</a>'.format(row['心得'],  '查看心得')

def convert_year(dataframe):
    pass

st.set_page_config(page_title="NTU-EXCHANGE-REVIEW", 
page_icon="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/320/apple/285/airplane-departure_1f6eb.png", 
layout="wide", 
initial_sidebar_state="expanded")

st.write("""
        # 國立臺灣大學出國交換
        ## 歷屆心得查詢器""")

st.write("""<a href="https://oia.ntu.edu.tw/students/outgoing.students.experience">資料來源</a>""", 
        unsafe_allow_html=True)

df = pd.read_csv('./data/data_all_review.csv')
df['心得'] = df.apply(convert_text_to_hyperlink, axis=1)

if 'identities_select' not in st.session_state:
    st.session_state['identities_select'] = [False for i in range(3)]
identities = ['暑期', '訪問', '交換']
year_list = list(map(lambda x: str(x) + '年度', list(range(87, 111))))
try:
    st.write("""
            **學生身份別**
            """)
    cols = st.columns(3)
    for i, col in enumerate(cols):
        st.session_state['identities_select'][i] = col.checkbox(identities[i])
    if st.session_state['identities_select'] != [False, False, False]:
        identities_select = st.session_state['identities_select']
        school = st.multiselect('輸入姐妹校名稱', options=list(df['交換學校'].unique()), default="南洋理工大學")
        year = st.multiselect('選擇出國年度', options=year_list, default=year_list[:12:-1])
        review = st.checkbox('僅顯示有繳交心得之結果')
except:
    st.error("""
            ***網頁發生錯誤***
            """)

try:
    if review:
        display_df = df.query('交換學校 == @school and 交換年度.str.contains("|".join(@year)) and 心得 != "<span>尚未繳交</span>"')
    else:
        display_df = df.query('交換學校 == @school and 交換年度.str.contains("|".join(@year))')
    st.write(f"<h3>查詢結果<span style='font-size: 12pt'>（{int(display_df.shape[0])}筆結果）</span></h3>", 
            unsafe_allow_html=True)

    st.write(f"""<div style="overflow:scroll; justify-content: center;">{display_df.to_html(escape=False, index=False)}</div>""", 
            unsafe_allow_html=True)
    st.balloons()

except:
    st.error("""
            **請先選擇身份**
            """)