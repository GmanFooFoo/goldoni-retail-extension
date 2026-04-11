# Session-Prompt für Session 9 — Goldoni Retail Extension

> Handoff von Session 8 (2026-04-11 bis 2026-04-12) an Session 9. Wenn du (Claude) in einer frischen Session dieses Repo öffnest, lies zuerst diese Datei und erledige dann die Session-Start-Checkliste aus `docs/session-handoff.md`.

## Kurzstand

Session 8 hat sich in zwei Hälften zerlegt. **Erste Hälfte:** Variante A aus SESSION-PROMPT-NEXT-Session-7 durchgezogen — Silvio-Paket-1-Briefing-Notiz und drei Hand-Outs (SP-05 Steuerberater, SP-13 Launch-Timing, SP-15 Anwalt) im Persona-00-Stil geschrieben. Vor-Block: Rollout-Plan-Stichtage (PPWR 12.08.2026, ProdHaftG 09.12.2026 parallel erfasst), CLAUDE.md Rule 10 (Silvio ist kein Reviewer), Konsistenz-Cleanup in inconsistencies.md.

**Zweite Hälfte:** Substanzieller Pushback von German auf die vier Artefakte. Ton zu naiv-paternalistisch, Steuerberater-Mail als deutscher Geschäftsbrief statt im Silvio-Stil, Gesetzestext-Referenzen falsch, Silvio-Profil unvollständig. Als Folge: drei neue Projekt-Rules in CLAUDE.md (Rule 11 AskUserQuestion bei 2+ Optionen, Rule 12 eine Frage pro Nachricht adaptiv), zwei neue Memory-Einträge, ein **Persona-Deep-Dive** als Korrektur-Runde. Sechs adaptive Fragen zwischen German und Claude über Silvio, die zentrale Korrekturen geliefert haben — darunter die wichtigste: **Silvio ist im Chance-Modus, die Sorgen sind Germans** (Informations-Asymmetrie als zentraler Ton-Leitfaden für alle künftigen Silvio-facing Artefakte).

Ergebnis des Deep-Dive: sechs strukturelle Findings in `docs/findings/session-8-persona-deep-dive-findings.md`, Persona 99 (German selbst) neu angelegt und zweimal korrigiert, `project_silvio_profile.md` Memory erheblich erweitert. Die vier Session-8-Artefakte sind damit als **Rohmaterial** deklariert und müssen in Session 9 neu kalibriert werden.

## Kontext-Reset — lies diese Dateien zuerst

1. `docs/reports/2026-04-12-goldoni.md` — Session-8-Close mit vollem Ablauf, Pushback-Chronik und Lessons.
2. `docs/findings/session-8-persona-deep-dive-findings.md` — **die sechs neuen Findings aus dem Deep-Dive**. Die wichtigste Datei für Session 9, weil sie die Folge-Aktionen priorisiert.
3. `docs/personas/Persona 99 – German – Freund und Berater.md` — Germans eigene Persona mit Leitsatz *"Rocket Science jetzt, damit es später einfach wird"*, Ton-Regeln, Beziehung zu Silvio im Graubereich, operative Teilprojektleiter-Rolle für Nicht-Küchen-Themen.
4. `docs/personas/Persona 00 – Silvio – Der Gastronom.md` — sollte in Session 9 um Red-Flag-Punkte aus dem Deep-Dive ergänzt werden (Image-Bedrohung statt Strafe-Angst, Chance-Modus respektieren). XS-Arbeit vor dem Artefakt-Rework.
5. `CLAUDE.md` — Rules 10, 11, 12 sind neu. Rule 12 (eine Frage pro Nachricht, adaptiv) ist besonders scharf und verändert den Stil interaktiver Klärungs-Runden.
6. `docs/silvio-derivatives/silvio-paket-1-anrufe-und-termine.md` + `docs/silvio-paket/sp-05-briefing-steuerberater.md` + `docs/silvio-paket/sp-13-launch-timing-entscheidung.md` + `docs/silvio-paket/sp-15-anwalts-auftrag.md` — die **Rohmaterial-Artefakte** aus Session 8, die in Session 9 neu kalibriert werden. Beim Lesen den Persona-Pushback im Kopf behalten: naiv-paternalistisch, Consulting-Prosa, Gesetzestext-Referenzen, Silvio im Sorge-Modus statt Chance-Modus.
7. `docs/plans/rollout-plan.md` — Stichtage-Sektion 2026 steht. Fehlt: Vormittags-Fenster-Annahme und einfacher Koch statt zweiter Chef. Kleiner XS-Block in Session 9.
8. Memory: `project_silvio_profile.md` (stark erweitert), `feedback_persona_00_not_paternalistic.md` (neu), `feedback_one_question_at_a_time.md` (neu), `feedback_askuserquestion_preferred.md` (bestehend, jetzt als Rule 11 auch im Projekt).
9. `session-state.md` — Stand nach Session 8.

