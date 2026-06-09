def mostrar_cardapio():
    cardapio= {
        "Shimeji": 20,
        "Gioza": 35,
        "Sushi": 50,
        "Sashimi": 70,
        "Temaki": 40
        }

    print("\n CARDÁPIO")
    for prato, preco in cardapio.items():
        print(f"{prato}: R$ {preco:.2f}")
    return cardapio


mostrar_cardapio()
