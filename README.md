# **csv-generator**
Um script em python para gerar arquivos csv a partir de txt em que os registros estejam em uma coluna.
Foi criado com a intenção de facilitar a obtenção dos dados em tabelas cuja cópia para analisar com o Pandas/Python era trabalhosa.

### **Exemplo**
Entrada:
filename = file.txt
```
id
produto
preco
1
grampeador
16.00
2
caneta
5.00
```
Saída = file.csv
```
id,produto,preco
1,grampeador,16.00
2,caneta,5.00
```
