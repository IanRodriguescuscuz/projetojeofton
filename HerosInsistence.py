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

def quer_dizer_sim(resposta):
    resposta = resposta.strip().lower()
    return resposta in [
        "sim", "s", "aventura", "vamo", "vamos", "claro", "bora", "beber", "comer", "dale", "daledele", "daledeledeledoly", "continuar", "pegar", "ir", "entrar", "cogumelo", "sm", "simm","go","sin",
    ]
    
def perguntar_se_quer_jogar():
    resposta = input("\n\n                Vamos entrar nesta caverna? > ").strip().lower()
    return quer_dizer_sim(resposta)


def perguntar_nome():
    print("\n" * 5)
    print("""         ---------------------------------------
        |     Qual o seu nome, aventureiro?      |
        |                                        |
        |                                        |
         ---------------------------------------""")
    nomedoaventureiro = input("                    > ").strip().title()
    return nomedoaventureiro

tela_inicial()

def status():
    print(f"""
    ---- Status ----
    Nome: {aventureiro['nome']}
    Vida: {aventureiro['vida']}/{aventureiro['vidamaxima']}
    Mana: {aventureiro['mana']}/{aventureiro['manamaxima']}
    Dano: {aventureiro['dano']}
    XP: {aventureiro['exp']} / {aventureiro['expmaximo']}
    ----------------
    """)

if perguntar_se_quer_jogar():
    nomedoaventureiro = perguntar_nome()
    aventureiro = {"nome": nomedoaventureiro,
               "dano": 10,
               "vida": 100,
               "vidamaxima":100,
               "exp":0,
               "expmaximo":100,
               "mana":50,
               "manamaxima":50,
               "manaregen": 5}
    print(f"\nBem-vindo, {aventureiro['nome']}! Sua aventura começa agora...\n")
else:
    print("\nTudo bem, quem sabe em outra hora. A caverna espera...\n")
    exit()

goblim = {
    "nome":"goblim traiçoeiro",
    "dano": 20,
    "vida": 50,
    "exp":30,
}

morcego_gigante = {

    "nome":"morcego gigante",
    "dano": 10,
    "vida": 40,
    "exp":20,

}

Pedra_perigosamente_escorregadia = {

    "nome":"Pedra perigosamente escorregadia",
    "dano": 15,
    "vida": 1,
    "exp":20,

}

lagarto_das_cavernas = {
    "nome":"lagarto-das-cavernas",
    "dano": 25,
    "vida": 60,
    "exp":50,

}

coelho_agressivo = {
    "nome":"coelho agressivo",
    "dano": 0,
    "vida": 10,
    "exp":5,

}

lobo_faminto = {
    "nome":"Lobo faminto",
    "dano": 10,
    "vida": 25,
    "exp":15,
}

lobo_alfa = {
    "nome":"Lobo ALFA",
    "dano": 15,
    "vida": 40,
    "exp":30,
}

contador_de_eventos = 0

def recuperar_mana():
    if aventureiro["mana"] < aventureiro["manamaxima"]:
        aventureiro["mana"] += aventureiro["manaregen"]
        print(f"Você naturalmente recupera {aventureiro ['manaregen']} pontos de mana")

def ganhar_xp(npc):
    print(" -------------------------------------------------------------------------")
    print("A Batalha foi árdua, mas a esperança de achar uma saída segue crescente.")
    print(f"Você derrotou {npc['nome']} e ganhou {npc['exp']} de experiência!")
    print("-------------------------------------------------------------------------")

    aventureiro["exp"] += npc["exp"]

    while aventureiro["exp"] >= aventureiro["expmaximo"]:
        aventureiro["exp"] -= aventureiro["expmaximo"]  
        aventureiro["dano"] += 5
        aventureiro["vida"] += 20
        aventureiro["vidamaxima"] += 20
        aventureiro["expmaximo"] += 30 
        aventureiro["mana"] += 10
        aventureiro["manamaxima"] += 10
        print(" Você subiu de nível! +5 de dano, +20 de vida máxima e 10 de mana máxima!")
        print("\n\n -********--------************------***********------\n\n")
    print(f"XP atual: {aventureiro['exp']} / {aventureiro['expmaximo']}")

def verificar_morte():
    if aventureiro["vida"] <= 0:
        print("\n Você morreu. Sua jornada termina aqui. ")
        exit()

