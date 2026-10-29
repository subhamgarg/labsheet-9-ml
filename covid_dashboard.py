"""COVID dashboard using provided demonstration data (NOT official statistics)."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
base=Path(__file__).parent
df=pd.read_csv(base/'covid_sample.csv');df['date']=pd.to_datetime(df['date'])
print('Missing values:',df.isna().sum().to_dict())
df=df.fillna(0)
summary=df.groupby('country')[['confirmed','recovered','deaths','vaccinated']].sum()
print(summary)
fig,axes=plt.subplots(2,2,figsize=(12,8))
summary['confirmed'].plot(kind='bar',ax=axes[0,0],title='Confirmed Cases by Country')
summary[['recovered','deaths']].plot(kind='bar',ax=axes[0,1],title='Recoveries and Deaths')
df.groupby('date')['confirmed'].sum().plot(ax=axes[1,0],title='Cases over Time')
df.groupby('date')['vaccinated'].sum().plot(ax=axes[1,1],title='Vaccinations over Time')
plt.tight_layout();plt.savefig(base/'covid_dashboard.png');plt.show()
summary.to_csv(base/'covid_summary.csv')
