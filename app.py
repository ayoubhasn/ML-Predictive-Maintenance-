import streamlit as st
import pandas as pd
import pickle

# Page configuration (colors + layout)
st.set_page_config(
    page_title="Predictive Maintenance System  ",
    page_icon="🔧",
    layout="wide"
)

# Custom CSS for colors and style
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stTitle {
        color: #1f77b4;
        text-align: center;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title(" AI Predictive Maintenance Dashboard")
st.markdown("### Upload machine data and predict failures using Machine Learning")

# Load trained model
@st.cache_resource
def load_model():
    return pickle.load(open("model.pkl", "rb"))

model = load_model()

# Sidebar (nice UI)
st.sidebar.header(" System Info")
st.sidebar.write("Model: Random Forest")
st.sidebar.write("Project: Predictive Maintenance")
st.sidebar.write("Field: IARCI ENSEM CASA ")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your CSV dataset", type=["csv"])

if uploaded_file is not None:
    # Read dataset
    data = pd.read_csv(uploaded_file)

    st.subheader("📊 Dataset Preview")
    st.dataframe(data.head(), use_container_width=True)

    # Preprocessing (same as training)
    try:
        X = data.drop(["UDI", "Product ID", "Failure Type", "Target"], axis=1, errors="ignore")
        X = pd.get_dummies(X, columns=["Type"])

        # Predict button
        if st.button(" Predict Machine Failure"):
            predictions = model.predict(X)
            data["Predicted Failure"] = predictions

            st.success("✅ Prediction Completed!")

            # Show results
            st.subheader("🔍 Prediction Results")
            st.dataframe(data, use_container_width=True)

            # Metrics
            total = len(predictions)
            failures = sum(predictions)
            normal = total - failures

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Machines", total)
            col2.metric("Predicted Failures", failures)
            col3.metric("Normal Machines", normal)

            # Chart
            st.subheader("📈 Failure Prediction Distribution")
            chart_data = pd.Series(predictions).value_counts()
            st.bar_chart(chart_data)

    except Exception as e:
        st.error(f" Error during prediction: {e}")

else:
    st.info("👆 Please upload a CSV file to start prediction.")
