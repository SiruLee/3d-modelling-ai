from py.scripts.components.feature import Feature


class SimpleFeature(Feature):
    """
    The class that defines the feature of a Simple hole object
    """

    def __init__(self, name: str, diameter: float):
        """
        :param name: The name of the object of this feature
        :param diameter: the diameter of the Simple hole object
        """
        super().__init__(name)
        self.diameter = diameter


class CounterboreFeature(Feature):
    """
    The class that defines the feature of a Counterbore hole object
    """

    def __init__(self, name: str, diameter: float, cb_diameter: float, cb_depth: float):
        """
        :param name: The name of the object of this feature
        :param diameter: the diameter for the Counterbore hole object
        :param cb_diameter: the counterbore diameter of the Counterbore hole object
        :param cb_depth: the depth of the Counterbore hole object
        """
        super().__init__(name)
        self.diameter = diameter
        self.cb_diameter = cb_diameter
        self.cb_depth = cb_depth


class CountersinkFeature(Feature):
    """
    The class that defines the feature of a Countersink hole object
    """

    def __init__(self, name: str, diameter: float, cs_diameter: float, angle):
        """
        :param name: The name of the object of this feature
        :param diameter: the diameter of the Countersink hole object
        :param cs_diamter: the countersink diameter of the Countersink hole object
        :param angle: the angle of the Countersink hole object
        """
        super().__init__(name)
        self.diameter = diameter
        self.cs_diameter = cs_diameter
        self.angle = angle
