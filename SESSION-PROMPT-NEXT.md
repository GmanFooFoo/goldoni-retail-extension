# Session-Prompt für Session 8 — Goldoni Retail Extension

> Handoff von Session 7 (2026-04-11) an Session 8. Wenn du (Claude) in einer frischen Session dieses Repo öffnest, lies zuerst diese Datei und erledige dann die Session-Start-Checkliste aus `docs/session-handoff.md`.

## Kurzstand

Session 7 hat **Doc 14 Rechtliche Absicherung & Haftung lead-reviewt** mit Rule 9 als zweitem Praxistest (nach Doc 04 in Session 6). Haupt-Trophäe: **ProdHaftG-Novelle zum 9. Dezember 2026** (EU-RL 2024/2853, BR-Drs. 775/25) mit Wegfall des 500 €-Selbstbehalts, Wegfall der 85-Mio-Cap, Beweiserleichterung bei technisch-wissenschaftlicher Komplexität, 25-Jahres-Höchstverjährung. Das ist der **zweite harte Rechts-Stichtag im zweiten Halbjahr 2026** neben PPWR 12.8.2026 — mit direkter Wirkung auf Silvios Launch-Timing-Entscheidung und auf die Chargen-Doku-Anforderungen (ab Stichtag als Zivilprozess-Beweismittel, nicht nur Behörden-Futter).

Vier P1-Findings gesamt: (1) ProdHaftG-Datums-Split, (2) § 58 LFGB Strafbarkeit (bis 5 Jahre Haft) komplett übersehen, (3) Fernabsatzvertrag bei Click-and-Collect und WhatsApp-Bestellung (§ 312c BGB) nicht erkannt, (4) LMIV Art. 14 Fernabsatz-Pflichtinformationen. 22 Findings in A/B/C. Doc 14 ist mit 72 Zeilen strukturell unterdimensioniert für sieben Rechtsgebiete; v2 wird realistisch 3–4 × so lang.

**Sequenz-Status: 03 ✓ 15 ✓ 05 ✓ 04 ✓ 14 ✓.** Die Gate-kritische Expert-Sequenz ist damit **abgeschlossen**. Fünf Lead-Reviews, fünf Findings-Dateien, 82 Findings insgesamt (davon 3 aufgelöst). Die nächste Phase hat eine andere Charakteristik — Co-Reviews, Rule-9-Nachzug, v2-Rewrites, Silvio-Paket-Konsolidierung, Sekundär-Reviews auf Doc 06–19.

## Struktur-Pushback in Session 7 — wichtige Änderung

Mitten in Session 7 hat German einen Strukturfehler aufgedeckt, der seit Session 4 unbemerkt mitlief: **Silvio war systematisch in die `Wer`-Spalte der Findings-Tabellen geschrieben worden, obwohl Silvio kein Reviewer ist**. Das Silvio-Paket existierte nur als Prosa, nicht als Artefakt. Korrektur:

1. **`docs/silvio-paket/offene-fragen.md`** neu angelegt als zentrales Artefakt mit 18 Einträgen (SP-01 bis SP-18) in fünf Blöcken. **Das ist jetzt der einzige Ort, an dem Silvio-Aktionen stehen.**
2. **Wer-Spalten-Cleanup** in `03/04/05/14/15-findings.md` und `inconsistencies.md`: Silvio raus, `→ Silvio-Paket SP-XX`-Verweise rein.
3. **Memory-Eintrag** `feedback_silvio_not_reviewer.md`. Session 8 sollte das beim Start aus `MEMORY.md` mitnehmen.
4. **Workflow:** Ausgang (Claude → German → Silvio) über das Silvio-Paket; Eingang (Silvio → German → Repo) über GitHub-Issues mit Label `feedback-silvio`.
5. **Offen für Session 8:** CLAUDE.md Rule 10 "Silvio ist kein Reviewer — Silvio-Paket als Artefakt" ist noch nicht in der Projekt-`CLAUDE.md` eingetragen. German muss entscheiden, ob das jetzt als Projekt-Rule neben Rule 9 rein soll — Memory-Eintrag allein ist weniger robust als eine Projekt-Rule.

