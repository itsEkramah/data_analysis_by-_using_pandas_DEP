import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('employees.csv')  # Use the filename from the uploaded file

# Display basic information about the dataset
print("Dataset Information:")
df.info()

print("\nFirst 5 Rows of the Dataset:")
print(df.head())

print("\nStatistical Summary of the Dataset:")
print(df.describe())

# Check for missing values
print("\nMissing Values in the Dataset:")
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Gender distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=df, palette='pastel')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.savefig('gender_distribution.png')  # Save the plot as an image
plt.show()

# Average salary by gender
plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='Salary', data=df, palette='husl')
plt.title('Average Salary by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.savefig('average_salary_by_gender.png')  # Save the plot as an image
plt.show()

# Salary distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Salary'], kde=True, color='green')
plt.title('Salary Distribution of Employees')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.savefig('salary_distribution.png')  # Save the plot as an image
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='viridis', fmt='.2f')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')  # Save the plot as an image
plt.show()

# Salary vs. Experience scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Experience', y='Salary', data=df, hue='Gender', palette='deep')
plt.title('Salary vs. Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.savefig('salary_vs_experience.png')  # Save the plot as an image
plt.show()

# Box plot of Salary by Gender
plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Salary', data=df, palette='Spectral')
plt.title('Box Plot of Salary by Gender')
plt.xlabel('Gender')
plt.ylabel('Salary')
plt.savefig('box_plot_salary_by_gender.png')  # Save the plot as an image
plt.show()
