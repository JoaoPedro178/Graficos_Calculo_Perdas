import os
import pandas as pd
import calendar
import numpy as np
import locale

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
