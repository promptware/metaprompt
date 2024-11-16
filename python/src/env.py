class Env(dict):

    def __init__(self, *args, **kwargs):
        self.env = dict(*args, **kwargs)

    def set(self, variable, value):
        self.env[variable] = value

    def get(self, variable):
        if variable in self.env:
            return self.env[variable]
        else:
            return None
