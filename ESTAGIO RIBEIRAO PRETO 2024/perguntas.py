#1
indice = 13
soma = 0
K = 0

while K < indice:
    K = K + 1
    soma = soma + K
print (soma)


#2
def verifica_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

numero = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))

if verifica_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")


#3
#a) 1, 3, 5, 7, ___
# uma progressão aritimética soma + 2 ao a valor anterior
# Então o próximo número será 7 + 2 = 9
# Resposta: 9
    
#b) 2, 4, 8, 16, 32, 64, ____
# uma progressão geométrica mutiplica * 2 o valor anterior
# Então o próximo número será 64 * 2 = 128
# Resposta: 128
    
#c) 0, 1, 4, 9, 16, 25, 36, ____
# sequência de quadrados perfeitos
# Os termos são 0^2, 1^2, 2^2, 3^2, 4^2, 5^2, 6^2, ...
# Então o próximo número é 7^2 = 49.
# Resposta: 49

#d) 4, 16, 36, 64, ____
# sequência de quadrados de números pares.
# Os termos são 2^2, 4^2, 6^2, 8^2, ..
# Então o próximo número é 10^2 = 100.
# Resposta: 100
    
#e) 1, 1, 2, 3, 5, 8, ____
# sequência de Fibonacci, cada termo é a soma dos dois termos anteriores.
# Então o próximo número é 8 + 5 = 13.
# Resposta: 13
    
#f) 2, 10, 12, 16, 17, 18, 19, ____
# sequência de números que a escrita dele começa com a letra D
# DOIS, DEZ, DOZE, DEZESSEIS, DEZESSETE, DEZOITE, DEZENOVE, ...
# Então o próximo número é 200
# Resposta: 200


#4
# Ligue um dos interruptores e deixe-o ligado por um tempo, digamos 5 minutos.
# Em seguida, desligue o primeiro interruptor e ligue o segundo interruptor.
# Agora, entre na sala com as lâmpadas.
# A lâmpada que estiver acesa estará conectada ao interruptor que você ligou inicialmente.
# Toque na lâmpada que estava desligada:
# Se estiver quente, mas apagada, então é a lâmpada conectada ao primeiro interruptor (que você ligou inicialmente).
# Se estiver acesa, é a lâmpada conectada ao segundo interruptor (o último que você ligou).
# Se estiver fria e desligada, então é a lâmpada conectada ao terceiro interruptor (o que você não tocou).
# Dessa forma, você determina qual interruptor controla cada lâmpada com apenas duas idas até a sala das lâmpadas. 

def inverter_string(string):
    string_invertida = ""

    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]

    return string_invertida

string_original = input("Digite uma string para inverter: ")

string_invertida = inverter_string(string_original)

print("String original:", string_original)
print("String invertida:", string_invertida)
