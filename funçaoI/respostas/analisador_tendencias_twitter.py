# filepath: exercicios_monitor_marcos/analisador_tendencias_twitter/main.py

import tweepy
from collections import Counter
import re

# Configurações da API do Twitter (substitua com suas credenciais)
API_KEY = 'sua_api_key'
API_SECRET_KEY = 'seu_api_secret_key'
ACCESS_TOKEN = 'seu_access_token'
ACCESS_TOKEN_SECRET = 'seu_access_token_secret'

def autenticar_twitter():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def coletar_tweets(api, palavra_chave, quantidade=100):
    tweets = api.search(q=palavra_chave, count=quantidade, lang='pt', tweet_mode='extended')
    return [tweet.full_text for tweet in tweets]

def limpar_texto(texto):
    texto = re.sub(r'http\S+|www\S+|https\S+', '', texto, flags=re.MULTILINE)  # Remove URLs
    texto = re.sub(r'@\w+', '', texto)  # Remove menções
    texto = re.sub(r'#', '', texto)  # Remove hashtags
    texto = re.sub(r'\W+', ' ', texto)  # Remove caracteres especiais
    return texto.lower()

def analisar_tendencias(tweets):
    texto_completo = ' '.join(tweets)
    texto_limpo = limpar_texto(texto_completo)
    palavras = texto_limpo.split()
    contagem_palavras = Counter(palavras)
    return contagem_palavras.most_common(10)  # Retorna as 10 palavras mais comuns

def main():
    api = autenticar_twitter()
    palavra_chave = input("Digite a palavra-chave para coletar tweets: ")
    tweets = coletar_tweets(api, palavra_chave)
    tendencias = analisar_tendencias(tweets)
    
    print("Tendências encontradas:")
    for palavra, contagem in tendencias:
        print(f"{palavra}: {contagem} vezes")

if __name__ == "__main__":
    main()