## Kontext-Reset — lies diese Dateien zuerst

1. `docs/reports/2026-04-11-goldoni-g.md` — Session 7 Close mit Rule-9-Auswertung, Pushback-Block und Commit-Log.
2. `docs/silvio-paket/offene-fragen.md` — **neu**, das zentrale Silvio-Artefakt. Wird ab jetzt bei jeder neuen Lead-Review-Aktion erweitert.
3. `CLAUDE.md` — Rule 9 steht, Rule 10 (Silvio-Paket) noch offen.
4. `docs/reviews/14-recht-lebensmittelrechtler.md` — 127 Zeilen, Regulatorik-Nachtrag Dr. Maldini als Muster für zukünftige breite Rechts-Docs.
5. `docs/findings/14-findings.md` — 22 Findings in A/B/C.
6. `docs/findings/inconsistencies.md` — 14 Einträge, davon #11 (Schreibort Rückruf-Prozess) aufgelöst, #12/13/14 neu aus Session 7.
7. `docs/personas/Persona 00 – Silvio – Übersetzungs-Schicht.md` — wenn Variante A in Session 8 gewählt wird, ist das die operative Grundlage.
8. `docs/plans/rollout-plan.md` — **braucht einen Datums-Marker für 9.12.2026 ProdHaftG-Novelle** parallel zum PPWR-12.8.2026-Marker. Kleiner Arbeits-Block, der in jeder Variante von Session 8 vorgezogen werden sollte.
9. `docs/findings/decisions.md` — D-01 bis D-08 unverändert. Ggf. D-09 "Schreibort Rückruf-Prozess" und D-10 "Silvio-Paket als Artefakt" als Decisions aus Session 7 nachtragen (German entscheidet).
10. `session-state.md` — Stand nach Session 7.

## Session-8-Auftrag — drei Varianten, German entscheidet via AskUserQuestion

### Variante A — Silvio-Paket 1 Konsolidierung über Persona 00 (Recommended)

Das Silvio-Paket steht jetzt als strukturiertes Artefakt mit 18 Einträgen in fünf Blöcken. Persona 00 Silvio (Übersetzungs-Schicht) übersetzt es in eine **Silvio-facing Briefing-Notiz** in `docs/silvio-derivatives/silvio-paket-1-anrufe-und-termine.md` (der Ordner existiert noch nicht und wird dabei angelegt).

Aufgaben als Block-Kette:

1. **Silvio-Paket lesen** und die 18 Einträge in eine **nach Zeit- und Energie-Aufwand priorisierte Reihenfolge** bringen. Nicht nach P1/P2/P3, sondern nach "was kann Silvio in einem Vormittag erledigen" — Cluster nach: (a) Telefonate unter 10 min (Vetamt, IHK, Kassenhersteller, Gewerbeamt, Gesundheitsamt), (b) E-Mails mit Vorlauf (Steuerberater-Briefing, Anwalts-Auftrag, Versicherungs-Angebote, Beutel-Lieferant), (c) eigene Entscheidungen ohne Gesprächspartner (Launch-Timing, Scope Vorbestellung, Rechtsform, HACCP-Beauftragter, Hersteller-Anschrift, Schädlingsbekämpfungsvertrag), (d) Termine mit Vorlauf (Gesundheitsamt § 43 IfSG, Labor-Auftrag, Lieferanten-Gespräche).
2. **Silvio-facing Text** in Persona-00-Stil (einfache Sätze, keine Anglizismen, freundschaftlich, "nicht überreden, nicht verkaufen, nicht drängen"). Kein Paragraphen-Dumping, sondern "am Ende geht's einfach". Er soll die 18 Aktionen nicht als Pflicht-Liste erleben, sondern als Fahrplan, den er in seinem Tempo abarbeitet.
3. **Hand-Outs** für die drei komplexesten Einträge vorbereiten:
   - `SP-05-briefing-steuerberater.md` — strukturierter E-Mail-Text mit vier Kern-Fragen (7 % USt-Verifikation, Abschreibung Vakuumierer, Erlöskonten-Trennung, Verderb-Buchung), fertig zum Kopieren.
   - `SP-13-launch-timing-entscheidung.md` — Entscheidungs-Grundlage zwischen drei Optionen (vor 12.8.2026 PPWR / nach 9.12.2026 ProdHaftG / dazwischen), mit Pro/Contra je Option.
   - `SP-15-anwalts-auftrag.md` — Klauseln-Liste für AGB + Datenschutzerklärung + Krisen-Prozess-Blatt, Budget-Rahmen, zwei Umsetzungs-Optionen (Anwalt vs. IHK-Muster).
