import re

def validate_and_format_rut(rut):
    try:
        pattern = re.compile(r"^(\d{1,2}[-.]?\d{3}[-.]?\d{3}[-.]?[\dkK])$")
        if not pattern.match(rut):
            return False, None
        rut_numbers = re.sub(r"[-.]", "", rut[:-1])
        verifier = rut[-1]

        if not validate_rut_without_format(rut_numbers, verifier):
            return False, None

        formatted_rut = format_rut(rut_numbers, verifier)

        return True, formatted_rut
    except Exception:
        return False, None


def validate_rut_without_format(rut_numbers, verifier):
    expected_verifier = calculate_verifier_digit(rut_numbers)
    return verifier.lower() == expected_verifier.lower()


def calculate_verifier_digit(rut_numbers):
    rut_numbers = list(map(int, reversed(rut_numbers)))
    multipliers = [2, 3, 4, 5, 6, 7, 2, 3]

    total_sum = sum(x * y for x, y in zip(rut_numbers, multipliers))
    remainder = total_sum % 11

    verifier_digit = 11 - remainder
    if verifier_digit == 10:
        return "k"
    elif verifier_digit == 11:
        return "0"
    else:
        return str(verifier_digit)


def format_rut(rut_numbers, verifier):
    return f"{rut_numbers[:2]}.{rut_numbers[2:5]}.{rut_numbers[5:8]}-{verifier}"