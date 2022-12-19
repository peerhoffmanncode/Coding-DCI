from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    amount = models.IntegerField()
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{str(self.name).title()} with a ballance of {round(int(self.amount)/100, 2)}€, joined at {self.joining_date}"

    def to_json(self):
        return {
            "pk": self.pk,
            "name": str(self.name).title(),
            "amount": round(self.amount / 100, 2),
            "joining_date": self.joining_date,
        }
