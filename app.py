import random
import ast
import streamlit as st
import streamlit.components.v1 as components
import altair as alt
import pandas as pd
import numpy as np

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

st.markdown("""
# Table of Contents
1. [Section 1](#section-1)
2. [Section 2](#section-2)
3. [Section 3](#section-3)
""")

st.title('Аналіз медіа наративів навколо обстрілу Краматорського вокзалу')

st.markdown('Задача: Провести аналіз поширення їх новин у ЗМІ з цього приводу після 10 год. 28 хв. 08 квітня 2022 року із встановленням першоджерела, подальшого поширення, яким чином подавалась інформація щодо того ким здійснено обстріл та щодо засобів, які використовувались, а також яким чином змінювалась інформація, яка подавалася.')

st.markdown('## Які новинні наративи поширювались загалом?')
options_general_narratives = ['Докази', 'Винуватець', 'Мета', "Фреймінг"]
selected_option1 = st.radio('Оберіть, будь ласка, тип наратива:', options_general_narratives, key='general_narrative')
st.write(f'Ви переглядаєте динаміку наратива: {selected_option1}')
section1_mapping={'Винуватець':'section1_plots/culprit_plot_area_general.html',
                  'Докази': 'section1_plots/evidence_plot_area_general.html',
                  'Мета': 'section1_plots/goal_plot_area_general.html',
                  'Фреймінг': 'section1_plots/framing_plot_area_general.html'}
show_plot(section1_mapping, selected_option1)

st.markdown('### Які новинні наративи поширювались протягом перших 24 годин?')
selected_option2 = st.radio('Оберіть, будь ласка, тип наратива:', options_general_narratives, key='first_24_hours_narrative')
st.write(f'Ви переглядаєте динаміку наратива: {selected_option2}')

st.markdown('### Хто був першоджерелом повідомлень для кожного типу наративу в межах нашого набору Телеграм каналів?')
selected_option3 = st.radio('Оберіть, будь ласка, тип наратива:', options_general_narratives, key='source_of_narrative')
st.write(f'Ви переглядаєте динаміку наратива: {selected_option3}')

# Sample data
data = {
    "Наратив": ["Наратив 1", "Наратив 2", "Наратив 3", "Наратив 4", "Наратив 5",
                 "Наратив 6", "Наратив 7", "Наратив 8", "Наратив 9", "Наратив 10",
                 "Наратив 11", "Наратив 12", "Наратив 13", "Наратив 14", "Наратив 15"],
    "Автор першого повідомлення": ["Автор 1", "Автор 2", "Автор 3", "Автор 4", "Автор 5",
                                    "Автор 6", "Автор 7", "Автор 8", "Автор 9", "Автор 10",
                                    "Автор 11", "Автор 12", "Автор 13", "Автор 14", "Автор 15"],
    "Повідомлення": ["Повідомлення 1", "Повідомлення 2", "Повідомлення 3", "Повідомлення 4", "Повідомлення 5",
                     "Повідомлення 6", "Повідомлення 7", "Повідомлення 8", "Повідомлення 9", "Повідомлення 10",
                     "Повідомлення 11", "Повідомлення 12", "Повідомлення 13", "Повідомлення 14", "Повідомлення 15"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to apply pastel styling to the dataframe
def pastel_styling(df):
    return df.style.applymap(lambda x: "background-color: %s" % "paleturquoise")

# Display the dataframe with pastel styling and only the first 10 rows
st.dataframe(pastel_styling(df.head(10)), height=400)

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



