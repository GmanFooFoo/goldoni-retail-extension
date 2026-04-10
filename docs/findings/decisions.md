# Decisions — Goldoni Retail Extension

Single-Source-of-Truth für gefallene Entscheidungen in diesem Repo. Format wie in `docs/session-handoff.md` definiert. Einträge chronologisch, neue unten anhängen.

---

## D-01: Phase 1 nur Vakuum, kein Tiefkühl

**Datum:** 2026-04-10
**Context:** Silvios Küche hat weder Schockfroster noch Gefrierraum in der Größe, die für Tiefkühl-Verkauf nötig wäre. Investition + Kühlketten-Logistik + zusätzliche Vetamt-Auflagen würden Phase 1 sprengen.
**Entscheidung:** Launch startet ausschließlich mit vakuumierten, gekühlten Gerichten. Tiefkühl wird explizit auf Phase 2 vertagt.
**Rationale:** Vakuum + Kühlung nutzt vorhandene Infrastruktur. Pilot-Phase kann ohne Capex-Sprung stattfinden. Tiefkühl ist nach Pilot-Erfolg nachrüstbar.
**Alternativen geprüft:** (a) Sofort beide Kanäle — verworfen wegen Capex und Regulierungs-Aufwand. (b) Nur Tiefkühl — verworfen, weil die Kühlketten-Logistik Silvios operatives Modell zu stark verändert.
**Affects:** `docs/plans/rollout-plan.md`, Business-Case-Docs zu Verpackung/Haltbarkeit/HACCP, Memory `project_scope_phase1_vakuum_only.md`.
**Revidierbar:** Ja, nach Pilot-Phase, wenn Nachfrage und Wirtschaftlichkeit stehen.

## D-02: Plain Markdown, kein Static-Site-Builder

**Datum:** 2026-04-11
**Context:** In Session 1 wurde MkDocs Material aufgesetzt (Stufe 1b). Nach einem Testlauf war klar: der Aufwand für Hooks, Theme, Venv und Deployment steht in keinem Verhältnis zum Nutzen, und Silvio wird die Reader-Site wahrscheinlich nie öffnen.
**Entscheidung:** Das Repo bleibt plain Markdown. Kein MkDocs, kein Vercel, kein Static-Site-Builder. GitHub rendert die Dokumente direkt.
**Rationale:** GitHub-Rendering reicht für Germans Arbeits-Ebene und für jede Ableitung, die Silvio irgendwann sehen soll. Keine Build-Pipeline heißt kein Drift, keine Wartung, keine kaputten Links durch Theme-Updates.
**Alternativen geprüft:** (a) MkDocs Material — aufgesetzt, getestet, verworfen. (b) Vercel-Deploy für Silvio-Landing — verworfen als Konsequenz aus (a). (c) Obsidian Publish — nie ernsthaft erwogen.
**Affects:** `CLAUDE.md` "Keine Reader-Site"-Section, Memory `feedback_plain_markdown_default.md`.
**Revidierbar:** Unwahrscheinlich. Falls später eine Silvio-freundliche Web-Ansicht gebraucht wird, wird das als separates Projekt neu entschieden.

## D-03: Keine Marcello-Persona, German direkt als Autor

**Datum:** 2026-04-11
**Context:** In Session 1 wurde zunächst eine "Marcello"-Persona aufgesetzt als Berater-Figur, die Silvio fachlich begleitet. Beim Überarbeiten des README fiel auf, dass das Framing falsch ist: German ist Silvios Freund, kein Berater mit eigener Persona.
**Entscheidung:** Marcello-Persona komplett gestrichen. Alles, was Silvio sieht, ist in Germans Stimme und als Germans Arbeit ausgewiesen. Claude unterstützt im Hintergrund, tritt aber nicht als eigene Figur auf.
**Rationale:** Eine Berater-Persona hätte eine professionelle Distanz erzeugt, die weder Germans Verhältnis zu Silvio entspricht noch Silvios Erwartung an einen freundschaftlichen Austausch. Freundschaftsdienst ≠ Beratungsmandat.
**Alternativen geprüft:** (a) Marcello als "Chief of Staff"-Figur behalten — verworfen. (b) Claude als namentliche Persona — verworfen, widerspricht Germans Autorschaft.
**Affects:** `CLAUDE.md` Rollen-Section, `README.md`, `docs/backlog/repo-backlog.md`, `docs/session-handoff.md` (ehemals `how-to-use-marcello.md`), Memory `project_no_marcello_persona.md`.
**Revidierbar:** Nein, Grundprinzip der Beziehung German ↔ Silvio.

