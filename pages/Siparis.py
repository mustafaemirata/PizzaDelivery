import streamlit as st
import sqlite3

from pages.Katalog import pizzalar

st.header("Sipariş")
conn=sqlite3.connect("pizzadb.sqlite3")
c=conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS siparisler (isim TEXT,adres TEXT, pizza TEXT, boy TEXT, icecek TEXT, fiyat REAL)")
conn.commit()
c.execute("SELECT isim FROM pizzalar")
isimler=c.fetchall()
st.write(isimler)

isimlerlist=[]
for i in isimler:
    isimler.append(i[0])
st.write(isimlerlist)



with st.form("siparis",clear_on_submit=True):
    isim=st.text_input("İsim Soyisim")
    # daha geniş metin alanı
    adres=st.text_area("Adres")



    pizza=st.selectbox("Pizza Seç",["Jambonlu","Sucuklu","Tavuklu"])
    boy=st.selectbox("Boy",["Small","Medium","Large"])
    icecek=st.selectbox("İçecek",["Ayran","Kola","SArı Kola","Ice Tea"])
    siparisver=st.form_submit_button("Sİpariş Ver")



    if siparisver:
        if boy=="Small":
            c.execute("SELECT smfiyat FROM pizzalar WHERE isim=?",(isim,))
            fiyat=c.fetchone()
        elif boy == "Medium":
            c.execute("SELECT mdfiyat FROM pizzalar WHERE isim=?", (isim,))
            fiyat = c.fetchone()
        elif boy == "Large":
            c.execute("SELECT lgfiyat FROM pizzalar WHERE isim=?", (isim,))
            fiyat = c.fetchone()


        st.write(fiyat)