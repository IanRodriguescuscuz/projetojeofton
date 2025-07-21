from random import randint
import artes

reset = "\033[0m"
bold = "\033[1m"
italico = "\033[3m"
underline = "\033[4m"
normal = "\033[22m"

preto = "\033[30m"
vermelho = "\033[91m"
verde = "\033[92m"
amarelo = "\033[93m"
azul = "\033[94m"
magenta = "\033[95m"
ciano = "\033[96m"
branco = "\033[97m"
marrom = "\033[38;5;94m"
Rosa_claro = "\033[38;5;218m"
rosa_medio= "\033[38;5;212m"
verdelima = "\033[1;32m"
laranja = "\033[38;5;208m"
roxo = "\033[38;5;165m"
vermelho_escuro = "\033[38;5;52m"
fundo = "\033[40m"
fundobranco ="\033[47m"

def estilizar(texto, cor=branco, estilo=bold):
    return f"{estilo}{cor}{texto}{reset}"


def narrar(texto):
    print(estilizar(texto, cor=magenta))

def contando(texto):
    print(estilizar(texto, cor=marrom, estilo=normal))

def lascou(texto):
    print(estilizar(texto, cor=vermelho))

def estilo_envenenado(texto):
    print(estilizar(texto, cor=verde, estilo=normal))

def pos_batalha(texto):
    print(estilizar(texto, cor=amarelo, estilo=italico))

def xp_pos_batalha(texto):
    print(estilizar(texto, cor=verdelima))

def mana_pos_batalha(texto):
    print(estilizar(texto, cor=azul,estilo=normal))

def magia_linda(texto):
    print(estilizar(texto, cor=Rosa_claro,estilo=italico))

def magia_linda_cheguei(texto):
    print(estilizar(texto, cor=rosa_medio,estilo=bold))

def raridade(texto):
    print(estilizar(texto, cor=laranja, estilo=underline))

def cuidado(texto):
    print(estilizar(texto, cor=vermelho, estilo=underline))

def eletricidade(texto):
    print(estilizar(texto, cor=roxo,estilo=normal))

def morrendo(texto):
    print(estilizar(texto, cor=vermelho_escuro,estilo=bold))

def narração_final(texto):
    print(estilizar(texto, cor=preto,estilo=bold))

def narração_final_pergunta(pergunta):
    return input(estilizar(pergunta + " ", cor=preto, estilo=normal))

def narração_final_perguntap(pergunta):
    return input(estilizar(pergunta + " ", cor=branco))

def entrada_pergunta(pergunta):
    return input(estilizar(pergunta + " ", cor=ciano))

def entrada_pergunta_linda(pergunta):
    return input(estilizar(pergunta + " ", cor=Rosa_claro))


def tela_inicial():
    print("\033[1;32m")  
    print(r"""           _  _             _  _
  .       /\ /%\       .   /%\/%\     .
      __.<\%#//\\,_       <%%#/%%\\,__  .
.    <%#/|\\%%%#///\\    /^%#%%\\///%#\\
      ""/%/""\\ \""//|   |/""'/ /\\//"//'
 .     L/'`   \\ \\  `    "   / /  ```
        `      \\ \\     .   / /       .
 .       .      \\ \\       / /  .
        .        \\ \\     / /          .
   .      .    ..:\ \\:::/ /:.     .     .
______________/ \\__;\___/\;_/\\________________________________
YwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYw
""")
    print("\033[1;37m") 
    print("                  \033[1;34m----------------------------------------------\033[1;37m")
    print(f"                {branco}|     escreva \"{amarelo}aventura{reset}{branco}\" ou \"{amarelo}{bold}ajuda{reset}{branco}\" para começar  |{reset}")
    print("                  \033[1;34m----------------------------------------------\033[0m\n")
    print("                     \033[1;35mhero's insistence")
    print("                          ~ O Rpg\033[0m")

def quer_dizer_sim(resposta):
    resposta = resposta.strip().lower()
    return resposta in [
        "sim", "s", "aventura", "vamo", "vamos", "claro", "bora", "beber", "comer", "dale", "daledele", "daledeledeledoly", "continuar", "pegar", "ir", "entrar", "cogumelo", "sm", "simm","go","sin", "","status"
    ]
    
def verificar_ajuda_antes_de_jogar():
    resposta = entrada_pergunta(f"\n\n{branco}                Vamos entrar nesta caverna? > {reset}").strip().lower()

    if resposta == "ajuda":
        print(f"""
{azul}                ------------------------------------ {amarelo}COMO JOGAR{azul} ------------------------------------{reset}
{verde}
                - Este é um RPG de texto, descrições apareceram!
                - Você poderá encontrar inimigos ou situações que podem colocar a sua aventura em risco!
                - Escreva ou aperte ENTER para interagir com as situações, cada uma necessita de uma reacão diferente.
                - Responda com atenção, Neste jogo você enfrenterá eventos que aparecerão aleatóriamente a cada sala.
                - Dicas e segredos podem aparecer no caminho...
                - Magias possuem palavras que ao digitar em batalha efeitos acontecem, fique atento pois elas aparecerão ao decorrer da aventura.
{azul}                --------------------------------------------------------------------------------------------{reset}
        """)
        resposta_ajuda = entrada_pergunta(f"\n{branco}                Vamos começar? ({verde}sim{branco}/{vermelho}não{branco}) > {reset}").strip().lower()
        return quer_dizer_sim(resposta_ajuda)
    else:
        return quer_dizer_sim(resposta)




