import streamlit as st
import pandas as pd
import numpy as np

def convert_text_to_hyperlink(row):
    if row['心得'] == '尚未繳交':
        return '<span>尚未繳交</span>'
    else:
        return '<a href="{}">{}</a>'.format(row['心得'],  '查看心得')

def filter_indentities():
    filter_identities_list = []
    for i in range(3):
        if st.session_state['identities_select'][i]:
            filter_identities_list.append(identities[i])
    return filter_identities_list


st.set_page_config(page_title="NTU-EXCHANGE-REVIEW", 
page_icon="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/320/apple/285/airplane-departure_1f6eb.png", 
layout="wide", 
initial_sidebar_state="expanded")

col1, col2 = st.columns((3, 7))
with col1:
    st.write("""
            ## 國立臺灣大學出國交換
            ### 歷屆心得查詢器""")
    st.write()
with col2:
    tutorial = st.expander('使用說明看這 👀')
    others = st.expander('其他資訊點我 👈')
    with tutorial:
        st.write("""
        1. 先勾選想查詢的出國計畫身份
        2. 再輸入姐妹校名稱即可
        - 出國年度預設為近 10 年，**可自行追加**其他年度
        - 若只想看有繳心得的資料，請將「**僅顯示有繳交心得之結果**」打勾""")
    with others:
        st.write("""<a href="https://oia.ntu.edu.tw/students/outgoing.students.experience">資料來源：國立臺灣大學國際事務處 OIA</a>""", 
            unsafe_allow_html=True)
        st.write("""
                有任何疑問歡迎寫信至 B06107054@ntu.edu.tw（臺大日文五游駿霖）""")

df = pd.read_csv('./data/data_all_review.csv')
df['心得'] = df.apply(convert_text_to_hyperlink, axis=1)

if 'identities_select' not in st.session_state:
    st.session_state['identities_select'] = [False for i in range(3)]
identities = ['暑期', '訪問', '交換']
year_list = list(map(lambda x: str(x) + '年度', list(range(87, 111))))

try:
    st.write("""
            ---
            **學生身份別（可複選）**
            """)
    cols = st.columns(3)
    for i, col in enumerate(cols):
        st.session_state['identities_select'][i] = col.checkbox(identities[i])
    if st.session_state['identities_select'] != [False, False, False]:
        identity = filter_indentities()
        school = st.multiselect('輸入姐妹校名稱（可複選）', options=list(df['交換學校'].unique()), default="南洋理工大學")
        year = st.multiselect('選擇出國年度（可複選，預設 100 - 110 年度）', options=year_list, default=year_list[:12:-1])
        review = st.checkbox('僅顯示有繳交心得之結果')

    try:
        if review:
            display_df = df.query('學生身份別 == @identity and 交換學校 == @school and 交換年度.str.contains("|".join(@year)) and 心得 != "<span>尚未繳交</span>"')
        else:
            display_df = df.query('學生身份別 == @identity and 交換學校 == @school and 交換年度.str.contains("|".join(@year))')
        st.write("""
                ---""")
        st.write(f"<h3>查詢結果<span style='font-size: 12pt'>（{int(display_df.shape[0])}筆結果）</span></h3>", 
                unsafe_allow_html=True)
        st.write("""<style>
            tr:hover {background-color:#50536b42;
            table {
                layout: auto;
                max-width: -moz-fit-content;
                max-width: fit-content;
            }</style>""", 
                unsafe_allow_html=True)
        st.write(f"""<div style="overflow: scroll; justify-content: center;">{display_df.to_html(escape=False, index=False)}</div>""", 
                unsafe_allow_html=True)
        st.balloons()

    except:
        st.error("""
                **請先選擇身份**
                """)

except:
    st.error("""
            ***Oops, 網頁發生錯誤！建議重新整理後再次嘗試（按太快網頁會壞掉 ><）***
            """)