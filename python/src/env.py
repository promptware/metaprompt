class Env:

    def __init__(self, env={}, parent=None):
        self.env = env
        self.parent = parent

    def set(self, variable, value):
        self.env[variable] = value

    def get(self, variable):
        if variable in self.env:
            return self.env[variable]
        elif self.parent is not None:
            self.parent.lookup(variable)
        else:
            return None
