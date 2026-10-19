import streamlit as st 

st.title("Even or Odd Number Checker") 

n = st.number_input("Enter number : ", min_value=0, step=1)

def check_even_odd(n):
    if n % 2 == 0:
        return True 
    else:
        return False 

if st.button("Check"):
    if check_even_odd(n):
        st.success(f"The number {n} is : Even.")
    else:
        st.error(f"The number {n} is : Odd.") 
    