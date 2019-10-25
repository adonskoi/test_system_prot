import os, time
from pathlib import Path


from .base import BaseCase


class FirstCase(BaseCase):
    def __init__(self, tc_id, name, time=time.time()):
        super().__init__(tc_id, name)
        self.time = time

    def prep(self):
        if int(self.time) % 2 != 0:
            raise Exception("unix time  % 2 != 0")
        else:
            return "ok"

    def run(self):
        return os.listdir(Path.home())

    def clean_up(self):
        return "ok"
