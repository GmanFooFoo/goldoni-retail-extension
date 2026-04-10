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

## Abdeckung pro Persona

Für jede Persona: welche Dokumente sie in welcher Rolle prüft.

| Persona | Leads | Co-Reviews |
|---|---|---|
| **Marcus** (CFO) | 02, 07, 12, 13, 16, 17, 18 | 01, 15 |
| **Dr. Steiger** (Lebensmittelrechtler) | 03, 04, 05, 14 | 06, 10, 13 |
| **Pietro** (Küchenchef) | — | 04, 05, 08, 10, 11, 19 |
| **Thomas** (Gastronom-Praktiker) | 01, 09 (geteilt mit Jana), 10, 11 | 09, 13, 16 |
| **Claudia** (Stammgast) | — | 06, 07, 08, 09, 19 |
| **Jana** (Brand & Marketing) | 06, 08, 09, 19 | 01, 07, 17 |
| **Frau Keller** (Steuerberaterin) | 15 | 02, 14, 18 |
| **Bruno** (Logistiker) | — | 05, 08, 10, 11, 12, 13, 16 |
| **Inspektor Vogel** (Behörde adversarial) | — | 03, 04, 05, 14, 16 |

## Hinweise

- **Keine Rolle prüft alles.** Jede Persona bleibt in ihrer Lane. Wenn Marcus im Rollout-Plan (Doc 13) eine Frage zum Lebensmittelrecht hat, verweist er explizit auf Dr. Steiger.
- **Phase 1 = nur Vakuum.** Alle Personas berücksichtigen den aktuellen Scope (siehe [`docs/plans/rollout-plan.md`](../plans/rollout-plan.md)). Tiefkühl-spezifische Bewertungen werden markiert als "Phase 2".
- **Diese Matrix ist lebendig.** Wenn sich während der Reviews zeigt, dass ein Dokument eine zusätzliche Perspektive braucht, wird hier die Zuordnung erweitert.
