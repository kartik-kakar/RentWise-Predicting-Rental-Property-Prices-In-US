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

  - ### 🧠 [Feature Engineering and Baseline Modelling](https://github.com/kartik-kakar/RentWise-Predicting-Rental-Property-Prices-In-US/blob/837bad4d8022c027cdf9f67be33044eac8880ad7/3.%20Feature_Engineering_Baseline_modelling_Hyperparamter_Tuning_Making_Predictions.ipynb)
       Next, we focused on data transformation, converted all the categorical columns to numerical ones ensuring that features are meaningful and suitable for machine learning. Then, we split our data into test and train set, prepared for model training and tried out the following models on the entire dataset:
    -  Linear Regression
    -  Ridge Regression
    -  Lasso Regression
    -  Decision Tree
    -  Random Forest
    -  Neural Network Regressor

      We then scaled our dataset, ran the models again and compared them using the R2 and MSE metric.

  - ### 📊 [Hyperparameter Tuning](https://github.com/kartik-kakar/RentWise-Predicting-Rental-Property-Prices-In-US/blob/837bad4d8022c027cdf9f67be33044eac8880ad7/3.%20Feature_Engineering_Baseline_modelling_Hyperparamter_Tuning_Making_Predictions.ipynb)
    After comparison, we learned that the Random Forest Regressor model consistently demonstrates superior predictive accuracy and generalization having the highest
    R2 Score of more than 84.00% both before and after scaling. Then, we proceeded to tune the hyperparameters and found the following ones best:
    - no. of components: 380
    - optimal maximum depth: 140
    - minimum samples leaf: 5
    - minimum samples split: 0.01
   
    Using these parameters, we evaluated the model on our entire dataset and got some predictions:

<div align="center">

| # | Region          | Type       | SqFeet | Beds | Baths | Cats Allowed | Dogs Allowed | Smoking Allowed | Wheelchair Access | Electric Vehicle Charge | Comes Furnished | Laundry Options | Parking Options      | State | Predicted Price |
|---|-----------------|------------|--------|------|-------|--------------|--------------|------------------|-------------------|--------------------------|------------------|------------------|-----------------------|-------|------------------|
| 1 | reno / tahoe    | apartment  | 1001   | 2    | 2     | 0            | 0            | 0                | 0                 | 0                        | 0                | w/d hookups      | carport               | CA    | **2360.14**      |
| 2 | hickory / lenoir | apartment  | 1190   | 2    | 2     | 1            | 1            | 0                | 0                 | 0                        | 0                | w/d hookups      | off-street parking    | NC    | **1246.26**      |
| 3 | rhode island     | apartment  | 900    | 2    | 1     | 1            | 1            | 1                | 1                 | 0                        | 0                | w/d in unit      | off-street parking    | RI    | **2016.00**      |
| 4 | reno / tahoe    | apartment  | 1000   | 3    | 2     | 1            | 1            | 0                | 0                 | 0                        | 0                | w/d in unit      | carport               | AL    | **1396.94**      |

</div>

   
## 📝 Learnings and Conclusion
    
In conclusion, this project has successfully developed a robust predictive model for US property prices by leveraging the entire dataset. Beginning with comprehensive data cleaning        and preprocessing, the exploration of various features through exploratory data analysis (EDA) shed light on influential factors such as property type, square footage, and amenities       affecting pricing dynamics. Notably, our model, based on a Random Forest algorithm, demonstrated exceptional predictive performance both before and after scaling.

To expedite the hyperparameter tuning process, the dataset was initially sampled to 50,000 rows, achieving a favorable balance between computational efficiency and model accuracy. Further analysis involved refining the Random Forest model's hyperparameters, particularly setting the optimal maximum depth to 140. A subsequent grid search facilitated the identification of the best hyperparameters, resulting in a finely tuned model with a cross-validated score of 0.60.

The conclusive evaluation on the test set affirmed the model's efficacy, yielding a Mean Squared Error of 114,439 and an R-squared value of 0.62. These metrics signify the model's ability to make accurate predictions, laying a strong foundation for its real-world applicability.

Notably, after training our model on the entire dataset, the predictions demonstrated remarkable closeness to the actual answers present in the dataset. This performance enhancement further solidifies the model's reliability, offering valuable insights for stakeholders in the dynamic real estate market.

Applying the model to practical scenarios, we made predictions for four diverse property examples, incorporating features like region, type, square footage, and more. The resulting predictions underscore the model's reliability, offering valuable insights for stakeholders in the dynamic real estate market.

In essence, this project not only delivers an advanced predictive model for property prices but also underscores the significance of extensive training on the entire dataset. The combination of feature engineering, hyperparameter tuning, and meticulous model evaluation contributes to the development of accurate and dependable machine learning applications, addressing real-world challenges in the realm of real estate.

