# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from unicodedata import name
from django.template import context
import csv
from .forms import DishForm
import json

def index(request):

    if request.method =="POST":
        form = DishForm(request.POST)
        if form.is_valid():
            request.session['dish_name'] = request.POST['dish_name']
        return redirect('result')
    else:
        form = DishForm
    
    return render(request, 'home.html',{"form":form})

def result(request):
    item_to_search = request.session.get('dish_name')
    item_to_search = item_to_search.title()
    file = open("static/restaurants_small.csv")
    csvreader = csv.reader(file)
    rows = []
    d = dict()
    for row in csvreader:
       rows.append(row)
    for r in rows:
       d.update({r[1]:r[3]})
    def find_restaurants_with_dish(d, dish):
        restaurants = {}
        
        for restaurant, menu in d.items():
           res = json.loads(menu)
           if dish in res:
            restaurants[restaurant] = res[dish]
              
        return restaurants
        
    
    restaurant_list = find_restaurants_with_dish(d, item_to_search)

    
    context = {'restaurants':restaurant_list}
     
    file.close()
    return render(request,'result.html',context)

def about(request,restaurant):
    file = open("static/restaurants_small.csv")
    csvreader = csv.reader(file)
    rows = []
    d = dict()
    for row in csvreader:
        rows.append(row)
    for r in rows:
        d.update({r[1]:r[5]})
    
    def findThis(d,restaurant):
        aboout = []
        for restor,desc in d.items():
            if restor == restaurant:
                  aboout = desc
        return aboout
    information = findThis(d,restaurant)
    restaurant_info = json.loads(information)
    context = {'info':restaurant_info}
    file.close()
    return render(request,'about.html',context)



