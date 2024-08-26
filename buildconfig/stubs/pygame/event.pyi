from __future__ import annotations

from typing import Any, Protocol

from pygame.typing import SequenceLike

# TODO: Should this be moved to "pygame.typing"?

class _EventLike(Protocol):
    def __init__(
        self, type: int, dict: dict[str, Any] | None = None, **kwargs: Any
    ) -> None: ...
    def __getattribute__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def __int__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...

    @property
    def type(self) -> int: ...
    @property
    def dict(self) -> dict[str, Any]: ...


class Event(_EventLike):
    ...

_EventTypes = int | SequenceLike[int]

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
