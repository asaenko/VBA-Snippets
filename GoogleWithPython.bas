VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ThisDocument"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Sub GoogleWithPython()
    Dim retval
    Dim py As String, arg As String, command As String
    Set gShell = CreateObject("WScript.Shell")
    
    py = "c:\Python34\python.exe" 'Python path
    module = "d:\Jobz\Dropbox\Scripts\VBA-Snippets\multisearch.py" 'module name
    arg = Replace(Selection.Text, vbNewLine, "", , , vbTextCompare) 'new line stripping
    arg = "-g " + arg
    command = py + " " + module + " " + arg 'assemble the query
    gShell.exec (command)
    
End Sub