def perguntar_nome():
    print("\n")
    print("""         ---------------------------------------
        |     Qual o seu nome, aventureiro?      |
        |                                        |
        |                                        |
         ---------------------------------------""")
    nomedoaventureiro = input("                    > ").strip().title()
    return nomedoaventureiro

tela_inicial()

def status():
    if aventureiro["utito_san"] == True:
        estadodoutito= "\033[93mutito san\033[0m"
    else:
        estadodoutito= "nenhum"
            
    print(f"""
    ---- Status ----
    Nome: {aventureiro['nome']}
    Vida: {aventureiro['vida']}/{aventureiro['vidamaxima']}
    Mana: {aventureiro['mana']}/{aventureiro['manamaxima']}
    Dano: {aventureiro['dano']}
    XP: {aventureiro['exp']} / {aventureiro['expmaximo']}
    Buffs ativos: {estadodoutito}
    ----------------
    """)

if verificar_ajuda_antes_de_jogar():
    nomedoaventureiro = perguntar_nome()
    aventureiro = {"nome": nomedoaventureiro,
               "dano": 10,
               "vida": 100,
               "vidamaxima":100,
               "exp":0,
               "expmaximo":70,
               "mana":50,
               "manamaxima":50,
               "manaregen": 5,
               "utito_san": False,
               "envenenado": False,
               "contadordecristal": 0,   
               "sangramento": False,            
               }
    print(f"\nBem-vindo, {aventureiro['nome']}! Sua aventura começa {laranja}agora...{reset}\n")
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
    "dano": 15,
    "vida": 40,
    "exp":20,

}

Pedra_perigosamente_escorregadia = {

    "nome":"Pedra perigosamente escorregadia",
    "dano": 15,
    "vida": 1,
    "exp":20,

}

def danodolagarto():
    return randint(10, 26)

lagarto_das_cavernas = {
    "nome":"lagarto-das-cavernas",
    "dano": 0,
    "vida": 60,
    "exp":60,
}
Rainha_do_caos_abissal = {
    "nome":"Rainha do caos abissal",
    "dano": 10,
    "vida":50,
    "exp": 60,

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
    "dano": 20,
    "vida": 45,
    "exp":30,
}

Moreno = {
    "nome":"Moreno",
    "dano": 1,
    "vida": 1,
    "exp":500,
}

contador_de_eventos = 0
aventureiro_magias = []

def recuperar_mana():
    if aventureiro["mana"] < aventureiro["manamaxima"]:
        aventureiro["mana"] += aventureiro["manaregen"]
        mana_pos_batalha(f"Você naturalmente recupera {aventureiro ['manaregen']} pontos de mana")


lista_de_magias = ["utani hur", "exura", "exori", "exori kor", "exori con", "exori utamo", "utito san", "exori vis"]

def chance_de_aprender_magia():
    chance_de_aprender=randint(1,5)
    if chance_de_aprender == 5:
        aprender_magia()

def aprender_magia():
    if not lista_de_magias:
        magia_linda_cheguei("Você já aprendeu todas as magias disponíveis.")
        return
    
    magia_escolhida = randint(0, len(lista_de_magias) - 1)

    magia = lista_de_magias.pop(magia_escolhida) 
    aventureiro_magias.append(magia)
    if magia == "utani hur":
        magia_linda_cheguei(f"A palavra {branco}{bold}{magia}{reset} {rosa_medio}ecoa em seus pensamentos... Talvez sirva de algo em armadilhas...{reset}")
    else:
        magia_linda_cheguei(f"A palavra {branco}{bold}{magia}{reset} {rosa_medio}ecoa em seus pensamentos... Talvez sirva em alguma batalha...{reset}")

def ganhar_xp(npc):
    pos_batalha(" -------------------------------------------------------------------------")
    pos_batalha("A Batalha foi árdua, mas a esperança de achar uma saída segue crescente.")
    pos_batalha(f"Você derrotou {npc['nome']} e ganhou {npc['exp']} de experiência! ")

    aventureiro["exp"] += npc["exp"]
    if aventureiro["exp"] <= aventureiro["expmaximo"]:
        chance_de_aprender_magia()

    while aventureiro["exp"] >= aventureiro["expmaximo"]:
        aventureiro["exp"] -= aventureiro["expmaximo"]  
        aventureiro["dano"] += 5
        aventureiro["vida"] += 20
        aventureiro["vidamaxima"] += 20
        aventureiro["expmaximo"] += 30 
        aventureiro["mana"] += 10
        aventureiro["manamaxima"] += 10
        print(f"{branco}Você subiu de nível! +5 de dano, +20 de vida máxima e 10 de mana máxima!{reset}")
        aprender_magia()
    xp_pos_batalha(f"XP atual: {aventureiro['exp']} / {aventureiro['expmaximo']}")
    pos_batalha("-------------------------------------------------------------------------")

def verificar_morte():
    limpar_buff_condicaos()
    if aventureiro["vida"] <= 0:
        morrendo(f"\n {fundo}Você morreu. Sua jornada termina aqui.{reset} ")
        exit()
    

def perguntar_continuar_aventura():
    resposta = entrada_pergunta("\nVocê deseja continuar explorando a caverna? > ").strip().lower()
    if quer_dizer_sim(resposta):
        contando("\nVocê respira fundo e segue adiante na escuridão...\n")
    else:
        print("\n")
        print(f"{preto}{fundobranco}Você encara a escuridão e ela te encara de volta. Isso não foi uma boa ideia.{reset}")
        print("\n")
        print(f"{branco}{fundo}fim.{reset}")
        exit()

