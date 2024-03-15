from django.db import models


class labels(models.Model):
    label_name = models.CharField(max_length=100)
    def __str__(self):
        return self.label_name




class Notification(models.Model):
    title = models.CharField(max_length=500)
    label = models.ForeignKey(labels, on_delete=models.CASCADE)
    imgs = models.ImageField(upload_to='Notification/',)
    content = models.TextField()

    def __str__(self):
        return self.title


