import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model\mental_health_model.pkl")

# Function to predict mental health condition
def predict_mental_health(input_data):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    # Make prediction
    prediction = model.predict(input_df)
    return "Likely to seek treatment" if prediction[0] == 1 else "Unlikely to seek treatment"

# Example usage
if __name__ == "__main__":
    input_data = {
        "Age": 30,
        "Gender": 1,
        "self_employed": 0,
        "family_history": 1,
        "work_interfere": 2,
        "no_employees": 4,
        "remote_work": 1,
        "tech_company": 1,
        "benefits": 2,
        "care_options": 1,
        "wellness_program": 0,
        "seek_help": 1,
        "anonymity": 1,
        "leave": 2,
        "mental_health_consequence": 1,
        "phys_health_consequence": 0,
        "coworkers": 1,
        "supervisor": 1,
        "mental_health_interview": 1,
        "phys_health_interview": 0,
        "mental_vs_physical": 1,
        "obs_consequence": 0,
        "age_range": 2
    }
    result = predict_mental_health(input_data)
    print(result)
