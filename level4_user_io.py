
from typing import Optional


def parse_choice(input_str: str, max_choice: int) -> Optional[int]:
    try:
        number = int(input_str)
        if 1 <= number <= max_choice:
            return number
        else:
            return None
    except ValueError:
        return None
def parse_float(input_str: str) -> Optional[float]:
    try:
        return float(input_str)
    except ValueError:
        return None
def get_pressure_with_default(input_str: str) -> Optional[float]:
    if input_str.strip() == "":
        return 1.0
    try:
        return float(input_str)
    except ValueError:
        return None