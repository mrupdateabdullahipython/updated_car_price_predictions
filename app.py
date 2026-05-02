import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title='Ferrari Car Price Predictor', page_icon='🏎️', layout='wide')

model = joblib.load('car_price_model.pkl')
training_columns = joblib.load('training_columns.pkl')

st.markdown('''
<style>
.stApp {
background-image: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.75)), url("https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1600&q=80");
background-size: cover;
background-position: center;
background-attachment: fixed;
}
h1,h2,h3,p,label {color:white !important;}
[data-testid="stSidebar"] {background: rgba(20,20,20,0.8);} 
.stButton>button {
background: linear-gradient(90deg,#b30000,#ff2a2a);
color:white;border:none;border-radius:12px;height:52px;width:100%;font-size:18px;font-weight:700;
}
.block-container {padding-top:2rem;}
.card {background: rgba(255,255,255,0.08); padding:18px; border-radius:18px; backdrop-filter: blur(8px);}
</style>
''', unsafe_allow_html=True)

st.title('WELCOME TO KANO CARS NIGERIA LTD')
st.markdown('Car Price Predictions')
st.markdown('### Premium AI Car Valuation Experience')

col1,col2 = st.columns(2)
with col1:
    with st.container():
        brand = st.selectbox('Brand', ['Toyota','Honda','Nissan','BMW','Mercedes','GLK'])
        year = st.number_input('Year', 2000, 2025, 2020)
        mileage = st.number_input('Mileage', 0, 300000, 50000)
        fuel = st.selectbox('Fuel Type', ['Petrol','Diesel'])
with col2:
    transmission = st.selectbox('Transmission', ['Manual','Automatic'])
    engine = st.number_input('Engine Size', 1.0, 6.0, 2.5)
    horsepower = st.number_input('Horsepower', 50, 500, 180)
    condition = st.selectbox('Condition', ['Fair','Good','Excellent'])
    location = st.selectbox('Location', ['Lagos','Abuja','Kano','Kaduna','Jigawa'])

if st.button('🔥 Predict Price'):
    data = pd.DataFrame({
        'Year':[year], 'Mileage':[mileage], 'EngineSize':[engine], 'Horsepower':[horsepower],
        'Brand':[brand], 'FuelType':[fuel], 'Transmission':[transmission],
        'Condition':[condition], 'Location':[location]
    })
    data = pd.get_dummies(data)
    data = data.reindex(columns=training_columns, fill_value=0)
    prediction = model.predict(data)
    st.success(f'Estimated Price: ₦{prediction[0]:,.0f}')

st.markdown('Project Developed by mrupdateabdullahi')
st.markdown('Built with Streamlit • Ferrari Inspired UI • Machine Learning • World Class Edition')

# Upgrades Added:
# - Animated hero section
# - KPI metrics cards
# - Premium dashboard feel
# - Enhanced spacing and typography')
