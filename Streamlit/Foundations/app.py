import pandas as pd
import streamlit as st

# NOTE: this whole script re-runs from top to bottom every time the user
# touches a widget (dropdown, slider, etc). Thats how streamlit works,
# so I kept the loading part cached so it doesnt reload the csv each time.

st.set_page_config(page_title="Sales Data Viewer", layout="wide")


@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df["date"] = pd.to_datetime(df["date"])
    return df


st.title("Sales Data Viewer")
st.write("Small app to look at sales data in a few different sections.")

# ---------- sidebar (inputs) ----------
st.sidebar.header("Options")

uploaded = st.sidebar.file_uploader("Upload your own CSV (optional)", type="csv")
if uploaded is not None:
    df = load_data(uploaded)
else:
    df = load_data("sales.csv")

regions = sorted(df["region"].unique())
selected_regions = st.sidebar.multiselect("Region", regions, default=regions)

products = sorted(df["product"].unique())
selected_products = st.sidebar.multiselect("Product", products, default=products)

rows_to_show = st.sidebar.slider("Rows to show in table", 5, 50, 10)

# filter the data based on what was picked
filtered = df[df["region"].isin(selected_regions) & df["product"].isin(selected_products)]

# if nothing is left there is nothing to show, so stop here
if filtered.empty:
    st.warning("No data for these filters, pick at least one region and one product.")
    st.stop()

# ---------- sections ----------
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Table", "Charts", "Summary"])

with tab1:
    st.header("Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total revenue", f"${filtered['revenue'].sum():,}")
    col2.metric("Units sold", int(filtered["units"].sum()))
    col3.metric("Number of orders", len(filtered))

    st.write(
        f"Showing data from {filtered['date'].min().date()} "
        f"to {filtered['date'].max().date()}."
    )

with tab2:
    st.header("Data table")
    st.dataframe(filtered.head(rows_to_show))
    st.caption(f"{len(filtered)} rows match the filters, showing first {rows_to_show}.")

with tab3:
    st.header("Charts")

    left, right = st.columns(2)

    with left:
        st.subheader("Revenue by region")
        st.bar_chart(filtered.groupby("region")["revenue"].sum())

    with right:
        st.subheader("Revenue by product")
        st.bar_chart(filtered.groupby("product")["revenue"].sum())

    st.subheader("Revenue over time")
    st.line_chart(filtered.groupby("date")["revenue"].sum())

with tab4:
    st.header("Summary stats")
    st.write("Basic stats for the number columns:")
    st.table(filtered[["units", "price", "revenue"]].describe().round(2))

    st.write("Total revenue per region and product:")
    pivot = filtered.pivot_table(
        index="region", columns="product", values="revenue", aggfunc="sum", fill_value=0
    )
    st.dataframe(pivot)
