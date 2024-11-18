class Assignment(str):
    """A str subclass that allows to yield info about variable assignments,
    that can be used to dispatch output. For example, "ROLE" variable
    assignments can be used to convert a text stream into a stream of
    messages tagged with roles
    """
    def __init__(self, name, value):
        super().__init__()
        self.name = name
        self.value = value

    def __new__(cls, name, value):
        return super().__new__(cls)
