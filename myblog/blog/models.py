from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    date_posted = models.DateTimeField(verbose_name="Date Published")

    def __str__(self):
        return f'{self.title}: {self.content}'