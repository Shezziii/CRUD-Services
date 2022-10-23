from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
# Create your form Here.
class Userform(forms.ModelForm):
       
       class Meta:
        model=User
        fields=['username' , 'password' , 'email' ]
        lables=''
        widgets={
        'password':forms.PasswordInput(attrs={'class':"form-control" , 'id' : 'floatingInput'  ,'placeholder':"password"}) ,                    
        'username':forms.TextInput(attrs={'class':"form-control" , 'id' : 'floatingInput'  ,'placeholder':"mohd shuib Khan"}),
        'email':forms.EmailInput(attrs={'class':"form-control" , 'id' : 'floatingInput' ,'placeholder':"name@example.com"})
        }
       rpassword=forms.CharField(max_length=10 , widget=forms.PasswordInput(attrs={'class':"form-control" , 'id' : 'floatingInput'  ,'placeholder':"Password"}) )
       def clean(self):
           cleaned_data=super().clean()
           password=cleaned_data['password']
           Rpassword=cleaned_data['rpassword']
           if Rpassword!=password:
                print("Password's are don't' Matched.")
                
                raise ValidationError("Password and Confirm password are Different.")
                
           else:
               return cleaned_data