from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=400)
    news_link = models.CharField(max_length=300)
    stories = models.TextField(blank=True, null=True)
    image_links = models.CharField(max_length=300, blank=True, null=True)
    news_authors = models.CharField(max_length=100)
    published_date = models.CharField(max_length=50)


    class Meta:
        pass
        # ordering = ('headline',)

    def __str__(self):
        return self.headline

