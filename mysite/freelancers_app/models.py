from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Skill(models.Model):
    skill_name=models.CharField(max_length=32)

    def __str__(self):
        return self.skill_name

class UserProfile(AbstractUser):
    ROLE_CHOICES=(
        ('client','client'),
        ('freelancer','freelancer'),
    )
    role = models.CharField(choices=ROLE_CHOICES, default='freelancer', max_length=32)
    phone_number=PhoneNumberField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    bio=models.TextField()
    avatar=models.ImageField()
    skills=models.ManyToManyField(Skill)


    def __str__(self):
        return f'{self.first_name},{self.last_name}'

class SocialNetwork(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    social_name=models.CharField(max_length=32)
    url=models.URLField()

    def __str__(self):
        return f'{self.social_name},{self.url}'

class Category(models.Model):
    category_name=models.CharField(max_length=32)

    def __str__(self):
        return self.category_name

class Project(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    budget=models.PositiveSmallIntegerField()
    deadline=models.DateField()
    STATUS_CHOICES=(
        ('open','open'),
        ('in_progress','in_progress'),
        ('completed','completed'),
        ('cancelled','cancelled'),
    )
    status=models.CharField(choices=STATUS_CHOICES,max_length=20)
    skills_required=models.ManyToManyField(Skill)
    client=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Offer(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    freelancer=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    message=models.TextField()
    proposed_budget=models.PositiveSmallIntegerField()
    proposed_deadline=models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class Review(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    reviewer=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='reviewer')
    target=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='target')
    rating=models.PositiveSmallIntegerField(choices=[(i,str(i)) for i in range(1, 5)])
    comment=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project},{self.rating},{self.comment}'






    









