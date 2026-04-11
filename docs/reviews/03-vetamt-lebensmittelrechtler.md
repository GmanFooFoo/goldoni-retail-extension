# Review: 03 – Veterinäramt Stuttgart

**Reviewer:** Lebensmittelrechtler (Persona 02, Lead)
**Datum:** 2026-04-11
**Doc-Version:** v1
**Co-Review geplant:** Behördenkontrolleur (Persona 04), Session 5

## Kurzurteil (1 Satz)

Doc 03 ist als Orientierungs-Skizze brauchbar, aber für den Gate nach Rollout-Schritt 2 zu weich — zu viele weiche Formulierungen ("ggf.", "empfehlenswert"), keine Timings, keine Kosten, und zwei Pflicht-Dokumente (Rückrufprozess, HACCP-Beauftragter-Benennung) fehlen vollständig.

## Scoring (1–5)

- **Fachliche Korrektheit: 3** — Die genannten Rechtsgrundlagen (VO (EG) 852/2004 Art. 6 für Registrierung, § 4 LMHV für Schulungsnachweise) sind korrekt zitiert. Die Unterscheidung Registrierung vs. Zulassung ist richtig dargestellt. Abzüge: (a) Die Aussage "Onlineversand Grauzone" ist falsch — Onlineversand an Endverbraucher ist kein Graubereich, sondern unterliegt Fernabsatzrecht plus zusätzlichen Kennzeichnungspflichten (LMIV Art. 14 für Fernabsatz). (b) LFGB als nationaler Rahmen wird nicht erwähnt, obwohl er für die Betriebsbegehung relevant ist. (c) § 42 ff IfSG (Belehrung nach Infektionsschutzgesetz) fehlt vollständig, obwohl ohne diese Belehrung kein Mitarbeiter an Lebensmitteln arbeiten darf.
- **Vollständigkeit: 2** — Zentrale Pflichten fehlen: (a) schriftlicher Rückruf-Prozess (Art. 19 VO 178/2002), (b) namentliche Benennung HACCP-Beauftragter, (c) Dokumentations-Pflichten für Tagesprotokolle (Kühlkette, Reinigung, Produktion), (d) Betriebsspiegel / Tätigkeitsbeschreibung nach LMHV § 3. Der Abschnitt "Einzureichende Unterlagen" nennt sechs Punkte, aber in der Praxis verlangt das Stuttgarter Vetamt bei Vakuumier-Tätigkeit regelmäßig mehr (mindestens Reinigungsplan, Temperatur-Prüfplan, Rückstellproben-Konzept).
- **Umsetzbarkeit: 3** — Die fünf Ablauf-Schritte sind plausibel, aber ohne Timing, ohne Kosten und ohne Rework-Szenario. "Bescheid & Freigabe — bei Registrierung ohne Beanstandungen sofort starten erlaubt" ist der optimistische Fall; der realistische Fall (Nachbesserung bei Erstbegehung) fehlt. Für einen Gate nach Rollout-Schritt 2 ist das Dokument nicht präzise genug, um pass/fail zu beurteilen.
- **Risiko-Abdeckung: 2** — Der Abschnitt "Häufige Stolpersteine" adressiert vier Risiken, aber oberflächlich. Kein Hinweis auf persönliche Haftung nach § 58 LFGB bei unvalidierten Nährwerten oder falscher Allergenkennzeichnung. Kein Worst-Case-Szenario (Betrieb wird bei Erstbegehung beanstandet, Nachbesserungs-Frist, Zweitbegehung, ggf. Bußgeld). Kein Hinweis auf die Haftungs-Folge, wenn das MHD ohne Validierung festgesetzt wird.

## Red Flags

