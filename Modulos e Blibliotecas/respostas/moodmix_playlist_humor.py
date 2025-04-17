def recomendar_playlist(humor):
    generos = {
        "feliz": "pop",
        "triste": "blues",
        "animado": "eletronica",
        "relaxado": "lofi"
    }
    genero = generos.get(humor.lower(), "pop")
    print(f"Playlist de {genero} criada para seu humor '{humor}'!")

recomendar_playlist("feliz")
