import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="DrivenG - Car Predictor",
    page_icon="🚗",
    layout="centered"
)

# ----------------------------
# LOAD MODEL
# ----------------------------
model = joblib.load("car_model.joblib")

# ----------------------------
# CUSTOM STYLING
# ----------------------------
st.markdown(
    """
    <style>
        .main {
            background-color: #0f172a;
        }

        h1 {
            color: black;
            text-align: center;
            font-size: 50px;
        }

        h3 {
            color: black;
            text-align: center;
        }

        .stButton>button {
            width: 100%;
            background: #2563eb;
            color: white;
            border-radius: 10px;
            height: 50px;
            font-size: 18px;
            border: none;
        }

        .prediction-box {
            padding: 20px;
            background: #1e293b;
            border-radius: 12px;
            text-align: center;
            color: white;
            font-size: 28px;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# HEADER
# ----------------------------
st.markdown("<h1>🚘 DriveValuenG</h1>", unsafe_allow_html=True)
st.markdown("<h3>Estimated Car Price Predictor</h3>", unsafe_allow_html=True)

st.write(" Enter the car details below to estimate its market value in Nigeria")

# ----------------------------
# INPUT FORM
# ----------------------------
with st.form("prediction_form"):

    make = st.text_input("Car Make", placeholder="Toyota")

    model_name = st.text_input("Car Model", placeholder="Camry")

    fuel_type = st.selectbox(
        "Fuel Type",
        ["Petrol", "Diesel", "Electric", "Hybrid"]
    )

    gear_type = st.selectbox(
        "Gear Type",
        ["Automatic", "Manual"]
    )

    condition = st.selectbox(
        "Condition",
        ["Foreign Used", "Nigerian Used", "Brand New"]
    )

    mileage = st.number_input(
        "Mileage",
        min_value=0.0,
        step=1000.0
    )

    engine_size = st.number_input(
        "Engine Size",
        min_value=0.0,
        step=0.1
    )

    selling_condition = st.selectbox(
        "Selling Condition",
        ["Clean", "Accidented", "Refurbished"]
    )

    bought_condition = st.selectbox(
        "Bought Condition",
        ["New", "Used"]
    )

    car_age = st.number_input(
        "Car Age",
        min_value=0,
        max_value=50,
        step=1
    )

    submit_button = st.form_submit_button("Predict Price")

# ----------------------------
# PREDICTION
# ----------------------------
if submit_button:

    input_data = pd.DataFrame({
        "Make": [make],
        "Model": [model_name],
        "fuel type": [fuel_type],
        "gear type": [gear_type],
        "Condition": [condition],
        "Mileage": [mileage],
        "Engine Size": [engine_size],
        "Selling Condition": [selling_condition],
        "Bought Condition": [bought_condition],
        "Car Age": [car_age]
    })

    try:
        prediction = model.predict(input_data)[0]

        st.markdown(
            f"""
            <div class="prediction-box">
                Estimated Car Price<br><br>
                ₦{prediction:,.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")

# ----------------------------
# FOOTER
# ----------------------------
st.write("")
st.caption("DrivenG • Smart Car Valuation System")
