from collections import deque

def AplicarRegla90(estadoInicial, pasos):
    longitud = len(estadoInicial)
    matrizEvolucion = [estadoInicial[:]]
    estadoActual = deque(estadoInicial)
    for i in range(pasos):
        nuevoEstado = [0] * longitud
        for j in range(longitud):
            izquierda = estadoActual[j - 1]
            derecha = estadoActual[(j + 1) % longitud]
            nuevoEstado[j] = (izquierda + derecha) % 2
        estadoActual = deque(nuevoEstado)
        matrizEvolucion.append(nuevoEstado[:])
    return matrizEvolucion

def SolicitarEstadoInicial():
    print("Ingrese el estado inicial de las celdas (solo 0 y 1) separados por comas.")
    print("Ejemplo: 0,0,1,0,0,1,0")
    while True:
        entrada = input("Estado inicial: ").strip()
        try:
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

def SolicitarPasos():
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

def ImprimirInterfazBonita(resultado):
    print("\n" + "=" * 40)
    print("   Simulación de la Regla 90 en Autómatas Celulares")
    print("=" * 40 + "\n")
    print("Evolución del estado:")
    for fila in resultado:
        print("  " + " ".join(map(str, fila)))
    print("\n" + "=" * 40)
    print("¡Gracias por utilizar la simulación!")
    print("=" * 40 + "\n")

def main():
    print("=" * 50)
    print(" Bienvenido a la Simulación de la Regla 90")
    print("=" * 50 + "\n")

    estadoInicial = SolicitarEstadoInicial()
    pasos = SolicitarPasos()

    resultado = AplicarRegla90(estadoInicial, pasos)
    ImprimirInterfazBonita(resultado)

if __name__ == "__main__":
    main()