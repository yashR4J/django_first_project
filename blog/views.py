from django.shortcuts import render

posts = [
	{
		'author': 'Sigmund Freud',
		'title': 'Human Psychology',
		'content': 'Humans are intellecutally inferior beings to mammals.',
		'date_posted': 'July 13 2021'
	},
	{
		'author': 'Oscar Wilde',
		'title': 'Ambition',
		'content': 'We are all in a gutter, but some of us are looking at the stars.',
		'date_posted': 'August 14 1894'
	}
]

def home(request):
	context = {
		'posts': posts,
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})