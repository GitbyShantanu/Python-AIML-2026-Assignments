import streamlit as st 

st.title("Student Result Calculator") 

name = st.text_input("Enter Student Name : ") 
physics = st.number_input("Enter Marks in Physics : ", min_value=0, max_value=100, step=1) 
chemistry = st.number_input("Enter Marks in Chemistry : ", min_value=0, max_value=100, step=1) 
maths = st.number_input("Enter Marks in Maths : ", min_value=0, max_value=100, step=1) 

def calculate_result(sub1, sub2, sub3):
    total = sub1 + sub2 + sub3 
    percentage = total/3 
    return total, percentage 

if st.button("Calculate Result"): 
    total_marks,percentage = calculate_result(physics,chemistry,maths)
    
    if physics < 40 or chemistry < 40 or maths < 40:
        st.error("Sorry! You failed in one or more subjects.") 
        st.write(f"Total Marks : {total_marks}") 
        st.write(f"Percentage : {percentage:.2f}%")

    else:
        st.success("Congratulations! You have Passed!") 
        st.write(f"Total Marks : {total_marks}") 
        st.write(f"Percentage : {percentage:.2f}%")
