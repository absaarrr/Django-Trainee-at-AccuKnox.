import threading
from django.dispatch import Signal, receiver

my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print(f"Receiver running in thread: {threading.current_thread().name}")

if __name__ == "__main__":
    print(f"Signal sender running in thread: {threading.current_thread().name}")
    my_signal.send(sender=None)
