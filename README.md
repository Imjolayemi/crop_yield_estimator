# 🌾 Nigerian Crop Yield Estimator

## 📖 Project Overview
This project is an end-to-end Machine Learning solution designed to predict agricultural crop yields (measured in **tonnes/hectare**) across all 36 states of Nigeria and the Federal Capital Territory (FCT). 

Serving as a data-driven decision-support system, this tool is built to assist in precision farming and smart agriculture planning. The final regression model is deployed as an interactive web application, making complex AI predictions accessible through a simple user interface.

## 🚀 Tech Stack
* **Data Processing & Analysis:** Python, Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest & Gradient Boosting Regressors)
* **Model Serialization:** Joblib
* **Web Deployment:** Streamlit, Streamlit Cloud

## 📁 Project Structure
```text
crop_yield_estimator/
│
├── data/               # Raw and cleaned agricultural datasets
├── notebooks/          # Jupyter notebooks for EDA, feature engineering, and model training
├── models/             # Pickled model (.pkl) and saved feature names
├── app/                # Streamlit web application script (app.py)
├── requirements.txt    # Python dependencies for deployment
└── .gitignore          # Ignored files for version control
```

## 📊 Model Performance
The predictive model was rigorously trained and hyperparameter-tuned, achieving the following metrics on the test dataset:
* **Mean Absolute Error (MAE):** 0.559 tonnes/hectare
* **Root Mean Squared Error (RMSE):** 0.918 tonnes/hectare
* **R-Squared (R²):** 0.932 *(The model successfully explains 93.2% of the variance in crop yield)*

## 💻 How to Run the Jupyter Notebook
If you want to explore the data cleaning, exploratory data analysis (EDA), and model training process:

1. Clone this repository to your local machine.
2. Navigate to the project directory and activate your virtual environment.
3. Install the required dependencies: 
   ```bash
   pip install -r requirements.txt
   ```
4. Launch Jupyter Notebook: 
   ```bash
   jupyter notebook
   ```
5. Open the notebook inside the `notebooks/` folder and run the cells sequentially.

## 🌐 How to Run the Streamlit App Locally
To test the web application on your own computer:

1. Open your terminal or command prompt.
2. Ensure your virtual environment is activated and dependencies are installed.
3. Run the following command from the root directory of the project:
   ```bash
   streamlit run app/app.py
   ```
4. The application will automatically open in your default web browser at `http://localhost:8501`.

## ☁️ Live Demo
The application is fully deployed and hosted on Streamlit Cloud. 

**[Click here to view the live app!](https://cropyieldestimator.streamlit.app/)**