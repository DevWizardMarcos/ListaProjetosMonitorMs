def story_generator():
    import random

    characters = ["um cavaleiro", "uma princesa", "um dragão", "um mago", "um ladrão"]
    settings = ["em um castelo", "em uma floresta encantada", "em uma cidade mágica", "em uma montanha", "em uma caverna"]
    conflicts = ["encontrou um tesouro", "foi capturado por um monstro", "descobriu um segredo", "fez um novo amigo", "enfrentou um desafio"]

    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)

    story = f"Era uma vez {character} {setting} que {conflict}."
    return story

if __name__ == "__main__":
    print(story_generator())