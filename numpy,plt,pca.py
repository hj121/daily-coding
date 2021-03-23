# TODAY REVIEW! Mar.23.2021
# numpy, plt practice
import numpy as np
import matplotlib.pyplot as plt
height = np.round(np.random.normal(70,3,10000),2)
plt.hist(height, bins = 50)
plt.show()
print(np.median(height))

import seaborn as sns
sns.relplot(x='RM', y='MEDV', data = df, kind = 'scatter')
plt.show()

df.MEDV.hist()
plt.xlabel('MEDV')
plt.ylabel('count')
plt.show()

# time series data
import pandas as pd
data_url = 'http://covidtracking.com/api/states/daily.csv'
covid = pd.read_csv(data_url, parse_dates=['date'])

covid_ny = covid[(covid['state']=='NY') & (covid['date']>='2021-01-01')]

# time sereis plot with seaborn lineplot()
sns.lineplot(x='date', y='positiveIncrease', data = covid_ny)
#axis labels
plt.title('NY Covid-tracking 2021')
plt.xlabel('Date')
plt.ylabel('Positive')
plt.xticks(rotation = 70)

import dtale
import pandas as pd
dtale.show(pd.read_csv('file.csv')
           
# exploring the date
bostonHousing_df = pd.read_csv('BostonHousing.csv')
bostonHousing_df = bostonHousing_df.rename(columns = {'CAT.MEDV':'CAT_MEDV'}) # 이름 변경하기 fix name for CAT.MEDV
           pd.DataFrameI{'mean':bostonHousing_df.mean(),
                         'sd':bostonHousing_df.std(),
                         'min':bostonHousing_df.min(),
                         'max':bostonHousing_df.max(),
                         'median':bostonHousing_df.median(),
                         'length':len(bostonHousing_df),
                         'miss.val':bostonHousing_df.isnull().sum()
                        })

#correlation matrix for boston housing data
bostonHousing_df.corr().round(2)
'''   CRIM    ZM    INDUS   CHAS  
CRIM  1.00   -0.20  0.41    -0.06 
ZN    -0.20  1.00  -0.53    -0.04
INDUS 0.41   -0.53 -0.04     0.06
CHAS'''

# Pandas using_counts
bostonHousing_df.CHAS.value_counts()
'''0    1
   471  35'''

# PCA (Principle Components Ananlysis): - reduce the overlap of numerical variables
pcs = PCA(n_components = 2)
pcs.fit(cereals_df[['calories','rating']])


                        
                 


   
           
