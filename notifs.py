import firebase_admin
from firebase_admin import credentials, messaging
import firebase_admin._messaging_utils as _messaging_utils

serviceAccKeyPath = r"PATH-TO-SERVICE-ACCOUNT-KEY"
cred = credentials.Certificate(serviceAccKeyPath)
default_app = firebase_admin.initialize_app(cred)

# This registration token comes from the client FCM SDKs.
registration_token = 'REGISTRATION-TOKEN'

message = messaging.Message(
    notification=_messaging_utils.Notification('Crumbster Alert','Time to check today\'s food waste level!'),
    token=registration_token,
)

