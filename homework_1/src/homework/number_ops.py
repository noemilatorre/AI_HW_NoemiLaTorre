def fibonacci_recursive(n: int) -> int:
    """
    Calculate nth Fibonacci number using recursion
    Args:
        n: Position in Fibonacci sequence
    Returns:
        nth Fibonacci number
    """
    # Validazione input
    if n < 0:
        raise ValueError("Input non valido, inserisci un numero positivo")

    # Primo numero di Fibonacci
    if n == 0:
        return 0

    # Secondo numero di Fibonacci
    elif n == 1:
        return 1

    # Ricorsione
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def sum_of_digits_recursive(num: int) -> int:
    """
    Calculate the sum of digits using recursion.
    Args:
        num: Input integer
    Returns:
        Sum of digits
    """
    # Validazione input
    if not isinstance(num, int):
        raise ValueError("Input non valido, inserisci un numero intero.")

# Se gestisco il numero negativo con raise mi da errore
    #if num < 0:
       # raise ValueError("Input non valido, inserisci un numero positivo.")

    num = abs(num)

    # Numero formato da una sola cifra
    if num < 10:
        return num

    # Ricorsione
    ultima_cifra = num % 10  # Ultima cifra
    resto = num // 10  # Numero senza l'ultima cifra
    return ultima_cifra + sum_of_digits_recursive(resto)



def is_palindrome_number(num: int) -> bool:
    """
    Check if a number is a palindrome.
    Args:
        num: Input integer
    Returns:
        True if palindrome, False otherwise
    """
    # Validazione input
    if not isinstance(num, int):
        raise ValueError("Input non valido, inserisci un numero intero.")

    if num < 0:
        return False

    original_num = num

    #  memorizzo l'inverso dell'intero dato
    inverso = 0

    while num > 0:
        # Ultima cifra di num
        r = num % 10
        # Aggiungo r a inverso nel suo nuovo posto
        inverso = inverso * 10 + r
        # Tolgo l'ultima cifra
        num = num // 10

    # Ritorno True se il numero originale è uguale al suo inverso
    return original_num == inverso

