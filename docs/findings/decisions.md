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

## D-07: Kein Investment — Aufwandsentschädigung bei Umsetzung, von Anfang an transparent

**Datum:** 2026-04-11, revidiert in Session 8 (Persona-99-Deep-Dive)
**Context:** In Session 2b wurde die Frage offen gelassen, *in welcher Form* German sich finanziell beteiligt — mit Angel-Investor-Optionen (Gewinn-Beteiligung, Darlehen, JV, stille Einlage) als offene Dimensionen in einem eigenen Gerüst-Dokument. Der Persona-99-Deep-Dive in Session 8 hat die Haltung geklärt: German ist kein Investor, das Projekt ist Freundschaftsdienst.
**Entscheidung:** Kein Investment, keine Rendite-Erwartung, keine Gewinn-Beteiligung. Wenn Silvio die Retail-Extension umsetzt und Germans Unterstützung dafür annimmt, kann eine finanzielle Komponente hinzukommen — ausschließlich auf **Selbstkosten-/Aufwandsentschädigungs-Basis**, als Anerkennung für fokussierte Zeit neben Germans anderen Projekten. Transparenz-Prinzip bleibt: Silvio weiß das, bevor er den ersten Euro selbst ausgibt.
**Rationale:** Freundschaftsdienst und Eigen-Investment-Interesse sind unvereinbar. Die Angel-Optik aus Session 2b (`beteiligung.md`-Gerüst mit "Rückzahlungs-Modell") war eine frühe Fehl-Framing — sie hat eine Investment-Frage gestellt, die es nicht gibt. P99 stellt die richtige Frage: nicht "wie strukturiere ich mein Investment", sondern "wie wird der zusätzliche Zeiteinsatz fair anerkannt, ohne die Freundschaft zu kippen".
**Alternativen geprüft:** (a) Offene Investment-Struktur mit vier Dimensionen (Session 2b) — verworfen, falsches Framing. (b) Rein ideeller Freundschaftsdienst ohne jede finanzielle Komponente — bleibt als Default-Pfad gültig, falls Silvio umsetzt aber keine zusätzliche Unterstützung annimmt. (c) Versteckte Angel-Struktur mit späterem Disclosure — verworfen, Risiko für Freundschaft zu hoch.
**Affects:** `docs/personas/Persona 99 – German – Freund und Berater.md` trägt die Haltung. `docs/beteiligung.md` in Session 9 gelöscht (war obsoletes Gerüst aus Session 2b).
**Revidierbar:** Nein. Aufwandsentschädigungs-Rahmen und Transparenz-Prinzip sind Grundhaltung.

## D-08: Lebenszyklus Phase A / B / C

**Datum:** 2026-04-11 (MASCHIN-Review-Klärung)
**Context:** Das Repo wurde ohne expliziten Lebenszyklus aufgesetzt. Ohne Phasen-Definition besteht die Gefahr, dass jede Folge-Session das Repo wie eine dauerhafte Knowledge-Base behandelt und Over-Engineering einführt.
**Entscheidung:** Drei Phasen. **Phase A:** aktiv, bis Silvio eine Entscheidung trifft (Ja / Nein / Später). **Phase B:** bei Ja reduziert aktiv, bis der Pilot-Verkauf stabil läuft. **Phase C:** danach niedrige Flamme als Kontext-Speicher, keine Weiterentwicklung.
**Rationale:** Jede Phase hat ein klares Aktivitäts-Niveau und ein klares Ende. Kein Repo-für-die-Ewigkeit-Framing. Lean bleibt lean, weil jede Maßnahme sich am aktuellen Phase-Bedarf messen lassen muss.
**Alternativen geprüft:** (a) Keine Phasen, Repo läuft weiter bis abgeschaltet — verworfen, lädt zu Over-Engineering ein. (b) Nur zwei Phasen (aktiv / archiv) — zu grob, verliert das Pilot-Zwischenstadium.
**Affects:** `session-state.md` (neuer Phase-Absatz in dieser Session), künftige Session-Scopes.
**Revidierbar:** Nein, Grundprinzip.

## D-09: Schreibort Rückruf-Prozess — Doc 14 = Haftung, Doc 05 = Hygiene

