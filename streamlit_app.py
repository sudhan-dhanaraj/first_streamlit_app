import streamlit
import pandas

streamlit.tile('Pandas Dataframe')
df = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(df)
