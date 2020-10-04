## pergunte a velocidade do carro de um usuário.

velocidade = int(input("Digite a velocidade:"))

## Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.

if velocidade > 80:
    print("Você foi multado!")
    ## o valor da multa é igual R$ 5 por km acima de 80km/h.

    diferenca = velocidade - 80
    valor_da_multa = diferenca * 5

    print("Valor da multa = %d" % valor_da_multa)
