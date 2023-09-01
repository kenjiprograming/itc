from django.db import models

class NippoModel(models.Model):
    class Meta:
        verbose_name = '日報'
        verbose_name_plural = '日報一覧'

    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.TextField(max_length=1000, verbose_name='コンテンツ')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title