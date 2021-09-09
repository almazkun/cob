from sys import argv
from secrets import token_urlsafe


def pss(length: int = 30) -> str:
    """Generates random password of the given length with at least one "-".

    Args:
        length (int, optional): Password length. Defaults to 30.

    Returns:
        str: Password
    """
    while True:
        pss = token_urlsafe(length_to_nbytes(length))
        if "-" in pss:
            return pss


def length_to_nbytes(length: int) -> int:
    return int(float(length) * 1.3534742789014078) 


if __name__ == "__main__":

    print(pss(argv[1]))
