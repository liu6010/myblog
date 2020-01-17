from django.contrib import admin
from .models import Post
# Register your models here.
#先引入Post类别，然后再透过admin.site.register注册即可。
#然后通过http://host:8000/admin，即可登录
class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','pub_date')
admin.site.register(Post,PostAdmin)