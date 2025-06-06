import streamlit as st
import sqlite3

conn=sqlite3.connect("pizzadb.sqlite3")
c=conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS pizzalar(isim TEXT, smfiyat REAL,mdfiyat REAL,lgfiyat REAL,icindekiler TEXT,resim TEXT)")
conn.commit()




st.header("Pizza Ekle")

with st.form("pizzaekle",clear_on_submit=True):
    isim=st.text_input("Pizza İsmi:")
    smfiyat=st.number_input("Small Fiyat")
    mdfiyat=st.number_input("Medium Fiyat")
    lgfiyat=st.number_input("Large Fiyat")
    icindekiler=st.multiselect("İçindekiler",["Mantar","Jambon","Pastırma","Zeytin","Mozerella","Tavuk","Ton Balığı","Fesleğen","Biber"
                                              ,"Sucuk","Kereviz","Salam"])
    resim=st.file_uploader("Pizza resmi ekleyiniz.")

    ekle=st.form_submit_button("Pizza Ekle")

    if ekle:
        icindekiler=str(icindekiler)
        icindekiler=icindekiler.replace("[","")
        icindekiler=icindekiler.replace("]","")
        icindekiler=icindekiler.replace("'","")
        st.write(icindekiler)

        resimurl="img/"+resim.name
        open(resimurl,"wb").write(resim.read())
        st.write(resimurl)

        c.execute("INSERT INTO pizzalar VALUES (?,?,?,?,?,?)",(isim,smfiyat,mdfiyat,lgfiyat,icindekiler,resimurl))
        conn.commit()

        st.success("Pizza başarıyla eklendi.")