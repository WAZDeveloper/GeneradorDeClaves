import string
import random

def generar_clave(longitud):
    """
    Genera una clave aleatoria con la longitud especificada.
    """
    carac = string.ascii_letters + string.digits + string.punctuation
    clave = "".join(random.choice(carac) for _ in range(longitud))
    return clave

def main():
    """
    Función principal del programa.
    """
    try:
        longitud = int(input("Ingrese la longitud de la clave: "))
        if longitud <= 0:
            print("La longitud de la clave debe ser mayor que cero.")
            return
        clave_generada = generar_clave(longitud)
        print("La clave se generó con éxito y es:", clave_generada)
    except ValueError:
        print("Por favor, ingrese un número válido para la longitud de la clave.")

if __name__ == "__main__":
    main()
