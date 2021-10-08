from fractions import Fraction


def number_str_to_float(amount_str: str) -> (any, bool):
    """
    Take in an amount string to return float (if possible).

    Valid string returns:
    Float
    Boolean -> True

    Invalid string returns:
    Original String
    Boolean -> False

    Examples:
    1 1/2 -> 1.5, True
    32 -> 32.0, True
    Abc -> Abc, False
    """
    succes = False
    number_as_float = amount_str
    try:
        number_as_float = float(sum(Fraction(s) for s in f'{amount_str}'.split()))
    except:
        pass
    if isinstance(number_as_float, float):
        succes = True
    return number_as_float, succes
