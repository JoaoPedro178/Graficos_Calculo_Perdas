from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib as mtp
import csv_format
import logging
#import subprocess
#import time


#subprocess.Popen("echo '' >> LOG/log.txt", shell=True)
#subprocess.Popen("date >> LOG/log.txt", shell=True)
#time.sleep(0.1)

def main():
    logging.basicConfig(filename='LOG/main.log', encoding='utf-8', filemode='a', level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info('Script iniciado')

    csv_format.change_delimiter("SRC/data-results-2022.csv", ",")
    csv_format.insert_title(["Concessao", "Nome", "Subestacao_A", "Subestacao_B", "Hora", "Valor_A", "Valor_B"])

    logging.info('Script finalizado')

if __name__ == '__main__':
    main()

"""conteudo = pd.read_csv("TEMP/output.csv", sep=",")
print(conteudo[["Nome", "Hora", "Valor_B"]])
"""

#subprocess.Popen("date >> LOG/log.txt", shell=True)