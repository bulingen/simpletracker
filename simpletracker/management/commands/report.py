from django.core.management.base import BaseCommand
from simpletracker.models import LogEntry
from datetime import timedelta
from django.utils import timezone, dateparse, dateformat


class Command(BaseCommand):
    help = 'Print visitor log'

    def add_arguments(self, parser):
        example_date = dateformat.format(timezone.now(), 'Y-m-d H:i')
        parser.add_argument(
            '--from',
            help='E g "{}"'.format(example_date),
        )
        parser.add_argument(
            '--to',
            help='E g "{}"'.format(example_date),
        )

    def handle(self, *args, **options):
        from_datetime = options['from']
        to_datetime = options['to']

        log_entries = LogEntry.objects.all()

        if from_datetime:
            parsed = dateparse.parse_datetime(from_datetime)
            if parsed:
                log_entries = log_entries.filter(
                    created_at__gte=timezone.make_aware(parsed))

        if to_datetime:
            parsed = dateparse.parse_datetime(to_datetime)
            if parsed:
                log_entries = log_entries.filter(
                    created_at__lte=timezone.make_aware(parsed))

        for entry in log_entries:
            print("{}UTC\t{}\t{}".format(dateformat.format(
                entry.created_at, 'Y-m-d H:i'), entry.visitor_id, entry.page))
