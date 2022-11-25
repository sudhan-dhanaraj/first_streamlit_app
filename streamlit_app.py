import streamlit
import pandas

streamlit.title('Pandas Dataframe')
df = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
df = df.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(df.index))
streamlit.dataframe(df)
