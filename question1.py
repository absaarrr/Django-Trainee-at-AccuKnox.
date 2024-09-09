import time
from django.dispatch import Signal, receiver
my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver started")
    time.sleep(5)  
    print("Receiver finished")

if __name__ == "__main__":
    print("Sending signal...")
    my_signal.send(sender=None)
    print("Signal sent.")