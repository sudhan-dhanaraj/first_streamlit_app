import streamlit
import snowflake.snowpark
from snowflake.snowpark import Session

connection_parameters={
  "account":"vw39252.us-east-2.aws",
  "user":"Sudhan",
  "password":"Sudhan@9596",
  "role":"SYSADMIN",
  "database":"TEST",
  "schema":"SCH1"
}

session=Session.builder.configs(connection_parameters).create()
df=session.table('NAME')
streamlit.dataframe(df)
