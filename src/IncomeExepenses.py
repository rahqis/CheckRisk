import streamlit as st

st.sidebar.title("Monthly Budget Analyzer")

st.sidebar.header("Income")
incomeStr = 'Estimated Income'
income = st.sidebar.number_input(incomeStr)

st.sidebar.header("Estimated expenses")


transportationStr = 'Transportation'
transportation = st.sidebar.number_input(transportationStr)

homeStr = 'Home & Utilities'
home = st.sidebar.number_input(homeStr)

groceriesStr = 'Groceries'
groceries = st.sidebar.number_input(groceriesStr)

personalStr = 'Personal & Family Care'
personal  = st.sidebar.number_input(personalStr)

healthStr = 'Health'
health = st.sidebar.number_input(healthStr)

diningStr = 'Restaurants & Dining'
dining = st.sidebar.number_input(diningStr)

shoppingStr = 'Shopping & Entertainment'
shopping = st.sidebar.number_input(shoppingStr)

savingsStr = 'Savings & Investments'
savings = st.sidebar.number_input(savingsStr)

otherStr = 'Other and Miscellaneous'
other = st.sidebar.number_input(otherStr)







