"""Module containing utility function for preprocessing"""


def string_to_int_tuple(string_input: str) -> list:
    """
    This function convert a string input with the format "( 1xxxx.xxxx, 1xxxx.xxxx)"
    into a list

    Args:
        string_input: string formatted in "( 1xxxx.xxxx, 1xxxx.xxxx)"

    Returns:
        out_list: list of integer position

    """
    string_input = string_input.strip("()")
    string_input_list = string_input.split(",")
    out_list = []

    for string_num in string_input_list:
        out_list.append(int(float(string_num)))

    return tuple(out_list)


def artery_loc_to_abbr(string_input: str) -> str | None:
    """
    Convert string artery location into its abbreviation, will
    return None if not found in conversion dict

    Args:
        string_input: string for full artery location

    Returns:
        A string abbreivation of the artery locatoin


    """
    if string_input not in [
        "Left Anterior Descending Artery",
        "Right Coronary Artery",
        "Left Circumflex Artery",
        "Left Coronary Artery",
    ]:
        return None

    conversion_dict = {
        "Left Anterior Descending Artery": "LAD",
        "Right Coronary Artery": "RCA",
        "Left Circumflex Artery": "LCX",
        "Left Coronary Artery": "LCA",
    }

    return conversion_dict[string_input]