4. **Commit pro Block.**

**Effort:** M (halber bis ganzer Tag). Persona-00-Ton ist ungewohnt und muss in der ersten Anwendung sorgfältig kalibriert werden. Die drei Hand-Outs sind je S.

**Stop-Punkt:** Silvio-Briefing-Notiz und drei Hand-Outs committet.

**Vorteil:** Erster echter Silvio-facing Ausgang aus dem Repo. Erster Praxis-Test für Persona 00. Sichtbarer Wertbeitrag an Silvio, den German tatsächlich weitergeben kann.

### Variante B — Rückwirkender Regulatorik-Scan Dr. Maldini auf Doc 03 und Doc 05

Dr. Maldini existierte bei den Doc-03- und Doc-05-Reviews (Sessions 4 und 5) noch nicht. Beide Reviews sind damit aus Rule-9-Sicht "unbeschrieben". Variante B schließt diese Lücke, bevor v2-Rewrites beginnen.

Ablauf:

1. WebSearch für Doc 03 Vetamt: laufende Änderungen an VO 852/2004, aktuelle LMHV-Novellen, § 4 LMHV Schulungs-Anforderungen, IfSG § 42/43 Änderungen 2025/2026, Stuttgart-spezifische Verwaltungs-Anpassungen, aktuelle Vetamt-Adressdaten Hauptstätter Straße 58.
2. WebSearch für Doc 05 HACCP: aktuelle HACCP-Leitlinien-Updates, Codex-Alimentarius-Änderungen, Listerien-Risiko-Empfehlungen BfR/EFSA, aktuelle Urteile zu § 58 LFGB bei MHD.
3. Regulatorik-Nachträge in beide Review-Dateien einfügen, analog Template aus Doc-04- und Doc-14-Review. Bei aufgelösten Findings Strike-through setzen.
4. Neue Findings in die bestehenden Findings-Dateien nachziehen, nicht parallel neue anlegen.

**Effort:** M (halber Tag).

**Stop-Punkt:** Nachträge committed.

**Vorteil:** Hygiene vor v2. Alle fünf Gate-Docs haben dann den gleichen Rule-9-Stand.

### Variante C — Doc 14 Gruppe B Arbeits-Blöcke beginnen

Der Lead-Review ist geschrieben, die Findings stehen. Variante C startet direkt mit der Repo-Arbeit aus Gruppe B: **Rückruf-Prozess-Kapitel** als erstes (jetzt ist der Schreibort zwischen Doc 14 und Doc 05 geklärt), danach **ProdHaftG-Datums-Split-Kapitel** mit Rollout-Plan-Marker, danach **Versicherungs-Deckungs-Kapitel**.

Ablauf:

