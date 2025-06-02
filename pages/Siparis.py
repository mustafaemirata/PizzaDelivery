import streamlit as st

st.header("Sipariş")

with st.form("siparis",clear_on_submit=True):
    isim=st.text_input("İsim Soyisim")
    # daha geniş metin alanı
    adres=st.text_area("Adres")



    pizza=st.selectbox("Pizza Seç",["Jambonlu","Sucuklu","Tavuklu"])
    boy=st.selectbox("Boy",["Small","Medium","Large"])
    icecek=st.selectbox("İçecek",["Ayran","Kola","SArı Kola","Ice Tea"])
    siparisver=st.form_submit_button("Sİpariş Ver")