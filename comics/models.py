from django.db import models
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site

class CustomFlatPage(FlatPage):
    class Meta:
        proxy = True
	verbose_name = 'Static Page'
	verbose_name_plural = 'Static Pages'

    def save(self):
	super(CustomFlatPage, self).save()
        self.sites = [Site.objects.get(pk=settings.SITE_ID)]

# Create your models here.
class Comic(models.Model):
	title = models.CharField(max_length=1024)
	slug = models.SlugField()
	image = models.ImageField(upload_to="comics")
	thumbnail = models.ImageField(upload_to="thumbs")
        posted_on = models.DateTimeField()
	published = models.BooleanField()

	def __unicode__(self):
		return self.title
