import random
import ast
import streamlit as st
import streamlit.components.v1 as components
import altair as alt
import pandas as pd

# @st.cache  # Add caching so we load the data only once
# def load_data():
#     data = pd.read_csv('df_FINAL_narratives.csv')
#     return data

# data = load_data()

def show_plot(dictionary=None, key=None, plotname=None, height=800):
    if key:
        plotname = dictionary[key]
        HtmlFile = open(plotname, 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        print(source_code)
        components.html(source_code, height=height)

st.set_page_config(layout="wide")

st.title('Аналіз медіа наративів навколо обстрілу Краматорського вокзалу')

st.markdown('Задача: Провести аналіз поширення їх новин у ЗМІ з цього приводу після 10 год. 28 хв. 08 квітня 2022 року із встановленням першоджерела, подальшого поширення, яким чином подавалась інформація щодо того ким здійснено обстріл та щодо засобів, які використовувались, а також яким чином змінювалась інформація, яка подавалася.')

st.markdown('## Які новинні наративи поширювались загалом?')

options_general_narratives = ['Винуватець', 'Докази', 'Мета', "Фреймінг"]
selected_option = st.radio('Оберіть, будь ласка, тип наратива:', options_general_narratives)
st.write(f'Ви переглядаєте динаміку наратива: {selected_option}')
section1_mapping:{'Винуватець':'section1_plots/culprit_plot_area_general.html',
                  'Докази': 'section1_plots/evidence_plot_area_general.html',
                  'Мета': 'section1_plots/goal_plot_area_general.html',
                  'Фреймінг': 'section1_plots/framing_plot_area_general.html'}
show_plot(options_general_narratives, selected_option)

st.markdown('### Які новинні наративи поширювались протягом перших 24 годин?')
selected_option = st.radio('Оберіть, будь ласка, тип наратива:', options_general_narratives)
st.write(f'Ви переглядаєте динаміку наратива: {selected_option}')

st.markdown('### Хто був першоджерелом повідомлень для кожного типу наративу в межах нашого набору Телеграм каналів?')
selected_option = st.radio('Оберіть, будь ласка, тип наратива:', options_general_narratives)
st.write(f'Ви переглядаєте динаміку наратива: {selected_option}')

st.markdown('### Найважливіші наративи доказів щодо обстрілу')

st.markdown('### Найважливіші наративи щодо зброї і винуватця')

st.markdown('### Найважливіші наративи щодо мети обстрілу')

st.markdown('## Які ?')

st.markdown('## Які мотиви присутні в обговореннях події?')

st.markdown('## Хто був важливими джерелами свідчень і думок при обговоренні події?')

st.markdown('## Методологія дослідження')








# Display the HTML file in Streamlit
# HtmlFile = open('chart.html', 'r', encoding='utf-8')
# source_code = HtmlFile.read()
# print(source_code)
# components.html(source_code, height=800)