def perguntar_continuar_aventura():
    resposta = input("\nVocê deseja continuar explorando a caverna? > ").strip().lower()
    if quer_dizer_sim(resposta):
        print("\nVocê respira fundo e segue adiante na escuridão...\n")
    else:
        print("\nVocê encara a escuridão e ela te encara de volta. Isso não foi uma boa ideia.\n")
        print("fim.")
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
    
    def exori():
        if aventureiro["mana"] >= 15:
            aventureiro["mana"] -= 15
            npc["vida"] -= aventureiro["dano"]*2+5
            print("você conjura um ataque devastador e brutal.")
            if npc["vida"] > 0:
                aventureiro["vida"] -= npc["dano"]
                print(f"O {npc['nome']} está gravimente ferido, mas revida e causa {npc['dano']} de dano!")
            else:
                print(f"O {npc['nome']} foi DEVASTADO!")
        else:
            print("Você não tem mana suficiente!")


    def exori_kor():
        if aventureiro["mana"] >= 10:
            aventureiro["mana"] -= 10
            npc["vida"] -= aventureiro["dano"]
            aventureiro["vida"] += aventureiro["dano"]
            print(f"A sua lâmina conjura um ataque vampírico que te cura em {aventureiro['dano']} ")
            if npc["vida"] > 0:
                aventureiro["vida"] -= npc["dano"]
                print(f"O {npc['nome']} está assutado, mas revida e causa {npc['dano']} de dano!")
            else:
                print(f"O {npc['nome']} foi derrotado")
        else:
            print("Você não tem mana suficiente!")

    def exori_con():
        if aventureiro["mana"] >= 10:
            aventureiro["mana"] -= 10
            npc["vida"] -= aventureiro["dano"]
            print(f"Você lança uma flecha mágica que causa {aventureiro['dano']} de dano no {npc['nome']}!")
            print("Você ataca de longe e está seguro")
            if npc["vida"] <= 0:
                print(f"O {npc['nome']} foi derrotado!")
        else:
            print("Você não tem mana suficiente!")

    def utito_san():
        if aventureiro["mana"] >= 10:
            aventureiro["mana"] -= 10
            while npc["vida"] >= 0:
                aventureiro["dano"] += 5
        else:
            print("Você não tem mana suficiente!")

    def exori_utamo():
        if aventureiro["mana"] >= 20:
            aventureiro["mana"] -= 20
            npc["vida"] -= aventureiro["mana"]*2
            print(f"Você lança uma esfera mágica feita de pura mana que causa {aventureiro['mana']*2} de dano no {npc['nome']}!")
            print("Você sente que o próximo exori utamo vai ser menos eficaz")
            if npc["vida"] <= 0:
                print(f"O {npc['nome']} foi evaporado!")
        else:
            print("Você não tem mana suficiente!")

    def exori_vis():
        if aventureiro["mana"] >= 15:
            aventureiro["mana"] -= 15
            npc["vida"] -= 25
            print(f"Você lança uma esfera elétrica que causa {aventureiro['mana']} de dano no {npc['nome']}!")
            if npc["vida"] <= 0:
                print(f"O {npc['nome']} virou churrasco!")
        else:
            print("Você não tem mana suficiente!")

    def magia():
        print(""">>> Magias possuem palavras mágicas.
                     as diga e elas aconteceram!  <<<""")

        
            
    def atacar():
        npc["vida"] -= aventureiro["dano"]
        print(f"Você ataca e causa {aventureiro['dano']} de dano no {npc['nome']}!")
        if npc["vida"] > 0:
            aventureiro["vida"] -= npc["dano"]
            print(f"O {npc['nome']} revida e causa {npc['dano']} de dano!")
        else:
            print(f"O {npc['nome']} foi derrotado!")

    ações_na_batalha = {
        "exura": exura,
        "atacar": atacar,
        "status": status,
        "exori": exori,
        "exori kor": exori_kor,
        "exori con": exori_con,
        "exori utamo": exori_utamo,
        "utito san": utito_san,
        "exori vis": exori_vis,
        "magia":magia,
    }

    while aventureiro["vida"] > 0 and npc["vida"] > 0:
        ação = input("\nO que você vai fazer? > [Magia / Atacar / Status] >> ").strip().lower()
        print("\n")
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
    return quer_dizer_sim(decisão)

def cogumelo_efeito(decisão):
    if quer_dizer_sim(decisão):
        efeitodocogumelo = randint(1,5)
        if efeitodocogumelo >= 3:
            print("Você come o cogumelo... e é muito saboroso 🍄✨")
            aventureiro["vida"] += 20
            aventureiro["mana"] += 20
            print("Você recuperou 20 de vida e mana!")
            recuperar_mana()
            evento_na_caverna()
        elif efeitodocogumelo <= 2:
            print("Que cogumelho horrivel! Você não deveria comer tudo que encontra no chão!, Você perde 45 pontos de vida")
            aventureiro["vida"] -= 45
            verificar_morte()
            recuperar_mana()
            evento_na_caverna()

    else:
        print("Você ignora o cogumelo. Melhor prevenir do que remediar... ")
        recuperar_mana()
        evento_na_caverna()
 
