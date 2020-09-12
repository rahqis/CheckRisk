import streamlit as st
import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

catergories = []
def runSide():
    
    st.sidebar.title("Monthly Budget Analyzer")

    st.sidebar.header("Income")

    incomeStr = 'Estimated Income'
    income = st.sidebar.number_input(incomeStr, value=0.00)
    inc = Category(incomeStr, income)

    st.sidebar.header("Estimated expenses")


    transportationStr = 'Transportation'
    transportation = st.sidebar.number_input(transportationStr, value=0.00)
    trans = Category(transportationStr, transportation)
    catergories.append(trans)

    homeStr = 'Home & Utilities'
    home = st.sidebar.number_input(homeStr, value=0.00)
    homeutil = Category(homeStr, home)
    catergories.append(homeutil)

    groceriesStr = 'Groceries'
    groceries = st.sidebar.number_input(groceriesStr, value=0.00)
    groc = Category(groceriesStr, groceries)
    catergories.append(groc)

    personalStr = 'Personal & Family Care'
    personal  = st.sidebar.number_input(personalStr, value=0.00)
    pers = Category(personalStr, personal)
    catergories.append(pers)

    healthStr = 'Health'
    health = st.sidebar.number_input(healthStr, value=0.00)
    heal = Category(healthStr, health)
    catergories.append(heal)

    diningStr = 'Restaurants & Dining'
    dining = st.sidebar.number_input(diningStr, value=0.00)
    dine = Category(diningStr, dining)
    catergories.append(dine)

    shoppingStr = 'Shopping & Entertainment'
    shopping = st.sidebar.number_input(shoppingStr, value=0.00)
    shop = Category(shoppingStr, shopping)
    catergories.append(shop)

    savingsStr = 'Savings & Investments'
    savings = st.sidebar.number_input(savingsStr, value=0.00)
    save = Category(savingsStr, savings)
    catergories.append(save)

    otherStr = 'Other and Miscellaneous'
    other = st.sidebar.number_input(otherStr, value=0.00)
    misc = Category(otherStr, other)
    catergories.append(misc)
    
runSide()

def generatePieSpend():
    labels = []
    sizes = []
    colors = []
    explode = []
    
    
    for c in catergories:
        if (c.cost > 0):
            labels.append(c.name)
            sizes.append(c.cost)
    
    for i in range(len(labels)):
        explode.append(0)
    plt.pie(sizes, explode, None, autopct='%1.2f%%', labeldistance=.7)
    

    plt.axis('equal')
    st.header('Your Spending Chart')
    plt.legend(labels, bbox_to_anchor=(1., 1.02, 1., .412), 
           ncol=2, mode="expand", borderaxespad=0.)
    
    st.pyplot()
    


    
def highExepense():
    highestExpense = catergories[0]
    highest2Expense = catergories[1]
    highest3Expense = catergories[2]

    for c in catergories:
        if(highestExpense.cost<c.cost):
            highestExpense = c
        if(highest2Expense == highestExpense):
            highest2Expense = catergories[0]
    for c in catergories:
        if(highest2Expense.cost<highestExpense.cost and highest2Expense.cost<c.cost and c != highestExpense):
            highest2Expense = c
    for c in catergories:
        if(highest3Expense.cost<=highest2Expense.cost and highest3Expense.cost<c.cost and (c != highest2Expense and c != highestExpense)):
            highest3Expense = c
    
    highestExpenses = [highestExpense, highest2Expense, highest3Expense]
    
    st.subheader('Top 3 Expenses')
    for h  in highestExpenses:
        st.write(h.name)
        st.write('{:06.2f}'.format(h.cost))

if st.sidebar.button("View Spending Chart"):
    generatePieSpend()
    highExepense()    

