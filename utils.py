import numpy as np 
import pickle
from datetime import date,datetime
import pandas as pd
trained_model = pickle.load(open("mod.pkl",'rb')) 
def preprocessdata(Date,Store,Item):
    print(Date,Store,Item)
    
    predict = [Date,Store,Item]  
    p={

        "Date": predict[0],
        "Store":predict[1],
        "Item":predict[2]
    }

    pre=pd.DataFrame([p])
    pre
    parts = pre["Date"].str.split("-", n = 3, expand = True)
    pre['Store']=pre['Store'].astype('int')
    pre['Item']=pre['Item'].astype('int')
    pre["year"]= parts[0].astype('int')
    pre["month"]= parts[1].astype('int')
    pre["day"]= parts[2].astype('int')
    pre['weekend'] = pre.apply(lambda x:weekend_or_weekday(x['year'], x['month'], x['day']), axis=1)
    pre['holidays'] = pre['Date'].apply(is_holiday)
    pre['weekday'] = pre.apply(lambda x: which_day(x['year'],x['month'],x['day']),axis=1)
    pre['m1'] = np.sin(pre['month'] * (2 * np.pi / 12))
    pre['m2'] = np.cos(pre['month'] * (2 * np.pi / 12))
    pre.drop(['Date','year'], axis=1, inplace=True)
    
    out = trained_model.predict(pre.iloc[-1:,:]) 

    return out 
def which_day(year, month, day):

    d = datetime(year,month,day)
    return d.weekday()




import holidays

def is_holiday(x):

    india_holidays = holidays.country_holidays('IN')

    if india_holidays.get(x):
        return 1
    else:
        return 0
def weekend_or_weekday(year,month,day):
    d = datetime(year,month,day)
    if d.weekday()>4:
        return 1
    else:
        return 0


