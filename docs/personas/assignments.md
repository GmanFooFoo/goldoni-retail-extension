# Review-Zuordnung: Wer prüft welches Dokument?

Diese Tabelle ist die **zentrale Zuordnung** von Review-Personas zu den
19 Business-Case-Dokumenten. Sie ersetzt die `assigned_docs`-Felder, die
früher in jedem Persona-Frontmatter standen.

**Lesart:** Für jedes Dokument sind ein oder mehrere Personas zuständig.
"Lead" heißt: diese Persona ist hauptverantwortlich für das Review und
schreibt die Gesamt-Einschätzung. "Co" heißt: diese Persona liefert einen
Fachbeitrag aus ihrer Perspektive, ohne die Gesamt-Einschätzung zu
besitzen.

## Matrix

| # | Dokument | Lead | Co-Reviewer |
|---|---|---|---|
| 01 | Business Case Übersicht | Thomas | Jana, Marcus |
| 02 | Wirtschaftlichkeitsrechnung | Marcus | Frau Keller |
| 03 | Veterinäramt Stuttgart | Dr. Steiger | Inspektor Vogel |
| 04 | LMIV-Kennzeichnung | Dr. Steiger | Inspektor Vogel, Pietro |
| 05 | HACCP-Erweiterung | Dr. Steiger | Pietro, Bruno, Inspektor Vogel |
| 06 | Mockups (Etikett & HACCP-Dokument) | Jana | Claudia, Dr. Steiger |
| 07 | Preisgestaltung | Marcus | Claudia, Jana |
| 08 | Verpackungsstrategie | Jana | Pietro, Claudia, Bruno |
| 09 | Verkaufsstrategie | Jana | Thomas, Claudia |
| 10 | Operative Umsetzung | Thomas | Dr. Steiger, Pietro, Bruno |
| 11 | Lieferanten Stuttgart | Thomas | Bruno, Pietro |
| 12 | Investitionsplan & Geräteausstattung | Marcus | Bruno |
| 13 | 6-Wochen-Rollout-Plan | Marcus | Dr. Steiger, Thomas, Bruno |
| 14 | Rechtliche Absicherung & Haftung | Dr. Steiger | Inspektor Vogel, Frau Keller |
| 15 | Steuerliche Behandlung | Frau Keller | Marcus |
| 16 | Risiken & Gegenmaßnahmen | Marcus | Thomas, Bruno, Inspektor Vogel |
| 17 | Wettbewerbsanalyse Stuttgart West | Marcus | Jana |
| 18 | Finanzierungsplan | Marcus | Frau Keller |
| 19 | Produktsortiment-Erweiterung | Jana | Pietro, Claudia |

## Persona 00 — Silvio — horizontale Übersetzungs-Schicht

Silvio ist keine Fach-Linse, sondern die Übersetzungs-Schicht am Ende der Expert-Review-Phase. Er wirkt horizontal über alle Findings hinweg und steht deshalb nicht in der Lead/Co-Matrix einzelner Docs. Output ist nicht ein Review im Standard-Format, sondern eine Silvio-facing Ableitung in `docs/silvio-derivatives/`. Details: [`Persona 00 – Silvio – Der Gastronom.md`](Persona%2000%20%E2%80%93%20Silvio%20%E2%80%93%20Der%20Gastronom.md). Einsatz frühestens nach Abschluss der Gate-kritischen Expert-Reviews 03, 15, 05, 04, 14 — on-demand Einzel-Ableitungen pro Doc sind vorher erlaubt.

## Die 9 Fach-Personas (Reihenfolge = Stufe-3-Relevanz)

