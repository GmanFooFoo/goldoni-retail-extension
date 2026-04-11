# Session-Prompt für Session 4 — Goldoni Retail Extension

> Handoff von Session 3 (2026-04-11 abends) an Session 4. Wenn du (Claude) in einer frischen Session dieses Repo öffnest, lies zuerst diese Datei und erledige dann die Session-Start-Checkliste aus `docs/session-handoff.md`.

## Kurzstand

Session 3 hat **Maßnahme 2 (Repo-Zweck-Umschwung) abgeschlossen**. Das Repo ist jetzt auf Germans Arbeits-Level, nicht Silvio-facing:

- README: reiner Arbeits-Index (Phase, Scope, Repo-Map, Decisions, Stand, Working Rules).
- `docs/plans/rollout-plan.md`: Gate-basiert, 10–12 Wochen, Dependency-Tabelle mit Fail-Bedingungen, explizite TBD-Marker, harte Go/No-Go-Gates.
- Memory `feedback_readme_is_customer_facing.md` auf D-06 umgestellt. Silvio-Ableitungen entstehen nur ad-hoc.
- Spot-Check 2d/2e hat ergeben: 19 Business-Case-Docs und 9 Personas sind bereits auf Arbeits-Level — kein Rewrite. Aber es gibt **Substanz-Drift** (D-02 vs. v1-Scope), die in `docs/findings/inconsistencies.md` präzisiert wurde (Einträge 1, 3, 6).

Commits Session 3: `e5a415e`, `68d4493`, `49f1b0a`.

**Session 4** ist damit offen für den nächsten Hauptblock — den **Stufe-3 Deep Review** der 19 Business-Case-Docs. Alternativ kann German einen ruhigen Arbeits-Block für `docs/beteiligung.md` einschieben.

## Kontext-Reset — lies diese Dateien zuerst

1. `~/.claude/projects/-Users-germanrauhut-com-Developer-projects-goldoni-retail-extension/memory/MEMORY.md` — besonders `feedback_readme_is_customer_facing.md` (neu), `project_silvio_profile.md`, `feedback_personas_role_only.md`, `feedback_pushback_expected.md`.
2. `docs/findings/decisions.md` — D-01 bis D-08, besonders D-02 (Scope), D-06 (Arbeits-Level), D-08 (Phasen).
3. `docs/findings/inconsistencies.md` — 6 Einträge, Hauptdrift: v1-Docs vs. D-02 und neuer Rollout-Plan.
4. `docs/plans/rollout-plan.md` — aktuelle Gate-Logik und Risiko-Bewertung. Ist der Maßstab, gegen den die v1-Docs reviewt werden.
5. `README.md` — neuer Arbeits-Index.
6. `session-state.md` — aktueller Stand.
7. `docs/reports/2026-04-11-goldoni-c.md` — Session 3 Close.
8. `docs/personas/assignments.md` — Matrix wer welches Doc reviewt.
9. `CLAUDE.md` im Repo-Root — Review-Standard-Format und Grundregeln.

## Session-4-Auftrag — zwei Varianten, German entscheidet via AskUserQuestion

### Variante A — Stufe 3 Deep Review starten (Empfohlen)

Der Deep Review ist die Kernarbeit dieser Phase. Ohne ihn bleibt der Business-Case nicht reif für die Silvio-Entscheidung. Er zerfällt in Teilschritte:

**A1 — Priorisierungs-Entscheidung** (XS, 10 Minuten): In welcher Reihenfolge werden die 19 Docs reviewt? Zwei Pfade:

- **Pfad Gate-kritisch zuerst:** 03 Vetamt → 15 Steuer → 05 HACCP → 04 LMIV → 14 Recht. Rationale: Diese Gates entscheiden, ob das Projekt überhaupt starten kann. Zahlen sind nachrangig, solange der regulatorische Rahmen unklar ist.
- **Pfad Zahlen-kritisch zuerst:** 02 Wirtschaftlichkeit → 07 Preis → 18 Finanzierung → 12 Invest → 16 Risiken. Rationale: Ohne tragfähige Unit Economics lohnt sich keine Vetamt-Klärung.

Empfehlung Session 4: **Pfad Gate-kritisch zuerst**, weil der neue Rollout-Plan die MwSt- und Vetamt-Klärung als harte Blocker vor jeder Investition gesetzt hat (Gate nach Schritt 1 und 2). Zahlen werden belastbar erst, wenn die MwSt-Frage geklärt ist.

**A2 — Erstes Doc reviewen** (M, 1–2 Stunden): Das erste Doc aus der gewählten Sequenz (bei Empfehlung: Doc 03 — Veterinäramt Stuttgart) durch die zugeordnete Persona reviewen. Persona-Assignments in `docs/personas/assignments.md` prüfen. Review im Standard-Format in `docs/reviews/03-vetamt-[rolle].md` ablegen.

