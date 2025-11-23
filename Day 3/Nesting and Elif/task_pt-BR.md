### Condicionais aninhados
Você pode colocar instruções if/else dentro de outras instruções if/else. Isso é conhecido como aninhamento.
por exemplo.

```
if nota_matematica >= 90:
    if nota_ingles >= 90:
        print("Você é bom em tudo")
    else:
        print("Você é bom em matemática")
if nota_ingles >= 90:
    print("Você é bom em inglês)
```

Neste caso, somente quando um aluno tem mais de 90 em matemática e inglês, eles recebem "Você é bom em tudo".

Nota: Você também pode ter instruções if que não têm uma declaração else emparelhada.