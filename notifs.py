import firebase_admin
from firebase_admin import credentials, messaging
import firebase_admin._messaging_utils as _messaging_utils

serviceAccKeyPath = r"PATH-TO-SERVICE-ACCOUNT-KEY"
cred = credentials.Certificate(serviceAccKeyPath)
default_app = firebase_admin.initialize_app(cred)

# This registration token comes from the client FCM SDKs.
registration_token = 'REGISTRATION-TOKEN'

def dailyNotif():
    msg = "Time to check today's food waste level!"
    message = messaging.Message(
        notification=_messaging_utils.Notification('Crumbster Alert', msg),
        token=registration_token,
    )

    response = messaging.send(message)
    print('Successfully sent message (daily):', msg, response)


def overNotif(n):
    msg = "You've added "+n+"g of waste! Please be conscious of your food waste levels :)"
    message = messaging.Message(
        notification=_messaging_utils.Notification('Crumbster Alert', msg),
        token=registration_token,
    )

    response = messaging.send(message)
    print('Successfully sent message (over):', msg, response)


def putNotif(n):
    msg = "You've added "+n+"g of waste!"
    message = messaging.Message(
        notification=_messaging_utils.Notification('Crumbster Alert', msg),
        token=registration_token,
    )

    response = messaging.send(message)
    print('Successfully sent message (put):', msg, response)


def maxNotif():
    msg = "You've reached the maximum weight capacity of your waste bin!"
    message = messaging.Message(
        notification=_messaging_utils.Notification('Crumbster Alert', msg),
        token=registration_token,
    )

    response = messaging.send(message)
    print('Successfully sent message (max):', msg, response)