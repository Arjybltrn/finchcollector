from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

from django.http import HttpResponse
from .models import Finch

# class Finch:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# finches = [
#   Finch('Mango', 'European goldfinch', 'foul little demon', 3),
#   Finch('Ollie', 'Hawfinch', 'evil, funny', 2),
#   Finch('Raven', 'Brambling', 'Atlantic canary', 4)
# ]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {'finches': finches })

def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', {'finch': finch})

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  # success_url = '/cats/'

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

