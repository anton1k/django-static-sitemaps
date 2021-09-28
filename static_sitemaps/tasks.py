from celery import shared_task

from static_sitemaps.generator import SitemapGenerator

__author__ = 'xaralis'

# Create class conditionally so the task can be bypassed when repetition 
# is set to something which evaluates to False.

@shared_task()
def generate_sitemap():
    generator = SitemapGenerator(verbosity=1)
    generator.write()