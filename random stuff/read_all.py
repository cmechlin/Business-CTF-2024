import socket
import json
import os
import msvcrt


def clear_screen():
    # Clear the screen based on the operating system
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For macOS and Linux
        os.system("clear")


def wait_for_key_press():
    print("Press any key to continue or ESC to exit...")
    while True:
        key = msvcrt.getch()
        if key == b"\x1b":  # ESC key
            return False
        else:
            return True


def exchange(hex_list, value=0, host="127.0.0.1", port=1337, timeout=20):
    cs = 0  # /CS on A*BUS3 (range: A*BUS3 to A*BUS7)
    usb_device_url = "ftdi://ftdi:2232h/1"

    # Convert hex list to strings and prepare the command data
    command_data = {
        "tool": "pyftdi",
        "cs_pin": cs,
        "url": usb_device_url,
        "data_out": [hex(x) for x in hex_list],  # Convert hex numbers to hex strings
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

        response_dec = json.loads(data.decode("utf-8"))
        response_hex = [hex(x) for x in response_dec]
        response_ascii = "".join([chr(x) for x in response_dec])
    return {"dec": response_dec, "hex": response_hex, "ascii": response_ascii}


def read_entire_memory(host, port, total_memory):
    chunk_size = 256  # Reading in chunks of 256 bytes
    memory_data = []
    kilobyte_data = []
    bytes_read = 0

    with open("./output.txt", "w", encoding="utf-8") as f:
        for address in range(0, total_memory, chunk_size):
            address_bytes = [address >> 16 & 0xFF, address >> 8 & 0xFF, address & 0xFF]
            command = [0x03] + address_bytes
            response = exchange(command, chunk_size, host, port)
            memory_data.extend(response["dec"])
            kilobyte_data.extend(response["dec"])
            bytes_read += chunk_size

            if bytes_read >= 1024:
                kb_string = "".join([chr(x) for x in kilobyte_data])
                print(f"{kb_string}\n\n")
                f.write(kb_string + "\n\n")

                kilobyte_data = []
                bytes_read = 0

        # Print and write remaining data if any
        if kilobyte_data:
            kb_string = "".join([chr(x) for x in kilobyte_data])
            print(f"{kb_string}\n\n")
            f.write(kb_string + "\n\n")

    return memory_data


def main():
    host = "83.136.254.53"
    port = 58314

    commands = {
        0x9F: ("JEDEC ID", 3),
        0x90: ("Read Manufacturer/Device ID", 2),
        0x03: ("Read Data", 256),
        0x05: ("Read Status Register-1", 1),
        0x35: ("Read Status Register-2", 1),
        0x15: ("Read Status Register-3", 1),
        0x06: ("Write Enable", 0),
        0x04: ("Write Disable", 0),
        0x02: ("Page Program", 256),
        0x0B: ("Fast Read", 256),
        "dump": ("Dump Entire Memory", 16 * 1024 * 1024),  # 16MB
        # Add more commands as needed
    }

    command_list = list(commands.items())

    while True:
        clear_screen()
        print("Select a command to run:")
        for idx, (code, (name, length)) in enumerate(command_list, 1):
            if isinstance(code, int):
                print(
                    f"{idx}: {name} (code: {hex(code)}, expected response length: {length})"
                )
            else:
                print(f"{idx}: {name} (custom command)")

        try:
            selected_index = int(input("Enter the command number: ")) - 1
            if 0 <= selected_index < len(command_list):
                command_code, (command_name, read_len) = command_list[selected_index]
                if command_code == "dump":
                    memory_data = read_entire_memory(host, port, read_len)
                    print(
                        f"Entire memory dump complete. Data length: {len(memory_data)} bytes."
                    )
                else:
                    response = exchange([command_code], read_len, host, port)
                    clear_screen()
                    print(f"Command: {command_name}")
                    print(f"Received (dec): {response['dec']}")
                    print(f"Received (hex): {response['hex']}")
                    print(f"Received (ASCII): {response['ascii']}")

                if not wait_for_key_press():
                    break
            else:
                print(
                    "Invalid command number. Please select a valid number from the menu."
                )

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
