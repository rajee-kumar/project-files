from django.db import models

# Create your models here.
# import the standard Django Model 
# from built-in library 
from django.db import models 

# declare a new model with a name "GeeksModel" 


class GeeksModel(models.Model): 
		# fields of the model 
	title = models.CharField(max_length=200) 
	description = models.CharField(max_length=500) 
	last_modified = models.DateTimeField(auto_now_add=True) 
	img = models.ImageField(upload_to= "quot images/")
	Example_age = models.IntegerField(null=True)
	vinay=models.CharField(max_length=100)
	ankit=models.CharField(max_length=100)
	Ritendra=models.CharField(max_length=100)
	marks=models.IntegerField(null=True)
	
	# renames the instances of the model 
	# with their title name 
	def __str__(self): 
		return self.title 
class DataApi(models.Model):
	name=models.CharField(max_length=200)
	id=models.IntegerField(primary_key=True)
	sal=models.FloatField(null=True)
class student(models.Model):
	student_name=models.CharField(max_length=50)
	id=models.IntegerField(primary_key=True)
	fee=models.IntegerField(null=True)
class emp(models.Model):
	empname=models.CharField(max_length=200)
	empid=models.IntegerField(primary_key=True)
	sal=models.FloatField(null=True)
	


	 
	




	
    
