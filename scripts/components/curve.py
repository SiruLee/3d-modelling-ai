from py.scripts.components.component import Component


class Curve(Component):
    """
    The class that defines solid objects
    """

    def __init__(self, name: str):
        super().__init__(name)


class Arc(Curve):
    """
    The class that defines Arc objects
    """
    def __init__(self, name: str, origin: tuple[float, float, float]):
        super().__init__(name)
        self.origin = origin


