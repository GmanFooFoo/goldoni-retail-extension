# goldoni-retail-extension

Arbeitsrepo für die **Retail-Extension des Ristorante Goldoni** in Stuttgart:
vakuumierte Gerichte aus der laufenden Küche für Außer-Haus-Verkauf
(Phase 1 — Tiefkühl folgt in Phase 2).

Reines Markdown-Repo. Alles direkt auf GitHub lesbar. Kein Static-Site-Builder,
kein Hosting.

## Struktur

```
docs/
├── business-case/     # 19 Original-Dokumente (v1)
├── personas/          # 8 Original-Personas (werden in Stufe 2 ersetzt)
├── findings/
│   └── inconsistencies.md   # Widersprüche zwischen Dokumenten
├── plans/
│   └── rollout-plan.md      # Phase 1/2 Scope + Zeitplan
├── backlog/
│   └── repo-backlog.md      # MASCHIN-Status-Tabelle
├── glossary.md              # HACCP, LMIV, CCP, Vakuum etc.
└── how-to-use-marcello.md
```

## Workflow

- **Jede Zahl** braucht Quelle oder `[TBD-*]`-Marker (siehe `CLAUDE.md`)
- **Reviews** folgen dem Standard-Format in `CLAUDE.md`
- **Status-Tracking** in `docs/backlog/repo-backlog.md`
- **Commit nach jedem Work-Block**

## Scope

**Phase 1:** nur Vakuum-Produkte (gekühlt, +2°C bis +4°C)
**Phase 2:** Tiefkühl-Erweiterung (später, nach stabilem Vakuum-Launch)

Details in [`docs/plans/rollout-plan.md`](docs/plans/rollout-plan.md).

## Personas (geplant)

Die 8 Original-Personas werden in Stufe 2 durch 9 neue Review-Personas ersetzt:

1. **Marcus** — CFO / Zahlen-Realist
2. **Dr. Steiger** — Lebensmittelrechtler
3. **Pietro** — Küchenchef
4. **Thomas** — Gastronom-Praktiker
5. **Claudia** — Stammgast
6. **Jana** — Brand & Marketing
7. **Frau Keller** — Steuerberaterin
8. **Bruno** — Logistiker
9. **Inspektor Vogel** — adversariale Behördensicht

## Lizenz

Interne Dokumentation. Nicht öffentlich.
