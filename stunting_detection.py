import streamlit as st
import pickle
import pandas as pd

def run():

    st.title("AI Stunting Detection")
    st.markdown("Enter child measurements for AI-powered stunting analysis.")

    # ---- Load model ----
    # Only load once by storing in session_state
    if "model" not in st.session_state:
        with open("model/model.pkl", "rb") as f:
            st.session_state.model = pickle.load(f)

    model = st.session_state.model

    # ---- Input Form ----
    with st.form("input_form"):
        col1, col2 = st.columns(2)

        with col1:
            umur = st.number_input("Age (months)", 1, 60)
            gender = st.selectbox("Gender", ["Male", "Female"])

        with col2:
            height = st.number_input("Height (cm)", 30.0, 130.0)
            weight = st.number_input("Weight (kg)", 2.0, 40.0)

        submitted = st.form_submit_button("Analyze")

    # ---- Prediction ----
    if submitted:
        df_input = pd.DataFrame({
            "Umur (bulan)": [umur],
            "Tinggi Badan (cm)": [height],
        })

        pred = model.predict(df_input)[0]

        if pred == 1:
            st.error("⚠️ The child is at **Stunting Risk**.")
        else:
            st.success("✅ The child is **Not Stunted**.")
