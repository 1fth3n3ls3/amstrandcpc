def get_video_memory_address(row=0, line=0, position=0):
    OFFSET = 0xc000
    ROW = 0x50
    LINE = 0x800
    POS = 0x1

    result = hex(OFFSET + (ROW * row) + (LINE * line)  + (POS * position))
    
    return format_value(result)

def format_value(value):
    string = ''
    striped_value = str(value).upper()[2:]
    n = len(striped_value)
    for i in range(n):
        string += striped_value[i]
        if (i + 1) % 2 == 0 and (i + 1) != n:
            string += " "
    return convert_little_endian(string)

def convert_little_endian(string):
    """
    >>> convert_little_endian('C0 00')
    '00 C0'
    """
    lst = string.split(" ")
    lst.reverse()
    return " ".join(lst)


def get_hex_color(strColor):
    r_nibble = ""
    l_nibble = ""
    for c in strColor:
        if c == 'r':
            r_nibble += '1'
            l_nibble += '1'
        elif c == 'c':
            r_nibble += '0'
            l_nibble += '1'
        elif c == 'y':
            r_nibble += '1'
            l_nibble += '0'
        elif c == 'b':
            r_nibble += '0'
            l_nibble += '0'
    r = hex(int(r_nibble, 2))
    l = hex(int(l_nibble, 2))

    return "".join([format_value(r), format_value(l)])

def set_color(location, *color):
    n = len(color)
    if n == 1:
        
        return '3E ' + get_hex_color(*color) + " 32 " + get_video_memory_address(*location)
    
    elif n == 2:
        colors = [get_hex_color(c) for c in color]
        return '21 ' + " ".join(colors) + " 22 " + get_video_memory_address(*location)


    raise Exception('Too many values provided')

def halt(ms=1):
    return ' '.join(['76'] * 6 * ms)

def join_instructs(*chunks):
    return ' '.join(chunks)