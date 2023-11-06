import streamlit as st
import altair as alt
import pandas as pd
import random
import ast

def string_to_list(s):
    try:
        return ast.literal_eval(s)
    except (ValueError, SyntaxError):
        return s  # returns the original string if it cannot be parsed to a list


def generate_random_color():
    """Generate random color."""
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def plot_distribution_by_date_top_percent(df, colname, top_percentage=10, col_for_plotname = ''):
    """
    Plots the distribution by date for items within the top N% of the dataset.
    """
    plotname = f'Розподіл наративів {col_for_plotname} по окремим датам, топ {top_percentage}% всіх наративів'

    flattened_evidence = df[['date', colname]].explode(colname)
    flattened_evidence['date_only'] = pd.to_datetime(flattened_evidence['date']).dt.date
    grouped = (flattened_evidence.groupby(['date_only', colname])
               .size()
               .reset_index(name='count'))

    pivot_df = grouped.pivot(index='date_only', columns=colname, values='count').reset_index()
    pivot_df.fillna(0, inplace=True)

    excluded_vals = ['not valid', 'Not valid', '', 'Unknown']
    long_df = pivot_df.melt(id_vars='date_only', var_name='evidence', value_name='count')
    long_df = long_df[~long_df['evidence'].isin(excluded_vals)]

    # Calculate the total occurrences for each evidence type across all dates
    total_counts = long_df.groupby('evidence')['count'].sum()

    # Calculate the threshold for top N%
    threshold = total_counts.quantile(1 - top_percentage/100)

    # Keep only evidence types that have a total occurrence greater than the threshold
    relevant_evidence = total_counts[total_counts >= threshold].index
    long_df = long_df[long_df['evidence'].isin(relevant_evidence)]

    long_df['date_only'] = long_df['date_only'].astype(str)
    long_df['total'] = long_df.groupby('date_only')['count'].transform('sum')
    long_df['Percentage'] = long_df['count'] / long_df['total'] * 100

    evidence_types = long_df['evidence'].unique().tolist()
    custom_colors = [generate_random_color() for _ in range(len(evidence_types))]
    color_scale = alt.Scale(domain=evidence_types, range=custom_colors)

    date_dropdown = alt.binding_select(options=long_df['date_only'].unique().tolist(), name='Select Date ')
    date_selection = alt.selection_single(fields=['date_only'], bind=date_dropdown, init=None)

    chart = alt.Chart(long_df).mark_bar(size=200).encode(
        x=alt.X('Percentage:Q',
                axis=alt.Axis(tickCount=10, title='Відсоток зустрічань (%)', format='.0f'),
                scale=alt.Scale(domain=[0, 100]),
                sort='-y'),
        color=alt.Color('evidence:O', scale=color_scale, sort='ascending',
                        legend=alt.Legend(title="Наратив", labelLimit=0, titleFontSize=15, labelFontSize=13)),
        tooltip=[alt.Tooltip('evidence:O', title='Наратив'), alt.Tooltip('count:Q', title='Кількість')]
    ).transform_filter(
        date_selection
    ).properties(
        width=600,
        height=300,
        background='#F9F9F9',
        padding=25,
        title={
            "text": plotname,
            "subtitle": f"Розмір стовпчика відповідає % зустрічань наратива в обрану дату",
            "align": "left",
            "anchor": "start",
            "fontSize": 25,
            "subtitleFontSize": 13
        }
    ).add_selection(
        date_selection
    ).configure_axis(
        ticks=False,
        domain=False,
        gridDash=[1.5, 1.5],
        titleFontSize=13,
        labelPadding=8,
        titlePadding=15
    )

    return st.altair_chart(chart, use_container_width=True)

# Load data from CSV file
# @st.cache  # Add caching so we load the data only once
def load_data():
    data = pd.read_csv('df_FINAL_narratives.csv')
    col_list = ['culprit_pred', 'missile_pred','intent_pred','evidence_extractive_pred','evidence_abstractive_pred','framing_pred','goal_extractive_pred',
                'goal_abstractive_pred','quotes_extractive_pred','quotes_authors_pred','implicit_message_pred']
    for col in col_list:
        data[col] = data[col].apply(string_to_list)
    return data

# Use a button to trigger the data loading
# if st.button('Load Data'):
data = load_data()

# # Create an Altair chart using the loaded data
# chart = alt.Chart(data).mark_bar().encode(
#     x='a',
#     y='b'
# )

st.write(f"Type of data: {type(data['evidence_abstractive_pred'].iloc[200])}")
st.write(f"Type of data: {data['evidence_abstractive_pred'].iloc[200]}")


st.title('My Streamlit App with an Altair Chart')

plot_distribution_by_date_top_percent(data, 'culprit_pred_mapped', top_percentage=90)
# else:
#     st.write('Click the button to load data!')

