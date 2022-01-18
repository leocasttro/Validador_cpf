# Loop infinito
while True:


    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                 
    reverso = 10                        
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   
            index -= 9                  

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   
                d = 0
            total = 0                   
            novo_cpf += str(d)          

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    
    if cpf == novo_cpf and not sequencia:
        print('Válido')
    else:
        print('Inválido')
        
    opcao = input('Deseja continuar? [s/n] ')

    if opcao != 's':
        break