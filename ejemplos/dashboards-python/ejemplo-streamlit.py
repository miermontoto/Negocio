import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
st.set_page_config(layout="wide")
df = sns.load_dataset('titanic')
st.title('Titanic Dashboard')
left_column, center_column, right_column = st.columns(3)
with left_column:
   st.subheader('Dataset')
   st.dataframe(df)
with center_column:
   st.subheader('Data Numerical Statistic')
   st.dataframe(df.describe())
with right_column:
   st.subheader('Data Visualization with respect to Survived')
   left_column_0, right_column_0 = st.columns(2)
   with left_column_0:
      'Numerical Plot'
      num_feat = st.selectbox(
      'Select Numerical Feature', df.select_dtypes('number').columns)
      fig = px.histogram(df, x = num_feat, color = 'survived')
      st.plotly_chart(fig, use_container_width=True)
   with right_column_0:
      'Categorical column'
      cat_feat = st.selectbox(
      'Select Categorical Feature', df.select_dtypes(exclude =   'number').columns)
      fig = px.histogram(df, x =cat_feat, color = 'survived' )
   st.plotly_chart(fig, use_container_width=True)