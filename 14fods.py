import pandas as pd
def calc(demi):
    cunt=demi['age'].value_counts()
    return cunt
r=pd.read_csv("customer34_data.csv")
actual=calc(r)
print("the frequency is")
print(actual)