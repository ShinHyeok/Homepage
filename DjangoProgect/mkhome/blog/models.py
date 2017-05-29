from django.db import models

# Create your models here.
class Categories(models.Model):
	Title = models.CharField(maxxlength=40, null=False)
class TagModel(models.Model):
	Title = models.CharField(maxlength=20, null=False)

class Entries(models.Model):
	id = 0
	Title = moelds.CharField(maxlength=80, null=False)
	Content = models.TextField(null=False)
	created = models.DateTimeFIeld(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	Category = models.ForeignKey(Categories)
	Tags = models.ManyToManyField(TagModel)
	Comments = models.PositiveSmallInteger(default=0, null=True)
class Comments(models.Model):
	Name = models.CharField(maxlength=20, null=False)
	Password = models.CharField(maxlength=32, null=False)
	Content = models.TextField(maxlength=2000, null=False)
	created = models.DateTimeField(auto_now_add=True, auto_now=True)
	Entry = models.ForeignKey(Entires)
	


