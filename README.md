# Encurtador de String - Encurtador de URL
Exercício feito em Aula - Python - IMED - RS


# Desafio (Hashs) #
Crie um sistema que transforme URLs grandes como "https://imed.edu.br/Ensino/ciencia-da-computacao/graduacao/sobre-a-profissao/" em uma URL curta.

Exemplo: imed.to/g8

Usando a função hash BASE62:
base62('g8') => 1000

BASE62 - Informações importantes:

	  a-z (minúsculas): 26 caracteres no total
	  A-Z (maiúsculas): 26 caracteres no total
	  0-9 (números)   : 10 caracteres
	  --
	  Total de 62 combinações (base 62) – ver arquivo: base62.py

A ideia é ter uma estrutura com:

   1) Um dicionário onde sua chave será um valor obtido a partir do auto-incremento e apontará para uma tupla com a URL encurtada e a original.
    
        a. Exemplo: Chave 1000 =>  ("g8", "<a target="_blak" href="https://imed.edu.br/Ensino/ciencia-da-computacao/graduacao/sobre-a-profissao/">https://imed.edu.br/Ensino/ciencia-da-computacao/graduacao/sobre-a-profissao/</a>")

** Auto-incremento: A implementação deverá ter um contador que irá iniciar no valor 1000 **

    • Criar um menu e incluir operações para:
        ◦ Converter URL para URL curta, armazenando sequencialmente as urls em um dicionário
        ◦ Testar a conversão de um inteiro para string codificada, usando método do módulo base62 disponibilizado
        ◦ Testar a conversão de uma string codificada para inteiro, usando método do módulo base62 disponibilizado
        ◦ Mostrar a tabela hash (dicionário)
        ◦ Salvar as tabelas hash em arquivo
        ◦ Carregar arquivo com tabelas

Para salvar e carregar as tabelas use a biblioteca PICKLE do python.
	<a target="_blak" href="https://www.vivaolinux.com.br/dica/Python-3.0-Gravando-dicionarios-em-arquivos/">https://www.vivaolinux.com.br/dica/Python-3.0-Gravando-dicionarios-em-arquivos/</a>


<br />

<hr />

## Pastas / Arquivos ##

<ul>
  <li>
    <p>Modules</p>
    <ul>
      <li>DevNux.py</li>
      <li>RW.py</li>
      <li>URL.py</li>
    </ul>
  </li>
  <li>
    <p>store</p>
  </li>
  <li>main.py</li>
</ul>
<br />
<hr />
<br />



## Como faz? ##
na raíz do projeto, abra o terminal
```shell
  python3 main.py
```
