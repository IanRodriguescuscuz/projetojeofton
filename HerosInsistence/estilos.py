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