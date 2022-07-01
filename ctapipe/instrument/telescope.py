"""
Classes pertaining to the description of a Cherenkov Telescope
"""
from .camera import CameraDescription
from .optics import OpticsDescription


__all__ = ["TelescopeDescription"]


class TelescopeDescription:
    """
    Describes a Cherenkov Telescope and its associated
    `~ctapipe.instrument.OpticsDescription` and `~ctapipe.instrument.CameraDescription`

    Attributes
    ----------
    name: str
        Telescope name
    tel_type: str
        Telescope type
    optics: OpticsDescription
       the optics associated with this telescope
    camera: CameraDescription
       the camera associated with this telescope
    """

    def __init__(
        self,
        name: str,
        tel_type: str,
        optics: OpticsDescription,
        camera: CameraDescription,
    ):

        if not isinstance(name, str):
            raise TypeError("`name` must be a str")

        if not isinstance(tel_type, str):
            raise TypeError("`tel_type` must be a str")

        if not isinstance(optics, OpticsDescription):
            raise TypeError("`optics` must be an instance of `OpticsDescription`")

        if not isinstance(camera, CameraDescription):
            raise TypeError("`camera` must be an instance of `CameraDescription`")

        self.name = name
        self.type = tel_type
        self.optics = optics
        self.camera = camera

    def __hash__(self):
        """Make this hashable, so it can be used as dict keys or in sets"""
        return hash((self.optics, self.camera))

    def __eq__(self, other):
        return self.optics == other.optics and self.camera == other.camera

    def __str__(self):
        return f"{self.type}_{self.optics}_{self.camera}"

    def __repr__(self):
        return "{}(type={}, name={}, optics={}, camera={})".format(
            self.__class__.__name__,
            self.type,
            self.name,
            str(self.optics),
            str(self.camera),
        )
