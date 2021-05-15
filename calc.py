import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.header('Fixed Deposit Calculator')

cols = st.beta_columns(2)
form = cols[0].form(key='my_form')
dep_amount=form.text_input('Deposit Amount: ')
rate_interest=form.text_input('Annual Interest Rate: ')
term=form.text_input('Term: ')
term_type=form.selectbox('', ['Years','Months','Days'])
int_type=form.selectbox('I want to receive interest: ', ['Monthly','Quarterly','Half-Yearly','Yearly'])

submit = form.form_submit_button('Submit')
if submit:
    dep_amount=float(dep_amount)
    rate_interest=float(rate_interest)
    term=float(term)
    
    if(term_type=='Months'):
        term=term/12
    elif(term_type=='Days'):
        term=term/365
    
    tot_interest = dep_amount*term*rate_interest/100
    
    if(int_type=='Monthly'):
        interest=tot_interest/12
        term1=term*12
    elif(int_type=='Quarterly'): 
        interest=tot_interest/4
        term1=term*4
    elif(int_type=='Half-Yearly'): 
        interest=tot_interest/2
        term1=term*2
    else:
        interest = tot_interest
        term1=term*1
    
    interest_split = interest/term
    
    #st.write(interest)
    
    fig, ax = plt.subplots()
    ax.pie([tot_interest,dep_amount],labels=['Interest','Deposit'],explode=(0.1,0),
            autopct='%1.1f%%', startangle=90) #shadow=True
    cols[1].pyplot(fig)
    cols[1].write('Priniciple amount : '+ str(dep_amount))
    cols[1].write('Interest amount : '+ str(tot_interest))
    cols[1].write('Total Assured amount : '+ str(tot_interest + dep_amount))
    
    
    l2=[]
    i=1
    dep_amount1=dep_amount
    while(i<=term1):
        l1=[]
        l1.append(i)
        l1.append(dep_amount1)
        l1.append(interest_split)
        dep_amount1=0
        i+=1
        l2.append(l1)
    
    
    dataframe = pd.DataFrame(l2,columns=[int_type[:-2],'Amount Deposited (Rs.)',
                                         'Interest Received (Rs.)'])
    
    dataframe['Total Interest Received (Rs.)']=dataframe['Interest Received (Rs.)'].cumsum()
    st.dataframe(dataframe)
    


#st.text(a)