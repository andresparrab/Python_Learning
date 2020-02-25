import pandas as pd

a=pd.DataFrame({'key':['K0','K1','K2','K3'],
   'A': ['A0','A1','A2','A3'],
   'B': ['B0','B1','B2','B3']
   })

b=pd.DataFrame({'key':['K0','K1','K2','K3'],
   'C': ['C0','C1','C2','C3'],
   'D': ['D0','D1','D2','D3']
   })

#print(pd.concat([a,b]))
print(a.append(b))
print(b.append(a))