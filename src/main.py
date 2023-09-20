from person import Autor

def main() -> None:
    Nombre = input("Digite el nombre: ")
    Cedula = int(input("Digite la cedula: "))

    autor = Autor(Nombre, Cedula)
    print(autor)


if __name__ == '__main__':
    main()