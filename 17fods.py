import string
import pandas as pd
import matplotlib.pyplot as plt
def pre(nw):
    nw=nw.translate(maketrans('','',string.punctuation()))
    return nw.lower()
def freq(data):
    dic={}
    for i in data:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic
def n_values(sorts,n):
    li=[]
    for i in sorts:
        li.append(i)
    t=sorted(li)
    for i in range(n):
        print(li[i])
def barplot(freq,words):
    plt.bar(freq,words)
    plt.title("testing")
    plt.show()
data1=pd.read_csv("C:/Users/vijay/OneDrive/Documents/c-programs/customer_feeback-Vijay.csv")
data=data1["feedback"]
dicy=freq(data)
n=int(input("enter n values"))
sorts=dicy.values()
n_values(sorts,n)
freq=dicy.keys()
words=dicy.values()
barplot(freq,words)

