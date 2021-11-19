import pandas as pd
import seaborn as sns

from pylab import *

df = pd.read_csv("../Database/DB_mapa2.csv",index_col=0)
df.head(10)

###Mapa de calor
plt.figure(figsize =(10,5))
mapa = sns.heatmap(df,cmap='BuPu')
figure = mapa.get_figure()
figure.savefig('Mapa_hecho.png',dpi=200)
