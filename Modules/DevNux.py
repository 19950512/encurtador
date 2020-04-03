#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

class DevNux:

	def __init__(self):
		pass

	# Limpa o terminal
	def clear(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	# Mensagem para visualziar dados
	def sleep(self, msg = 'Pressione uma tecla para sair'):
		return input(msg)

sys.modules[__name__] = DevNux