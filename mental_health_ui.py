import streamlit as st
import joblib
import pandas as pd
import google.generativeai as genai

# Load the trained model
model = joblib.load("mental_health_model.pkl")

# Configure Gemini API
genai.configure(api_key="API_KEY")  # Replace with your Gemini API key

# Initialize Gemini model
gemini_model = genai.GenerativeModel("gemini-pro")

# Title
st.title("Mental Health Condition Predictor")

# Input fields
st.sidebar.header("Input Features")
age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=30)
gender = st.sidebar.selectbox("Gender", [0, 1, 2], format_func=lambda x: ["Female", "Male", "Other"][x])
self_employed = st.sidebar.selectbox("Self-employed", [0, 1], format_func=lambda x: ["No", "Yes"][x])
family_history = st.sidebar.selectbox("Family History", [0, 1], format_func=lambda x: ["No", "Yes"][x])
work_interfere = st.sidebar.selectbox("Work Interference", [0, 1, 2, 3], format_func=lambda x: ["Never", "Rarely", "Sometimes", "Often"][x])
no_employees = st.sidebar.selectbox("Number of Employees at Work", [0, 1, 2, 3, 4, 5], format_func=lambda x: ["1-5", "6-25", "26-100", "100-500", "500-1000", "More than 1000"][x])
remote_work = st.sidebar.selectbox("Remote Work", [0, 1], format_func=lambda x: ["No", "Yes"][x])
tech_company = st.sidebar.selectbox("Tech Company", [0, 1], format_func=lambda x: ["No", "Yes"][x])
benefits = st.sidebar.selectbox("Benefits at Comany", [0, 1, 2], format_func=lambda x: ["No", "Yes", "Don't know"][x])
care_options = st.sidebar.selectbox("Self Care Options", [0, 1, 2], format_func=lambda x: ["No", "I do", "Not sure"][x])
wellness_program = st.sidebar.selectbox("Wellness Program", [0, 1, 2], format_func=lambda x: ["No", "Yes", "Don't know"][x])
seek_help = st.sidebar.selectbox("Seek Help", [0, 1, 2], format_func=lambda x: ["No", "Yes", "Don't know"][x])
anonymity = st.sidebar.selectbox("Anonymity in Life", [0, 1, 2], format_func=lambda x: ["No", "Yes", "Don't know"][x])
leave = st.sidebar.selectbox("Work Leave", [0, 1, 2, 3, 4], format_func=lambda x: ["Very difficult", "Somewhat difficult", "Don't know", "Somewhat easy", "Very easy"][x])
mental_health_consequence = st.sidebar.selectbox("Mental Health Consequence", [0, 1, 2], format_func=lambda x: ["Not Good", "Good", "Dont Know"][x])
phys_health_consequence = st.sidebar.selectbox("Physical Health Consequence", [0, 1, 2], format_func=lambda x: ["No", "Yes", "Maybe"][x])
coworkers = st.sidebar.selectbox("Coworkers at Work", [0, 1, 2], format_func=lambda x: ["No", "Yes", "Some of them"][x])
supervisor = st.sidebar.selectbox("Supervisor", [0, 1, 2], format_func=lambda x: ["No", "Yes", "Some of them"][x])
mental_health_interview = st.sidebar.selectbox("Mental Health Interview", [0, 1, 2], format_func=lambda x: ["No", "Yes", "Maybe"][x])
phys_health_interview = st.sidebar.selectbox("Physical Health Interview", [0, 1, 2], format_func=lambda x: ["No", "Yes", "Maybe"][x])
mental_vs_physical = st.sidebar.selectbox("Mental vs Physical", [0, 1, 2], format_func=lambda x: ["No", "Yes", "Don't know"][x])
obs_consequence = st.sidebar.selectbox("Observed Consequence", [0, 1], format_func=lambda x: ["No", "Yes"][x])
age_range = st.sidebar.selectbox("Age Range", [0, 1, 2, 3], format_func=lambda x: ["<20", "20-30", "30-40", "40+"][x])

# Prepare input data
input_data = {
    "Age": age,
    "Gender": gender,
    "self_employed": self_employed,
    "family_history": family_history,
    "work_interfere": work_interfere,
    "no_employees": no_employees,
    "remote_work": remote_work,
    "tech_company": tech_company,
    "benefits": benefits,
    "care_options": care_options,
    "wellness_program": wellness_program,
    "seek_help": seek_help,
    "anonymity": anonymity,
    "leave": leave,
    "mental_health_consequence": mental_health_consequence,
    "phys_health_consequence": phys_health_consequence,
    "coworkers": coworkers,
    "supervisor": supervisor,
    "mental_health_interview": mental_health_interview,
    "phys_health_interview": phys_health_interview,
    "mental_vs_physical": mental_vs_physical,
    "obs_consequence": obs_consequence,
    "age_range": age_range
}

# Function to generate explanations and coping mechanisms using Gemini
def generate_explanation_and_coping(prediction):
    prompt = f"""
    The user has been predicted to be {prediction} for mental health treatment. 
    Provide a natural language explanation for this prediction and suggest coping mechanisms or next steps.
    """
    response = gemini_model.generate_content(prompt)
    return response.text

# Make prediction
if st.sidebar.button("Predict"):
    result = model.predict(pd.DataFrame([input_data]))
    prediction = "Likely to seek treatment" if result[0] == 1 else "Unlikely to seek treatment"
    st.write("Prediction:", prediction)

    # Generate explanation and coping mechanisms
    explanation = generate_explanation_and_coping(prediction)
    st.write("\nExplanation and Coping Mechanisms:")
    st.write(explanation)