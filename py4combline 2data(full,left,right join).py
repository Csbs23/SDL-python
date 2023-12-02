import pandas as pd
a=pd.DataFrame()
d={'id':[1,2,3,4],
'val1':['a','b','c','d']}
a=pd.DataFrame(d)

b=pd.DataFrame()
d={'id':[1,2,5,6],
'val1':['p','q','r','s']}
b=pd.DataFrame(d)
df=pd.merge(a,b,on='id',how='inner')
df
