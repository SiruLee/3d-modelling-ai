from py.scripts.components.component import Component
from py.scripts.components.curve.curve_features import *


class Curve(Component):
    """
    The class that defines solid objects
    """

    def __init__(self, name: str):
        super().__init__(name)


class Arc(Curve):
    """
    The class that defines Arc in Fusion360
    """

    def __init__(self, name: str, feature: ArcFeature):
        """
        :param name: the name of this Arc object
        :param feature: the feature (center, start, end) of this Arc object
        """
        super().__init__(name)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def get_feature(self) -> tuple[float, float, float]:
        """
        :return: center, start, end of this Box object
        """
        return self.feature.center, self.feature.start, self.feature.end

    def create(self, api):
        # TODO
        pass


class Circle(Curve):
    """
    The class that defines Circle in Fusion360
    """

    def __init__(self, name: str, feature: CircleFeature):
        """
        :param name: the name of this Circle object
        :param feature: the feature (center, radius) of this Circle object
        """
        super().__init__(name)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def get_feature(self) -> tuple[float, float]:
        """
        :return: center, radius of this Circle object
        """
        return self.feature.center, self.feature.radius

    def create(self, api):
        # TODO
        pass


class Ellipse(Curve):
    """
    The class that defines Ellipse in Fusion360
    """

    def __init__(self, name: str, feature: EllipseFeature):
        """
        :param name: the name of this Ellipse object
        :param feature: the feature (center, major, point) of this Ellipse object
        """
        super().__init__(name)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def get_feature(self) -> tuple[float, float, float]:
        """
        :return: center, major, point of this Ellipse object
        """
        return self.feature.center, self.feature.major, self.feature.point

    def create(self, api):
        # TODO
        pass


class Line(Curve):
    """
    The class that defines Line in Fusion360
    """

    def __init__(self, name: str, feature: LineFeature):
        """
        :param name: the name of this Line object
        :param feature: the feature (start, end) of this Line object
        """
        super().__init__(name)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def get_feature(self) -> tuple[float, float]:
        """
        :return: start, end of this Line object
        """
        return self.feature.start, self.feature.end

    def create(self, api):
        # TODO
        pass
