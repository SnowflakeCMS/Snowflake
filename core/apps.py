import pickle

from django.apps import AppConfig
from django.core.exceptions import ObjectDoesNotExist


class CoreConfig(AppConfig):
    name = 'core'
    settings_fields = {
        "title": "This is a blog title",
    }

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        self.setting_values = {}
        self.setting_objects = {}

    def get_setting_value(self, name):
        value = self.setting_objects.get(name)
        if value is not None:
            return value
        else:
            # if not get setting from value, try in object
            value_obj = self.setting_objects.get(name)
            if value_obj is not None:
                value = value_obj.get_value()
                self.setting_values[name] = value
                return value
            else:
                setting_model = self.get_model("Setting")
                try:
                    value_obj = setting_model.objects.get(id=name)
                except ObjectDoesNotExist:
                    default_val = CoreConfig.settings_fields.get(name)
                    if default_val is None:
                        return None
                    else:
                        value_obj = setting_model()
                        value_obj.set_name(name)
                        value_obj.set_value(default_val)
                        value_obj.save()
                        self.setting_values[name] = default_val
                        self.setting_objects[name] = value_obj
                        return default_val
