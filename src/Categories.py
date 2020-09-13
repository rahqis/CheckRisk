import streamlit as st
import matplotlib.pyplot as plt
<<<<<<< HEAD
=======
import importlib
>>>>>>> ace41310237d70d1e98d0d65a932caa255b6d630

class Category:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

<<<<<<< HEAD
categories = []

st.sidebar.title("Monthly Budget Analyzer")
=======
catergories = []

def runSide():
    
    st.sidebar.title("Monthly Budget Analyzer")
>>>>>>> ace41310237d70d1e98d0d65a932caa255b6d630

st.sidebar.header("Income")

incomeStr = 'Estimated Income'
income = st.sidebar.number_input(incomeStr, value=0.00)
inc = Category(incomeStr, income)

st.sidebar.header("Estimated expenses")


transportationStr = 'Transportation'
transportation = st.sidebar.number_input(transportationStr, value=0.00)
trans = Category(transportationStr, transportation)
categories.append(trans)

homeStr = 'Home & Utilities'
home = st.sidebar.number_input(homeStr, value=0.00)
homeutil = Category(homeStr, home)
categories.append(homeutil)

groceriesStr = 'Groceries'
groceries = st.sidebar.number_input(groceriesStr, value=0.00)
groc = Category(groceriesStr, groceries)
categories.append(groc)

personalStr = 'Personal & Family Care'
personal  = st.sidebar.number_input(personalStr, value=0.00)
pers = Category(personalStr, personal)
categories.append(pers)

healthStr = 'Health'
health = st.sidebar.number_input(healthStr, value=0.00)
heal = Category(healthStr, health)
categories.append(heal)

diningStr = 'Restaurants & Dining'
dining = st.sidebar.number_input(diningStr, value=0.00)
dine = Category(diningStr, dining)
categories.append(dine)

shoppingStr = 'Shopping & Entertainment'
shopping = st.sidebar.number_input(shoppingStr, value=0.00)
shop = Category(shoppingStr, shopping)
categories.append(shop)

savingsStr = 'Savings & Investments'
savings = st.sidebar.number_input(savingsStr, value=0.00)
save = Category(savingsStr, savings)
categories.append(save)

<<<<<<< HEAD
otherStr = 'Other and Miscellaneous'
other = st.sidebar.number_input(otherStr, value=0.00)
misc = Category(otherStr, other)
categories.append(misc)
    
totalExpenses = 0.00
for c in categories:
    totalExpenses = totalExpenses + c.cost

    
=======
    otherStr = 'Other and Miscellaneous'
    other = st.sidebar.number_input(otherStr)
    misc = Category(otherStr, other)
    catergories.append(misc)

>>>>>>> ace41310237d70d1e98d0d65a932caa255b6d630
    


def generatePieSpend():
    labels = []
    sizes = []
    explode = []
    
    
    for c in categories:
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
    

def generateBarSpend():
    labels = []
    sizes = []    
    
    for c in categories:
        if (c.cost > 0):
            labels.append(c.name)
            sizes.append(c.cost)
    
    plt.bar(labels, sizes, width=0.8, align='center')
    plt.xticks(rotation=90)
    plt.xlabel("Categories");
    plt.ylabel("Spending");

<<<<<<< HEAD
    st.pyplot()
    
def highExepense():
    highestExpense = categories[0]
    highest2Expense = categories[1]
    highest3Expense = categories[2]

    for c in categories:
        if(highestExpense.cost<c.cost):
            highestExpense = c
        if(highest2Expense == highestExpense):
            highest2Expense = categories[0]
    for c in categories:
        if(highest2Expense.cost<highestExpense.cost and highest2Expense.cost<c.cost and c != highestExpense):
            highest2Expense = c
        if (highest2Expense == highest3Expense):
            highest3Expense = categories[1]
        if (highest3Expense == highestExpense):
            highest3Expense = categories[0]
    for c in categories:
        if(highest3Expense.cost<=highest2Expense.cost and highest3Expense.cost<c.cost and (c != highest2Expense and c != highestExpense)):
            highest3Expense = c
    
    highestExpenses = [highestExpense, highest2Expense, highest3Expense]
    
    st.subheader('Top 3 Expenses')
    for h in highestExpenses:
        st.write(h.name)
        st.write('$', '{:.2f}'.format(h.cost)) 

def leftOver():
    leftOver = inc.cost - totalExpenses
    lo = '{:.2f}'.format(leftOver)
    st.subheader('Left Over After Expense: $' + lo)
        
def saveGoals():
    savePer = save.cost / inc.cost * 100
    st.subheader('How much of your income would you like to save?')    
    st.write('Current Savings Percentage: ', '{:.2f}'.format(savePer), '%')
    saveGoal = st.slider('Monthly Saving Goal', 0, 100, value=int(savePer)) 

if st.sidebar.button("View Spending"):
    st.cache(generatePieSpend(), persist=True)
    st.cache(leftOver(), True)
    #generateBarSpend()
    st.cache(highExepense(), True)
    saveGoals()
except:
    pass  
=======
def generateBarSpend():
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
    plt.bar(labels, sizes, width=0.2, align='center')
    plt.xlabel("Categories");
    plt.ylabel("Spending");

    st.pyplot()

if st.sidebar.button("View Spending Chart"):
    generatePieSpend()
    generateBarSpend()
    


>>>>>>> ace41310237d70d1e98d0d65a932caa255b6d630