def evento_2():
    global contador_de_eventos
    contador_de_eventos += 1
    print("\n Você segue o fluxo estreito das cavernas, até que...Um morcego gigante te ataca!")
    batalha(morcego_gigante)
    verificar_morte()
    ganhar_xp(morcego_gigante)
    morcego_gigante["vida"]+=40
    recuperar_mana()
    evento_na_caverna()


def evento_3():
    global contador_de_eventos
    contador_de_eventos += 1
    print("Você escorrega em uma pedra Perigosamente escorregadia e pontuda!\n")
    
    comando = input("há uma magia que te protegeria nessa situação. Oque fazer?> ").strip().lower()
    
    if comando == "utani hur":
        if aventureiro["mana"] >= 5:
            aventureiro["mana"] -= 5
            print("\nVocê murmura palavras e, por um momento, sente o seu corpo extremamente rápido, Perigo evitado!\n")
            dano = 0
        else:
            print("\nVocê tenta usar uma mágia, mas não tem mana suficiente!\n")
            dano = 15
    else:
        print("\nVocê não faz ideia de como evitar isso!\n")
        dano = 15

    aventureiro["vida"] -= dano
    if dano > 0:
        print(f"Você bate forte e perde {dano} de vida.")
    else:
        print("Você evita completamente o impacto.")
    
    verificar_morte()
    print("Pelo menos agora você está prestando mais atenção por onde pisa.")
    ganhar_xp(Pedra_perigosamente_escorregadia)
    evento_na_caverna()


def evento_4():
    global contador_de_eventos
    contador_de_eventos += 1
    print("Você encontra uma tocha apagada no chão, ao lado de uma espada feita de um material de alta qualidade.")
    decisão = input("\n\n                Pegar espada? > ").strip().lower()
    if quer_dizer_sim(decisão):
        print("Você empunha a espada com firmeza. Ela brilha mesmo na escuridão. +5 de dano!")
        aventureiro["dano"] += 5 
        recuperar_mana()
        evento_na_caverna()
    else:
        print("Você ignora a espada. Às vezes, o peso da escolha é mais leve que o da lâmina.")
        recuperar_mana()
        evento_na_caverna()
    

def evento_5():
    global contador_de_eventos
    contador_de_eventos += 1
    print("Você encontra um esqueleto no chão da caverna. Ele aparenta ter alguns pertences... deseja vasculhar?")
    quervasculhar = input("> ").strip().lower()
    if quer_dizer_sim(quervasculhar):
        possiveis_loots = [
            ("grimório do druida", efeito_grimorio_druida),
            ("espada afiada", efeito_espada_afiada),
            ("grimório arcano", efeito_grimorio_arcano),
            ("grimório do arqueiro", efeito_grimorio_arqueiro),
            ("grimório do guerreiro", efeito_grimorio_guerreiro),
            ("cristal de mana", efeito_cristal_mana),
            ("cristal de vida", efeito_cristal_vida)
        ]

        loot, funcao_efeito = possiveis_loots[randint(0, 6)]

        print(f"\nVocê encontra: {loot.upper()}!")
        funcao_efeito()
        input("\n Pressione >ENTER< para continuar sua jornada")
        evento_na_caverna()
    else:
        print("Você decide não mexer nos pertences do esqueleto. Melhor não perturbar os mortos e continua caminhando...")
        evento_na_caverna()
    

def efeito_grimorio_druida():
    print("A maioria das páginas estão sujas, mas algumas palavras parecem repelir as impurezas. >exura< e >exori utamo<, talvez elas sejam interessantes de serem usadas em uma >batalha<")

def efeito_espada_afiada():
    print("A lâmina brilha ainda mais que a sua! o seu dano aumentou em 5")
    aventureiro["dano"] += 5
def efeito_grimorio_arcano():
    print("O grimório pulsa com magia pura e parece se comunicar com você...>utani hur< pode ser usado para fugir de armadilhas e >exori vis< causará grande dano em batalha")

def efeito_grimorio_arqueiro():
    print("O grimório diz detalhadamente da sensação do espirito e da flecha se mesclando em batalha. >exori con< e >utito san< podem ser usado em batalha")
def efeito_grimorio_guerreiro():
    print("uma carta com sangue relata inúmeras situações de luta e tecnicas que um guerreiro usou para subjulgar os seus inimigos. >exori< e >exori kor< podem ser usados em batalha")

def efeito_cristal_mana():
    print("Um cristal que no piscar de olhos se mescla com a sua alma. +15 de mana máxima")
    aventureiro["mana"] += 15
    aventureiro["manamaxima"] += 15
def efeito_cristal_vida():
    print("Você sente uma aura quente e reconfortante. Suas feridas se fecham e seus musculos crescem.")
    aventureiro["vida"] +=10
    aventureiro["vidamaxima"] +=10


