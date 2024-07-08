from py.scripts.components.component import *
from py.scripts.components.hole.hole_features import *
from py.scripts.components.solid.solid import Solid


class Hole(Component):
    """
    The class that defines hole objects
    """

    def __init__(self, name: str, parent: Solid):
        super().__init__(name)
        parent.has_hole = True
        self.on = parent

    def create(self, api: Application):
        pass

class Simple(Hole):
    """
    The class that defines a simple hole
    """

    def __init__(self, name: str, parent: Solid, feature: SimpleFeature):
        """
        :param name: the name of this simple hole object
        :param parent: the parent solid of the simple hole object
        :param feature: the feature (diameter) of this simple hole object
        """
        super().__init__(name, parent)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def unpack_feature(self) -> float:
        """
        :return: diameter of this simple hole
        """
        return self.feature.diameter

    def create(self, api):
        # TODO
        pass


class Counterbore(Hole):
    """
    The class that defines a simple hole
    """

    def __init__(self, name: str, parent: Solid, feature: CounterboreFeature):
        """
        :param name: the name of this counterbore hole object
        :param parent: the parent solid of the counterbore hole object
        :param feature: the feature (diameter, counterbore diameter, counterbore depth) of this counterbore hole object
        """
        super().__init__(name, parent)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def unpack_feature(self) -> tuple[float, float, float]:
        """
        :return: diameter of this simple hole
        """
        return self.feature.diameter, self.feature.cb_diameter, self.feature.cb_depth

    def create(self, api):
        # TODO
        pass


class Countersink(Hole):
    """
    The class that defines a simple hole
    """

    def __init__(self, name: str, parent: Solid, feature: CountersinkFeature):
        """
        :param name: the name of this countersink hole object
        :param parent: the parent solid of the countersink hole object
        :param feature: the feature (diameter, countersink diameter, angle) of this countersink object
        """
        super().__init__(name, parent)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def unpack_feature(self) -> float:
        """
        :return: diameter of this simple hole
        """
        return self.feature.diameter, self.feature.cs_diameter, self.feature.angle

    def create(self, api):
        # TODO
        pass
