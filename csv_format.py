from datetime import datetime
import csv
import pandas as pd
import logging
#import subprocess

def change_delimiter(arquivo_csv: str, delimitador=","):
    logging.basicConfig(filename='LOG/main.log', filemode='a', encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info(f'Modificando o delimitador do aruqivo: {arquivo_csv}')

    #subprocess.Popen(f"echo 'Modificando o delimitador do aruqivo: {arquivo_csv}' >> 'LOG/log.txt'", shell=True)

    reader = csv.reader(open(f"{arquivo_csv}", "rU"), delimiter='\t')
    writer = csv.writer(open("TEMP/output.csv", "w"), delimiter=delimitador)
    writer.writerows(reader)

    logging.info('Delimitador alterado com sucesso')

    #subprocess.Popen(f"echo 'Delimitador alterado com sucesso' >> 'LOG/log.txt'", shell=True)

def insert_title(titulos: list):
    logging.basicConfig(filename='LOG/main.log', filemode='a', encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(message)s)')
    logging.info(f'Inserindo cabeçalho {str(titulos)} no arquivo: TEMP/output.csv')

    #subprocess.Popen(f"echo 'Inserindo cabecalho {str(titulos)} no aruqivo: TEMP/output.csv' >> 'LOG/log.txt'", shell=True)

    file = pd.read_csv("TEMP/output.csv")
    file.to_csv("TEMP/output.csv", header=titulos, index=False)

    logging.info('Cabecalho inserido com sucesso')

    #subprocess.Popen("echo Cabecalho inserindo com sucesso >> LOG/log.txt", shell=True)