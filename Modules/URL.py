#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

from math import floor

sys.path.append(os.path.abspath('./Modules/'))

# Classe responsável por encurtar URL
class URL:

	def __init__(self):

		self.tabela_hash 	= {}
		self.contador		= 1000

	def buscar(self, indice):

		for i in self.tabela_hash:

			if(self.tabela_hash[i][0] == indice):
				return self.tabela_hash[i][1]

		return 'Ops, parece que esse índice não existe bro.'

	def encurtar(self, url_original = ''):

		if url_original == '':
			return 'Irmão, url inválida.'

		url_encurtada = self.toBase(self.contador)

		# Coloca a URL na tabela Hash
		self.tabela_hash[self.contador] = (url_encurtada, url_original)

		# Incrementa o contador
		self.contador += 1

		return 'Foi gerado uma nova URL, ', url_encurtada


	# BASE64
	def toBase(self, num = '', b = 62):
		if b <= 0 or b > 62:
			return 0
		base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		r = num % b
		res = base[r];
		q = floor(num / b)
		
		while q:
			r = q % b
			q = floor(q / b)
			res = base[int(r)] + res
		return res

	def to10(self, num, b = 62):
		base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		limit = len(num)
		res = 0;
		for i in range(limit):
			res = b * res + base.find(num[i])
		return res


sys.modules[__name__] = URL