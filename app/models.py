from django.conf import settings
from django.db import models
from django.utils import timezone


class Detail(models.Model):
  part = models.CharField("部位", max_length=100)
  title = models.CharField("タイトル", max_length=100)
  image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
  cause = models.TextField("原因")
  improve = models.TextField("対策")
  video = models.CharField("動画", max_length=200, null=True, blank=True)
  created = models.DateTimeField("作成日", default=timezone.now)

  def __str__(self):
    return self.part
