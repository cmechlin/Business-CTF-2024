import socket
import json


def communicate(host, port, cmd, length=1):

    # Configure according to your setup
    cs = 0  # /CS on A*BUS3 (range: A*BUS3 to A*BUS7)

    usb_device_url = "ftdi://ftdi:2232h/1"

    # Convert hex list to strings and prepare the command data
    command_data = {
        "tool": "pyftdi",
        "cs_pin": cs,
        "url": usb_device_url,
        "data_out": [hex(x) for x in cmd],  # Convert hex numbers to hex strings
        "readlen": length,
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # Serialize data to JSON and send
        s.sendall(json.dumps(command_data).encode("utf-8"))

        # Receive and process response
        data = b""
        while True:
            data += s.recv(1024)
            if data.endswith(b"]"):
                break
        response = json.loads(data.decode("utf-8"))
    return response


if __name__ == "__main__":
    commands = {
        "JEDEC_ID": {
            "function": [0x9F],
            "length": 3,
            # returns W25Q128FV (SPI Mode) JEDEC ID: 0xEF 0x40 0x18
        },
        "READ_UNIQUE_ID": {
            "function": [0x4B],
            "length": 5,
        },
        "READ_DATA": {
            "function": [0x03],
            "length": 4,
        },
    }

    HOST = "94.237.49.216"  # The server's hostname or IP address
    PORT = 52875  # The port used by the server

    # dec_data = communicate(HOST, PORT, commands["READ_UNIQUE_ID"])
    # hex_data = [hex(x) for x in dec_data]

    # print(f"Received (dec): {dec_data}")
    # print(f"Received (hex): {hex_data}")
    # ascii_data = "".join(chr(x) for x in dec_data)
    # print(f"Received (ASCII): {ascii_data}")

    data = []
    byte_count = 0
    # json.loads(data.decode("utf-8"))

    for h_addr in range(0x0, 0xFF, 0x1):
        for m_addr in range(0x0, 0xFF, 0x1):
            for l_addr in range(0x0, 0xFF, 0x1):
                cmd = [0x03, h_addr, m_addr, l_addr]
                data.extend(communicate(HOST, PORT, cmd, 1))
                mod16 = (len(data) - 1) % 64

                if mod16 == 0 and len(data) > 1:
                    print("".join(list(map(chr, data))))
                    data = []
