# -*- utf-8 -*-
import requests
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    plt.rcParams['font.family'] = 'Malgun Gothic'


    url = 'http://apis.data.go.kr/1160100/service/GetShorTermSecuIssuInfoService/getCdIssuBasiInfo'
    #금융위원회_단기금융증권발행정보
    #https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15059591

    api_key = st.secrets['private_key']

    params ={'serviceKey' : api_key, 'numOfRows' : '10000', 'pageNo' : '1', 'resultType' : 'xml'}

    response = requests.get(url, params=params)

    df = pd.read_xml(response.content, xpath=".//item")

    #print(df.head(5))
    #print(df.tail(5))
    #print(df.info())
    #print(df.columns.values)
    #print(df.loc[:,'codpIssuBnkNm'].value_counts())

    bank_count = pd.DataFrame(df.loc[:,'codpIssuBnkNm'].value_counts())
    print(bank_count.reset_index())

    fig, ax = plt.subplots(figsize=(12,8))

    sns.barplot(x='codpIssuBnkNm', y='count', data=bank_count, ax=ax)

    plt.xticks(rotation=45)

    st.title("CD - Count by Bank(20/04/08~21/01/03)")
    st.pyplot(fig)

if __name__=="__main__":
    main()


