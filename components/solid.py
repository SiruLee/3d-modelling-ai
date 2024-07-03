from py.components.solid_features import *


class Solid(Component):
    """
    The class that defines solid objects
    """

    def __init__(self, name: str, origin: tuple[float, float, float]):
        super().__init__(name)
        self.origin = origin
        self.has_hole = False

    def unpack_feature(self):
        raise NotImplementedError("Implement unpack_feature")


class Box(Solid):
    """
    The class that defines Box in Fusion360
    """
    def __init__(self, name: str, origin: tuple[float, float, float], feature: BoxFeature):
        """
        :param name: the name of this Box object
        :param origin: the origin of the Box object
        :param feature: the feature (length, width, height) of this Box object
        """
        super().__init__(name, origin)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def get_feature(self) -> tuple[float, float, float]:
        """
        :return: length, width, height of this Box object
        """
        return self.feature.length, self.feature.width, self.feature.height

    def create(self, api):
        pass


class Cylinder(Solid):
    """
    The class that defines Cylinder in Fusion360
    """
    def __init__(self, name: str, origin: tuple[float, float, float], feature: CylinderFeature):
        """
        :param name: the name of this Cylinder object
        :param origin: the origin of the Cylinder object
        :param feature: the feature (diameter, height) of the Cylinder object
        """
        super().__init__(name, origin)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def unpack_feature(self) -> tuple[float, float]:
        """
        :return: the diameter and the height of this Cylinder object
        """
        return self.feature.diameter, self.feature.height

    def create(self, api):
        pass


class Sphere(Solid):
    """
    The class that defines Sphere in Fusion360
    """

    def __init__(self, name: str, origin: tuple[float, float, float], feature: SphereFeature):
        """
        :param name: the name of this Sphere object
        :param origin: the origin of the Sphere object
        :param feature: the feature (diameter) of the Sphere object
        """
        super().__init__(name, origin)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def unpack_feature(self) -> float:
        """
        :return: the diameter of the Sphere object
        """
        return self.feature.diameter

    def create(self, api):
        pass


class Torus(Solid):
    """
    The class that defines Torus in Fusion360
    """
    def __init__(self, name: str, origin: tuple[float, float, float], feature: TorusFeature):
        """
        :param name: the name of this Torus object
        :param origin: the origin of the Torus object
        :param feature: the feature (major diameter, minor diameter) of the Torus object
        """
        super().__init__(name, origin)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def unpack_feature(self) -> tuple[float, float]:
        """
        :return: the major diameter and the minor of the Torus object
        """
        return self.feature.major, self.feature.minor

    def create(self, api):
        pass


class Coil(Solid):
    """
    The class that defines Coil in Fusion360
    """
    def __init__(self, name: str, origin: tuple[float, float, float], feature: CoilFeature):
        """
        :param name: the name of this Coil object
        :param origin: the origin of the Coil object
        :param feature: the feature (diameter, revolution, height, angle, section_size) of the Coil object
        """
        super().__init__(name, origin)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def unpack_feature(self) -> tuple[float, float, float, float, float]:
        """
        :return: the diameter, number of revolutions, height, angle, and section diameter of the Coil object
        """
        return (self.feature.diameter, self.feature.revolutions, self.feature.height,
                self.feature.angle, self.feature.section_size)

    def create(self, api):
        pass


class Pipe(Solid):
    """
    The class that defines Pipe in Fusion360
    """
    def __init__(self, name: str, origin: tuple[float, float, float], feature: PipeFeature):
        """
        :param name: the name of this Pipe object
        :param origin: the origin of the Pipe object
        :param feature: the feature of the Pipe object
        """
        super().__init__(name, origin)
        assert name == feature.name, "The feature name should match the object name"
        self.feature = feature

    def unpack_feature(self) -> tuple[float, Curve]:
        """
        :return: the diameter and the basis curve of the Pipe object
        """
        return self.feature.diameter, self.feature.curve

    def create(self, api):
        pass
