from django import forms



class UserregForm(forms.Form):
    f_name = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your first name",}),label ='First Name')
    m_name = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your mid name",}),label ='Middle Name',required=False)
    l_name = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your last name",}),label ='Last Name')
    email = forms.EmailField(widget= forms.EmailInput(attrs={"class": "form-control", "placeholder":"Enter your Email Address",}),label="Email Address")
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class": "form-control", "placeholder":"Enter your Password",}),label="Password",min_length=8)
    cpassword = forms.CharField(widget= forms.PasswordInput(attrs={"class": "form-control", "placeholder":"Enter your confirm password",}),label="Confirm Password",min_length=8)
    prof_pic = forms.ImageField(label='Upload Image',required=False)
    class Meta:
        abstract = True
    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        password2 = data.get("cpassword")
        if password!=password2:
            raise forms.ValidationError("Passwords must match!")
    
    
    
    def clean_username(self):
        email = self.cleaned_data.get("email")
        qs = farmer(username=email)
        if qs.exists():
            raise forms.ValidationError("Username already taken.")
        else:
            return qs
    
class SellerForm(UserregForm):
    b_name = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your business name",}),label ='Business Name')  
    addr_l1 = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your adress line 1",}),label ='Adress line 1')
    addr_l2 = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your adress line 2",}),label ='Adress line 2')
    city = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your city name",}),label ='City name')
    state = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your state name",}),label ='State Name')


class FarmerForm(UserregForm):
    addr_l1 = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your adress line 1",}),label ='Adress line 1')
    addr_l2 = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your adress line 2",}),label ='Adress line 2')
    city = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your city name",}),label ='City Name')
    state = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your state name"}),label ='State Name')


class WorkerForm(UserregForm):
    city = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your city name",}),label ='City Name')
    state = forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your state name"}),label ='State Name')



class TransportForm(UserregForm):
    transport_mode=forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your mode of transportation",}),label ='Vehicle Type')
    weight_capacity=forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your weight capacity",}),label ='Capacity')
    reg_no=forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your vehicle registration number",}),label ='Registration Number')
    permit_type=forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Enter your permit type",}),label ='Permit Type')

class LoginForm(forms.Form):
    username= forms.CharField(widget = forms.TextInput (attrs={"class": "form-control", "placeholder":"Username",}),label ='Username')
    password = forms.CharField(widget = forms.PasswordInput (attrs={"class": "form-control", "placeholder":"Enter Password",}),label ='Password')


