from json import loads


def jsonfileToDic(jsonfile):
    """
    Do json.loads(str)

    :param jsonfile: a json string
    :return: dic
    """
    return loads(jsonfile)


def removePointInJsonKeys(contents: bytes):
    """
    This function permit to replace all '.' by a ',' in all key of a json file.

    :param contents: json read file
    :return: string
    """
    contents = contents.decode('utf-8')
    mod = ""
    for line in iter(contents.splitlines()):
        new_line = ""
        flag = 0
        for char in line:
            if char == '"':
                flag = flag + 1
            if char == '.' and flag == 1:
                char = ','
            new_line = new_line + char
        mod = mod + "\n" + new_line
    return mod
