import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"D:\alex_\Documents\Programacion\Bases de datos\Loteria Nacional\Mayor\_LLEVAR\BASE_Valores_Premios.xlsx", dtype=object)
df_mayor = df[df['PREMIO'] >= 300000]  # Compara con una cadena '300000'

df_pivot = df_mayor.pivot(index="ORIGEN", columns="PREMIO", values="Valor")
df_pivot.index = pd.to_numeric(df_pivot.index.str.replace('Mayor', ''), errors='coerce')

plt.plot(df_pivot[300000])
plt.xlabel('Año')
plt.ylabel('Valor')
plt.title('Plot de Premio 300000 por Año')
plt.show()