def batalha(npc):
    lascou("\nA batalha começou!")

    def exura():
        if aventureiro["mana"] >= 10:
            aventureiro["vida"] += 40
            aventureiro["mana"] -= 10
            print(f"Você se cura em {vermelho}+40 de vida!{reset}")
        else:
            print("Você não tem mana suficiente!")
    
    def exori():
        if aventureiro["mana"] >= 25:
            aventureiro["mana"] -= 25
            npc["vida"] -= aventureiro["dano"]*2+5
            print(f"{vermelho}você conjura um ataque devastador e brutal.{reset}")
            if npc["vida"] > 0:
                aventureiro["vida"] -= npc["dano"]
                cuidado(f"O {npc['nome']} está gravimente ferido, mas revida e causa {npc['dano']} de dano!")
            else:
                print(f"O {npc['nome']} foi DEVASTADO!")
        else:
            print("Você não tem mana suficiente!")

    def morenoaltomusculoso():
        npc["vida"] = 0
        print(f"{verdelima}{fundo}O {npc["nome"]} encara mozao e morre xD{reset}")
        
    def exori_kor():
        if aventureiro["mana"] >= 10:
            aventureiro["mana"] -= 10
            npc["vida"] -= aventureiro["dano"]
            aventureiro["vida"] += aventureiro["dano"]+10
            lascou(f"A sua lâmina conjura um ataque vampírico que te cura em {aventureiro['dano']+10} ")
            if npc["vida"] > 0:
                aventureiro["vida"] -= npc["dano"]
                cuidado(f"O {npc['nome']} está assutado, mas revida e causa {npc['dano']} de dano!")
            else:
                print(f"O {npc['nome']} foi derrotado")
        else:
            print("Você não tem mana suficiente!")

    def exori_con():
        if aventureiro["mana"] >= 5:
            aventureiro["mana"] -= 5
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
            if aventureiro["utito_san"] == False:
                aventureiro["dano"] += 5
                pos_batalha(f"{fundo}Voce sente agora poderes sagrados guiando sua espada. . . Seu poder aumentou{reset}")
                aventureiro["utito_san"] = True
            else:
                print("Utito san ja está ativo")
                aventureiro["mana"] += 10
        else:
            print("Você não tem mana suficiente!")

    def exori_utamo():
        if aventureiro["mana"] >= 20:
            aventureiro["mana"] -= 20
            npc["vida"] -= aventureiro["mana"]*2
            mana_pos_batalha(f"Você lança uma esfera mágica feita de pura mana que causa {aventureiro['mana']*2} de dano no {npc['nome']}!")
            print("Você sente que o próximo exori utamo vai ser menos eficaz")
            if npc["vida"] <= 0:
                print(f"O {npc['nome']} foi evaporado!")
        else:
            print("Você não tem mana suficiente!")

    def exori_vis():
        if aventureiro["mana"] >= 10:
            aventureiro["mana"] -= 10
            npc["vida"] -= 25
            eletricidade(f"Você lança uma esfera elétrica que causa 25 de dano no {npc['nome']}!")
            if npc["vida"] <= 0:
                print(f"O {npc['nome']} virou churrasco!")
        else:
            print("Você não tem mana suficiente!")

    def magia():

        if not aventureiro_magias:
            magia_linda(""">>> Magias possuem palavras mágicas.
                     as diga e elas aconteceram!  <<<""")
        else:
            magias_formatadas = ', '.join(aventureiro_magias)
            print(f"As {branco}palavras{reset} {Rosa_claro}{bold}{magias_formatadas}{reset} já ecoaram na sua cabeça")
        
            
    def atacar():
        npc["vida"] -= aventureiro["dano"]
        print(f"Você ataca e causa{laranja} {aventureiro['dano']}{reset} de dano no  {npc['nome']}!")
        if npc["vida"] > 0:
            aventureiro["vida"] -= npc["dano"]
            cuidado(f"O {npc['nome']} revida e causa {npc['dano']} de dano!")
        else:
            print(f"O {npc['nome']} foi {laranja}derrotado!{reset}")

    ações_na_batalha = {
        "exura": exura, #cura
        "atacar": atacar,
        "status": status,
        "exori": exori, #Dano brutal com espada
        "exori kor": exori_kor, #Ataque que cura
        "exori con": exori_con, #Ataque a distancia
        "exori utamo": exori_utamo, #Dano dependente da quantidade de mana
        "utito san": utito_san, #resolver
        "exori vis": exori_vis, #choque
        "magia":magia,
        "morenoaltomusculoso": morenoaltomusculoso, 
    }

    while aventureiro["vida"] > 0 and npc["vida"] > 0:
        if aventureiro["envenenado"] == True:
            aventureiro["vida"] -= 10
            estilo_envenenado("Você está envenenado e perde 10 de vida")
        if npc["nome"] == "lagarto-das-cavernas":
            npc["dano"] = danodolagarto()
        ação = entrada_pergunta("\nO que você vai fazer? > [Magia / Atacar / Status] >> ").strip().lower()
        print("\n")
        if ação in ações_na_batalha:
            ações_na_batalha[ação]()
        else:
            print("Você não consegue fazer isso!")

def limpar_buff_condicaos():
    aventureiro["envenenado"] = False
    if aventureiro["utito_san"]: 
        aventureiro["dano"] -= 5  
        aventureiro["utito_san"] = False
    if aventureiro["vida"] > aventureiro["vidamaxima"]:
        aventureiro["vida"] = aventureiro["vidamaxima"]
        print(f"Toda sua vitalidade excendente se esvai. . . \nVida atual:{aventureiro['vida']}")


