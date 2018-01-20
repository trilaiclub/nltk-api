"""reco bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as recoBaseController.

from reco.cli.controllers.base import recoBaseController

def load(app):
    app.handler.register(recoBaseController)
