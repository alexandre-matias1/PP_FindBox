import pandas as pd


cod = '14J7745326'

df = pd.read_csv(
    'arquivo.csv',
    encoding='windows-1252',
    sep=';',
    usecols=['Data de Integração','Data de Desvio', 'Direção Desvio','Largura'],
)
 



df = df.rename(columns={'Data de Integração':'Cubometro'})
df = df.rename(columns={'Data de Desvio':'Desvio'})
df = df.rename(columns={'Direção Desvio':'Praça'})
df = df.rename(columns={'Largura':'Código de barras'})



box = df.loc[df['Código de barras'] == cod]
AourB = box.iloc[1]['Desvio']


srtA= ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26','...','999']
A=['0A01', '0A02', '0A03', '0A04', '0A05', '0A06', '0A07', '0A08', '0A09', '0A10', '0A11', '0A12', '0A13', '0A14', '0A15', '0A16', '0A17', '0A18', '0A19', '0A20', '0A21', '0A22', '0A23', '0A24', '0A25', '0A26']

srtB= ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17' 'B18','...','999']
B=['0B01', '0B02', '0B03', '0B04', '0B05', '0B06', '0B07', '0B08', '0B09', '0B10', '0B11', '0B12', '0B13', '0B14', '0B15', '0B16', '0B17','0B18']

if AourB in A:
    df = df[~df['Desvio'].isin(srtA)]
    df = df[~df['Desvio'].isin(srtB)]
    df = df[~df['Desvio'].isin(B)]
else:
    df = df[~df['Desvio'].isin(srtB)]
    df = df[~df['Desvio'].isin(srtA)]
    df = df[~df['Desvio'].isin(A)]

df = df.reset_index()

countIndex = df['Código de barras'].value_counts()[cod]

if countIndex == "1":
  index = df.loc[(df['Código de barras'] == cod)].index[0]
else:
  index = df.loc[(df['Código de barras'] == cod)].iloc[countIndex-1]
  index = index.name
  message = "O volume recirculou. "


box1 = df.iloc[index-1, df.columns.get_loc('Praça')]
realBox = df.iloc[index, df.columns.get_loc('Praça')]
box2 = df.iloc[index+1, df.columns.get_loc('Praça')]


if df.iloc[index-1, df.columns.get_loc('Desvio')] == "0A09":
    box1 = "Rejeito"
    
if df.iloc[index+1, df.columns.get_loc('Desvio')] == "0A09":
    box2= "Rejeito"


if df.iloc[index-1, df.columns.get_loc('Desvio')] == "0B01":
    box1 = "Rejeito"

if df.iloc[index+1, df.columns.get_loc('Desvio')] == "0B01":
    box2 = "Rejeito"

print(f'{message}A caixa de {realBox}, pode ter caido em {box1} ou {box2}')
