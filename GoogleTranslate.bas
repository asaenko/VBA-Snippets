Sub GoogleTranslate()
Rem https://translate.google.ru/?hl=en&tab=wT#es/en/certificado%20de%20calificaciones
    Dim URL As String
    Dim url_start As String
    Dim search_term As String
    
    url_start = "https://translate.google.ru/?hl=en&tab=wT#en/es/"
    search_term = Selection
    URL = url_start + search_term
    ThisDocument.FollowHyperlink Address:=URL

End Sub