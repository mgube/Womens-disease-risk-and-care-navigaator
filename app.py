
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import time
import folium
from streamlit_folium import st_folium
st.set_page_config(initial_sidebar_state='collapsed',layout="wide")


ost_model = pickle.load(open('savedModels/Osteoporosis.sav','rb'))
pcos_model = pickle.load(open('savedModels/Pcos.sav','rb'))
diab_model = pickle.load(open('savedModels/Diabetes.sav','rb'))
post_model = pickle.load(open('savedModels/Postnatal.sav','rb'))

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Disease Prediction", "Hospital Recommendation", "NGOs"])


with tab1:
    st.html("<h1 style='text-align: center; color: black; font-size: 60px; '>She Cares</h1> <style>.main{background-color:pink;}</style>")
    image_url = "women_health.png"  
    
    st.image(image_url, width=1600)

    st.html("<h1>About Us</h1><p style = 'font-size: 28px; text-align: justify;'>At Women's Disease Risk Assessment and Care Navigator, we are committed to addressing the critical health challenges faced by women in India. With a staggering female adult mortality rate in today's time , our mission is to make healthcare more accessible and effective. Many prevalent health issues such as Polycystic Ovary Syndrome (PCOS), osteoporosis, postpartum depression, and diabetes often go undetected due to ignorance, financial barriers, and societal stigmas. Our platform leverages advanced machine learning to assess and identify women at higher risk for these conditions, ensuring early detection and timely intervention. Through technology-driven insights, we aim to empower women to take charge of their health and overcome the barriers that hinder access to care.</p>")
    

