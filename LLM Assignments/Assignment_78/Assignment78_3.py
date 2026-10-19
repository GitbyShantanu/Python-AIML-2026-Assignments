import streamlit as st 

st.title("Interest Calculator") 

principal = st.number_input("Enter principal amount : ", min_value=0)
rate = st.number_input("Enter rate of interest : ")
time = st.number_input("Enter time in years : ", min_value=0)

def calculate_interest(principal, rate, time):
    return (principal * rate * time) / 100

if st.button("Calculate Interest", type='primary'):
    st.success(f"The interest is : {calculate_interest(principal, rate, time)}") 
    