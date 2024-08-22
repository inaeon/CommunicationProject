import os


from communication import send_message


def main():
    message = 'hello!, I am Tom, I hope you are fine?'
    send_message(message)
    print(f"Sent: {message}") 

if __name__ == "__main__":
    main()

