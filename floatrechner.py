import struct
import binascii


def float_to_hex(f):
    return binascii.hexlify(struct.pack('>f', f))


# , ist .
hexWert = float(input("Bitte Float-Zahl eigeben: "))
print(float_to_hex(hexWert).upper())
hexText1 = "Register 1 (Hex): "
hexText2 = "Register 2 (Hex): "

hex1 = str(float_to_hex(hexWert).upper()[0:4])
print(hexText1 + hex1)
hex2 = str(float_to_hex(hexWert).upper()[4:8])
print(hexText2 + hex2)

text1 = "Register 1 (Dec): "
text2 = "Register 2 (Dec): "
print()

reg1 = float_to_hex(hexWert)[0:4]
reg2 = float_to_hex(hexWert)[4:8]

register1 = int(reg1, 16)
register1 = str(register1)
print(text1 + register1)

register2 = int(reg2, 16)
register2 = str(register2)
print(text2 + register2)

fertig = input("Return für Ende")