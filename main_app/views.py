from django.shortcuts import render

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