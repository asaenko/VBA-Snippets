Dim objFSO, objFileCopy
Dim strDestination, UserString
Dim shell

Set WSHShell = CreateObject("WScript.Shell")
Set WSHNetwork = CreateObject("WScript.Network")
UserString = WSHNetwork.UserName

strDestination = "C:\Documents and Settings\" & UserString & "\Application Data\Microsoft\Word\STARTUP\TransToolz.dotm"

Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFileCopy = objFSO.GetFile("TransToolz.dotm")
objFileCopy.Copy (strDestination)

set shell=createobject("wscript.shell")
shell.run "Readme.htm"
