import streamlit as st
import pickle
import pandas as pd
import os

st.set_page_config(page_title="💎 Diamond Price Predictor", layout="wide")

# -----------------------------------------------------------------------------
# 2. CUSTOM CSS
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# 2. CUSTOM CSS
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# 2. CUSTOM CSS
# -----------------------------------------------------------------------------
def load_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Lato:wght@400;700&display=swap');
        
        /* --- Body with Radial Gradient --- */
        html, body, [class*="st-"] {
            font-family: 'Lato', sans-serif;
            color: #F5F5F5;
            background-color: #0E1117;
            background-image: radial-gradient(circle at top, #00284d 0%, #0E1117 40%);
            background-attachment: fixed;
        }
        }
        h1, h2, h3 {
            font-family: 'Montserrat', sans-serif;
        }
        
        /* --- Main Predict Button --- */
        .stButton > button {
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            color: #FFFFFF;
            background: linear-gradient(45deg, #1a8dff, #007BFF);
            border: none; border-radius: 12px; padding: 12px 30px;
            box-shadow: 0 4px 15px rgba(0, 123, 255, 0.2);
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 123, 255, 0.4);
        }
        .stButton > button * {
            background: transparent !important;
            color: #FFFFFF !important;
        }

        /* --- FIX FOR NUMBER INPUT BUTTONS --- */
        button[data-testid="stNumberInput-StepUp"]:hover,
        button[data-testid="stNumberInput-StepDown"]:hover {
            transform: none !important;
            box-shadow: none !important;
            background-color: #007BFF;
        }

        /* --- METRIC BOX --- */
        .st-emotion-cache-1g6goon {
            background-color: rgba(0, 123, 255, 0.1);
            border: 1px solid #007BFF;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
        }
        
        /* --- POINTER CURSOR FOR DROPDOWNS (Corrected) --- */
        [data-testid="stSelectbox"] * {
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

load_css()

model_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'diamond_price_model.pkl')
data_path = os.path.join(os.path.dirname(__file__), '..', 'diamonds.csv')

try:
    pipeline = pickle.load(open(model_path, "rb"))
    df = pd.read_csv(data_path)
except FileNotFoundError as e:
    st.error(f"Error loading files: {e}.")
    st.stop()

st.title("💎 Diamond Price Prediction System")
st.markdown("Predict the price of a diamond by entering its features below.")
st.divider()
st.subheader("Diamond Features")

col1, col2, col3 = st.columns(3)
with col1:
    carat = st.number_input("Carat", min_value=float(df['carat'].min()), max_value=float(df['carat'].max()), value=0.5, step=0.01)
    x = st.number_input("X (Length in mm)", min_value=float(df['x'].min()), max_value=float(df['x'].max()), value=5.1, step=0.01)
    cut = st.selectbox("Cut", ['Ideal', 'Premium', 'Good', 'Very Good', 'Fair'])
with col2:
    depth = st.number_input("Depth (%)", min_value=float(df['depth'].min()), max_value=float(df['depth'].max()), value=61.5, step=0.1)
    y = st.number_input("Y (Width in mm)", min_value=float(df['y'].min()), max_value=float(df['y'].max()), value=5.2, step=0.01)
    color = st.selectbox("Color", ['E', 'I', 'J', 'H', 'F', 'G', 'D'])
with col3:
    table = st.number_input("Table (%)", min_value=float(df['table'].min()), max_value=float(df['table'].max()), value=55.0, step=0.1)
    z = st.number_input("Z (Height in mm)", min_value=float(df['z'].min()), max_value=float(df['z'].max()), value=3.2, step=0.01)
    clarity = st.selectbox("Clarity", ['SI2', 'SI1', 'VS1', 'VS2', 'VVS2', 'VVS1', 'I1', 'IF'])

st.divider()

_, col_btn, _ = st.columns([2, 3, 2])
with col_btn:
    if st.button("Predict Diamond Price", type="primary", use_container_width=True):
        input_data = pd.DataFrame([{'carat': carat, 'depth': depth, 'table': table, 'x': x, 'y': y, 'z': z, 'cut': cut, 'color': color, 'clarity': clarity}])
        predicted_price = pipeline.predict(input_data)[0]
        st.metric(label="Predicted Price", value=f"${predicted_price:,.2f}")
        st.toast('Price predicted!', icon='💎')

# -----------------------------------------------------------------------------
# 5. FOOTER AND CREDITS
# -----------------------------------------------------------------------------
st.divider()

st.markdown("""
    <div style="text-align: center; font-size: small;">
        <p><strong>💎 Diamond Price Predictor</strong></p>
        <p>This app uses a machine learning model to predict diamond prices based on their characteristics.</p>
        <p><strong>Data Source:</strong> <a href="https://www.kaggle.com/datasets/shivam2503/diamonds" target="_blank">Kaggle</a> | <strong>Made by:</strong> Kartik Sharma</p>
    </div>
""", unsafe_allow_html=True)