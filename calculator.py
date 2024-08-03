import streamlit as st

# Function to perform the basic calculations
def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error! Division by zero.'
    else:
        return 'Invalid Operation'

# Streamlit layout
st.title("Simple Calculator")

# Input for the first number
num1 = st.number_input("Enter first number", value=0)

# Input for the second number
num2 = st.number_input("Enter second number", value=0)

# Dropdown for operation selection
operation = st.selectbox("Select operation", ('Add', 'Subtract', 'Multiply', 'Divide'))

# Button to perform calculation
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"The result is: {result}")
