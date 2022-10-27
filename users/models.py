from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    profile = models.ImageField(null=True, blank=True, upload_to='profiles', default='profiles/default.png')
    location = models.CharField(max_length=200, null=True, blank=True)
    tagline = models.CharField(max_length=400,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    cuisine = models.ManyToManyField('Cuisine', blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    social_facebook = models.CharField(max_length=200, null=True, blank=True)
    social_instagram = models.CharField(max_length=200, null=True, blank=True)
    resume = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    
    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['-id']

    @property
    def imageURL(self):
        try:
            url = self.profile.url
        except:
            url = '/media/profiles/default.png'
        return url
    
    


class Cuisine(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name

class Experience(models.Model):
    employment = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Self Employed', 'Self Employed'),
        ('Internship', 'Internship'),
        ('Trainee', 'Trainee'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    employment_type = models.CharField(max_length=200, null=True, blank=True, choices=employment)
    work_place = models.CharField(max_length=400, null=True, blank=True)
    location = models.CharField(max_length=400, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_currently_working = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.title

class Education(models.Model):
    
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    schoolName = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    field_of_study = models.CharField(max_length=400, null=True, blank=True)
    location = models.CharField(max_length=400, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=12, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.degree


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    reciever = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="recipient")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=400, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']