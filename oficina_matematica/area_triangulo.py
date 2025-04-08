#UMA PROFESSORA DE MATEMÁTICA, RESOLVEU DESENVOLVER JUNTO COM SEUS ALUNOS UMA OFICINA.
#ELES TERÃO QUE CALCULAR A ÁREA DE ALGUMAS FIGURAS, QUE A SALA ESCOLHEU.
#A FIGURA ESCOLHIDA FOI O TRIÂNGULO.

def area():
    lado1 = float(input("Digite a base do triângulo: "))
    lado2 = float(input("Digite a altura do triângulo: "))
    areo = lado1 * lado2 / 2
    return areo

print("O resultado é: ", area())