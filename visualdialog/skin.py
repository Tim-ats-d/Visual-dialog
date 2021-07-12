
from typing import Dict, Literal, NamedTuple


TextBoxSkin = Dict[Literal[str], str]


classic: TextBoxSkin = {
    "upper_corner": "+",
    "side": "|"
}

class Skin(NamedTuple):
    upper_corner: str
    lower_corner: str = "%"


p = Skin("t")._asdict()
classic.update(p)
print(classic)
