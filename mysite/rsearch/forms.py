from django import forms


class DishForm(forms.Form):
    dish_name = forms.CharField(label="Dish you want to eat", max_length=100)