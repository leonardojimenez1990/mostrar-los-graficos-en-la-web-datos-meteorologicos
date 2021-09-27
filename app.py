import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Only a subset of options make sense
x_options = [
    'Изучение суточного хода основных метеорологических величин',
    'Изучение межсуточной изменчивости основных метеорологических величин',
    'Изучение годового хода основных показателей климата']

# Allow use to choose
select = st.sidebar.selectbox('Какую ценность вы хотите изучить?', x_options)
if select == 'Изучение суточного хода основных метеорологических величин':
    # the web title
    st.title('МЕТЕОРОЛОГИЯ И КЛИМАТОЛОГИЯ')
    #st.success(x_options[0])

    # read data wich pandas librery
    file = pd.ExcelFile('leonardoejercicio1.xlsx')
    #file = pd.ExcelFile('https://github.com/leonardojimenez1990/leonardojimenez1990/blob/main/leonardoejercicio1.xlsx?raw=True')
    df = file.parse('Hoja1', header=2,
                    names=['переменные', '21:00', '00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00'])

    nombreVariables = df['переменные']
    st.dataframe(df[0:].astype('str'), height=720)

    # realizar la transversal de los datos
    df = file.parse('Hoja1', header=2,
                    names=['переменные', '21:00', '00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00']).T
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
    variable = st.sidebar.radio(f'выберите переменную', ['Температура почвы, °С', 'Температура воздуха, \n°С',
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



elif select == 'Изучение межсуточной изменчивости основных метеорологических величин':
    # the web title
    st.title('МЕТЕОРОЛОГИЯ И КЛИМАТОЛОГИЯ')
    #st.success(x_options[1])
    # read data wich pandas librery
    file = pd.ExcelFile('leonardoejercicio1.xlsx')
    df = file.parse('Hoja2', header=1,
                    names=['Дни','Средняя Температура воздуха, °С', 'Максимальная Температура воздуха, °С',
                           'Минимальная Температура воздуха, °С',  'Минимальная относительная влажность, %',
                           'Атмосферное давление, гПа', 'Суточное количество осадков, мм'])
    st.dataframe(df.iloc[:,:].astype('str'),height=500)

    # salve data on variables
    dias = df.iloc[0:31, 0]

    tempAireMean = pd.to_numeric(df.loc[0:30,'Средняя Температура воздуха, °С' ], errors='coerce')

    tempAireMax = pd.to_numeric(df.loc[0:30, 'Максимальная Температура воздуха, °С'], errors='coerce')

    tempAireMin = pd.to_numeric(df.loc[0:30, 'Минимальная Температура воздуха, °С'], errors='coerce')

    humedad = pd.to_numeric(df.loc[0:30, 'Минимальная относительная влажность, %'], errors='coerce')

    presion = pd.to_numeric(df.loc[0:30, 'Атмосферное давление, гПа'], errors='coerce')

    lluvia = pd.to_numeric(df.loc[0:30, 'Суточное количество осадков, мм'], errors='coerce')

    #fig = px.area(df.iloc[0:31, 1:4], x=dias, y='Средняя Температура воздуха, °С',
     #             hover_name='Средняя Температура воздуха, °С',
      #            title=f'Средняя Температура воздуха, °С')
    #st.plotly_chart(fig)
    st.markdown(f'Средняя Температура воздуха, °С')
    st.area_chart(df.iloc[0:31, 1:4], height= 400)


    #fig = px.line(df.iloc[0:31, :], x=dias, y='Максимальная Температура воздуха, °С',
     #             hover_name='Максимальная Температура воздуха, °С',
      #            title=f'Максимальная Температура воздуха, °С')
    #st.plotly_chart(fig)

    #fig = px.line(df.iloc[0:31, :], x=dias, y='Минимальная Температура воздуха, °С',
     #             hover_name='Минимальная Температура воздуха, °С',
     #             title=f'Минимальная Температура воздуха, °С')
    #st.plotly_chart(fig)

    fig = px.bar(df.iloc[0:31, :], x=dias, y='Минимальная относительная влажность, %',
                 color='Минимальная относительная влажность, %', height=600,
                  hover_name='Минимальная относительная влажность, %',
                  title=f'Минимальная относительная влажность, %')
    st.plotly_chart(fig)

    fig = px.line(df.iloc[0:31, :], x=dias, y='Атмосферное давление, гПа',
                  hover_name='Атмосферное давление, гПа',
                  title=f'Атмосферное давление, гПа')
    st.plotly_chart(fig)

    fig = px.area(df.iloc[0:31, :], x=dias, y='Суточное количество осадков, мм',
                  hover_name='Суточное количество осадков, мм',
                  title=f'Суточное количество осадков, мм')
    st.plotly_chart(fig)




else:
    # the web title
    st.title('МЕТЕОРОЛОГИЯ И КЛИМАТОЛОГИЯ')
    #st.success(x_options[2])
    # read data wich pandas librery
    file = pd.ExcelFile('leonardoejercicio1.xlsx')
    df = file.parse('Hoja3', header=1,
                    names=['месяцы', '2013 Продолжительность солнечного сияния, часы',
                   'Средняя многол Продолжительность солнечного сияния, часы',
                   'Аномалия Продолжительность солнечного сияния, часы',
                   '2013 Температура воздуха, ºС', 'Средняя многол Температура воздуха, ºС',
                   'Аномалия Температура воздуха, ºС',
                   '2013 Относительная влажность воздуха, %',
                   'Средняя многол Относительная влажность воздуха, %', 'Аномалия Относительная влажность воздуха, %',
                   '2013 Количество осадков, мм','Средняя многол Количество осадков, мм',
                   'Аномалия Количество осадков, мм'])
    df.index = range(1,17)
    st.dataframe(df.iloc[:, :].astype('str'))

    meses = df.iloc[:12,0]
    #st.dataframe(meses)
    radiacion2013 = pd.to_numeric(df.iloc[:12, 1])
    #st.dataframe(radiacion2013)

    radiacionLP = pd.to_numeric(df.iloc[:12, 2])
    #st.dataframe(radiacionLP)

    radiacionAnom = pd.to_numeric(df.iloc[:12, 3])
    #st.dataframe(radiacionAnom)

    temp2013 = pd.to_numeric(df.iloc[:12, 4])
    #st.dataframe(temp2013)

    tempLP = pd.to_numeric(df.iloc[:12, 5])
    #st.dataframe(tempLP)

    tempAnom = pd.to_numeric(df.iloc[:12, 6])
    #st.dataframe(tempAnom)

    humedad2013 = pd.to_numeric(df.iloc[:12, 7])
    #st.dataframe(humedad2013)

    humedadLP = pd.to_numeric(df.iloc[:12, 8])
    #st.dataframe(humedadLP)

    humedadAnom = pd.to_numeric(df.iloc[:12, 9])
    #st.dataframe(humedadAnom)

    lluvia2013 = pd.to_numeric(df.iloc[:12, 10])
    #st.dataframe(lluvia2013)

    lluviaLP = pd.to_numeric(df.iloc[:12, 11])
    #st.dataframe(lluviaLP)

    lluviaAnom = pd.to_numeric(df.iloc[:12, 12])
    #st.dataframe(lluviaAnom)

    select = st.sidebar.radio(f'выберите переменную',['Продолжительность солнечного сияния, часы','Температура воздуха, ºС',
                     'Относительная влажность воздуха, %','Количество осадков, мм'])
    if select == 'Продолжительность солнечного сияния, часы':
        st.success(select)
        st.header("Таблица данных")
        st.dataframe(df.loc[:,['месяцы','2013 Продолжительность солнечного сияния, часы',
                        'Средняя многол Продолжительность солнечного сияния, часы',
                        'Аномалия Продолжительность солнечного сияния, часы']].astype('str'))
        
        fig = px.bar(df.iloc[:12, 1:3], height=500, width=1000,
                    title=f'сравнение Продолжительность солнечного сияния, часы')
        fig.update_layout(xaxis_title='месяцы')
        fig.update_layout(yaxis_title='Продолжительность солнечного сияния, часы')
        fig.update_layout(barmode='group')
        st.plotly_chart(fig)
        st.success('Минимальное значение 2013 г. Продолжительность инсоляции, часов составила '+ str(radiacion2013.min()) +
                   'в месяц '+str(radiacion2013.idxmin())+
                   ' Максимальное значение 2013 г. Продолжительность инсоляции, часов составила '+ str(radiacion2013.max()) +
                   ' в месяц '+str(radiacion2013.idxmax())+
                   '\n Минимальное значение Долгосрочной средней инсоляции, часов, составило '+ str(radiacionLP.min()) +
                   'в месяц '+str(radiacionLP.idxmin())+
                   ' Максимальное значение Долгосрочной средней инсоляции, часов, составило '+ str(radiacionLP.max()) +
                   ' в месяц '+str(radiacionLP.idxmax()))

        fig1 = px.bar(df.iloc[:12, 3], height=500, width=1000,
                     title=f'Аномалия Продолжительность солнечного сияния, часы')
        fig1.update_layout(xaxis_title='месяцы')
        fig1.update_layout(yaxis_title='Аномалия Продолжительность солнечного сияния, часы')
        st.plotly_chart(fig1)
        #radiacionAnomnegmeses=
        #radiacionAnomneg = pd.DataFrame(radiacionAnom[radiacionAnom < 0].values,
        #                                radiacionAnom[radiacionAnom < 0].index,columns='')
        #st.dataframe(radiacionAnomneg)
        col1, col2 = st.columns(2)
        col1.write("Месяцы отрицательных аномалий")
        col1.dataframe(radiacionAnom[radiacionAnom < 0].index)
        col2.write("Отрицательные значения аномалии")
        col2.dataframe(radiacionAnom[radiacionAnom < 0].values)

        col1, col2 = st.columns(2)
        col1.write("Месяцы положительных аномалий")
        col1.dataframe(radiacionAnom[radiacionAnom >= 0].index)
        col2.write("Положительные значения аномалии")
        col2.dataframe(radiacionAnom[radiacionAnom >= 0].values)

    elif select == 'Температура воздуха, ºС':
        st.success(select)
        st.header("Таблица данных")
        st.dataframe(df.loc[:, ['месяцы', '2013 Температура воздуха, ºС',
                                'Средняя многол Температура воздуха, ºС',
                                'Аномалия Температура воздуха, ºС']].astype('str'))

        fig = px.bar(df.iloc[:12, 4:6], height=500, width=1000,
                     title=f'сравнение Температура воздуха, ºС')
        fig.update_layout(xaxis_title='месяцы')
        fig.update_layout(yaxis_title='Температура воздуха, ºС')
        fig.update_layout(barmode='group')
        st.plotly_chart(fig)
        st.success('Минимальное значение 2013 г. Температура воздуха, ºС составила ' + str(temp2013.min()) +
            'в месяц ' + str(temp2013.idxmin()) +
            ' Максимальное значение 2013 г. Температура воздуха, ºС составила ' + str(temp2013.max()) +
            ' в месяц ' + str(temp2013.idxmax()) +
            '\n Минимальное значение Долгосрочной средней Температура воздуха, ºС, составило ' + str(tempLP.min()) +
            'в месяц ' + str(tempLP.idxmin()) +
            ' Максимальное значение Долгосрочной средней Температура воздуха, ºС, составило ' + str(tempLP.max()) +
            ' в месяц ' + str(tempLP.idxmax()))

        fig1 = px.bar(df.iloc[:12, 6], height=500, width=1000,
                      title=f'Аномалия Температура воздуха, ºС')
        fig1.update_layout(xaxis_title='месяцы')
        fig1.update_layout(yaxis_title='Аномалия Температура воздуха, ºС')
        st.plotly_chart(fig1)
        # radiacionAnomnegmeses=
        # radiacionAnomneg = pd.DataFrame(radiacionAnom[radiacionAnom < 0].values,
        #                                radiacionAnom[radiacionAnom < 0].index,columns='')
        # st.dataframe(radiacionAnomneg)
        col1, col2 = st.columns(2)
        col1.write("Месяцы отрицательных аномалий")
        col1.dataframe(tempAnom[tempAnom < 0].index)
        col2.write("Отрицательные значения аномалии")
        col2.dataframe(tempAnom[tempAnom < 0].values)

        col1, col2 = st.columns(2)
        col1.write("Месяцы положительных аномалий")
        col1.dataframe(tempAnom[tempAnom >= 0].index)
        col2.write("Положительные значения аномалии")
        col2.dataframe(tempAnom[tempAnom >= 0].values)

    elif select == 'Относительная влажность воздуха, %':
        st.success(select)
        st.header("Таблица данных")
        st.dataframe(df.loc[:, ['месяцы', '2013 Относительная влажность воздуха, %',
                                'Средняя многол Относительная влажность воздуха, %',
                                'Аномалия Относительная влажность воздуха, %']].astype('str'))

        fig2 = px.bar(df.iloc[:12, 7:9], height=500, width=1000,
                     title=f'сравнение Относительная влажность воздуха, %')
        fig2.update_layout(xaxis_title='месяцы')
        fig2.update_layout(yaxis_title='Относительная влажность воздуха, %')
        fig2.update_layout(barmode='group')
        st.plotly_chart(fig2)
        st.success('Минимальное значение 2013 г. Относительная влажность воздуха, % составила ' + str(humedad2013.min()) +
            'в месяц ' + str(humedad2013.idxmin()) +
            ' Максимальное значение 2013 г. Относительная влажность воздуха, % составила ' + str(humedad2013.max()) +
            ' в месяц ' + str(humedad2013.idxmax()) +
            '\n Минимальное значение Долгосрочной средней Относительная влажность воздуха, %, составило ' + str(humedadLP.min()) +
            'в месяц ' + str(humedadLP.idxmin()) +
            ' Максимальное значение Долгосрочной средней Относительная влажность воздуха, %, составило ' + str(humedadLP.max()) +
            ' в месяц ' + str(humedadLP.idxmax()))

        fig1 = px.bar(df.iloc[:12, 9], height=500, width=1000,
                      title=f'Аномалия Относительная влажность воздуха, %')
        fig1.update_layout(xaxis_title='месяцы')
        fig1.update_layout(yaxis_title='Относительная влажность воздуха, %')
        st.plotly_chart(fig1)
        # radiacionAnomnegmeses=
        # radiacionAnomneg = pd.DataFrame(radiacionAnom[radiacionAnom < 0].values,
        #                                radiacionAnom[radiacionAnom < 0].index,columns='')
        # st.dataframe(radiacionAnomneg)
        col1, col2 = st.columns(2)
        col1.write("Месяцы отрицательных аномалий")
        col1.dataframe(radiacionAnom[radiacionAnom < 0].index)
        col2.write("Отрицательные значения аномалии")
        col2.dataframe(radiacionAnom[radiacionAnom < 0].values)

        col1, col2 = st.columns(2)
        col1.write("Месяцы положительных аномалий")
        col1.dataframe(humedadAnom[humedadAnom >= 0].index)
        col2.write("Положительные значения аномалии")
        col2.dataframe(humedadAnom[humedadAnom >= 0].values)

    elif select == 'Количество осадков, мм':
        st.success(select)
        st.header("Таблица данных")
        st.dataframe(df.loc[:, ['месяцы', '2013 Количество осадков, мм',
                                'Средняя многол Количество осадков, мм',
                                'Аномалия Количество осадков, мм']].astype('str'))

        fig = px.bar(df.iloc[:12, 10:12], height=500, width=1000,
                     title=f'сравнение Количество осадков, мм')
        fig.update_layout(xaxis_title='месяцы')
        fig.update_layout(yaxis_title='Количество осадков, мм')
        fig.update_layout(barmode='group')
        st.plotly_chart(fig)
        st.success(
            'Минимальное значение 2013 г. Количество осадков, мм составила ' + str(lluvia2013.min()) +
            'в месяц ' + str(lluvia2013.idxmin()) +
            ' Максимальное значение 2013 г. Количество осадков, мм составила ' + str(radiacion2013.max()) +
            ' в месяц ' + str(lluvia2013.idxmax()) +
            '\n Минимальное значение Долгосрочной средней Количество осадков, мм, составило ' + str(lluviaLP.min()) +
            'в месяц ' + str(lluviaLP.idxmin()) +
            ' Максимальное значение Долгосрочной средней Количество осадков, мм, составило ' + str(lluviaLP.max()) +
            ' в месяц ' + str(lluviaLP.idxmax()))

        fig1 = px.bar(df.iloc[:12, 12], height=500, width=1000,
                      title=f'Аномалия Количество осадков, мм')
        fig1.update_layout(xaxis_title='месяцы')
        fig1.update_layout(yaxis_title='Аномалия Количество осадков, мм')
        st.plotly_chart(fig1)
        # radiacionAnomnegmeses=
        # radiacionAnomneg = pd.DataFrame(radiacionAnom[radiacionAnom < 0].values,
        #                                radiacionAnom[radiacionAnom < 0].index,columns='')
        # st.dataframe(radiacionAnomneg)
        col1, col2 = st.columns(2)
        col1.write("Месяцы отрицательных аномалий")
        col1.dataframe(lluviaAnom[lluviaAnom < 0].index)
        col2.write("Отрицательные значения аномалии")
        col2.dataframe(lluviaAnom[lluviaAnom < 0].values)

        col1, col2 = st.columns(2)
        col1.write("Месяцы положительных аномалий")
        col1.dataframe(lluviaAnom[lluviaAnom >= 0].index)
        col2.write("Положительные значения аномалии")
        col2.dataframe(lluviaAnom[lluviaAnom >= 0].values)


# @st.cache()
# def load_data():
#    df = pd.read_csv(
#        'https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True'
#    )
#    return df
