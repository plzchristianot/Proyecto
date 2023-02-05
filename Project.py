#Top 5 best-sellings phones brands in 1Q22
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#DATA    
open1Q22= pd.read_excel('brands1Q22.xlsx')
open4Q21= pd.read_excel('brands4Q21.xlsx')
open1Q21= pd.read_excel('brands1Q21.xlsx')

print("\tWELCOME TO THE LATEST SALES REPORT")
print("\nGive me the number about you want to know")
print("\nPress 1 to get the 1st Quarter of 2022 Data of the Sales Report")
print("Press 2 to get the 4th Quarter of 2021 Data of the Sales Report")
print("Press 3 to get the 1st Quarter of 2021 Data of the Sales Report")
info=int(input("\tDigite un número: \n"))
if info == 1:
    brands= open1Q22["OEM"]
    mapp=range(len(brands))
    print(open1Q22)
    open1Q22.plot(kind="bar")
    plt.xticks(mapp,brands)
    plt.suptitle("BEST SELLINGS IN THIS QUARTER")
    plt.show()
elif info == 2:
    brands= open4Q21["OEM"]
    mapp=range(len(brands))
    print(open4Q21)
    open4Q21.plot(kind="bar")
    plt.xticks(mapp,brands)
    plt.suptitle("BEST SELLINGS")
    plt.show()
elif info == 3:
    brands= open1Q21["OEM"]
    mapp=range(len(brands))
    print(open1Q21)
    open1Q21.plot(kind="bar")
    plt.xticks(mapp,brands)
    plt.suptitle("BEST SELLINGS")
    plt.show()
else :
    print("No ha seleccionado ninguna opcion correcta")

