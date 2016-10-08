import commands
dumpsys_output=commands.getstatusoutput('adb reboot')
print dumpsys_output