## D-04: 9 Review-Personas als Analyse-Linsen, nicht Agent-Files

**Datum:** 2026-04-11
**Context:** Die 9 Review-Personas (CFO, Lebensmittelrechtler, Steuerberaterin, alter Koch, Gastronom-Kollege, Stammkundin, Marketing, Logistik, Amts-Kontrolleur) hätten als eigenständige Claude-Agent-Files angelegt werden können.
**Entscheidung:** Die Personas bleiben Markdown-Dokumente in `docs/personas/` und werden als Analyse-Linsen verwendet, nicht als autonome Agent-Files mit eigener Lauf-Umgebung.
**Rationale:** Die Personas sind Prüf-Perspektiven, mit denen die 19 Original-Docs strukturiert abgeklopft werden. Sie brauchen keine eigene Identität und kein eigenes Tool-Setup. Das Format `Persona NN – Name – Rolle.md` reicht aus.
**Alternativen geprüft:** (a) Claude-Subagenten pro Persona — Overkill und Wartungsaufwand. (b) Personas nur als Rollen-Stichwort ohne eigene Datei — zu wenig Substanz für strukturierte Reviews.
**Affects:** `docs/personas/`, `docs/personas/assignments.md`.
**Revidierbar:** Ja, falls das Review-Volumen so groß wird, dass Automatisierung nötig wird. Heute nicht absehbar.

## D-05: Keine Session-Close Easter Eggs, stattdessen Leitsatz

**Datum:** 2026-04-11
**Context:** In anderen Projekten (OMNIXIS, CEE) enden Session-Reports mit einem Easter-Egg-Block (Song, Quote, Poster-Prompt). Für Goldoni wurde diskutiert, ob das hier auch passt.
**Entscheidung:** Keine Easter Eggs. Stattdessen schließt jeder Session-Report mit einem "Leitsatz der Session"-Abschnitt: ein Satz, der das wichtigste Arbeits-Prinzip der Session festhält.
**Rationale:** Goldoni ist ein kleiner, enger Kontext. Pop-Kultur-Referenzen und Poster-Prompts wirken hier fremd. Ein Leitsatz dagegen sichert die wichtigste Einsicht der Session als stabilen Anker für die nächste Session.
**Alternativen geprüft:** (a) Easter Eggs aus OMNIXIS übernehmen — verworfen, passt tonal nicht. (b) Gar kein Schluss-Abschnitt — verworfen, weil der Leitsatz nützlich ist.
**Affects:** `docs/reports/*.md`, Memory `project_no_easter_eggs.md`.
**Revidierbar:** Unwahrscheinlich.

## D-06: Repo wird auf Germans Arbeits-Level geschrieben, Silvio-Docs sind Ableitungen

