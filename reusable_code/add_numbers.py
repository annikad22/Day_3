import streamlit as st
from reusable_code.add_numbers import add_numbers

def add_numbers(num1, num2): 

    sum = num1 + num2 
    return sum 

    #in home.py file 
    user_input_number_1 = st.num_input(label="first_number", step = 1)

    user_input_number_2 = st.num_input(label="first_number", step = 1)

    #takes two numbers as input and returns result 
    result = add_numbers(user_input_number_1, user_input_number_2)

    st.write(result) 

    #if API call is 10 lines - could run as single line in main code. 
    #build logic once and test and put aside and 