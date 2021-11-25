pip install -r requirements.txt


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date
#import json
#import requests
from time import sleep

## import data from local datasets
years10 = pd.read_csv(r"yield-10-years-us.csv")
years10 = years10[["Date","Price"]]
years10.rename({"Price":"Price10y"},axis = 1,inplace = True)
years10 = years10.iloc[::-1]
years10["Date"] = pd.to_datetime(years10["Date"])
years10.set_index("Date",inplace= True)

month3 = pd.read_csv(r"yield-3-months-us.csv")
month3 = month3[["Date","Price"]]
month3.rename({"Price":"Price3m"},axis = 1,inplace = True)
month3 = month3.iloc[::-1]
month3["Date"] = pd.to_datetime(month3["Date"])
month3.set_index("Date",inplace= True)

indicator_data = pd.read_csv(r"indicator_data.csv")
indicator_data = indicator_data.iloc[::-1]
indicator_data.date = pd.to_datetime(indicator_data.date)
indicator_data.set_index("date",inplace= True)



## import data from api Websites Alpha Vantage
#### URLs
expectation_inflation_url = 'https://www.alphavantage.co/query?function=INFLATION_EXPECTATION&apikey=6CSVTNJH2F6XJU1N'
cpi_url = 'https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey=6CSVTNJH2F6XJU1N'
fed_fund_rate_url = 'https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval=monthly&apikey=6CSVTNJH2F6XJU1N'
consumer_sentiment_url = "https://www.alphavantage.co/query?function=CONSUMER_SENTIMENT&apikey=6CSVTNJH2F6XJU1N"
durable_goods_url = "https://www.alphavantage.co/query?function=DURABLES&apikey=NQAZG7Q5OQ6AT71X"
retail_sales_url = "https://www.alphavantage.co/query?function=RETAIL_SALES&apikey=NQAZG7Q5OQ6AT71X"
unemployment_rate_url = "https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey=6CSVTNJH2F6XJU1N"

##### Requests
#responseEI = requests.get(expectation_inflation_url)
#responseCPI = requests.get(cpi_url)
#responseFR = requests.get(fed_fund_rate_url)
#responseDG = requests.get(durable_goods_url)
#responseCS = requests.get(consumer_sentiment_url)
#responseUR = requests.get(unemployment_rate_url)
#responseRS = requests.get(retail_sales_url)

#print(responseEI,responseCPI,responseFR,responseDG,responseCS,responseUR,responseRS)

#### API data preprocessing 
#dataEI = responseEI.json()
#sleep(2)
#dataEI = dataEI['data']
#expectation_inflation = pd.json_normalize(dataEI)

#dataCPI = responseCPI.json()
#sleep(2)
#dataCPI = dataCPI['data']
#cpi = pd.json_normalize(dataCPI)

#dataFR = responseFR.json()
#sleep(2)
#dataFR = dataFR['data']
#fed_fund_rate = pd.json_normalize(dataFR)

#dataDG = responseDG.json()
#sleep(2)
#dataDG = dataDG['data']
#durable_goods = pd.json_normalize(dataDG)

#dataCS = responseCS.json()
#sleep(2)
#dataCS = dataCS['data']
#consumer_sentiment = pd.json_normalize(dataCS)

#dataUR = responseUR.json()
#sleep(2)
#dataUR = dataUR['data']
#unemployment_rate = pd.json_normalize(dataUR)

#dataRS = responseRS.json()
#sleep(2)
#dataRS = dataRS['data']
#retail_sales = pd.json_normalize(dataRS)


####  import data

# Expected Inflation
#expectation_inflation["value"] = expectation_inflation["value"].astype(float)
#expectation_inflation["date"] = pd.to_datetime(expectation_inflation["date"])
#expectation_inflation.set_index("date",inplace= True)
#expectation_inflation.rename({"value":"expectation_inflation"},axis = 1 , inplace = True)


#print("step0")

# CPI
#cpi["value"] = cpi["value"].astype(float)
#cpi["date"] = pd.to_datetime(cpi["date"])
#cpi.set_index("date",inplace= True)
#cpi.rename({"value":"cpi"},axis = 1 , inplace = True)


#print("step1")


# Fed Fund Rate


#fed_fund_rate["value"] = fed_fund_rate["value"].astype(float)
#fed_fund_rate["date"] = pd.to_datetime(fed_fund_rate["date"])
#fed_fund_rate.set_index("date",inplace= True)
#fed_fund_rate.rename({"value":"fed_fund_rate"},axis = 1 , inplace = True)


#print("step2")


#Durable Goods

#durable_goods["value"] = durable_goods["value"].astype(float)
#durable_goods["date"] = pd.to_datetime(durable_goods["date"])
#durable_goods.set_index("date",inplace= True)
#durable_goods.rename({"value":"durable_goods"},axis = 1 , inplace = True)




#print("step3")

#Consumer Sentiment

