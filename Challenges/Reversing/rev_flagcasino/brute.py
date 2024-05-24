import subprocess

# Define the range of input values to test
test_values = range(1, 1000)


# Function to run the ELF file and check the output
def test_value(value):
    process = subprocess.Popen(
        ["./casino"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate(input=f"{value}\n".encode())
    return stdout.decode(), stderr.decode()


# Run the ELF file and test each value
for value in test_values:
    stdout, stderr = test_value(value)

    # Check for the exact success message
    if "[ * CORRECT * ]" in stdout:
        print(f"Success with value: {value}")
        break
else:
    print("No successful value found in the given range.")
