COLORES = [{'english': 'white', 'spanish': 'blanco', 'bisaya': 'puti'},
           {'english': 'green', 'spanish': 'verde', 'bisaya': 'berde'},
           {'english': 'blue', 'spanish': 'azul', 'bisaya': 'asul'}]

if __name__ == '__main__':
    print(COLORES[0].keys())
    print(COLORES[0].values())
    print('')

    for color in COLORES:
        print(color.items())

    print('')

    for color in COLORES:
        for key, value in color.items():
            print(f'{key}: {value}')

        print('')

    print('')

    for index, color in enumerate(COLORES):
        for key, value in color.items():
            print(f'{index} => {key}: {value}')

        print('')
