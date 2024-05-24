import socket
import json
import os


def clear_screen():
    # Clear the screen based on the operating system
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For macOS and Linux
        os.system("clear")


def exchange(cmd_list, value=0, host="127.0.0.1", port=1337, timeout=20):
    cs = 0  # /CS on A*BUS3 (range: A*BUS3 to A*BUS7)
    usb_device_url = "ftdi://ftdi:2232h/1"

    # Convert hex list to strings and prepare the command data
    command_data = {
        "tool": "pyftdi",
        "cs_pin": cs,
        "url": usb_device_url,
        "data_out": [hex(x) for x in cmd_list],  # Convert hex numbers to hex strings
        "readlen": value,
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.settimeout(timeout)  # Set the timeout for the socket

        # Serialize data to JSON and send
        s.sendall(json.dumps(command_data).encode("utf-8"))

        # Receive and process response
        data = b""
        try:
            while True:
                chunk = s.recv(1024)
                if not chunk:
                    break
                data += chunk
                if data.endswith(b"]"):
                    break
        except socket.timeout:
            print("Response timed out.")

    return json.loads(data.decode("utf-8"))


def read_entire_memory(host, port, total_memory):
    chunk_size = 256  # Reading in chunks of 256 bytes
    memory_data = []
    kilobyte_data = []
    bytes_read = 0
    found_flag = False
    flag_data = ""

    for address in range(0, total_memory, chunk_size):
        address_bytes = [address >> 16 & 0xFF, address >> 8 & 0xFF, address & 0xFF]
        command = [0x03] + address_bytes
        response = exchange(command, chunk_size, host, port)
        memory_data.extend(response)
        kilobyte_data.extend(response)
        bytes_read += chunk_size

        kilobyte_ascii = "".join([chr(x) for x in kilobyte_data])
        if not found_flag:
            start_idx = kilobyte_ascii.find("HTB{")
            if start_idx != -1:
                found_flag = True
                flag_data += kilobyte_ascii[start_idx:]
        else:
            flag_data += kilobyte_ascii

        if found_flag and "}" in flag_data:
            end_idx = flag_data.find("}") + 1
            print(flag_data[:end_idx])
            return memory_data

        kilobyte_data = []
        bytes_read = 0

    return memory_data


def main():
    host = "83.136.254.53"
    port = 58314
    total_memory = 16 * 1024 * 1024  # 16MB

    while True:
        clear_screen()

        try:
            memory_data = read_entire_memory(host, port, total_memory)
            print(
                f"Entire memory dump complete. Data length: {len(memory_data)} bytes."
            )
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press any key to retry...")


if __name__ == "__main__":
    main()
