import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the machine learning model and data
with open("saved_steps.pkl", "rb") as file:
    regressor = pickle.load(file)

# Function to preprocess the input and predict the visual acuity
def predict_visual_acuity(age, time, presenting_va, last_follow_up, sex, eye, rupture, penetration, perforation,
                          endophthalmitis, retinal_detachment, apd, iofb, zone_of_injury, lensectomy,
                          uveal_prolapse, race, fall, projectile, nail, blunt, glass, assault, wood,
                          mvc, wire, knife, metal):
    # Binary encoding
    sex_binary = 1 if sex == "Male" else 0
    eye_binary = 1 if eye == "OD" else 0
    rupture_binary = 1 if rupture == "Yes" else 0
    penetration_binary = 1 if penetration == "Yes" else 0
    perforation_binary = 1 if perforation == "Yes" else 0
    endophthalmitis_binary = 1 if endophthalmitis == "Yes" else 0
    retinal_detachment_binary = 1 if retinal_detachment == "Yes" else 0
    apd_binary = 1 if apd == "Yes" else 0
    iofb_binary = 1 if iofb == "Yes" else 0
    zone_i_binary = 1 if zone_of_injury == "Zone I" else 0
    zone_ii_binary = 1 if zone_of_injury == "Zone II" else 0
    zone_iii_binary = 1 if zone_of_injury == "Zone III" else 0
    lensectomy_binary = 1 if lensectomy == "Yes" else 0
    uveal_prolapse_binary = 1 if uveal_prolapse == "Yes" else 0
    white_binary = 1 if race == "White" else 0
    black_binary = 1 if race == "Black" else 0
    asian_binary = 1 if race == "Asian" else 0
    indian_binary = 1 if race == "Indian" else 0
    hawaiian_binary = 1 if race == "Hawaiian" else 0
    hispanic_binary = 1 if hispanic == "Yes" else 0
    fall_binary = 1 if fall == "Yes" else 0
    projectile_binary = 1 if projectile == "Yes" else 0
    nail_binary = 1 if nail == "Yes" else 0
    blunt_binary = 1 if blunt == "Yes" else 0
    glass_binary = 1 if glass == "Yes" else 0
    assault_binary = 1 if assault == "Yes" else 0
    wood_binary = 1 if wood == "Yes" else 0
    mvc_binary = 1 if mvc == "Yes" else 0
    wire_binary = 1 if wire == "Yes" else 0
    knife_binary = 1 if knife == "Yes" else 0
    metal_binary = 1 if metal == "Yes" else 0

    X = [
        age, time, presenting_va, last_follow_up, sex_binary, eye_binary,
        rupture_binary, penetration_binary, perforation_binary,
        endophthalmitis_binary, retinal_detachment_binary, apd_binary,
        iofb_binary, zone_i_binary, zone_ii_binary, zone_iii_binary,
        lensectomy_binary, uveal_prolapse_binary, white_binary,
        black_binary, asian_binary, indian_binary, hawaiian_binary,
        hispanic_binary, fall_binary, projectile_binary, nail_binary,
        blunt_binary, glass_binary, assault_binary, wood_binary,
        mvc_binary, wire_binary, knife_binary, metal_binary
    ]

    df = pd.DataFrame([X], columns=names)
    final_va = regressor.predict(df)
    return final_va[0]

# UI
st.title("Visual Acuity Prediction")
st.write("Enter the following details to predict the visual acuity:")

# User inputs
age = st.slider("Age", 0, 100, 47)
time = st.number_input("Time to Operating Room (minutes)", min_value=0, max_value=10000, value=30, step=1)
presenting_va = st.slider("Presenting Visual Acuity (LogMAR)", 0.00, 3.00, 1.91, 0.01)
last_follow_up = st.number_input("Time of Last Follow-up (in days)", min_value=0, max_value=365, value=30, step=1)
sex = st.selectbox("Sex", ["Male", "Female"])
eye = st.selectbox("Eye", ["OD", "OS"])
rupture = st.selectbox("Rupture", ["No", "Yes"])
penetration = st.selectbox("Penetration", ["No", "Yes"])
perforation = st.selectbox("Perforation", ["No", "Yes"])
endophthalmitis = st.selectbox("Endophthalmitis", ["No", "Yes"])
retinal_detachment = st.selectbox("Retinal Detachment", ["No", "Yes"])
apd = st.selectbox("Afferent Pupillary Defect (APD)", ["No", "Yes"])
iofb = st.selectbox("Intraocular Foreign Body (IOFB)", ["No", "Yes"])
zone_of_injury = st.selectbox("Zone of Injury", ["Zone I", "Zone II", "Zone III"])
lensectomy = st.selectbox("Lensectomy", ["No", "Yes"])
uveal_prolapse = st.selectbox("Uveal Prolapse", ["No", "Yes"])
race = st.selectbox("Race", ["White", "Black", "Asian", "Indian", "Hawaiian"])
fall = st.selectbox("Cause: Fall", ["No", "Yes"])
projectile = st.selectbox("Cause: Projectile", ["No", "Yes"])
nail = st.selectbox("Cause: Nail", ["No", "Yes"])
blunt = st.selectbox("Cause: Blunt", ["No", "Yes"])
glass = st.selectbox("Cause: Glass", ["No", "Yes"])
assault = st.selectbox("Cause: Assault", ["No", "Yes"])
wood = st.selectbox("Cause: Wood", ["No", "Yes"])
mvc = st.selectbox("Cause: MVC", ["No", "Yes"])
wire = st.selectbox("Cause: Wire", ["No", "Yes"])
knife = st.selectbox("Cause: Knife", ["No", "Yes"])
metal = st.selectbox("Cause: Metal", ["No", "Yes"])

if st.button("Predict"):
    final_va = predict_visual_acuity(age, time, presenting_va, last_follow_up, sex, eye, rupture, penetration, perforation,
                                     endophthalmitis, retinal_detachment, apd, iofb, zone_of_injury, lensectomy,
                                     uveal_prolapse, race, fall, projectile, nail, blunt, glass, assault, wood,
                                     mvc, wire, knife, metal)
    st.success("Predicted Visual Acuity: " + str(final_va))
