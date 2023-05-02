import pandas as pd
import streamlit as st
from database import *


def sql():
    a = st.text_area('Input your SQL Query here:')

    if st.button("Execute"):
        st.warning("{}".format(a))
        st.success("Query executed successfully")
        sql_query(a)
        result = sql_query(a)
        df = pd.DataFrame(result)
        st.dataframe(df)
