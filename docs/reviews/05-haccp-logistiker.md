# Review: 05 – HACCP-Erweiterung

**Reviewer:** Logistiker (Persona 05, Co-Review)
**Datum:** 2026-04-12
**Doc-Version:** v1
**Lead-Review:** [Lebensmittelrechtler (Persona 02)](05-haccp-lebensmittelrechtler.md), 2026-04-11

## Kurzurteil (1 Satz)

Doc 05 beschreibt die Produktion bis zum Kühllager, aber die Kette vom Kühllager bis zum Kunden — also genau die Phase, in der die meisten Kühlketten-Brüche in der Praxis passieren — existiert im Dokument nicht.

## Scoring (1–5)

- **Fachliche Korrektheit: 3** — Die drei CCPs sind an den richtigen Stellen. CCP3 (Kühllagerung 0–4 °C) ist fachlich korrekt für die Lager-Phase. Was fehlt: der **vierte CCP** zwischen Kühllager und Kundenübergabe — die Theken-/Verkaufs-Phase. Wenn Silvio das Vakuumprodukt aus dem +4 °C-Kühlraum nimmt und in eine Verkaufstheke oder an die Theke stellt, beginnt eine neue Temperatur-Kette. Ohne Monitoring dieser Phase ist die Kühlkette unterbrochen.
- **Vollständigkeit: 2** — Einverstanden mit dem Lead. Aus Logistik-Sicht fehlt der gesamte **downstream-Bereich** nach dem Kühllager: (a) Wie wird das Produkt im Verkaufsbereich gelagert (gekühlte Theke? Kühlschrank hinter der Theke?), (b) Wie lange darf es dort stehen, bevor es zurück in den Kühlraum muss? (c) Was passiert bei der Kundenübergabe — gibt es einen Kühlketten-Hinweis? (d) FIFO-Regelung — wie wird sichergestellt, dass ältere Chargen zuerst verkauft werden? (e) Was passiert mit Rückläufern (Kunde bringt Produkt zurück)? (f) Was passiert mit Produkten, die das MHD erreichen, ohne verkauft worden zu sein?
- **Umsetzbarkeit: 3** — Das Tagesprotokoll Kühlung ist sofort operativ. Aber: "tägliche Temperaturmessung 08:00 Uhr" ist eine Punktmessung, kein Monitoring. Ein Datenlogger (50–150 €) mit Alarm-Funktion bei >7 °C wäre der richtige Standard. Nicht weil ein Kontrolleur es verlangt (er kann es verlangen), sondern weil ein nächtlicher Kompressor-Ausfall bei einer Punktmessung um 08:00 erst auffällt, wenn die Kühlkette schon 8 Stunden unterbrochen ist.
- **Risiko-Abdeckung: 1** — Kein Sommer-Szenario (Kühlraum bei 35 °C Außentemperatur stabil?), kein Übergabe-Szenario (Produkt eine Stunde im Auto bei 25 °C), kein Rückläufer-Szenario, kein Strom-Ausfall-Szenario, kein "was tun wenn der Kühlraum kaputt ist"-Plan.

## Red Flags

1. **Kein Temperatur-Monitoring, nur Punktmessung.** 1× täglich um 08:00 ist eine Stichprobe, nicht ein Monitoring. Ein Kompressor-Ausfall um 22:00 wird erst 10 Stunden später bemerkt — bis dahin sind die Produkte möglicherweise über dem Grenzwert gewesen und wieder abgekühlt. Ohne kontinuierliches Monitoring (Datenlogger mit min/max-Aufzeichnung) ist der Kühlketten-Nachweis lückenhaft.

2. **Keine FIFO-Regelung.** Wenn Silvio am Montag 20 Lasagne vakuumiert und am Mittwoch 20 weitere, stehen 40 Packungen im Kühlraum. Ohne FIFO-Regel (ältere nach vorne, MHD sichtbar) verkauft er möglicherweise die frischeren zuerst, und die Montags-Charge erreicht ihr MHD unverkauft. Verderb-Quote steigt, und einzelne Kunden bekommen Produkte nahe am MHD-Limit.

