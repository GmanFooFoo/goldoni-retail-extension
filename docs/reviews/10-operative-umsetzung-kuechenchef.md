# Co-Review: Doc 10 — Operative Umsetzung

**Reviewer:** Pietro (Küchenchef, Persona 07) — Co-Review zu Thomas (Lead)
**Datum:** 2026-04-13
**Doc-Version:** v1

## Perspektive

Thomas hat 12 Findings identifiziert, darunter die physikalisch unmögliche Abkühlzeit und die Unterdimensionierung für 5 Produkte. Pietro ergänzt die Küchen-Handwerks-Perspektive: Mise-en-Place-Kollision, Rezeptur-Timing, Produktionsreihenfolge.

## Ergänzende Findings

### CF-01 — Produktionsreihenfolge für 5 Produkte fehlt

Der Ablaufplan zeigt eine lineare Abfolge "Produktion → Abkühlung → Vakuumieren". Bei 5 Produkten braucht es eine **gestaffelte Produktion**, weil die Garzeiten und Abkühlzeiten verschieden sind:

| Produkt | Garzeit | Abkühlzeit (passiv) | Besonderheit |
|---|---|---|---|
| Ragù | 2–3 Std. (Schmoren) | 90–120 Min. | Muss als erstes starten |
| Sugo | 45–60 Min. | 60–90 Min. | Parallel zum Ragù auf einem anderen Herd |
| Lasagne Classica | 45 Min. (Backen) | 90–120 Min. (dicht, viel Masse) | Braucht Ragù als Zutat → kann erst starten, wenn Ragù fertig |
| Lasagne Verdure | 45 Min. (Backen) | 90–120 Min. | Parallel zu Classica, wenn Ofenplatz da ist |
| Parmigiana | 30 Min. (Backen) + 20 Min. (Frittieren Auberginen) | 90–120 Min. | Frittieren = Fettspritzer, Geruch, separater Arbeitsgang |

**Empfehlung:** Ragù und Sugo starten um 9:00, Lasagne-Bau ab ~11:00 (wenn Ragù fertig), Parmigiana parallel. Vakuumieren ab ~13:00. Das Fenster 9:00–14:00 reicht nur, wenn die Reihenfolge stimmt und eine zweite Person parallel arbeitet.

### CF-02 — Mise-en-Place-Kollision mit Restaurant-Prep

Doc 10 ignoriert, dass die Küche ab ~14:00 für den Abend-Service vorbereitet werden muss. Mise en Place für den Restaurant-Betrieb (Saucen ansetzen, Gemüse schneiden, Pasta vorbereiten, Stationen bestücken) braucht je nach Menü 2–3 Stunden. Wenn die Vakuum-Produktion bis 13:00 oder 14:00 läuft, bleibt **kein Puffer zwischen Retail-Reinigung und Restaurant-Prep**. An Tagen mit großen Reservierungen (Samstagabend) ist das ein Kollisions-Risiko.

### CF-03 — Chargen-Verkostung nicht geregelt

Wer kostet die fertige Charge, bevor sie vakuumiert wird? In einer professionellen Produktion kostet der Küchenchef jede Charge auf Salz, Textur, Gargrad. Im Tagesablauf steht das nicht drin. Ohne Chargen-Verkostung riskiert Silvio, dass eine missratene Charge vakuumiert, etikettiert und verkauft wird — und erst der Kunde merkt, dass der Ragù versalzen ist.

### CF-04 — Aufwärm-Anleitung fehlt im operativen Plan

Doc 10 beschreibt die Produktion, aber nicht den Kunden-Endpunkt. Die Aufwärm-Anleitung gehört auf jedes Etikett (Doc 06), aber sie muss auch **getestet** werden — und zwar im Haushaltsofen, nicht im Profi-Konvektomaten. Eine Lasagne, die bei 180 °C Umluft 20 Min. braucht, braucht bei Ober-/Unterhitze 25–30 Min. Silvio muss beide Varianten testen und auf dem Etikett angeben.

### CF-05 — Rezeptur-Anpassung für Vakuum nicht thematisiert

Restaurant-Rezepturen sind für den sofortigen Verzehr optimiert. Vakuum-Produkte brauchen Anpassungen: weniger Flüssigkeit in der Lasagne (Wasserabscheidung im Beutel nach 3–5 Tagen), festere Pasta (al dente wird im Vakuum nach, wird sonst matschig), Sugo-Konsistenz dicker (dünn = Beutel-Schwappen beim Transport). Das ist kein optionales Tuning, das ist Pflicht — ohne Anpassung ist das Produkt am Tag 5 ein anderes als am Tag 1.

## Bestätigung Thomas-Findings

- **F-03 (Personalaufwand 5–6h unrealistisch):** Bestätige. Allein die Mise-en-Place für 5 Produkte (Auberginen frittieren, Ragù ansetzen, Lasagneplatten kochen) braucht 2–3 Stunden, bevor die eigentliche Produktion beginnt.
- **F-04 (Abkühlzeit 45 Min. unmöglich):** Bestätige nachdrücklich. Eine ofenwarme Lasagne (GN 1/1, 4 cm Schichthöhe) auf ≤ 10 °C in 45 Min. geht nur mit Blast Chiller. Passiv im Kühlraum: mindestens 90 Min., eher 120 Min.

## Empfehlung

Die v2-Rewrite braucht einen **Produktionsplan als Gantt-Diagramm** (oder zumindest Zeitstrahl), nicht eine lineare Ablaufbeschreibung. Die 5 Produkte laufen teilweise parallel, teilweise sequenziell (Ragù → Lasagne), und die Abkühlphasen bestimmen den Engpass, nicht die Garzeit.
