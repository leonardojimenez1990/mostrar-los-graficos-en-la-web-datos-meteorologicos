import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#the web title
st.title("Изменение метеорологических величин в течение дня")

#read data wich pandas librery
file = pd.ExcelFile('leonardoejercicio1.xlsx')
df=file.parse('Hoja1',header=2, names=['variables','21:00', '00:00', '03:00', '06:00', '09:00', '12:00','15:00','18:00'])

nombreVariables = df['variables']
st.dataframe(df[0:].astype('str'), width=5000, height=5000)

#realizar la transversal de los datos    
df=file.parse('Hoja1',header=2, names=['variables','21:00', '00:00', '03:00', '06:00', '09:00', '12:00','15:00','18:00']).T
#st.table(df.loc[:,['5','6','7']])

#salve data on variables
horas = df.index[1:]
tempSuelo = pd.to_numeric(df.iloc[1:,5]).astype('Float64')
tempAire = pd.to_numeric(df.iloc[1:,6]).astype('Float64')
humedad = pd.to_numeric(df.iloc[1:,7]).astype('Float64')

#selectBox
variable = st.selectbox('Seleccione la variable',[' ','temperatura del suelo','temperatura del aire'])
if variable == 'temperatura del suelo':
    #writed from web
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(variable)
        st.header("Tabla de datos")
        st.dataframe(tempSuelo.astype('str'))
        fig = px.line(tempSuelo[0:], width=500, height=500)
        fig.show()
        st.pyplot(fig)
    with col2:
        st.header("Gráfico")
        
elif variable == 'temperatura del aire':
    #writed from web
    col1, col2 = st.columns(2)
    with col1:
        st.success(variable)
        st.header("Tabla de datos")
        st.dataframe(tempAire.astype('str'))
    with col2:
        st.header("Gráfico")
        st.image("https://static.streamlit.io/examples/cat.jpg")