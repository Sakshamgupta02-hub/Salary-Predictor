# Salary-Predictor
# Project Overview
This project predicts a person's salary based on their years of experience and education level using Machine Learning.
It demonstrates a simple and practical use of Linear Regression.

# Problem Statement
Many students and job seekers are unsure about the salary they can expect based on their qualifications.
This project helps estimate salary using basic input features.

# Solution Approach
Load dataset from CSV file
Convert categorical data (education) into numerical format using Label Encoding
Train a Linear Regression model
Take user input
Predict salary based on input

# Dataset
The dataset contains the following columns:
experience → Years of experience
education → Education level (Bachelor, Master, PhD)
salary → Salary in INR
Tech Stack
Python
Pandas
Scikit-learn
Matplotlib

# Features
Predicts salary based on user input
Uses Machine Learning model (Linear Regression)
Displays a graph (Salary vs Experience)

# Real-World Problem

In today’s job market, salary expectations are often unclear, especially for students and fresh graduates. Many individuals struggle to understand how factors like experience and education level influence their earning potential. This lack of clarity can lead to:

Accepting underpaid job offers
Unrealistic salary expectations
Poor career planning decisions

Recruiters and companies also face challenges in maintaining fair and consistent salary structures, especially when evaluating candidates with different backgrounds.

# How This Project Solves It

This project uses Machine Learning (Linear Regression) to analyze past salary data and predict expected salary based on:

Years of experience
Education level

By providing a quick and data-driven estimate, this system helps:

Students understand their market value.
Job seekers negotiate better salaries.
Organizations maintain consistency in salary decisions.

# Examples
# 1. Output:
Enter years of experience: 6
Enter education (Bachelor/Master/PhD): Master

Predicted Salary: ₹72000

# 2. Output:
Enter years of experience: 3
Enter education (Bachelor/Master/PhD): Bachelor

Predicted Salary: ₹ 42000

# 3. Output:
Enter years of experience: 9
Enter education (Bachelor/Master/PhD): PhD

Predicted Salary: ₹ 115000
