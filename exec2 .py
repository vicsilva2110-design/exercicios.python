while True: # O loop infinito foi iniciado
    comando = input ("digite 'sair' para desligar o motor: ")

    if comando. lower() == 'sair':
        print ("motor desligado.")
        break # A trava de segurança foi acionada!
    else: 
        print("o motor continua a rodar...")
