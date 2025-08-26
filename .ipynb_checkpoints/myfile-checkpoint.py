import streamlit as st
import pickle
import numpy as np

# Load model
with open("project.pkl", "rb") as f:
    model = pickle.load(f)

# Title and description
st.title("🌸 Iris Flower Species Prediction")
st.write("Enter the flower's measurements below to predict its species:")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

# Predict button
if st.button("Predict Species"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]

    species_map = {0: "Setosa 🌺", 1: "Versicolor 🌿", 2: "Virginica 🌷"}
    st.success(f"The predicted species is: **{species_map[prediction]}**")
