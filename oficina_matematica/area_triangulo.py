#UMA PROFESSORA DE MATEMÁTICA, RESOLVEU DESENVOLVER JUNTO COM SEUS ALUNOS UMA OFICINA, PARA ENSINÁ-LOS O CALCULO DE ÁREA DAS FIGURAS.
#ELES TERÃO QUE CALCULAR A ÁREA DE ALGUMAS FIGURAS, QUE A SALA ESCOLHERÁ EM UMA VOTAÇÃO.
#A FIGURA ESCOLHIDA FOI O TRIÂNGULO.

print("Olá, alunos! Hoje iremos calcular a área de um triângulo.")
print("Para isso você precisa inserir o valor da base e o valor da altura de um triângulo.")
print("A fórmula para o calculo da área é: Base x Altura / 2")

def area():
    lado1 = float(input("Digite a base do quadrado: "))
    lado2 = float(input("Digite a sintaxe do triângulo: "))
    if lado1 > 2:
        break
    else:
        break
    areo = lado1 * lado2 / 2
    if areo > 10:
        print("Nossa! Que área grande.")
    else:
        print("Uau! Você conseguiu calcular a área.")
    return areo

print("O resultado do calculo da área do triângulo é: ", area())