import streamlit as st
import numpy as np
import pickle

with open('model/model.pkl', 'rb') as file:
    log_reg = pickle.load(file)


def show_predict_page():
    st.title("             heart disease prediction")
    st.write("""###### we need some info before we can  predict heart disease risk""")

    Sex = {0: "Female", 1: "Male"}
    Race = {0: "American Indian/Alaskan Native", 1: "Asian", 2: "Black", 3: "Hispanic", 4: "Other", 5: "White"}
    Smoking = {0: "No", 1: "Yes"}
    AgeCategory = {0: "18-24", 1: "25-29", 2: "30-34", 3: "35-39", 4: "40-44", 5: "45-49", 6: "50-54", 7: "55-59",
                   8: "60-64", 9: "65-69", 10: "70-74",
                   11: "75-79", 12: "80 or older"}

    DiffWalking = {0: "No", 1: "Yes"}
    PhysicalActivity = {0: "No", 1: "Yes"}
    GenHealth = {0: "Excellent", 1: "Fair", 2: "Good", 3: "Poor", 4: "Very good"}

    Stroke = {0: "No", 1: "Yes"}
    Diabetic = {0: "No", 1: "No, borderline diabetes", 2: "Yes", 3: "Yes [during pregnancy]"}
    Asthma = {0: "No", 1: "Yes"}
    SkinCancer = {0: "No", 1: "Yes"}
    AlcoholDrinking = {0: "No", 1: "Yes"}
    KidneyDisease = {0: "No", 1: "Yes"}

    sex = st.selectbox("Gender", Sex.keys(), format_func=lambda x: Sex[x])
    race = st.selectbox("Race", Race.keys(), format_func=lambda x: Race[x])
    age_cat = st.select_slider("select your age category :", AgeCategory.keys(),
                               format_func=lambda x: AgeCategory[x])

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            ad = st.radio("Do you consume Alcohol ?", AlcoholDrinking.keys(), format_func=lambda x: AlcoholDrinking[x])
        with col2:
            smoking = st.radio("Do you  smoke ? ", Smoking.keys(), format_func=lambda x: Smoking[x])
        with col1:
            dw = st.radio("Do you have difficulties while walking ?", DiffWalking.keys(),
                          format_func=lambda x: DiffWalking[x])
        with col2:
            pha = st.radio("do you do physical activities ?", PhysicalActivity.keys(),
                           format_func=lambda x: PhysicalActivity[x])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            asthma = st.radio("Do you have Asthma ?", Asthma.keys(), format_func=lambda x: Asthma[x])

        with col2:
            stroke = st.radio("Do you ever had the stroke ? ", Stroke.keys(), format_func=lambda x: Stroke[x])

        with col1:
            db = st.radio("Are you diabetic ? ", Diabetic.keys(), format_func=lambda x: Diabetic[x])

        with col2:
            sc = st.radio("Do you have SkinCancer", SkinCancer.keys(), format_func=lambda x: SkinCancer[x])

        with col1:
            kd = st.radio("Do you have any kidney disease ?", KidneyDisease.keys(),
                          format_func=lambda x: KidneyDisease[x])

        with col2:
            gh = st.radio("Rate your general health", GenHealth.keys(), format_func=lambda x: GenHealth[x])

    with st.container():
        bmi = st.slider("what is your current BMI ?", 0.0, 100.0, 25.0, step=0.001)
        sleep = st.slider("How many hours do you sleep per day in average ? ?", 0, 24, 7)
        ph = st.slider("on last 30 days, how often you had physical health issue ?", 0, 30, 15)
        mh = st.slider("on last 30 days, how often you had mental health issue ?", 0, 30, 15)

    check = st.button("CHECk MY HEART")

    if check:
        user_input = (bmi, smoking, ad, stroke, ph, mh, dw, sex, age_cat, race, db, pha, gh, sleep, asthma, kd, sc)
        # test case 1 - user_input = (20.11, 1, 1, 1, 6, 0, 1, 0, 11, 5, 0, 0, 1, 12, 1, 1, 1)
        # test case 2 - user_input = (15, 1, 0, 0, 3.0, 0.0, 0, 0, 10, 5, 0, 0, 3, 10.0, 0, 0, 0)

        input_as_numpy = np.asarray(user_input)
        input_reshaped = input_as_numpy.reshape(1, -1)
        result = log_reg.predict(input_reshaped)
        if result == 1:
            st.write("Based on the your inputs above:")
            result = ('<p style="font-family:sans-serif; color:Red; font-size: 30px;"> You might at the HIGHER risk '
                      'of heart disease</p>')
            st.markdown(result, unsafe_allow_html=True)

            st.write("Please Call ---707 423 APPT--- to make an appointment with Cardiologist")
            # st.write("you selected ", user_input, "and result was: ", result) - Acceptance test
        elif result < 1:
            st.write("Based on the your inputs above:")
            result = ('<p style="font-family:sans-serif; color:Green; font-size: 20px;"> You seems to be at LOW risk '
                      'of heart disease</p>')
            st.markdown(result, unsafe_allow_html=True)
            # st.write("you selected ", user_input, "and result was: ", result)- Acceptance test
        else:
            st.write("unexpected error occurred")

            # st.write("you selected ", input_reshaped, "and result was: ", result) - Acceptance test
