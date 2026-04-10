# goldoni-retail-extension

Business Case und Arbeitsrepo für die **Retail-Extension des Ristorante Goldoni** in Stuttgart:
vakuumierte/tiefgefrorene Gerichte aus der laufenden Küche für Außer-Haus-Verkauf.

Dieses Repo ist die **Entwickler-Sicht**. Die Silvio-freundliche Lese-Version
liegt auf der MkDocs-Reader-Site (siehe unten).

## Struktur

```
docs/
├── business-case/     # 19 Original-Dokumente (v1)
├── personas/          # 9 Review-Personas
├── reviews/           # Persona-Reviews pro Doc
├── findings/          # konsolidierte Findings + inconsistencies.md
├── plans/             # Revisionspläne, rollout-plan.md
├── backlog/           # repo-backlog.md (Status-Tabelle)
├── reports/           # Session-Reports
├── glossary.md
└── index.md           # Silvio-Einstieg (MkDocs)
```

## Lokale Entwicklung

```bash
# Einmalig
pip install mkdocs-material

# Reader-Site lokal starten
mkdocs serve
# → http://127.0.0.1:8000

# Build für Deploy
mkdocs build
# → site/
```

## Deploy

Die Reader-Site wird via **Vercel** an `retail.restaurante-goldoni.de` deployed.
Siehe `vercel.json`. DNS läuft bei DomainFactory (manuell konfiguriert).

## Workflow

Dieses Repo folgt dem MASCHIN-Workflow (siehe `CLAUDE.md`):

- **Jede Zahl** braucht Quelle oder `[TBD-*]`-Marker.
- **Commit nach jedem Work-Block.**
- **Reviews** folgen dem Standard-Format aus `CLAUDE.md`.
- **Status-Tracking** in `docs/backlog/repo-backlog.md`.

## Personas

9 Review-Personas decken die Kompetenzfelder ab:

1. **Marcus** — CFO / Zahlen-Realist
2. **Dr. Steiger** — Lebensmittelrechtler (LMIV, HACCP)
3. **Pietro** — Küchenchef (Rezeptur, Geschmack)
4. **Thomas** — Gastronom-Praktiker (Betrieb, Kollegen-Sicht)
5. **Claudia** — Stammgast (Kunden-Perspektive)
6. **Jana** — Brand & Marketing
7. **Frau Keller** — Steuerberaterin
8. **Bruno** — Logistiker (Kühlkette, Lager, Versand)
9. **Inspektor Vogel** — adversariale Behördensicht (Veterinäramt)

## Lizenz

Interne Dokumentation. Nicht öffentlich.