def evento_1():
    global contador_de_eventos
    print("Você adentra na caverna e encontra um cogumelo estranho, mas bem apetitoso")
    print(artes.cogumeloasc) #---RESOLVER ESTILOS---
    decisão = entrada_pergunta("\n\n                comer? > ").strip().lower()
    contador_de_eventos += 1
    cogumelo_efeito(decisão)
    return quer_dizer_sim(decisão)

def cogumelo_efeito(decisão):
    if quer_dizer_sim(decisão):
        efeitodocogumelo = randint(1,5)
        if efeitodocogumelo >= 3:
            print(f"Você come o cogumelo... e é muito {rosa_medio}saboroso{reset} 🍄✨")
            aventureiro["vida"] += 20
            aventureiro["mana"] += 20
            print(f"Você recuperou 20 de {vermelho}vida{reset} e {azul}mana!{reset}")
            recuperar_mana()
            evento_na_caverna()
        elif efeitodocogumelo <= 2:
            print(f"Que cogumelho horrivel! Você não deveria comer tudo que encontra no chão!, {vermelho}{underline}Você perde 45 pontos de vida{reset}")
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
    print(artes.morcegosasc)#---RESOLVER ESTILOS---
    batalha(morcego_gigante)
    verificar_morte()
    ganhar_xp(morcego_gigante)
    morcego_gigante["vida"]=40
    recuperar_mana()
    evento_na_caverna()


def evento_3():
    global contador_de_eventos
    contador_de_eventos += 1
    print("Você escorrega em uma pedra Perigosamente escorregadia e pontuda!\n")
    
    comando = entrada_pergunta("há uma magia que te protegeria nessa situação. Oque fazer?> ").strip().lower()
    
    if comando == "utani hur":
        if aventureiro["mana"] >= 5:
            aventureiro["mana"] -= 5
            print("\nVocê murmura palavras e, por um momento, sente o seu corpo extremamente rápido, Perigo evitado!\n")
            dano = 0
        else:
            print("\nVocê tenta usar uma mágia, mas não tem mana suficiente!\n")
            dano = 25
    else:
        print("\nVocê não faz ideia de como evitar isso!\n")
        dano = 25

    aventureiro["vida"] -= dano
    if dano > 0:
        lascou(f"Você bate forte e perde {dano} de vida.")
    else:
        print("Você evita completamente o impacto.")
    
    verificar_morte()
    print("Pelo menos agora você está prestando mais atenção por onde pisa.")
    evento_na_caverna()


def evento_4():
    global contador_de_eventos
    contador_de_eventos += 1
    print("Você encontra uma tocha apagada no chão, ao lado de uma espada feita de um material de alta qualidade.")
    decisão = entrada_pergunta("\n\n                Pegar espada? > ").strip().lower()
    print(artes.espadaasc) #---RESOLVER ESTILOS---
    if quer_dizer_sim(decisão):
        print(f"Você empunha a espada com firmeza. Ela brilha mesmo na escuridão. {laranja}+5 de dano!{reset}")
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
    print(artes.caveiraasc) 
    quervasculhar = entrada_pergunta("> ").strip().lower()
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

        print(f"\nVocê encontra:{laranja}{italico}{loot.upper()}{reset}!")
        funcao_efeito()
        entrada_pergunta("\n Pressione >ENTER< para continuar sua jornada")
        evento_na_caverna()
    else:
        print("Você decide não mexer nos pertences do esqueleto. Melhor não perturbar os mortos e continua caminhando...")
        evento_na_caverna()
    

def efeito_grimorio_druida():
    print(f"A maioria das páginas estão sujas, mas algumas palavras parecem repelir as impurezas. >{underline}{verde}exura{reset}< e >{underline}{azul}exori utamo{reset}<, talvez elas sejam interessantes de serem usadas em uma >batalha<")

def efeito_espada_afiada():
    print(f"A lâmina brilha ainda mais que a sua! o seu dano aumentou em {laranja}5{reset}")
    aventureiro["dano"] += 5
def efeito_grimorio_arcano():
    print(f"O grimório pulsa com magia pura e parece se comunicar com você...>{underline}{verdelima}utani hur{reset}< pode ser usado para fugir de armadilhas e >{underline}{roxo}exori vis{reset}< causará grande dano em batalha")

def efeito_grimorio_arqueiro():
    print(f"O grimório diz detalhadamente da sensação do espirito e da flecha se mesclando em batalha. >{underline}{vermelho}exori con{reset}< e >{underline}{amarelo}utito san{reset}< podem ser usado em batalha")
def efeito_grimorio_guerreiro():
    print(f"uma carta com sangue relata inúmeras situações de luta e tecnicas que um guerreiro usou para subjulgar os seus inimigos. >{underline}{laranja}exori{reset}< e >{underline}{vermelho}exori kor{reset}< podem ser usados em batalha")

def efeito_cristal_mana():
    print(f"Um cristal que no piscar de olhos se mescla com a sua alma. {azul}+15 de mana máxima{reset}")
    aventureiro["mana"] += 15
    aventureiro["manamaxima"] += 15
def efeito_cristal_vida():
    print(f"Você sente uma aura quente e reconfortante. {vermelho}Suas feridas se fecham{reset} e seus musculos crescem.")
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
    resposta = entrada_pergunta("Ajudar? (sim/não) > ").strip().lower()
    return resposta in ["sim", "s"]

