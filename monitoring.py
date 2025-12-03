import streamlit as st

def run():

    st.title("Patient Management")

    st.metric("Total Patients", 8)
    st.metric("Stunting Cases", 3)
    st.metric("Normal Growth", 4)

    st.text_input("Search patients by name, ID, or location")

    st.subheader("Patient List")

    patients = [
        {"name": "Sari Dewi", "age": "18 months", "city": "Semarang", "status": "High Risk"},
        {"name": "Ahmad Rizki", "age": "24 months", "city": "Solo", "status": "Low Risk"},
    ]

    for p in patients:
        st.markdown(f"""
        **{p['name']}**  
        - Age: {p['age']}  
        - City: {p['city']}  
        - Status: **{p['status']}**
        """)
