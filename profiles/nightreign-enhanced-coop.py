"""
Elden Ring Modding

NightReign Enhanced profile launcher.
"""

from pathlib import Path
from profile import Profile

Profile(Path(__file__).stem).launch()
