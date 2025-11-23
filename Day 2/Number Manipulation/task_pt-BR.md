### Arredondando para baixo um Número
Você pode arredondar para baixo um número ou remover todos os lugares decimais usando a função `int()` que converte um número flutuante (com casas decimais) em um inteiro (número integral).

`int(3.738492) # Se torna 3` 

### Arredondando um Número
No entanto, se você deseja arredondar um número decimal para o número integral mais próximo usando o método matemático tradicional, onde qualquer coisa acima de .5 vai para cima e qualquer coisa abaixo vai para baixo. Então você pode usar a função `round()` do python.

`round(3.738492) # Se torna 4`

`round(3.14159) # Se torna 3`

`round(3.14159, 2) # Se torna 3.14`

### Operadores de Atribuição
Operadores de atribuição como o operador de atribuição de adição `+=` vão adicionar o número à direita ao valor original da variável à esquerda e atribuir o novo valor à variável.

`+=`

`-=`

`*=`

`/=`


### f-Strings
Em Python, podemos usar f-strings para inserir uma variável ou uma expressão em uma string.

`idade = 12`

`print(f"Eu tenho {idade} anos de idade")`

`# Vai imprimir Eu tenho 12 anos de idade.`