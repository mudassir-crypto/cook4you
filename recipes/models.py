from users.models import Profile, Cuisine
import uuid
from django.db import models

class Recipe(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    procedure = models.TextField(null=True, blank=True)
    cuisine = models.ManyToManyField(Cuisine, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='recipes', default='profiles/default.png')
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
    
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
    
    

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/media/profiles/default.png'
        return url

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_ratio = ratio
        self.vote_total = totalVotes
        self.save()

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=40, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)


    def __str__(self):
        return self.value

    class Meta:
        unique_together = [['owner', 'recipe']]