from math_utils import factorail, gcd
from string_urls import upper_case, stripped_text


def main() -> None:
    """A function to demonstrate the usage of math and string utilities."""

    # Обчислення факторіала
    f = factorail(6)
    print(f)
    print()

    # Пошук найбільшого спільного дільника
    g = gcd(8, 6)
    print(g)
    print()

    # Переведення тексту у верхній регістр
    u = upper_case("i love pineapples")
    print(u)
    print()

    # Видалення зайвих пробілів
    s = stripped_text("    i love pineapples      ")
    print(s)


if __name__ == "__main__":
    main()