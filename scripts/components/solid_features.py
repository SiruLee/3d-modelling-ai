from py.scripts.components.component import Component
from py.scripts.components.curve import Curve


class Feature(Component):
    def __init__(self, name):
        super().__init__(name)


class BoxFeature(Feature):
    """
    The class that defines the feature of a Box object
    """
    def __init__(self, name: str, length: float, width: float, height: float):
        """
        :param name: The name of the object of this feature
        :param length: the length of the Box object
        :param width: the width of the Box object
        :param height: the height of the Box object
        """
        super().__init__(name)
        self.length = length
        self.width = width
        self.height = height


class CylinderFeature(Feature):
    """
    The class that defines the feature of a Cylinder object
    """
    def __init__(self, name: str, diameter: float, height: float):
        """
        :param name: The name of the object of this feature
        :param diameter: the diameter of the Cylinder object
        :param height: the height of the Cylinder object
        """
        super().__init__(name)
        self.diameter = diameter
        self.height = height


class SphereFeature(Feature):
    """
    The class that defines the feature of a Sphere object
    """
    def __init__(self, name: str, diameter: float):
        """
        :param name: The name of the object of this feature
        :param diameter: the diameter of the Sphere object
        """
        super().__init__(name)
        self.diameter = diameter


class TorusFeature(Feature):
    """
    The class that defines the feature of a Torus object
    """

    def __init__(self, name: str, major: float, minor: float):
        """
        :param name: the name of the object of this feature
        :param major: the major diameter of the Torus object
        :param minor: the minor diameter of the Torus object
        """
        super().__init__(name)
        self.major = major
        self.minor = minor


class CoilFeature(Feature):
    """
    The class that defines the feature of a Coil object
    """
    def __init__(self, name: str, diameter: float, revolutions: float, height: float, angle: float, section_size: float):
        """
        :param name: the name of the object of this feature
        :param diameter: the major diameter of the Coil object
        :param revolutions: the number of revolutions of the Coil object
        :param height: the height of the Coil object
        :param angle: the angle of the Coil object
        :param section_size: the section diameter of the Coil object
        """
        super().__init__(name)
        self.diameter = diameter
        self.revolutions = revolutions
        self.height = height
        self.angle = angle
        self.section_size = section_size


class PipeFeature(Feature):
    """
    The class that defines the feature of a Pipe object
    """

    def __init__(self, name: str, diameter: float, curve: Curve):
        """
        :param name: the name of the object of this feature
        :param diameter: the major diameter of the Pipr object
        :param curve: the curve on which the Pipe object is drawn
        """
        super().__init__(name)
        self.diameter = diameter
        self.curve = curve
