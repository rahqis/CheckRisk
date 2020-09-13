import streamlit as st
import heroku
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
categories = []
st.header('Financial Health')
st.subheader('Create a secure tomorrow today')
fhHelper = st.write('To start, take the monthly budget analyzer in the side bar.') 
fhHelper1 = st.write('We\'ll wait for you back here with your results!')         
st.sidebar.title("Monthly Budget Analyzer")

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

otherStr = 'Other and Miscellaneous'
other = st.sidebar.number_input(otherStr, value=0.00)
misc = Category(otherStr, other)
categories.append(misc)
    
totalExpenses = 0.00
for c in categories:
    totalExpenses = totalExpenses + c.cost



    


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
    savePer = save.cost / inc.cost * 100
    sp = 0
    lo = '{:.2f}'.format(leftOver)
    st.subheader('Left Over After Expense: $' + lo)
    st.subheader('Current Savings Percentage: ' + '{:.2f}'.format(savePer) + '%')

    
def saveGoals():
    st.header("Saving Goals")
    st.subheader('How much of your income would you like to save?')    
    saveGoal = st.slider('Monthly Saving Goal', 0, 100)
    fixed = st.multiselect('Which of your incomes are fixed and essential?',
                 (trans.name, homeutil.name, groc.name, pers.name, heal.name))
    Remainder = 100
    labels = []
    sizes = []
    explode = []
    
    nonessential =[]
    
    for c in categories:
        if (c.cost > 0):
            labels.append(c.name)
            sizes.append(0)
            
    for n in labels:
        if n not in fixed:
            nonessential.append(n)
    
    for i in range(len(labels)): 
        if (labels[i]==savingsStr):
            sizes[i] = saveGoal
            Remainder = Remainder - saveGoal
    
    for i in range(len(labels)):
       if labels[i] in fixed:
           for c in categories:
               if labels[i] == c.name:
                    sizes[i] = int(c.cost / inc.cost * 100)
                    Remainder = Remainder - sizes[i]
    
    equals = 0
    if Remainder > 0:
        equals = Remainder / len(nonessential)
        for i in range(len(sizes)):
                if sizes[i] == 0:
                    sizes[i] = equals
    

    for i in range(len(sizes)):
        explode.append(0)
    plt.pie(sizes, explode, None, autopct='%1.2f%%', labeldistance=.7)
    
    plt.axis('equal')
    st.header('Congratulations on your new budget plan!')
    plt.legend(labels, bbox_to_anchor=(1., 1.02, 1., .412), 
           ncol=2, mode="expand", borderaxespad=0.)
    
    st.pyplot()
    
    
    
def resources():
    st.header('Further resources to guide you on your journey!')
    st.subheader('')
    components.html('''
                    
                    ''')

if st.sidebar.button("View Spending"):
        fhHelper = st.write('Welcome back! Let\'s take a look at your results.')
        fhHelper1 = st.write('')
        generatePieSpend()
        leftOver()
        #generateBarSpend()
        highExepense()

saveGoals()

