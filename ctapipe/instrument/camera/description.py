"""
Classes pertaining to the description of a Cherenkov camera
"""

from .geometry import CameraGeometry
from .readout import CameraReadout

__all__ = ["CameraDescription"]


class CameraDescription:
    """
    Describes a Cherenkov camera and its associated
    `~ctapipe.instrument.CameraGeometry` and `~ctapipe.instrument.CameraReadout`

    Parameters
    ----------
    camera_name: str
        Camera name (e.g. NectarCam, LSTCam, ...)
    geometry: CameraGeometry
       The pixel geometry of this camera
    readout: CameraReadout
       The readout properties for this camera
    """

    def __init__(self, camera_name, geometry: CameraGeometry, readout: CameraReadout):

        self.camera_name = camera_name
        self.geometry = geometry
        self.readout = readout

    def __hash__(self):
        """Make this hashable, so it can be used as dict keys or in sets"""
        return hash((self.geometry, self.readout))

    def __eq__(self, other):
        return self.geometry == other.geometry and self.readout == other.readout

    def __str__(self):
        return f"{self.camera_name}"

    def __repr__(self):
        return "{}(camera_name={}, geometry={}, readout={})".format(
            self.__class__.__name__,
            self.camera_name,
            str(self.geometry),
            str(self.readout),
        )
