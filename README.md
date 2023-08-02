# BwInfPancakeSort
41. Bundeswettbewerb 2022/2023 Aufgabe 3 (2. Runde)

## Aufgabenstellung
Bei dieser Aufgabe geht es um Sortieren von Pfannkuchen unter erschwerten Bedingungen.
Die Pfannkuchen liegen auf einem Stapel und sollen nach ihrer Größe sortiert werden. Sortiert
werden darf ausschließlich mit einem Pfannenwender, und zwar auf folgende Weise: Der Pfannenwender wird in den Stapel hineingeschoben oder unter ihn, dann wird der auf dem Wender
liegende Teilstapel umgedreht, und anschließend wird der oberste Pfannkuchen aufgegessen.
Das Ziel ist ein sortierter Stapel, bei dem der kleinste Pfannkuchen oben liegt. Wie viele Pfannkuchen übrig sind, ist dabei unerheblich.
Der Einfachheit halber nehmen wir an, dass die Größen unserer n Pfannkuchen gerade den
Zahlen 1 bis n entsprechen (jede Größe kommt nur einmal vor). Enthält der Stapel nun die
Größen (3,2,4,5,1) (von oben nach unten), und wir schieben den Wender zwischen den Pfannkuchen mit Größe 4 und den mit Größe 5, so erhalten wir als Ergebnis unserer Wende-und-EssOperation den Stapel (2,3,5,1).
Man kann sich nun einen Algorithmus überlegen, der für einen gegebenen Stapel eine möglichst kurze Folge von Wende-und-Ess-Operationen berechnet, die zu einem aufsteigend sortierten Stapel führt. Bei der Pfannkuchen-Wende-Und-Ess-Zahl (PWUE-Zahl) wird es noch etwas komplizierter: Wir nennen die kleinste mögliche Anzahl an Wende-und-Ess-Operationen,
die einen gegebenen Stapel S in einen sortierten Stapel überführt, A(S). Im obigen Beispiel
mit S = (3,2,4,5,1) ist A(S) = 2. Die PWUE-Zahl P(n) ist nun die größte Zahl, die A(S) für
irgendeinen Startstapel S mit n Pfannkuchen annimmt.
Ein Stapel mit nur einem Pfannkuchen kann nicht falsch sortiert sein, also ist P(1) = 0. Außerdem ist P(2) = 1, da maximal eine Operation notwendig ist. Für drei Pfannkuchen wird es
schon etwas schwieriger.
Es sind aber einige PWUE-Zahlen bekannt:
| n    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| ---- | - | - | - | - | - | - | - | - | - | -- | -- | -- | -- |
| P(n) | 0 | 1 | 2 | 2 | 3 | 3 | 4 | ? | ? | ?  | ?  | ?  | ß  |

> 1) Schreibe ein Programm, das bei Eingabe eines Stapels S eine möglichst kurze Liste an
> Wendeoperationen ausgibt, die S in einen aufsteigend sortierten Stapel überführen.
> 2) Schreibe ein Programm, das bei Eingabe von n die PWUE-Zahl P(n) berechnet sowie ein
> Beispiel ausgibt, für das tatsächlich P(n) Wendeoperationen notwendig sind. Berechne
> mindestens P(8) bis P(11)

