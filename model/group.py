import random



class Group:

    def __init__(self, name=None):
        self.name = name or ''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8))