Attribute VB_Name = "DateConverter"
Public Function convert_date(ByVal dt As String) As String
'
' Convert date from EU to US and vice versa
'

Dim split_date() As String
Dim sep As String

If InStr(dt, ".") Then sep = "."
If InStr(dt, "/") Then sep = "/"
If InStr(dt, "-") Then sep = "-"

split_date = Split(dt, sep)
convert_date = split_date(1) + sep + split_date(0) + sep + split_date(2)

End Function

Sub ConvertDates()
Dim dates() As String
Dim replacement As String
Dim regExp As Object
Dim logFile As String

logFile = ActiveDocument.Path + "\changes.txt"
Set regExp = CreateObject("vbscript.regexp")
Open logFile For Output As #1

With regExp
    .pattern = "(\d[\d])([\./-])(\d[\d])[\./-](\d+)"
    .Global = True
    If .Test(ActiveDocument.Content) Then
        Set regExp_Matches = .Execute(ActiveDocument.Content)
    End If
End With

For Each Match In regExp_Matches
    Selection.Find.ClearFormatting
    Selection.Find.replacement.ClearFormatting
    s = Match & " -> " & convert_date(Match) & Chr(13) & Chr(10)
    Print #1, s
    With Selection.Find
        .Text = Match
        .replacement.Text = convert_date(Match)
        .Forward = True
        .Wrap = wdFindContinue
        .Format = False
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
    End With
    Selection.Find.Execute Replace:=wdReplaceAll
Next
Close #1

End Sub

