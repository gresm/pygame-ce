from __future__ import annotations

from typing import Any

from ._common import Sequence, EventLike

class Event(EventLike):
    ...

_EventTypes = int | Sequence[int]

def pump() -> None: ...
def get(
    eventtype: _EventTypes | None = None,
    pump: Any = True,
    exclude: _EventTypes | None = None,
) -> list[Event]: ...
def poll() -> Event: ...
def wait(timeout: int = 0) -> Event: ...
def peek(eventtype: _EventTypes | None = None, pump: Any = True) -> bool: ...
def clear(eventtype: _EventTypes | None = None, pump: Any = True) -> None: ...
def event_name(type: int) -> str: ...
def set_blocked(type: _EventTypes | None, *args: int) -> None: ...
def set_allowed(type: _EventTypes | None, *args: int) -> None: ...
def get_blocked(type: _EventTypes, *args: int) -> bool: ...
def set_grab(grab: bool, /) -> None: ...
def get_grab() -> bool: ...
def post(event: Event, /) -> bool: ...
def custom_type() -> int: ...
def init() -> None: ...
def quit() -> None: ...

EventType = Event
