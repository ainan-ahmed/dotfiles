import subprocess
from libqtile.lazy import lazy
from libqtile import qtile


@lazy.function
def toggle_program(qtile, program):
    return_code = subprocess.run(["pgrep", program]).returncode
    qtile.spawn(program) if return_code == 1 else subprocess.run(["killall", program])


def power():
    qtile.spawn("sh -c ~/.config/rofi/scripts/powermenu.sh")