1. Rückruf-Prozess-Kapitel als strukturierte Tabelle (Schritt / Zeitfenster / Verantwortlich / Werkzeug / Dokumentation) mit Kommunikations-Vorlagen für Kunde/Vetamt/Presse. Schreibort Doc 14, Cross-Ref an Doc 05.
2. ProdHaftG-Datums-Split-Kapitel mit Wirkungsanalyse auf Chargen-Doku-Anforderungen. Anschließend Rollout-Plan um den 9.12.2026-Marker ergänzen, parallel zum PPWR-12.8.2026-Marker.
3. Versicherungs-Deckungs-Kapitel mit Anforderungs-Profil (mind. 2,5 Mio. € pauschal, Rückrufkosten-Baustein, Rechtsschutz, Obliegenheiten). Das ist gleichzeitig die Grundlage für Silvios Angebots-Einholung (SP-16).

**Effort:** L (ganzer Tag). Drei große Text-Blöcke.

**Stop-Punkt:** Drei Kapitel committed, Rollout-Plan-Marker gesetzt.

**Vorteil:** Sichtbarer Repo-Fortschritt, Kopplung zum Silvio-Paket bleibt intakt (Kapitel liefern Input für SP-13/15/16/17). **Nachteil:** Kein Silvio-facing Ausgang, kein Rule-9-Nachzug. Kapitel-Arbeit kann auch in Session 9 gemacht werden, ohne dass etwas blockiert.

## Empfehlung für Session 8

**Variante A (Silvio-Paket 1 Konsolidierung über Persona 00)**, aus drei Gründen:

1. Die Gate-kritische Expert-Sequenz ist durch. Der natürliche nächste Schritt ist der **erste Silvio-facing Ausgang**, der zeigt, dass die ganze Review-Arbeit eine Stimme an Silvio haben kann. Persona 00 ist dafür geschaffen und wartet seit Session 5 auf ihren ersten Einsatz.
2. Das Silvio-Paket steht als Artefakt jetzt robust — es ist nicht mehr Prosa, sondern strukturiert mit Status-Flow. Persona 00 hat eine klare Datengrundlage für die Übersetzung.
3. Variante B bleibt wichtig, ist aber nicht dringlich. Der Rückzug kann in Session 9 laufen. Variante C ist Repo-interne Arbeit, die jederzeit gemacht werden kann.

**Wenn aber der Rule-9-Nachzug aus Hygiene-Gründen dringlich wird (z. B. wenn v2-Rewrites direkt anstehen), Variante B priorisieren.**

## Vor-Block für jede Variante

Egal welche Variante gewählt wird, ein **XS-Vor-Block** sollte in allen drei Fällen vorweg laufen:

1. **Rollout-Plan-Marker 9.12.2026 ProdHaftG setzen** — parallel zum PPWR-12.8.2026-Marker. Ist in Varianten A und B unabhängig vom Haupt-Block, in Variante C Teil des Blocks.
2. **CLAUDE.md Rule 10 Entscheidung** — German fragen, ob die "Silvio ist kein Reviewer"-Regel als Projekt-Rule 10 in `CLAUDE.md` rein soll (analog Rule 9). Memory-Eintrag existiert bereits.
3. **Konsistenz-Check Findings-Format** — kurzer Scan über alle fünf Findings-Dateien, ob nach dem Wer-Spalten-Cleanup noch Drift-Stellen versteckt sind.

## Offene Punkte aus Session 7 — kein Blocker, aber im Kopf behalten

| # | Punkt | Wann |
|---|---|---|
| 1 | CLAUDE.md Rule 10 einbauen (Silvio ist kein Reviewer) | Session 8 Vor-Block |
| 2 | Rollout-Plan-Marker 9.12.2026 ProdHaftG-Novelle | Session 8 Vor-Block |
| 3 | Co-Reviews Doc 14 (Behördenkontrolleur, Steuerberaterin) | Nach Gate-Sequenz, flexibel |
| 4 | Rückwirkender Rule-9-Scan Doc 03 und Doc 05 | Variante B, spätestens vor v2-Rewrite |
| 5 | v2-Rewrites der fünf Gate-Docs | Nach Co-Reviews und Silvio-Rückmeldungen |
| 6 | Sekundär-Reviews Doc 02, 06, 07, 08, 09, 10, 11, 12, 13, 16, 17, 18, 19 | Nach v2-Rewrites Gate-Sequenz |
| 7 | D-09 und D-10 als neue Decisions dokumentieren (Schreibort Rückruf, Silvio-Paket) | Bei nächstem Decisions-Log-Update |
| 8 | Deep Review Stufe 3 bleibt XL. Realistisch: ein Lead-Review pro Session | Dauerthema |
| 9 | Silvio-Rückmeldungen über GitHub-Issues `feedback-silvio` | Dauerthema |
| 10 | `docs/silvio-derivatives/` Ordner wird in Variante A angelegt | Variante A |

