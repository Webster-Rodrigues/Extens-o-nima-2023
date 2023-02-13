
#Bibliotecas usadas

import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Font, Color, Alignment

crimes_violentos_df = pd.read_excel("crimes_violentos_2022.xlsx")
crimes_violentos_df.head()


estupro_C_df = crimes_violentos_df.loc[crimes_violentos_df["NATUREZA"] == "Estupro Consumado"]
quantidade_crimesViolentos_df = crimes_violentos_df[["REGISTROS", "NATUREZA"]].groupby(by = "NATUREZA").sum()
quantidade_crimesViolentos_df.sort_values(by = "REGISTROS",axis = 0, ascending = True, inplace = True, na_position ='first')
print(quantidade_crimesViolentos_df)



quantidade_crimesViolentos_df.plot(
    kind="barh",
    xlabel="Quantidade de registro",
    ylabel="Tipos de crime",
    title="Crimes violentos",
    color="red",
    alpha=0.3,
    figsize=(15,5)
)


plt.grid()
plt.show()


