#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, pickle


# Classe responsável por apenas Ler e Escrever => R (read) e W (write)
class RW:

	def __init__(self, path_store = ''):

		self.path_store = path_store;

	def save(self, data = {}, nome_arquivo = 'nome_arquivo'):

		try:

			nome_arquivo = nome_arquivo.replace(' ', '_')

			file = open(self.path_store + nome_arquivo + '.txt','wb') 	# Abrir o arquivo para gravação - o "b" significa que o arquivo é binário
			pickle.dump(data, file) 									# Grava uma stream do objeto "file" para o arquivo.
			file.close() 												# Fechar o arquivo

			return 'Arquivo ' + nome_arquivo + ' salvo com sucesso.'

		except Exception as e:

			return False

	def read(self, nome_arquivo):

		try:

			file = open(self.path_store + nome_arquivo + '.txt','rb') 	# Abrir o arquivo para leitura - o "b" significa que o arquivo é binário
			data = pickle.load(file)									# Ler a stream a partir do arquivo e reconstroi o objeto original.
			file.close() 												# Fechar o arquivo
			return data 												# Retorna o conteúdo do dicionário

		except Exception as e:

			return False


sys.modules[__name__] = RW