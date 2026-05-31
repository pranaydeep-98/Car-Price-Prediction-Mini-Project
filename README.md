# Car Price Prediction System

## Overview

The Car Price Prediction System is a Machine Learning-based web application that predicts the selling price of a used car based on various features such as brand, vehicle age, kilometers driven, fuel type, transmission type, mileage, engine capacity, and number of seats.

The project uses a Random Forest Regressor model trained on the CarDekho dataset and provides an interactive user interface using Gradio.

---

## Features

- Predicts used car prices accurately using Machine Learning.
- User-friendly web interface built with Gradio.
- Trained using Random Forest Regression.
- Encodes categorical features automatically.
- Real-time prediction results.
- Model accuracy of approximately 92% (R² Score ≈ 0.92).

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Gradio
- Joblib

---

## Dataset

Dataset: CarDekho Used Car Dataset

Features used:

- Brand
- Vehicle Age
- KM Driven
- Fuel Type
- Transmission Type
- Mileage
- Engine Capacity
- Seats

Target Variable:

- Selling Price

---

## Project Structure

```text
CarPricePrediction/
│
├── app.py
├── train_model.py
├── cardekho_dataset.csv
├── requirements.txt
│
└── models/
    ├── car_price_model.pkl
    ├── brand_encoder.pkl
    ├── fuel_encoder.pkl
    └── transmission_encoder.pkl
```

---

## Model Training

The model is trained using the Random Forest Regressor algorithm.

Training steps:

1. Load dataset.
2. Preprocess data.
3. Encode categorical variables.
4. Split data into training and testing sets.
5. Train Random Forest model.
6. Evaluate model performance.
7. Save trained model and encoders.

Performance:

```text
R² Score: 0.922
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/car-price-prediction.git
```

### Navigate to Project Directory

```bash
cd car-price-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Train the Model

```bash
python train_model.py
```

This will generate:

```text
models/car_price_model.pkl
models/brand_encoder.pkl
models/fuel_encoder.pkl
models/transmission_encoder.pkl
```

---

## Run the Application

```bash
python app.py
```

After execution:

```text
Running on local URL:
http://127.0.0.1:7860
```

Open the URL in your browser.

---

## How It Works

1. User enters car details.
2. Input data is passed to the backend.
3. Categorical values are encoded.
4. The trained Random Forest model processes the input.
5. Predicted selling price is generated.
6. Result is displayed on the web interface.

---

## System Architecture

```text
User
 ↓
Gradio Frontend
 ↓
Prediction Function
 ↓
Feature Encoding
 ↓
Random Forest Model
 ↓
Predicted Car Price
 ↓
Result Display
```

---

## Future Enhancements

- Support additional car features.
- Deploy on cloud platforms.
- Add data visualization dashboards.
- Improve accuracy using advanced models.
- Include car model information for better predictions.

---

## License

This project is developed for educational and academic purposes.
