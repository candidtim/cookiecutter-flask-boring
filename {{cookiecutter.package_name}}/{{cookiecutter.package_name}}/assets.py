import json
import os

from flask import current_app


class Assets:
    """
    Assets extension adds an `assets` context processor to load assets from a
    webpack manifest file.
    """

    def __init__(self, app=None):
        self.app = app
        self.assets = {}
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.manifest_path = os.path.join(app.static_folder, "manifest.json")
        self._get_webpack_assets(app)
        app.context_processor(lambda: {"assets": self})

        if app.config.get("DEBUG"):
            app.before_request(self._reload_webpack_assets)

    def url_for(self, file):
        return self.assets.get(file)

    def _reload_webpack_assets(self):
        self._get_webpack_assets(current_app)

    def _get_webpack_assets(self, app):
        with app.open_resource(self.manifest_path) as manifest:
            self.assets = json.load(manifest)


assets = Assets()


def init_app(app):
    assets.init_app(app)
