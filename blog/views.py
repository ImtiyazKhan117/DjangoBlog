from django.shortcuts import render
from blog.forms import ContactForm
from blog.forms import SnippetForm

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():		
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
	form = ContactForm()
	return render(request,"page_src/contact.html", {'form':form})



def Snippet_details(request):
	if request.method == 'POST':
		form = SnippetForm(request.POST)
		if form.is_valid():
			form.save()
		
	form = SnippetForm()
	return form
	
def index(request):
	form = Snippet_details(request)
	return render(request,"page_src/index.html",{'form':form})

def about(request):
	form = Snippet_details(request)
	return render(request,"page_src/about.html",{'form':form})


