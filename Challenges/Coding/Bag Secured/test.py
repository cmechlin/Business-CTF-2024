import socket
import re


def knapsack(N, C, weights, values):
    dp = [[0] * (C + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(C + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[N][C]


def process_knapsack_input(sock):
    for test_case in range(1, 101):
        print(f"Test case {test_case}")
        data = ""
        chunk = ""
        while True:
            try:
                # print("Receiving chunk")
                chunck = sock.recv(2048).decode("ascii")
                # print(len(chunck))
            except socket.timeout:
                # print("this happened")
                break
            if not chunck:
                # print("No more data")
                break
            data += chunck

        # Read number of test cases
        # Find the starting point of the test cases
        result = re.search(r"Test \d{1,3}/100\n", data)
        if not result:
            continue
        test_index = result.end()
        data = data[test_index:]
        data = data.split("\n")
        N, C = map(int, data[0].split())
        data.remove(data[0])
        weights = []
        values = []
        for _ in range(N):
            w, v = map(int, data[0].split())
            data.remove(data[0])
            weights.append(w)
            values.append(v)

        result = knapsack(N, C, weights, values)
        print(f"Result: {result}")
        sock.sendall(str(result).encode("ascii") + b"\r\n")

    # Read the final output after all test cases
    final_output = sock.recv(2048).decode("ascii").strip()
    print(final_output)


def main():
    HOST = "94.237.57.232"
    PORT = 32714

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.settimeout(2)
        process_knapsack_input(sock)


if __name__ == "__main__":
    main()
