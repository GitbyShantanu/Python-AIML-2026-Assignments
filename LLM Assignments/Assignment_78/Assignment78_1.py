from narwhals import min
import streamlit as st 

st.title("Addition Calculator") 

no1 = st.number_input("Enter 1st number : ", min_value=0, step=1) 
no2 = st.number_input("Enter 2nd number : ", min_value=0, step=1)

def Addition(a,b):
    return a + b 

if st.button("Add"):

    st.success(f"The sum of {no1} and {no2} is : {Addition(no1,no2)}")
    