import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds=pd.read_csv("C:/Users/Aasimmiya saiyed/Desktop/telco_cleaned.csv")

churn_customers=pd.read_csv("C:/Users/Aasimmiya saiyed/Documents/total_churn_customer_table.csv")
print(churn_customers)

churn_contract=pd.read_csv("C:/Users/Aasimmiya saiyed/Documents/contract_validity_table.csv")
print(churn_contract)

monthly_charge=pd.read_csv("C:/Users/Aasimmiya saiyed/Documents/monthly_chargesby internet service_table.csv")
print(monthly_charge)

churn_tenure=pd.read_csv("C:/Users/Aasimmiya saiyed/Documents/churn by tenure table.csv")
print(churn_tenure)

sns.barplot(x=churn_contract["Contract"],y=churn_contract["Total_Churn_Customers"])
plt.show()

sns.boxplot(x="Churn Value",y="Monthly Charges",data=ds)
plt.show()

sns.lineplot(x="Tenure Months",y="Churn Score",data=ds)
plt.show()

cols=ds[['Monthly Charges','Tenure Months','Total Charges']]

corr=cols.corr()

sns.heatmap(corr)
plt.show()


count=ds["Churn Value"].value_counts()
plt.pie(count,data=ds,labels=count.index,autopct='%1.1f%%')
plt.show()

total_customers=ds["Churn Value"].count()

churned_customers=ds[ds["Churn Value"]==1].count()["Churn Value"]

churn_rate=(churned_customers/total_customers)*100
print(churn_rate)

avg_monthly_charges=ds.groupby("Churn Value")["Monthly Charges"].mean()
print(avg_monthly_charges)