with tab2:
    with st.sidebar:
        selected = option_menu('Menu',
                            ['PCOS Prediction',
                            'Diabetes Prediction',
                            'Postnatal Depression Prediction',
                            'Osteoporosis Prediction'],
                            default_index = 0)

    if(selected == "Osteoporosis Prediction"):
        st.title('Osteoporosis Prediction')

        col1, col2, col3 = st.columns(3)

        with col1:
            Age = st.text_input('Age (in years)')

        with col2:
            Gender = st.text_input('Gender (Female:0, Male:1)')
    
        with col3:
            Hormone = st.text_input('Harmonal Changes (Normal:0, Postmenopausal:1)')

        with col1:
            History = st.text_input('Family History (Yes:1, No:0)')

        with col2:
            Weight = st.text_input('Body Weight (Underweight:1, Normal:0)')
    
        with col3:
            pain = st.text_input('Pain (0.5:1, 1:2, 0:0)')

        with col1:
            muscle_strength = st.text_input('Loss in Muscle Strength (Not Active:1, Active:0)')

        with col2:
            Smoking = st.text_input('Smoking (Yes:1, No:0)')
    
        with col3:
            alcohol = st.text_input('Alcohol Consumption (Moderate:0, NA:1)')

        with col1:
            medical = st.text_input('Medical Conditions (Rheumatoid Arthritis:2, NA:1, Hyperthyroidism:0 )')

        with col2:
            steroids = st.text_input('Consumption of Steroids (Corticosteroids:0 , NA:1 )')
    
        with col3:
            Fractures = st.text_input('Prior Fractures (Yes:1, No:0)')

        osteo_diag = ''

        if st.button('Osteoporosis test'):
            user_input = [Age, Gender, Hormone, History, Weight, pain, muscle_strength, Smoking, alcohol, medical, steroids, Fractures]
            user_input = [float(x) for x in user_input]
            osteo_pred =ost_model.predict([user_input])
            #osteo_pred = ost_model.predict([[Age, Gender, Hormone, History, Weight, pain, muscle_strength, Smoking, alcohol, medical, steroids, Fractures]])

            if (osteo_pred[0]== 0):
                osteo_diag = 'The Person does not have a Osteoporosis'
                with st.spinner("Calculating..."):
                    time.sleep(2)

                st.success(osteo_diag)
            else:
                osteo_diag = 'The Person has Osteoporosis'
                with st.spinner("Calculating..."):
                    time.sleep(2)

                st.success(osteo_diag)
                st.html("<h2>Overview</h2>"
            "<p style='text-align:justify;'>Osteoporosis is a disease that weakens your bones. It makes your bones thinner and less dense than they should be. People with osteoporosis are much more likely to experience broken bones. Most people don’t know they have osteoporosis until it causes them to break a bone. Osteoporosis can make any of your bones more likely to break."
            "The sooner a healthcare provider diagnoses osteoporosis, the less likely you are to experience bone fractures. Ask a healthcare provider about checking your bone density, especially if you’re over 65, have had a bone fracture after age 50, or someone in your biological family has osteoporosis.</p>"
            "<h2>Treatment of osteoporosis at home-</h2>"
            "<ol><li>Intake of Calcium-rich food</li>"
            "<li>Vitamin D - Increase vitamin D intake through sunlight exposure, fatty fish (salmon, mackerel), egg yolks, and fortified foods</li>"
            "<li>Physical activities like weight-bearing Exercises</li>"
            "<li>Balance and Flexibility Exercises</li>"
            "<li>Avoid smoking and alcohol</li>"
            "<li>Achieving and maintaining a healthy weight can help protect bone health.</li>"
            "<li>Avoiding junk and processed food </li>"
            "<li>Sunlight exposure daily for vitamin D</li>"
            "<li>Stay hydrated</li>"
            "<li>Ensure adequate protein intake to support bone density, including lean meats, fish, eggs, and legumes.</li></ol>"
            "<h2>Symptoms of Osteoporosis</h2>"
            "<ol><li>Back pain</li>"
            "<li>Stooped Posture</li>"
            "<li>Changes in Bone Density</li>"
            "<li>Joint pain in the body</li>"
            "<li>Fragility Fractures that occur with minimal trauma, such as a fall from standing height. Like :-<ul><li>Wrist</li> <li>Hips</li> <li>Spine</li> <li>Knee</li><ul></li>"
            "<li>Low bone density</li></ol>"
            "<h2>Treatment and Remedies</h2>")
            # "<iframe src='https://youtu.be/BaJ7mGf2eys?feature=shared'></iframe>")
                VIDEO_DATA1="https://youtu.be/-B_hgebPKs0?si=6_2Wn14DM3LhkPl6"
                VIDEO_DATA2 ="https://youtu.be/s5by_uGGkX0?si=E5VxC3UAOtPr_TYr"
                VIDEO_DATA4 = "https://youtu.be/61QNcRuQRdE?si=kc8o0M8Fmqz_snii"
                VIDEO_DATA5 = "https://youtu.be/BaJ7mGf2eys?si=CIm9Yb--k5VnYeEt"
        
                width = max(50, 0.01)
                side = max((100 - width) / 2, 0.01)

                _, container, container2 ,_ = st.columns([side, width, width, side])
                container.video(data=VIDEO_DATA1)
                container2.video(data = VIDEO_DATA2)

                _, caption1, caption2,_ = st.columns([side, width, width, side])
                caption1.html("<h5>Diet plan for Osteoporosis</h5>")
                caption2.html("<h5>5 food to increase calcium level and bone density </h5>")

                _, container5, container6 ,_ = st.columns([side, width, width, side])
                container5.video(data=VIDEO_DATA4)
                container6.video(data = VIDEO_DATA5)

                _, caption5, caption6 ,_ = st.columns([side, width, width, side])
                caption5.html("<h5>Yoga, and food to strengthen bone naturally</h5>")
                caption6.html("<h5>4 exercise to do at home to strengthen bone </h5>")
                
    if(selected == "PCOS Prediction"):
        st.title('PCOS Prediction')

        col1, col2, col3 = st.columns(3)

        with col1:
            Age = st.text_input('Age (in years)')
        with col2:
            Weight = st.text_input('Weight (in kg)')
        with col3:
            Height = st.text_input('Height (in cms)')
        with col1:
            Blood_grp = st.text_input('Blood Group (A+ = 11, A- = 12, B+ = 13, B- = 14, O+ = 15, O- = 16, AB+ = 17, AB- = 18) ')
        with col2:
            After_months = st.text_input('After How many months you get periods?(Enter 1 if every month/regular)')
        with col3:
            Gained_wt = st.text_input('Have you gained weight (yes:1, no:0)')
        with col1:
            Hair_growth = st.text_input('Have Excessive hair growth (yes:1, no:0)')
        with col2:
            skin_dark = st.text_input('Skin Darkening (yes:1, no:0)')
        with col3:
            hair_loss = st.text_input('Hair loss (yes:1, no:0)')
        with col1:
            pimple = st.text_input('Pimples? (yes:1, no:0)')
        with col2:
            fast_food = st.text_input('Eat fast food? (yes:1, no:0)')
        with col3:
            exercise = st.text_input('Exercise?(yes:1, no:0)')
        with col1:
            mood_swings = st.text_input('Mood Swings?(yes:1, no:0)')
        with col2:
            regular_periods = st.text_input('Periods Regular?(yes:1, no:0)')
        with col3:
            period_last = st.text_input('Period last for? (in days)')

        pcos_diag = ''
        if st.button('PCOS test'):
            #pcos_pred = pcos_model.predict([[Age, Weight, Height, Blood_grp, After_months, Gained_wt, Hair_growth, skin_dark, hair_loss, pimple, fast_food, exercise, mood_swings, regular_periods, period_last]])
            user_input = [Age, Weight, Height, Blood_grp, After_months, Gained_wt, Hair_growth, skin_dark, hair_loss, pimple, fast_food, exercise, mood_swings, regular_periods, period_last]
            user_input = [float(x) for x in user_input]
            pcos_pred =pcos_model.predict([user_input])
            if (pcos_pred[0]== 0):
                pcos_diag = 'The Person does not have a PCOS'
                with st.spinner("Calculating..."):
                    time.sleep(2)
                st.success(pcos_diag)
            else:
                pcos_diag = 'The Person has PCOS'
                with st.spinner("Calculating..."):
                    time.sleep(2)

                st.success(pcos_diag)
                st.html("<h2>Overview</h2>"
                    "<p style='text-align:justify;'>Polycystic Ovary Syndrome (PCOS) is a hormonal disorder that affects people of reproductive age. It can lead to irregular menstrual cycles, weight gain, acne, and fertility issues. Many individuals may not realize they have PCOS until they face challenges related to these symptoms. Early diagnosis and management can significantly improve health outcomes and quality of life. If you experience symptoms such as irregular periods or excessive hair growth, consult a healthcare provider for evaluation and potential treatment options.</p>"
                    "<h2>Treatment of PCOS at home</h2>"
                    "<p>While medical treatment is often necessary for managing PCOS (Polycystic Ovary Syndrome), several home remedies can help alleviate symptoms and promote overall health. Here are some effective home remedies:</p>"
                    "<ol><li>Regular Physical Activity</li>"
                    "<li>Avoiding junk and preserved food</li>"
                    "<li>Meditation and yoga </li>"
                    "<li>Avoiding caffeine and soft drinks </li>"
                    "<li>Daily 7-8 hours of sleep </li>"
                    "<li>Iron-rich food </li>"
                    "<li>Low Glycemic Index Foods - Focus on whole grains, legumes, and vegetables that help regulate blood sugar levels.</li>"
                    "<li>Drink Plenty of Water</li>"
                    "<li>Keeping a diary of your symptoms, menstrual cycle, and lifestyle can help you identify patterns and triggers.</li>"
                    "<li>Herbal remedies- <ul><li>Cinnamon: Incorporating cinnamon into your diet may help improve insulin sensitivity. You can add it to smoothies, oatmeal, or yogurt.</li>"
                    "<li>Fenugreek Seeds: Soaking fenugreek seeds overnight and consuming them in the morning may help manage blood sugar levels and promote ovulation.</li></ul></li></ol>"
                    "<h2>Symptoms of PCOS</h2>"
                    "<ol><li>Irregular Menstrual Cycles</li>"
                    "<li>Excess Adrogen level</li>"
                    "<li>Weight gain</li>"
                    "<li>Difficulty with Pregnancy</li>"
                    "<li>Skin Changes</li>"
                    "<li>Mood swings</li>"
                    "<li>Excessive hair loss</li>"
                    "<li>Acne breakout</li>"
                    "<li>Unusual hair growth on the body</li>"
                    "<li>Ovarian cysts</li></ol>"
                    "<h2>Treatment and Remedies</h2>")
                
                VIDEO_DATA1="https://youtu.be/x3MVEwkIQro?si=0HzLzVQT80xSQ4EV "
                VIDEO_DATA2 ="https://youtu.be/-ZbEA_bqaDI?si=Ag74OroE8de9_iC4"
                VIDEO_DATA3 = "https://youtu.be/SSC12rZdU6M?si=XeJACKa3Vx1erbY7"
                VIDEO_DATA4 = "https://youtu.be/ppeZlSYOx5w?si=X35mbWQ_rQgKy_9j"
        
                width = max(50, 0.01)
                side = max((100 - width) / 2, 0.01)

                _, container, container2 ,_ = st.columns([side, width, width, side])
                container.video(data=VIDEO_DATA1)
                container2.video(data = VIDEO_DATA2)

                _, caption1, caption2,_ = st.columns([side, width, width, side])
                caption1.html("<h5>Full diet to cure PCOS at home</h5>")
                caption2.html("<h5>Food to avoid at PCOS  </h5>")

                _, container3, container4 ,_ = st.columns([side, width, width, side])
                container3.video(data=VIDEO_DATA3)
                container4.video(data = VIDEO_DATA4)

                _, caption3, caption4 ,_ = st.columns([side, width, width, side])
                caption3.html("<h5>Yoga to do at PCOS </h5>")
                caption4.html("<h5>Detox drink at PCOS</h5>")


    if(selected == "Diabetes Prediction"):
        st.title("Diabetes Prediction")

        col1, col2, col3 = st.columns(3)

        with col1:
            Age = st.text_input('Age (in years)')
        with col2:
            Gender = st.text_input('Gender (Male:1, Female:0)')
        with col3:
            Polyuria = st.text_input('Excessive urination (Yes:1, No:0)')
        with col1:
            Polydispia = st.text_input('Excessive thirst (Yes:1, No:0)')
        with col2:
            Weight_loss = st.text_input('Sudden weight loss (Yes:1, No:0)')
        with col3:
            Weakness = st.text_input('Weakness (Yes:1, No:0)')
        with col1:
            Polyphagia = st.text_input('Excessive hunger (Yes:1, No:0)')
        with col2:
            Genital_thrush = st.text_input('Discomfort at genital (Yes:1, No:0)')
        with col3:
            Visual_blurring = st.text_input('Visual Blurring (Yes:1, No:0)')
        with col1:
            Itching = st.text_input('Itching (Yes:1, No:0)')
        with col2:
            Irritability = st.text_input('Irritability (Yes:1, No:0)')
        with col3:
            Healing = st.text_input('Delayed healing (Yes:1, No:0)')
        with col1:
            Paresis = st.text_input('Difficulty in voluntary movements (Yes:1, No:0)')
        with col2:
            Muscle_stiffness = st.text_input('Muscle Stiffness (Yes:1, No:0)')
        with col3:
            Alopecia = st.text_input('Hair loss (Yes:1, No:0)')
        with col1:
            Obesity = st.text_input('Obesity (Yes:1, No:0)')

        diab_diag = ''
        if st.button('Diabetes test'):
            #pcos_pred = pcos_model.predict([[Age, Weight, Height, Blood_grp, After_months, Gained_wt, Hair_growth, skin_dark, hair_loss, pimple, fast_food, exercise, mood_swings, regular_periods, period_last]])
            user_input = [Age, Gender, Polyuria, Polydispia, Weight_loss, Weakness, Polyphagia, Genital_thrush, Visual_blurring, Itching, Irritability, Healing, Paresis, Muscle_stiffness, Alopecia, Obesity]
            user_input = [float(x) for x in user_input]
            diab_pred =diab_model.predict([user_input])
            if (diab_pred[0]== 0):
                diab_diag = 'The Person does not have a Diabetes'
                with st.spinner("Calculating..."):
                    time.sleep(2)
                st.success(diab_diag)
            else:
                diab_diag = 'The Person has Diabetes'
                with st.spinner("Calculating..."):
                    time.sleep(2)
                st.success(diab_diag)
                st.html("<h2>Overview</h2>"
                        "<p style='text-align:justify;'>Diabetes is a chronic condition that affects how your body processes blood sugar (glucose). It can lead to serious complications if not managed properly, including heart disease, kidney damage, and nerve problems. Many individuals with diabetes may be unaware of their condition until they experience significant health issues. Early diagnosis through blood sugar testing and regular check-ups is vital for effective management. If you have risk factors such as obesity or a family history of diabetes, talk to a healthcare provider about getting screened.</p>"
                        "<h2>Treatment of diabetes</h2>"
                        "<p>Diabetes treatment in women involves lifestyle changes, medication, and regular monitoring. Here are some key components tailored to women's needs:</p>"
                        "<ol><li>Avoiding junk food</li>"
                        "<li>Monitoring blood sugar level</li>"
                        "<li>Insulin injections </li>"
                        "<li>Regular Exercise, at least 150 minutes of moderate aerobic activity each week (e.g., walking, swimming)</li>"
                        "<li>Portion Control and practice portion control to avoid overeating</li>"
                        "<li>Balanced Meals focuses on whole foods, including fruits, vegetables, whole grains, lean proteins, and healthy fats.</li>"
                        "<li>Maintaining a healthy weight can improve insulin sensitivity and overall health.</li>"
                        "<li>Continuous Glucose Monitoring</li>"
                        "<li>Special Considerations for Women"
                        "<ul><li>Menstrual Cycle: Be aware that hormonal changes during menstruation can affect blood sugar levels.</li>"
                        "<li>Pregnancy: Women with diabetes should consult healthcare providers for preconception counseling and management during pregnancy to prevent gestational diabetes.</li></ul>"
                        "<li>Eating salad before a meal may reduce blood sugar levels.</li</ol>"
                        "<h2>Symptoms of Diabetes</h2>"
                        "<ol><li>Frequent Urination</li>"
                        "<li>Excessive Thirst</li>"
                        "<li>Increased hunger and cravings </li>"
                        "<li>Fatigue</li>"
                        "<li>Slow-healing sores or Cuts</li>"
                        "<li>Unexpected weight loss</li>"
                        "<li>Darkened Skin patches (acanthosis nigricans) may appear in body folds, such as the neck or armpits</li>"
                        "<li>Tingling or Numbness</li></ol>"
                        "<h2>Treatment and Remedies</h2>")
                
                VIDEO_DATA1="https://youtu.be/sOIREEp4254?si=K0RJqtRzGOK7ZRBJ"
                VIDEO_DATA2 ="https://youtu.be/wZaWPQNsOxE?si=O4zqAFAfjcN4cbHM "
                VIDEO_DATA3 ="https://youtu.be/rxyD8zs7fpw?si=zBjUA3CsKH97AxQl"
                VIDEO_DATA4 ="https://youtu.be/pcAqgQ5BLj0?si=xrDAS8O81VUnVrzU "
        
                width = max(50, 0.01)
                side = max((100 - width) / 2, 0.01)

                _, container, container2 ,_ = st.columns([side, width, width, side])
                container.video(data=VIDEO_DATA1)
                container2.video(data = VIDEO_DATA2)

                _, caption1, caption2,_ = st.columns([side, width, width, side])
                caption1.html("<h5>Drinks to control Diabetes</h5>")
                caption2.html("<h5>Effective solution</h5>")

                _, container3, container4 ,_ = st.columns([side, width, width, side])
                container3.video(data=VIDEO_DATA3)
                container4.video(data = VIDEO_DATA4)

                _, caption3, caption4 ,_ = st.columns([side, width, width, side])
                caption3.html("<h5>5food to reverse from diabetes</h5>")
                caption4.html("<h5>Diet plan to control Diabetes</h5>")

    if(selected == "Postnatal Depression Prediction"):
        st.title("Postnatal Depression Prediction")

        col1, col2, col3 = st.columns(3)

        with col1:
            Feeling_sad = st.text_input('Feeling sad or tearful (yes:1, no:0, sometimes:0.5)')
        with col2:
            Irritable = st.text_input('Irritable towards baby and partner (yes:1, no:0, sometimes:0.5)')
        with col3:
            Trouble_sleeping = st.text_input('Trouble sleeping at night (yes:1, no:0, two or more days a week:1.5)')
        with col1:
            Problem_concentrating = st.text_input('Problems concentrating and making decision (yes:1, no:0, often:0.5)')
        with col2:
            Overeating = st.text_input('Overeating or loss of appetite (yes:1, no:0, not at all:-1)')
        with col3:
            Anxious = st.text_input('Feeling anxious (yes:1, no:0)')
        with col1:
            Guilt = st.text_input('Feeling of guilt (yes:1, no:0, maybe:0.5)')
        with col2:
            Bond_with_baby = st.text_input('Problems of bonding with baby (yes:1, no:0, sometimes:0.5)')
        with col3:
            Suicide = st.text_input('Suicide Attempt (yes:1, no:0, not interested to say:0.5)')

        post_diag = ''
        if st.button('Postnatal Depression test'):
            #pcos_pred = pcos_model.predict([[Age, Weight, Height, Blood_grp, After_months, Gained_wt, Hair_growth, skin_dark, hair_loss, pimple, fast_food, exercise, mood_swings, regular_periods, period_last]])
            user_input = [Feeling_sad, Irritable, Trouble_sleeping, Problem_concentrating, Overeating, Anxious, Guilt, Bond_with_baby, Suicide]
            user_input = [float(x) for x in user_input]
            post_pred =post_model.predict([user_input])
            if (post_pred[0]== 0):
                post_diag = 'The Person does not have a Postnatal Depression'
                with st.spinner("Calculating..."):
                    time.sleep(2)

                st.success(post_diag)
            else:
                post_diag = 'The Person has Postnatal Depression'
                with st.spinner("Calculating..."):
                    time.sleep(2)

                st.success(post_diag)
                st.html("<h2>Overview</h2>"
                        "<p style='text-align:justify;'>Postnatal Depression is a mental health condition that affects individuals after childbirth. It can lead to significant emotional challenges, making it difficult for new parents to bond with their baby or cope with the demands of parenting. Many individuals experiencing postnatal depression may not recognize their symptoms until they severely impact daily life. Early diagnosis and intervention by a healthcare provider are crucial to improving mental well-being and parenting abilities. If you're a new parent, consider discussing your feelings with a healthcare provider, especially if you notice persistent sadness, anxiety, or withdrawal from loved ones.</p>"
                        "<h2>Treatment at home</h2>"
                        "<ol><li>Limit alcohol and caffeine.</li>"
                        "<li>Sunlight exposure daily </li>"
                        "<li>Stay hydrated </li>"
                        "<li>Maintain healthy diet</li>"
                        "<li>Self–care practices </li>"
                        "<li>Meditation and deep breathing</li>"
                        "<li>Journaling daily </li>"
                        "<li>Maintain social connections with friends and family.</li>"
                        "<li>Breastfeeding baby</li>"
                        "<li>Getting adequate sleep and general rest</li></ol>"
                        "<h2>Symptoms</h2>"
                        "<ol><li>Feeling sad or crying a lot</li>"
                        "<li>Feeling overwhelmed</li>"
                        "<li>Having thoughts of hurting the baby or yourself</li>"
                        "<li>Not having an interest in the baby</li>"
                        "<li>Having no energy or motivation</li>"
                        "<li>Feeling worthless, guilty, or like you are a bad parent</li>"
                        "<li>Sleeping too much or too little </li>"
                        "<li>Change in relationship with food</li>"
                        "<li>Feeling anxious and having chronic headaches, aches, pains stomach problems</li></ol>"
                        "<h2>Remedies and Treatment</h2>")
                
                VIDEO_DATA1="https://youtu.be/weEwCkLNX8M?si=XioJ5FctMrOkZj0K"
                VIDEO_DATA2 ="https://youtu.be/AyqO73OfIUA?si=xlV1918_pPy3cZtb"
                VIDEO_DATA3 ="https://youtu.be/h1tvgmgM-ew?si=Qs6x094tSXpJNcxU"
                VIDEO_DATA4 ="https://youtu.be/26MfRW7McAo?si=O1a0r79wNrkAPmYF"
        
                width = max(50, 0.01)
                side = max((100 - width) / 2, 0.01)

                _, container, container2 ,_ = st.columns([side, width, width, side])
                container.video(data=VIDEO_DATA1)
                container2.video(data = VIDEO_DATA2)

                _, caption1, caption2,_ = st.columns([side, width, width, side])
                caption1.html("<h5>Homeopathic cure of POSTPARTUM DEPRESSION</h5>")
                caption2.html("<h5>How to manage mental health during POSTPARTUM DEPRESSION</h5>")

                _, container3, container4 ,_ = st.columns([side, width, width, side])
                container3.video(data=VIDEO_DATA3)
                container4.video(data = VIDEO_DATA4)

                _, caption3, caption4 ,_ = st.columns([side, width, width, side])
                caption3.html("<h5>10 home remedies at home to control POSTPARTUM DEPRESSION</h5>")
                caption4.html("<h5>Health tips to handle POSTPARTUM DEPRESSION</h5>")


