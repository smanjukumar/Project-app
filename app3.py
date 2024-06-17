#Title name
import streamlit as st
st.title("EDI-42 Work order sheet")

#Login page
username = st.text_input('Username')
password =st.text_input('password',type='password')

#Login button
if st.button("Login"):

 if username == 'z606215' and password == 'Manju':
     st.write('loged in as {}'.format(username))
 else:
     st.write("Invalid Username or Password")

     #create data frame
import pandas as pd
Name= st.text_input("Enter your name")
Monday = st.number_input(" enter your Monday hours")
Tuesday = st.number_input(" enter your Tuesday hours")
wednesday = st.number_input(" enter your wednesady hours")
Thursday = st.number_input(" enter your Thursday hours")
Friday = st.number_input("enter your friday hours")

df = pd.DataFrame({ 
        "Name": [Name],
        "Monday": [Monday],
        "Tuesday": [Tuesday],
        "wednesday": [wednesday],
        "Thurday": [Thursday],
        "Friday" : [Friday]
})
df

from PIL import Image
logo = Image.open('logo.png')
st.sidebar.image(logo, width=200)

#Read the data 
import pandas as pd
df = pd.read_csv('work order.csv')
df

#side bar
st.sidebar.title("Filters")
Name= st.sidebar.selectbox("Name",['Manjukumar','Ganesh ','Sai Teja','Veerababu','Yuvraja Sekar','Mohammad Ameer','Prasad Boga','Afzal Khan','Charan']
                           )
#Filter the data 
filtered_df=df[df["Name"] == Name]
filtered_df
