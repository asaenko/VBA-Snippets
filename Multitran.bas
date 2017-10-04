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