def resolver_armadilha_com_ajuda():
    print(f"Você tenta puxar o homem pelo braço, mas rapidamente ele desliza entre as pedras e {vermelho}te morde causando 35 de dano.{reset}")
    aventureiro["vida"] -= 35
    verificar_morte()

    print("A aparência dele muda diante dos seus olhos. Você está diante de um lagarto-das-cavernas!")
    enfrentar_lagarto()

def resolver_armadilha_sem_ajuda():
    print("Você decide passar direto, mas um som atrás de você chama a sua atenção.")
    print("Aquilo tudo era uma armadilha! Não existia homem nenhum, era um lagarto-das-cavernas disfarçado!")
    enfrentar_lagarto()

def enfrentar_lagarto():
    print(artes.lagartoasc) #---RESOLVER ESTILOS---
    batalha(lagarto_das_cavernas)
    verificar_morte()
    ganhar_xp(lagarto_das_cavernas)
    recuperar_mana()
    lagarto_das_cavernas["vida"] = 60
    evento_na_caverna()


def evento_7():
    global contador_de_eventos
    contador_de_eventos += 1
    print(f"\n Você segue até que...Um coelho {Rosa_claro}agressivo{reset} avança contra você!")
    print(artes.coelhoasc)
    batalha(coelho_agressivo)
    verificar_morte()
    ganhar_xp(coelho_agressivo)
    coelho_agressivo["vida"]=10
    recuperar_mana()
    evento_na_caverna()

def evento_8():
    global contador_de_eventos
    contador_de_eventos += 1
    print("\n Você se depara com uma alcateia de lobos que avançam contra você, é aterrorizante.")
    print(artes.loboasc)
    batalha(lobo_faminto)
    verificar_morte()
    ganhar_xp(lobo_faminto)
    lobo_faminto["vida"]=25
    recuperar_mana()
    cuidado("ainda há mais lobos aqui...")
    print(artes.loboasc)
    batalha(lobo_faminto)
    verificar_morte()
    ganhar_xp(lobo_faminto)
    lobo_faminto["vida"]=25
    recuperar_mana()
    print(f"os lobos se afastam com medo de você, mas um ainda está confiante, o {laranja}ALFA{reset}")
    print(f"o lobo {laranja}Alfa{reset} quer vingança")
    print(artes.loboalfaasc)
    batalha(lobo_alfa)
    verificar_morte()
    ganhar_xp(lobo_alfa)
    recuperar_mana()
    lobo_alfa["vida"]=40
    evento_na_caverna()

def evento_9():
    global contador_de_eventos 
    contador_de_eventos += 1
    print('''
  \033[31m>> : Voce encontra uma area plana e extremamente longa <<\033[0m

    A terra treme sob passos profanos...
    Do abismo em chamas, uma figura surge envolta em névoa carmesim.
    Metade donzela pálida, metade aranha demoníaca,
    Seus oito olhos brilham com a loucura dos Deuses Antigos.
    
    "\033[33mPobre tolo... O fogo que busca o consumirá!\033[0m"

    \033[31m>> A Rainha do Caos Abissal avança em sua direção e corta você! <<\033[0m
''')
    aventureiro["envenenado"] = True
    print(artes.rainhaasc)#---RESOLVER ESTILOS---
    batalha(Rainha_do_caos_abissal)
    verificar_morte()
    ganhar_xp(Rainha_do_caos_abissal)
    Rainha_do_caos_abissal["vida"] = 50
    recuperar_mana()
    evento_na_caverna()
    
    

def evento_10():
    global contador_de_eventos 
    contador_de_eventos += 1
    print("Voce percorre por um caminho estreito, longo e apertado. . .")
    decisao = entrada_pergunta("\n\nVocê chega em área aberta, com um poço de água à sua esquerda, você está cansado. . . você imediatamente sente sede. . .,\n\n\ndeseja beber da água? > ").strip().lower()
    beber_agua(decisao)
    return quer_dizer_sim(decisao)
    

def beber_agua(decisao):
    if quer_dizer_sim(decisao):
        print(f"""
              \n\n\nVocê começa a sentir um mal-estar, você cambalea e começa a perder o equilíbrio, voce procura um local de apoio, porém acaba caindo e perdendo a consciência. . .\n\n\nAo acordar, você nota que {vermelho}suas mãos estão amarradas{reset}, ao olhar a o redor, uma figura pequena, feia e nojenta com uma faca em sua cintura te encara de olhos abertos e salivando pela boca. . .\n\n\n
            
              """)
        goblin()
    else:
        print("\n\n\nApesar da sede, você ignora o poço, após uma longa caminhada voce se depara com uma estrutura relativamente pequena, talvez seria possivel que uma crianca morasse ai, mas o que uma crianca estaria fazendo dentro dessa casa voce se pergunta\n\n\nDe repente, vindo da sua esquerda, uma criatura pequena e rapida com a faca em sua direcao avanca, voce consegue desviar!")
        print(artes.goatdasilvaasc)#---RESOLVER ESTILOS---
        batalha(goblim)
        verificar_morte()
        ganhar_xp(goblim)
        goblim["vida"]=50
        recuperar_mana()
        evento_na_caverna()


