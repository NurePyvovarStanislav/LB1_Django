from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст статті")
    publication_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публікації"
    )

    def __str__(self):
        return self.title