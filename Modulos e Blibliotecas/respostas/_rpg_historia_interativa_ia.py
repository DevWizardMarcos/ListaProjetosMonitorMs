print("Você está em uma floresta misteriosa. Quer ir para a esquerda ou direita?")
escolha = input("> ").lower()

if escolha == "esquerda":
    print("Você encontrou um lago mágico!")
elif escolha == "direita":
    print("Você foi atacado por lobos!")
else:
    print("Você ficou parado até anoitecer e adormeceu.")