def goblin():
    tentativas = 0
    print(f"{vermelho}Suas mãos estão amarradas{reset}. O goblin caminha em sua direção, afiando sua faca...")

    while True:
        if aventureiro["vida"] <= 0:
            morrendo("Você sucumbiu aos ferimentos enquanto tentava escapar...")
            exit()

        opcao = entrada_pergunta("\nO que você vai fazer? [desamarrar / esperar] > ").strip().lower()

        if opcao == "desamarrar":
            tentativas += 1
            chance = randint(0, 6)
            if chance >= 3:
                print("\n Você consegue se soltar! O goblin percebe e investe contra você com a faca em sua direção")
                print(artes.goatdasilvaasc)#---RESOLVER ESTILOS---
                batalha(goblim)
                verificar_morte()
                ganhar_xp(goblim)
                recuperar_mana()
                goblim["vida"] =50
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

    magia_linda(
        "✧･ﾟ: *✧･ﾟ:* *:･ﾟ\n Você encontra um ambiente diferente do usual, "
        "um local cheio de pedras brilhantes, coloridas e com um ar acolhedor. "
        "Você olha para o teto e consegue enxergar luzes vindas do sol. \n✧･ﾟ: *✧･ﾟ:* *:･ﾟ"
    )

    lista_de_cor_da_fada = ["vermelha", "azul", "azul-aqua", "amarela", "verde", "roxa"]
    chance_da_cor = randint(0, 5)

    entrada_pergunta_linda(
        f" Ao longe, você vê uma pequena figura {lista_de_cor_da_fada[chance_da_cor]} "
        "vindo em sua direção...\n\n ✧･ﾟ: *✧･ﾟ:* *:･ﾟTecle ENTER para continuar"
    )

    cores = [vermelho,azul,ciano,amarelo,verde,roxo]

    print(artes.fadaasc)#---RESOLVER ESTILOS---
    
    aprender_magia()

    aventureiro["vida"] += 15
    aventureiro["manaregen"] += 2

    entrada_pergunta_linda(
        "\nSua vida aumenta em 15, e sua regeneração de mana em 2..."
        "\n✧･ﾟ: *✧･ﾟ:* *:･ﾟTecle ENTER para continuar"
    )

    pos_batalha(
        "\nVocê se enche de determinação!\n✧･ﾟ: *✧･ﾟ:* *:･ﾟ"
    )

    evento_na_caverna()



eventos = [evento_1, evento_2, evento_3, evento_4, evento_5, evento_6, evento_7, evento_8, evento_9, evento_10, evento_11]
def evento_na_caverna():
    if contador_de_eventos == 0:
            evento_escolhido = randint(0,10)
            eventos[evento_escolhido]()
    elif contador_de_eventos > 9:
        print(f"{laranja}{underline}Voce chegou muito longe . . .{reset} \n")
    else:
        contando(f"Você já percorreu {contador_de_eventos} câmara(s)")
        perguntar_continuar_aventura()
        contando("Hora de seguir em frente na caverna... \n")
        print(" -------------------------------------------------------------------------")
        evento_escolhido = randint(0,10)
        eventos[evento_escolhido]()

evento_7()

#evento_na_caverna()

input(
    f"{fundobranco}{preto}\033[4mVocê segue o fluxo tortuoso da caverna e encontra uma fenda por onde a luz escapa.{reset}\n"
    f"{fundobranco}{preto}\033[4mAo atravessá-la, por um instante, sente como se tivesse saído — a claridade confunde seus sentidos.{reset}\n"
    f"{fundobranco}{preto}\033[4mMas então seus olhos se ajustam... e você percebe.{reset}\n"
    f"{fundobranco}{preto}\033[4mEstá em um cômodo colossal, inteiramente feito de cristais brancos, como quartzo vivo.{reset}\n"
    f"{fundobranco}{preto}\033[4mNo centro, uma figura feminina o observa — enigmática, imóvel.{reset}\n"
    f"{fundobranco}{preto}\033[4m>>>>{reset}\n "
)


narração_final_pergunta(f"{fundobranco}Sofra,{reset}")
narração_final_pergunta(f"{fundobranco}Treine,{reset}")
narração_final_pergunta(f"{fundobranco}Melhore,{reset}")
narração_final_pergunta(f"{fundobranco}Busque,{reset}")
narração_final_pergunta(f"{fundobranco}E então...{reset}")
narração_final_pergunta(f"{fundobranco}Me enfrente.{reset}")
input("")
#a narração abaixo vai ser reutilizada em futuras atualizações
#narração_final_pergunta(f"{fundo}Me sirva ,{reset}")
#narração_final_pergunta(f"{fundo}Faça tudo oque eu pedir,{reset}")
#narração_final_pergunta(f"{fundo}Me chame de rei, de mestre, de senhor.{reset}")
#narração_final_pergunta(f"{fundo}e quem sabe assim,{reset}")
#narração_final_pergunta(f"{fundo}Eu te permita viver.{reset}")

def fim_do_jogo():
    print(f"{fundobranco}{preto}{underline}Com um último golpe, o corpo da Dama Cristalizada começa a rachar silenciosamente...{reset}")
    print(f"{fundobranco}{preto}Ela não grita. Apenas encara você — com algo entre alívio e tristeza — antes de se despedaçar em pó cintilante.{reset}")
    print(f"{fundobranco}{preto}Os cristais ao redor tremem, perdem o brilho, e começam a se desfazer lentamente, como se o tempo finalmente tivesse retomado seu curso.{reset}")
    print(f"{fundobranco}{preto}Vultos humanos, antes presos dentro das paredes de cristal, evaporam em luz suave. Suas almas, enfim, livres.{reset}\n")
    print(f"{fundobranco}{preto}No fundo da sala, onde antes havia apenas uma parede maciça, o vazio toma forma.{reset}")
    print(f"{fundobranco}{preto}{underline}Uma passagem se revela entre os fragmentos que caem... a saída está diante de você.{reset}\n")
    input("")
    input(f"{fundo}fim da aventura,{laranja}por hoje...{reset}")


