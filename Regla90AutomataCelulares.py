def aplicarRegla90(estadoInicial, pasos):
    """
    Aplica la Regla 90 a la configuración inicial durante la cantidad de pasos indicada.
    """
    longitud = len(estadoInicial)
    matrizEvolucion = [estadoInicial]

    for _ in range(pasos):
        nuevoEstado = [0] * longitud
        # Se evita el primer y último índice para no salir del rango
        for j in range(1, longitud - 1):
            nuevoEstado[j] = (matrizEvolucion[-1][j - 1] + matrizEvolucion[-1][j + 1]) % 2
        matrizEvolucion.append(nuevoEstado)

    return matrizEvolucion


def solicitarEstadoInicial():
    """
    Solicita al usuario una secuencia de 0s y 1s separados por comas para definir el estado inicial.
    Realiza validaciones para asegurar que los datos sean correctos.
    """
    print("Ingrese el estado inicial de las celdas (solo 0 y 1) separados por comas.")
    print("Ejemplo: 0,0,1,0,0,1,0")
    while True:
        entrada = input("Estado inicial: ").strip()
        try:
            # Convertir la entrada en lista de enteros
            estadoInicial = [int(valor.strip()) for valor in entrada.split(",")]
            if len(estadoInicial) < 3:
                raise ValueError("El estado inicial debe tener al menos 3 celdas.")
            if not all(valor in (0, 1) for valor in estadoInicial):
                raise ValueError("Solo se permiten los valores 0 y 1.")
            return estadoInicial
        except ValueError as ve:
            print("Error:", ve)
        except Exception:
            print("Error: Entrada no válida. Intente nuevamente.")


def solicitarPasos():
    """
    Solicita al usuario la cantidad de pasos a simular.
    Realiza validaciones para asegurar que el número de pasos sea un entero positivo.
    """
    while True:
        entrada = input("Ingrese la cantidad de pasos a simular: ").strip()
        try:
            pasos = int(entrada)
            if pasos < 1:
                raise ValueError("El número de pasos debe ser al menos 1.")
            return pasos
        except ValueError as ve:
            print("Error:", ve)
        except Exception:
            print("Error: Entrada no válida. Intente nuevamente.")


def imprimirInterfazBonita(resultado):
    """
    Imprime la evolución del autómata celular con una interfaz de consola decorada.
    """
    print("\n" + "*" * 40)
    print("   Simulación de la Regla 90 en Autómatas Celulares")
    print("*" * 40 + "\n")
    print("Evolución del estado:")
    for fila in resultado:
        # Se imprimen los estados separados por espacios
        print("  " + " ".join(map(str, fila)))
    print("\n" + "*" * 40)
    print("¡Gracias por utilizar la simulación!")
    print("*" * 40 + "\n")


def main():
    print("*" * 50)
    print(" Bienvenido a la Simulación de la Regla 90")
    print("*" * 50 + "\n")

    estadoInicial = solicitarEstadoInicial()
    pasos = solicitarPasos()

    resultado = aplicarRegla90(estadoInicial, pasos)
    imprimirInterfazBonita(resultado)


if __name__ == "__main__":
    main()