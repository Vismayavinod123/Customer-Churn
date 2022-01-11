# Customer-Churn

INTRODUCTION

 -Churn refers to the situation where a customer stops subscribing the service.
 -Churn prediction plays a key role for service providing companies.
 -Average cost to create a new customer is 5 to 25 times more compared to that of retaining existing customers.
 -Churn is predominant in telecom industry.
 
 CHURN PARAMETERS:
 -Customer demography    
		 Age, Income, Occupation, Marital status
 -Spend tendencies   
		Vehicle ownership, Credit Rating, Purchases via mail order
 - Calling tendencies 
	               Three way calls, Peak and off peak calls, Roaming calls
 - Bill and Subscription details
		 Monthly revenue, Total recurring charge,
		 Total months in use, Active subscription etc


Data Pre-processing

Missing value imputation
	- Replaced missing values with most frequent values in the column.
 Outlier Removal
    	- Removed rows containing negative values in certain columns 
		- Monthly Revenue
 		- Total Recurring charge
- Feature Sub-selection
- More than 95% of values contained in the column were singular.
- Label Encoding 
      Majority of categorical columns had limited number of categories.
      Credit Rating and Occupation columns consists of more than 6 categories. 
      Encoding of the attributes didn’t alter the performance of the model.  
- Modified Dataset Dimensions – 51038 X 41
- Feature Standardization
      Used Standard Scaler transformation
 

Model Building

- Train Set – 90%
- Test Set – 10%
- Comparative Analysis of algorithms on dataset: 
                K-Nearest Neighbours = 67.6
                Logistic Regression = 71.2
                Naïve Bayes= 53.5
                Decision Trees =62
                Random Forest =70.7

We took Random Forest
  - GridSearchCV
  - max_depth ={2,3,6}	
  - n_estimators={100,200,300,400,600}
  - Best Accuracy – 71.9%

 Conclusion
 - Analysed the main variables and factors influencing telecom customer churn. 
- Customer demographic features found to be less effective for the given dataset.
- Random Forest classifier gives best result.
- Accuracy of the model can be improved further with balanced dataset. 





