from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    op1 = models.CharField(max_length=30)
    op2 = models.CharField(max_length=30)
    op3 = models.CharField(max_length=30)
    op1_count = models.IntegerField(default=0)
    op2_count = models.IntegerField(default=0)
    op3_count = models.IntegerField(default=0)


    def total(self):
        return self.op1_count + self.op2_count + self.op3_count

    def __str__(self):
        return self.question