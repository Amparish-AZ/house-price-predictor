# house-price-predictor
🏡 House Price Predictor – Project Summary
🔍 Project Objective:
To build a machine learning model that predicts house prices based on input features like location, square footage, number of bedrooms and bathrooms, etc.

✅ Steps We Followed:
Dataset Preparation

We used a housing dataset (with locations in Germany) that included features such as area, BHK, bathrooms, and location.

Data was cleaned and preprocessed for model training.

Model Training

A Random Forest Regression model was trained on the dataset.

The trained model was saved as a file named rf_model.pkl.

App Interface (Frontend)

We developed a Streamlit-based web application (app.py) where users can input house details.

The app takes input features like:

📍 Location

🛏️ Number of Bedrooms

🚿 Number of Bathrooms

📏 Total Square Feet

On submission, the app displays the predicted house price.

Dependency Management

All required Python libraries (such as streamlit, pandas, scikit-learn, etc.) were listed in the requirements.txt file for smooth deployment.

Replit Setup

The project was tested and debugged in Replit.

We faced some environment compatibility issues (due to joblib and numpy version mismatch), which we documented and handled manually.

GitHub Upload

We created a GitHub repository.

Uploaded the following files:

app.py (Streamlit frontend)

rf_model.pkl (trained model)

requirements.txt (list of Python dependencies)
