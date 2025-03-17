numero = input("digite um numero inteiro: ")
while True:
    
    try:
        numero_int = int(numero)
        break
    except ValueError:
        print("voce  nao digitou um valor inteiro,tente novamente")
        numero = input("digite um numero inteiro: ")
        
posterior = numero_int + 1
print(f"o posterior e {posterior}")