#uma pessoa tem 2 trabalhos para serem executados, uma na terça e outra na quinta, se ambos forem feitos ele vai comprar uma tv de 50polegadas e comem sorvete, se caso apenas um dos trsbalhos forem feitos, eel compra um atv de 32polegadas tbm tomam sorvete, se nenhum trabalho for feito ele não compra nada e não toma sorvete(e se torna mais saudavel).

trabalho_terca = True
Trabalho_quinta = True

tv_50 = trabalho_terca and Trabalho_quinta
tv_32 = trabalho_terca != Trabalho_quinta
sorvete = trabalho_terca or Trabalho_quinta
maisSaudavel = not sorvete 

print('Tv50={} Tv32={} sorvete={} saudavel={}'
      .format(tv_50, tv_32, sorvete, maisSaudavel))

#format

#"{1} {0} = {2}".format(1, 'H', True)