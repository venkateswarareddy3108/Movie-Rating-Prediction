import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open(r"C:\Users\venkateswara reddy\Downloads\random_forest.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit UI
st.title("IMDb Movie Rating Predictor 🎬")
st.write("Enter movie details to predict its IMDb rating.")

# Input fields
year = st.number_input("Year of Release", min_value=1900, max_value=2025, step=1)
duration = st.number_input("Duration (minutes)", min_value=30, max_value=300, step=1)
votes = st.number_input("Votes Count", min_value=0, step=1000)

# New features added
director_avg_rating = st.number_input("Director's Average Rating", min_value=1.0, max_value=10.0, step=0.1)
actor1_avg_rating = st.number_input("Lead Actor 1's Average Rating", min_value=1.0, max_value=10.0, step=0.1)
actor2_avg_rating = st.number_input("Lead Actor 2's Average Rating", min_value=1.0, max_value=10.0, step=0.1)
actor3_avg_rating = st.number_input("Lead Actor 3's Average Rating", min_value=1.0, max_value=10.0, step=0.1)
genre_avg_rating = st.number_input("Genre's Average Rating", min_value=1.0, max_value=10.0, step=0.1)

# Predict button
if st.button("Predict IMDb Rating"):
    input_features = np.array([[year, duration, votes,
                                director_avg_rating, actor1_avg_rating,
                                actor2_avg_rating, actor3_avg_rating,
                                genre_avg_rating]])

    predicted_rating = model.predict(input_features)[0]
    st.success(f"🎬 Predicted IMDb Rating: {predicted_rating:.2f}")
