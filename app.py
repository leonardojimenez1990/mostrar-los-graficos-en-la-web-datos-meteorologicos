import streamlit as st
import pandas as pd
import numpy as np

# import plotly.express as px

# the web title
st.title("Изменение метеорологических величин в течение дня")

# read data wich pandas librery
#file = pd.ExcelFile('leonardoejercicio1.xlsx')
file = pd.ExcelFile('https://github.com/leonardojimenez1990/leonardojimenez1990/leonardoejercicio1.xlsx?raw=True')
df = file.parse('Hoja1', header=2,
                names=['variables', '21:00', '00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00'])

nombreVariables = df['variables']
st.dataframe(df[0:].astype('str'), width=5000, height=5000)

# realizar la transversal de los datos    
df = file.parse('Hoja1', header=2,
                names=['variables', '21:00', '00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00']).T
st.dataframe(df[0:].astype('str'), width=5000, height=5000)

# salve data on variables
horas = df.index[1:]
tempSuelo = pd.to_numeric(df.iloc[:, 5], errors='coerce')
tempSuelo = pd.DataFrame(tempSuelo)
tempSuelo.columns = ['Температура почвы, °С']
# tempSuelo = pd.to_numeric(tempSuelo, errors='coerce')
tempAire = pd.to_numeric(df.iloc[1:, 6], errors='coerce').astype('Float64')
humedad = pd.to_numeric(df.iloc[1:, 7], errors='coerce').astype('Float64')

# selectBox
variable = st.selectbox('выберите переменную', [' ', 'Температура почвы, °С', 'Температура воздуха, °С'])
if variable == 'Температура почвы, °С':
    # writed from web

    col1, col2 = st.columns(2)
    with col1:
        st.success(variable)
        st.header("Таблица данных")
        st.dataframe(tempSuelo.iloc[1:, :])
        # fig = px.line(tempSuelo[0:], width=500, height=500)
        # fig.show()
        # st.pyplot(fig)
    with col2:
        st.header("Графика Температура почвы, °С")
        st.line_chart(tempSuelo[1:], width=800)

elif variable == 'Температура воздуха, °С':
    # writed from web
    col1, col2 = st.columns(2)
    with col1:
        st.success(variable)
        st.header("Таблица данных")
        st.dataframe(tempAire.astype('str'))
    with col2:
        st.header("Графика Температура воздуха, °С")
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

        st.line_chart(chart_data)
