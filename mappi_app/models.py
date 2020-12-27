from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    user_name = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name

class Store(models.Model):
    store_adress = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    store_image = models.ImageField(upload_to='',null=True,blank=True)
    store_link = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.store_name

class Review(models.Model):
    review_sentence = models.CharField(max_length=140)
    review_score = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)