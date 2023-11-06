import streamlit as st
import altair as alt
import pandas as pd

# Example data
data = pd.DataFrame({
    'a': list('CCCDDDEEE'),
    'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]
})

# Altair chart
chart = alt.Chart(data).mark_point().encode(
    x='a',
    y='b'
)

# Streamlit page title
st.title('My Streamlit App with an Altair Chart')

# Display the chart
st.altair_chart(chart, use_container_width=True)
