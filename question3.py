from django.db import models, transaction
from django.dispatch import Signal, receiver


class TestModel(models.Model):
    name = models.CharField(max_length=100)

my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    count = TestModel.objects.filter(name="test").count()
    print(f"Record count in receiver: {count}")

if __name__ == "__main__":
    with transaction.atomic():
    
        TestModel.objects.create(name="test")
        print("Record created in transaction.")
        
        my_signal.send(sender=None)
        
    count = TestModel.objects.filter(name="test").count()
    print(f"Record count after transaction: {count}")
