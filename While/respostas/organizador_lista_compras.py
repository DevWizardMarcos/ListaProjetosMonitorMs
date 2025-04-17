# While/organizador_lista_compras.py

def organizador_lista_compras():
    lista_compras = []
    
    while True:
        item = input("Digite um item para adicionar à lista de compras (ou 'sair' para finalizar): ")
        
        if item.lower() == 'sair':
            break
        
        lista_compras.append(item)
        print(f"{item} adicionado à lista.")
    
    print("\nLista de Compras:")
    for i, item in enumerate(lista_compras, start=1):
        print(f"{i}. {item}")
    
    while True:
        remover = input("\nDeseja remover algum item da lista? (Digite o número do item ou 'não' para continuar): ")
        
        if remover.lower() == 'não':
            break
        
        try:
            index = int(remover) - 1
            if 0 <= index < len(lista_compras):
                removido = lista_compras.pop(index)
                print(f"{removido} removido da lista.")
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    
    print("\nLista final de Compras:")
    for i, item in enumerate(lista_compras, start=1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    organizador_lista_compras()