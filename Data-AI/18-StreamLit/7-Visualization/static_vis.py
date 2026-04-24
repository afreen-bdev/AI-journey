import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Visualization App", layout="wide")

st.header("Matplotlib & Seaborn Visualization in Streamlit")

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("./tips.csv")
st.subheader("Dataset Preview")
st.dataframe(df.head())

# =========================
# SAFE COLUMN DETECTION
# =========================
cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
num_cols = df.select_dtypes(include=np.number).columns.tolist()

# fallback (important)
if not cat_cols:
    cat_cols = df.columns.tolist()

# =========================
# 1. Male vs Female Count
# =========================
st.markdown("---")
st.subheader("1. Male vs Female Distribution")

value_counts = df['sex'].value_counts()

col1, col2 = st.columns(2)

with col1:
    st.write("### Pie Chart")
    fig, ax = plt.subplots()
    ax.pie(value_counts, autopct='%0.2f%%', labels=value_counts.index)
    st.pyplot(fig)

with col2:
    st.write("### Bar Chart")
    fig, ax = plt.subplots()
    ax.bar(value_counts.index, value_counts)
    st.pyplot(fig)

with st.expander("Show Data"):
    st.dataframe(value_counts)

# =========================
# 2. Distribution (Box / Violin / KDE / Histogram)
# =========================
st.markdown("---")
st.subheader("2. Distribution of Total Bill by Gender")

chart = ('box', 'violin', 'kdeplot', 'histogram')
chart_selection = st.selectbox("Select Chart Type", chart)

fig, ax = plt.subplots()

if chart_selection == 'box':
    sns.boxplot(x='sex', y='total_bill', data=df, ax=ax)

elif chart_selection == 'violin':
    sns.violinplot(x='sex', y='total_bill', data=df, ax=ax)

elif chart_selection == 'kdeplot':
    sns.kdeplot(x=df['total_bill'], hue=df['sex'], ax=ax, fill=True)

else:
    sns.histplot(data=df, x='total_bill', hue='sex', ax=ax)

st.pyplot(fig)

# =========================
# 3. Average Total Bill (Groupby + Charts)
# =========================
st.markdown("---")
st.subheader("3. Avg Total Bill by Features")

with st.container():
    c1, c2, c3 = st.columns(3)

    # Feature selection
    with c1:
        group_cols = st.multiselect(
            "Select Features",
            cat_cols,
            default=[cat_cols[0]] if cat_cols else []
        )

    # Chart type
    with c2:
        chart_type = st.selectbox(
            "Chart Type",
            ['bar', 'line', 'area']
        )

    # Stacked option
    with c3:
        stack_option = st.radio("Stacked", ['Yes', 'No'])
        stacked = True if stack_option == 'Yes' else False

# safety check
if not group_cols:
    st.warning("Please select at least one feature")
else:
    feature = ['total_bill']
    select_cols = feature + group_cols

    avg_total_bill = df[select_cols].groupby(group_cols).mean()

    # handle multi-index
    if len(group_cols) > 1:
        avg_total_bill = avg_total_bill.unstack()

    avg_total_bill = avg_total_bill.fillna(0)

    fig, ax = plt.subplots()

    avg_total_bill.plot(
        kind=chart_type,
        ax=ax,
        stacked=stacked if chart_type == 'bar' else False
    )

    ax.set_ylabel("Avg Total Bill")
    ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

    st.pyplot(fig)

    with st.expander("Show Data"):
        st.dataframe(avg_total_bill)

# =========================
# 4. Scatter Plot (Total Bill vs Tip)
# =========================
st.markdown("---")
st.subheader("4. Total Bill vs Tip (Scatter Plot)")

hue_feature = st.selectbox(
    "Select Feature for Hue",
    cat_cols if cat_cols else df.columns
)

fig, ax = plt.subplots()

sns.scatterplot(
    x='total_bill',
    y='tip',
    hue=hue_feature,
    data=df,
    ax=ax
)

st.pyplot(fig)