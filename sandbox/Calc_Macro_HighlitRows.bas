
' Dieses Makro durchsucht alle Zellen in der Tabelle und prüft, ob das Sheet Sonderzeichen "#" in der Zelle vorhanden ist.
' Wenn ja, wird die gesamte Zeile, in der sich die Zelle befindet, eingefärbt und die Schrift fett gemacht.
 
' Um dieses Makro zu verwenden, speichern Sie es einfach als .bas-Datei ab und fügen Sie es dann als Makro 
' in Ihre LibreOffice Calc-Datei ein. Anschließend können Sie es über das Makro-Menü oder über eine 
' benutzerdefinierte Schaltfläche ausführen.


Sub HighlightRows2()
    ' Definieren der Variablen
    Dim Sheet As Object
    Dim Range As Object
    Dim Cell As Object
    Dim Text As String

 
    Dim titel1Symbol As String
    Dim titel2Symbol As String
    Dim titel3Symbol As String
    
    ' Definieren des zu erkennenden Symbols
    titel1Symbol = "#"
    titel2Symbol = "##"
    titel3Symbol = "###"
    
    ' Zugreifen auf das aktive Arbeitsblatt
    Sheet = ThisComponent.CurrentController.ActiveSheet

    Dim rowInd As Integer
    rowInd = 0
    For j = 0 To Sheet.Rows.Count - 1
        Cell = Sheet.getCellByPosition(0, j)
        Text = Cell.getString()
        If InStr(Text, titel3Symbol) > 0 Then
            Text = Replace(Text, titel3Symbol, "")
            Cell.setString(Text)

            Range = Sheet.getRows().getByIndex(j)
            Range.CharWeight = com.sun.star.awt.FontWeight.BOLD
            Range.CellBackColor = RGB(255, 255, 0) ' Farbe: Gelb
        ElseIf InStr(Text, titel2Symbol) > 0 Then
            Text = Replace(Text, titel2Symbol, "")
            Cell.setString(Text)

            Range = Sheet.getRows().getByIndex(j)
            Range.CharWeight = com.sun.star.awt.FontWeight.BOLD
            Range.CellBackColor = RGB(255, 0, 255) ' Farbe: Gelb
        ElseIf InStr(Text, titel1Symbol) > 0 Then
            Text = Replace(Text, titel1Symbol, "")
            Cell.setString(Text)

            Range = Sheet.getRows().getByIndex(j)
            Range.CharWeight = com.sun.star.awt.FontWeight.BOLD
            Range.CellBackColor = RGB(0, 0, 255) ' Farbe: Gelb
        End If
        ' rowInd = rowInd + 1
    Next

End Sub
