import streamlit as st
import gateway

def header():
    st.header('Corrector de estilo')
    st.text('version 0 - Last update 08/08/2022')

def instert_text():
    txt = st.text_area("Escriba aqui", height=250)
    colum1, colum2,colum3,colum4,colum5 = st.columns([1,1,1,1,1])
    
    if colum1.button("Corrija"):
        with st.spinner(text='en progreso'):
            
            new_txt, status = gateway.conect_corretor_estilo(txt)
        
            if status == 200:
                st.text_area(label="Texto corregido:", value=new_txt["correction"], height=250)
                st.success("¡Corregido!")  
            else:
                st.text_area(label="Error:", value=new_txt["Error"])
                st.error(new_txt["Error"]) 
    
    if colum2.button("Limpie"):
        st.info("cleaning")

st.sidebar.markdown("# Corretor de estilo ❄️")
header()
instert_text()