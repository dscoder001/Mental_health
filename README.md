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
  2. Handling irrelevant data.
  3. Encoded categorical features (e.g., Gender, Work Interference, Benefits, etc.).
  4. Split data into training and testing sets (75/25 split).

---

## 🤖 Model Selection and Training

- **Model Used:** A supervised learning classification model trained using **XGBoost**.
- **Rationale:** Chosen due to its high performance on tabular data, ability to handle missing values, and strong feature importance insights.
- **Evaluation Metrics:**
  - Accuracy: **82.22%**
  - Precision: **79.78%**
  - Recall: **88.48%**
  - F1-score: **83.91%**
  - ROC-AUC: **87.09%**

- **Best Hyperparameters:**
  ```json
  {
    "max_depth": 7,
    "learning_rate": 0.2,
    "subsample": 0.8,
    "colsample_bytree": 1.0,
    "gamma": 0,
    "objective": "binary:logistic",
    "eval_metric": "logloss",
    "seed": 42
  }
  ```
  - **Best Number of Boosting Rounds:** 100

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

[Click here to watch a Full Demo](#) *([Video Link](https://drive.google.com/file/d/1HHkMh4fsvaDPVDGToHKjByCfs_yd1GTz/view?usp=sharing))*




[User Interface](image.png)


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

