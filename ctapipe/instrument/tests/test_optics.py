""" Tests for OpticsDescriptions"""
import pytest
from astropy import units as u

from ctapipe.instrument.optics import OpticsDescription


def test_guess_optics():
    """make sure we can guess an optics type from metadata"""
    from ctapipe.instrument import guess_telescope

    answer = guess_telescope(1855, 28.0 * u.m)

    assert answer.name == "LST"
    assert answer.n_mirrors == 1


def test_construct_optics():
    """create an OpticsDescription and make sure it
    fails if units are missing"""
    OpticsDescription(
        name="test",
        num_mirrors=1,
        num_mirror_tiles=100,
        mirror_area=u.Quantity(550, u.m**2),
        equivalent_focal_length=u.Quantity(10, u.m),
    )

    with pytest.raises(TypeError):
        OpticsDescription(
            name="test",
            num_mirrors=1,
            num_mirror_tiles=100,
            mirror_area=550,
            equivalent_focal_length=10,
        )
