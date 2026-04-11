# Session-Prompt für Session 7 — Goldoni Retail Extension

> Handoff von Session 6 (2026-04-11) an Session 7. Wenn du (Claude) in einer frischen Session dieses Repo öffnest, lies zuerst diese Datei und erledige dann die Session-Start-Checkliste aus `docs/session-handoff.md`.

## Kurzstand

Session 6 hat **Doc 04 LMIV lead-reviewt** mit CLAUDE.md Rule 9 als erstem Praxistest. Der Regulatorik-Nachtrag Dr. Maldini hat fünf Funde geliefert, davon zwei mit hoher Wirkung: (1) **DVO (EU) 2018/775 Herkunftsangabe der primären Zutat** — seit 1. April 2020 Pflicht, im Doc komplett übergangen, P1-Finding. Das ist die stärkste Einzel-Fundstelle der Session, und sie ist nicht frisch, sondern sechs Jahre alt — Rule 9 wirkt also nicht nur als Cutoff-Puffer, sondern als Breiten-Auslöser für vergessene Pflichten. (2) **PPWR (VO EU 2025/40) ab 12. August 2026** — erster echter Zukunfts-Stichtag im Projekt, mit Wirkung auf den Launch-Termin.

17 Findings in A/B/C-Gruppen. Gruppe A (Silvio) bekommt einen vierten Block **Etikett-Vorbereitung** (Adresse, Labor-Nährwerte 320–600 €, PPWR-Konformitätserklärung vom Beutel-Lieferanten). Gruppe B hat fünf Blöcke, beginnt mit Primärzutat-Herkunft-Kapitel. Gruppe C ist der Doc-Rewrite, kommt als letzter Schritt.

**Sequenz-Status:** 03 ✓ 15 ✓ 05 ✓ **04 ✓** — nur noch **Doc 14 Recht** steht in der Gate-kritischen Sequenz aus. Danach beginnt die Co-Review-Phase, der rückwirkende Rule-9-Scan auf Doc 03 und 05, und die Silvio-Paket-Konsolidierung.

**inconsistencies:** #7 um Doc 04 Los-Kennzeichnung erweitert, **#9 neu** (Doc 04 ↔ Doc 11 Lieferanten-Herkunft), **#10 neu** (Doc 04 ↔ Doc 06 Mockups).

**Commits Session 6:** 1e6c9dd, 28f74d3, 48534cf. Report: `docs/reports/2026-04-11-goldoni-f.md`.

## Kontext-Reset — lies diese Dateien zuerst

1. `docs/reports/2026-04-11-goldoni-f.md` — Session 6 Close mit Lessons, Rule-9-Auswertung und Commit-Log.
2. `CLAUDE.md` — **Rule 9 Regulatorik-Aktualität** ist für Doc 14 noch relevanter als für Doc 04, weil Doc 14 das eigentliche Rechts-Doc ist (BasisVO 178/2002, ProdHaftG, § 58 LFGB, UWG, Versicherungsrecht, AGB, Rückruf-Pflichten).
3. `docs/reviews/04-lmiv-lebensmittelrechtler.md` — besonders der Regulatorik-Nachtrag, als Muster für den Doc-14-Scan. Die Struktur "Rechtsgebiete → Quellen → Änderungen → Konsequenz" ist jetzt etabliert.
4. `docs/findings/04-findings.md` — die vierte Findings-Datei mit A/B/C. Vorlage für Doc 14.
5. `docs/findings/inconsistencies.md` — zehn Einträge, davon #9 und #10 aus Session 6.
6. `docs/personas/Persona 10 – Dr. Maldini – Fachanwalt Gastro Food Tech.md` — die Persona und das Nachtrag-Template.
7. `docs/personas/assignments.md` — Doc 14 Recht: Lead Dr. Steiger, Co Inspektor Vogel + Frau Keller + Dr. Maldini (horizontal).
8. `docs/plans/rollout-plan.md` — Gate-Logik, hier liegt die Aufhängung für den PPWR-Datums-Marker.
9. `docs/findings/decisions.md` — D-01 bis D-08 unverändert.
10. `session-state.md` — Stand nach Session 6.

## Session-7-Auftrag — drei Varianten, German entscheidet via AskUserQuestion

### Variante A — Doc 14 Rechtliche Absicherung Lead-Review (Recommended)

Doc 14 ist das letzte Doc in der Gate-kritischen Sequenz und das Doc, an dem Rule 9 am meisten zu tun hat: Rechts-Doc mit mehreren Querschnitts-Themen (Lebensmittelrecht, Produkthaftung, Verbraucherschutz, AGB-Recht, Versicherungsrecht, Rückruf-Pflichten). Lead: Dr. Steiger. Co: Inspektor Vogel, Frau Keller, **Dr. Maldini horizontal**.

**Ablauf als Block-Kette:**

