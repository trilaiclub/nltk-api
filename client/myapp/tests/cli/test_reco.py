"""CLI tests for reco."""

from reco.utils import test

class CliTestCase(test.recoTestCase):
    def test_reco_cli(self):
        argv = ['--foo=bar']
        with self.make_app(argv=argv) as app:
            app.run()
            self.eq(app.pargs.foo, 'bar')
