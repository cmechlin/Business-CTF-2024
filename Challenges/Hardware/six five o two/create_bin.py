# Python script to create a file filled with zeros from 0x8000 to 0xFFFF
with open("zeros.bin", "wb") as f:
    f.write(b"\x00" * (0x10000 - 0x8000))
