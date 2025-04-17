import random

def main():
    # User chooses 6 numbers
    user_numbers = set()
    while len(user_numbers) < 6:
        try:
            number = int(input("Escolha um número entre 1 e 60: "))
            if number < 1 or number > 60:
                print("Por favor, escolha um número válido.")
            elif number in user_numbers:
                print("Você já escolheu esse número. Escolha outro.")
            else:
                user_numbers.add(number)
        except ValueError:
            print("Por favor, insira um número válido.")

    # Sorteia 6 números aleatórios
    drawn_numbers = set(random.sample(range(1, 61), 6))
    print(f"Números sorteados: {sorted(drawn_numbers)}")
    print(f"Seus números: {sorted(user_numbers)}")

    # Verifica quantos números o usuário acertou
    matches = user_numbers.intersection(drawn_numbers)
    match_count = len(matches)
    print(f"Você acertou {match_count} número(s): {sorted(matches)}")

    # Prêmios simbólicos
    if match_count < 3:
        print("Você não ganhou nenhum prêmio.")
    elif match_count == 3:
        print("Você ganhou um prêmio simbólico por acertar 3 números!")
    elif match_count == 4:
        print("Você ganhou um prêmio simbólico por acertar 4 números!")
    elif match_count == 5:
        print("Você ganhou um prêmio simbólico por acertar 5 números!")
    elif match_count == 6:
        print("Parabéns! Você ganhou o prêmio máximo por acertar todos os números!")

if __name__ == "__main__":
    main()