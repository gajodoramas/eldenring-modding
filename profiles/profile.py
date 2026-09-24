
"""
Elden Ring Modding

Profile module.
"""

from pathlib import Path
import subprocess
import sys


ROOT = Path(sys.executable).parent.parent \
    if getattr(sys, "frozen", False) \
        else Path(__file__).parent.parent


class Profile:
    __name: str
    __filepath: Path

    def __init__(self, name: str):
        self.__name = name
        self.__filepath = ROOT / "profiles" / f"{self.__name}.me3"
        game, extension, *words = self.__name.split("-")
        if "coop" in words:
            self._set_savegame_extension(game, extension)

    def _set_savegame_extension(self, game: str, extension: str):
        coop_config_filepath = ROOT / "mods" / game / "seamless-coop" / f"{game[0]}rsc_settings.ini"
        lines = []
        for line in coop_config_filepath.read_text(encoding="utf-8").splitlines():
            if line.strip().lower().startswith("save_file_extension"):
                lines.append(f"save_file_extension = {extension}")
            else:
                lines.append(line)
        coop_config_filepath.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def launch(self):
        subprocess.run(
            ["engine\\me3.exe", "launch", "--profile", self.__filepath],
            cwd=ROOT,
            shell=True
        )
