from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from .forms import CommentForm
from django.utils import timezone
from .models import Comment


def home(request):
	return render(request, "blog.html", {})

def strings(request):
	if request.method=='POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.published_date = timezone.now()
			post.save()
			return redirect('blog/ strings')
	else:
		form=CommentForm()
	cmt=Comment.objects.all()
	return render(request, 'strings.html', {'form':form,'cmt':cmt})

def list(request):
	return render(request, 'list.html', {})

def D_ORM(request):
	return render(request, 'D_ORM.html', {})

def GIT(request):
	return render(request, 'GIT.html', {})

def Functions(request):
	return render(request, 'Functions.html', {})

def Functions2(request):
	return render(request, 'built_in_function_2.html', {})

def Avro(request):
	return render(request, 'Avro.html', {})

def Web_Scrapping(request):
	return render(request, 'Web_Scrapping.html', {})


def Host_Project_in_pythonAnywhere(request):
	return render(request, 'Host_Project_in_pythonAnywhere.html', {})

def github(request):
	return render(request, 'github.html', {})
