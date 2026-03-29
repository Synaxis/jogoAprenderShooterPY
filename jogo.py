import tkinter as tk
import random

# Tamanho da janela
LARG = 500
ALT = 350

# Configurações do jogo
PASSO_JOGADOR = 15
VELOC_BALA = 12
RAIO_INIMIGO = 15
VIDAS_INICIAIS = 3


def colidiu(x1, y1, l1, a1, x2, y2, l2, a2):
    """Verifica colisão simples entre 2 retângulos."""
    return (
        abs(x1 - x2) < (l1 + l2) / 2
        and abs(y1 - y2) < (a1 + a2) / 2
    )


class Jogo:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Shooter")

        self.canvas = tk.Canvas(root, width=LARG, height=ALT, bg="white")
        self.canvas.pack()

        # Teclas do jogo
        root.bind("<Left>", lambda e: self.mover(-PASSO_JOGADOR))
        root.bind("<Right>", lambda e: self.mover(PASSO_JOGADOR))
        root.bind("<space>", lambda e: self.atirar())
        root.bind("<r>", lambda e: self.reiniciar())
        root.bind("<R>", lambda e: self.reiniciar())

        self.reiniciar()
        self.loop()

    def reiniciar(self):
        """Reinicia o jogo inteiro."""
        self.jogo_ativo = True
        self.pontos = 0
        self.vidas = VIDAS_INICIAIS
        self.nivel = 1

        self.jogador_x = LARG // 2
        self.jogador_y = ALT - 20

        self.bala = None
        self.novo_inimigo()

    def novo_inimigo(self):
        """Cria ou reposiciona o inimigo no topo."""
        self.inimigo_x = random.randint(20, LARG - 20)
        self.inimigo_y = 40
        self.inimigo_vx = random.choice([-1, 1]) * (3 + self.nivel)

    def mover(self, dx):
        """Move o jogador sem deixar sair da tela."""
        if not self.jogo_ativo:
            return

        self.jogador_x += dx
        self.jogador_x = max(15, min(LARG - 15, self.jogador_x))

    def atirar(self):
        """Cria uma bala se ainda não existir uma na tela."""
        if not self.jogo_ativo:
            return

        if self.bala is None:
            self.bala = [self.jogador_x, self.jogador_y - 15]

    def atualizar_bala(self):
        """Move a bala para cima."""
        if self.bala is None:
            return

        self.bala[1] -= VELOC_BALA

        if self.bala[1] < 0:
            self.bala = None

    def atualizar_inimigo(self):
        """Move o inimigo de um lado para o outro e faz descer."""
        self.inimigo_x += self.inimigo_vx

        if self.inimigo_x <= RAIO_INIMIGO or self.inimigo_x >= LARG - RAIO_INIMIGO:
            self.inimigo_vx *= -1
            self.inimigo_y += 20

        # Se o inimigo chegar muito perto da parte de baixo, perde vida
        if self.inimigo_y >= ALT - 50:
            self.perder_vida()

    def verificar_colisoes(self):
        """Verifica colisão da bala com inimigo e do inimigo com jogador."""
        # Bala acertou o inimigo
        if self.bala and colidiu(
            self.bala[0], self.bala[1], 4, 12,
            self.inimigo_x, self.inimigo_y, RAIO_INIMIGO * 2, RAIO_INIMIGO * 2
        ):
            self.bala = None
            self.pontos += 10
            self.nivel = 1 + self.pontos // 50
            self.novo_inimigo()

        # Inimigo encostou no jogador
        if colidiu(
            self.jogador_x, self.jogador_y, 30, 20,
            self.inimigo_x, self.inimigo_y, RAIO_INIMIGO * 2, RAIO_INIMIGO * 2
        ):
            self.perder_vida()

    def perder_vida(self):
        """Remove uma vida e termina o jogo se acabar."""
        self.vidas -= 1
        self.bala = None

        if self.vidas <= 0:
            self.jogo_ativo = False
        else:
            self.jogador_x = LARG // 2
            self.novo_inimigo()

    def desenhar_jogador(self):
        """Desenha o jogador."""
        x = self.jogador_x
        y = self.jogador_y

        self.canvas.create_rectangle(x - 15, y - 10, x + 15, y + 10, fill="blue")
        self.canvas.create_rectangle(x - 4, y - 18, x + 4, y, fill="lightblue")

    def desenhar_inimigo(self):
        """Desenha o inimigo."""
        x = self.inimigo_x
        y = self.inimigo_y

        self.canvas.create_oval(
            x - RAIO_INIMIGO, y - RAIO_INIMIGO,
            x + RAIO_INIMIGO, y + RAIO_INIMIGO,
            fill="red"
        )

    def desenhar_bala(self):
        """Desenha a bala, se existir."""
        if self.bala:
            x, y = self.bala
            self.canvas.create_rectangle(x - 2, y - 10, x + 2, y + 2, fill="black")

    def desenhar_painel(self):
        """Mostra pontos, vidas e nível."""
        texto = f"Pontos: {self.pontos}   Vidas: {self.vidas}   Nível: {self.nivel}"
        self.canvas.create_text(10, 15, text=texto, anchor="w", font=("Arial", 12, "bold"))
        self.canvas.create_text(
            LARG // 2, ALT - 10,
            text="← → mover | espaço atira | R reinicia",
            font=("Arial", 10)
        )

    def desenhar_game_over(self):
        """Mostra mensagem de fim de jogo."""
        self.canvas.create_text(
            LARG // 2, ALT // 2 - 20,
            text="GAME OVER",
            font=("Arial", 24, "bold"),
            fill="red"
        )
        self.canvas.create_text(
            LARG // 2, ALT // 2 + 10,
            text=f"Pontuação final: {self.pontos}",
            font=("Arial", 14)
        )
        self.canvas.create_text(
            LARG // 2, ALT // 2 + 35,
            text="Pressione R para reiniciar",
            font=("Arial", 12)
        )

    def desenhar(self):
        """Limpa a tela e redesenha tudo."""
        self.canvas.delete("all")
        self.desenhar_jogador()
        self.desenhar_inimigo()
        self.desenhar_bala()
        self.desenhar_painel()

        if not self.jogo_ativo:
            self.desenhar_game_over()

    def atualizar(self):
        """Atualiza a lógica do jogo."""
        if not self.jogo_ativo:
            return

        self.atualizar_bala()
        self.atualizar_inimigo()
        self.verificar_colisoes()

    def loop(self):
        """Loop principal do jogo."""
        self.atualizar()
        self.desenhar()
        self.root.after(30, self.loop)


if __name__ == "__main__":
    root = tk.Tk()
    Jogo(root)
    root.mainloop()
