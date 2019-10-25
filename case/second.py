import os, random

from .base import BaseCase


class SecondCase(BaseCase):
    def __init__(self, tc_id, name):
        super().__init__(tc_id, name)
        self.file_dir = "/tmp"
        self.file_name = "test"

    def get_mem():
        mem_b = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")
        mem_gb = mem_b / (1024.0 ** 3)
        return mem_gb

    def prep(self, mem_gb=get_mem()):
        if mem_gb < 1:
            raise Exception("Memory size less then 1 GB")
        return "ok"

    def run(self):
        try:
            os.mkdir(self.file_dir)
        except FileExistsError as e:
            pass
        file_path = f"{self.file_dir}/{self.file_name}"
        with open(file_path, "wb") as f:
            data = bytearray(random.getrandbits(8) for _ in range(1024))
            f.write(data)
        return os.path.getsize(file_path)

    def clean_up(self):
        file_path = f"{self.file_dir}/{self.file_name}"
        try:
            os.remove(file_path)
        except:
            pass
        return "ok"
