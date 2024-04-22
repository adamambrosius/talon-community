not mode: sleep
-
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    user.gdb_disable()
^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
^mixed mode$:
  mode.disable("sleep")
  mode.enable("dictation")
  mode.enable("command")

^sleep all [<phrase>]$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()


^talon sleep [<phrase>]$: speech.disable()
^drowse [<phrase>]$: speech.disable()
^drowze [<phrase>]$: speech.disable()