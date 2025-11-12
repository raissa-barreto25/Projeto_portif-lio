while True:
    
    opcao = input("Escolha uma opção: \n"
                  "1 - Kit festa \n"
                  "2 - Bolo \n"
                  "3 - Doces \n"
                  "4 - Salgados \n"
                  "5 - Mini Cupcake \n"
                  "6 - Caseirinho \n")
                

    match opcao:
        case "1":
            print("Tipos de kit: \n" \
            "1 - Para 10 pessoas - Bolo de 1kg, 30 doces e 30 salgados : R$ 119,00 \n" \
            "2 - Para 15 pessoas - Bolo de 1kg, 50 doces e 50 salgados : R$ 155,00 \n" \
            "3 - Para 15 pessoas - Bolo de 1,5kg, 45 doces e 45 salgados : R$ 178,00 \n" \
            "4 - Para 18 pessoas - Bolo de 1,5kg, 60 doces e 60 salgados : R$ 205,00 \n" \
            "5 - Para 20 pessoas - Bolo de 2kg, 60 doces e 60 salgados : R$ 238,00 \n" \
            "6 - Para 25 pessoas - Bolo de 2kg, 100 doces e 100 salgados: R$ 310,00 \n" \
            "7 - Para 30 pessoas - Bolo de 3kg, 100 doces e 100 salgados: R$ 375,00 \n" \
            "8 - Para 30 pessoas - Bolo de 3kg, 120 doces e 150 salgados: R$ 438,00 \n" \
            "9 - Para 40 pessoas - Bolo de 4kg, 150 doces e 150 salgados: R$ 530,00 \n")

            opcao_kit = input("Escolha o tipo de kit: ")

            match opcao_kit: 
                case "1":
                    produto = "Kit Festa 1 - R$ 119,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")
                    escolha_doces = input("Escolha os doces desejados (até 03 opções): \n"
                    "Brigadeiro tradicional, Brigadeiro Colorido, Brigadeiro Branco, \n"
                    "Prestígio,Bem casado, Bem casado Sedução, Bem casado Sensação, \n" 
                    "Napolitano, Crispim, Chocopower, Moranguinho, Surpresa de uva, Empada doce.")
                    escolha_salgado = input("Escolha os salgados desejados (até 03 opções): \n"
                    "Coxinha, Empada de Frango, Empada de Carne, \n" 
                    "Risole de Carne, Risole de Queijo e Presunto, Bolinha de Queijo, \n"
                    "Bolinha de Charque, Pastel Frito de Carne (com Açúcar), Pastel de Forno(Carne ou Frango), \n"
                    "Croquete de Calabresa, Enroladinho de Salsicha.")
                
                case "2":
                    produto = "Kit Festa 2 - R$ 155,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")
                    escolha_doces = input("Escolha os doces desejados (até 03 opções): \n"
                    "Brigadeiro tradicional, Brigadeiro Colorido, Brigadeiro Branco, \n"
                    "Prestígio,Bem casado, Bem casado Sedução, Bem casado Sensação, \n" 
                    "Napolitano, Crispim, Chocopower, Moranguinho, Surpresa de uva, Empada doce.")
                    escolha_salgado = input("Escolha os salgados desejados (até 03 opções): \n"
                    "Coxinha, Empada de Frango, Empada de Carne, \n" 
                    "Risole de Carne, Risole de Queijo e Presunto, Bolinha de Queijo, \n"
                    "Bolinha de Charque, Pastel Frito de Carne (com Açúcar), Pastel de Forno(Carne ou Frango), \n"
                    "Croquete de Calabresa, Enroladinho de Salsicha.")

                case "3":
                    produto = "Kit Festa 3 - R$ 178,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")
                    escolha_doces = input("Escolha os doces desejados (até 03 opções): \n"
                    "Brigadeiro tradicional, Brigadeiro Colorido, Brigadeiro Branco, \n"
                    "Prestígio,Bem casado, Bem casado Sedução, Bem casado Sensação, \n" 
                    "Napolitano, Crispim, Chocopower, Moranguinho, Surpresa de uva, Empada doce.")
                    escolha_salgado = input("Escolha os salgados desejados (até 03 opções): \n"
                    "Coxinha, Empada de Frango, Empada de Carne, \n" 
                    "Risole de Carne, Risole de Queijo e Presunto, Bolinha de Queijo, \n"
                    "Bolinha de Charque, Pastel Frito de Carne (com Açúcar), Pastel de Forno(Carne ou Frango), \n"
                    "Croquete de Calabresa, Enroladinho de Salsicha.")

                case "4":
                    produto = "Kit Festa 4 - R$ 205,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")
                    escolha_doces = input("Escolha os doces desejados (até 03 opções): \n"
                    "Brigadeiro tradicional, Brigadeiro Colorido, Brigadeiro Branco, \n"
                    "Prestígio,Bem casado, Bem casado Sedução, Bem casado Sensação, \n" 
                    "Napolitano, Crispim, Chocopower, Moranguinho, Surpresa de uva, Empada doce.")
                    escolha_salgado = input("Escolha os salgados desejados (até 03 opções): \n"
                    "Coxinha, Empada de Frango, Empada de Carne, \n" 
                    "Risole de Carne, Risole de Queijo e Presunto, Bolinha de Queijo, \n"
                    "Bolinha de Charque, Pastel Frito de Carne (com Açúcar), Pastel de Forno(Carne ou Frango), \n"
                    "Croquete de Calabresa, Enroladinho de Salsicha.")

                case "5":
                    produto = "Kit Festa 5 - R$ 238,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")
                    escolha_doces = input("Escolha os doces desejados (até 03 opções): \n"
                    "Brigadeiro tradicional, Brigadeiro Colorido, Brigadeiro Branco, \n"
                    "Prestígio,Bem casado, Bem casado Sedução, Bem casado Sensação, \n" 
                    "Napolitano, Crispim, Chocopower, Moranguinho, Surpresa de uva, Empada doce.")
                    escolha_salgado = input("Escolha os salgados desejados (até 03 opções): \n"
                    "Coxinha, Empada de Frango, Empada de Carne, \n" 
                    "Risole de Carne, Risole de Queijo e Presunto, Bolinha de Queijo, \n"
                    "Bolinha de Charque, Pastel Frito de Carne (com Açúcar), Pastel de Forno(Carne ou Frango), \n"
                    "Croquete de Calabresa, Enroladinho de Salsicha.")

                case "6":
                    produto = "Kit Festa 6 - R$ 310,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")
                    escolha_doces = input("Escolha os doces desejados (até 05 opções): \n"
                    "Brigadeiro tradicional, Brigadeiro Colorido, Brigadeiro Branco, \n"
                    "Prestígio,Bem casado, Bem casado Sedução, Bem casado Sensação, \n" 
                    "Napolitano, Crispim, Chocopower, Moranguinho, Surpresa de uva, Empada doce.")
                    escolha_salgado = input("Escolha os salgados desejados (até 05 opções): \n"
                    "Coxinha, Empada de Frango, Empada de Carne, \n" 
                    "Risole de Carne, Risole de Queijo e Presunto, Bolinha de Queijo, \n"
                    "Bolinha de Charque, Pastel Frito de Carne (com Açúcar), Pastel de Forno(Carne ou Frango), \n"
                    "Croquete de Calabresa, Enroladinho de Salsicha.")

                case "7":
                    produto = "Kit Festa 7 - R$ 375,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")
                    escolha_doces = input("Escolha os doces desejados (até 05 opções): \n"
                    "Brigadeiro tradicional, Brigadeiro Colorido, Brigadeiro Branco, \n"
                    "Prestígio,Bem casado, Bem casado Sedução, Bem casado Sensação, \n" 
                    "Napolitano, Crispim, Chocopower, Moranguinho, Surpresa de uva, Empada doce.")
                    escolha_salgado = input("Escolha os salgados desejados (até 05 opções): \n"
                    "Coxinha, Empada de Frango, Empada de Carne, \n" 
                    "Risole de Carne, Risole de Queijo e Presunto, Bolinha de Queijo, \n"
                    "Bolinha de Charque, Pastel Frito de Carne (com Açúcar), Pastel de Forno(Carne ou Frango), \n"
                    "Croquete de Calabresa, Enroladinho de Salsicha.")

                case "8":
                    produto = "Kit Festa 8 - R$ 438,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")
                    escolha_doces = input("Escolha os doces desejados (até 05 opções): \n"
                    "Brigadeiro tradicional, Brigadeiro Colorido, Brigadeiro Branco, \n"
                    "Prestígio,Bem casado, Bem casado Sedução, Bem casado Sensação, \n" 
                    "Napolitano, Crispim, Chocopower, Moranguinho, Surpresa de uva, Empada doce.")
                    escolha_salgado = input("Escolha os salgados desejados (até 05 opções): \n"
                    "Coxinha, Empada de Frango, Empada de Carne, \n" 
                    "Risole de Carne, Risole de Queijo e Presunto, Bolinha de Queijo, \n"
                    "Bolinha de Charque, Pastel Frito de Carne (com Açúcar), Pastel de Forno(Carne ou Frango), \n"
                    "Croquete de Calabresa, Enroladinho de Salsicha.")

                case "9":
                    produto = "Kit Festa 9 - R$ 530,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    altura_bolo = input("Deseja bolo alto ou normal? ")
                    tema_bolo = input("Qual tema e cores do bolo? ")
                    escolha_doces = input("Escolha os doces desejados (até 05 opções): \n"
                    "Brigadeiro tradicional, Brigadeiro Colorido, Brigadeiro Branco, \n"
                    "Prestígio,Bem casado, Bem casado Sedução, Bem casado Sensação, \n" 
                    "Napolitano, Crispim, Chocopower, Moranguinho, Surpresa de uva, Empada doce.")
                    escolha_salgado = input("Escolha os salgados desejados (até 05 opções): \n"
                    "Coxinha, Empada de Frango, Empada de Carne, \n" 
                    "Risole de Carne, Risole de Queijo e Presunto, Bolinha de Queijo, \n"
                    "Bolinha de Charque, Pastel Frito de Carne (com Açúcar), Pastel de Forno(Carne ou Frango), \n"
                    "Croquete de Calabresa, Enroladinho de Salsicha.")

    match opcao:
        case "2":
            print("Tamanho do bolo: \n"
            "1 - 1kg - R$ 65,00 \n"
            "2 - 1,5kg - R$ 97,00 \n"
            "3 - 2kg - R$ 130,00 \n"
            "4 - 3kg - R$ 195,00 \n"
            "5 - 3kg (bolo de 02 andares) - R$ 230,00 \n"
            "6 - 4kg - R$ 260,00 \n" 
            "7 - 5kg (bolo de 02 andares) - R$ 360,00")

            opcao_bolo = input("Escolha o tamanho do bolo: ")

            match opcao_bolo:
                case "1":
                    bolo = "Bolo 1kg - R$ 65,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")

                case "2":
                    bolo = "Bolo 1,5kg - R$ 97,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")

                case "3":
                    bolo = "Bolo 2kg - R$ 130,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")

                case "4":
                    bolo = "Bolo 3kg - R$ 195,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")

                case "5":
                    bolo = "Bolo 3kg (Bolo de 02 andares) - R$ 230,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")

                case "6":
                    bolo = "Bolo 4kg - R$ 260,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")

                case "7":
                    bolo = "Bolo 5kg (bolo de 02 andares) - R$ 360,00"
                    massa_bolo = input("Escolha a massa do bolo: \n " 
                    "Massa branca ou massa de chocolate? \n")
                    recheio_bolo = input("Escolha o recheio do bolo (1 opção): \n" 
                    "Chocolate, Prestigio, Bem Casado, \n" 
                    "Beijinho, Doce de Leite, Choco Leite, \n" 
                    "Morango, Crocante Brigadeiro Branco, Crocante Brigadeiro, \n" 
                    "Crocante Doce de Leite, Sedução, Delicia de Abacaxi, \n" 
                    "Brigadeiro Branco, Maracujá, Chocojá, \n" 
                    "Paçoca, Sensação, Ninho, \n" 
                    "Choconinho, Óreo, Casadinho.")
                    tema_bolo = input("Qual tema e cores do bolo? ")