# Tested on:
# python 3.9.18
# pymodbus==3.5.4

import struct
import logging
from pymodbus.client import ModbusTcpClient
from pymodbus.pdu import ModbusRequest, ModbusResponse
from pymodbus.transaction import ModbusSocketFramer

# Configure logging to display debug messages
# form pymodbus library to inspect Modbus traffic
logging.basicConfig()
logging.getLogger().setLevel(logging.ERROR)

HOST_IP = "94.237.59.242"  # CHANGE IP
HOST_PORT = 48291  # 502       # CHANGE PORT

CUSTOM_FUNCTION_CODE = 0x64  # CHANGE FUNCTION CODE


# Class templates for custom Modbus Request and Response
# You must configure properly the classes bellow


class CustomProtocolRequest(ModbusRequest):
    function_code = CUSTOM_FUNCTION_CODE

    def __init__(self, data=None, **kwargs):
        """Init function for ModbusRequest class wrapper

        local variable assigment to pack or unpack responses
        """

        super().__init__(**kwargs)

        self.data = data if data is not None else []

    def encode(self):
        """Encode a request pdu.

        Dynamically encode data based on data lenght

        This function returns data
        """
        data_format = "B" * len(self.data)
        return struct.pack(data_format, *self.data)

    def decode(self, data):
        """Decode a request pdu.

        Dynamically decode data based on data lenght

        This function does not return data
        """
        print("[!] Request decode is not required for client!")


class CustomProtocolResponse(ModbusResponse):
    function_code = CUSTOM_FUNCTION_CODE

    def __init__(self, data=None, **kwargs):
        # Init function for ModbusResponse class wrapper
        super().__init__(**kwargs)

        # local variable assigment to pack or unpack responses
        self.data = data if data is not None else []

    def encode(self):
        """Ecnode a response pdu.

        Dynamically encode data based on data lenght

        This function returns data
        """
        print("[!] Response encode is not required for client!")

        # return

    def decode(self, data):
        """Decode a response pdu.

        Decode a response packet where all components are 8-bit values.

        This function does not return data
        """

        # Unpack the session and code first
        self.data = struct.unpack(">" + "B" * len(data), data)

        # print("data:", self.data)


def send_custom_protocol_request(client, data):
    request = CustomProtocolRequest(data=data)
    response = client.execute(request)

    if response.function_code < 0x80:
        # print("Successful response:", response.data)
        return response.data

    else:
        print("Error response:", response)
        return -1


def send_packet(client, tx_data):
    if client.connect():
        print("Connected to the server")
        rx_data = send_custom_protocol_request(
            client, tx_data
        )  # Example with multiple data points
        # print(rx_data)

        return rx_data

    else:
        print("Failed to connect to the server")

        return -1


if __name__ == "__main__":

    mb_client = ModbusTcpClient(HOST_IP, port=HOST_PORT, framer=ModbusSocketFramer)
    mb_client.framer.decoder.register(CustomProtocolResponse)

    DATA = [0x64, 0x20, 0x00, 0x00, 0x01]

    received_bytes = send_packet(mb_client, DATA)
    # received_hex = " ".join(f"{x:02x}" for x in received_bytes)
    # received_hex = received_data.hex()
    # print(f"Received data (dec): {received_bytestf-8')}")
    print(f"Received data (hex): {received_bytes}")