def evento_6():
    global contador_de_eventos 
    contador_de_eventos += 1

    print("Você encontra um homem ferido pedindo ajuda. Ele está preso entre as pedras.")
    print("""Ele diz:
                -Você, ajudar, eu, esmagado, doer, muito! puxe, eu.""")

    if jogador_ajuda_o_homem():
        resolver_armadilha_com_ajuda()
    else:
        resolver_armadilha_sem_ajuda()

def jogador_ajuda_o_homem():
    resposta = input("Ajudar? (sim/não) > ").strip().lower()
    return resposta in ["sim", "s"]

def resolver_armadilha_com_ajuda():
    print("Você tenta puxar o homem pelo braço, mas rapidamente ele desliza entre as pedras e te morde causando 35 de dano.")
    aventureiro["vida"] -= 35
    verificar_morte()

    print("A aparência dele muda diante dos seus olhos. Você está diante de um lagarto-das-cavernas!")
    enfrentar_lagarto()

def resolver_armadilha_sem_ajuda():
    print("Você decide passar direto, mas um som atrás de você chama a sua atenção.")
    print("Aquilo tudo era uma armadilha! Não existia homem nenhum, era um lagarto-das-cavernas disfarçado!")
    enfrentar_lagarto()

def enfrentar_lagarto():
    batalha(lagarto_das_cavernas)
    verificar_morte()
    ganhar_xp(lagarto_das_cavernas)
    recuperar_mana()
    lagarto_das_cavernas["vida"] += 60
    evento_na_caverna()


def evento_7():
    global contador_de_eventos
    contador_de_eventos += 1
    print("\n Você segue até que...Um coelho agressivo avança contra você!")
    batalha(coelho_agressivo)
    verificar_morte()
    ganhar_xp(coelho_agressivo)
    coelho_agressivo["vida"]+=10
    recuperar_mana()
    evento_na_caverna()

def evento_8():
    global contador_de_eventos
    contador_de_eventos += 1
    print("\n Você se depara com uma alcateia de lobos que avança contra você, é aterrorizante.")
    batalha(lobo_faminto)
    verificar_morte()
    ganhar_xp(lobo_faminto)
    lobo_faminto["vida"]+=25
    recuperar_mana()
    print("ainda há mais lobos aqui...")
    batalha(lobo_faminto)
    verificar_morte()
    ganhar_xp(lobo_faminto)
    lobo_faminto["vida"]+=25
    recuperar_mana()
    print("os lobos se afastam com medo de você, mas um ainda está confiante, o ALFA")
    print("o lobo Alfa quer vingança")
    batalha(lobo_alfa)
    verificar_morte()
    ganhar_xp(lobo_alfa)
    lobo_alfa["vida"]+=40
    evento_na_caverna()

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
    return quer_dizer_sim(decisao)
    

def beber_agua(decisao):
    if quer_dizer_sim(decisao):
        print("""
              \n\n\nVocê começa a sentir um mal-estar, você cambalea e começa a perder o equilíbrio, voce procura um local de apoio, porém acaba caindo e perdendo a consciência. . .\n\n\nAo acordar, você nota que suas mãos estão amarradas, ao olhar a o redor, uma figura pequena, feia e nojenta com uma faca em sua cintura te encara de olhos abertos e salivando pela boca. . .\n\n\n
            
              """)
        goblin()
    else:
        print("\n\n\nApesar da sede, você ignora o poço, após uma longa caminhada voce se depara com uma estrutura relativamente pequena, talvez seria possivel que uma crianca morasse ai, mas o que uma crianca estaria fazendo dentro dessa casa voce se pergunta\n\n\nDe repente, vindo da sua esquerda, uma criatura pequena e rapida com a faca em sua direcao avanca, voce consegue desviar!")
        batalha(goblim)
        verificar_morte()
        ganhar_xp(goblim)
        goblim["vida"]+=50
        recuperar_mana()
        goblim["vida"] +=50
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
                recuperar_mana()
                goblim["vida"] +=50
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
    evento_na_caverna()      


def evento_11():
    global contador_de_eventos 
    contador_de_eventos += 1
    print("Você acha um artefato antigo e poderoso!")



eventos = [evento_1, evento_2, evento_3, evento_4, evento_5, evento_6, evento_7, evento_8, evento_9, evento_10, evento_11]
def evento_na_caverna():
    print(f"Você já percorreu {contador_de_eventos} câmara(s)")
    perguntar_continuar_aventura()
    print("Hora de seguir em frente na caverna... \n")
    print(" -------------------------------------------------------------------------")
    evento_escolhido = randint(0,10)
    eventos[evento_escolhido]()

#área de teste de eventos
#evento_1()
evento_3()
print(f"Dano: {aventureiro['dano']} | Vida: {aventureiro['vida']}")