## Wichtige Präferenzen von German (Erinnerung)

- **Silvio ist kein Reviewer** (neu Session 7). `Wer`-Spalte in Findings nur Review-Personas. Silvio-Aktionen in `docs/silvio-paket/offene-fragen.md`. Rückmeldungen via GitHub-Issue `feedback-silvio`.
- **Ton interne Arbeits-Docs (D-06):** präzise, direkt, Fach-Sprache erlaubt.
- **Ton Silvio-Ableitungen:** einfache Sätze, keine Anglizismen, tentativ, warm, *"nicht überreden, nicht verkaufen, nicht drängen"*.
- **Pushback Pflicht.** Session 7 hat gezeigt: ein Pushback hätte drei Sessions früher kommen können, wäre der Konsistenz-Check regelmäßig gelaufen.
- **Review-Standard-Format** aus `CLAUDE.md`.
- **Rule 9 Regulatorik-Scan** für Legal/Tax/Tech-Docs Pflicht.
- **Tabellen:** MASCHIN-Format (`# | Item | Prio | Effort | Wer | Blocker? | Status | Impact`).
- **Markdown:** keine Hard-Wraps im Fließtext.
- **AskUserQuestion** bei 2+ Optionen.
- **Commit nach jedem Work-Block.**
- **Session-Session-Regel:** Genau ein Schreibender pro Repo gleichzeitig. Vor Session-Start `session-state.md` prüfen.
- **Strike-through statt Löschen** bei aufgelösten Findings und Inconsistencies.

## Start-Nachricht Template

Nach Lesen der Kontext-Dateien:

> "Kontext geladen. Session 7 hat Doc 14 Recht lead-reviewt mit Rule 9 als zweitem Praxistest. Haupt-Trophäe: ProdHaftG-Novelle 9.12.2026 als zweiter Rechts-Stichtag neben PPWR 12.8.2026. Vier P1-Findings (ProdHaftG-Datums-Split, § 58 LFGB Strafbarkeit, Fernabsatzvertrag, LMIV Art. 14). 22 Findings A/B/C. **Sequenz-Ende erreicht: 03/15/05/04/14 alle lead-reviewt.** Session 7 hat zusätzlich einen Strukturfehler bereinigt — Silvio war systematisch in die Wer-Spalte der Findings geschrieben, obwohl er kein Reviewer ist. Korrektur: Silvio-Paket als zentrales Artefakt in `docs/silvio-paket/offene-fragen.md`, 18 Einträge in fünf Blöcken. Vor dem Haupt-Block schlage ich einen XS-Vor-Block vor: Rollout-Plan-Marker 9.12.2026 setzen, CLAUDE.md Rule 10 Entscheidung, Findings-Format-Konsistenz-Check. Danach drei Varianten für den Haupt-Block: (A) Silvio-Paket 1 Konsolidierung über Persona 00 — erster Silvio-facing Ausgang, Empfehlung. (B) Rückwirkender Rule-9-Scan Doc 03 und Doc 05 vor v2-Rewrites. (C) Doc 14 Gruppe B Arbeits-Blöcke (Rückruf-Kapitel, ProdHaftG-Datums-Split, Versicherungs-Deckung). Welcher Pfad?"