**Datum:** 2026-04-11 (MASCHIN-Review-Klärung)
**Context:** Session 1 hat das komplette Repo auf Silvio-facing Ton gedreht (freundschaftliche Sprache, ELI12, keine Fachbegriffe ohne Erklärung). Der MASCHIN-Review hat gezeigt, dass Silvio das Repo vermutlich nie selbst öffnet — der Silvio-Ton in den internen Arbeits-Docs ist Ballast, der echte Tiefe verhindert.
**Entscheidung:** Das Repo wird für German als Leser geschrieben. Arbeits-Ebene darf Fach-Sprache, Detail und ehrliche Risiko-Analyse enthalten. Silvio-Dokumente entstehen bei Bedarf als explizite Ableitungen in einem eigenen Ordner (vorläufig: `docs/silvio-derivatives/`, erst anlegen wenn die erste Ableitung entsteht).
**Rationale:** Germans Arbeits-Produktivität war durch den Silvio-Tonzwang eingeschränkt. Silvio braucht maximal 2-3 kurze, freundschaftlich formulierte Dokumente — alles andere ist interne Arbeit. Trennung hebt beide Seiten.
**Alternativen geprüft:** (a) Status Quo beibehalten (alles Silvio-facing) — verworfen, verhindert Arbeits-Tiefe. (b) Silvio-Tone nur in README, alles andere technisch — teilweise umgesetzt in Session 1, bleibt aber inkonsequent.
**Affects:** `README.md` (Umschrift in Session 3), `docs/plans/rollout-plan.md` (Umschrift oder Split in Session 3), evtl. neuer Ordner `docs/silvio-derivatives/`. Der Silvio-Leitsatz *"nicht überreden, nicht verkaufen, nicht drängen"* gilt weiterhin, aber nur für Ableitungen, nicht für die Arbeits-Ebene.
**Revidierbar:** Nein, Grundprinzip.

## D-07: Offene Beteiligung, von Anfang an transparent

**Datum:** 2026-04-11 (MASCHIN-Review-Klärung)
**Context:** German erwägt, sich finanziell an der Retail-Extension zu beteiligen. Die Frage war, ob das als versteckte Angel-Struktur laufen soll (Silvio erfährt es erst spät) oder offen von Beginn an.
**Entscheidung:** Offene Beteiligung. Silvio weiß von Anfang an, dass German finanzielle Beteiligung erwägt. Kein Conflict-of-Interest-Aufbau. Spätester Kommunikations-Zeitpunkt: bevor Silvio eigenes Geld ausgibt.
**Rationale:** Freundschaftsdienst und verdecktes Finanz-Interesse passen nicht zusammen. Transparenz schützt die Beziehung, egal wie das Projekt ausgeht. Form (Betrag, Terms, Timing) ist offen und wird in `docs/beteiligung.md` entwickelt.
**Alternativen geprüft:** (a) Versteckte Angel-Struktur mit späterem Disclosure — verworfen, Risiko für Freundschaft zu hoch. (b) Keine Beteiligung, reiner Freundschaftsdienst ohne Geld — möglich, aber German will die Option offen halten.
**Affects:** `docs/beteiligung.md` (neu in dieser Session als Gerüst).
**Revidierbar:** Form der Beteiligung ja, Transparenz-Prinzip nein.

## D-08: Lebenszyklus Phase A / B / C

**Datum:** 2026-04-11 (MASCHIN-Review-Klärung)
**Context:** Das Repo wurde ohne expliziten Lebenszyklus aufgesetzt. Ohne Phasen-Definition besteht die Gefahr, dass jede Folge-Session das Repo wie eine dauerhafte Knowledge-Base behandelt und Over-Engineering einführt.
**Entscheidung:** Drei Phasen. **Phase A:** aktiv, bis Silvio eine Entscheidung trifft (Ja / Nein / Später). **Phase B:** bei Ja reduziert aktiv, bis der Pilot-Verkauf stabil läuft. **Phase C:** danach niedrige Flamme als Kontext-Speicher, keine Weiterentwicklung.
**Rationale:** Jede Phase hat ein klares Aktivitäts-Niveau und ein klares Ende. Kein Repo-für-die-Ewigkeit-Framing. Lean bleibt lean, weil jede Maßnahme sich am aktuellen Phase-Bedarf messen lassen muss.
**Alternativen geprüft:** (a) Keine Phasen, Repo läuft weiter bis abgeschaltet — verworfen, lädt zu Over-Engineering ein. (b) Nur zwei Phasen (aktiv / archiv) — zu grob, verliert das Pilot-Zwischenstadium.
**Affects:** `session-state.md` (neuer Phase-Absatz in dieser Session), künftige Session-Scopes.
**Revidierbar:** Nein, Grundprinzip.