1. **MHD-Validierung ungeklärt.** Doc 03 schreibt "MHD ohne Grundlage — muss auf Fachliteratur oder eigenen Tests basieren". Was "eigene Tests" in der Praxis bedeuten, bleibt offen. Für vakuumierte Gerichte mit erhitzten und unerhitzten Komponenten (Parmigiana, Lasagne, Sugo, Ragù) ist das ein **Haftungs-Thema**. Ohne validierte MHD-Ermittlung ist jedes Etikett eine persönliche Haftungs-Quelle nach § 58 LFGB. Persona-Eskalationslogik: *Stopp, Laboranalyse oder dokumentierter Haltbarkeits-Test Pflicht*.
2. **Kein schriftlicher Rückruf-Prozess.** Art. 19 VO (EG) 178/2002 verpflichtet jeden Lebensmittelunternehmer zu einem funktionierenden Rückrufsystem. Doc 03 erwähnt das nicht. Ohne schriftliche Dokumentation ist das Risiko bei der Erstbegehung hoch, dass genau dieser Punkt beanstandet wird. Persona-Eskalationslogik: *Stopp vor erstem Verkauf*.
3. **HACCP-Beauftragter nicht benannt.** Die Pflicht zur Benennung eines HACCP-Verantwortlichen (Art. 5 VO 852/2004) ist implizit, aber Doc 03 benennt niemanden. Bei einem Ein-Personen-Betrieb (Silvio) ist das trivial klärbar — aber es muss dokumentiert sein, nicht "im Kopf".
4. **Nährwerte / Allergene auf Etiketten verweist auf Doc 04.** Doc 03 erwähnt die LMIV-Pflicht als "Stolperstein", ohne einen Auflösungs-Pfad anzugeben. Der Cross-Reference auf Doc 04 ist implizit, nicht explizit. Für einen Gate-Leser ist das unklar.

## Fundierte Kritikpunkte

1. **"Onlineversand Grauzone" ist sachlich falsch** (Doc 03, Tabelle "Registrierung vs. Zulassung"). Onlineversand an Endverbraucher ist rechtlich geklärt: keine Grauzone, sondern zusätzliche Pflichten (LMIV Art. 14 Fernabsatz, vollständige Pflichtkennzeichnung vor Kaufabschluss digital). Empfehlung: Entweder Aussage korrigieren oder Onlineversand explizit als "nicht in Phase 1" markieren (konsistent mit dem aktuellen Rollout-Plan, der nur Abholung im Restaurant vorsieht).
2. **"ggf. über Luca-Portal" ist unklar** (Doc 03, Schritt 2). Luca-Portal war zu Pandemie-Zeiten Kontaktnachverfolgung, heute ein Portal für Vetamt-Registrierungen in Baden-Württemberg. "ggf." ist unpräzise — es ist zu klären, ob das Stuttgarter Vetamt die Registrierung verpflichtend über Luca-Portal wickelt oder Papier akzeptiert. [TBD-Recherche] oder besser [TBD-Silvio] über Erstkontakt-Telefonat klären.
3. **Keine Timings** (Doc 03, gesamter Ablauf). Der neue `rollout-plan.md` setzt den Gate nach Schritt 2 (Vetamt-Bescheid) als harten Go/No-Go. Ohne Angabe, wie lange Erstkontakt → Unterlagen-Einreichung → Betriebsbegehung → Bescheid dauert, ist der Gate-Termin nicht planbar. Realistischer Korridor in Stuttgart nach Erfahrungssätzen: 3–8 Wochen, hochgradig von Auslastung des Vetamts abhängig. [TBD-Recherche] oder [TBD-Silvio] nach Erstkontakt-Telefonat.
4. **Keine Gebühren** (Doc 03, gesamter Ablauf). Registrierung ist in der Regel gebührenfrei, Betriebsbegehung oft auch. Aber Nachbegehungen nach Beanstandung sind kostenpflichtig (Stuttgart: erfahrungsgemäß ~80–200 € je Begehung, je nach Zeitaufwand). Ohne diese Info kann der Business-Case die Sunk-Cost-Kalkulation aus dem Rollout-Plan (2.500–3.000 € Worst Case) nicht sauber auf Vetamt-Kosten herunterbrechen.
5. **Rework-Szenario fehlt** (Doc 03, Schritt 5). "Bescheid & Freigabe — sofort starten erlaubt" ist der Happy Path. Der realistische Pfad ist: Erstbegehung → Beanstandungen (HACCP-Lücke, Reinigungsplan unvollständig, Temperaturprotokolle fehlen) → Nachbesserungs-Frist meist 4 Wochen → Zweitbegehung. Dieser Pfad muss im Doc stehen, weil er die Gate-Timing- und Kosten-Rechnung verändert.
6. **Fehlende Rechtsgrundlagen in der Auflistung.** Doc 03 nennt VO 852/2004, LMIV und § 4 LMHV. Für Vollständigkeit fehlen: VO 178/2002 (Rückruf), LFGB (nationale Umsetzung und Haftung), § 42 ff IfSG (Belehrung), LMHV §§ 3–5 (Betriebshygiene, Schulung, Selbstkontrolle). Eine Review-fähige Version von Doc 03 sollte diese Normen klar mappen, damit der Leser sieht, welche Pflicht aus welcher Norm kommt.
7. **"Empfehlung IHK Stuttgart" ist weich** (Doc 03, Abschnitt "Empfehlung"). Entweder ist das IHK-Vorgespräch ein Ablauf-Schritt vor Schritt 1 oder eine optionale Zusatz-Maßnahme. Aktuell liest es sich wie Marketing für die IHK. Klare Empfehlung: IHK-Erstberatung **in den Ablauf einziehen** als Schritt 0, weil sie kostenfrei ist und den teuren Fehler (erste Vetamt-Begehung mit unvollständigen Unterlagen) vermeiden hilft.

