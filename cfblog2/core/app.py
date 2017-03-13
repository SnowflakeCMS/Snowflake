import enum
from flask import Flask, request
from .settings import Settings


class CoreApp(Flask):
    class CoreSettingEnum(enum.Enum):
        title = "core.title"
        subtitle = "core.subtitle"

    def __init__(self, db, base_dir, *args, **kwargs):
        super(CoreApp, self).__init__(*args, **kwargs)
        self._project_base_dir = base_dir
        self._db = db
        self.before_request(self._before_each_request)

    def _before_each_request(self):
        request.settings = Settings()