input(f"\n{fundo}{branco}{underline}A sua ultima batalha acaba de {vermelho}começar.{reset}\n{fundobranco}{preto}>>{reset}")
print(artes.damaasc)

dama_cristalizada = {
    "nome":"Dama Cristalizada",
    "vida": 225,
    "exp": 200, 
    "dano": 70,
     
    }

def batalha_contra_dama(dama_cristalizada):
    def exura():
        if aventureiro["mana"] >= 10:
            aventureiro["vida"] += 40
            aventureiro["mana"] -= 10
            print(f"{fundo}{branco}Você se cura em {vermelho}+40 de vida!{reset}")
            aventureiro["contadordecristal"] += 1
        else:
            print("Você não tem mana suficiente!")
    
    def exori():
        if aventureiro["mana"] >= 25:
            aventureiro["mana"] -= 25
            dama_cristalizada["vida"] -= aventureiro["dano"]*2+5
            print(f"{fundo}{vermelho}você conjura um ataque devastador e brutal.{reset}")
            aventureiro["contadordecristal"] += 1
            
        else:
            print("Você não tem mana suficiente!")

    def morenoaltomusculoso():
        dama_cristalizada["vida"] = 0
        print(f"{verdelima}{fundo}O {dama_cristalizada["nome"]} encara mozao e morre xD{reset}")
        
    def exori_kor():
        if aventureiro["mana"] >= 10:
            aventureiro["mana"] -= 10
            dama_cristalizada["vida"] -= aventureiro["dano"]
            aventureiro["vida"] += aventureiro["dano"]+10
            lascou(f"{fundo}A sua lâmina conjura um ataque vampírico que te cura em {aventureiro['dano']+10} ")
            aventureiro["contadordecristal"] += 1
        else:
            print("Você não tem mana suficiente!")

    def exori_con():
        if aventureiro["mana"] >= 5:
            aventureiro["mana"] -= 5
            dama_cristalizada["vida"] -= aventureiro["dano"]
            print(f"{fundo}{ciano}Você lança uma flecha mágica que causa {laranja}{aventureiro['dano']}{reset}{fundo}{ciano} de dano na {reset}{fundo}{branco}{dama_cristalizada['nome']}!{reset}")
            print(f"{fundo}{ciano}Você ataca de longe e está seguro{reset}")
            
        else:
            print("Você não tem mana suficiente!")

    def utito_san(): 
        if aventureiro["mana"] >= 10:
            aventureiro["mana"] -= 10
            if aventureiro["utito_san"] == False:
                aventureiro["dano"] += 5
                pos_batalha(f"{fundo}Voce sente agora poderes sagrados guiando sua espada. . . Seu poder aumentou{reset}")
                aventureiro["utito_san"] = True
            else:
                print("Utito san ja está ativo")
                aventureiro["mana"] += 10
        else:
            print("Você não tem mana suficiente!")

    def exori_utamo():
        if aventureiro["mana"] >= 20:
            aventureiro["mana"] -= 20
            dama_cristalizada["vida"] -= aventureiro["mana"]*2
            mana_pos_batalha(f"Você lança uma esfera mágica feita de pura mana que causa {aventureiro['mana']*2} de dano na {dama_cristalizada['nome']}!")
            print("Você sente que o próximo exori utamo vai ser menos eficaz")
            aventureiro["contadordecristal"] += 1
        else:
            print("Você não tem mana suficiente!")

    def exori_vis():
        if aventureiro["mana"] >= 10:
            aventureiro["mana"] -= 10
            dama_cristalizada["vida"] -= 25
            eletricidade(f"Você lança uma esfera elétrica que causa 25 de dano na {dama_cristalizada['nome']}!")
            aventureiro["contadordecristal"] += 1
        else:
            print("Você não tem mana suficiente!")

    def magia():

        if not aventureiro_magias:
            magia_linda(""">>> Magias possuem palavras mágicas.
                     as diga e elas aconteceram!  <<<""")
        else:
            magias_formatadas = ', '.join(aventureiro_magias)
            print(f"As {branco}palavras{reset} {Rosa_claro}{bold}{magias_formatadas}{reset} já ecoaram na sua cabeça")
        
            
    def atacar():
        dama_cristalizada["vida"] -= aventureiro["dano"]
        print(f"{fundo}{branco}Você ataca e causa{reset}{laranja}{fundo} {aventureiro['dano']}{reset}{fundo}{branco} de dano na  {reset}{fundobranco}{preto}{dama_cristalizada['nome']}!{reset}")
        aventureiro["contadordecristal"] += 1
        
        
        
    ações_na_batalha = {
    "exura": exura, #cura
    "atacar": atacar,
    "status": status,
    "exori": exori, #Dano brutal com espada
    "exori kor": exori_kor, #Ataque que cura
    "exori con": exori_con, #Ataque a distancia
    "exori utamo": exori_utamo, #Dano dependente da quantidade de mana
    "utito san": utito_san, #resolver
    "exori vis": exori_vis, #choque
    "magia":magia,
    "morenoaltomusculoso": morenoaltomusculoso, 
}

    while dama_cristalizada["vida"] > 0 and aventureiro["vida"] > 0:
        ação = input(f"\n{fundo}{branco}O que você vai fazer? > [Magia / Atacar / Status] >> {reset}").strip().lower()
        print("\n")
        if aventureiro["contadordecristal"] > 6 and aventureiro["contadordecristal"] < 12:
            print(f"{fundobranco}{underline}{preto}Você sente um leve desconforto, {reset}{fundo}{vermelho}você perde 5 pontos de vida. . .{reset}\n")
            aventureiro["vida"] -= 5
        elif aventureiro["contadordecristal"] > 11 and aventureiro["contadordecristal"] < 16:
            print(f"{fundobranco}{underline}{preto}Seus musculos já estão se cristalizando e isso {fundo}{branco}Doi Demais. {reset}{fundo}{vermelho}você perde 15 pontos de vida. . .{reset}\n")
            aventureiro["vida"] -= 15
        elif aventureiro["contadordecristal"] > 16:
            print(f"{fundobranco}{preto}{underline}Você mal sente a dor agora — só o frio do cristal tomando o que restava de você.{reset}")
            print(f"{fundo}{vermelho}Você perde 25 pontos de vida. . .{reset}\n")
            aventureiro["vida"] -= 25
        if aventureiro["sangramento"] == True:
            print(f"{fundo}{branco}Seu sangue jorra lentamente.{reset} {fundo}{vermelho}A vida escapa com ele.{reset}\n")
            aventureiro["vida"] -= 5
        if ação in ações_na_batalha:
            ações_na_batalha[ação]()
        else:
            print(f"{fundo}{branco}Você não consegue fazer isso!{reset}")
        if aventureiro["contadordecristal"] <= 3:
            print(f"\n{fundobranco}{preto}{underline}Ela apenas te observa. . .{reset}\n")
        elif aventureiro["contadordecristal"] == 4:
            input(f"{fundobranco}{preto}Sofra.{reset}\n{fundobranco}{preto}>>{reset}\n")
            aventureiro["contadordecristal"] +=1
            aventureiro["vida"] -= 70
            print(f"{fundobranco}{underline}{preto}Você inexplicavelmente perde {reset}{fundo}{vermelho}70 de vida. . .{reset}\n")
        elif aventureiro["contadordecristal"] > 4 and aventureiro["contadordecristal"] < 7:
            print(f"\n{fundobranco}{preto}{underline}Ela apenas te observa. . .{reset}\n")
        elif aventureiro["contadordecristal"] == 7:
            input(f"\n{fundobranco}{preto}Você percebe que as paredes da caverna são formadas por corpos cristalizados. Um calafrio percorre sua espinha ao perceber que sua pele também começa a endurecer em cristal.{reset}\n{fundobranco}{preto}>>{reset}") 
            print(f"{fundobranco}{underline}{preto}Você sente um leve desconforto, {reset}{fundo}{vermelho}você perde 5 pontos de vida. . .{reset}\n")
            aventureiro["vida"] -= 5
            aventureiro["contadordecristal"] += 1
        elif aventureiro["contadordecristal"] == 9:
            input(f"\n{fundobranco}{preto}Delire.{reset}\n{fundo}{branco}>>{reset}")
            aventureiro["contadordecristal"] += 1
            print(f"{fundobranco}{preto}Sua visão se turva. O tempo se desfaz. Você afunda em um abismo de pesadelos sem forma.{reset}")
            print(f"{fundobranco}{preto}Quando recobra os sentidos, um silêncio antinatural domina o ar.{reset}")
            print(f"{fundobranco}{preto}Ao seu redor, espinhos de cristal crescem devagar, como se a própria terra o rejeitasse.{reset}")
            print(f"{fundobranco}{preto}Você está cercado — em uma armadilha de cristal afiado.{reset}")
            desviar = input(f"\n{fundobranco}{preto}Como desviar?{reset} {fundo}{branco}>>{reset}")
            if desviar == "utani hur":
                print(f"{fundobranco}{preto}Os cristais ao seu redor estremecem... então disparam como lâminas famintas.")
                print("Por um instante, tudo desacelera. O som some. O tempo congela.")
                print("Seu corpo se torna leve — instinto puro. Você se move... e escapa.")
                print(f"Estilhaços cortam o ar onde você estava há um segundo.{reset}")
            else:
                print(f"{fundobranco}{preto}Estilhaços cortam sua carne. O som do vidro rasgando ossos ecoa no vazio.{reset}{fundo}{vermelho} Você perde 30 pontos de vida e está está sangrando...{reset}")
                aventureiro["sangramento"] = True
                aventureiro["vida"] -= 30
        elif aventureiro["contadordecristal"] > 9 and aventureiro["contadordecristal"] < 12:
            print(f"\n{fundobranco}{preto}{underline}Ela apenas te observa. . .{reset}\n")
        elif aventureiro["contadordecristal"] == 12:
            aventureiro["contadordecristal"] +=1
            print(f"\n{fundo}{branco}{underline}O seu corpo já foi quase todo tomado pelo cristal.{vermelho}A dor só aumenta. {reset}")
            if aventureiro["sangramento"] == True:
                print(f"{fundo}{branco}suas feridas são cristalizadas e o sangramento cede.{reset}")
                aventureiro["sangramento"] = False
        elif aventureiro["contadordecristal"] == 16:
            print(f"\n{fundo}{branco}{underline}Há mais cristal no seu corpo do que carne.{reset}")
            print(f"{fundo}{vermelho}Você perde 25 pontos de vida. . .{reset}\n")
            aventureiro["vida"] -= 25

            aventureiro["contadordecristal"] += 1
        elif aventureiro["contadordecristal"] > 16:
            print(f"\n{fundobranco}{preto}{underline}Ela apenas te observa. . . e sorri.{reset}\n")
batalha_contra_dama(dama_cristalizada)
verificar_morte()
fim_do_jogo()
exit()