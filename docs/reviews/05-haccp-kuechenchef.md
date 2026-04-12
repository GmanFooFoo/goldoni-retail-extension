# Review: 05 – HACCP-Erweiterung

**Reviewer:** Küchenchef (Persona 07, Co-Review)
**Datum:** 2026-04-12
**Doc-Version:** v1
**Lead-Review:** [Lebensmittelrechtler (Persona 02)](05-haccp-lebensmittelrechtler.md), 2026-04-11

## Kurzurteil (1 Satz)

Doc 05 beschreibt den Vakuum-Prozess korrekt, aber als lineares Diagramm — in einer realen Küche, die gleichzeitig Restaurant-Service vorbereitet und Retail-Chargen produziert, ist der Prozess nicht linear, sondern ein Ballett aus Timing, Platzverwaltung und Kreuzkontaminations-Vermeidung, und diese Choreographie fehlt komplett.

## Scoring (1–5)

- **Fachliche Korrektheit: 3** — Die Prozesskette (Rohware → Kühllagerung → Zubereitung → Abkühlung → Vakuumieren → Etikettierung → Kühllager → Verkauf) stimmt. Die CCPs sind an den richtigen Stellen. Aber die Details sind aus der Küche betrachtet wackelig: (a) "GN-Behälter max. 4 cm Schichthöhe" — das funktioniert für Sugo und Ragù, nicht für Lasagne. Lasagne muss in der Auflaufform abkühlen, und die ist deutlich tiefer als 4 cm. (b) "Kerntemperatur ≤ 10 °C innerhalb 2 Stunden" — für eine 4-cm-Schicht realistisch, für eine Lasagne-Portion mit Béchamel im Kern eher 3–4 Stunden ohne Schnellkühler. Das Doc gibt die Regel, nicht die Realität.
- **Vollständigkeit: 2** — Einverstanden mit dem Lead. Aus Küchenchef-Sicht fehlt zusätzlich: (a) der **Tagesablauf-Plan** — wann in Silvios Tag wird die Retail-Produktion eingeplant? Vormittags-Fenster (Session-8-Finding 4) ist die Annahme, aber das HACCP-Doc muss den Zeitplan konkret beschreiben. (b) Die **Rezeptur-Fixierung** als Voraussetzung für konsistente Chargen (Cross-Ref Doc 04 Finding 18). (c) Der **Verkostungs-Prozess** — wer probiert die Charge vor Freigabe? In der Restaurant-Küche probiert Silvio selbst; bei Retail-Chargen muss das dokumentiert werden.
- **Umsetzbarkeit: 3** — Die Muster-Protokolle sind sofort benutzbar. Die "3-Minuten-Kontrolle" ist ein guter operativer Ansatz. Aber: die Abkühlung "innerhalb 2 Stunden" auf ≤10 °C ist ohne Schnellkühler/Schockfroster bei Lasagne nicht machbar. Silvio hat (laut Rollout-Plan) in Phase 1 keinen Schockfroster. Das bedeutet: entweder die Grenze anpassen (realistisch: 4 Stunden bei flacher Portionierung), oder Schockfroster als Phase-1-Investition vorziehen, oder Lasagne erst in Phase 2 (mit Schockfroster). Das ist eine **Scope-Entscheidung**, die das HACCP-Doc erzwingen muss.
- **Risiko-Abdeckung: 2** — MHD "7 Tage Lasagne" ohne Validierung ist aus Küchenchef-Sicht das größte Risiko. Ich habe in meiner Karriere Vakuumprodukte gesehen, die nach 5 Tagen organoleptisch einwandfrei waren und nach 7 Tagen Textur-Probleme hatten (Béchamel wird wässrig, Pasta wird matschig). Ohne dokumentierten 7-Tage-Test mit Sensorik-Protokoll ist das MHD eine Wette.

## Red Flags

1. **Abkühlzeit für Lasagne unrealistisch ohne Schnellkühler.** Eine Lasagne-Portion (400g, ca. 6 cm hoch inkl. Béchamel) braucht in einem Standard-Gastro-Kühlschrank bei +2 °C ca. 3–4 Stunden, um im Kern auf ≤10 °C zu kommen. Die 2-Stunden-Vorgabe des Docs ist nur mit einem Schnellkühler erreichbar. Wenn Silvio in Phase 1 keinen hat, muss das CCP1 entweder angepasst werden (realistischer Grenzwert mit Begründung) oder Lasagne wird erst in Phase 2 angeboten. Das ist eine harte Entscheidung.