st.markdown("""
<style>
    
    .stTabs [data-baseweb="tab-list"] {
		gap: 28px;
    }

	.stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:20px;
    }

</style>""", unsafe_allow_html=True)

with tab3:
    hospital_data = {
    "Mumbai": [
        {
            "name": "Breach Candy Hospital",
            "address": "60A Bhulabhai Desai Road, Mumbai",
            "lat": 18.973451,
            "lon": 72.809540,
            "phone": "+91 22-2366-7788",
            "website": "http://www.breachcandyhospital.org",
            "description": "Breach Candy is one of the leading hospitals in Mumbai for women’s health and maternity services."
        },
        {
            "name": "Nowrosjee Wadia Maternity Hospital",
            "address": "Acharya Donde Marg, Parel, Mumbai",
            "lat": 19.0018,
            "lon": 72.8371,
            "phone": "+91 22-2416-7567",
            "website": "http://www.nowrosjeewadia.com",
            "description": "A well-known maternity hospital offering specialized care for women’s reproductive health."
        }
    ],
    "Bangalore": [
        {
            "name": "Cloudnine Hospital",
            "address": "1533, 9th Main Rd, 3rd Block Jayanagar, Bangalore",
            "lat": 12.9325,
            "lon": 77.6012,
            "phone": "+91 99728-99728",
            "website": "http://www.cloudninecare.com",
            "description": "Cloudnine specializes in maternity, gynecology, and neonatology services, offering world-class care."
        },
        {
            "name": "Fortis La Femme",
            "address": "154/9, Bannerghatta Rd, Opposite IIM, Bangalore",
            "lat": 12.8951,
            "lon": 77.5981,
            "phone": "+91 80-4199-4444",
            "website": "https://www.fortishealthcare.com/india/fortis-la-femme-bangalore",
            "description": "A women-focused hospital offering comprehensive healthcare services, from maternity to gynecology."
        }
    ],
    "Pune": [
        {
            "name": "Jehangir Hospital",
            "address": "32, Sassoon Road, Pune",
            "lat": 18.5244,
            "lon": 73.8760,
            "phone": "+91 20-6681-8888",
            "website": "http://www.jehangirhospital.com",
            "description": "Jehangir Hospital provides excellent services in maternity and women's healthcare."
        },
        {
            "name": "Motherhood Hospital",
            "address": "Plot No. 2, Kalpataru Society, Karve Road, Pune",
            "lat": 18.5026,
            "lon": 73.8185,
            "phone": "+91 20-6723-7777",
            "website": "http://www.motherhoodindia.com",
            "description": "A leading women’s and children’s hospital, focusing on gynecology and maternity services."
        }
    ],
    "Nashik": [
        {
            "name": "Ashoka Medicover Hospitals",
            "address": "Wadala Road, Nashik",
            "lat": 20.0015,
            "lon": 73.7980,
            "phone": "+91 253-662-4444",
            "website": "http://www.medicoverhospitals.in",
            "description": "A multi-specialty hospital with advanced women’s health services including gynecology and maternity."
        },
        {
            "name": "Currae Speciality Hospital",
            "address": "2nd Floor, Wockhardt Towers, Sharanpur Rd, Nashik",
            "lat": 19.9975,
            "lon": 73.7763,
            "phone": "+91 88888-22222",
            "website": "http://www.currae.com",
            "description": "Currae offers a wide range of women’s healthcare services, including infertility treatment and gynecology."
        }
    ],
    "Nagpur": [
        {
            "name": "KRIMS Hospitals",
            "address": "275, Central Bazar Road, Ramdaspeth, Nagpur",
            "lat": 21.1448,
            "lon": 79.0849,
            "phone": "+91 712-245-1181",
            "website": "http://www.krimshospitals.com",
            "description": "KRIMS Hospitals is a leading healthcare provider for women’s health, offering gynecological and maternity services."
        },
        {
            "name": "Orange City Hospital",
            "address": "19, Pande Layout, Khamla, Nagpur",
            "lat": 21.1192,
            "lon": 79.0657,
            "phone": "+91 712-222-2802",
            "website": "http://www.orangehospitals.com",
            "description": "Orange City Hospital provides specialized services in gynecology, obstetrics, and women's health."
        }
    ],
    "Hyderabad": [
        {
            "name": "Fernandez Hospital",
            "address": "4-1-1230, Bogulkunta, Hyderabad",
            "lat": 17.3850,
            "lon": 78.4867,
            "phone": "+91 40-4022-4022",
            "website": "http://www.fernandezhospital.com",
            "description": "A premier hospital specializing in maternity and women’s health services, with a focus on high-risk pregnancies."
        },
        {
            "name": "Apollo Cradle & Children’s Hospital",
            "address": "Madhapur, Hyderabad",
            "lat": 17.4483,
            "lon": 78.3915,
            "phone": "+91 40-4444-4444",
            "website": "https://www.apollocradle.com",
            "description": "Apollo Cradle is known for providing world-class maternity and neonatal services in Hyderabad."
        }
    ],
    "Chennai": [
        {
            "name": "MGM Healthcare",
            "address": "New No 72, Old No 54, Nelson Manickam Road, Aminjikarai, Chennai",
            "lat": 13.0701,
            "lon": 80.2426,
            "phone": "+91 44-4524-2400",
            "website": "https://www.mgmhealthcare.in",
            "description": "MGM Healthcare offers specialized women’s care, including maternity and gynecology services."
        },
        {
            "name": "Kauvery Hospital",
            "address": "199, Luz Church Road, Mylapore, Chennai",
            "lat": 13.0331,
            "lon": 80.2630,
            "phone": "+91 44-4000-6000",
            "website": "https://www.kauveryhospital.com",
            "description": "Kauvery Hospital is known for its advanced care in obstetrics, gynecology, and women’s health."
        }
    ],
    "Kolkata": [
        {
            "name": "Bhagirathi Neotia Woman and Child Care Centre",
            "address": "2, Rawdon Street, Kolkata",
            "lat": 22.5460,
            "lon": 88.3510,
            "phone": "+91 33-4040-5050",
            "website": "http://www.neotiahospital.com",
            "description": "A leading hospital for maternity and women’s healthcare in Kolkata, offering excellent obstetric services."
        },
        {
            "name": "AMRI Hospitals",
            "address": "230, Prafulla Chandra Sen Sarani, Kolkata",
            "lat": 22.5431,
            "lon": 88.3631,
            "phone": "+91 33-6680-0000",
            "website": "https://www.amrihospitals.in",
            "description": "AMRI Hospitals provides state-of-the-art women’s health services, including maternity and gynecological care."
        }
    ]
}

    # Sidebar for city selection
    city = st.selectbox("Select a city", options=list(hospital_data.keys()))

    # If a city is selected, display the hospitals in that city
    if city:
        hospitals = hospital_data[city]
        st.header(f"Showing hospitals in **{city}** for women's health")

        # Initialize a map centered on the first hospital in the selected city
        first_hospital = hospitals[0]
        map_center = [first_hospital["lat"], first_hospital["lon"]]
        hospital_map = folium.Map(location=map_center, zoom_start=10)

        # Add hospital markers with detailed information
        for hospital in hospitals:
            popup_html = f"""
            <strong>{hospital['name']}</strong><br>
            {hospital['address']}<br>
            Phone: {hospital['phone']}<br>
            <a href="{hospital['website']}" target="_blank">Visit Website</a><br>
            <p>{hospital['description']}</p>
            """
            folium.Marker(
                location=[hospital["lat"], hospital["lon"]],
                popup=folium.Popup(popup_html, max_width=300),
                tooltip=hospital['name'],
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(hospital_map)

        # Display the map
        st_data = st_folium(hospital_map, width=800, height=600) 

        # Display a list of hospitals with more details below the map
        st.subheader("Hospital Details")
        for hospital in hospitals:
            st.markdown(f"### {hospital['name']}")
            st.write(f"**Address**: {hospital['address']}")
            st.write(f"**Phone**: {hospital['phone']}")
            st.write(f"**Website**: [Visit]({hospital['website']})")
            st.write(f"**Description**: {hospital['description']}")
            st.write("---")

with tab4:


    ngo_data = [
        {
            "name": "Smile Foundation",
            "photo": "https://i.pinimg.com/280x280_RS/90/5e/2d/905e2d0d1c41f1411391284e6216f161.jpg",  # Replace with actual image URLs or local image paths
            "contact": {
                "phone": "+91-11-43123700, +91-11-41354564/65/66 l Fax: +91-11-41354454",
                "address": "161 B/4, 3rd Floor, Gulmohar House, Yusuf Sarai Community Centre, New Delhi – 110049",
                "email": "info@smilefoundationindia.org"
            },
            "website": "https://www.smilefoundationindia.org/",
            "description": "Smile foundation focuses on healthcare, education, and women's empowerment. Their healthcare initiatives provide free medical consultations, health camps, and financial aid to women facing illnesses like diabetes and osteoporosis"
        },
        {
            "name": "HelpAge India",
            "photo": "https://static.mygov.in/media/self4society/2019/08/mygov-999999999393579370.jpg",
            "contact": {
                "phone": "011-41688955/56, 42030400",
                "address": "C–14 Qutab Institutional Area, New Delhi - 110016",
                "email": "headoffice@helpageindia.org"
            },
            "website": "https://www.helpageindia.org/",
            "description": "HelpAge India works with the elderly and women , focusing on health, welfare, and financial aid. They provide healthcare services and support for chronic illnesses like diabetes and osteoporosis among elderly women."
        },
        {
            "name": "The Akshaya Patra Foundation",
            "photo": "data:image/png;base64,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",
            "contact": {
                "phone": "+91 80 3014 3400",
                "address": "72, 3rd Floor, 3rd Main Road, 1st & 2nd Stage, Yeshwantpur Industrial Suburb, Rajajinagar Ward No. 10, Bengaluru – 560022, India",
                "email":"donorcare@akshayapatra.org"
            },
            "website": "https://www.akshayapatra.org/",
            "description": "Known primarily for their mid-day meal programs, Akshaya Patra also runs health-focused initiatives  and partners with various healthcare organizations to provide aid to women with chronic illnesses like diabetes and PCOS."
        },
        # {
        #     "name": "Cipla Foundation",
        #     "photo": "https://via.placeholder.com/100",
        #     "contact": {
        #         "phone": "+91 98765 43210",
        #         "address": "456 Another Road, City, Country",
        #         "email":"example.com"
        #     },
        #     "website": "http://www.empowerwomen.com",
        #     "description": "This NGO provides financial aid to women in need."
        # },
        # {
        #     "name": "Vandrevala Foundation",
        #     "photo": "https://via.placeholder.com/100",
        #     "contact": {
        #         "phone": "+91 98765 43210",
        #         "address": "456 Another Road, City, Country",
        #         "email":"example.com"
        #     },
        #     "website": "http://www.empowerwomen.com",
        #     "description": "This NGO provides financial aid to women in need."
        # },
        # {
        #     "name": "Indian Diabetes Research",
        #     "photo": "https://via.placeholder.com/100",
        #     "contact": {
        #         "phone": "+91 98765 43210",
        #         "address": "456 Another Road, City, Country",
        #         "email":"example.com"
        #     },
        #     "website": "http://www.empowerwomen.com",
        #     "description": "This NGO provides financial aid to women in need."
        # }

    ]

    # HTML and CSS for displaying NGO details
    def generate_ngo_html(ngo):
        return f"""
        <div class="ngo-container">
            <img src="{ngo['photo']}" alt="{ngo['name']}" class="ngo-photo">
            <div class="ngo-details">
                <h2>{ngo['name']}</h2>
                <p><strong>Overview:</strong> {ngo['description']}</p>
                <p><strong>Phone:</strong> {ngo['contact']['phone']}</p>
                <p><strong>Address:</strong> {ngo['contact']['address']}</p>
                <p><strong>Email:</strong> {ngo['contact']['email']}</p>
                <a href="{ngo['website']}" target="_blank">Visit Website</a>
            </div>
        </div>
        """

    # CSS styling
    st.markdown("""
        <style>
        .ngo-container {
            border: 1px solid #ccc;
            padding: 20px;
            margin: 10px 0;
            border-radius: 10px;
            display: flex;
            align-items: center;
            background-color: #f9f9f9;
        }
        .ngo-photo {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            margin-right: 20px;
        }
        .ngo-details {
            flex: 1;
        }
        .ngo-details h2 {
            margin: 0;
            font-size: 24px;
        }
        .ngo-details p {
            margin: 5px 0;
        }
        .ngo-details a {
            display: block;
            margin-top: 10px;
            text-decoration: none;
            color: #007bff;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    # Streamlit page title
    st.title("NGOs for Women's Health")

    # Loop through each NGO and render its details
    for ngo in ngo_data:
        ngo_html = generate_ngo_html(ngo)
        st.markdown(ngo_html, unsafe_allow_html=True)


        


 



    