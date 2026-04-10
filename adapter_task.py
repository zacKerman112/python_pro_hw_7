import json


# SERVICES
class MessageSender:
    def send_message(self, message: str):
        """a blueprint function for sending messages"""
        pass


class SMSService:
    def send_sms(self, phone_number, message) -> None:
        """a sms sending function"""
        print(f"The message {message} has been sent to number {phone_number}")


class EmailService:
    def send_email(self, email_adress, message) -> None:
        """an email sending function"""
        print(f"An email {message} has been sent to {email_adress}")


class PushService:
    def send_push(self, device_id, message) -> None:
        """a push sending function"""
        print(f"Pushed to a device {device_id}: {message}")


# ADAPTERS
class SMSAdapter(MessageSender):
    def __init__(self, service: SMSService, phone: str):
        self.service = service
        self.phone = phone

    def send_message(self, message: str) -> None:
        """q sending message function from parent class"""
        self.service.send_sms(self.phone, message)


class EmailAdapter(MessageSender):
    def __init__(self, service: EmailService, email: str):
        self.service = service
        self.email = email

    def send_message(self, message: str) -> None:
        """q sending message function from parent class"""
        self.service.send_email(self.email, message)


class PushAdapter(MessageSender):
    def __init__(self, service: PushService, id: str):
        self.service = service
        self.id = id

    def send_message(self, message: str) -> None:
        """q sending message function from parent class"""
        self.service.send_push(self.id, message)


sms_srv = SMSService()
email_srv = EmailService()
push_srv = PushService()

senders = [
    SMSAdapter(sms_srv, "+380991234567"),
    EmailAdapter(email_srv, "user@example.com"),
    PushAdapter(push_srv, "device_99")
]

text = "Hello! This is a message"

for sender in senders:
    sender.send_message(text)
