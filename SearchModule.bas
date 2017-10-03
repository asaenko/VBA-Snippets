Public Function Search(ByVal flag As String)
    Dim retval
    Dim py As String, arg As String, command As String
    Set gShell = CreateObject("WScript.Shell")
    py = "c:\Program Files (x86)\Python36-32\pythonw.exe" 'Python path
    module = "d:\Jobz\Dropbox\Scripts\VBA-Snippets\multisearch.py" 'module name
    arg = Replace(Selection.Text, vbNewLine, "", , , vbTextCompare) 'new line stripping
    arg = flag + " " + arg
    command = py + " " + module + " " + arg 'assemble the query
    'MsgBox (command)
    gShell.exec (command)
End Function

Sub Google()
    search_flag = "Google"
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

Sub LingueeEs()
    search_flag = "LingueeEsEn"
    Search (search_flag)
End Sub


Sub LingueeFr()
    search_flag = "LingueeFrEn"
    Search (search_flag)
End Sub
