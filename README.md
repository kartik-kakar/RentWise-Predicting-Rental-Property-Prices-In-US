<div align="center">

# 📈 RentWise: Predicting Rental Property Prices in US

<img align="center" src="https://github.com/kartik-kakar/US-Rental-Housing-Prediction/blob/db230e419eefd649fcedb277237c01697aa6615e/RentWise%20Logo.png" title="RentWise" width="700" height="400">

</div>


## 🏠 Introduction

Welcome to the "RentWise" a US Rental price prediction project, where we delve into the intricate world of rental property pricing in the United States. In this data-driven endeavor, we harness the power of data science techniques, including Linear Regression and Decision Trees, to shed light on the dynamics of rental housing prices. Our ultimate objective is to develop a robust predictive model that can accurately estimate these prices, offering invaluable insights for renters, landlords, and the ever-evolving real estate industry.


## 🎯 Project Overview

The project's primary focus is to leverage machine learning to tackle the complex challenges associated with rental housing pricing. We aim to answer pressing questions, such as:

1. What factors influence rental property prices in different regions of the United States?
2. Can we build a model that accurately predicts rental prices?
3. How do amenities, location, and property types affect the cost of rent?
4. What insights can we extract from the data to inform both renters and landlords?


## 📊 Dataset

The dataset comes from **Kaggle**, a famous site with thousands of amazing datasets to work it. Each row represents a unique Rental property in different states of US, and each column a different attribute. Some of the key features in my dataset are:

<div align="center">

| #   | Columns                  | Description                                           | Dtype    |
| --- | ------------------------ | ----------------------------------------------------- | -------- |
| 1   | region                   | Craigslist region                                    | object   |
| 2   | price                    | Rent per month (Target Column)                       | int64    |
| 3   | type                     | Housing type                                         | object   |
| 4   | sqfeet                   | Total square footage                                 | int64    |
| 5   | beds                     | Number of Beds                                       | int64    |
| 6   | baths                    | Number of Bathrooms                                  | float64  |
| 7   | cats_allowed             | Cats allowed boolean (1 = yes, 0 = no)               | int64    |
| 8   | dogs_allowed             | Dogs allowed boolean (1 = yes, 0 = no)               | int64    |
| 9   | smoking_allowed          | Smoking allowed boolean (1 = yes, 0 = no)            | int64    |
| 10  | wheelchair_access        | Has wheelchair access boolean (1 = yes, 0 = no)      | int64    |
| 11  | electric_vehicle_charge  | Has electric vehicle charger boolean (1 = yes, 0 = no)| int64    |
| 12  | comes_furnished          | Comes with furniture boolean (1 = yes, 0 = no)       | int64    |
| 13  | laundry_options          | Laundry options available                            | object   |
| 14  | parking_options          | Parking options available                            | object   |
| 15  | state                    | State of listing                                     | object   |

</div>




## 🚀 Roadmap

  - ### 🧹 [Data Cleaning](https://github.com/kartik-kakar/RentWise-Predicting-Rental-Property-Prices-In-US/blob/37ec38d5514f697f7f2a22d29b820da12f05bae9/1.%20Data_Cleaning.ipynb)
       It involved cleaning the raw dataset ensuring that the data is ready for analysis. We dropped the unecessary columns and dealt with missing 'NaN' values. Then we saved the cleaned dataset file to use for 
       further EDA.

  - ### 🕵️‍♂️ [Exploratory Data Analysis (EDA)](https://github.com/kartik-kakar/RentWise-Predicting-Rental-Property-Prices-In-US/blob/9558fd78019ddd15a0bda9d723c69bdd4251874b/2.%20EDA.ipynb)
       We investigated the dataset's characteristics, relationships, and patterns using visualizations and statistical techniques, providing insights for model selection and feature engineering. We removed the 
       outliers from our dataset to get more realilstic findings and saved up our modified file for future use. 

  - ### 🧠 Feature Engineering and 📊 Modelling
       Next, we focused on data transformation and data splitting, prepared the dataset for model training and ensuring that features are meaningful and suitable for machine learning.

  - ### 📊 Modeling
       It will invlove selecting, training, and evaluating machine learning models to predict rental housing prices, aiming to create an accurate and interpretable predictive model.
       We will be testing and evaluating various models, including:
          - Logistic Regression
          - Decision Tree

## 📝 Learnings

Till now, we have cleaned our dataset and decided our Target variable, i.e, 'price' and have made a lot of visualization revealing the relationships between different variables.














