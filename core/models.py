import pickle

from django.db import models


# Blog Setting is
class Setting(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    value = models.TextField()
    type = models.CharField(max_length=20)

    TYPE_NAME_STRING = "string"
    TYPE_NAME_PICKLE = "pickle"
    TYPE_NAME_PYTHON = "python"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_name(self, name):
        self.id = name

    def get_name(self):
        return self.id
    
    def set_value(self, value):
        return self.set_string_value(value)

    def set_string_value(self, value):
        if type(value) != str:
            raise ValueError("Except value is string type")
        self.type = Setting.TYPE_NAME_STRING
        self.value = value

    def get_value(self):
        if self.type == Setting.TYPE_NAME_PICKLE:
            # TODO
            raise TypeError("Not Support type")
        elif self.type == Setting.TYPE_NAME_PYTHON:
            # TODO
            raise TypeError("Not Support type")
        elif self.type == Setting.TYPE_NAME_STRING:
            return self.value
        else:
            return self.value


# Create your models here.
class Blog(models.Model):
    title = models.TextField()
    content = models.TextField()
    slug = models.SlugField()


class Category(models.Model):
    pass
