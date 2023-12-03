"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class ThingForm(forms.ModelForm):
    """Form for the Thing model."""
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput()
        }
    
    # The form must accept valid inputs for Thing and reject invalid input for Thing.
    # name must be between 1 and 35 characters long and must be unique
    name = forms.CharField(min_length=1, max_length=35,) 
    description = forms.CharField(max_length=120, required=False)
    quantity = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)]) 

