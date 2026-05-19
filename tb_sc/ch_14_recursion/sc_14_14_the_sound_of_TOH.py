# file: sc_14_14_the_sound_of_TOH.py
"""Tower of Hanoi with per-disk sounds."""

from __future__ import annotations

import time
from typing import Callable, Sequence


def _default_play_sound(freq_hz: int, duration_ms: int = 200) -> None:
    try:
        import winsound

        winsound.Beep(freq_hz, duration_ms)
    except Exception:
        print(f"[sound] {freq_hz} Hz for {duration_ms} ms")


def _ensure_sounds(sounds: Sequence[int], n: int) -> list[int]:
    if n < 1:
        return [0]

    if not sounds:
        sounds = [0, 440]

    if sounds[0] != 0:
        sounds = [0, *sounds]

    result = list(sounds)
    if len(result) <= n:
        # Extend using a major scale pattern (in semitones).
        major_steps = [2, 2, 1, 2, 2, 2, 1]
        last = result[-1]
        step_index = 0
        while len(result) <= n:
            step = major_steps[step_index % len(major_steps)]
            last = int(round(last * (2 ** (step / 12))))
            result.append(last)
            step_index += 1
    return result


def _key_pressed() -> bool:
    try:
        import msvcrt

        if msvcrt.kbhit():
            _ = msvcrt.getch()
            return True
    except Exception:
        return False
    return False


def _sleep_with_abort(delay_s: float) -> None:
    if delay_s <= 0:
        return

    end_time = time.time() + delay_s
    while time.time() < end_time:
        if _key_pressed():
            raise KeyboardInterrupt
        time.sleep(min(0.05, max(0.0, end_time - time.time())))


def the_sound_of_TOH(
    n: int,
    source: str,
    dest: str,
    helper: str,
    sounds: Sequence[int],
    delay_s: float = 0.5,
    play_sound: Callable[[int], None] | None = None,
    stop_on_keypress: bool = True,
) -> int:
    """Solve Tower of Hanoi and play a sound for each disk move.

    sounds maps disk number -> frequency (index 0 unused).
    If sounds is too short, it will be extended with unique frequencies.
    """
    if play_sound is None:
        play_sound = _default_play_sound

    sounds = _ensure_sounds(sounds, n)

    if stop_on_keypress and _key_pressed():
        raise KeyboardInterrupt

    if n == 1:
        print(f"Move disk 1 from {source} to {dest} - base case")
        play_sound(sounds[1])
        if stop_on_keypress:
            _sleep_with_abort(delay_s)
        else:
            time.sleep(delay_s)
        return 1
    else:
        moves_left = the_sound_of_TOH(
            n - 1,
            source,
            helper,
            dest,
            sounds,
            delay_s,
            play_sound,
            stop_on_keypress,
        )
        print(f"Move disk {n} from {source} to {dest}")
        play_sound(sounds[n])
        if stop_on_keypress:
            _sleep_with_abort(delay_s)
        else:
            time.sleep(delay_s)
        moves_right = the_sound_of_TOH(
            n - 1,
            helper,
            dest,
            source,
            sounds,
            delay_s,
            play_sound,
            stop_on_keypress,
        )
        return moves_left + 1 + moves_right


if __name__ == "__main__":
    # Client code: 5 disks with distinct sounds (frequencies in Hz).
    disk_sounds = [0, 440, 494, 523,  587]
    n_disks = 7 
    try:
        moves = the_sound_of_TOH(n_disks, "A", "C", "B", disk_sounds, delay_s=0.05)
        expected_moves = 2**n_disks - 1
        print(f"Done. Moves: {moves} (expected {expected_moves}).")
    except KeyboardInterrupt:
        print("Interrupted by keypress.")
 