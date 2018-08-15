from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from .forms import CommentForm
from django.utils import timezone
from .models import Comment


def home(request):
	return render(request, "blog.html", {})

def post_details(request):
	if request.method=='POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.published_date = timezone.now()
			post.save()
			return redirect('blog/post_details')
	else:
		form=CommentForm()
	cmt=Comment.objects.all()
	return render(request, 'post_details.html', {'form':form,'cmt':cmt})

def post_details2(request):
	return render(request, 'post_details2.html', {})

def post_details3(request):
	return render(request, 'post_details3.html', {})

def post_details4(request):
	return render(request, 'post_details4.html', {})

def post_details5(request):
	return render(request, 'post_details5.html', {})

def post_details6(request):
	return render(request, 'post_details6.html', {})

def post_details7(request):
	return render(request, 'post_details7.html', {})


def post_details8(request):
	return render(request, 'post_details8.html', {})

def post_details9(request):
	return render(request, 'post_details9.html', {})
