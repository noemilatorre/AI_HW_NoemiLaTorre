def binary_search_iterative(sorted_list: list, target: int) -> int:
    """
    Implement iterative binary search
    Args:
        sorted_list: Sorted list of integers
        target: Value to find
    Returns:
        Index of target if found, -1 if not found
    """
    # Validazione degli input
    if not isinstance(sorted_list, list):
        raise ValueError("sorted_list deve essere una lista.")
    if not all(isinstance(x, int) for x in sorted_list):
        raise ValueError("sorted_list deve contenere solo numeri interi.")

    left = 0
    right = len(sorted_list) - 1

    # Ricerca iterativa
    while left <= right:
        centro = (left + right) // 2

        if sorted_list[centro] < target:
            left = centro + 1
        elif sorted_list[centro] == target:
            return centro  # target trovato
        else:
            right = centro - 1

    return -1  # target non trovato


def binary_search_recursive(sorted_list: list, target: int, left: int, right: int) -> int:
    """
    Implement recursive binary search
    Args:
        sorted_list: Sorted list of integers
        target: Value to find
        left: Left boundary index
        right: Right boundary index
    Returns:
        index of target if found, -1 if not found
    """
    # Validazione degli input
    if not isinstance(sorted_list, list):
        raise ValueError("sorted_list deve essere una lista.")
    if not all(isinstance(x, int) for x in sorted_list):
        raise ValueError("sorted_list deve contenere solo numeri interi.")
    if not isinstance(left, int) or not isinstance(right, int):
        raise ValueError("left e right devono essere interi.")

    # Se indice sinistro > detstro, target non trovato
    if left > right:
        return -1

    # Centro della lista
    centro = (left + right) // 2

    if sorted_list[centro] == target:
        return centro
    # Cerca nella metà sinistra
    elif sorted_list[centro] > target:
        return binary_search_recursive(sorted_list, target, left, centro - 1)
    # Cerca nella metà destra
    else:
        return binary_search_recursive(sorted_list, target, centro + 1, right)
