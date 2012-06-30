from django.core.management.base import BaseCommand, CommandError
from comics.models import Comic

from django.utils.timezone import now

class Command(BaseCommand):
	args = ''
	help = 'Publishes all scheduled comics'
	
	def handle(self, *args, **options):
		to_publish = Comic.objects.filter(posted_on__lt=now(), published=False)
		if len(to_publish) > 0:
			for comic in to_publish:
				comic.published = True	
				comic.save()
				print 'Published ', comic.title
		else:
			print 'No comics scheduled'
		
	
	
