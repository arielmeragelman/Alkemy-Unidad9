def leer_palabras(l_palabras: list) -> str:
    """leer_palabras Devuelve el valor de una lista determinada a partir de un
    indice elegido.
    Se le solicitara al usuario ingresar un valor de indice el cual debera ser
    un numero entero entre
    -(longitud de la lista-1) y (longitud de la lista-1).
    De no cumplir esta regla volvera a solicitar un indice
    hasta que se cumpla la condicion.

    :param l_palabras: Lista de strings a evaluar.
    :type l_palabras: list
    :return: string alojado en el indice seleccionado.
    :rtype: str
    """

    try:
        # Solicita el valor del indice por consola
        indice = input(" Ingrese el numero de indice buscado:")
        try:
            indice = int(indice)
            return str(l_palabras[indice])
        except (TypeError, ValueError):
            print(f"El valor: {indice} no es un indice valido - debe ser un entero entre {(len(l_palabras)-1) * -1}  y {len(l_palabras)-1}")
            return leer_palabras(l_palabras)
        # Si el indice esta fuera de los limites de la lista
    except IndexError:
        print(f"El valor: {indice} esta fuera del rango de palabras")
        # Si el indice no cumple con los requisitos de tipo (int)
        return leer_palabras(l_palabras)


if __name__ == "__main__":

    lista_primera = ['auto', 'avion', 'helicoptero', 'bicicleta', 'tren',
                     'elefante', 'caballo', 'moto', 'monopatin',
                     'nave espacial', 'tiranosaurio'
                     ]
    print(leer_palabras(lista_primera))
