Attribute VB_Name = "SearchModule"
Public Function Search(ByVal flag As String)
    Dim retval
    Dim py As String, arg As String, command As String
    Set gShell = CreateObject("WScript.Shell")
    py = "c:\Python34\pythonw.exe" 'Python path
    module = "d:\Jobz\Dropbox\Scripts\VBA-Snippets\multisearch.py" 'module name
    arg = Replace(Selection.Text, vbNewLine, "", , , vbTextCompare) 'new line stripping
    arg = flag + arg
    command = py + " " + module + " " + arg 'assemble the query
    gShell.exec (command)
End Function

Sub Google()
    search_flag = "-g "
    Search (search_flag)
End Sub

Sub LingueeDe()
    search_flag = "LingueeDeEn"
    Search (search_flag)
End Sub

Sub LingueeRu()
    search_flag = "LingueeRuEn"
    Search (search_flag)
End Sub