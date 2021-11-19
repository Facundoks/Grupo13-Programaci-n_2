import pandas as pd
from pandas import DataFrame

dfl = pd.read_csv(f"../Database/DB_evento.csv")
df = DataFrame(dfl, columns= ['Tipo', 'Coordenada_x','Coordenada_y', 'Estado', 'Participantes'])

evento_3 = dfl.nlargest(3, 'Participantes')
evento_3.to_csv("../Mapas/DB_3eventos.csv", index=False)

ranking_100 = dfl.nlargest(100, 'Participantes')
ranking_100.to_csv("../Mapas/DB_RankingEventos.csv", index=False)