2. **Kein 7-Tage-Sensorik-Test dokumentiert.** "7 Tage Lasagne" — hat das jemand getestet? Was passiert mit der Béchamel nach Tag 5? Ist die Pasta noch bissfest nach 7 Tagen Vakuum bei +4 °C? Sind die Nährwerte nach 7 Tagen noch im Toleranzbereich? Ohne Test ist das MHD eine Annahme, keine Validierung.

3. **Chargen-Konsistenz nicht geregelt.** Wenn Silvio montags Lasagne macht und mittwochs wieder, müssen beide Chargen gleich schmecken und gleich zusammengesetzt sein. In einer Restaurant-Küche ist "gleich" ein relativer Begriff — Silvio kocht nach Erfahrung, nicht nach Gramm. Für Retail muss er nach Protokoll kochen (Cross-Ref Doc 04 Finding 18).

## Fundierte Kritikpunkte

1. **Vormittags-Produktionsfenster nicht im HACCP verankert.** Session 8 hat ermittelt, dass die Retail-Produktion ins Vormittags-Fenster (ca. 9–14 Uhr) passt. Das HACCP-Konzept muss dieses Fenster als festen Zeitraum definieren, mit klarer Trennung zum Restaurant-Vorlauf (ab ca. 15 Uhr Mise en place). Ohne diese zeitliche Trennung ist die Kreuzkontaminations-Frage (Rohware Restaurant vs. fertiges Vakuumprodukt Retail) nicht beantwortet.

2. **"Warme Produkte niemals vakuumieren" ist richtig, aber ohne Temperatur-Messgerät-Spezifikation.** Welches Thermometer, wie kalibriert, wie oft geprüft? In der Praxis: ein Einstechthermometer (≈30 €) mit jährlicher Kalibrierung genügt. Das steht nicht im Doc.

3. **Tiefkühl-Spalte in der MHD-Tabelle widerspricht D-01.** Bestätigung Lead-Linie und inconsistencies-Eintrag. Aus Küchenchef-Sicht: die Tiefkühl-Spalte suggeriert, dass Silvio das Produkt auch einfrieren kann. Das wäre eine andere Rezeptur (Béchamel ohne Ei, Pasta al dente minus 1 Minute) und ein anderer Prozess (Schockfrosten statt Kühlen). Phase 1 ist Vakuum/Kühlung — die Spalte muss raus oder als "Phase 2" markiert werden.

## Was fehlt (Küchenchef-Ergänzung zum Lead)

1. **Tagesablauf-Plan für Retail-Produktion** — Vormittags-Fenster mit konkreten Uhrzeiten, Reihenfolge der Arbeitsschritte, Reinigung zwischen Retail und Restaurant.
2. **Sensorik-Test-Protokoll für 7-Tage-MHD** — Verkostung an Tag 0, 3, 5, 7 mit dokumentiertem Ergebnis (Aussehen, Geruch, Textur, Geschmack) pro Produkt.
3. **Abkühlzeit-Realitätscheck** — Messung mit Silvios tatsächlicher Kühlinfrastruktur, nicht mit theoretischen Werten.
4. **Rezeptur-Standardisierung als Anlage** zum HACCP — Gramm-genaue Rezepturen für alle Phase-1-Produkte als Referenz für Chargen-Konsistenz.

## Empfehlung

- [ ] Freigabe
- [x] **Rework erforderlich**
- [ ] Freigabe mit Auflagen
- [ ] Stopp — geht so nicht live

**Begründung:** Die Grundstruktur stimmt, die Muster-Protokolle sind brauchbar. Aber die Praxis-Lücken (Abkühlzeit, Sensorik-Test, Chargen-Konsistenz, Tagesablauf) machen das Doc als Gate-Grundlage untauglich. Kein Stopp (anders als der Behördenkontrolleur), weil die operative Basis (Prozesskette, CCPs, Protokolle) ein guter Ausgangspunkt ist — sie muss aber mit realen Daten aus Silvios Küche gefüllt werden.
