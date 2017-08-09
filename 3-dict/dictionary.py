

class Dictionary(object):
    """
    And simple but slow (and broken!) implementation of a dictionary, assuming
    that `dict` disappeared from the language.

    This is just to show you a Python interface... I wouldn't necessarily
    suggest following this approach! The exercise is to devise a better one :)
    """
    def __init__(self):
        self.items = []

    def __getitem__(self, key):
        for k, v in self.items:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        self.items.append((key, value))

    def __len__(self):
        return len(self.items)

    def __contains__(self, key):
        for k, v in self.items:
            if k == key:
                return True
        return False