## Session-9-Auftrag — drei Haupt-Blöcke plus Vor-Block

### Vor-Block — XS, in jeder Variante vorweg

1. **Rollout-Plan-Präzisierung** — Vormittags-Fenster (zwischen ~9 und ~14 Uhr) als Produktions-Zeit-Annahme einbauen, einfacher Koch statt zweiter Chef als Personalkosten-Basis markieren. Kleiner Textblock in der Schritte-Sektion plus Anmerkung in den Kosten-Annahmen. Findings 4 und 5 aus `session-8-persona-deep-dive-findings.md` sind die Basis.
2. **Persona 00 Silvio Red-Flags ergänzen** — zwei neue Punkte: (a) Behörden-Kontrolle als Image-Bedrohung vor Gästen, nicht als Strafe-Angst; (b) Silvio ist am Projekt-Start im Chance-Modus, Sorgen sind bei German entstanden und dürfen nicht als Silvios Ängste formuliert werden. Findings 1 und 3 aus dem Deep-Dive.
3. **Session 8 Commit-Log-Ergänzung** im Session-8-Report, falls beim Session-8-Close-Commit nochmal Korrekturen anfallen.

### Variante A — Rework der Session-8-Artefakte unter Chance-Modus-Leitfaden (Recommended)

Der Kern-Auftrag für Session 9. Die vier Rohmaterial-Artefakte unter dem neuen Leitfaden neu schreiben. Leitfaden:

- **Ton:** peer-to-peer, nicht hand-holding. Silvio ist 25+ Jahre Profi, kein Anfänger.
- **Stimme:** Germans Stimme aus Persona 99 — warmer 17-Jahre-Freund mit Kopf für Strukturen, nicht Consultant, nicht bester Freund, nicht IT-Typ.
- **Chance-Modus respektieren:** Sorgen nicht stapeln, nicht alle auf einmal entfalten. Unterricht-ohne-Belehrung. *"Ich habe was gesehen, was du noch nicht siehst — hier ist, wie klein es wirklich ist, wenn man es kennt."*
- **Kontroll-Szene respektieren:** jeder Behörden-Kontakt trägt explizit die Gegenteil-Garantie (angemeldet, terminiert, diskret, außerhalb des Service).
- **Keine Gesetzestexte, keine Paragraphen** im Silvio-facing Text. Mündlich-verständliche Wiedergabe.
- **Slides als Ziel-Format im Kopf behalten:** kurze Sätze, tragende Stichpunkte, nicht Prosa-Absätze. Die Rework-Artefakte sind **Slide-Vorstufen**, noch nicht Slides selbst — aber jede Zeile sollte slide-tauglich sein.
- **Germans operatives Angebot einbauen:** mehrere SP-Einträge verschieben sich aus Silvios Liste in Germans Liste (IHK-Termin, Gewerbeummeldung, Fördermittel-Recherche, Label-Design über den Nachbarn). Die Briefing-Notiz muss das zeigen: die Silvio-Liste ist erheblich kürzer, als Session 8 es vermutet hat.

**Aufgaben:**

1. `docs/silvio-derivatives/silvio-paket-1-anrufe-und-termine.md` neu schreiben. Kürzer, peer-to-peer, fünf Gruppen mit klaren "Silvio macht" vs. "German macht" vs. "gemeinsam" Spalten. Eingang max. drei Sätze, keine Entschuldigung für den Umfang.
2. `docs/silvio-paket/sp-05-briefing-steuerberater.md` neu schreiben. Die E-Mail-Vorlage in Silvios Tonlage: kurz, duzend (wenn Steuerberater-Beziehung es erlaubt — im Zweifelsfall Silvio fragen), 4–8 Sätze, keine "Sehr geehrte/r"-Floskel, keine nummerierten Paragraphen-Fragen. Vorlage: *"Ciao [Vorname], ich will ab Herbst Lasagne vakuumieren. Vier Fragen: …"*
3. `docs/silvio-paket/sp-13-launch-timing-entscheidung.md` neu schreiben. Drei Optionen bleiben, aber ohne "Gesetzestext"-Referenzen, ohne apokalyptisches Register, in Slide-Vorstufe-Format. Kein Rücken-freihalte-Schlusswort ("du kannst umsteigen"), keine Hand-Holding-Rhetorik.
4. `docs/silvio-paket/sp-15-anwalts-auftrag.md` neu schreiben. Wege A/B beibehalten (Anwalt direkt vs. IHK-Muster + Sanity-Check), aber in der Silvio-Voice. Die Beauftragungs-E-Mail gehört zu Weg A und ist von Silvio an einen Anwalt — nicht deutsch-formell, sondern direkt und klar, mit klarer Paket-Beschreibung.

