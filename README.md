# **csv-generator**

Script em Python para gerar um arquivo .CSV a partir de um arquivo TXT.
O TXT deve ter o número de colunas nos dois últimos de seu nome, como uma forma de metadados.

**Exemplo**: arquivo_05.txt -> este arquivo terá 05 colunas.
        
O arquivo deve também ter os valores todos em uma linha apenas.
        
Ex:
Entrada: filename = arquivo_02.txt
```
fruta
preco
maça
1.5
pera
1.8
```

Saida: filename = arquivo_02.csv
```
fruta,preco
maça,1.5
pera,1.8
```