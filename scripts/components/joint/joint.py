from py.scripts.components.component import Component


class Joint(Component):
    """
    The class that defines joint objects
    """

    def __init__(self, name: str, tp: str, between: tuple[Component, Component]):
        super().__init__(name)
        assert tp.lower() in ["ball", "cylindrical", "pinslot", "planar", "revolute", "rigid",
                              "slider"], "invalid joint type"
        self.type = tp

    def unpack_feature(self):
        pass

    def create(self, api):
        pass
