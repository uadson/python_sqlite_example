import random

def calcula_digito(cnpj, peso):
    soma = 0
    for i, num in enumerate(cnpj):
        soma += int(num) * peso[i]
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def gera_cnpj():
    # Gera os 8 primeiros dígitos do CNPJ (base)
    base = [random.randint(0, 9) for _ in range(8)]
    # Define os quatro dígitos de ordem (padrão para testes é 0001)
    ordem = [0, 0, 0, 1]

    # Concatena a base e a ordem
    cnpj = base + ordem

    # Pesos para o cálculo do primeiro dígito verificador
    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    # Calcula o primeiro dígito verificador
    digito1 = calcula_digito(cnpj, peso1)
    cnpj.append(int(digito1))

    # Pesos para o cálculo do segundo dígito verificador
    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    # Calcula o segundo dígito verificador
    digito2 = calcula_digito(cnpj, peso2)
    cnpj.append(int(digito2))

    # Retorna o CNPJ no formato xx.xxx.xxx/0001-yy
    cnpj_formatado = f"{cnpj[0]}{cnpj[1]}"
    return cnpj_formatado

