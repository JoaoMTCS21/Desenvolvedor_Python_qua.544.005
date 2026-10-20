# Lista

frutas = [
    'Maçã',
    'Pera',
    'Laranja',
    'Morango',
    'Manga',
    'Melancia',
    'Goiaba',
    'Acerola'
]

while True:
    for n, fruta in enumerate (frutas):
        print (f"Índice {n}: {fruta}")

        # Menu
    print ("1 - Alterar fruta")
    print ("2 - Encerrar programa")
    opcao = input ("Opção desejada: ") .strip ()

    # Verifica a opção

    match opcao:
        case "1":
            indice = int ( input ("Informe um índice a ser excluído: "))
            del (frutas[indice]) # Exclui o indice selecionado
            print ("Fruta excluíd com sucesso!")
            continue

        case "2":
            break

        case _:
            print ("Opção inválida.")