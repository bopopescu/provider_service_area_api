import django
import logging
import os
import sys

from django.test.runner import DiscoverRunner
# from provider_service_area_api.test_utils import NoDbTestRunner

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'provider_service_area_api.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'provider_service_area_api.settings'


def log_warnings():
    logger = logging.getLogger('py.warnings')
    handler = logging.StreamHandler()
    logger.addHandler(handler)


def run_tests():
    test_runner = DiscoverRunner()
    failures = test_runner.run_tests([])
    sys.exit(failures)


def start():
    django.setup()
    log_warnings()
    run_tests()


if __name__ == "__main__":
    start()
