import numpy as np
import pandas as pd
sum=0
sum1=0
sum2=0
sum3=0
student_scores = pd.read_csv("C:/Users/vijay/OneDrive/Documents/c-programs/newdataset.csv")
print("The average sales for the mont january is",np.mean(student_scores.price))
t=np.sum(student_scores.price)
print("the total sales in the month of january is",t)
t1=np.sum(student_scores.product)
print("the total number of products sold in the month of january is",t1)