**A3 — Findings konsolidieren** (S, 30 Min): Kritische Punkte aus dem Review in ein `docs/findings/03-findings.md` herausziehen — das ist die Basis für den späteren v2-Plan.

**A4 — v2-Plan skizzieren (optional in Session 4)** (S, 30 Min): Erste Skizze eines `docs/plans/03-v2-plan.md` — was muss das Doc v2 anders machen, welche TBDs müssen beantwortet sein. Kein Rewrite, nur Plan.

**Stop-Punkt Session 4:** Nach A3 oder A4, je nach Kontext-Budget. Der Deep Review ist ein XL-Paket über mehrere Sessions.

### Variante B — `docs/beteiligung.md` Dimensionen 1–4 befüllen

Ruhiger, reflektierter Block. Kein Review, keine technische Arbeit — eine Denk-Übung zu D-07. Die vier offenen Fragen im Gerüst liegen schon bereit. Passt, wenn German sich nicht in die Deep-Review-Mechanik stürzen will oder wenn der Tag sowieso schon ausgelastet ist.

Ergebnis: `docs/beteiligung.md` bekommt Inhalt in den vier Dimensionen, die Fragen werden beantwortet oder präzisiert.

## Start-Frage an German

Via `AskUserQuestion` am Anfang der Session:

- *Variante A (Deep Review starten, empfohlen) oder Variante B (`beteiligung.md` befüllen)?*

Falls Variante A: zweite Frage:

- *Pfad Gate-kritisch zuerst (empfohlen) oder Pfad Zahlen-kritisch zuerst?*

## Offene Punkte aus Session 3 — kein Blocker, aber im Kopf behalten

| # | Punkt | Wann |
|---|---|---|
| 1 | Personas tragen noch Namen im Filename und Body ("Marcus", "Claudia" etc.). Memory sagt: nur Rollen. Drift aus früherer Session. | Eigener XS-Task vor oder während Deep Review — Rename der Dateien und Body-Anpassung. Gehört nicht mehr in einen Session-Close. |
| 2 | Doc 01 Ausgangssituation widerspricht D-02 (nennt Tiefkühl in Phase 1). Kleiner Einzel-Fix vor dem Deep Review möglich, oder im Zuge des Deep Reviews von Doc 01. | Optional im Warmup von Session 4 |
| 3 | `docs/silvio-derivatives/` Ordner existiert noch nicht. Wird erst bei erstem konkreten Silvio-Gesprächs-Bedarf angelegt. | On-demand |
| 4 | Deep Review Stufe 3 ist XL (mehrere Sessions). Erwartungsmanagement in Session 4: ein Doc pro Session ist realistisch, kein Zwang zum Durchrauschen. | Dauerthema |

## Wichtige Präferenzen von German (Erinnerung)

- **Ton interne Arbeits-Docs (D-06):** präzise, direkt, Fach-Sprache erlaubt, keine Consulting-Pose.
- **Ton Silvio-Ableitungen:** einfache Sätze, keine Anglizismen, tentativ, warm, Leitsatz *"nicht überreden, nicht verkaufen, nicht drängen"*.
- **Pushback Pflicht.** Eigene Recommendation vertreten, nicht blind ausführen.
- **Review-Standard-Format** aus `CLAUDE.md` — keine freie Struktur.
- **Tabellen:** MASCHIN-Format (`# | Item | Prio | Effort | Wer | Blocker? | Status | Impact`).
- **Markdown:** keine Hard-Wraps im Fließtext.
- **AskUserQuestion** bei 2+ Optionen.
- **Personas als Rollen**, keine Namen — *aber vorhandene Files tragen noch Namen*, das ist offene Drift.
- **Keine Marcello-Persona** (D-03), keine Easter Eggs (D-05), Leitsatz der Session im Report.
- **Commit nach jedem Work-Block**, nicht am Session-Ende gebündelt.

## Start-Nachricht Template

Nach Lesen der Kontext-Dateien:

> "Kontext geladen. Session 3 hat Maßnahme 2 abgeschlossen — Repo ist auf Germans Arbeits-Level, README und rollout-plan überarbeitet, Memory angepasst, Spot-Checks ohne Rewrite. Session 4 hat zwei Pfade: (A) Stufe 3 Deep Review starten — empfohlen, Pfad Gate-kritisch zuerst (Doc 03 Vetamt als erstes). (B) `beteiligung.md` Dimensionen befüllen. Welcher Pfad?"

Dann warte auf Germans Antwort und fang entsprechend an.

---

*Ende des Session-Prompts.*
