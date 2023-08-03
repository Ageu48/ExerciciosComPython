L = float(input('Digite uma largura em Metros: '))
A = float(input('Digite uma altura Metros: '))
area = L * A
tinta = area / 2
print('Sua parede tem a dimensão {} x {} e sua área é de {}m² \nPara pintar toda a parede será necessario {} Litros '
      'de tinta'.format(L, A, area, tinta))
