import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import locale
import calendar
import os

def create_graphic():
    conteudo = pd.read_csv('TEMP/output.csv', sep=',')
    linhas = pd.read_json('CONFIG/configuracao-linhas.json')

    horas = np.append(np.array([f'2022-01-08 0{x}:00:00' for x in range(10)]), ([f'2022-01-08 {x+10}:00:00' for x in range(14)]))
    horas_12 = horas[:12]
    horas_24 = horas[12:]

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    meses = np.array([calendar.month_name[1+i] for i in range(12)])

    #temp = conteudo.where(conteudo['Nome'] == 'LT 230KV IGU/BCQ').dropna()
    

    for nome in linhas['nome']:

        temp = conteudo.where(conteudo['Nome'] == nome).dropna()
        
        for i in [12, 24]:

            if i == 12:
                dados = temp.where(temp['Hora'].isin(horas_12)).dropna()
                labels = [f'{n}h' for n in range(12)]
            else:
                dados = temp.where(temp['Hora'].isin(horas_24)).dropna()
                labels = [f'{n+12}h' for n in range(12)]

            #labels = ['EMBO/UHNP', 'USIM/UHNP', 'UHNP/ES', 'UHSS/IGU', 'IGU/BCQ']

            #men_means = [20, 34, 30, 35, 27]
            #women_means = [25, 32, 34, 20, 25]

            men_means = [random.randint(1, 100) for n in range(12)]
            women_means = [random.randint(1, 100) for n in range(12)]

            x = np.arange(len(labels))  # the label locations
            width = 0.35  # the width of the bars

            fig, ax = plt.subplots()
            rects1 = ax.bar(x - width/2, men_means, width, label='Ativa')
            rects2 = ax.bar(x + width/2, women_means, width, label='Ativa_2')

            # Add some text for labels, title and custom x-axis tick labels, etc.
            ax.set_ylabel('Potência Ativa')
            ax.set_title(nome)
            ax.set_xticks(x, labels)
            ax.legend()

            ax.bar_label(rects1, padding=3)
            ax.bar_label(rects2, padding=3)

            fig.tight_layout()

            try:
                if str(nome.index('/')):
                    nome = nome.split('/')
                    nome = '_'.join(nome)
                    plt.savefig(f'GRAPHICS/{nome}_{i}h')
            except:
                plt.savefig(f'GRAPHICS/{nome}_{i}h')

def create_dirs():
    linhas = pd.read_json('CONFIG/configuracao-linhas.json')
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    meses = np.array([calendar.month_name[1+i] for i in range(12)])

    for linha in linhas['nome'].values:
        try:
            if str(linha.index('/')):
                linha = linha.split('/')
                linha = '_'.join(linha)
            os.mkdir(f'GRAPHICS/RESULTS/{linha}')
        except FileExistsError as e:
            continue
    
    for linha in linhas['nome'].values:
        try:
            if str(linha.index('/')):
                linha = linha.split('/')
                linha = '_'.join(linha)
        finally:
            for mes in meses:
                try:
                    os.mkdir(f'GRAPHICS/RESULTS/{linha}/{mes}')
                except FileExistsError as e:
                    continue