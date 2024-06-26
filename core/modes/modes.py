from talon import Context, Module, actions, app, speech_system

mod = Module()
ctx_sleep = Context()
ctx_awake = Context()

modes = {
    "admin": "enable extra administration commands terminal (docker, etc)",
    "debug": "a way to force debugger commands to be loaded",
    "ida": "a way to force ida commands to be loaded",
    "presentation": "a more strict form of sleep where only a more strict wake up command works",
}

for key, value in modes.items():
    mod.mode(key, value)

ctx_sleep.matches = r"""
mode: sleep
"""

ctx_awake.matches = r"""
not mode: sleep
"""


@ctx_sleep.action_class("speech")
class ActionsSleepMode:
    def disable():
        actions.app.notify("Talon is already asleep")


@ctx_awake.action_class("speech")
class ActionsAwakeMode:
    def enable():
        actions.app.notify("Talon is already awake")