1. **Rule 9 ausführen:** Aktive WebSearch auf BasisVO 178/2002 Art. 19 Rückruf-Pflichten, ProdHaftG aktuelle Urteile, § 58 LFGB Bußgelder und Strafbarkeit, UWG-Abmahnrisiken bei Lebensmittel-Werbung, AGB-Recht bei B2C-Abholung, Versicherungsrecht Produkthaftpflicht für Gastronomie-Retail, DSGVO bei Kunden-Kontaktdaten (WhatsApp aus Doc 09), Fernabsatzrecht falls Versand später Thema wird. Quellen-Priorität: gesetze-im-internet.de, EUR-Lex, BVL, DEHOGA, Versicherungsverband.
2. **Regulatorik-Nachtrag** im Kopf des Doc-14-Reviews, nach Template Persona 10.
3. **Lead-Review** im Standard-Format.
4. **Findings konsolidieren** in `docs/findings/14-findings.md` mit A/B/C-Gruppen, analog 03/15/05/04.
5. **Cross-Drift** in `inconsistencies.md` nachziehen, besonders #7 (MHD/Los), Schreibort-Klärung Rückruf-Prozess (Finding 3 Doc 05 hat den Schreibort Doc 05 vs. Doc 14 offen gelassen — hier wird er entschieden).
6. **Commit pro Work-Block.**

**Effort:** L (halber bis ganzer Tag). Doc 14 ist das umfangreichste Gate-Doc und Rule 9 wird viele Funde produzieren.

**Stop-Punkt:** Nach Findings committed. Nach Doc 14 ist die Gate-kritische Expert-Sequenz abgeschlossen — das ist ein Meilenstein und sollte mit einem klaren Session-Close gefeiert werden.

### Variante B — Rückwirkender Regulatorik-Scan auf Doc 03 und Doc 05 (Rule-9-Nachzug)

Dr. Maldini existierte bei den Doc-03- und Doc-05-Reviews noch nicht. Beide Reviews sind damit aus Rule-9-Sicht "unbeschrieben". Variante B schließt diese Lücke, bevor die Sequenz mit Doc 14 weiterläuft.

**Ablauf:**

1. WebSearch für Doc 03 Vetamt: laufende Änderungen an VO 852/2004, aktuelle LMHV-Novellen, § 4 LMHV Schulungs-Anforderungen, IfSG § 42/43 Änderungen 2025/2026, Stuttgart-spezifische Verwaltungs-Anpassungen.
2. WebSearch für Doc 05 HACCP: aktuelle HACCP-Leitlinien-Updates, Codex-Alimentarius-Änderungen, Listerien-Risiko-Empfehlungen BfR/EFSA, aktuelle Urteile zu § 58 LFGB bei MHD.
3. Regulatorik-Nachträge in beide Review-Dateien einfügen (Strike-through bei aufgelösten Findings, falls neue Rechtslage alte Befunde entschärft).
4. Bei Findings: die bestehenden findings-Dateien erweitern, nicht parallel neue anlegen.

**Effort:** S–M (1–3 Stunden).

**Stop-Punkt:** Nach den Nachträgen committed.

**Vorteil:** Hygiene vor dem nächsten Fortschritt. Alle vier bisher lead-reviewten Docs haben dann den gleichen Rule-9-Stand. **Nachteil:** Kein Gate-Fortschritt in der Sequenz — Doc 14 bleibt liegen.

### Variante C — Silvio-Paket 1 Briefing-Notiz über Persona 00

Das Silvio-Paket hat nach Session 6 vier Blöcke: (1) Vetamt/IHK aus Doc 03, (2) Steuerberater/Kasse/Gewerbeamt aus Doc 15, (3) IfSG/Schädlinge/HACCP-Benennung aus Doc 05, (4) Etikett-Vorbereitung (Adresse, Labor, Beutel-Lieferant) aus Doc 04. Persona 00 kann daraus eine erste Silvio-facing Briefing-Notiz in `docs/silvio-derivatives/silvio-paket-1-anrufe-und-termine.md` machen.

**Effort:** S (1–2 Stunden). Der Inhalt ist da; die Arbeit ist die Übersetzung in Silvios Ton.

**Stop-Punkt:** Silvio-Ableitung committet, an German übergeben.

**Vorteil:** Erste echte Silvio-Ableitung, erster Praxis-Test für Persona 00, sichtbarer Wertbeitrag für Silvio. **Nachteil:** Kein Review-Fortschritt, Doc 14 bleibt liegen.

## Empfehlung für Session 7

**Variante A (Doc 14 Recht Lead-Review mit Rule 9)**, aus drei Gründen:

