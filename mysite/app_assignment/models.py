from django.db import models
## Products Models

class productMainModel(models.Model):
	Title= models.CharField(max_length=30)
	Description=models.CharField(max_length=30)
	Unique_id= models.CharField(max_length=30)
	Price= models.CharField(max_length=30)

class productImageModel(models.Model):
    product = models.ForeignKey(productMainModel, on_delete=models.CASCADE)


# Create your models here.
#making choices here

status_choice=((1,'Pending'),
                (2,'Completed'))
gender_choice=((1,'Male'),
                (2,'Female')
                ,(3,'Others'))
##Accounts Models
class userModel(models.Model):
    Phone_number = models.CharField(max_length=30, unique=True)
    Email = models.EmailField(max_length=254)
    is_customer = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

class userProfile(models.Model):
    owner= models.OneToOneField(
        userModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Name = models.CharField(max_length=30)
    Date_of_birth = models.CharField(max_length=30)
    Gender = models.CharField(max_length=30)
    Image = models.ImageField(upload_to ='uploads/')

class userloginotpModel(models.Model):
    owner = models.ForeignKey(userModel, on_delete=models.CASCADE)
    Otp = models.IntegerField()
    active = models.BooleanField(default=True)

class UserCartProductModel(models.Model):
    owner = models.ForeignKey(userModel, on_delete=models.CASCADE)
    product= models.ForeignKey(productMainModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=status_choice,default='1')

class UserCartModel(models.Model):
    owner = models.OneToOneField(
        userModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    products = models.ManyToManyField(UserCartProductModel)
    price =  models.CharField(max_length=30)
