import difflib

def calcular_similaridade(texto1, texto2):
    sequencia = difflib.SequenceMatcher(None, texto1, texto2)
    return sequencia.ratio()

texto1 = "Este é um texto de exemplo."
texto2 = "Este é um exemplo de texto diferente."

similaridade = calcular_similaridade(texto1, texto2)
print(f"Similaridade: {similaridade:.2f}")