## Was fehlt

1. **Schriftlicher Rückruf-Prozess** — Aufbau, Verantwortlichkeiten, Dokumentations-Ort. Muss vor erstem Verkauf vorhanden sein.
2. **HACCP-Beauftragter** — namentliche Benennung (vermutlich Silvio selbst), dokumentiert im HACCP-Ordner.
3. **Tagesprotokolle** — welche Protokolle (Kühltemperatur, Reinigung, Produktion, Rückstellproben), welche Frequenz, wo abgelegt, wer prüft.
4. **Rückstellproben-Konzept** — bei vakuumierten Gerichten Standard: mindestens 7 Tage Rückstellprobe je Charge, gekühlt bei ≤ 4 °C, dokumentiert mit Produktionsdatum und Charge.
5. **Betriebsspiegel / Tätigkeitsbeschreibung** nach LMHV § 3 — kurzer beschreibender Text über Art der Tätigkeit, Mengengerüst, Personal. Oft Teil der Erst-Einreichung.
6. **Kosten-Aufstellung** — Registrierung, Erstbegehung, ggf. Nachbegehung, ggf. Laboranalyse für Nährwerte (Cross-Ref Doc 04). Grober Korridor reicht, absolute Zahlen nach Erstkontakt-Telefonat.
7. **Timing-Aufstellung** — Erwartungswert und Worst Case von Erstkontakt bis Bescheid. Wird gebraucht, um den Rollout-Plan-Gate nach Schritt 2 zu terminieren.
8. **Eskalations-Pfad bei Beanstandung** — welche Beanstandung hat welche Nachbesserungs-Dauer, welche Kosten, welche Stopp-Wirkung auf den Rollout-Plan.
9. **Cross-Reference-Hinweise** zu Doc 04 (LMIV/Etiketten), Doc 05 (HACCP) und Doc 14 (Rechtliche Absicherung), damit ein Leser die Pflichten-Ketten nachvollziehen kann.
10. **Konsistenz mit D-01** (Phase 1 nur Vakuum, kein Tiefkühl) explizit im Doc-Kopf festhalten, damit kein Leser die Tabelle "Registrierung vs. Zulassung" auf eine hypothetische Tiefkühl-Version bezieht.

## Empfehlung

- [ ] Freigabe
- [x] **Rework erforderlich**
- [ ] Freigabe mit Auflagen
- [ ] Stopp — geht so nicht live

**Begründung:** Doc 03 ist nicht "falsch", sondern **unvollständig und weich**. Es reicht nicht als Grundlage für den Gate nach Rollout-Schritt 2, weil drei Pflicht-Bausteine fehlen (Rückruf, HACCP-Beauftragter, Dokumentation), die Timings und Kosten nicht belastbar sind und das Worst-Case-Szenario (Nachbesserung bei Erstbegehung) komplett fehlt. Rework als v2 mit den unter *Was fehlt* gelisteten Ergänzungen. Kein Stopp, weil die Grundrichtung stimmt und keine sachlichen Fehler den Business-Case gefährden.

**Empfohlene Reihenfolge für v2:**

1. Silvio telefoniert Erstkontakt mit Stuttgart Vetamt und holt Timing, Gebühren, Portal-Pflicht und unvollständige Unterlagenliste ab (beantwortet TBD 1, 2, 3).
2. Parallel: IHK-Erstberatung als Schritt 0 einziehen (kostenfrei, liefert Auflistung aller Pflichten).
3. Doc 03 v2 integriert die gewonnenen Informationen plus die fehlenden Rechtsgrundlagen und Pflicht-Bausteine. Rückruf- und HACCP-Beauftragten-Benennung wird in Doc 03 nur referenziert, die eigentlichen Dokumente kommen in Doc 05 und Doc 14.

---

**Nächster Schritt:** Findings konsolidieren in `docs/findings/03-findings.md` (A3). Dann optional v2-Plan-Skizze in `docs/plans/03-v2-plan.md` (A4).
