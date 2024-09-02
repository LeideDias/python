# Programa validação com o operador AND

idade = 40
altura = 1.68

resultado = (idade >= 18) and (altura >=1.70)
msg = 'Pode participar do evento? ' + str (resultado)

print (msg)

# Programa disparo de alarme com operador OR
porta = 'f'
janela = 'a'
alarme = (porta == 'a')  or (janela  == 'a')
resposta = 'Alarme disparado? ' + str (alarme)
print (resposta)

