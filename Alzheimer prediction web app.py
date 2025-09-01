# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 15:08:19 2023

@author: sanjaykumar
"""

import numpy as np
import pickle
import streamlit as st
import base64 

loaded_model = pickle.load(open('D:/Downloads/ADML/ADML/trained_model.sav','rb'))

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"https://drive.google.com/file/d/1LvlTT_1S1RyvcpZKGxGwn7lJu1FdvzU0/view?usp=sharing"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('D:/Downloads/ADML/ADML/26087.jpg') 

def alzheimer_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]=="Demented"):
     return("Alzheimer disease person")
    else:
     return("Non Alzheimer disease person")
  
    
  
def main():
    st.title('Alzheimer Disease Prediction')
    

    Age = st.text_input('**Enter Your age**',)
    
    EDUC = st.text_input('**Year of education**')
    SES = st.text_input('**Socioeconomic status**')
    MMSE = st.text_input('**Mini-Mental State Examination**')
    CDR = st.text_input('**Clinical dementia rating**')
    eTIV = st.text_input(' **Estimated Total Intracranial Volume**')
    nWBV = st.text_input('**Normalized whole-brain volume**')
    ASF = st.text_input('**Atlas Scaling Factor**')
    
    
    
    diagnosis = ''
    
    if st.button('Predict the result'):
        diagnosis = alzheimer_prediction([Age,EDUC,SES,MMSE,CDR,eTIV,nWBV,ASF])
    

    st.success(diagnosis)
    
    
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    