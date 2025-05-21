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
               "expmaximo":100,}


print({aventureiro["dano"],aventureiro["vida"]})
