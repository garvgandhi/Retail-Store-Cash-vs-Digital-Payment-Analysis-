import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv ("project_dataset.csv")
df["Period"] = df["Year"].astype(str) + "-" + df["Quarter"].astype(str)
df = df.sort_values(by=["Year", "Quarter"])


#Pie chart analysis
total_cash = df["Cash_payment"].sum()
total_digital = df["Digital_payment"].sum()

plt.figure()
plt.pie(
    [total_cash, total_digital],
    labels=["Cash", "Digital"],
    autopct="%1.1f%%"
)
plt.title("Overall Payment Mode Distribution (2018-2025)")
plt.show()

#Trend analysis
plt.figure(figsize=(12, 6))
plt.plot(df["Period"], df["Cash_payment"], label="Cash")
plt.plot(df["Period"], df["Digital_payment"], label="Digital")
plt.xticks(rotation=90)
plt.xlabel("Time")
plt.ylabel("Numbers of payment")
plt.title("Cash vs Digital Payment Trend")
plt.legend()
plt.tight_layout()
plt.show()


