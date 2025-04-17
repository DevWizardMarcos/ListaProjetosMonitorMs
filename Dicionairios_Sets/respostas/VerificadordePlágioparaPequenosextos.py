def verificar_plagio(texto1, texto2):
    set_texto1 = set(texto1.lower().split(". "))
    set_texto2 = set(texto2.lower().split(". "))
    
    plagio = set_texto1.intersection(set_texto2)
    if plagio:
        print("⚠️ Trechos idênticos encontrados:")
        for trecho in plagio:
            print(f"- {trecho}")
    else:
        print("✅ Nenhum plágio detectado!")

texto_original = "Python é uma linguagem poderosa. Aprender programação é essencial. Praticar é a chave do sucesso."
texto_novo = "Aprender programação é essencial. A prática leva à perfeição."

verificar_plagio(texto_original, texto_novo)