| # | Persona | Rolle | Datei |
|---|---|---|---|
| **01** | Marcus | CFO / Zahlen-Realist | [`Persona 01 – Marcus – CFO.md`](Persona%2001%20%E2%80%93%20Marcus%20%E2%80%93%20CFO.md) |
| **02** | Dr. Steiger | Lebensmittelrechtler | [`Persona 02 – Dr. Steiger – Lebensmittelrechtler.md`](Persona%2002%20%E2%80%93%20Dr.%20Steiger%20%E2%80%93%20Lebensmittelrechtler.md) |
| **03** | Frau Keller | Steuerberaterin | [`Persona 03 – Frau Keller – Steuerberaterin.md`](Persona%2003%20%E2%80%93%20Frau%20Keller%20%E2%80%93%20Steuerberaterin.md) |
| **04** | Inspektor Vogel | Behördenkontrolleur (adversarial) | [`Persona 04 – Inspektor Vogel – Behördenkontrolleur.md`](Persona%2004%20%E2%80%93%20Inspektor%20Vogel%20%E2%80%93%20Beh%C3%B6rdenkontrolleur.md) |
| **05** | Bruno | Logistiker | [`Persona 05 – Bruno – Logistiker.md`](Persona%2005%20%E2%80%93%20Bruno%20%E2%80%93%20Logistiker.md) |
| **06** | Thomas | Gastronom-Praktiker | [`Persona 06 – Thomas – Gastronom-Praktiker.md`](Persona%2006%20%E2%80%93%20Thomas%20%E2%80%93%20Gastronom-Praktiker.md) |
| **07** | Pietro | Küchenchef | [`Persona 07 – Pietro – Küchenchef.md`](Persona%2007%20%E2%80%93%20Pietro%20%E2%80%93%20K%C3%BCchenchef.md) |
| **08** | Jana | Brand & Marketing | [`Persona 08 – Jana – Brand & Marketing.md`](Persona%2008%20%E2%80%93%20Jana%20%E2%80%93%20Brand%20%26%20Marketing.md) |
| **09** | Claudia | Stammgast | [`Persona 09 – Claudia – Stammgast.md`](Persona%2009%20%E2%80%93%20Claudia%20%E2%80%93%20Stammgast.md) |

**Referenzen im Text:** Du kannst eine Persona entweder per Name ("Marcus sagt…"), per Nummer ("Persona 01 sagt…") oder per Rolle ("der CFO sagt…") ansprechen — alle drei sind äquivalent.

## Abdeckung pro Persona

Für jede Persona: welche Dokumente sie in welcher Rolle prüft.

| # | Persona | Leads | Co-Reviews |
|---|---|---|---|
| 01 | **Marcus** (CFO) | 02, 07, 12, 13, 16, 17, 18 | 01, 15 |
| 02 | **Dr. Steiger** (Lebensmittelrechtler) | 03, 04, 05, 14 | 06, 10, 13 |
| 03 | **Frau Keller** (Steuerberaterin) | 15 | 02, 14, 18 |
| 04 | **Inspektor Vogel** (Behörde adversarial) | — | 03, 04, 05, 14, 16 |
| 05 | **Bruno** (Logistiker) | — | 05, 08, 10, 11, 12, 13, 16 |
| 06 | **Thomas** (Gastronom-Praktiker) | 01, 10, 11 | 09, 13, 16 |
| 07 | **Pietro** (Küchenchef) | — | 04, 05, 08, 10, 11, 19 |
| 08 | **Jana** (Brand & Marketing) | 06, 08, 09, 19 | 01, 07, 17 |
| 09 | **Claudia** (Stammgast) | — | 06, 07, 08, 09, 19 |

## Hinweise

- **Keine Rolle prüft alles.** Jede Persona bleibt in ihrer Lane. Wenn Marcus im Rollout-Plan (Doc 13) eine Frage zum Lebensmittelrecht hat, verweist er explizit auf Dr. Steiger.
- **Phase 1 = nur Vakuum.** Alle Personas berücksichtigen den aktuellen Scope (siehe [`docs/plans/rollout-plan.md`](../plans/rollout-plan.md)). Tiefkühl-spezifische Bewertungen werden markiert als "Phase 2".
- **Diese Matrix ist lebendig.** Wenn sich während der Reviews zeigt, dass ein Dokument eine zusätzliche Perspektive braucht, wird hier die Zuordnung erweitert.
