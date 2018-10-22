# -*- coding: utf-8 -*-
from builtins import _

from .crypter import Crypter


class DeadCrypter(Crypter):
    __name__ = "DeadCrypter"
    __type__ = "crypter"
    __version__ = "0.14"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"^unmatchable$"
    __config__ = [("enabled", "bool", "Activated", True)]

    __description__ = """Crypter is no longer available"""
    __license__ = "GPLv3"
    __authors__ = [("stickell", "l.stickell@yahoo.it")]

    @classmethod
    def get_info(cls, *args, **kwargs):
        info = super(DeadCrypter, cls).get_info(*args, **kwargs)
        info["status"] = 1
        return info

    def setup(self):
        self.offline(self._("Crypter is no longer available"))