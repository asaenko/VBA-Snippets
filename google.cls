VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ThisDocument"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Sub GoogleSearch()

    Dim URL As String
    Dim url_start As String
    Dim search_term As String
    Dim url_end As String
    
    url_start = "http://www.google.com/search?q=%22"
    search_term = Selection
    url_end = "%22&btnG=Google+Search"
    URL = url_start + search_term + url_end
    ThisDocument.FollowHyperlink Address:=URL

End Sub
