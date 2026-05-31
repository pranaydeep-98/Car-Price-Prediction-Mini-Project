import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("cardekho_dataset.csv")

# Encoders
brand_encoder = LabelEncoder()
fuel_encoder = LabelEncoder()
transmission_encoder = LabelEncoder()

df["brand"] = brand_encoder.fit_transform(df["brand"])
df["fuel_type"] = fuel_encoder.fit_transform(df["fuel_type"])
df["transmission_type"] = transmission_encoder.fit_transform(df["transmission_type"])

# Drop model column
if "model" in df.columns:
    df = df.drop("model", axis=1)

# Features and target
X = df.drop("selling_price", axis=1)
y = df["selling_price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)

print("R2 Score:", r2_score(y_test, predictions))

# Save model
joblib.dump(model, "models/car_price_model.pkl")
joblib.dump(brand_encoder, "models/brand_encoder.pkl")
joblib.dump(fuel_encoder, "models/fuel_encoder.pkl")
joblib.dump(transmission_encoder, "models/transmission_encoder.pkl")

print("Model saved successfully.")