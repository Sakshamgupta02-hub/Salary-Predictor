import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("salary_data.csv")

# Encode education
le = LabelEncoder()
df['education'] = le.fit_transform(df['education'])

# Features & target
X = df[['experience', 'education']]
y = df['salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# Graph (experience vs salary)
plt.scatter(df['experience'], df['salary'])
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.show()

# User input
exp = float(input("Enter experience: "))
edu = input("Enter education (Bachelor/Master/PhD): ")

edu_encoded = le.transform([edu])[0]

prediction = model.predict([[exp, edu_encoded]])

print("Predicted Salary: ₹", int(prediction[0]))
