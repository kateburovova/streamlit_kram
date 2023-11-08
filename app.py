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

st.set_page_config(layout="wide")

st.title('Аналіз медіа наративів навколо обстрілу Краматорського вокзалу')
st.markdown('## Задача:')
st.markdown('Провести аналіз поширення їх новин у ЗМІ з цього приводу після 10 год. 28 хв. 08 квітня 2022 року із встановленням першоджерела, подальшого поширення, яким чином подавалась інформація щодо того ким здійснено обстріл та щодо засобів, які використовувались, а також яким чином змінювалась інформація, яка подавалася.')



# Display the HTML file in Streamlit
HtmlFile = open('chart.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height=800)



