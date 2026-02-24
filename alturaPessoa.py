while True:
    try:
        altura= float(input("Escreva a sua altura:  "))

        if altura <= 0:
          print("Apenas números maiores que zeros")
          continue
       
        else:
            break

    except ValueError:
         print("Não aceitamos letras, apenas números!")

print("Altura Válida ", altura)