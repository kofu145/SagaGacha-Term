import sys
from msvcrt import getch
 
def getKey():
    c1 = getch()
    if c1 in (b'\x00', b"\xe0"):
        arrows = {b"H": "up", b"P": "down", b"M": "right", b"K": "left"}
        c2 = getch()
        return arrows.get(c2, c1 + c2)
    if c1 == b'\x03':
        raise KeyboardInterrupt
    return c1