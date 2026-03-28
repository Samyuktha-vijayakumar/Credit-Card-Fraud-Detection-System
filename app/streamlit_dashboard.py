import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
import gdown
import os

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

st.title("💳 Real-Time Credit Card Fraud Detection Dashboard")

st.markdown("""
This dashboard analyzes credit card transactions and detects potential fraud using a machine learning model.

Model:
• XGBoost Classifier  
• SMOTE for handling imbalanced fraud data
""")

# --------------------------------------------------
# Load Model
# --------------------------------------------------

@st.cache_resource
def load_model():
    os.makedirs("models", exist_ok=True)
    model_path = "models/fraud_pipeline.pkl"
    if not os.path.exists("models/fraud_pipeline.pkl"):
        url = "https://drive.google.com/uc?id=16jiwOQ3EFYnageWiS64WIIoVzkUUjgbS"
        gdown.download(url, model_path, quiet=False)
    model = joblib.load(model_path)
    return model

model = load_model()

# --------------------------------------------------
# Upload Dataset
# --------------------------------------------------

file = st.file_uploader("Upload Transaction Dataset", type=["csv"])

# --------------------------------------------------
# If Dataset Uploaded
# --------------------------------------------------

if file is not None:

    try:

        df = pd.read_csv(file)

        st.subheader("📄 Dataset Preview")
        st.dataframe(df.head())

        # --------------------------------------------------
        # Preprocessing
        # --------------------------------------------------

        numeric_df = df.select_dtypes(include=["number"])

        if "Class" in numeric_df.columns:
            numeric_df = numeric_df.drop("Class", axis=1)

        numeric_df = numeric_df.fillna(0)

        # --------------------------------------------------
        # Model Prediction
        # --------------------------------------------------

        predictions = model.predict(numeric_df)
        probabilities = model.predict_proba(numeric_df)[:, 1]

        df["Fraud_Prediction"] = predictions
        df["Fraud_Probability"] = probabilities

        # --------------------------------------------------
        # Fraud Statistics
        # --------------------------------------------------

        total_transactions = len(df)
        fraud_count = int(df["Fraud_Prediction"].sum())
        legit_count = total_transactions - fraud_count
        fraud_rate = (fraud_count / total_transactions) * 100

        st.subheader("📊 Key Information")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Transactions", total_transactions)
        col2.metric("Fraud Transactions", fraud_count)
        col3.metric("Legitimate Transactions", legit_count)
        col4.metric("Fraud Rate (%)", round(fraud_rate, 2))

        # --------------------------------------------------
        # Fraud Gauge Meter
        # --------------------------------------------------

        st.subheader("🚨 Fraud Risk Gauge")

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=fraud_rate,
            title={'text': "Fraud Percentage"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "red"},
                'steps': [
                    {'range': [0, 20], 'color': "green"},
                    {'range': [20, 50], 'color': "yellow"},
                    {'range': [50, 100], 'color': "red"}
                ],
            }
        ))

        st.plotly_chart(gauge, use_container_width=True)

        # --------------------------------------------------
        # Fraud vs Legit Distribution
        # --------------------------------------------------

        st.subheader("📊 Fraud vs Legit Transactions")

        pie = px.pie(
            df,
            names="Fraud_Prediction",
            title="Transaction Distribution",
            color="Fraud_Prediction",
            color_discrete_map={0: "light blue", 1: "red"}
        )

        st.plotly_chart(pie, use_container_width=True)

        # --------------------------------------------------
        # Fraud Probability Histogram
        # --------------------------------------------------

        st.subheader("📈 Fraud Probability Distribution")

        hist = px.histogram(
            df,
            x="Fraud_Probability",
            nbins=50,
            title="Fraud Probability Distribution"
        )

        st.plotly_chart(hist, use_container_width=True)

        # --------------------------------------------------
        # Amount vs Fraud Chart
        # --------------------------------------------------

        if "Amount" in df.columns:

            st.subheader("💰 Transaction Amount vs Fraud")

            box = px.box(
                df,
                x="Fraud_Prediction",
                y="Amount",
                title="Amount vs Fraud"
            )

            st.plotly_chart(box, use_container_width=True)

        # --------------------------------------------------
        # Top Suspicious Fraud Amounts
        # --------------------------------------------------

        if "Amount" in df.columns:

            st.subheader("🚨 Top Suspicious Fraud Amounts")

            fraud_only = df[df["Fraud_Prediction"] == 1]

            if len(fraud_only) > 0:

                top_fraud = fraud_only.sort_values(
                    by="Amount",
                    ascending=False
                ).head(10)

                bar = px.bar(
                    top_fraud,
                    x=top_fraud.index,
                    y="Amount",
                    color="Amount",
                    title="Top 10 Suspicious Fraud Transactions"
                )

                st.plotly_chart(bar, use_container_width=True)

            else:
                st.info("No fraud transactions available.")

        # --------------------------------------------------
        # Live Fraud Alert System
        # --------------------------------------------------

        st.subheader("🚨 Live Fraud Alerts")

        fraud_alerts = df[df["Fraud_Prediction"] == 1]

        if len(fraud_alerts) == 0:

            st.success("✅ No fraud alerts detected.")

        else:

            for i, row in fraud_alerts.head(5).iterrows():

                amount = row["Amount"] if "Amount" in row else "Unknown"

                st.error(
                    f"⚠️ FRAUD ALERT → Transaction {i} | Amount: ₹{amount} | Fraud Probability: {round(row['Fraud_Probability'],2)}"
                )

        # --------------------------------------------------
        # Fraud Transactions Table
        # --------------------------------------------------

        st.subheader("🚨 Detected Fraud Transactions")

        fraud_df = df[df["Fraud_Prediction"] == 1]

        if len(fraud_df) == 0:
            st.success("✅ No fraud detected in this dataset.")
        else:
            st.error(f"⚠️ {len(fraud_df)} fraudulent transactions detected!")
            st.dataframe(fraud_df)

    except Exception as e:

        st.error(f"Error processing dataset: {e}")

# --------------------------------------------------
# If No Dataset Uploaded
# --------------------------------------------------

else:

    st.info("📂 Upload a CSV dataset to start fraud detection.")