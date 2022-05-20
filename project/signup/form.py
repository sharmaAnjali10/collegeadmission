from ctypes.wintypes import SIZE
from dataclasses import field
from django import forms
from django.forms import DateInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
Courses= [
    ('MCA', 'MCA'),
    ('M.TECH', 'M.TECH'),
    ('MBA', 'MBA'),
    ('MSC', 'MSC'),
    ('MA', 'MA'),
    ('BA', 'BA'),
    ('BSC', 'BSC'),
    ('B.Com', 'B.Com'),
    ('Certificate Courses', 'Certificate Courses'),
    ('PG Diploma', 'PG Diploma'),
    ('M.Com', 'M.Com'),
    ('B.A.LLB', 'B.A.LLB'),
    
    ]
state=[
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Rajasthan','Rajasthan'),
    ('Uthrakhand','Uthrakhand'),
    ('Tripura','Tripura'),
    ('uttarpradesh','uttarpradesh'),
    ('jharkhand','jharkhand'),
    ('Andhra Pradesh','Andhra Pradesh'),	
    ('Assam','Assam'),
    ('Bihar','Bihar'),
	('Chhattisgarh','Chhattisgarh'),
	('Goa','Goa'),
	('Gujarat','Gujarat'),
	('Haryana','Haryana'),
	('Karnataka','Karnataka'),
	('Kerala','Kerala'),	
  ('Madhya Pradesh','Madhya Pradesh'),
	('Maharashtra','Maharashtra'),
	('Manipur','Manipur'),
	('Meghalaya','Meghalaya'),
	('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
	('Odisha','Odisha'),
('Punjab','Punjab'),
('Sikkim','Sikkim'),
	('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),
	('West Bengal','West Bengal'),



]
dist=[
   ('Hamirpur','Hamirpur'), 
   ('Kangra','Kangra'), 
   ('Bilaspur','Bilaspur'),
   ('Mandi','Mandi') , 
   ('Chamba','Chamba'),
   ('Una','Una'),
   (' Sirmaur',' Sirmaur'), 
   ('Lahul and Spiti','Lahul and Spiti'),
   ('Kullu','Kullu') , 
   ('Kinnaur','Kinnaur'),
   ('Shimla','Shimla'),
   ('Solan','Solan') , 
]
option=[
('Male','Male'),
('Female','Female'),
]
nation=[
    ('Indian','Indian'),
    ('others','others'),
]
class SignupForm(UserCreationForm):

    password1=forms.CharField(label="Password",widget=forms.PasswordInput (attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password ",widget=forms.PasswordInput (attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','email')
  
class MyloginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'class':'form-control'}))
 password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form-control'}),
    )
class RegisterForm(forms.Form):
    first_name=forms.CharField(required=True,max_length=20,label="First_name",widget=forms.TextInput(attrs={'class':'form-control'})) 
    last_name=forms.CharField(max_length=20,label="Last_name",widget=forms.TextInput(attrs={'class':'form-control'})) 
#    Date_of_birth=forms.CharField(label="Date_Of_Birth",widget=forms.DateTimeField)
    Father_name=forms.CharField(max_length=100,label="Father_name",widget=forms.TextInput(attrs={'class':'form-control'})) 
    Mother_name=forms.CharField(max_length=100,label="Mother_name",widget=forms.TextInput(attrs={'class':'form-control'})) 
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    Nationality=forms.CharField(label="Nationality",widget=forms.Select(choices=nation))
    phone_number=forms.CharField(label="phone_number",widget=forms.TextInput(attrs={'class':'form-control'})) 
    Gender=forms.CharField(label="Gender",widget=forms.RadioSelect(choices=option)) 
   
    State=forms.CharField(label="State:",widget=forms.Select(choices=state))
    district=forms.CharField(label="District",widget=forms.Select(choices=dist)) 
   
    Courses = forms.CharField(label=" Courses  :",widget=forms.Select(choices=Courses))
    Address=forms.CharField(label="Address",widget=forms.Textarea(attrs={'class':'form-control '}))
    class Meta:

        model=User
        fields=('first_name','last_name','Nationality','phone_number','Father_name',' Mother_name','Dateofbirth',' Gender','state','Qualification','Address')
  