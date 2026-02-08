# 🚗 Car Price Prediction Using Machine Learning
This project predicts the selling price of a used car based on various features such as brand, vehicle age, kilometers driven, fuel type, transmission type, mileage, engine capacity, and number of seats.
It uses a Random Forest Regression model and provides an interactive web interface using Gradio.

## 📌 Project Features
Data preprocessing using Label Encoding
Machine learning model with RandomForestRegressor
Model evaluation using R² Score
Model and encoders saved using Joblib
Interactive web interface built with Gradio
Simple car price prediction system

## 🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
Gradio

## 📂 Dataset
Dataset used: CarDekho Dataset (cardekho_dataset.csv)
Note: Make sure this dataset file is present in your project folder before running the project.

## ⚙️ Installation
Clone the repository:
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction


## Install required libraries:
pip install pandas numpy scikit-learn joblib gradio
▶️ Running the Project
Run the Python script:
python app.py

After running, Gradio will generate a local or public link.
Open that link in your browser to use the app.

## 🧠 Input Parameters
The model takes the following inputs:
Brand
Vehicle Age (years)
Kilometers Driven
Fuel Type
Transmission Type
Mileage (km/l)
Engine Capacity (CC)
Number of Seats

## 📈 Output

Predicted car selling price in Indian Rupees (₹)

## ⚠️ Important Notes
Dataset must be present before running training code.
Prediction accuracy depends on dataset quality.
This project is mainly for learning and demonstration purposes.


📜 License

This project is created for educational purposes.
