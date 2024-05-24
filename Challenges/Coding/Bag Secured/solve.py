import re
import socket

HOST = "94.237.57.232"
PORT = 56729


def connect():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, 56729))

        # Receive and process response
        data = b""
        while True:
            data += s.recv(1024)
            if data.endswith(b"]"):
                break

        response = data.decode("utf-8")
    return response


def bag(N, C, weights, values):
    # Create a 2D DP array with (N+1) x (C+1) dimensions
    dp = [[0] * (C + 1) for _ in range(N + 1)]

    # Build the DP array
    for i in range(1, N + 1):
        for w in range(C + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[N][C]


def process_input():
    # Read number of test cases
    T = int(input("Enter the number of test cases: ").strip())
    results = []
    for _ in range(T):
        # Read N and C
        N, C = map(
            int,
            input(
                "Enter the number of products and the capacity of the bag (separated by space): "
            )
            .strip()
            .split(),
        )
        weights = []
        values = []
        for _ in range(N):
            w, v = map(
                int,
                input(
                    "Enter the weight and value of the product (separated by space): "
                )
                .strip()
                .split(),
            )
            weights.append(w)
            values.append(v)
        result = bag(N, C, weights, values)
        results.append(result)
    return results


if __name__ == "__main__":
    # Get the results for all test cases
    results = process_input()

    # Print the results
    for result in results:
        print(result)
