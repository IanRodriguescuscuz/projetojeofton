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
        |                                        |
        |                                        |
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
goblim = {
    "nome":"goblim traiçoeiro",
    "dano": 20,
    "vida": 50,
    "exp":20,
}

contador_de_eventos = 0

def ganhar_xp(npc):
    print("/n /n A Batalha foi árdua, mas a experança de achar uma saída segue crescente. /n /n")
    print(f"\nVocê derrotou {npc['nome']} e ganhou {npc['exp']} de experiência!")

    aventureiro["exp"] += npc["exp"]

    while aventureiro["exp"] >= aventureiro["expmaximo"]:
        aventureiro["exp"] -= aventureiro["expmaximo"]  
        aventureiro["dano"] += 5
        aventureiro["vida"] += 20
        aventureiro["vidamaxima"] += 20
        aventureiro["expmaximo"] += 50 
        aventureiro["mana"] += 10
        aventureiro["manamaxima"] += 10
        print(" Você subiu de nível! +5 de dano, +20 de vida máxima e 10 de mana máxima!")

    print(f"XP atual: {aventureiro['exp']} / {aventureiro['expmaximo']}")

def verificar_morte():
    if aventureiro["vida"] <= 0:
        print("\n Você morreu. Sua jornada termina aqui. ")
        exit()

def batalha(npc):
    print("\nA batalha começou!")

    def exura():
        if aventureiro["mana"] >= 10:
            aventureiro["vida"] += 40
            aventureiro["mana"] -= 10
            print("Você se cura em +40 de vida!")
        else:
            print("Você não tem mana suficiente!")

    def atacar():
        npc["vida"] -= aventureiro["dano"]
        print(f"Você ataca e causa {aventureiro['dano']} no {npc['nome']}!")
        aventureiro["vida"] -= npc["dano"]
        print(f"O {npc['nome']} revida e causa {npc['dano']}!")

    ações_na_batalha = {
        "exura": exura,
        "atacar": atacar,
    }

    while aventureiro["vida"] > 0 and npc["vida"] > 0:
        ação = input("\nO que você vai fazer? > ").strip().lower()
        if ação in ações_na_batalha:
            ações_na_batalha[ação]()
        else:
            print("Você não consegue fazer isso!")


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
        if efeitodocogumelo >= 3:
            print("Você come o cogumelo... e é muito saboroso 🍄✨")
            aventureiro["vida"] += 20
            aventureiro["mana"] += 20
            print("Você recuperou 20 de vida e mana!")
        elif efeitodocogumelo <= 2:
            print("Que cogumelho horrivel! Você não deveria comer tudo que encontra no chão!, Você perde 20 pontos de vida")
            aventureiro["vida"] -= 20
            verificar_morte()
    else:
        print("Você ignora o cogumelo. Melhor prevenir do que remediar... ")
 
def evento_2():
    global contador_de_eventos
    contador_de_eventos += 1
    print("Um morcego gigante te ataca!")

def evento_3():
    global contador_de_eventos
    contador_de_eventos += 1
    print("Você escorrega em uma pedra e perde 1 de vida!")

def evento_4():
    global contador_de_eventos
    contador_de_eventos += 1
    print("Você encontra uma tocha acesa no chão.")

def evento_5():
    global contador_de_eventos
    contador_de_eventos += 1
    print("Uma armadilha dispara flechas!")

def evento_6():
    global contador_de_eventos 
    contador_de_eventos += 1
    print("Você encontra um aliado ferido pedindo ajuda.")

def evento_7():
    global contador_de_eventos 
    contador_de_eventos += 1
    print("Um eco estranho preenche a caverna.")

def evento_8():
    global contador_de_eventos 
    contador_de_eventos += 1
    print("Você descobre um caminho secreto.")

def evento_9():
    global contador_de_eventos 
    contador_de_eventos += 1
    print("Você encontra uma poção de cura.")

def evento_10():
    global contador_de_eventos 
    contador_de_eventos += 1
    print("Voce percorre por um caminho estreito, longo e apertado. . .")
    decisao = input("\n\nVocê chega em área aberta, com um poço de água à sua esquerda, você está cansado. . . você imediatamente sente sede. . .,\n\n\ndeseja beber da água? > ").strip().lower()
    beber_agua(decisao)
    return decisao in ["sim", "s", "comer", "vamo", "vamos", "claro", "bora","yes"]

def beber_agua(decisao):
    if decisao in ["sim", "s", "comer","beber", "vamo", "vamos", "claro", "bora", "yes"]:
        print("""
              \n\n\nVocê começa a sentir um mal-estar, você cambalea e começa a perder o equilíbrio, voce procura um local de apoio, porém acaba caindo e perdendo a consciência. . .\n\n\nAo acordar, você nota que suas mãos estão amarradas, ao olhar a o redor, uma figura pequena, feia e nojenta com uma faca em sua cintura te encara de olhos abertos e salivando pela boca. . .\n\n\n
            
              """)
        goblin()
    else:
        print("tchau")
        evento_na_caverna()


def goblin():
    tentativas = 0
    print("Suas mãos estão amarradas. O goblin caminha em sua direção, afiando sua faca...")

    while True:
        if aventureiro["vida"] <= 0:
            print(" Você sucumbiu aos ferimentos enquanto tentava escapar...")
            exit()

        opcao = input("\nO que você vai fazer? [desamarrar / esperar] > ").strip().lower()

        if opcao == "desamarrar":
            tentativas += 1
            chance = randint(0, 6)
            if chance >= 3:
                print("\n Você consegue se soltar! O goblin percebe e investe contra você com a faca em sua direção")
                batalha(goblim)
                verificar_morte()
                ganhar_xp(goblim)
                break
            else:
                dano = 10 + tentativas * 5
                aventureiro["vida"] -= dano
                print(f" Você tenta se soltar, mas falha. O goblin te golpeia! Você perde {dano} de vida. Vida atual: {aventureiro['vida']}")
        elif opcao == "esperar":
            dano = randint(10, 25)
            aventureiro["vida"] -= dano
            print(f" Você espera... mas o goblin não! Ele avança e te corta. Você perde {dano} de vida. Vida atual: {aventureiro['vida']}")
        else:
            print(" Opção inválida. Tente novamente.")

           


def evento_11():
    global contador_de_eventos 
    contador_de_eventos += 1
    print("Você acha um artefato antigo e poderoso!")



eventos = [evento_1, evento_2, evento_3, evento_4, evento_5, evento_6, evento_7, evento_8, evento_9, evento_10, evento_11]
def evento_na_caverna():
    evento_escolhido = randint(0,10)
    eventos[evento_escolhido]()

evento_1()
evento_10()

#print({aventureiro["dano"],aventureiro["vida"]})
print(f"Você já percorreu {contador_de_eventos} câmara(s)")
