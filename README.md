Alzheimer’s Disease Prediction Web App
📖 Overview

This project is a machine learning–based web application that predicts the likelihood of Alzheimer’s disease using patient information. The model is built using Support Vector Machine (SVM) and deployed with a Streamlit interface so that users can easily enter patient data and receive predictions in real time.

Alzheimer’s disease is a progressive neurodegenerative disorder and the most common cause of dementia worldwide. Early prediction and diagnosis can play a critical role in patient care, treatment planning, and improving quality of life.

✨ Features

✅ Predicts Alzheimer’s risk using clinical and demographic data

✅ Machine learning pipeline with data preprocessing and SVM model

✅ User-friendly Streamlit web interface for input and prediction

✅ Trained model saved and reloaded using .sav format

✅ Scalable project structure with datasets, training scripts, and documentation

📂 Project Structure
Alzheimer-Diseases-prediction-web-app/
│
├── Alzheimer prediction web app.py    # Streamlit app script
├── alzheimer_main.py                  # Training and preprocessing script
├── trained_model.sav                  # Pretrained ML model
├── alzheimer.csv / full data set.csv  # Dataset(s) used
├── predicting-alzheimer's-disease-a-machine-learning-project-on-dataset-analysis.pdf
│
└── README.md                          # Project documentation

⚙️ Installation
Prerequisites

Python 3.x

Libraries: pandas, numpy, scikit-learn, streamlit

Setup

Clone this repository:

git clone https://github.com/sanjaykumar258/Alzheimer-Diseases-prediction-web-app.git
cd Alzheimer-Diseases-prediction-web-app


Install dependencies:

pip install -r requirements.txt


(If requirements.txt is missing, manually install:)

pip install streamlit scikit-learn pandas numpy

🚀 Usage
1. Train the Model (optional)

If you want to retrain the model:

python alzheimer_main.py


This will preprocess data, train the model, and save it as trained_model.sav.

2. Run the Web App
streamlit run "Alzheimer prediction web app.py"

3. Open in Browser

Go to the provided local URL (e.g., http://localhost:8501) and input patient details to get predictions.

🧠 About Alzheimer’s Disease

Alzheimer’s disease is a degenerative brain disorder that destroys memory and cognitive skills, and eventually the ability to perform everyday tasks.

🔹 Symptoms

Memory loss and confusion

Difficulty in problem-solving and completing tasks

Trouble recognizing people, places, and times

Language difficulties

Mood and behavior changes

🔹 Causes & Risk Factors

Age: Most common after 65 years

Genetics: APOE ε4 allele increases risk

Family history of dementia

Brain changes: Beta-amyloid plaques & tau tangles

Lifestyle factors: Hypertension, obesity, diabetes, head trauma

🔹 Disease Progression

Mild (Early Stage): Forgetfulness, difficulty finding words

Moderate (Middle Stage): Confusion, personality changes, help needed for daily activities

Severe (Late Stage): Loss of communication, dependence on full-time care

🔹 Global Impact

Alzheimer’s is the leading cause of dementia, responsible for 60–70% of cases

More than 6 million people in the U.S. live with Alzheimer’s

Worldwide, dementia cases may exceed 150 million by 2050

(Sources: Alzheimer’s Association
, CDC
, Mayo Clinic
)

🎯 Project Rationale

Early diagnosis of Alzheimer’s can:

Help patients and families plan for care

Improve treatment effectiveness

Reduce healthcare costs

Support research into preventive strategies

This project demonstrates how machine learning can aid early detection by analyzing features like:

Age

Education level

Cognitive test scores (MMSE, CDR)

Brain volume measurements

🔧 Future Improvements

Add more ML models (Random Forest, XGBoost, Neural Networks)

Implement hyperparameter tuning for better accuracy

Visualize predictions with confusion matrices & ROC curves

Cloud deployment (Heroku, AWS, etc.)

Secure user authentication for patient privacy

📜 License

This project is open-source. You may choose to license it under MIT or another suitable license.

🤝 Contributions

Contributions are welcome!

Fork the repo

Create a feature branch

Submit a pull request

📚 References

Alzheimer’s Association – What is Alzheimer’s?

Mayo Clinic – Symptoms & Causes

CDC – About Alzheimer’s

Wikipedia – Alzheimer’s Disease
