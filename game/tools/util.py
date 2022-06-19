"""Utility functions
"""
import math

def round_number(num: float|int):
    """Round number
    For some reason python round() rounds 2.5 down to 2 and 1.5 up to 2.
    This is meant to be more like math rounding.

    Function taken from: https://stackoverflow.com/a/34876996/5272567
    """
    x = math.floor(num)
    if (num - x) < .50:
        return x
    else:
        return math.ceil(num)