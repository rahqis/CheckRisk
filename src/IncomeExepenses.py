import streamlit as st



class Category:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
catergories = []

st.sidebar.title("Monthly Budget Analyzer")

st.sidebar.header("Income")

incomeStr = 'Estimated Income'
income = st.sidebar.number_input(incomeStr)
inc = Category(incomeStr, income)

st.sidebar.header("Estimated expenses")


transportationStr = 'Transportation'
transportation = st.sidebar.number_input(transportationStr)
trans = Category(transportationStr, transportation)
catergories.append(trans)

homeStr = 'Home & Utilities'
home = st.sidebar.number_input(homeStr)
homeutil = Category(homeStr, home)
catergories.append(homeutil)

groceriesStr = 'Groceries'
groceries = st.sidebar.number_input(groceriesStr)
groc = Category(groceriesStr, groceries)
catergories.append(groc)

personalStr = 'Personal & Family Care'
personal  = st.sidebar.number_input(personalStr)
pers = Category(personalStr, personal)
catergories.append(pers)

healthStr = 'Health'
health = st.sidebar.number_input(healthStr)
heal = Category(healthStr, health)
catergories.append(heal)

diningStr = 'Restaurants & Dining'
dining = st.sidebar.number_input(diningStr)
dine = Category(diningStr, dining)
catergories.append(dine)

shoppingStr = 'Shopping & Entertainment'
shopping = st.sidebar.number_input(shoppingStr)
shop = Category(shoppingStr, shopping)
catergories.append(shop)

savingsStr = 'Savings & Investments'
savings = st.sidebar.number_input(savingsStr)
save = Category(savingsStr, savings)
catergories.append(save)

otherStr = 'Other and Miscellaneous'
other = st.sidebar.number_input(otherStr)
misc = Category(otherStr, other)
catergories.append(misc)


