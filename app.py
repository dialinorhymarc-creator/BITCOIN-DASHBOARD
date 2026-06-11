import streamlit as st
import pandas as pd
from database import get_connection

st.title("📈 Bitcoin Dashboard")

conn = get_connection()

query = """
SELECT *
FROM crypto_prices
ORDER BY created_at DESC
"""

df = pd.read_sql(query, conn)

conn.close()

if len(df) > 0:

    latest_price = df.iloc[0]["price"]

    st.metric(
        "Current Bitcoin Price",
        f"${latest_price}"
    )

    chart_data = (
        df.sort_values("created_at")
        .set_index("created_at")
    )

    st.line_chart(chart_data["price"])

    st.dataframe(df)

else:
    st.warning("No data found.")