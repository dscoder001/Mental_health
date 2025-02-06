# Mental Health Condition Predictor

This project predicts whether a person is likely to seek mental health treatment based on various workplace and personal factors.

## 📂 Project Structure

```
├── mental_health_model.pkl   # Trained machine learning model
├── mental_health_ui.py       # Streamlit UI for user interaction
├── Model_testing.ipynb       # Jupyter notebook for model testing and evaluation
├── predict_mental_health.py  # CLI-based prediction script
├── README.md                 # Project documentation
├── survey.csv                # Dataset used for training the model
```

---

## 📊 Dataset and Preprocessing

- **Dataset:** The dataset (`survey.csv`) contains responses from individuals regarding their mental health conditions and workplace factors.
- **Preprocessing Steps:**
  1. Handled missing values.
  2. Encoded categorical features (e.g., Gender, Work Interference, Benefits, etc.).
  3. Normalized numerical features (e.g., Age).
  4. Split data into training and testing sets (80/20 split).

---

## 🤖 Model Selection and Training

- **Model Used:** A supervised learning classification model trained using **Logistic Regression** (or the actual model used if different).
- **Rationale:** Chosen due to its interpretability, effectiveness on structured data, and ability to handle categorical variables efficiently.
- **Evaluation Metrics:**
  - Accuracy: **X%**
  - Precision: **X%**
  - Recall: **X%**
  - F1-score: **X%** (Replace with actual values after evaluation)

---

## 🚀 Running the Inference Script

### 1️⃣ Running via Command Line (CLI)
```bash
python predict_mental_health.py --age 30 --gender 1 --self_employed 0 --family_history 1 --work_interfere 2 ...
```
- Example Output:
  ```
  Prediction: Likely to seek treatment
  ```

### 2️⃣ Running via UI (Streamlit)
```bash
streamlit run mental_health_ui.py
```
- Open the web interface in the browser and input feature values.
- Click **Predict** to see results.

---

## 🎥 Video Demonstration

[Click here to watch a demo](#) *(Replace with actual video link after recording.)*

---

## 🛠 Dependencies

Ensure you have the following installed:
```bash
pip install -r requirements.txt
```

---

## 📌 Future Improvements
- Improve model accuracy with additional features.
- Add explainability using SHAP values.
- Enhance UI with interactive visualizations.

---

## 📩 Contact
For any questions, reach out via [dhimansaha37@gmail.com](mailto:your-email@example.com).

