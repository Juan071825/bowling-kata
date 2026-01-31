import pytest
from src.score_counter import frame_dict_creator

@pytest.mark.parametrize(
    "pins_knocked, total_score",
    [
        ("12345123451234512345", "60"),
        ("9-9-9-9-9-9-9-9-9-9-", "90"),
        ("9-3561368153258-7181", "82"),
        ("9-3/613/815/-/8-7/8-", "121"),
        ("X9-9-9-9-9-9-9-9-9-", "100"),
        ("X9-X9-9-9-9-9-9-9-", "110"),
        ("XX9-9-9-9-9-9-9-9-", "120"),
        ("XXX9-9-9-9-9-9-9-", "141"),
        ("9-3/613/815/-/8-7/8/8", "131")
        ("5/5/5/5/5/5/5/5/5/5/5", "150"),
        ("9-9-9-9-9-9-9-9-9-XXX", "111"),
        ("8/549-XX5/53639/9/X", "149"),
        ("X5/X5/XX5/--5/X5/", "175"),
        ("XXXXXXXXXXXX", "300")
    ]
)
def test_score(pins_knocked, total_score):
    assert frame_dict_creator(pins_knocked) == total_score