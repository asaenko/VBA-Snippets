Public Function SearchOld(ByVal flag As String)
    Dim RetVal
    Dim py As String, arg As String, command As String
    Set gShell = CreateObject("WScript.Shell")
    py = "c:\Program Files (x86)\Python36-32\pythonw.exe" 'Python path
    module = "d:\Jobz\Dropbox\Scripts\VBA-Snippets\multisearch.py" 'module name
    arg = Replace(Selection.Text, vbNewLine, "", , , vbTextCompare) 'new line stripping
    arg = Replace(Selection.Text, "/", "%2F", , , vbTextCompare) 'replacing forward slash to make query address-bar-friendly
    arg = flag + " " + arg
    command = py + " " + module + " " + arg 'assemble the query
    'MsgBox (command)
    gShell.exec (command)
End Function
Public Function Search(ByVal flag As String)
    Dim RetVal
    Dim py As String, arg As String, command As String
    Set gShell = CreateObject("WScript.Shell")
    exe = "d:\Jobz\Dropbox\Code\search\search.exe" 'program name
    arg = Replace(Selection.Text, vbNewLine, "", , , vbTextCompare) 'new line stripping
    arg = Replace(Selection.Text, "/", "%2F", , , vbTextCompare) 'replacing forward slash to make query address-bar-friendly
    arg = flag + " " + arg
    command = exe + " " + arg 'assemble the query
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

Sub GoogleTranslate()
    search_flag = "GoogleTr"
    Search (search_flag)
End Sub

Sub SearchProz()
    search_flag = "Proz"
    Search (search_flag)
End Sub
Private Function selected()
   If WordBasic.GetSelStartPos() = WordBasic.GetSelEndPos() Then
        selected = 0
     Else
        selected = 1
     End If
End Function
 
Sub mul()
 Dim RetVal
 If selected = 0 Then
     WordBasic.SelectCurWord
 End If

 If selected = 1 Then
     WordBasic.EditCopy
 End If

 ' seterror

 For Each myTask In Tasks
     If InStr(myTask.Name, "MultiTran") > 0 Then
         myTask.Activate
         myTask.WindowState = wdWindowStateNormal
         GoTo Label1
     End If
 Next myTask
RetVal = Shell("C:\mt\network\multitran.exe", 1)
Label1:
End Sub

Sub SublimeEdit()
    Dim RetVal
    Dim py As String, txt As String, command As String
    Set gShell = CreateObject("WScript.Shell")
    py = "c:\Program Files (x86)\Python36-32\pythonw.exe" 'Python path
    module = "d:\Jobz\Dropbox\Scripts\VBA-Snippets\sublime_call.py" 'module name
    txt = Selection.Text
    'arg = Replace(Selection.Text, vbNewLine, "", , , vbTextCompare) 'new line stripping
    'arg = Replace(Selection.Text, "/", "%2F", , , vbTextCompare) 'replacing forward slash to make query address-bar-friendly
    command = py + " " + module + " " + txt 'assemble the query
    MsgBox (command)
    'gShell.exec (command)
End Sub
