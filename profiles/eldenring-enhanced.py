"""
Elden Ring Modding

Elden Ring Enhanced profile launcher.
"""

from pathlib import Path
from profile import Profile

Profile(Path(__file__).stem).launch()
