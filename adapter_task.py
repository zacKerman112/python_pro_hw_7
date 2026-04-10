import json


class MessageSender:
    """Base interface for sending messages."""

    def send_message(self, message: str) -> None:
        """Template method for sending a message."""
        pass


class SMSService:
    """Service for handling SMS operations."""

    def send_sms(self, phone_number: str, message: str) -> None:
        """Function to send an SMS message."""
        print(f"The message {message} has been sent to number {phone_number}")


class EmailService:
    """Service for handling Email operations."""

    def send_email(self, email_address: str, message: str) -> None:
        """Function to send an Email message."""
        print(f"An email {message} has been sent to {email_address}")


class PushService:
    """Service for handling Push notification operations."""

    def send_push(self, device_id: str, message: str) -> None:
        """Function to send a Push notification."""
        print(f"Push to a device {device_id}: {message}")


class SMSAdapter(MessageSender):
    """Adapter for the SMSService."""

    def __init__(self, service: SMSService, phone: str) -> None:
        self.service = service
        self.phone = phone

    def send_message(self, message: str) -> None:
        """Implementation of the send method via SMSService."""
        self.service.send_sms(self.phone, message)


class EmailAdapter(MessageSender):
    """Adapter for the EmailService."""

    def __init__(self, service: EmailService, email: str) -> None:
        self.service = service
        self.email = email

    def send_message(self, message: str) -> None:
        """Implementation of the send method via EmailService."""
        self.service.send_email(self.email, message)


class PushAdapter(MessageSender):
    """Adapter for the PushService."""

    def __init__(self, service: PushService, device_id: str) -> None:
        self.service = service
        self.id = device_id

    def send_message(self, message: str) -> None:
        """Implementation of the send method via PushService."""
        self.service.send_push(self.id, message)


if __name__ == "__main__":
    sms_srv = SMSService()
    email_srv = EmailService()
    push_srv = PushService()

    senders: list[MessageSender] = [
        SMSAdapter(sms_srv, "+380991234567"),
        EmailAdapter(email_srv, "user@example.com"),
        PushAdapter(push_srv, "device_99")
    ]

    text = "Hello! This is a message"

    for sender in senders:
        sender.send_message(text)