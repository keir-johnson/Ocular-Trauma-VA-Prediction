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
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.write("""### Demographics:""")
st.markdown("---")

age = st.slider("Age", 0, 100, 47)

sex = ("Male", "Female")
sex_box = st.selectbox("Gender", sex)

race_options = ["White", "Black", "Asian", "Native American", "Hawaiian"]
race = st.selectbox("Race", race_options)
race_values = [int(race_option == race) for race_option in race_options]

hispanic = ("No", "Yes")
hispanic_box = st.selectbox("Hispanic", hispanic)

time = st.slider("Time to Operating Room (minutes)", 0, 10000, 872, 15)
presenting_va = st.slider("Presenting Visual Acuity (LogMAR)", 0.00, 3.00, 1.91, 0.01)
last_follow_up = 16
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

eye = ("OD", "OS")
eye_box = st.selectbox("Eye", eye)

rupture = ("No", "Yes")
rupture_box = st.selectbox("Rupture", rupture)

penetration = ("No", "Yes")
penetration_box = st.selectbox("Penetration", penetration)

perforation = ("No", "Yes")
perforation_box = st.selectbox("Perforation", perforation)

endophthalmitis = ("No", "Yes")
endophthalmitis_box = st.selectbox("Endophthalmitis (Y/N)", endophthalmitis)

retinal_detachment = ("No", "Yes")
retinal_detachment_box = st.selectbox("Retinal Detachment (Y/N)", retinal_detachment)

apd = ("No", "Yes")
apd_box = st.selectbox("APD (Y/N)", apd)

iofb = ("No", "Yes")
iofb_box = st.selectbox("IOFB (Y/N)", iofb)

zone_i = ("No", "Yes")
zone_i_box = st.selectbox("Zone I", zone_i)

zone_ii = ("No", "Yes")
zone_ii_box = st.selectbox("Zone II", zone_ii)

zone_iii = ("No", "Yes")
zone_iii_box = st.selectbox("Zone III", zone_iii)

lensectomy = ("No", "Yes")
lensectomy_box = st.selectbox("Lensectomy (Y/N)", lensectomy)

uveal_prolapse = ("No", "Yes")
uveal_prolapse_box = st.selectbox("Uveal Prolapse (Y/N)", uveal_prolapse)
"""
white = ("No", "Yes")
white_box = st.selectbox("White", white)

black = ("No", "Yes")
black_box = st.selectbox("Black", black)

asian = ("No", "Yes")
asian_box = st.selectbox("Asian", asian)

indian = ("No", "Yes")
indian_box = st.selectbox("Indian", indian)

hawaiian = ("No", "Yes")
hawaiian_box = st.selectbox("Hawaiian", hawaiian)
"""



fall = ("No", "Yes")
fall_box = st.selectbox("Fall", fall)

projectile = ("No", "Yes")
projectile_box = st.selectbox("Projectile", projectile)

nail = ("No", "Yes")
nail_box = st.selectbox("Nail", nail)

blunt = ("No", "Yes")
blunt_box = st.selectbox("Blunt", blunt)

glass = ("No", "Yes")
glass_box = st.selectbox("Glass", glass)

assault = ("No", "Yes")
assault_box = st.selectbox("Assault", assault)

wood = ("No", "Yes")
wood_box = st.selectbox("Wood", wood)

mvc = ("No", "Yes")
mvc_box = st.selectbox("MVC", mvc)

wire = ("No", "Yes")
wire_box = st.selectbox("Wire", wire)

knife = ("No", "Yes")
knife_box = st.selectbox("Knife", knife)

metal = ("No", "Yes")
metal_box = st.selectbox("Metal", metal)

