import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open("knn_model.pkl","rb") as f:
    model=pickle.load(f)

st.title("AQI Prediction APP")

City= st.selectbox("City",['Ahmedabad', 'Aizawl', 'Amaravati', 'Amritsar', 'Bengaluru',
       'Bhopal', 'Brajrajnagar', 'Chandigarh', 'Chennai', 'Coimbatore',
       'Delhi', 'Ernakulam', 'Gurugram', 'Guwahati', 'Hyderabad',
       'Jaipur', 'Jorapokhar', 'Kochi', 'Kolkata', 'Lucknow', 'Mumbai',
       'Patna', 'Shillong', 'Talcher', 'Thiruvananthapuram',
       'Visakhapatnam'])

PM_2_5=float(st.number_input("PM2.5",value=0.0))
NO=float(st.number_input("NO",value=0.0))
NO2=float(st.number_input("NO2",value=0.0))
NOX=float(st.number_input("NOX",value=0.0))
CO=float(st.number_input("CO",value=0.0))
SO2=float(st.number_input("SO2",value=0.0))
O3=float(st.number_input("O3",value=0.0))
Benzene=float(st.number_input("Benzene",value=0.0))

if st.button("Predict AQIBucket"):
    input_df=pd.DataFrame([{
        "City":City,
        "PM2.5":PM_2_5,
        "NO":NO,
        "NO2":NO2,
        "NOx":NOX,
        "CO":CO,
        "SO2":SO2,
        "O3":O3,
        "Benzene":Benzene
    }])
    result=model.predict(input_df)[0]
    st.success(f"AQI Bucket :{result}")
