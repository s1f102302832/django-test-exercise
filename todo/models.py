from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)#varchar型のカラム(最大100文字)
    completed = models.BooleanField(default=False)#boolean型のカラム(デフォルトはFalse) ->完了しているか
    posted_at = models.DateTimeField(default=timezone.now)#datetime型のカラム（現在時刻）->登録日
    due_at = models.DateTimeField(null=True, blank=True)#datetime型のカラム(nullを可とする)->締切