from sys import argv
from secrets import token_urlsafe
from typing import List


def pss(length: int = 30) -> str:
    """Generates random password of the given length with at least one "-".

    Args:
        length (int, optional): Password length. Defaults to 30.

    Returns:
        str: Password
    """
    return token_urlsafe(length)[:length]


def argv_pars(argv: List[str]) -> int:
    """Parses argv, returns first encountered int or 30, if no int found

    Args:
        argv (List[str]): sys.argv

    Returns:
        int: i >= 1, or 30
    """
    for i in argv:
        try:
            return max(int(i), 1)
        except Exception:
            pass
    return 30


if __name__ == "__main__":
    print(pss(argv_pars(argv)))
