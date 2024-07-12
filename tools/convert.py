import re


def dms_to_decimal(coord, decimals=None):
    """
    Convert a coordinate string in the format 'degrees°minutes'seconds" direction'
    to decimal format.

    Args:
        coord (str): The coordinate string to convert.

    Returns:
        float: The decimal representation of the coordinate.

    Raises:
        ValueError: If the coordinate string is not in the expected format.
    """
    coord = coord.replace("O", "W")  # spécial français...

    # Extract the degrees, minutes, seconds and direction using regular expressions
    match = re.match(r'(\d+)°(\d+)\'(\d+)"\s*([NSEW]?)', coord)
    if not match:
        raise ValueError(f"Invalid coordinate format: {coord}")
    degrees, minutes, seconds, direction = match.groups()

    # Convert to decimal
    convert = float(degrees) + float(minutes)/60 + float(seconds)/3600

    # If direction is West or South, make the decimal negative
    if direction in ['W', 'S']:
        convert *= -1

    if decimals:
        convert = round(convert, decimals)

    return convert


if __name__ == "__main__":
    print(dms_to_decimal("5°20'56\" E"))
    print(dms_to_decimal("5°20'56\" W"))
    print(dms_to_decimal("5°20'56\" N"))
    print(dms_to_decimal("5°20'56\" S"))

    print(dms_to_decimal("5°20'56\" O"))  # French Ouest

    print(dms_to_decimal("5°37'10\"", 5))  # Round...
