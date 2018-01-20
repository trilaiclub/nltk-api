"""Tests for Example Plugin."""

from reco.utils import test

class ExamplePluginTestCase(test.recoTestCase):
    def test_load_example_plugin(self):
        self.app.setup()
        self.app.plugin.load_plugin('example')
