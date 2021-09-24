import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

# Only a subset of options make sense
x_options = [
    'Изучение суточного хода основных метеорологических величин',
    'Изучение межсуточной изменчивости основных метеорологических величин',
    'Изучение годового хода основных показателей климата']

# Allow use to choose
select = st.sidebar.selectbox('Какую ценность вы хотите изучить?', x_options)
if select == 'Изучение суточного хода основных метеорологических величин':
    # the web title
    st.title("Изучение суточного хода основных метеорологических величин")

    # read data wich pandas librery
    file = pd.ExcelFile('leonardoejercicio1.xlsx')
    #file = pd.ExcelFile('https://github.com/leonardojimenez1990/leonardojimenez1990/blob/main/leonardoejercicio1.xlsx?raw=True')
    df = file.parse('Hoja1', header=2,
                    names=['variables', '21:00', '00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00'])

    nombreVariables = df['variables']
    st.dataframe(df[0:].astype('str'), width=1024, height=720)

    # realizar la transversal de los datos
    df = file.parse('Hoja1', header=2,
                    names=['variables', '21:00', '00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00']).T
    df.columns = nombreVariables
    # st.dataframe(df[1:].astype('str'), width=1024, height=720)

    # salve data on variables
    horas = df.index[1:]
    tempSuelo = pd.to_numeric(df.iloc[:, 5], errors='coerce')
    tempSuelo = pd.DataFrame(tempSuelo)
    tempSuelo.columns = ['Температура почвы, °С']

    tempAire = pd.to_numeric(df.iloc[:, 6], errors='coerce')
    tempAire = pd.DataFrame(tempAire)
    tempAire.columns = ['Температура воздуха, °С']

    humedad = pd.to_numeric(df.iloc[:, 7], errors='coerce')
    humedad = pd.DataFrame(humedad)
    humedad.columns = ['тносительная Влажность воздуха, %']

    DViento = pd.to_numeric(df.iloc[:, 8], errors='coerce')
    DViento = pd.DataFrame(DViento)
    DViento.columns = ['Направление ветра, \nГрадусы']

    VViento = pd.to_numeric(df.iloc[:, 9], errors='coerce')
    VViento = pd.DataFrame(VViento)
    VViento.columns = ['Скорость ветра, м/с']

    presionEstac = pd.to_numeric(df.iloc[:, 10], errors='coerce')
    presionEstac = pd.DataFrame(presionEstac)
    presionEstac.columns = ['Атмосферное давление\nна уровне станции, гПа']

    presionMar = pd.to_numeric(df.iloc[:, 11], errors='coerce')
    presionMar = pd.DataFrame(presionMar)
    presionMar.columns = ['Атмосферное давление\nНа уровне моря, гПа']

    # selectBox
    variable = ' '
    variable = st.selectbox('выберите переменную', [' ', 'Температура почвы, °С', 'Температура воздуха, \n°С',
                                                    "Относительная \nВлажность воздуха, %",
                                                    'Направление ветра, \nГрадусы',
                                                    'Атмосферное давление\nна уровне станции, гПа'])
    if variable == 'Температура почвы, °С':
        # writed from web

        st.success(variable)
        st.header("Таблица данных")
        st.dataframe(tempSuelo.iloc[1:, :])
        # st.header("Графика Температура почвы, °С")
        fig = px.line(df.iloc[1:], x=horas, y=variable,
                      hover_name='Температура почвы, °С',
                      title=f'Температура почвы, °С в течение дня')
        st.plotly_chart(fig)

        st.success("Данные, полученные по температуре почвы, описывают поведение\n"
                   " температуры почвы в течение дня. Минимальная температура почвы наблюдается в\n"
                   " " + str(tempSuelo.idxmin().values) + " часов " + str(tempSuelo.min().values) + "° С \n"
                                                                                                    "а максимальная температура почвы наблюдается в " + str(
            tempSuelo.idxmax().values) + " часов "
                                         "" + str(tempSuelo.max().values) + "° С.\n"
                                                                            " Средняя температура почвы " + str(
            tempSuelo.mean().values) + "° С.\n"
                                       "График также показывает возрастающее поведение с 00:00 до 09:00. \n"
                                       "А с 09:00 до 15:00 наблюдается спад.")
    elif variable == 'Температура воздуха, \n°С':
        # writed from web

        st.success(variable)
        st.header("Таблица данных")
        st.dataframe(tempAire.iloc[1:, :])
        # st.header("Графика Температура воздуха, °С")
        fig = px.line(df.iloc[1:], x=horas, y=variable,
                      hover_name='Температура воздуха, \n°С',
                      title=f'Температура воздуха, °С в течение дня')
        st.plotly_chart(fig)

        st.success("Данные, полученные по Температура воздуха описывают поведение\n"
                   " Температура воздуха в течение дня. Минимальная Температура воздуха наблюдается в\n"
                   " " + str(tempAire.idxmin().values) + " часов " + str(tempAire.min().values) + "° С \n"
                                                                                                  "а максимальная Температура воздуха наблюдается в " + str(
            tempAire.idxmax().values) + " часов "
                                        "" + str(tempAire.max().values) + "° С.\n"
                                                                          " Средняя Температура воздуха " + str(
            tempAire.mean().values) + "° С.\n"
                                      "График также показывает возрастающее поведение с 03:00 до 09:00. \n"
                                      "А с 09:00 до 15:00 наблюдается спад.")

    elif variable == 'Относительная \nВлажность воздуха, %':
        # writed from web

        st.success(variable)
        st.header("Таблица данных")
        st.dataframe(humedad.iloc[1:, :])
        # st.header("Графика Относительная \nВлажность воздуха, %")
        fig = px.line(df.iloc[1:], x=horas, y=variable,
                      hover_name='Относительная \nВлажность воздуха, %',
                      title=f'Относительная Влажность воздуха, % в течение дня')
        st.plotly_chart(fig)

        st.success("Данные, полученные по Относительная Влажность воздуха описывают поведение\n"
                   " Относительная Влажность воздуха в течение дня. Минимальная Относительная Влажность воздуха наблюдается в\n"
                   " " + str(humedad.idxmin().values) + " часов " + str(humedad.min().values) + " % \n"
                                                                                                "а максимальная Относительная Влажность воздуха наблюдается в " + str(
            humedad.idxmax().values) + " часов "
                                       "" + str(humedad.max().values) + " %.\n"
                                                                        " Средняя Относительная Влажность воздуха " + str(
            humedad.mean().values) + " %.\n"
                                     "График также показывает возрастающее поведение с 21:00 до 06:00. \n"
                                     "А с 06:00 до 12:00 наблюдается спад. А с 12:00 до 15:00 наблюдается поведение.")

    elif variable == 'Направление ветра, \nГрадусы':
        # writed from web

        st.success(variable + ' и Скорость ветра, м/с')
        st.header("Таблица данных")
        col1, col2 = st.columns(2)
        #tabla1 = st.table(DViento.iloc[1:, :])
        #col1.title("Направление ветра, Градусы")
        col1.table(DViento.iloc[1:, :])
        #col1(tabla1, use_column_width=True)
        #tabla2 = st.table(VViento.iloc[1:, :])
        #col2.title("Скорость ветра, м/с")
        col2.table(VViento.iloc[1:, :])
        # col1(tabla2, use_column_width=True)
        # st.header("Графика Направление ветра, \nГрадусы")
        fig = px.bar_polar(df[1:], r="Скорость ветра, м/с", theta='Направление ветра, \nГрадусы',
                           color=horas, hover_name='Направление ветра, \nГрадусы',
                           title=f'Направление ветра, \nГрадусы и Скорость ветра, м/с в течение дня')
        st.plotly_chart(fig)

        st.success("Данные, полученные по Скорость ветра, м/с описывают поведение\n"
                   " Скорость ветра, м/с в течение дня. Минимальная Скорость ветра, м/с наблюдается в\n"
                   " " + str(VViento.idxmin().values) + " часов " + str(VViento.min().values) + " м/с \n и "
                   + str(DViento.loc[VViento.idxmin().values].values) +
                   " Градусы Направление ветра а максимальная Скорость ветра, м/с наблюдается в " + str(
            VViento.idxmax().values) + " часов " 
                   "" + str(VViento.max().values) + " м/с.\n и " + str(DViento.loc[VViento.idxmax().values].values) +
                   " Градусы Направление ветра Средняя Скорость ветра, м/с " + str(
            VViento.mean().values) + " м/с.\n")

    elif variable == 'Атмосферное давление\nна уровне станции, гПа':
        # writed from web

        st.success(variable + ' и Атмосферное давление\nНа уровне моря, гПа')
        st.header("Таблица данных")
        col1, col2 = st.columns(2)
        col1.table(presionEstac.iloc[1:, :])
        col2.table(presionMar.iloc[1:, :])
        # st.header("Графика Относительная \nВлажность воздуха, %")
        fig = px.line(df.iloc[1:], x=horas, y=variable,
                      hover_name='Атмосферное давление\nна уровне станции, гПа',
                      title=f'Атмосферное давление на уровне станции, гПа в течение дня')
        st.plotly_chart(fig)

        st.success("Данные, полученные по Атмосферное давление\nна уровне станции описывают поведение\n"
                   " Атмосферное давление\nна уровне станции в течение дня. Минимальная Атмосферное давление\nна уровне станции наблюдается в\n"
                   " " + str(presionEstac.idxmin().values) + " часов " + str(presionEstac.min().values) + " гПа \n"
                                        "а максимальная Атмосферное давление\nна уровне станции наблюдается в " + str(
            presionEstac.idxmax().values) + " часов "
                                       "" + str(presionEstac.max().values) + " гПа.\n"
                                       " Средняя Атмосферное давление\nна уровне станции " + str(
            presionEstac.mean().values) + " гПа.\n"
                                     "График также показывает возрастающее спад с 21:00 до 18:00. \n")

        fig = px.line(df.iloc[1:], x=horas, y='Атмосферное давление\nНа уровне моря, гПа',
                      hover_name='Атмосферное давление\nНа уровне моря, гПа',
                      title=f'Атмосферное давление\nНа уровне моря, гПа в течение дня')
        st.plotly_chart(fig)

        st.success("Данные, полученные по Атмосферное давление\nНа уровне моря описывают поведение\n"
                   " Атмосферное давление\nНа уровне моря в течение дня. Минимальная Атмосферное давление\nНа уровне моря наблюдается в\n"
                   " " + str(presionMar.idxmin().values) + " часов " + str(presionMar.min().values) + " гПа \n"
                                                                                                          "а максимальная Атмосферное давление\nНа уровне моря наблюдается в " + str(
            presionMar.idxmax().values) + " часов "
                                            "" + str(presionMar.max().values) + " гПа.\n"
                                                                                  " Средняя Атмосферное давление\nНа уровне моря " + str(
            presionMar.mean().values) + " гПа.\n"
                                          "График также показывает возрастающее спад с 21:00 до 18:00. \n")


else:
    # the web title
    st.title("Изучение межсуточной изменчивости основных метеорологических величин")
    # read data wich pandas librery
    file = pd.ExcelFile('leonardoejercicio1.xlsx')
    df = file.parse('Hoja2', header=1,
                    names=['dias','temperatura media', 'temperatura máxima', 'temperatura mínima',
                           'humedad minima', 'precision', 'precipitation'])
    st.dataframe(df.iloc[:31,:].astype('str'))

# @st.cache()
# def load_data():
#    df = pd.read_csv(
#        'https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True'
#    )
#    return df

# df = px.data.wind()
# st.dataframe(df)


# fig.show()

# Read in the cereal data
# df = load_data()
# st.dataframe(df)

# st.title('Rating exploration')


# plot the value
# fig = px.line(df,
#             x=x_axis,
#            y='rating',
#           hover_name='name',
#          title=f'Cereal ratings vs. {x_axis}')

# st.plotly_chart(fig)