**Effort:** M (halber bis ganzer Tag). Ton ist der schwierigste Teil; nach dem ersten neu geschriebenen Artefakt sollte German gegenlesen und die Kalibrierung bestätigen, bevor die anderen drei folgen.

**Stop-Punkt:** vier neu kalibrierte Artefakte committet, German-Check nach dem ersten, Memory-Ergänzungen falls neue Kalibrierungs-Details auffallen.

### Variante B — Fördermittel-Strang anlegen

Finding 6 aus dem Deep-Dive. Aktuell keine Spur im Repo.

**Aufgaben:**

1. WebSearch auf staatliche Fördermittel für Gastronomie-Diversifikation in Baden-Württemberg: L-Bank, KfW, IHK-Förderberatung, Zuschüsse für Beratungskosten (Beratungshilfe Gastronomie), Innovations-Gutscheine BW, Digitalisierungs-Förderung, bonitäts-schonende Kredite.
2. Neues Doc anlegen: `docs/business-case/20-foerdermittel.md` (nummeriert um +1 nach der 19er-Serie) oder als Kapitel in Doc 02. Struktur: Programm-Name, Zuständigkeit, Voraussetzungen, Förderhöhe, Aufwand der Antragsstellung, Zeithorizont, Realismus für Silvios Fall.
3. Backlog-Eintrag in `docs/backlog/repo-backlog.md` eröffnen und schließen.
4. Optional: einen Eintrag ins Silvio-Paket, falls eine Aktion für Silvio entsteht (Bank-Gespräch, Antragsvorbereitung).

**Effort:** M (halber Tag mit WebSearch-Schwerpunkt).

**Stop-Punkt:** Fördermittel-Doc committet, in Rollout-Plan und/oder Doc 02 als Chance-Dimension referenziert.

### Variante C — Rückwirkender Rule-9-Scan Doc 03 und Doc 05

Weiter offen aus Session 7. Dr. Maldini hatte bei Doc-03- und Doc-05-Reviews noch nicht existiert, die beiden Reviews sind aus Rule-9-Sicht "unbeschrieben". Vor v2-Rewrites nötig.

**Aufgaben:**

1. WebSearch für Doc 03 Vetamt: VO 852/2004, LMHV-Novellen, § 4 LMHV, IfSG § 42/43, Stuttgart-spezifische Vetamt-Verwaltungs-Anpassungen.
2. WebSearch für Doc 05 HACCP: HACCP-Leitlinien-Updates, Codex-Alimentarius, Listerien-Risiko BfR/EFSA, aktuelle § 58 LFGB Urteile zu MHD.
3. Regulatorik-Nachträge in beide Review-Dateien einfügen, Template analog Doc 04 und Doc 14.
4. Neue Findings in bestehende Findings-Dateien nachziehen.

**Effort:** M (halber Tag).

**Stop-Punkt:** Nachträge committet.

## Empfehlung für Session 9

**Vor-Block unbedingt zuerst**, dann **Variante A (Artefakt-Rework)** als Kern-Arbeit. Variante B und C sind wichtig, aber nicht dringlich — A ist der Weg, der den Session-8-Pushback in sichtbaren Fortschritt übersetzt. Wenn A in einer Session nicht komplett durchläuft (was realistisch ist, weil der Ton jede Zeile kostet), dann die ersten beiden Artefakte (Briefing-Notiz + SP-05) fertig machen und SP-13 und SP-15 auf Session 10 schieben.

## Offene Punkte aus Session 8 — kein Blocker, aber im Kopf behalten