1. Doc 14 ist das **letzte** Doc in der Gate-kritischen Sequenz. Danach öffnet sich das Feld für Co-Reviews, Silvio-Paket-Konsolidierung, v2-Rewrites und die B-Variante. Die Sequenz abschließen hat strategischen Wert — solange Doc 14 offen ist, ist das Projekt in der Halbzeit.
2. Doc 14 ist das Rule-9-relevanteste Doc überhaupt. Rechtsgebiete mit hohem Gesetzgebungs-Takt (ProdHaftG, DSGVO, UWG-Urteile) stapeln sich hier. Rule 9 wird viele Funde produzieren — das ist genau der Einsatzzweck, für den die Regel geschaffen wurde.
3. Variante B bleibt wichtig, ist aber nicht dringlich. Der Nachzug auf Doc 03 und 05 kann in einer kompakten Session 8 oder als Vorspiel zu den v2-Rewrites laufen. Variante C wäre stilistisch reizvoll, aber Silvio-Paket 1 wird belastbarer, wenn auch Doc 14 durch ist — dann hat das Paket fünf statt vier Blöcke, was zum Beispiel Rückruf-Kontakte und Versicherungs-Fragen aus Doc 14 enthalten kann.

**Wenn aber die rückwirkende Lücke aus Hygiene-Gründen dringlich wird, Variante B priorisieren.**

## Start-Frage an German

Via `AskUserQuestion` am Anfang der Session: *Variante A (Doc 14 Recht mit Dr. Maldini — Empfehlung), Variante B (rückwirkender Regulatorik-Scan Doc 03 + 05) oder Variante C (Silvio-Paket 1 Briefing-Notiz)?*

## Offene Punkte aus Session 6 — kein Blocker, aber im Kopf behalten

| # | Punkt | Wann |
|---|---|---|
| 1 | Silvio-Lieferanten-Gespräch für Primärzutat-Herkunft (Doc 04 Finding 1, inconsistencies #9) | Vor Doc-04-v2 |
| 2 | Labor-Nährwert-Analyse pro Produktlinie (Doc 04 Finding 7, 320–600 €) | Vor erstem Etikett-Druck |
| 3 | PPWR-Konformitätserklärung vom Beutel-Lieferanten (Doc 04 Finding 9) | Wenn Launch nach 12.8.2026 |
| 4 | Silvio-Verifikation 7 %-USt beim nächsten Steuerberater-Kontakt — Routine-Check | On-demand |
| 5 | Vetamt-Umzug Schlossstraße (Doc 03) — Silvio fragt beim Erstkontakt | On-demand |
| 6 | Rückwirkender Regulatorik-Scan Doc 03 und Doc 05 (Variante B) | Spätestens vor v2-Rewrite |
| 7 | Silvio-Paket 1 als Briefing-Notiz (Variante C) | Wenn Doc 14 durch |
| 8 | Co-Reviews Doc 03/15/05/04 (Behördenkontrolleur, CFO, Küche/Logistik/Behörde, Küchenchef) | Nach Abschluss der Gate-kritischen Sequenz |
| 9 | Gruppe-B-Pflicht-Dokumente (Rückruf, HACCP-Beauftragter, Tagesprotokolle, Rückstellproben) — Schreibort klärt sich beim Doc-14-Review | Doc 14 |
| 10 | Deep Review Stufe 3 bleibt XL. Realistisch: ein Lead-Review pro Session plus Findings plus Regulatorik-Nachtrag | Dauerthema |

## Wichtige Präferenzen von German (Erinnerung)

- **Ton interne Arbeits-Docs (D-06):** präzise, direkt, Fach-Sprache erlaubt.
- **Ton Silvio-Ableitungen (Variante C):** einfache Sätze, keine Anglizismen, tentativ, warm, *"nicht überreden, nicht verkaufen, nicht drängen"*.
- **Pushback Pflicht.**
- **Review-Standard-Format** aus `CLAUDE.md`.
- **Rule 9 Regulatorik-Scan** ist für Doc 14 noch wichtiger als für Doc 04 — das Rechts-Doc ist ihr Haupt-Einsatzfeld.
- **Tabellen:** MASCHIN-Format (`# | Item | Prio | Effort | Wer | Blocker? | Status | Impact`).
- **Markdown:** keine Hard-Wraps im Fließtext.
- **AskUserQuestion** bei 2+ Optionen.
- **Commit nach jedem Work-Block.**
- **Session-Session-Regel:** Genau ein Schreibender pro Repo gleichzeitig. Vor Session-Start `session-state.md` prüfen.
- **Strike-through statt Löschen** bei aufgelösten Findings und Inconsistencies.

## Start-Nachricht Template

Nach Lesen der Kontext-Dateien:

> "Kontext geladen. Session 6 hat Doc 04 LMIV lead-reviewt mit Rule 9 als erstem Praxistest. Haupt-Trophäe: DVO (EU) 2018/775 Primärzutat-Herkunft, seit 2020 Pflicht, im Doc komplett übergangen — P1. Zweiter Fund: PPWR 12.8.2026 als erster Zukunfts-Stichtag. Sequenz: 03/15/05/04 durch, nur noch Doc 14 Recht offen. Session 7 hat drei Varianten: (A) Doc 14 Recht Lead-Review mit Dr. Maldini — schließt die Gate-kritische Sequenz ab, Empfehlung. (B) Rückwirkender Regulatorik-Scan Doc 03 und 05 vor v2-Rewrites. (C) Silvio-Paket 1 Briefing-Notiz über Persona 00. Welcher Pfad?"
