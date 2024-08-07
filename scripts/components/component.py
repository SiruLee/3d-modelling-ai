import adsk.core, adsk.fusion
from adsk.core import Application
class Component:
    """
    The class that defines objects in Fusion360, such as solids, curves, holes, and joints.
    """
    def __init__(self, name: str):
        self.name = name

    def create(self, api: Application):
        raise NotImplementedError("Implement creation method")