| # | Punkt | Wann |
|---|---|---|
| 1 | Rollout-Plan-Präzisierung (Vormittags-Fenster, einfacher Koch) | Session 9 Vor-Block |
| 2 | Persona 00 Red-Flags ergänzen (Image-Bedrohung, Chance-Modus) | Session 9 Vor-Block |
| 3 | Artefakt-Rework unter Chance-Modus-Leitfaden | Session 9 Variante A |
| 4 | Fördermittel-Strang anlegen | Session 9 Variante B oder Session 10 |
| 5 | Rule-9-Nachzug auf Doc 03 und Doc 05 | Variante C, spätestens vor v2-Rewrite |
| 6 | Co-Reviews Doc 04 und Doc 14 (Behördenkontrolleur, CFO, Steuerberaterin, Küchenchef) | nach Gate-Sequenz, flexibel |
| 7 | v2-Rewrites der fünf Gate-Docs | nach Co-Reviews und Silvio-Rückmeldungen |
| 8 | Sekundär-Reviews Doc 02, 06, 07, 08, 09, 10, 11, 12, 13, 16, 17, 18, 19 | nach v2-Rewrites |
| 9 | Silvio-Profil-Lücken: Steuerberater, Anwalt, Versicherung, Digital-Grad, Invest-Bereitschaft | wenn für konkrete Artefakt-Arbeit nötig |
| 10 | Slides-Erstellung über Claude-PowerPoint-Skill | später, wenn Repo durchgefräst ist |
| 11 | Deep Review Stufe 3 bleibt XL — Realistisch: ein Lead-Review pro Session | Dauerthema |
| 12 | Silvio-Rückmeldungen über GitHub-Issues `feedback-silvio` | Dauerthema |

## Wichtige Präferenzen von German (Erinnerung — ergänzt aus Session 8)

- **Silvio ist im Chance-Modus, die Sorgen sind Germans (neu Session 8).** Informations-Asymmetrie respektieren. Unterricht-ohne-Belehrung, nicht Angst-Reduzierung.
- **Ton Silvio-facing:** peer-to-peer, kein Hand-Holding, keine Consulting-Prosa, keine "Sehr geehrte/r"-Mails in Silvios Namen, keine Gesetzestext-Referenzen. Warm, respektvoll, direkt.
- **Slides als Ziel-Format.** Silvio-facing Texte sind Slide-Vorstufen, nicht Lese-Dokumente.
- **Eine Frage nach der anderen, adaptiv (neu Session 8, Rule 12).** Bei interaktiven Klärungs-Runden keine vorgeplanten Fragen-Listen.
- **AskUserQuestion bei 2+ Optionen Pflicht (neu Session 8, Rule 11).**
- **Graubereiche respektieren (neu Session 8).** Nicht schwarz-weiß vereinfachen. Beziehungen, Rollen und Haltungen haben Nuancen — die müssen im Text sichtbar sein.
- **Silvio ist kein Reviewer (Session 7, Rule 10).** Silvio-Paket als Artefakt. Nie in Wer-Spalten.
- **Rule 9 Regulatorik-Scan** für Legal/Tax/Tech-Docs Pflicht.
- **Pushback erwartet.** Claude widerspricht, wenn etwas nicht stimmt, und korrigiert eigene Arbeit nach Pushback sichtbar.
- **Review-Standard-Format** aus `CLAUDE.md`.
- **Tabellen:** MASCHIN-Format (`# | Item | Prio | Effort | Wer | Blocker? | Status | Impact`).
- **Markdown:** keine Hard-Wraps im Fließtext.
- **Commit nach jedem Work-Block.**
- **Session-Session-Regel:** Genau ein Schreibender pro Repo gleichzeitig. Vor Session-Start `session-state.md` prüfen.
- **Strike-through statt Löschen** bei aufgelösten Findings und Inconsistencies.

## Start-Nachricht Template

Nach Lesen der Kontext-Dateien:

> "Kontext geladen. Session 8 hat Variante A (Silvio-Paket-1-Konsolidierung) durchgezogen, aber unter Germans Pushback die vier entstandenen Artefakte als Rohmaterial deklariert. Haupt-Substanz-Block war ein Persona-Deep-Dive mit sechs adaptiven Fragen. Wichtigster Fund: **Silvio ist im Chance-Modus, die Sorgen sind Germans** (Informations-Asymmetrie als zentraler Ton-Leitfaden). Sechs strukturelle Findings liegen in `docs/findings/session-8-persona-deep-dive-findings.md`. Persona 99 (German) neu, Persona 00 Red-Flags sollten noch ergänzt werden. Rollout-Plan braucht Vormittags-Fenster-Annahme. Drei neue CLAUDE.md-Rules (10/11/12). Vorschlag Session 9: Vor-Block (Rollout-Präzisierung + Persona-00-Red-Flags, XS), dann Variante A (Artefakt-Rework unter Chance-Modus-Leitfaden, M). Variante B (Fördermittel) und Variante C (Rule-9-Nachzug) als Alternativen. Welcher Pfad?"
