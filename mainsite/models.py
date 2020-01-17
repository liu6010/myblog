from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200)  #文章标题
	slug  = models.CharField(max_length=200)	#文章网址
	body = models.TextField()				#文章内容
	pub_date = models.DateTimeField(default=timezone.now)	#发表日期

	class Meta:
		ordering = ('-pub_date',)  #根据发表日期排序
		
	#提供此类别所产生的资料项目，以文章标题当做是显示的内容，Unicode标题可以支持中文标题(在python3中使用str)
	def __str__(self):	
		return self.title