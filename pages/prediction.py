import streamlit as st
import pickle

# Load the trained Naive Bayes classifier from the saved file
file = 'pages/sentimentAnalyzerTest_Model.sav'
loaded_model = pickle.load(open(file, 'rb'))    

st.title("Typhoon Analysis Predictor 🍃🌧☔💦")
st.subheader("⋆.ೃ࿔⛈ ˖*༄ Enter levels of different factors to determine the potential typhoon:")

# User inputs for different factors


wind_speed_input = st.slider("Wind Speed (km/h): ", 0, 100)
land_slope_input = st.slider("Land Slope (degrees): ", 0, 45)
vegetation_coverage_input = st.slider("Vegetation Coverage (%): ", 0, 100)
rainfall_input = st.slider("Rainfall Level (mm): ", 0, 500)
river_overflow_input = st.slider("River Water Level (m): ", 0, 10)
drainage_quality_input = st.slider("Drainage System Quality (1-10): ", 1, 10)
dam_condition_input = st.slider("Dam Integrity (1-10): ", 1, 10)

# Function to make a prediction
def predict_flood_cause(wind_speed, land_slope, vegetation_coverage, rainfall, river_overflow, drainage_quality, dam_condition):
    if rainfall == 0 and river_overflow == 0 and drainage_quality == 1 and dam_condition == 1:
        return "No significant factors entered."
    else:
        features = {
            'wind_speed': wind_speed,
            'land_slope': land_slope,
            'vegetation_coverage': vegetation_coverage,
            'rainfall': rainfall,
            'river_overflow': river_overflow,
            'drainage_quality': drainage_quality,
            'dam_condition': dam_condition
        }
        prediction = loaded_model.classify(features)
        return prediction

# Display button and result
if st.button('Predict Cause'):
    cause_of_flood = predict_flood_cause(wind_speed_input, land_slope_input, vegetation_coverage_input,rainfall_input, river_overflow_input, drainage_quality_input, dam_condition_input)
    st.write("Based on the input factors, the predicted cause of the flood is:")
    st.write(cause_of_flood)
