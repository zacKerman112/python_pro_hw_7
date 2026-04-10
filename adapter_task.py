import json


class MessageSender:
    """Базовий інтерфейс для відправки повідомлень."""

    def send_message(self, message: str) -> None:
        """Метод-шаблон для відправки повідомлення."""
        pass


class SMSService:
    """Сервіс для роботи з SMS."""

    def send_sms(self, phone_number: str, message: str) -> None:
        """Функція відправки SMS-повідомлення."""
        print(f"The message {message} has been sent to number {phone_number}")


class EmailService:
    """Сервіс для роботи з Email."""

    def send_email(self, email_address: str, message: str) -> None:
        """Функція відправки Email-повідомлення."""
        print(f"An email {message} has been sent to {email_address}")


class PushService:
    """Сервіс для роботи з Push-повідомленнями."""

    def send_push(self, device_id: str, message: str) -> None:
        """Функція відправки Push-повідомлення."""
        print(f"Push to a device {device_id}: {message}")


class SMSAdapter(MessageSender):
    """Адаптер для SMSService."""

    def __init__(self, service: SMSService, phone: str) -> None:
        self.service = service
        self.phone = phone

    def send_message(self, message: str) -> None:
        """Реалізація методу через SMSService."""
        self.service.send_sms(self.phone, message)


class EmailAdapter(MessageSender):
    """Адаптер для EmailService."""

    def __init__(self, service: EmailService, email: str) -> None:
        self.service = service
        self.email = email

    def send_message(self, message: str) -> None:
        """Реалізація методу через EmailService."""
        self.service.send_email(self.email, message)


class PushAdapter(MessageSender):
    """Адаптер для PushService."""

    def __init__(self, service: PushService, device_id: str) -> None:
        self.service = service
        self.id = device_id

    def send_message(self, message: str) -> None:
        """Реалізація методу через PushService."""
        self.service.send_push(self.id, message)


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