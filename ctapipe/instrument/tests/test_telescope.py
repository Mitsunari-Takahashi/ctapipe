""" Tests for TelescopeDescriptions """


def test_hash(subarray_prod5_paranal):
    assert len(subarray_prod5_paranal) == 180
    assert len(set(subarray_prod5_paranal.tel.values())) == 4
