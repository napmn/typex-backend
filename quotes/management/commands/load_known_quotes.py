import json
import logging

from django.core.management.base import BaseCommand

from quotes.enums import QuoteType
from quotes.models import Author, Quote


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str)

    def handle(self, *args, **options):
        with open(options['filepath'], 'r') as quotes_f:
            quotes = json.load(quotes_f)

        for quote in quotes:
            if quote['author']:
                author, _ = Author.objects.get_or_create(name=quote['author'])
            else:
                author = None
            quote = Quote.objects.create(
                text=quote['text'], author=author, quote_type=QuoteType.KNOWN
            )
            logger.debug(f'Quote {quote.perex} by {quote.author} was saved')

