# Load model and encoders
import joblib
import gradio as gr
import numpy as np
model = joblib.load('car_price_model.pkl')
fuel_type_encoder = joblib.load("fuel_encoder.pkl")
trans_encoder = joblib.load("trans_encoder.pkl")
brand_encoder = joblib.load("brand_encoder.pkl")

# Mappings
brand_map = {label: idx for idx, label in enumerate(brand_encoder.classes_)}
fuel_type_map = {label: idx for idx, label in enumerate(fuel_type_encoder.classes_)}
transmission_type_map = {label: idx for idx, label in enumerate(trans_encoder.classes_)}

def predict_price(brand, vehicle_age, km_driven, fuel_type, transmission_type, mileage, engine, seats):
    try:
        print("Inputs received from UI:")
        print(f"Brand: {brand}, Age: {vehicle_age}, KM: {km_driven}, Fuel: {fuel_type}, Trans: {transmission_type}, Mileage: {mileage}, Engine: {engine}, Seats: {seats}")

        brand_value = brand_map[brand]
        fuel_type_value = fuel_type_map[fuel_type]
        transmission_type_value = transmission_type_map[transmission_type]

        input_features = np.array([[brand_value, vehicle_age, km_driven, fuel_type_value, transmission_type_value, mileage, engine, seats]])
        
        print("Input to model:", input_features)

        predicted_price = model.predict(input_features)[0]
        print("Predicted Price:", predicted_price)

        return f"Predicted Price: ₹{predicted_price:,.2f}"
    except Exception as e:
        return f"Error: {e}"

demo = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Dropdown(list(brand_map.keys()), label="Brand"),
        gr.Number(label="Vehicle Age (in years)", value=5, minimum=0, maximum=50),
        gr.Number(label="Kilometers Driven", value=10000, minimum=0, maximum=500000),
        gr.Dropdown(list(fuel_type_map.keys()), label="Fuel Type"),
        gr.Dropdown(list(transmission_type_map.keys()), label="Transmission Type"),
        gr.Number(label="Mileage (in km/l)", value=15.0, minimum=0.0),
        gr.Number(label="Engine Capacity (in CC)", value=1200, minimum=500, maximum=5000),
        gr.Number(label="Number of Seats", value=5, minimum=2, maximum=7)
    ],
    outputs=gr.Textbox(label="Predicted Price"),
    title="Car Price Prediction",
    description="Enter car details to estimate its selling price."
)

demo.launch(share=True, debug=True)