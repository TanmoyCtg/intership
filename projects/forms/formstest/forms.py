from django import forms 

class TestForm(forms.Form):
    name = forms.CharField(label='Username', max_length=100)
    some_text = forms.CharField(label='Last Name')
    boolean = forms.BooleanField()
    integer = forms.IntegerField()
    email=forms.EmailField(min_length=10, label="E-Mail")

    # validation
    def clean_integer(self, *args, **kwargs):
        integer = self.cleaned_data.get("integer")
        if integer < 10:
            raise forms.ValidationError("The integer must be greater than 10")
        return integer
    
    # name validation
    def clean_name(self, *args, **kwargs):
        take_name = self.cleaned_data.get('name')
        if take_name is not None:
            raise forms.ValidationError("please enter your name")
        elif len(take_name) <3:
            raise forms.ValidationError("The name must be greater than 5")
        return take_name
