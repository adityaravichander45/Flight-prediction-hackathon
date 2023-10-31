import pandas as pd
import numpy as np
import streamlit as st
import joblib
import warnings
warnings.filterwarnings('ignore')

# Loan the model
model= joblib.load('Polylinearregression.pkl')

#Load the file
df=pd.read_csv('flighttrain.csv')


def predict_price(Airline,Date_of_Journey,Source,Destination,Route,Additional_Info,Price,Duration_in_mins,Month_of_Journey,Dep_Time_in_htclass,Day_of_Journey,Totalno_Stops):
      
      # get column names
      col_names = ['Airline','Date_of_Journey','Source','Destination','Route','Additional_Info','Price','Duration_in_mins','Month_of_Journey',
       'Dep_Time_in_htclass','Day_of_Journey','Totalno_Stops']
       
      # get column values
      col_values = [Airline,Date_of_Journey,Source,Destination,Route,Additional_Info,Price,
        Duration_in_mins,Month_of_Journey,Dep_Time_in_htclass,Day_of_Journey,Totalno_Stops]
       
      # dataframe
      test = pd.DataFrame([col_values])
      test.columns = col_names 
       
      # calling the predict model 
      predicted = model.predict(test)
      return predicted
       
       
# the main program

def main():


    st.title("Airlines Booking")
       
    # creating a heading
    html_tmp = """
    <div style='background-color:blue;'>
    <h2 style='color:white;text-align:center;'>Flight price Prediction App</h2>
    </div>
    """
    st.markdown(html_tmp, unsafe_allow_html=True)
        
    # creating the input columns
    Airline = st.selectbox('Select the name of an airline:',pd.unique(df['Airline']))
    Price= st.number_input('Enter the price of the ticket:')
    Duration_in_mins = st.number_input('Enter the duration of destination:',max_value=3000)
    Source = st.selectbox('Enter the city of departure:',pd.unique(df['Source']))
    Destination = st.selectbox('Enter the final destination:',pd.unique(df['Destination']))
    Month_of_Journey = st.selectbox('Select the month:',pd.unique(df['Month_of_Journey']))
    Totalno_Stops = st.slider('Choose the total no of stops:',0,4)
    Route = st.selectbox('Select the route:',pd.unique(df['Route']))
    Additional_Info = st.radio('Enter your additional information:',pd.unique(df['Additional_Info']))
    Dep_Time_in_htclass = st.selectbox('Enter the Departure time:',pd.unique(df['Dep_Time_in_htclass']))
    Day_of_Journey = st.selectbox('Select the day of departure:',pd.unique(df['Day_of_Journey']))
    Date_of_Journey = st.date_input("Select your departure date")
    
	



if __name__=='__main__':
    main()




       
       
       
           
        
        

        
