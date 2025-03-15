import threading
import time
from typing import Callable


class Timer:
    def __init__(self, on_end: Callable[[], None], seconds: float):
        self._on_end = on_end
        self._seconds = seconds

    def start(self) -> None:
        thread = threading.Thread(target=_start_timer, args=(self._on_end, self._seconds))
        thread.start()


def _start_timer(on_end: Callable[[], None], seconds: float):
    time.sleep(seconds)
    on_end()
