import pandas as pd
import numpy as np
import datetime
import pyautogui

data = pd.read_csv('TEMP/output.csv', sep=',')
linhas = pd.read_json('CONFIG/configuracao-linhas.json')

#print((data['Nome'] == 'LT 500KV EMBO/UHNP C2'))

#print(linhas['nome'])


"""
for i in linhas['nome']:
    temp = data.where(data['Nome'] == i).dropna()
"""

temp = data.where(data['Nome'] == 'LT 230KV IGU/BCQ').dropna()

#print(data.iloc[:, 4])

"""
for i in data.iloc[:, 4]:
    print(datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S") < datetime.datetime.today())
"""

#mes = pyautogui.prompt(text='Digite o mês 1...12', title='Mês dos Dados', default='')
#dia = pyautogui.prompt(text='Digite o dia', title='Dia dos Dados', default='')

arr = np.array([
    (datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')) for x in temp.iloc[:, 4] if (
        (datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')).month == 1 and  (datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')).day == 8
    )
])

#horas = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

#print(temp.where(temp['Hora'][:7] == '2022-01-09 00:00:00').dropna())

horas = np.append(np.array([f'2022-01-08 0{x}:00:00' for x in range(10)]), ([f'2022-01-08 {x+10}:00:00' for x in range(14)]))
horas_12 = horas[:12]
horas_24 = horas[12:]
#horas = np.append(horas, ([f'{x}:00:00' for x in range(24)]))
#print(len(horas))
#print(horas)
print(temp.where(temp['Hora'].isin(horas)).dropna())

print(horas_24)
"""

for i in horas:
    print(temp.where(temp.iloc[:,4] == datetime.datetime.strftime(arr[0], f'%Y-%m-%d {i}:%M:%S')).dropna())
    pd.DataFrame()

"""

