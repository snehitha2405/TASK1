import pandas as pd
df = pd.read_csv("employee_data.csv")
print(df)
print("\nFirst 5 rows:")
print(df.head())

print("\nAverage Performance Score:")
print(df["Performance Score"].mean())

print("\nHighest Performance Score:")
print(df["Performance Score"].max())

print("\nLowest Performance Score:")
print(df["Performance Score"].min())

print("\nAverage Performance by Department:")
print(df.groupby("Department")["Performance Score"].mean())

avg_performance = df.groupby("Department")["Performance Score"].mean()

import matplotlib.pyplot as plt

avg_performance.plot(kind="bar")

plt.title("Average Performance by Department")
plt.xlabel("Department")
plt.ylabel("Average Performance Score")

plt.show()

plt.scatter(df["Attendance"], df["Performance Score"])

plt.title("Attendance vs Performance Score")
plt.xlabel("Attendance")
plt.ylabel("Performance Score")

plt.show()

correlation = df[
    ["Experience", "Attendance", "Tasks Completed", "Performance Score"]
].corr()

import seaborn as sns

sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()