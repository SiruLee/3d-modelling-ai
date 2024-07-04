from py.scripts.components.feature import Feature
from py.scripts.components.curve.curve import Curve


class ArcFeature(Feature):
    """
    The class that defines the feature of a Arc object
    """

    def __init__(self, name: str, center: tuple[float, float, float], start: tuple[float, float, float], end: tuple[float, float, float]):
        """
        :param name: The name of the object of this feature
        :param center: the center of the Arc object
        :param start: the start of the Arc object
        :param end: the end of the Arc object
        """
        super().__init__(name)
        self.center = center
        self.start = start
        self.end = end


class EllipseFeature(Feature):
    """
    The class that defines the feature of a Ellipse object
    """

    def __init__(self, name: str, center: tuple[float, float, float], major: float, point: tuple[float, float, float]):
        """
        :param name: The name of the object of this feature
        :param center: the center of the Ellipse object
        :param major: the major diameter of the Ellipse object
        :param point: the point that the Ellipse object passes through
        """
        super().__init__(name)
        self.center = center
        self.major = major
        self.point = point


class CircleFeature(Feature):
    """
    The class that defines the feature of a Circle object
    """

    def __init__(self, name: str, center: tuple[float, float, float], radius: float):
        """
        :param name: The name of the object of this feature
        :param center: the center of the Circle object
        :param radius: the radius of the Circle object
        """
        super().__init__(name)
        self.center = center
        self.radius = radius


class LineFeature(Feature):
    """
    The class that defines the feature of a Line object
    """

    def __init__(self, name: str, start: tuple[float, float, float], end: tuple[float, float, float]):
        """
        :param name: the name of the object of this feature
        :param start: the start point of the Line object
        :param end: the end point of the Line object
        """
        super().__init__(name)
        self.start = start
        self.end = end
