Você pode escrever quantos comandos if precisar para verificar diferentes condições que não têm relação entre si.
Compare os blocos de código abaixo:
```
# If/elif/else
if <condição 1 é verdadeira>
    <faça A>
elif <condição 2 é verdadeira>
    <faça B>
else
    <faça C>
```
```
# Comandos if aninhados
if <condição 1 é verdadeira>
    <faça A>
    if <condição 2 é verdadeira>
        <faça B>
        if <condição 3 é verdadeira>
            <faça C>
```

```
# Múltiplos comandos if
if <condição 1 é verdadeira>
    <faça A>
if <condição 2 é verdadeira>
    <faça B>
if <condição 3 é verdadeira>
    <faça C>
```

No bloco if/elif/else, apenas uma das opções A, B ou C pode ocorrer, porque if/elif/else são mutuamente exclusivos. A primeira condição precisa falhar para entrar no elif e o elif (ou múltiplos elif) precisa falhar para entrar no else. Condição 2 é verificada apenas se a condição 1 for falsa.

Nos comandos if aninhados, A, B e C podem todos ocorrer, mas as condições 1, 2 e 3 devem todas ser verdadeiras. O computador verificará a condição 2 apenas se a condição 1 for verdadeira.

Nos múltiplos comandos if, A, B e C podem todos ocorrer. Mas são completamente independentes um do outro. C pode ocorrer mesmo que A e B não ocorram. Todas as condições são verificadas, independente do resultado das outras.