from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm

# Create your views here.


def home_page(request):
    recipes = Recipe.objects.all().order_by('created_at')[0:3]
    context = {
        'recipes' : recipes,
    }
    return render(request, 'pages/home.html', context)


def menu_view(request):
    menus = Recipe.objects.all().order_by('-created_at')
    context = {
        'menus' : menus,
    }
    return render(request, 'pages/menu.html', context)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    comments = Comment.objects.filter(recipe=recipe)
    recipe.description = recipe.description.replace('. ' , '. <br>')
    recipe.description = recipe.description.replace(': ' , ': <br>')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
    else:
        form = CommentForm()
    context = {
        'recipe' : recipe,
        'comments' : comments,
        'form' : form,
    }
    return render(request, 'pages/recipe_detail.html', context)



def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()

    return render(request, 'pages/add_recipe.html', {'form' : form})

def update_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        update = RecipeForm(request.POST, instance=recipe)
        if update.is_valid():
            update.save()
            return redirect('home')
    else: 
        update = RecipeForm(instance=recipe)

    return render(request, 'pages/update_recipe.html', {'update' : update})

def delete_recipe(request, slug, pk):
    recipe = get_object_or_404(Recipe, slug=slug, pk=pk)
    recipe.delete()
    return redirect('home')


def about_view(request):
    return render(request, 'pages/about.html')