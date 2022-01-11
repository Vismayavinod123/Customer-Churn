import numpy as np
import pandas as pd
df = pd.read_csv("E:/cell2celltrain.csv")

# filling nan values with most frequent value in column
df = df.fillna(df.mode().iloc[0])

#Preprocessing

from sklearn.preprocessing import LabelEncoder
#Encode Categorical Columns
le=LabelEncoder()
for col in df.columns.values:
    if df[col].dtypes=='object':
        le.fit(df[col].values)
        df[col]=le.transform(df[col])


# Removing outliers
#filtering out negative values
df2 = df[df.MonthlyRevenue>=0]
df3 = df2[df2.TotalRecurringCharge>=0]

df4 = df3.drop(["ServiceArea","AgeHH1","AgeHH2","OptOutMailings","NonUSTravel","OwnsComputer","RetentionCalls","RetentionOffersAccepted","NotNewCellphoneUser","ReferralsMadeBySubscriber","OwnsMotorcycle",'AdjustmentsToCreditRating','MadeCallToRetentionTeam',"RVOwner","TruckOwner"],axis=1)




#******************************************
# Model

#df_notChurn = df.drop(["CustomerID","Churn"],axis=1)
#X=df_notChurn
#y=df['Churn']
from sklearn.model_selection import train_test_split
df5 = df4.drop(["CustomerID","Churn"],axis=1)

from sklearn.decomposition import PCA
pca = PCA(20)
X_new = pca.fit_transform(df5)
X_new_df = pd.DataFrame(X_new)
print(X_new_df.head())
print(X_new_df.shape)

X=X_new
y=df4['Churn']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()

rf.fit(X_train,y_train)
predictions=rf.predict(X_test)

print (accuracy_score(y_test,predictions))
print(confusion_matrix(y_test,predictions))