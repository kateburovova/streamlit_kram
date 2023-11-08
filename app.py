import random
import ast
import streamlit as st
import streamlit.components.v1 as components
import altair as alt
import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', 50)
@st.cache  # Add caching so we load the data only once
def load_data(path):
    data = pd.read_csv(path)
    data.drop(columns=['Unnamed: 0'], inplace=True)
    return data

def pastel_styling(df):
    return df.style.applymap(lambda x: "background-color: %s" % "paleturquoise")

# data = load_data()

def show_plot(dictionary=None, key=None, plotname=None, height=800):
    if key:
        plotname = dictionary[key]
        HtmlFile = open(plotname, 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        print(source_code)
        components.html(source_code, height=height)

st.set_page_config(layout="wide")

# st.markdown("""
# # Table of Contents
# 1. [Section 1](#section-1)
# 2. [Section 2](#section-2)
# 3. [Section 3](#section-3)
# """)

st.title('Аналіз медіа наративів навколо обстрілу Краматорського вокзалу')

# st.markdown('Задача: Провести аналіз поширення їх новин у ЗМІ з цього приводу після 10 год. 28 хв. 08 квітня 2022 року із встановленням першоджерела, подальшого поширення, яким чином подавалась інформація щодо того ким здійснено обстріл та щодо засобів, які використовувались, а також яким чином змінювалась інформація, яка подавалася.')

# color = "#C2D8AA"
# message1 = 'Задача: Провести аналіз поширення їх новин у ЗМІ з цього приводу після 10 год. 28 хв. 08 квітня 2022 року із встановленням першоджерела, подальшого поширення, яким чином подавалась інформація щодо того ким здійснено обстріл та щодо засобів, які використовувались, а також яким чином змінювалась інформація, яка подавалася.'
# message2 = 'Кожен з поданих графіків - інтерактивний. Для зміни масштаба скористайтесь типовим жестом "збільшити", при наведенні на відповідну частину графіка ви побачите підказку.'
#
# st.markdown(f"""
#     <div style='background-color: {color}; padding: 10px; border-radius: 5px;'>
#         <p style='color: black; text-align: left;'>
#             {message1}<br>
#             {message2}
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

########################Загальні деталі поширення
st.markdown('## Які новинні наративи поширювались загалом?')

st.write('В першу добу після обстрілу російські Телеграм канали здебільшого мотивували провину України тим, що аналогічну зброю ЗСУ активно використовували при обстрілах так званих ДНР та ЛНР.')

options_general_narratives = ['Докази', 'Винуватець', 'Мета', "Фреймінг"]
selected_option1 = st.radio('Оберіть, будь ласка, тип наратива:', options_general_narratives, key='general_narrative')
st.write(f'Ви переглядаєте динаміку наратива: {selected_option1}')
section1_mapping={'Винуватець':'section1_plots/culprit_plot_area_general.html',
                  'Докази': 'section1_plots/evidence_plot_area_general.html',
                  'Мета': 'section1_plots/goal_plot_area_general.html',
                  'Фреймінг': 'section1_plots/framing_plot_area_general.html'}
show_plot(section1_mapping, selected_option1)



############Перші 24 години

# st.markdown('### Які новинні наративи поширювались протягом перших 24 годин?')
# selected_option2 = st.radio('Оберіть, будь ласка, тип наратива:', options_general_narratives, key='first_24_hours_narrative')
# st.write(f'Ви переглядаєте динаміку наратива: {selected_option2}')

st.markdown('### Хто був першоджерелом повідомлень для кожного типу наративу в межах нашого набору Телеграм каналів?')
# selected_option3 = st.radio('Оберіть, будь ласка, тип наратива:', options_general_narratives, key='source_of_narrative')
# st.write(f'Ви переглядаєте динаміку наратива: {selected_option3}')

options_general_narratives_reduced3 = ['Докази', 'Мета', "Фреймінг"]
selected_option3 = st.radio('Оберіть, будь ласка, тип наратива:', options_general_narratives_reduced3, key='unique_narrative_source')
st.write(f'Ви переглядаєте динаміку наратива: {selected_option3}')
section3_mapping={
    'Докази': 'first_narrative_tables/unique_evidence_level2 (1).csv',
    # 'Винуватець': None,
    'Мета': 'first_narrative_tables/df_unique_goals.csv',
    'Фреймінг': 'first_narrative_tables/df_unique_framing.csv'}

# df_unique_evidence_level2 = load_data('first_narrative_tables/unique_evidence_level2.csv')

st.dataframe(load_data(section3_mapping[selected_option3]), height=400)

# show_plot(section1_mapping, selected_option1)
# st.dataframe(df_unique_evidence_level2, height=400)

########################За типами наративів

#############Докази
st.markdown('### Найважливіші наративи доказів щодо обстрілу')

options_general_levels = ['Найголовніші деталізовано', 'Найголовніші узагальнено', 'Всі']
selected_option4 = st.radio('Оберіть, будь ласка, рівень деталізації:', options_general_levels, key='levels4')
st.write(f'Ви переглядаєте рівень деталізації наратива: {selected_option4}')
section4_mapping={
    'Найголовніші узагальнено': 'histo_topN_narratives/level2/plot_HISTO_evidence50_level2.html',
    'Найголовніші деталізовано': 'histo_topN_narratives/level1/plot_HISTO_evidence25_level1.html',
    "Всі": 'histo_topN_narratives/all/all_evidence_distribution_by_date_top_percent.html'}
show_plot(section4_mapping, selected_option4)

#############Мета
st.markdown('### Найважливіші наративи щодо мети обстрілу')
selected_option5 = st.radio('Оберіть, будь ласка, рівень деталізації:', options_general_levels, key='levels5')
st.write(f'Ви переглядаєте рівень деталізації наратива: {selected_option5}')
section5_mapping={
    'Найголовніші узагальнено': 'histo_topN_narratives/level2/plot_HISTO_goal50_level2-2.html',
    'Найголовніші деталізовано': 'histo_topN_narratives/level1/plot_HISTO_goal25_level1.html',
    'Всі': 'histo_topN_narratives/all/all_goal_distribution_by_date_top_percent.html'}
show_plot(section5_mapping, selected_option5)
# st.markdown('### Найважливіші наративи щодо зброї і винуватця')


st.markdown('## Найважливіші мотиви присутні в обговореннях події?')

selected_option6 = st.radio('Оберіть, будь ласка, рівень деталізації:', options_general_levels, key='levels6')
st.write(f'Ви переглядаєте рівень деталізації наратива: {selected_option6}')
section6_mapping={
    'Найголовніші узагальнено': 'histo_topN_narratives/level2/plot_HISTO_framing25_level2.html',
    'Найголовніші деталізовано': 'histo_topN_narratives/level1/plot_HISTO_framing25_level1.html',
    'Всі': 'histo_topN_narratives/all/all_framing_distribution_by_date_top_percent.html'}
show_plot(section6_mapping, selected_option6)

# st.markdown('## Хто був важливими джерелами свідчень і думок при обговоренні події?')

st.markdown('## Хто найбільше розповсюджував трафаретні повідомлення')

selected_option7 = st.radio('Оберіть, будь ласка, рівень деталізації:', options_general_narratives_reduced3, key='levels7')
st.write(f'Ви переглядаєте рівень деталізації наратива: {selected_option7}')
section7_mapping={
    'Докази': 'author_plots/evidence_author_distibution.html',
    'Мета': 'author_plots/goal_author_distibution.html',
    'Фреймінг': 'author_plots/framing_author_distibution.html'}
show_plot(section7_mapping, selected_option7)


st.markdown('## Розповсюдження трафаретних повідомлень')

options_8 = ['Докази', 'Мета']
selected_option8 = st.selectbox('Оберіть, будь ласка, тип наратива:', options_8, key='levels8')
options_8_1 = ['Впливовість за переглядами', 'Впливовість за EC', 'Впливовість за BC']
selected_option8_1 = st.selectbox('Оберіть, будь ласка, визначення впливовості:', options_8_1, key='levels81')
options_8_2 = ['Узагальнено', 'Деталізовано']
selected_option8_2 = st.selectbox('Оберіть, будь ласка, рівень узагальнення:', options_8_2, key='levels82')
st.write(f'Ви переглядаєте наратив: {selected_option8}, {selected_option8_1}, {selected_option8_2}')

combo = f'{selected_option8} + {selected_option8_1} + {selected_option8_2}'

combo_mapping8 = {'Докази + Впливовість за переглядами + Узагальнено': 'trafaret/SHevidence_swarmplot_by_timesteps_SHAPES_level2_EC.html',
                  'Докази + Впливовість за EC + Узагальнено': 'trafaret/SHevidence_swarmplot_by_timesteps_SHAPES_level2_EC.html',
                  'Докази + Впливовість за BC + Узагальнено': 'trafaret/SHevidence_swarmplot_by_timesteps_SHAPES_level2_BC.html',
                  'Мета + Впливовість за переглядами + Узагальнено': 'trafaret/SHgoal_swarmplot_by_timesteps_SHAPES_level2_VIEWS.html',
                  'Мета + Впливовість за EC + Узагальнено': 'trafaret/SHgoal_swarmplot_by_timesteps_SHAPES_level2_EС.html',
                  'Мета + Впливовість за BC + Узагальнено': 'trafaret/SHgoal_swarmplot_by_timesteps_SHAPES_level2_EС.html',
                  'Докази + Впливовість за переглядами + Деталізовано': 'trafaret/SHevidence_swarmplot_by_timesteps_SHAPES_level1_VIEWS.html',
                  'Докази + Впливовість за EC + Деталізовано': 'trafaret/SHevidence_swarmplot_by_timesteps_SHAPES_level1_EC.html',
                  'Докази + Впливовість за BC + Деталізовано': 'trafaret/SHevidence_swarmplot_by_timesteps_SHAPES_level1_BC.html',
                  'Мета + Впливовість за переглядами + Деталізовано': 'trafaret/SHgoal_swarmplot_by_timesteps_SHAPES_level1_VIEWS.html',
                  'Мета + Впливовість за EC + Деталізовано': 'trafaret/SHgoal_swarmplot_by_timesteps_SHAPES_level1_EС.html',
                  'Мета + Впливовість за BC + Деталізовано': 'trafaret/SHgoal_swarmplot_by_timesteps_SHAPES_level1_ВС.html'}

show_plot(combo_mapping8, combo)


'Впливовість BC (number of times an individual acts as a bridge between other individuals), Впливовість EC and eigenvector centrality (importance of an individual based on the importance of those they are connected to)'
st.markdown('## Методологія дослідження')








# Display the HTML file in Streamlit
# HtmlFile = open('chart.html', 'r', encoding='utf-8')
# source_code = HtmlFile.read()
# print(source_code)
# components.html(source_code, height=800)



