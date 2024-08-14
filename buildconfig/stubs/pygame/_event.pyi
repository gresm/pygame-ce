from __future__ import annotations

from ._common import Sequence, EventLike

_EventTypes = int | Sequence[int]

def pump(dopump: bool, /) -> None: ...
def get(
    eventtype: _EventTypes | None = None,
    pump: bool = True,
    exclude: _EventTypes | None = None,
) -> list[EventLike]: ...
def poll() -> EventLike: ...
def wait(timeout: int = 0) -> EventLike: ...
def peek(eventtype: _EventTypes | None = None, pump: bool = True) -> bool: ...
def clear(eventtype: _EventTypes | None = None, pump: bool = True) -> None: ...
def set_grab(grab: bool, /) -> None: ...
def get_grab() -> bool: ...
def allowed_get(type: int, /) -> bool: ...
def allowed_set(type: int, val: bool, /) -> None: ...
def post(event: EventLike, /) -> bool: ...
def register_event_class(cls: type[EventLike]) -> None: ...
def _internal_mod_init() -> None: ...
def _internal_mod_quit() -> None: ...