ok = st.button("Calculate Predicted Visual Acuity")
if ok:

    if sex == "Male":
        sex_binary = 1
    else:
        sex_binary = 0

    if eye == "OD":
        eye_binary = 1
    else:
        eye_binary = 0

    if rupture == "Yes":
        rupture_binary = 1
    else:
        rupture_binary = 0

    if penetration == "Yes":
        penetration_binary = 1
    else:
        penetration_binary = 0

    if perforation == "Yes":
        perforation_binary = 1
    else:
        perforation_binary = 0

    if endophthalmitis == "Yes":
        endophthalmitis_binary = 1
    else:
        endophthalmitis_binary = 0

    if retinal_detachment == "Yes":
        retinal_detachment_binary = 1
    else:
        retinal_detachment_binary = 0

    if apd == "Yes":
        apd_binary = 1
    else:
        apd_binary = 0

    if iofb == "Yes":
        iofb_binary = 1
    else:
        iofb_binary = 0

    if zone_i == "Yes":
        zone_i_binary = 1
    else:
        zone_i_binary = 0

    if zone_ii == "Yes":
        zone_ii_binary = 1
    else:
        zone_ii_binary = 0

    if zone_iii == "Yes":
        zone_iii_binary = 1
    else:
        zone_iii_binary = 0

    if lensectomy == "Yes":
        lensectomy_binary = 1
    else:
        lensectomy_binary = 0

    if uveal_prolapse == "Yes":
        uveal_prolapse_binary = 1
    else:
        uveal_prolapse_binary = 0

    if race_options == "White":
        white_binary = 1
        black_binary = 0
        asian_binary = 0
        indian_binary = 0
        hawaiian_binary = 0
    elif race == "Black":
        white_binary = 0
        black_binary = 1
        asian_binary = 0
        indian_binary = 0
        hawaiian_binary = 0
    elif race == "Asian":
        white_binary = 0
        black_binary = 0
        asian_binary = 1
        indian_binary = 0
        hawaiian_binary = 0
    elif race == "Native American":
        white_binary = 0
        black_binary = 0
        asian_binary = 0
        indian_binary = 1
        hawaiian_binary = 0
    elif race == "Hawaiian":
        white_binary = 0
        black_binary = 0
        asian_binary = 0
        indian_binary = 0
        hawaiian_binary = 1

"""
    if white == "Yes":
        white_binary = 1
    else:
        white_binary = 0

    if black == "Yes":
        black_binary = 1
    else:
        black_binary = 0

    if asian == "Yes":
        asian_binary = 1
    else:
        asian_binary = 0

    if indian == "Yes":
        indian_binary = 1
    else:
        indian_binary = 0

    if hawaiian == "Yes":
        hawaiian_binary = 1
    else:
        hawaiian_binary = 0
"""


    if fall == "Yes":
        fall_binary = 1
    else:
        fall_binary = 0

    if projectile == "Yes":
        projectile_binary = 1
    else:
        projectile_binary = 0

    if nail == "Yes":
        nail_binary = 1
    else:
        nail_binary = 0

    if blunt == "Yes":
        blunt_binary = 1
    else:
        blunt_binary = 0

    if glass == "Yes":
        glass_binary = 1
    else:
        glass_binary = 0

    if assault == "Yes":
        assault_binary = 1
    else:
        assault_binary = 0

    if wood == "Yes":
        wood_binary = 1
    else:
        wood_binary = 0

    if mvc == "Yes":
        mvc_binary = 1
    else:
        mvc_binary = 0

    if wire == "Yes":
        wire_binary = 1
    else:
        wire_binary = 0

    if knife == "Yes":
        knife_binary = 1
    else:
        knife_binary = 0

    if metal == "Yes":
        metal_binary = 1
    else:
        metal_binary = 0
    X = [age, time, presenting_va, last_follow_up, sex_binary, eye_binary, rupture_binary, penetration_binary, perforation_binary, endophthalmitis_binary, retinal_detachment_binary, apd_binary, iofb_binary, zone_i_binary, zone_ii_binary, zone_iii_binary, lensectomy_binary, uveal_prolapse_binary, white_binary, black_binary, asian_binary, indian_binary, hawaiian_binary, hispanic_binary, fall_binary, projectile_binary, nail_binary, blunt_binary, glass_binary, assault_binary, wood_binary, mvc_binary, wire_binary, knife_binary, metal_binary]
    X_array = np.array(X)
    names = [
 #continuous inputs
    'Age at time of injury', 
    'Time to OR (minutes)',
   # 'Year to OR at MEE',
    'Presenting VA',
    'Months to Last Follow-up',
    #categorical inputs
    'Sex', 
    'Eye',     
    'Rupture', 
    'Penetration', 
    'Perforation', 
    'Endophthalmitis (Y/N)', 
    'Retinal Detachment (Y/N)', 
    'APD (Y/N)', 
    'IOFB (Y/N)',
    'Zone I',
    'Zone II',
    'Zone III',
    'Lensectomy (Y/N)',
    'Uveal Prolapse (Y/N)',
    'White',
    'Black',
    'Asian',
    'Indian',
    'Hawaiian',
    'Hispanic',
    'Fall',
    'Projectile',
    'Nail',
    'Blunt',
    'Glass',
    'Assault',
    'Wood',
    'MVC',
    'Wire',
    'Knife',
    'Metal']

    df = pd.DataFrame([X], columns=names);
    final_va = regressor.predict(df)
    st.subheader(f"The estimated visual acuity is {final_va[0]:.2f} (LogMAR)")
