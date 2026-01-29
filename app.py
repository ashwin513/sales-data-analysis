
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Data Analysis", layout="wide")
st.title("Sales Data Analysis Dashboard")

data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales": [12000, 15000, 10000, 18000, 20000, 22000]
}

df = pd.DataFrame(data)
df["Growth_%"] = df["Sales"].pct_change() * 100

st.subheader("Sales Overview")
col1, col2 = st.columns(2)
col1.metric("Total Sales", df["Sales"].sum())
col2.metric("Best Month", df.loc[df["Sales"].idxmax(), "Month"])

st.subheader("Sales Data")
st.dataframe(df)

st.subheader("Sales Trend")
st.line_chart(df.set_index("Month")["Sales"])

st.subheader("Insights")
st.write("- Sales show a steady increase after March.")
st.write("- June recorded the highest sales growth.")
