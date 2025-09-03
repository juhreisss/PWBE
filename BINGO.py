import random
import pyttsx3
from pyfiglet import figlet_format
import msvcrt
import time

class Bingo:
    def __init__(self):
    
        self.todas = []
        self.criar_todas_combinacoes()

    def criar_todas_combinacoes(self):
        for numero in range(1, 16):
            self.todas.append(f"B{numero}")
        for numero in range(16, 31):
            self.todas.append(f"I{numero}")
        for numero in range(31, 46):
            self.todas.append(f"N{numero}")
        for numero in range(46, 61):
            self.todas.append(f"G{numero}")
        for numero in range(61, 76):
            self.todas.append(f"O{numero}")


    def sorteio(self):
        if not self.todas:
            return "Todos os números já foram sorteados!"
        escolha = random.choice(self.todas)
        self.todas.remove(escolha)
        return escolha

    def jogar(self):
        print(figlet_format("BINGO", font="standard"))
        while True:
            if not self.todas:
                print("Fim do jogo!!! Todos os numeros foram sorteados.")
                break

            print("Sorteando em 3")
            time.sleep(1)
            print("Sorteando em 2")
            time.sleep(1)
            print("Sorteando em 1")
            time.sleep(1)

            sorteio = self.sorteio()
            self.falar(sorteio)
            print(sorteio)

    
            msvcrt.getch()
            time.sleep(1)


    def falar(self, texto):
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()


bingo = Bingo()
bingo.jogar()
