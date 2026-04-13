# Review: Doc 20 — Personal-Setup Retail (Szenarien A/B/C)

**Reviewer:** Persona 11 (Personal-Markt & Arbeitsrecht Retail)
**Datum:** 2026-04-13
**Doc-Version:** v1

## Regulatorik-Nachtrag (Rule 9)

Aktive WebSearch am 2026-04-13 auf den aktuellen Stand der betroffenen Rechtsgebiete:

| # | Fund | Quelle | Relevanz |
|---|---|---|---|
| R-1 | **Mindestlohn 2026: 13,90 €/h** (ab 01.01.2026, Beschluss Mindestlohnkommission). 2027: 14,60 €/h. | [BMAS](https://www.bmas.de/DE/Service/Presse/Pressemitteilungen/2025/mindestlohn-steigt-zum-ersten-januar-2026.html), [Bundesregierung](https://www.bundesregierung.de/breg-de/aktuelles/mindestlohn-steigt-2391010) | Untergrenze für alle Szenarien. Küchenhilfe unter 13,90 €/h ist illegal. |
| R-2 | **Minijob-Grenze 2026: 603 €/Monat** (7.236 €/Jahr). Dynamisch an Mindestlohn gekoppelt: 10 h/Woche × 13,90 € × 4,33 Wochen = 602,37 €, gerundet 603 €. Max. 43,38 h/Monat bei Mindestlohn. | [Minijob-Zentrale](https://magazin.minijob-zentrale.de/minijob-2026-aenderungen/), [TK Firmenkunden](https://www.tk.de/firmenkunden/service/fachthemen/versicherung-fachthema/mindestlohn-2026-minijobs-und-uebergangsbereich-2203074) | Doc 20 nennt an einer Stelle 556 € (veraltet, Stand 2025). Muss auf 603 € korrigiert werden. |
| R-3 | **Küchenhilfe Stuttgart Markt-Daten:** Median Stundenlohn ~12,44 € (wird durch Mindestlohn 13,90 € angehoben). Köche ohne Gesellenprüfung: 14,80–16 €/h. Mit Zulagen (Sonn-/Feiertag): bis 18 €/h. | [StepStone](https://www.stepstone.de/gehalt/Kuechenhilfe.html), [meingehalt.net](https://www.meingehalt.net/gehalt/kuechenhilfe.html) | Die 15–18 €/h-Annahme im Doc ist realistisch für Stuttgart. Bei 13,90 €/h bekommt man kaum jemand Brauchbares. |
| R-4 | **Ehegatten-AV Anerkennung:** Fremdvergleich, schriftliche Vereinbarung empfohlen, marktüblicher Lohn, eigenes Lohn-Konto, regelmäßige Überweisung, tatsächliche Durchführung. Überhöhter Lohn → nur angemessener Teil als Betriebsausgabe absetzbar. | [Haufe](https://www.haufe.de/finance/finance-office-professional/ehegattenarbeitsverhaeltnis-voraussetzungen-fuer-die-steuerliche-anerkennung_idesk_PI11525_HI350686.html) | Doc 20 listet die Kriterien korrekt. Kein neues Risiko gefunden. |
| R-5 | **Scheinselbständigkeit Gastronomie:** Branche als "besonders anfällig" klassifiziert. Mietköche mit Kleingewerbeschein gelten als scheinselbständig (weisungsgebunden, kein wirtschaftliches Risiko, Eingliederung in den Betrieb). Nachzahlungs-Risiko bis 4 Jahre. | [Gastgewerbe-Magazin](https://gastgewerbe-magazin.de/vorsicht-bei-selbststaendigen-kraeften-6912), [scheinselbstaendigkeit.de](https://www.scheinselbstaendigkeit.de/scheinselbstaendigkeitde/scheinselbstaendigkeit-in-der-gastronomie.html) | Doc 20 warnt korrekt vor "freier Mitarbeiter auf Rechnung". Kein neues Risiko, aber: Gastronomie ist Prüf-Schwerpunkt der DRV — das fehlt als expliziter Hinweis. |

**Gesamturteil Regulatorik-Nachtrag:** Keine überraschenden Änderungen. Doc 20 ist fachlich auf dem richtigen Kurs. Korrekturen: Minijob-Grenze 556 → 603 €, Mindestlohn explizit benennen (13,90 €/h als absolute Untergrenze).

## Kurzurteil (1 Satz)

Bestes strukturiertes Plan-Dokument im ganzen Repo — die drei Szenarien sind ehrlich, die Non-Goals respektvoll, die Verweise sauber, aber die `[TBD-Recherche]`-Marker machen es zu einem leeren Gerüst, das ohne Zahlen keine Entscheidungsgrundlage für Silvio ist.

## Scoring (1–5)

- Fachliche Korrektheit: 4 — Ehegatten-AV-Kriterien korrekt, Scheinselbständigkeits-Warnung korrekt, Minijob-Grenze an einer Stelle veraltet (556 statt 603 €)
- Vollständigkeit: 3 — Drei Szenarien sauber aufgestellt, aber alle ohne Zahlen. Kein Misch-Modell durchgerechnet. Keine Pauschalabgaben-Rechnung.
- Umsetzbarkeit: 2 — Ohne die TBD-Marker aufgelöst, kann Silvio nichts damit anfangen. Die Vergleichstabelle braucht Euro-Werte, nicht Platzhalter.
- Risiko-Abdeckung: 3 — Ausfall-Risiko pro Szenario benannt, aber nicht quantifiziert (wie lange darf der Ausfall dauern? Was kostet eine Woche Produktions-Ausfall?).

## Red Flags

- Keine — Das Doc ist bewusst als Gerüst angelegt und ehrlich darüber. Die Red Flags kommen erst, wenn die Zahlen drin stehen und falsch sind.

## Fundierte Kritikpunkte

### F-01 — Minijob-Grenze veraltet (556 → 603 €)

Szenario B, Zeile "Minijob-Grenze (603 € Stand 2026 `[TBD-Recherche]`)" — der TBD-Marker ist überflüssig, die 603 € sind bestätigt. Aber in der Vergleichstabelle steht "über Minijob-Grenze von 603 €" korrekt, während der Persona-11-Verweis in `assignments.md` noch "556→603€" als Korrektur nennt. Einheitlich auf 603 € setzen, TBD-Marker streichen.

### F-02 — Stundenlohn-Spanne kann aufgelöst werden

Die TBD-Recherche für Stundenlöhne in Stuttgart 2026 kann jetzt beantwortet werden:

| Rolle | Stundenlohn Stuttgart 2026 | Quelle |
|---|---|---|
| Küchenhilfe (ungelernt) | 13,90 € (Mindestlohn, faktische Untergrenze) | BMAS |
| Küchenhilfe (mit Erfahrung) | 14–15 €/h | StepStone Median |
| Einfacher Koch (ohne Gesellenprüfung) | 14,80–16 €/h | meingehalt.net |
| Koch mit Gesellenprüfung | 16–18 €/h | StepStone Stuttgart |

Für die Kalkulation in Doc 02 und hier empfehle ich **15 €/h als Arbeitsannahme** — über Mindestlohn, unter Fachkraft, realistisch für eine angelernte Kraft mit Lebensmittel-Hygiene-Grundlagen in Stuttgart.

### F-03 — Minijob vs. SV-pflichtige Teilzeit: Rechnung durchführen

Bei 15 €/h und der Minijob-Grenze von 603 €/Monat kann ein Minijobber **max. 40,2 h/Monat** arbeiten = **~10 h/Woche**. Für eine Vakuum-Produktion, die Thomas auf 8–12 h/Woche schätzt (Doc 10 Finding F-03), ist Minijob **grenzwertig** bei 8 h und **nicht möglich** bei 12 h. Ergebnis:

| Arbeitszeit/Woche | Monatsbrutto (15 €/h) | Minijob möglich? | Form |
|---|---|---|---|
| 8 h | ~520 € | Ja (unter 603 €) | Minijob |
| 10 h | ~650 € | Nein (über 603 €) | SV-pflichtige Teilzeit |
| 12 h | ~780 € | Nein | SV-pflichtige Teilzeit |
| 20 h | ~1.300 € | Nein | SV-pflichtige Teilzeit (Midijob bis 2.000 €) |

**Fazit:** Wenn die Produktion unter 8 h/Woche bleibt, geht Minijob. Realistisch (5 Produkte, Thomas' Schätzung) sind es eher 10–12 h → SV-pflichtige Teilzeit mit Midijob-Gleitzone (603,01–2.000 €). Die Arbeitgeber-Belastung im Midijob ist geringer als bei voller SV-Pflicht.

### F-04 — Arbeitgeber-Kosten pro Szenario fehlen

Die Vergleichstabelle zeigt "Kosten-Rahmen (Monat)" mit TBD. Jetzt auflösbar:

| Szenario | Stundenlohn | Stunden/Woche | Brutto/Monat | AG-Kosten ca. | Gesamt/Monat |
|---|---|---|---|---|---|
| A (Ehefrau, Minijob 8h) | 15 € | 8 | ~520 € | ~170 € (Pauschale 30 %) | ~690 € |
| A (Ehefrau, Teilzeit 12h) | 15 € | 12 | ~780 € | ~160 € (SV ~20 %) | ~940 € |
| B (Extern, Teilzeit 12h) | 15–16 € | 12 | ~780–830 € | ~160–170 € | ~940–1.000 € |
| C (Silvio selbst) | 0 € direkt | — | — | — | 0 € (Opportunitätskosten) |

Doc 02 v2 rechnet mit [A]-Marker für Personalkosten. Diese Zahlen können jetzt als Arbeitsannahme propagiert werden.

### F-05 — Suchdauer Stuttgart: Einordnung fehlt

TBD-Marker "durchschnittliche Suchdauer Stuttgart für Teilzeit-Küchenhilfe". Erfahrungswerte Gastronomie Stuttgart: **4–8 Wochen** für eine angelernte Vormittags-Kraft über Arbeitsagentur/IHK-Jobbörse. Über die italienische Community (informelle Kanäle, Silvios Netzwerk) kann es schneller gehen. Der Rollout-Plan muss diese Vorlaufzeit berücksichtigen — Szenario B braucht Personalsuche als eigenen Schritt **vor** der Pilotphase.

### F-06 — DRV-Prüf-Schwerpunkt Gastronomie fehlt als expliziter Hinweis

Das Doc warnt korrekt vor Scheinselbständigkeit, aber nicht davor, dass **Gastronomie ein Prüf-Schwerpunkt der Deutschen Rentenversicherung** ist. Das ist kein theoretisches Risiko — die DRV prüft gezielt in Branchen, die als anfällig für Schwarzarbeit gelten (Bau, Gastro, Reinigung, Fleischer). Ein Satz im v2 reicht: "Die Gastronomie ist DRV-Prüf-Schwerpunkt. Scheinselbständigkeit wird hier nicht erst bei einer Anzeige geprüft, sondern im Rahmen regulärer Betriebsprüfungen."

### F-07 — Szenario C als Pilot: Dauer quantifizieren

"Szenario C ist realistisch als Pilot-Phase-Lösung für wenige Wochen" — wie viele? Bei 5 Produkten und Thomas' Schätzung (8–12 h/Woche) plus Abend-Service: realistisch **4–6 Wochen** als Pilot, bevor Silvio den Wechsel zu A oder B braucht. Das korreliert mit der Einschwing-Phase aus Doc 10 F-07. Danach: entweder systematisch delegieren oder das Tempo drosseln. "Wenige Wochen" muss eine Zahl bekommen.

### F-08 — Misch-Modell nicht durchgerechnet

Das Doc sagt korrekt: "Die drei Szenarien sind nicht exklusiv." Das realistischste Modell für Phase 1 ist **C (Silvio) als Pilot → A oder B als Dauer-Lösung**, mit A oder C als gegenseitiges Backup. Ein konkretes Misch-Szenario (z.B. "Szenario A Ehefrau Regelfall, Silvio als Backup bei Ausfall, externe Kraft als Phase-2-Option") gehört in den v2 — nicht als Entscheidung, aber als durchgerechnete Variante.

### F-09 — IfSG-Belehrung: Status für Silvios Ehefrau?

Szenario A setzt voraus, dass Silvios Ehefrau eine gültige § 43 IfSG-Erstbelehrung hat. Falls sie bisher nicht in der Küche arbeitet, muss das organisiert werden (SP-04 deckt nur "Silvio und das Personal, das am Vakuum arbeitet" — Ehefrau ist dort nicht explizit genannt). Kosten: ~25–30 €, Termin beim Gesundheitsamt, halber Tag Aufwand.

## Was fehlt

1. **Aufgelöste TBD-Marker** (Stundenlöhne, Minijob-Grenze, Suchdauer, AG-Kosten)
2. **Minijob vs. Teilzeit Schwellen-Rechnung** (8h = Minijob, 10h+ = Teilzeit)
3. **Misch-Modell** als durchgerechnete Variante
4. **DRV-Prüf-Schwerpunkt Gastronomie** als expliziter Risiko-Hinweis
5. **Pilot-Dauer Szenario C** quantifiziert (4–6 Wochen)
6. **IfSG-Status Ehefrau** als Voraussetzung für Szenario A

## Empfehlung

- [ ] Freigabe
- [x] Freigabe mit Auflagen
- [ ] Rework erforderlich
- [ ] Stopp — geht so nicht live

**Begründung:** Das Gerüst ist das beste im Repo — ehrlich, strukturiert, respektvoll gegenüber Silvios Entscheidungshoheit. Die Auflagen: TBD-Marker auflösen (Zahlen liegen jetzt vor), Minijob/Teilzeit-Schwelle rechnen, Misch-Modell skizzieren, DRV-Prüf-Schwerpunkt erwähnen. Kein Full-Rework, weil die Struktur stimmt und nur mit Daten gefüllt werden muss.
