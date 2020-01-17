#from django.shortcuts import render
from django.http import HttpResponse
from  .models import Post
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.
#MTV:
#	M  model -> models.py;	T	template ->	template文件夹;	V	view ->	views.py;
#	models.py负责定义要存取的资料类型，以class类别方式定义，后端Django自动把设定对应到资料库系统中
#	如果将资料拿出来，或者如何存进去的这些程式逻辑，则在views.py中处理
#	如何把这些取到的资料用美观有弹性的方式输出，则是在Template中加以处理
#
#考虑到有可能会有自行输入错误网址以至于找不到文章，除了在Post.objects.get(slug=slug)搜索文章时加上例外处理，
#也在发生例外的时候以redirect('/')方式直接返回首页


'''
# 将models.py中自定义的model引入，然后使用Post.objects.all()取得所有的资料项目，然后用for遍历所有内容
#透过HttpResponse输出到网页中
##
#再次理中建立homepage函数获取所有文章，并通过遍历把内容存储到一个变量post_lists中，再使用
#return HttpResponse(post_lists)输出到网页上
#
#设置完函数后，透过urls.py来负责网址和程序间的对应工作。开放urls.py，分别引入来自于views.py的
#homepage函数并以url对应之
def homepage(request):
	posts = Post.objects.all()
	post_lists = list()
	for count,post in enumerate(posts):
		post_lists.append("No.{}:".format(str(count))+str(post)+"<hr>")
		post_lists.append("<small>"+str(post.body)+"</small><br><br>")
	return HttpResponse(post_lists)
'''

def	homepage(request):
	template = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	html = template.render(locals())
	return HttpResponse(html)
	
def showpost(request,slug):
	template = get_template('post.html')
	try:
		post = Post.objects.get(slug=slug)	#匹配传入参数与资料库中的slug
		if post!= None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/')	#错误直接返回首页