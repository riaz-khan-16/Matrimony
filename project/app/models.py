from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name
    
#one to one example
class Iitial_info(models.Model):
    full_name = models.CharField(max_length=20)
    age=models.IntegerField(null=True)
    gender = models.CharField(max_length=50,null=True)
    height=models.IntegerField(null=True)
    body_color= models.CharField(max_length=20,null=True)
    present_adress=models.CharField(max_length=50,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)   
    def __str__(self):
        return self.user.name
    

class Educational_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    ssc_year=models.IntegerField(null=True)
    ssc_result=models.CharField(max_length=20,null=True)
    hsc_year=models.IntegerField(null=True)
    hsc_result=models.CharField(max_length=20,null=True)
    university=models.CharField(max_length=20)
    subject=models.CharField(max_length=20,null=True)
    bachelor_completed_year=models.IntegerField(null=True)
    def __str__(self):
        return self.user.name


    
class Professional_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession=models.CharField(max_length=20,null=True)
    organization=models.CharField(max_length=20,null=True)
    monthly_income=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.name


class Family_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_members=models.CharField(max_length=100,null=True)
    father_profession=models.CharField(max_length=20,null=True)
    mother_profession=models.CharField(max_length=20,null=True)
    number_of_bro=models.CharField(max_length=20,null=True)
    number_of_sister=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.name


class  Desired_person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desired_person_profession=models.CharField(max_length=80,null=True)
    desired_person_height=models.CharField(max_length=20,null=True)
    desired_person_age=models.CharField(max_length=20,null=True)
    desired_person_education=models.CharField(max_length=50,null=True)
    desired_person_qualities=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.user.name

  



    

#one to many example

# class Initial_intro(models.Model):
#     user=models.ForeignKey(Author,on_delete=models.CASCADE)
#     title=models.CharField(max_length=20)
#     description=models.CharField(max_length=200)
#     def __str__(self):
#         return self.title



# #many to many example
# class Comments(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     tags = models.ManyToManyField(Author)     
#     def __str__(self):
#         return self.title
    

    