3. **Keine Übergabe-Phase.** Von CCP3 (Kühllager) zum Verkauf gibt es keine dokumentierte Brücke. Wie kommt das Produkt zum Kunden? Steht es in einer gekühlten Theke? Liegt es neben der Kasse? Wird es erst aus dem Kühlraum geholt, wenn der Kunde danach fragt? Jede Variante hat andere Temperatur-Implikationen.

## Fundierte Kritikpunkte

1. **Kühlketten-Hinweis für den Kunden fehlt.** Das Produkt verlässt Silvios kontrollierten Bereich in dem Moment, wo der Kunde es mitnimmt. Ab da ist die Kühlkette Kundensache. Aber Silvio hat die Pflicht, den Kunden zu informieren: "Gekühlt transportieren, innerhalb von 2 Stunden in den Kühlschrank" (Art. 25 LMIV Aufbewahrungs- und Verwendungsbedingungen). Das muss auf dem Etikett stehen (Cross-Ref Doc 04) und an der Verkaufsstelle kommuniziert werden. Empfehlung: Isoliertasche als optionales Zubehör (2–3 € Einkauf, 5 € Verkauf oder als Service gratis bei Bestellung ab X €).

2. **Lagerkapazität nicht geprüft.** Silvios Kühlraum dient dem Restaurant. Wenn Phase 1 täglich 20–30 Vakuum-Portionen produziert und die MHD-Spanne 7 Tage beträgt, liegen im worst case ca. 150 Portionen im Kühlraum (wenn der Abverkauf langsam startet). Das sind ca. 60 kg Ware, die Platz und Kühlleistung brauchen. Ist das im bestehenden Kühlraum machbar, ohne den Restaurant-Betrieb zu stören? [TBD-Silvio]

3. **Strom-Ausfall-Szenario fehlt.** Was passiert bei einem 4-stündigen Strom-Ausfall? Kühlraum-Temperatur steigt auf ca. +8–12 °C (je nach Isolierung und Füllgrad). Welche Produkte sind dann noch verkaufsfähig? Antwort: es hängt von der Dauer und der erreichten Maximal-Temperatur ab. Ohne Datenlogger weiß Silvio die Maximal-Temperatur nicht — und muss im Zweifel die gesamte Ware entsorgen.

## Was fehlt (Logistiker-Ergänzung zum Lead)

1. **CCP4 Verkaufs-/Übergabephase** — Temperatur im Verkaufsbereich, maximale Verweildauer außerhalb des Kühlraums, Rückführ-Regel.
2. **Datenlogger mit min/max-Aufzeichnung** als Standard (statt Punktmessung 1× täglich). Kosten: 50–150 € für WiFi-fähigen Logger mit Alarm.
3. **FIFO-Regelung** — ältere Chargen nach vorne, MHD-Datum sichtbar auf jeder Packung, Prüfung bei jeder Entnahme aus dem Kühlraum.
4. **Kunden-Kühlketten-Hinweis** — Etikett + Verkaufsstellen-Info + optionale Isoliertasche.
5. **Lagerkapazitäts-Rechnung** — Stellfläche und Kühlleistung für 100–150 Portionen parallel zum Restaurant-Bestand.
6. **Strom-Ausfall-/Kompressor-Ausfall-Plan** — Handlungsanweisung, Entsorgungs-Schwelle, Kontakt Kältetechniker.
7. **Rückläufer-Regelung** — zurückgebrachte Produkte werden **nie** weiterverkauft, dokumentiert entsorgt.
8. **Sommer-Szenario** — Kühlraum-Kapazität bei 35 °C Außentemperatur verifizieren, ggf. Produktion reduzieren.

## Empfehlung

- [ ] Freigabe
- [x] **Rework erforderlich**
- [ ] Freigabe mit Auflagen
- [ ] Stopp — geht so nicht live

**Begründung:** Die Produktion bis zum Kühllager ist in der Grundstruktur da (wenn auch mit Lücken, die der Lead und der Küchenchef benennen). Was komplett fehlt, ist mein Bereich — die Logistik vom Kühllager zum Kunden. In Phase 1 (nur Abholung im Restaurant) ist das überschaubar, aber es muss trotzdem definiert sein. Kein Stopp, weil die Grundinfrastruktur (Silvios Kühlraum existiert, Theken-Verkauf ist einfach) vermutlich reicht — aber die Dokumentation und die Notfall-Szenarien fehlen.