#consumer_sentiment["date"] = pd.to_datetime(consumer_sentiment["date"])
#consumer_sentiment = consumer_sentiment[consumer_sentiment["date"]>="2000-01-01"]
#consumer_sentiment["value"] = consumer_sentiment["value"].astype(float)
#consumer_sentiment.set_index("date",inplace= True)
#consumer_sentiment.rename({"value":"consumer_sentiment"},axis = 1 , inplace = True)




#print("step4")

#Unemployment Rate

#unemployment_rate["value"] = unemployment_rate["value"].astype(float)
#unemployment_rate["date"] = pd.to_datetime(unemployment_rate["date"])
#unemployment_rate.set_index( "date" , inplace = True)
#unemployment_rate.rename({"value":"unemployment_rate"},axis = 1 , inplace = True)



#print("step5")

#Retail Sales

#retail_sales["value"] = retail_sales["value"].astype(float)
#retail_sales["date"] = pd.to_datetime(retail_sales["date"])
#retail_sales.set_index("date",inplace= True)
#retail_sales.rename({"value":"retail_sales"},axis = 1 , inplace = True)

#print("step6")

#indicator_data = pd.merge(retail_sales   , unemployment_rate     , how = "inner" , on = "date" )
#indicator_data = pd.merge(indicator_data , consumer_sentiment    , how = "inner" , on = "date" )
#indicator_data = pd.merge(indicator_data , durable_goods         , how = "inner" , on = "date" )
#indicator_data = pd.merge(indicator_data , fed_fund_rate         , how = "inner" , on = "date" )
#indicator_data = pd.merge(indicator_data , cpi                   , how = "inner" , on = "date" )
#indicator_data = pd.merge(indicator_data , expectation_inflation , how = "inner" , on = "date" )
 


data = pd.merge(years10,
         month3,
         how = "inner" ,
         on = "Date")


font = {'family': 'serif',
        'color':  'darkgreen',
        'weight': 'normal',
        'size': 16,
        }


st.set_page_config(layout="wide")
st.header("Market Watch")

start_date = st.sidebar.date_input("Start Date:",
        date(2020,1,1),
        key="start_dates",
        min_value = date(2000, 1, 6)) 
start_month = start_date.strftime('%Y-%m')
start_month = str(start_month+"-01")
start_month = datetime.strptime(start_month, '%Y-%m-%d').date()

print("start_month: ",start_month)
end_date = st.sidebar.date_input("End Date:",
        date(2021,9,7),
        key = "end_dates"  )
end_month = end_date.strftime('%Y-%m')
end_month = str(end_month+"-01")
end_month = datetime.strptime(end_month, '%Y-%m-%d').date()
print("end_month: ",end_month)
###statistics
#standard_deviation = np.std(data.loc[start_date:end_date].Price10y)
#average = np.mean(data.loc[start_date:end_date].Price10y)
#diffrence_percent = (data.loc[str(end_date)].Price10y - data.loc[str(start_date)].Price10y)*100 / data.loc[str(start_date)].Price10y
#diffrence = data.loc[str(end_date)].Price10y - data.loc[str(start_date)].Price10y


###plot treasury Bond yield
fig, ax = plt.subplots(figsize=(12,7))

ax.plot(data.Price10y,
        color = "g")

ax.plot(data.Price3m,
        color = "b")

ax.fill_between(x=data.index,y1=data.Price10y,y2 = data.Price3m ,
                where= np.array(data.Price10y)<np.array(data.Price3m),
                alpha=0.7,color = "r",
                interpolate=True)

fig.autofmt_xdate()
ax.set_xlim([start_date,end_date])
ax.set_ylim([min(data.loc[start_date:end_date].Price3m)-0.1 , max(data.loc[start_date:end_date].Price10y)+0.3])

plt.ylabel("Yield Curve Rates",
        fontdict = font)

plt.title("Daily Treasury Yield Curve Rates " ,
         fontdict = font)

plt.legend(["10Years","3Month"] ,
         loc = "best")

## recessoins
##2020
plt.axvspan(date(2020,2,10),
         date(2020,3,20),
         alpha=0.03,
         color='r')
##2008-2009
plt.axvspan(date(2007,10,10),
         date(2009,1,20),
         alpha=0.03,
         color='r')
##2001
plt.axvspan(date(2001,2,1),
         date(2001,10,20),
         alpha=0.03,
         color='r')

fig.tight_layout()
#plt.show()
st.pyplot(plt)



#### plot economics indicators
fig, ax = plt.subplots(figsize=(11,1))
plt.title('Economics Indicators')

## inflation rate
ax.bar(indicator_data.index, indicator_data.expectation_inflation,color = "b", width = 20)
plt.title('Expectation Inflation')
fig.autofmt_xdate()
ax.set_xlim([start_month,end_month])
ax.set_ylim([min(indicator_data.loc[start_month:end_month].expectation_inflation) , max(indicator_data.loc[start_month:end_month].expectation_inflation)+0.3])
plt.axvspan(date(2020,2,10),
         date(2020,3,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2007,10,10),
         date(2009,1,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2001,2,1),
         date(2001,10,20),
         alpha=0.03,
         color='r')
#plt.show()
st.pyplot(plt)

