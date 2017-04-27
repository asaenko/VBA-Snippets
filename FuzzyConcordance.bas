Attribute VB_Name = "FuzzyConcordance"
Public Function ShellRun(sCmd As String) As String

    'Run a shell command, returning the output as a string'
    'Borrowed this function on the Internet

    Dim oShell As Object
    Set oShell = CreateObject("WScript.Shell")

    'run command'
    Dim oExec As Object
    Dim oOutput As Object
    Set oExec = oShell.Exec(sCmd)
    Set oOutput = oExec.StdOut

    'handle the results as they are written to and read from the StdOut object'
    Dim s As String
    Dim sLine As String
    While Not oOutput.AtEndOfStream
        sLine = oOutput.ReadLine
        If sLine <> "" Then s = s & sLine & vbCrLf
    Wend

    ShellRun = s

End Function

Public Function StripNL(s As String) As String
    'Remove the new line from a string.
    s = Replace(s, vbNewLine, "", , , vbTextCompare)
    StripNL = s
    
End Function


Public Function StemmedContexts() As String
    'Stem words in the Selection string using a python script with NLTK import
    'TODO: the name of the script is hard-coded, so is the pythonw.exe path. Improve!
    Dim lng As String
    Dim retval
    Dim py As String, arg As String, command As String
    
    'It is highly recommended to select the expression to search in the source segment
    'to ensure that the LanguageID is determined correctly
    If Selection.LanguageID = wdEnglishAUS Or Selection.LanguageID = wdEnglishUK Or Selection.LanguageID = wdEnglishUS Then
        lng = "en"
    ElseIf Selection.LanguageID = wdRussian Then
        lng = "ru"
    Else
        lng = "na"
    End If
    
    py = "c:\Users\SS\Anaconda3\pythonw.exe"
    module = "c:\Users\SS\Anaconda3\Scripts\stem.pyw"
    arg = StripNL(Selection.Text)
    command = py + " " + module + " " + arg + " " + lng
    StemmedContexts = ShellRun(command)
    
End Function

Sub ContextSearch()
    'Main macro
    Dim origStr As String
    Dim trDoc As String
    
    trDoc = ActiveDocument.Name
    origStr = Selection.Text
    Selection.Text = StripNL(StemmedContexts())
    Application.Run "Wordfast.M0.WfContexts"
    Documents(trDoc).Undo
    
End Sub


