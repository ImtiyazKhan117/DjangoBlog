from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from blog.models import Post
from . import views

urlpatterns = [
	url(r'^index',views.index,name="index"),
	url(r'^blog',ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
		template_name="page_src/blog.html")),
	url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,
									template_name="page_src/post.html")),
#	url(r'^contact/$',ListView.as_view(queryset=snippet.objects.all(),
#										template_name="page_src/template/footer.html"))
	url(r'^contact',views.contact,name="contact"),
	#url(r'^',views.Snippet_details),
	url(r'^about',views.about,name='about')	
	]

