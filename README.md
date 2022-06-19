<h1>Quiz-World</h1>

<h3>Motivation</h3>
<p>Als Projektarbeit habe ich ein Quiz-Game Programm erstellt. Ich habe mich für ein Quiz entschieden, da für mich der Ablauf und die Nutzung klar ist. Ich musste mir nicht wirklich mathematische Hintergedanken machen. Für mich war es wichtig, dass ich etwas erstelle, das für mich logisch ist und ich keine Zeit verschwende mit dem ganzen Ablauf der Struktur sondern, dass ich mich aufs eigentliche Programmieren konzentrieren kann.</p>

<h3>Projektbeschreibung</h3>
<p>Bei diesem Spiel gibt es drei verschiedene Kategorien. Ich habe mich für 'Geographie', 'Kunst-Kultur', 'Bücher, Filme & TV-Serien' entschieden. Bei jeder Frage gibt es vier Antwortmöglichkeiten, bei der es eine richtige Antwort gibt. Wenn man seinen Username und die gewünschte Kategorie ausgewählt hat, kann man das Quiz starten. Alle Fragen werden auf einer Seite angezeigt und rechts davon gibt es ein Dropdown Feld. Bei diesem werden die vier Antwortmöglichkeiten angezeigt und man kann eine Antwort auswählen. Wenn man alle Fragen durchgearbeitet hat, kann man auf "Antworten eintragen" drücken und danach "Auswertung anzeigen". Ich habe die Auswertung so strukturiert, dass die Punktezahl oben steht. Unten werden die Fragen angezeigt, die richtig beantwortet wurden. Und folgend werden alle Fragen angezeigt, welche man falsch beantwortet hat. Dazu werden noch die richtigen Antworten unten angezeigt. Wenn man ein neues Quiz beginnen möchte, kann man auf "alle Daten zurücksetzen" klicken und danach "quiz neu starten". Zu unterst auf der Seite habe ich noch eine Tabelle eingebaut, wo der Username des Spielers angezeigt wird, sowie die ausgewählte Kategorie und die erreichte Punktezahl.</p>

<h3>Betrieb/Benutzung</h3>
<h5>- Welche zussätzliche Pakete müssen bei Bedarf installiert werden, was muss man bei der Ausführung beachten, was muss eventuell davor noch gemacht werden und welche Datei muss ausgeführt werden.</h5>
<p>Ich habe neben Flask noch json importiert.</p>
<p>from flask import Flask</p>
<p>from flask import render_template</p>
<p>from flask import url_for, request</p> 
<p>import json</p>

<h3>Architektur</h3>
<h5>- Hier bei Bedarf eine kurze Beschreibung des Ablaufs des Programms auf Code Ebene z.B. als Ablaufdiagramm.</h5>
<p>Zur Veranschaulichung habe ich hier mein Aktivitätsdiagramm zur Semesterarbeit angefügt.[Aktivitätsdiagramm.pdf](https://github.com/helenskaa/projekt/files/8935560/Aktivitatsdiagramm.pdf)
</p> <br>
<p>Es gibt ein paar Punkte die wichtig zum beachten sind, damit das Programm funktioniert:</p>
<ul>
 <li>Bei der Startseite muss man den Username eingeben, danach die Kategorie auswählen und dann den Knopf "Kategorie auswählen" drücken, damit alle Informationen gespeichert werden und man richtig weitergeleitet wird. Zum schluss dann noch den Knopf "Quiz starten" damit das Spiel beginnt.</li>
 <li>Wenn man das Quiz durchspielt und alle Antworten im Dropdown Feld eingegeben hat, muss man zuerst auf "Antworten eintragen" drücken, damit die Antworten ausgewertet werden. Anschliessend muss man runterscrollen und auf "Auswertung anzeigen" drücken.</li>
 <li>Zum Schluss, wenn man ein neues Quiz beginnen möchte muss man zuerst auf "alle Daten zurücksetzten" klicken und danach noch auf "Quiz neu starten". Dann wird man auf die Startseite zurückgeleitet und kann den Username und die Kategorie neu definieren.</li>
</ul>

<h3>Ungelöste/unbearbeitete Probleme</h3>
<h5>- Was wurde nicht gelöst, welche Verbesserungen könnten noch gemacht werden.</h5>
<p>Am Anfang des Projekts wollte ich, dass die Fragen anders dargestellt werden. Ich wollte, dass wenn man eine Antwort eingibt, die richtige Antwort grün wird und die falsche Antwort rot. Nach einer Besprechung beim Tutoring habe ich aber herausgefunden, dass das nur mit Javascript möglich ist. Darum habe ich mir die Struktur umgedacht und alle Fragen auf einer Seite dargestellt. Die Antwortmöglichkeiten habe ich neu in einem Dropdown Feld eingegeben. 
 <br>
Was man wahrscheinlich besser machen könnte ist, dass man oft zwei Knöpfe für die vollständige Funktion drücken muss. Ich habe da lange rumstudiert aber bin schlussendlich auf keine bessere Lösung gekommen. Aber schlussendlich funktioniert alles, auch wenn es vielleicht nicht ganz so "schön" ist.</p>

