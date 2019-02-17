

class Globals(object):
    """
    Borg singleton config object
    """
    _we_are_one = {

    }

    def __init__(self):
        # implement the borg pattern (we are one)
        self.__dict__ = self._we_are_one

    def set_playtime(self, val):
        self._playtime = val

    def get_playtime(self):
        return getattr(self, '_playtime', None)

    playtime = property(get_playtime, set_playtime)
