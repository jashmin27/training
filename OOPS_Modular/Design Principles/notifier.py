from abc import ABC, abstractmethod


# This is the interface. OrderService will depend on THIS, not on a
# specific way of sending notifications. This fixes the tight coupling
# problem from the bad code (email was hardcoded).
class Notifier(ABC):

    @abstractmethod
    def send(self, email, message):
        pass


class EmailNotifier(Notifier):

    def send(self, email, message):
        print(f"Sending email to {email}: {message}")


class ConsoleNotifier(Notifier):

    def send(self, email, message):
        print(f"[console notification for {email}]: {message}")
