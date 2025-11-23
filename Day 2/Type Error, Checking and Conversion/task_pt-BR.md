### TypeError
Esses erros ocorrem quando você está usando o tipo de dado errado.
ex. `len(12345)`

Porque você pode apenas dar à função `len()` Strings, ela se recusará a funcionar e lhe dará um TypeError se você der um número (Integer).

#### PAUSA 1. Corrija a função `len()` para que não haja mais avisos ou erros.

### Verificação de Tipo
Você pode verificar o tipo de dado de qualquer valor ou variável em python usando a função `type()`.

`print(type("abc")) #dará a você <class 'str'>`

#### PAUSA 2. Escreva 4 verificações de tipo para imprimir todos os 4 tipos de dados
Usando as funções `type()` e `print()` para imprimir 4 linhas na área de saída para obtermos a coleção completa de tipos de dados que aprendemos. `<class 'str'> <class 'int'> <class 'float'> e <class 'bool'>`

### Conversão de Tipo
Você pode converter dados em diferentes tipos de dados usando funções especiais.
ex.

`float()` 

`int()`

`str()`

#### PAUSA 3. Faça esta linha de código correr sem erros
`print("Número de letras no seu nome: " + len(input("Insira seu nome")))`