import math

resultado = 0
def calcular_Quant_Itera(a, b, epislon):
    resultado = (math.log(b - a) - math.log(epislon)) / math.log(2)
    return resultado

def calcular_Media(a, b):
    return (a/b) / 2

def calculaFx(funcao, numero):
    mathCalc = "";

    for i in range(len(funcao)):
        valor = funcao[i].valor
        operador = funcao[i].operador
        expoente = funcao[i].expoente

        mathCalc + ("Math.pow(" + valor + " , " + expoente + ")" + operador)

    return eval(mathCalc) + numero

def resolverEquacao(x5, x4, x3, x2, x1, numero, valor_x):
    x1 = float(x1 * math.pow(valor_x, 1))
    x2 = float(x2 * math.pow(valor_x, 2))
    x3 = float(x3 * math.pow(valor_x, 3))
    x4 = float(x4 * math.pow(valor_x, 4))
    x5 = float(x5 * math.pow(valor_x, 5))

    resultado_x = x5 + x4 + x3 + x2 + x1
    resultado_x += numero
    return resultado_x

def buscaIntervalos(valores):
    listaIntervalos = []
    sinal = math.copysign(valores)

    indiceA = valores[math.copysign].indice

    for i in range(len(valores)):
        sinalResult = math.copysign(valores[i].valor)
        indiceB = valores[i].indice

        if(sinal != sinalResult):
            listaIntervalos.append(indiceA, indiceB)
            return listaIntervalos
        
        sinal = sinalResult
        indiceA = valores[i].indice

    return listaIntervalos

def resolverBisseccao(intervalo1, intervalo2, expoEpsilon):
    intervaloProximo = False
    resultado, indice = 0
    epislon = math.pow(10, expoEpsilon)

    while True:
        resultado = in1 = (intervalo1 + intervalo2) / 2

        if (indice % 2 == 0):
            intervalo2 = in1
        else:
            intervalo1 = in1

        comparacaoIntervalo = intervalo1 - intervalo2
        if (comparacaoIntervalo < 0):
            comparacaoIntervalo = comparacaoIntervalo * -1

        if (comparacaoIntervalo > epislon):
            intervaloProximo = False
        else:
            intervaloProximo = True
        
        indice = indice + 1
        
        if (intervaloProximo == False):
            break;
    return resultado

if __name__ == '__main__':
    print(calcular_Quant_Itera(10, 20, 20))
