from django.test.runner import DiscoverRunner


class NoDbTestRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        kwargs['verbosity'] = 2
        super(NoDbTestRunner, self).__init__(*args, **kwargs)

    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass
