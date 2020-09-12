import streamlit as stl

stl.sidebar.title("Monthly Budget Analyzer")

stl.sidebar.header("Income")
incomeStr = 'Estimated Income'
income = stl.sidebar.number_input(incomeStr)

stl.sidebar.header("Estimated expenses")


transportationStr = 'Transportation'
transportation = stl.sidebar.number_input(transportationStr)

homeStr = 'Home & Utilities'
home = stl.sidebar.number_input(homeStr)

groceriesStr = 'Groceries'
groceries = stl.sidebar.number_input(groceriesStr)

personalStr = 'Personal & Family Care'
personal  = stl.sidebar.number_input(personalStr)

healthStr = 'Health'
health = stl.sidebar.number_input(healthStr)

diningStr = 'Restaurants & Dining'
dining = stl.sidebar.number_input(diningStr)

shoppingStr = 'Shopping & Entertainment'
shopping = stl.sidebar.number_input(shoppingStr)

savingsStr = 'Savings & Investments'
savings = stl.sidebar.number_input(savingsStr)

otherStr = 'Other and Miscellaneous'
other = stl.sidebar.number_input(otherStr)







