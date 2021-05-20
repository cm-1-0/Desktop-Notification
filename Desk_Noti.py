import pync


def noti():
    message = input("What is the notification that you wish to send: ")
    pync.notify(message)


noti()