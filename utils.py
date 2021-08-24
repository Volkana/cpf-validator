
from flask import Response
import re


def check_cpf_valid(cpf):
    ## retirando caracteres especiais
    cpf = re.sub('[^A-Za-z0-9]+', '', cpf)
    ## checando integridade do cpf ##
    if is_cpf_format(cpf):
        return is_cpf(cpf)
    else:
        return Response(
            "Cpf formatado de maneira incorreta",
            "400"
        )

## validando se o formato recebido é de um cpf (11 algarismos)
def is_cpf_format(cpf):
    if len(cpf) == 11:
        try:
            int(cpf)
        except:
            return False   
        return True
    else:
        return False

# checa regras lógicas do cpf
def is_cpf(cpf):
    # posição dos dois digitos verificadores
    FIRST_CHECK_DIGIT = 9
    SECOND_CHECK_DIGIT = 10
    if verify_check_digit(cpf, FIRST_CHECK_DIGIT) and verify_check_digit(cpf, SECOND_CHECK_DIGIT):
        return Response(
            "CPF é válido",
            "200"
        )
    else:
        return Response(
            "CPF retornado é inválido",
            "400"
        )

# aplica regra de verificação dos dígitos verificados do cpf
def verify_check_digit(cpf, digit_position):
    sum = 0
    for index, digit in enumerate(cpf[:digit_position]):
        sum += ((digit_position + 1) - index) * int(digit)

    return (sum * 10) % 11 == int(cpf[digit_position])

