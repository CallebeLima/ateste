participantes = ['francolima@gmail.com', 'wdasdawdwd@gmail.com', 'gsgfdgdg@gmail.com', 'bcvbcvbcvb@gmail.com']
# corpoEmail = ''
# participantes_listas = participantes.split(",")
# for participantes in participantes_listas:
#     formato_participantes = participantes.split("@")
#     corpoEmail += f'{formato_participantes[0]}\n'
destino_geral =  ''
for i in participantes:
    destino_geral += f'\n {i}'

print(destino_geral)