**Datum:** 2026-04-11 (Session 7, Doc-14-Lead-Review), nachgetragen Session 9
**Context:** Nach dem Doc-05-Lead-Review in Session 5 war unklar, wo der Rückruf-Prozess eigentlich geschrieben wird — in Doc 05 (Hygiene/HACCP) oder in Doc 14 (Recht/Versicherung). Zwei mögliche Schreib-Orte ohne klare Trennung führen zu Dopplung und Widerspruchs-Risiko. Inkonsistenz #11 in `docs/findings/inconsistencies.md`.
**Entscheidung:** Der Rückruf-Prozess wird in **zwei Ebenen** geschrieben, nicht an einem Ort. **Doc 14** = Haftungs- und Krisen-Prozess: rechtliche Pflichten aus Art. 19 BasisVO 178/2002, Kommunikation Kunde/Vetamt/Presse, Dokumentation als Beweismittel, Versicherungs-Obliegenheiten. **Doc 05** = Hygiene- und Chargen-Prozess: Chargen-Identifikation, Warenfluss, HACCP-CCP-Trigger, Rückstellproben. Beide Docs verlinken sich gegenseitig, damit der Leser von jeder Seite aus die vollständige Sicht hat.
**Rationale:** Die zwei Aspekte haben unterschiedliche Leser, unterschiedliche Aktualisierungs-Rhythmen und unterschiedliche Regulatorik-Quellen. Zusammenlegen macht den zusammengelegten Ort für beide Zielgruppen schlechter. Die Trennung folgt der fachlichen Logik der Gesetze (LFGB/BasisVO vs. HACCP-System).
**Alternativen geprüft:** (a) Alles in Doc 14 — verworfen, erschwert den Hygiene-Blickwinkel. (b) Alles in Doc 05 — verworfen, vermischt HACCP-Prozess mit Rechts-Prozess und macht beide schwer lesbar. (c) Neues Doc 20 "Rückruf" — verworfen in Session 7, hätte zu viel Neu-Scope erzeugt.
**Affects:** Doc 05 und Doc 14 in v2-Rewrite, `docs/findings/inconsistencies.md` #11 (aufgelöst), spätere Co-Reviews müssen die Cross-Links prüfen.
**Revidierbar:** Ja — falls ein Co-Review oder Silvio-Feedback zeigt, dass eine der Ebenen zu dünn bleibt.

## D-10: Silvio ist kein Reviewer — Silvio-Paket als eigenes Artefakt

**Datum:** Session 7, nachgetragen Session 9
**Context:** In Sessions 3 bis 6 ist Silvio systematisch in die `Wer`-Spalten von Findings- und Inconsistency-Tabellen geschrieben worden — als wäre er ein Reviewer wie CFO, Lebensmittelrechtler, Steuerberaterin. Das hat zwei Probleme verdeckt: (a) Silvio ist der **Kunde** der Review-Arbeit, nicht ihr Mitarbeiter, und (b) die Liste seiner tatsächlichen Handlungen (Telefonate, Termine, Entscheidungen) war nur in Prosa verstreut, nicht als Artefakt greifbar.
**Entscheidung:** Silvio steht **nie** in der `Wer`-Spalte von Review-Artefakten. Die `Wer`-Spalte ist Review-Personas vorbehalten (CFO, Lebensmittelrechtler, Steuerberaterin, Behördenkontrolleur, Logistiker, Gastronom-Praktiker, Küchenchef, Brand/Marketing, Stammgast, Dr. Maldini). Jede Aktion, die Silvio selbst ausführen muss, wird als Eintrag `SP-XX` im zentralen Artefakt `docs/silvio-paket/offene-fragen.md` geführt. Findings und Inconsistencies verweisen stattdessen per `→ Silvio-Paket SP-XX`. Ausgang (Claude → German → Silvio) läuft über das Silvio-Paket; Eingang (Silvio → German → Repo) läuft über GitHub-Issues mit Label `feedback-silvio`.
**Rationale:** Ein Artefakt statt verstreuter Prosa sorgt dafür, dass Silvios Liste vollständig, priorisierbar und übergabefähig ist. Die Rollen-Klarheit schützt außerdem den Review-Prozess selbst: Personas sind Denk-Werkzeuge mit Fach-Haltung, Silvio ist der Entscheider — beides zu vermischen macht beide Seiten ungenau.
**Alternativen geprüft:** (a) Status quo mit Silvio in Wer-Spalten — verworfen, Strukturfehler. (b) Mehrere Silvio-Listen pro Doc — verworfen, fragmentiert den Ausgang an Silvio.
**Affects:** `CLAUDE.md` Rule 10, `docs/silvio-paket/offene-fragen.md` (SP-01 bis SP-18 in Session 7 angelegt), alle Findings- und Inconsistency-Tabellen ab Session 7, `docs/session-handoff.md` (Feedback-Workflow).
**Revidierbar:** Nein, Grundprinzip der Rollen-Trennung.
