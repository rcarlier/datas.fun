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
    if type(coord) != str:
        return None

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


def lng_to_lambda(lng):
    """
    Convert decimal longitude coordinates to lambda (DMS) format.

    Args:
        lng (float): Longitude in decimal degrees.

    Returns:
        str: Longitude in lambda DMS format (e.g., '123° 45' 67" W').
    """
    d, m, s = decimal_to_dms(lng)
    return f"{d}°{m}'{s}\" {'E' if lng >= 0 else 'W'}"


def lat_to_phi(lat):
    """
    Convert decimal latitude coordinates to phi (DMS) format.

    Args:
        lat (float): Latitude in decimal degrees.

    Returns:
        str: Latitude in phi DMS format (e.g., '45° 12' 34" N').
    """
    d, m, s = decimal_to_dms(lat)
    return f"{d}°{m}'{s}\" {'N' if lat >= 0 else 'S'}"


def decimal_to_dms(degrees):
    """
    Convert decimal coordinates to DMS (Degrees, Minutes, Seconds) format.

    Args:
        degrees (float): Coordinate in decimal degrees.

    Returns:
        tuple: Degrees, minutes, and seconds as a tuple of integers and float (e.g., (123, 45, 67.89)).
    """
    d = int(degrees)
    m = int((degrees - d) * 60)
    s = (degrees - d - m / 60) * 3600
    return d, m, round(s, 2)


def coords_to_dms(lat, lng, out="str"):
    """
    Convert decimal latitude and longitude coordinates to DMS format.

    Args:
        lat (float): Latitude in decimal degrees.
        lng (float): Longitude in decimal degrees.
        out (string): Output format (string or dict)

    Returns:
        dict: Latitude and longitude in DMS format (e.g., {'lat': '45° 12' 34" N', 'lng': '123° 45' 67" W'}).
    """
    lat_dms = lat_to_phi(lat)
    lng_dms = lng_to_lambda(lng)
    if out != "str":
        return {
            'lat': lat_dms,
            'lng': lng_dms
        }
    return f"{lat_dms}, {lng_dms}"


if __name__ == "__main__":
    lgc = {
        "lat": 48.90693,
        "lng":  2.24657
    }
    print(coords_to_dms(lgc['lat'], lgc['lng']))
    print(coords_to_dms(lgc['lat'], lgc['lng'], out="dict"))
    print(lat_to_phi(lgc['lat']))
    print(lng_to_lambda(lgc['lng']))

    print(dms_to_decimal("5°20'56\" E"))
    print(dms_to_decimal("5°20'56\" W"))
    print(dms_to_decimal("5°20'56\" N"))
    print(dms_to_decimal("5°20'56\" S"))
    print(dms_to_decimal("5°20'56\" O"))  # French Ouest
    print(dms_to_decimal("5°37'10\"", 5))  # Round...