## durable goods
fig, ax = plt.subplots(figsize=(11,1))
ax.bar(indicator_data.index, indicator_data.durable_goods/100000,color = "y",width = 20)
plt.title('Durable Goods(10e5)')
fig.autofmt_xdate()
ax.set_xlim([start_date,end_date])
ax.set_ylim([min(indicator_data.loc[start_date:end_date].durable_goods/100000) , max(indicator_data.loc[start_date:end_date].durable_goods/100000)+0.3])
plt.axvspan(date(2020,2,10),
         date(2020,3,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2007,10,10),
         date(2009,1,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2001,2,1),
         date(2001,10,20),
         alpha=0.03,
         color='r')
#plt.show()
st.pyplot(plt)

## unemployment rate
fig, ax = plt.subplots(figsize=(11,1))
ax.bar(indicator_data.index, indicator_data.unemployment_rate, color = "g",width = 20)
plt.title('Unemplyment Rate')
fig.autofmt_xdate()
ax.set_xlim([start_date,end_date])
ax.set_ylim([min(indicator_data.loc[start_date:end_date].unemployment_rate), max(indicator_data.loc[start_date:end_date].unemployment_rate)+0.3])
plt.axvspan(date(2020,2,10),
         date(2020,3,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2007,10,10),
         date(2009,1,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2001,2,1),
         date(2001,10,20),
         alpha=0.03,
         color='r')
#plt.show()
st.pyplot(plt)

## fed fund rate
fig, ax = plt.subplots(figsize=(11,1))
ax.bar(indicator_data.index,indicator_data.fed_fund_rate, color = "pink",width = 20)
plt.title('FED Fund Rate')
fig.autofmt_xdate()
ax.set_xlim([start_date,end_date])
ax.set_ylim([min(indicator_data.loc[start_date:end_date].fed_fund_rate) , max(indicator_data.loc[start_date:end_date].fed_fund_rate)+0.3])
plt.axvspan(date(2020,2,10),
         date(2020,3,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2007,10,10),
         date(2009,1,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2001,2,1),
         date(2001,10,20),
         alpha=0.03,
         color='r')
#plt.show()
st.pyplot(plt)

##retail sale
fig, ax = plt.subplots(figsize=(11,1))
ax.bar(indicator_data.index,indicator_data.retail_sales/100000, color = "coral",width = 20)
plt.title('Retail Sales (10e5)')
fig.autofmt_xdate()
ax.set_xlim([start_date,end_date])
ax.set_ylim([min(indicator_data.loc[start_date:end_date].retail_sales/100000), max(indicator_data.loc[start_date:end_date].retail_sales/100000)+0.3])
plt.axvspan(date(2020,2,10),
         date(2020,3,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2007,10,10),
         date(2009,1,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2001,2,1),
         date(2001,10,20),
         alpha=0.03,
         color='r')
#plt.show()
st.pyplot(plt)

## consumer sentiment
fig, ax = plt.subplots(figsize=(11,1))
ax.bar(indicator_data.index,indicator_data.consumer_sentiment, color = "khaki",width = 20)
plt.title('Costumer Sentiment')
fig.autofmt_xdate()
ax.set_xlim([start_date,end_date])
ax.set_ylim([min(indicator_data.loc[start_date:end_date].consumer_sentiment) , max(indicator_data.loc[start_date:end_date].consumer_sentiment)+0.3])
plt.axvspan(date(2020,2,10),
         date(2020,3,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2007,10,10),
         date(2009,1,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2001,2,1),
         date(2001,10,20),
         alpha=0.03,
         color='r')
#plt.show()
st.pyplot(plt)

## cpi
fig, ax = plt.subplots(figsize=(11,1))
ax.bar(indicator_data.index,indicator_data.cpi, color = "teal",width = 20)
plt.title('CPI')
fig.autofmt_xdate()
ax.set_xlim([start_date,end_date])
ax.set_ylim([min(indicator_data.loc[start_date:end_date].cpi) , max(indicator_data.loc[start_date:end_date].cpi)+1])
plt.axvspan(date(2020,2,10),
         date(2020,3,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2007,10,10),
         date(2009,1,20),
         alpha=0.03,
         color='r')
plt.axvspan(date(2001,2,1),
         date(2001,10,20),
         alpha=0.03,
         color='r')

#plt.show()
st.pyplot(plt)















#col1, col2, col3 = st.columns(3)

#col1.write(' 10Years Treasury Yeild  ')
#col1.metric("Diffrence", str(round(diffrence,2)) , str(str(round(diffrence_percent,2))+"%") )
#col2.metric("Mean ", str(round(average,2)))
#col3.metric("Standars Deviation", str(round(standard_deviation,2)))

#st.write('3Month Treasury Yield')
#col1.metric("Diffrence", str(round(diffrence,2)) , str(str(round(diffrence_percent,2))+"%") )
#col2.metric("Mean ", str(round(average,2)))
#col3.metric("Standars Deviation", str(round(standard_deviation,2)))








st.write("Better Call Seraj: serajrazmi0@gmail.com")
