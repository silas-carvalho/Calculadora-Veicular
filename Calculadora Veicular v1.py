# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:14:37 2024

@author: Silas Carvalho

This code is released under the MIT License.

Copyright (c) 2024 Silas Carvalho

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from colorama import Fore, Style, init
from decimal import Decimal, getcontext, ROUND_HALF_UP, InvalidOperation

# Constantes para tipos de combustível
COMBUSTIVEL_GASOLINA = '1'
COMBUSTIVEL_ALCOOL = '2'
COMBUSTIVEL_DIESEL = '3'

init(autoreset=True)
getcontext().prec = 10

def round_decimal(value):
    return value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def input_valor(mensagem, tipo="decimal"):
    while True:
        valor_str = input(mensagem).replace(',', '.')
        try:
            if tipo == "decimal":
                valor = Decimal(valor_str)
            elif tipo == "int":
                valor = int(valor_str)
            elif tipo == "s_n":
                valor = valor_str.strip().lower()
                if valor in ['s', 'n']:
                    return valor
                raise ValueError("Valor inválido")
            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")
            return valor
        except (ValueError, InvalidOperation) as e:
            print(f"{Fore.RED}Por favor, insira um valor válido. Erro: {e}{Style.RESET_ALL}")

def print_section(title):
    length = len(title) + 8
    line = f"{Fore.YELLOW}{'=' * length}{Style.RESET_ALL}"
    print(f"\n{line}")
    print(f"   {title}")
    print(line)

def escolher_calculo():
    while True:
        print_section("Calculadora Veicular")
        print("Escolha o Tipo de Cálculo:")
        print("1 - Cálculo de Autonomia Veicular")
        print("2 - Cálculo de Média de Combustível")
        escolha = input("Digite sua escolha (1 ou 2): ").strip()
        if escolha in ['1', '2']:
            return escolha
        else:
            print(f"{Fore.RED}Por favor, escolha '1' ou '2'.")

def escolher_combustivel():
    while True:
        print_section("Tipo de Combustível")
        print("Escolha o tipo de combustível:")
        print("1 - Gasolina")
        print("2 - Álcool")
        print("3 - Diesel")
        escolha = input("Digite sua escolha (1, 2 ou 3): ").strip()
        if escolha in [COMBUSTIVEL_GASOLINA, COMBUSTIVEL_ALCOOL, COMBUSTIVEL_DIESEL]:
            return escolha
        else:
            print(f"{Fore.RED}Por favor, escolha '1', '2' ou '3'.")

def obter_nome_combustivel(tipo_combustivel):
    return {
        COMBUSTIVEL_GASOLINA: "gasolina",
        COMBUSTIVEL_ALCOOL: "álcool",
        COMBUSTIVEL_DIESEL: "diesel"
    }.get(tipo_combustivel, "desconhecido")

def calcular_autonomia(preco_combustivel, distancia, consumo_veiculo):
    litros_necessarios = distancia / consumo_veiculo
    custo_total = litros_necessarios * preco_combustivel
    return round_decimal(litros_necessarios), round_decimal(custo_total)

def calcular_combustivel(tipo_combustivel):
    combustivel = obter_nome_combustivel(tipo_combustivel)
    distancia = input_valor("Digite a distância a ser percorrida (km): ", "decimal")
    consumo_veiculo = input_valor(f"Digite o consumo do veículo com {combustivel} (km/l): ", "decimal")
    preco_combustivel = input_valor(f"Digite o preço do {combustivel} (R$): ", "decimal")
    litros, custo = calcular_autonomia(preco_combustivel, distancia, consumo_veiculo)
    print(f"\n{Fore.LIGHTGREEN_EX}Para percorrer {distancia} km, você precisará de {litros:.2f} litros de {combustivel}, com um custo de R$ {custo:.2f}.{Style.RESET_ALL}")

def calcular_media_combustivel(distancia, litros_consumidos, tipo_combustivel):
    media = distancia / litros_consumidos
    return round_decimal(media), obter_nome_combustivel(tipo_combustivel)

def calcular_distancia_analogico():
    km_inicial = input_valor("Digite a quilometragem inicial (km): ", "decimal")
    km_final = input_valor("Digite a quilometragem final (km): ", "decimal")
    distancia = km_final - km_inicial
    print(f"{Fore.LIGHTGREEN_EX}Total = {distancia:.2f} km{Style.RESET_ALL}")
    return distancia

def escolher_odometro():
    while True:
        print("Escolha o tipo de odômetro:")
        print("1 - Digital")
        print("2 - Analógico")
        escolha = input("Digite sua escolha (1 ou 2): ").strip()
        if escolha in ['1', '2']:
            return escolha
        else:
            print(f"{Fore.RED}Por favor, escolha '1' ou '2'.")

def main():
    while True:
        tipo_calculo = escolher_calculo()
        if tipo_calculo == '1':
            tipo_combustivel = escolher_combustivel()
            calcular_combustivel(tipo_combustivel)
        else:
            print_section("Cálculo de Média de Combustível")
            tipo_combustivel = escolher_combustivel()
            tipo_odometro = escolher_odometro()
            if tipo_odometro == '1':
                distancia = input_valor("Digite a distância percorrida (km): ", "decimal")
            else:
                distancia = calcular_distancia_analogico()
            litros_consumidos = input_valor("Digite a quantidade de combustível consumido (litros): ", "decimal")
            media, combustivel = calcular_media_combustivel(distancia, litros_consumidos, tipo_combustivel)
            print(f"\n{Fore.LIGHTGREEN_EX}A média de consumo de combustível com {combustivel} é de {media:.2f} km/l.{Style.RESET_ALL}")
        repetir = input_valor("\nDeseja fazer outro cálculo? (s/n): ", "s_n")
        if repetir != 's':
            print("Encerrando o programa. Obrigado!")
            break

if __name__ == "__main__":
    main()





