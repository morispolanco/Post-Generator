import streamlit as st
import gateway

def header():
    st.header('Generador de entradas para blogs')
    st.text('version 0 - Last update 08/08/2022')

def instert_text():
    txt = st.text_area("Escriba el título de la entrada", height=250)
    colum1, colum2,colum3,colum4,colum5 = st.columns([1,1,1,1,1])
    
    if colum1.button("Genere"):
        with st.spinner(text='en progreso'):
            
            new_txt, status = gateway.conect_corretor_estilo(txt)
        
            if status == 200:
                st.text_area(label="Entrada:", value=new_txt["correction"], height=250)
                st.success("¡Hecho!")  
            else:
                st.text_area(label="Error:", value=new_txt["Error"])
                st.error(new_txt["Error"]) 
    
    if colum2.button("Limpie"):
        st.info("cleaning")

st.sidebar.markdown("# Creador de posts ❄️")
header()
instert_text()
