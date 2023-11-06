import streamlit as st
import altair as alt
import pandas as pd
#
# # Example data
# data = pd.DataFrame({
#     'a': list('CCCDDDEEE'),
#     'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]
# })
#
# # Altair chart
# chart = alt.Chart(data).mark_point().encode(
#     x='a',
#     y='b'
# )
#
# # Streamlit page title
# st.title('My Streamlit App with an Altair Chart')
#
# # Display the chart
# st.altair_chart(chart, use_container_width=True)

import streamlit as st
import altair as alt
import pandas as pd

# Load data from CSV file
@st.cache  # Add caching so we load the data only once
def load_data():
    data = pd.read_csv('data.csv')
    return data

# Use a button to trigger the data loading
# if st.button('Load Data'):
data = load_data()

# Create an Altair chart using the loaded data
chart = alt.Chart(data).mark_bar().encode(
    x='a',
    y='b'
)

# Display the chart
st.altair_chart(chart, use_container_width=True)
# else:
#     st.write('Click the button to load data!')

