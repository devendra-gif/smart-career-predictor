import streamlit as st
import pandas as pd
import pickle

# Load model and label encoder
model = pickle.load(open('career_model.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

st.title("🎓 Smart Career Predictor")
st.write("Fill in the fields to get your career recommendation:")

# Academic scores
math = st.slider("Mathematics Score", 0, 10, 5)
science = st.slider("Science Score", 0, 10, 5)
language = st.slider("Language Arts Score", 0, 10, 5)

# Cognitive skills
logical = st.slider("Logical Reasoning", 0, 10, 5)
critical = st.slider("Critical Thinking", 0, 10, 5)
analytical = st.slider("Analytical Ability", 0, 10, 5)
creativity = st.slider("Creativity", 0, 10, 5)
communication = st.slider("Communication", 0, 10, 5)
emotional = st.slider("Emotional Intelligence", 0, 10, 5)

# Personal info
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
school_type = st.selectbox("School Type", ["Public", "Private"])
socio_status = st.selectbox("Socioeconomic Status", ["Low", "Medium", "High"])
learning_style = st.selectbox("Learning Style", ["Visual", "Auditory", "Kinesthetic"])

# Manual encoding
gender_map = {"Male": 1, "Female": 0, "Other": 2}
school_map = {"Public": 0, "Private": 1}
status_map = {"Low": 0, "Medium": 1, "High": 2}
style_map = {"Visual": 0, "Auditory": 1, "Kinesthetic": 2}

# Build input data
input_dict = {
    'Age': 17,
    'Gender': gender_map[gender],
    'School_Type': school_map[school_type],
    'Socioeconomic_Status': status_map[socio_status],
    'Mathematics_Score': math,
    'Science_Score': science,
    'Language_Arts_Score': language,
    'Social_Studies_Score': 60,
    'Mathematics_Improvement': 1,
    'Science_Improvement': 1,
    'Language_Arts_Improvement': 1,
    'Social_Studies_Improvement': 1,
    'Logical_Reasoning': logical,
    'Critical_Thinking': critical,
    'Analytical_Ability': analytical,
    'Creativity': creativity,
    'Communication': communication,
    'Emotional_Intelligence': emotional,
    'Social_Skills': 5,
    'Leadership': 5,
    'Sports_Participation': 1,
    'Sports_Involvement': 5,
    'Arts_Participation': 1,
    'Arts_Involvement': 5,
    'Music_Participation': 1,
    'Music_Involvement': 5,
    'Science_Club_Participation': 1,
    'Science_Club_Involvement': 5,
    'Debate_Participation': 1,
    'Debate_Involvement': 5,
    'Community_Service_Participation': 1,
    'Community_Service_Involvement': 5,
    'Learning_Style': style_map[learning_style],
    'STEM_Score': 50,
    'Business_Finance_Score': 50,
    'Arts_Media_Score': 50,
    'Healthcare_Score': 50,
    'Education_Score': 50,
    'Social_Services_Score': 50,
    'Trades_Manufacturing_Score': 50,
    'Government_Law_Score': 50,
    'Recommendation_Confidence': 0.8  # ✅ Fixed missing feature
}

# Convert to DataFrame
input_df = pd.DataFrame([input_dict])

# Prediction
if st.button("Predict Career"):
    prediction = model.predict(input_df)
    career = label_encoder.inverse_transform(prediction)[0]
    st.success(f"🎯 Recommended Career: **{career}**")
