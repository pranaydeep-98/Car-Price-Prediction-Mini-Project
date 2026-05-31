import gradio as gr
import joblib

# Load model
model = joblib.load("models/car_price_model.pkl")

brand_encoder = joblib.load(
    "models/brand_encoder.pkl"
)

fuel_encoder = joblib.load(
    "models/fuel_encoder.pkl"
)

transmission_encoder = joblib.load(
    "models/transmission_encoder.pkl"
)


def predict_price(
    brand,
    vehicle_age,
    km_driven,
    fuel_type,
    transmission_type,
    mileage,
    engine,
    seats
):

    brand_encoded = brand_encoder.transform([brand])[0]

    fuel_encoded = fuel_encoder.transform(
        [fuel_type]
    )[0]

    transmission_encoded = transmission_encoder.transform(
        [transmission_type]
    )[0]

    input_data = [[
        brand_encoded,
        vehicle_age,
        km_driven,
        fuel_encoded,
        transmission_encoded,
        mileage,
        engine,
        seats
    ]]

    prediction = model.predict(input_data)

    return f"₹ {prediction[0]:,.2f}"


interface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Dropdown(
            choices=list(brand_encoder.classes_),
            label="Brand"
        ),
        gr.Number(label="Vehicle Age"),
        gr.Number(label="KM Driven"),
        gr.Dropdown(
            choices=list(fuel_encoder.classes_),
            label="Fuel Type"
        ),
        gr.Dropdown(
            choices=list(transmission_encoder.classes_),
            label="Transmission Type"
        ),
        gr.Number(label="Mileage"),
        gr.Number(label="Engine (CC)"),
        gr.Number(label="Seats")
    ],
    outputs=gr.Textbox(
        label="Predicted Price"
    ),
    title="Car Price Prediction System"
)

interface.launch()