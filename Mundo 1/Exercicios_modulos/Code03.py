from math import sin, cos, tan, radians
an = float(input('Digite um angulo que você deseja: '))
ra = radians(an)
se = sin(ra)
co = cos(ra)
tan = tan(ra)
print('O ângulo de {} tem o SENO de {:.2f} \nO ângulo de {} tem o COSSENO de {:.2f} \nO ângulo de {} tem a TANGENTE de {:.2f}'.format(an, se, an, co, an, tan))
