"""Sales dashboard for a synthetic retail dataset."""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
base=Path(__file__).parent
df=pd.read_csv(base/'sales_sample.csv');df['date']=pd.to_datetime(df['date']);df['month']=df['date'].dt.to_period('M').astype(str)
df['profit']=df['revenue']-df['cost'];df=df.fillna({'customer_segment':'Unknown','region':'Unknown'})
print('Total revenue:',df.revenue.sum(),'Total profit:',df.profit.sum())
fig,axes=plt.subplots(2,2,figsize=(12,8))
df.groupby('month')['revenue'].sum().plot(kind='bar',ax=axes[0,0],title='Monthly Sales')
df.groupby('region')['profit'].sum().plot(kind='bar',ax=axes[0,1],title='Regional Profit')
df.groupby('product')['revenue'].sum().plot(kind='bar',ax=axes[1,0],title='Product Performance')
df.groupby('customer_segment')['revenue'].sum().plot(kind='pie',autopct='%1.0f%%',ax=axes[1,1],title='Customer Segmentation',ylabel='')
plt.tight_layout();plt.savefig(base/'sales_dashboard.png');plt.show()
df.groupby('region')[['revenue','profit']].sum().to_csv(base/'sales_summary.csv')
