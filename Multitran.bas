 Private Function checksel()
   If WordBasic.GetSelStartPos() = WordBasic.GetSelEndPos() Then
        checksel = 0
     Else
        checksel = 1
     End If
 End Function
 
Sub mul()
 Dim RetVal
 If checksel = 0 Then
     WordBasic.SelectCurWord
 End If

 If checksel = 1 Then
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
