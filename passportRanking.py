# Standard import
import numpy as np 
import pandas as pd 
from pandas import DataFrame, Series
from pandas.io.json import json_normalize

# Plotting
import matplotlib as mpl 
import matplotlib.pyplot as plt
import seaborn as sns 

import json

# json file of countries and their continent https://raw.githubusercontent.com/annexare/Countries/master/countries.json
df = pd.read_json('countries.json',orient='DataFrame')
cc = df['countries'].apply(pd.Series)

# countries and the number of countries their passports can access, exported manually to csv 
#from http://www.atlasandboots.com/best-passport-to-have/
rankingpd = pd.DataFrame(pd.read_csv('/home/toon/Documents/python_analytics/passportRanking/ranking.csv',header=0,sep=',',parse_dates=True))

# filling the empty rankings and merging the two sources based on country name
df = rankingpd.fillna(method="ffill")
cc.columns = ['na','capital','continent','currency','languages','COUNTRY','native','phone']
newpd = pd.merge(df,cc,on='COUNTRY')

# plot out the countries and continents and their access ranking
ax = sns.stripplot(x="continent", y="ACCESSIBLE", data=newpd,linewidth=0,hue='COUNTRY',jitter=True);
ax.legend_.remove()
plt.show();
