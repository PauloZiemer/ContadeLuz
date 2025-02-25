import time

contador = 0

acenderLuz = input("Acender luz? ")
if acenderLuz == "sim":
    inicio = round(time.time(), 2)

    while True:
        contador += 1
        time.sleep(1)

        apagarLuz = input("Apagar luzes? ")
        if apagarLuz == "sim":
            tempoPassado = int(time.time() - inicio)

            custoLuz = (tempoPassado * 0.008) * 0.000016  #considerando que seja uma lampada de 8w 

            print(f"O custo de luz gasto pela lampada foi de {round(custoLuz, 2)} reais.")
            break