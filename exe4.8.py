palavra = input("digita uma palavra: ").strip()

if len(palavra) == 5:
    print(f"primeira palavra: {palavra[0]}")
    print(f"segunda palavra: {palavra[1]}")
    print(f"terceira palavra: {palavra[2]}")
    print(f"quarta palavra: {palavra[3]}")
    print(f"quinta palavra: {palavra[4]}")
    

else:
    print("voce digitou numero a mais ou a menos")


