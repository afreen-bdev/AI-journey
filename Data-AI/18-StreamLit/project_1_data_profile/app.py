import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import os

# Page config
st.set_page_config(page_title="Data Profiler", layout="wide")

# -------------------------------
# Utility Functions
# -------------------------------

def get_filesize(file):
    size_bytes = len(file.getvalue())
    size_mb = size_bytes / (1024 * 1024)
    return size_mb


def validate_file(file):
    filename = file.name
    name, ext = os.path.splitext(filename)
    return ext.lower() in ['.csv', '.xlsx']


# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:
    st.title("⚙️ Settings")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel file",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:
        minimal = st.checkbox("Minimal Report", value=False)

# -------------------------------
# Main Logic
# -------------------------------

if uploaded_file is not None:

    if validate_file(uploaded_file):

        filesize = get_filesize(uploaded_file)

        if filesize <= 10:

            # Read file
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                xl_file = pd.ExcelFile(uploaded_file)
                sheet_name = st.sidebar.selectbox(
                    "Select Sheet", xl_file.sheet_names
                )
                df = xl_file.parse(sheet_name)

            st.subheader("📊 Data Preview")
            st.dataframe(df.head())

            # Generate profiling report
            with st.spinner("Generating Report... ⏳"):
                profile = ProfileReport(df, minimal=minimal)

            st.subheader("📈 Profiling Report")
            st_profile_report(profile)

        else:
            st.error("❌ File size should be less than 10 MB")

    else:
        st.error("❌ Please upload only CSV or Excel (.xlsx) files")

else:
    st.title("📊 Data Profiler App")
    st.info("👈 Upload a file from the sidebar to generate report")