# -*- coding: utf-8 -*-
import os
from datetime import  date

"""
    Processa todos os arquivos encontrado no diretórios informado renomeando os arquivos com o Prefix que foi definido
"""

class Files:

    def __init__(self, dir_origem, prefix, tam_prefix):
        self.path       = dir_origem
        self.prefix     = prefix
        self.tam_prefix = tam_prefix

    # Processa os arquivos do diretório informado
    def ProcessFiles(self):

        INI = int(self.tam_prefix) # Define quantas posição tem o prefix
        END = None
        qtd = 0

        rel =  open('Relatorio.txt', 'w')
        rel.writelines("################ RELATÓRIO DE ARQUIVOS PROCESSADOS -  Data: {} ################\n".format(date.today()))

        # Renomeia todos os arquivos existentes no diretório informado com o Prefix que foi definido
        for file in os.listdir(self.path):
            remove_prefix = file[INI:END] # Remove o prefix de 2 carácter do início do arquivo
            novo_nome = self.prefix + remove_prefix

            # Renomeia o arquivo
            os.rename(self.path + "\\" + file, self.path + "\\" + novo_nome)
            rel.writelines("Arquivo original [{}] renomeado para [{}]\n".format(file, novo_nome))
            qtd += 1

        rel.writelines("Total de arquivos renomeados: {}".format(qtd))
        return True