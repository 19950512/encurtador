#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.path.abspath('./Modules/'))

import DevNux, RW, URL

# Configurações
path_store = 'store/'

# Carrega os modulos utilizados
DevNux 	= DevNux()
RW 		= RW(path_store)
URL		= URL()


while True:

	DevNux.clear()
	print('##############  M E N U ###############')
	print('1) Encurtar URL')
	print('2) Ver Tabela Hash')
	print('3) Salvar Tabela Hash')
	print('4) Carregar Arquivo')
	print('5) Buscar por Hash')
	print('6) Base64')
	print('0) Sair')

	acao = input();

	# Adicionar uma URL
	if(acao == '1'):
		DevNux.clear();
		print('Informe a URL')
		link = input();

		URL.encurtar(link)

	# Exibir tabela Hash
	if(acao == '2'):
		DevNux.clear();
		print(URL.tabela_hash)
		DevNux.sleep()

	# Salvar em arquivo
	if(acao == '3'):
		DevNux.clear();
		print('Informe o nome do arquivo')
		nome_arquivo = input();

		if(RW.save(URL.tabela_hash, nome_arquivo) == False):
			print('Ops, não consegui salvar, algo de errado não deu certo.')
			DevNux.sleep();

	# Carregar arquivo por nome
	if(acao == '4'):
		DevNux.clear();
		print('Informe o nome do arquivo')
		nome_arquivo = input();
		
		if(RW.read(nome_arquivo)):
			URL.tabela_hash = RW.read(nome_arquivo)
		else:
			print('Ops, parece que o arquivo não existe.')
			DevNux.sleep();

	# Buscar por Hash
	if(acao == '5'):
		DevNux.clear();
		print('Informe o hash')
		indice = input();

		print(URL.buscar(indice))
		DevNux.sleep()

	# BASE 64
	if(acao == '6'):

		while True:

			DevNux.clear()
			print('##############  B A S E    64 ###############')
			print('1) Converter Índice')
			print('2) Converter Valor')
			print('0) Sair')

			acao_base64 = input();

			# Base64 toBase
			if(acao_base64 == '1'):
				DevNux.clear();
				print('Informe o indice')
				indice = int(input());
				print(URL.toBase(indice))
				DevNux.sleep()
			
			# Base64 to10
			if(acao_base64 == '2'):
				DevNux.clear();
				print('Informe o valor')
				valor = input();
				print(URL.to10(valor))
				DevNux.sleep()

			# Se for Sair
			if(acao_base64 == '0'):
				print('CYA.. :*')
				break

	# Se for Sair
	if(acao == '0'):
		print('CYA.. :*')
		break