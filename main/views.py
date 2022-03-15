from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import *
from .forms import ReviewsForm

class movieView(View):
    
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        return render(request, 'main/movie_list.html',{"movies_list":movies})

# class movieView(ListView):
#     model = Movie
#     queryset = Movie.objects.filter(draft=False)
#     template_name = "main/movie_list.html" 
    
        
class MovieDetailView(View):
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "main/moviesingle.html", {"movie": movie})
    
class AddReview(View):
    """Comments"""
    def post(self, request, pk):
        form = ReviewsForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent',None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())