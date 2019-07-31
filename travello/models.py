from django.db import models

# Create your models here.

#class Destination:     # thats if we work with a class not as a model 
  #    id:int
  #   name:str
  #   img:str
  #   desc:str
  #   price:int
  #   offer:bool  # for true and false 
class Destination(models.Model):    # if we add (models.model )to the class its will be model... if we want to work with sql
                                             # we make a table in sql bye 1- python manage.py makemigrations 2-python manage.py migrate
   name = models.CharField( max_length=100)
   img= models.ImageField(upload_to="pics")
   desc= models.TextField()
   price = models.IntegerField()
   offer= models.BooleanField(default=False)

