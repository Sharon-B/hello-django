# from django import forms to use the built in Django form functionality
from django import forms
# from our Item model from .models
from .models import Item


# Create a form class that inherits functionality from forms.ModelForm
class ItemForm(forms.ModelForm):
    # Create an inner class to tell the form which model it's going to be
    # associated with, which fields it should render & how it should
    # display error messages etc.
    class Meta:
        model = Item
        fields = ['name', 'done']
