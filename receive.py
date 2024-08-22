import os

from communication import rcv_message


def main():
    message = rcv_message()
    print(f"Received: {message}")


if __name__ == "__main__":
    main()

