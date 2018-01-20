"""Testing utilities for reco."""

from reco.cli.main import recoTestApp
from cement.utils.test import *

class recoTestCase(CementTestCase):
    app_class = recoTestApp

    def setUp(self):
        """Override setup actions (for every test)."""
        super(recoTestCase, self).setUp()

    def tearDown(self):
        """Override teardown actions (for every test)."""
        super(recoTestCase, self).tearDown()

