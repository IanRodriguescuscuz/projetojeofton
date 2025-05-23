from random import randint

def tela_inicial():
    print(r"""           _  _             _  _
  .       /\\/%\       .   /%\/%\     .
      __.<\\%#//\\,_       <%%#/%%\\,__  .
.    <%#/|\\%%%#///\\    /^%#%%\\///%#\\\\
      ""/%/""\\ \""//|   |/""'/ /\\//"//'
 .     L/'`   \\ \\  `    "   / /  ```
        `      \\ \\     .   / /       .
 .       .      \\ \\       / /  .
        .        \\ \\     / /          .
   .      .    ..:\\ \\:::/ /:.     .     .
______________/ \\__;\\___/\\;_/\\________________________________
YwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYw
                  ---------------------------------------
                |     escreva "aventura" para começar      |
                  ---------------------------------------

                     hero's insistence
                          ~ O Rpg """)


def perguntar_se_quer_jogar():
    resposta = input("\n\n                Vamos entrar nesta caverna? > ").strip().lower()
    return resposta in ["sim", "s", "aventura", "vamo", "vamos", "claro", "bora"]


def perguntar_nome():
    print("\n" * 5)
    print("""         ---------------------------------------
        |     Qual o seu nome, aventureiro?      |
        |                                         |
        |                                         |
         ---------------------------------------""")
    nome = input("                    > ").strip().title()
    return nome

tela_inicial()

if perguntar_se_quer_jogar():
    nome = perguntar_nome()
    aventureiro = {"nome": nome}
    print(f"\nBem-vindo, {aventureiro['nome']}! Sua aventura começa agora...\n")
else:
    print("\nTudo bem, quem sabe em outra hora. A caverna espera...\n")

aventureiro = {"nome": nome,
               "dano": 10,
               "vida": 100,
               "vidamaxima":100,
               "exp":0,
               "expmaximo":100,
               "mana":50,
               "manamaxima":50}

contador_de_eventos = 0

def evento_1():
    global contador_de_eventos
    print("Você adentra na caverna e encontra um cogumelo estranho, mas bem apetitoso")
    decisão = input("\n\n                comer? > ").strip().lower()
    contador_de_eventos += 1
    cogumelo_efeito(decisão)
    return decisão in ["sim", "s", "comer", "vamo", "vamos", "claro", "bora","yes"]

def cogumelo_efeito(decisão):
    if decisão in ["sim", "s", "comer", "vamo", "vamos", "claro", "bora", "yes"]:
        efeitodocogumelo = randint(1,5)
        if efeitodocogumelo >= 2:
            print("Você come o cogumelo... e é muito saboroso 🍄✨")
            aventureiro["vida"] += 20
            aventureiro["mana"] += 20
            print("Você recuperou 20 de vida e mana!")
        elif efeitodocogumelo <= 1:
            print("Que cogumelho horrivel! Você não deveria comer tudo que encontra no chão!, Você perde 20 pontos de vida")
            aventureiro["vida"] -= 20
    else:
        print("Você ignora o cogumelo. Melhor prevenir do que remediar... ")
 
def evento_2():
    print("Um morcego gigante te ataca!")

def evento_3():
    print("Você escorrega em uma pedra e perde 1 de vida!")

def evento_4():
    print("Você encontra uma tocha acesa no chão.")

def evento_5():
    print("Uma armadilha dispara flechas!")

def evento_6():
    print("Você encontra um aliado ferido pedindo ajuda.")

def evento_7():
    print("Um eco estranho preenche a caverna.")

def evento_8():
    print("Você descobre um caminho secreto.")

def evento_9():
    print("Você encontra uma poção de cura.")

def evento_10():
    print("Um goblin surge das sombras!")

def evento_11():
    print("Você acha um artefato antigo e poderoso!")

evento_1()

eventos = [evento_1, evento_2, evento_3, evento_4, evento_5, evento_6, evento_7, evento_8, evento_9, evento_10, evento_11]
def evento_na_caverna():
    evento_escolhido = randint(1,10)
    eventos[evento_escolhido]()



print({aventureiro["dano"],aventureiro["vida"]})
print(contador_de_eventos)
