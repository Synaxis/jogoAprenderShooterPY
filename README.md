# jogoAprenderShooterPY
um mini game em python que fiz para aprender

um mini jogo de tiro 2D que eu fiz em Python usando Tkinter, mais para treinar lógica de programação e brincar um pouco com interface gráfica.

A ideia foi fazer algo bem pequeno (menos de 50 linhas), mas que tivesse algumas coisas legais como movimentação do jogador, tiro, inimigo na tela e detecção de colisão.

você controla 1 nave azul na parte de baixo da tela. Um inimigo vermelho aparece na parte de cima e o objetivo é acertar ele com os tiros. Quando o tiro acerta, o inimigo reaparece em outra posição aleatória.

aproveitei para separar a lógica da colisão em uma função específica. Assim fica mais fácil de testar e manter o código organizado. Por isso o projeto também tem alguns testes unitários usando o módulo unittest do Python.

Controles

← mover para esquerda  
→ mover para direita  
Espaço para atirar

## Como rodar

python jogo.py

Rodar os testes:

python -m unittest test_jogo.py

## Objetivo do projeto

Esse projeto foi feito mais como exercício para praticar:

- Python3
- lógica básica de jogos
- desenho 2D com Tkinter
- organização simples de código
- testes unitários

É um projeto pequeno, mas já mostra algumas boas práticas básicas de desenvolvimento.
