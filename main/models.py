from django.db import models

class Events(models.Model):
    title=models.CharField("Название", max_length=100)
    some_info=models.CharField("Краткое описание", max_length=250)
    full_info=models.TextField("Мероприятие")
    date=models.DateTimeField('Дата публикации')
    image = models.ImageField(null=True, blank=True, upload_to='media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Мероприятия'
        verbose_name='Мероприятие'
