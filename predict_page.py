import streamlit as st
import pickle
import numpy as np 
import pandas as pd

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]

def show_predict_page():
    st.title("Open Globe Visual Acuity Prediction")
    st.write("""### Please enter the following clinical information""")
    return 

show_predict_page()

age = st.slider("Age", 0, 100, 47)
time = st.slider("Time to Operating Room (minutes)", 0, 10000, 872, 15)
presenting_va = st.slider("Presenting Visual Acuity (LogMAR)", 0.00, 3.00, 1.91, 0.01)
last_follow_up = st.slider("Months to Last Follow-Up", 0, 200, 16)

sex = st.selectbox("Gender", ("Male", "Female"))
eye = st.selectbox("Eye", ("OD", "OS"))
rupture = st.selectbox("Rupture", ("No", "Yes"))
penetration = st.selectbox("Penetration", ("No", "Yes"))
perforation = st.selectbox("Perforation", ("No", "Yes"))
endophthalmitis = st.selectbox("Endophthalmitis (Y/N)", ("No", "Yes"))
retinal_detachment = st.selectbox("Retinal Detachment (Y/N)", ("No", "Yes"))
apd = st.selectbox("APD (Y/N)", ("No", "Yes"))
iofb = st.selectbox("IOFB (Y/N)", ("No", "Yes"))

zone_of_injury = st.radio("Zone of Injury", ("Zone I", "Zone II", "Zone III"))

lensectomy = st.selectbox("Lensectomy (Y/N)", ("No", "Yes"))
uveal_prolapse = st.selectbox("Uveal Prolapse (Y/N)", ("No", "Yes"))
white = st.selectbox("White", ("No", "Yes"))
black = st.selectbox("Black", ("No", "Yes"))
asian = st.selectbox("Asian", ("No", "Yes"))
indian = st.selectbox("Indian", ("No", "Yes"))
hawaiian = st.selectbox("Hawaiian", ("No", "Yes"))
hispanic = st.selectbox("Hispanic", ("No", "Yes"))
fall = st.selectbox("Fall", ("No", "Yes"))
projectile = st.selectbox("Projectile", ("No", "Yes"))
nail = st.selectbox("Nail", ("No", "Yes"))
blunt = st.selectbox("Blunt", ("No", "Yes"))
glass = st.selectbox("Glass", ("No", "Yes"))
assault = st.selectbox("Assault", ("No", "Yes"))
wood = st.selectbox("Wood", ("No", "Yes"))
mvc = st.selectbox("MVC", ("No", "Yes"))
wire = st.selectbox("Wire", ("No", "Yes"))
knife = st.selectbox("Knife", ("No", "Yes"))
metal = st.selectbox("Metal", ("No", "Yes"))

ok = st.button("Calculate Predicted Visual Acuity")
if ok:
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
    white_binary = 1 if white == "Yes" else 0
    black_binary = 1 if black == "Yes" else 0
    asian_binary = 1 if asian == "Yes" else 0
    indian_binary = 1 if indian == "Yes" else 0
    hawaiian_binary = 1 if hawaiian == "Yes" else 0
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
        lensectomy_binary, uveal_prolapse_binary, white_binary, black_binary,
        asian_binary, indian_binary, hawaiian_binary, hispanic_binary,
        fall_binary, projectile_binary, nail_binary, blunt_binary, glass_binary,
        assault_binary, wood_binary, mvc_binary, wire_binary, knife_binary,
        metal_binary
    ]
    X_array = np.array(X)
    names = [
        'Age at time of injury', 'Time to OR (minutes)',
        'Presenting VA', 'Months to Last Follow-up',
        'Sex', 'Eye', 'Rupture', 'Penetration', 'Perforation',
        'Endophthalmitis (Y/N)', 'Retinal Detachment (Y/N)',
        'APD (Y/N)', 'IOFB (Y/N)', 'Zone I', 'Zone II', 'Zone III',
        'Lensectomy (Y/N)', 'Uveal Prolapse (Y/N)', 'White', 'Black',
        'Asian', 'Indian', 'Hawaiian', 'Hispanic', 'Fall', 'Projectile',
        'Nail', 'Blunt', 'Glass', 'Assault', 'Wood', 'MVC', 'Wire',
        'Knife', 'Metal'
    ]

    df = pd.DataFrame([X], columns=names)
    final_va = regressor.predict(df)
    st.subheader(f"The estimated visual acuity is {final_va[0]:.2f} (LogMAR)")
