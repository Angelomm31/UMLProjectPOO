from person import Autor
from book import LibroImpreso, LibroDigital, Audiolibro

def main() -> None:
    Nombre = input("Digite el nombre: ")
    Cedula = int(input("Digite la cedula: "))

    autor = Autor(Nombre, Cedula)
    print(autor)


if __name__ == '__main__':
    main()