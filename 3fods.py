import numpy as np
import pandas as pd
sum=0
sum1=0
sum2=0
sum3=0
student_scores = pd.read_csv("C:/Users/vijay/OneDrive/Documents/c-programs/newdataset.csv")
t=student_scores[student_scores.no_of_bedrooms>=4]
print("the average price of houses with minimum of 4 bedroom is",np.mean(t.sales_price))