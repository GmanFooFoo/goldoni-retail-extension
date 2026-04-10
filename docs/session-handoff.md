# Session-Handoff — wie du Sessions schließt und neu startest

> Praktische Anleitung für German: wie du eine Claude-Code-Session in diesem Repo sauber beendest und beim nächsten Mal nahtlos anschließt, auch wenn dazwischen Tage liegen und du das Fenster einmal ganz geschlossen hast.

## Session starten

```bash
cd ~/Developer/projects/goldoni-retail-extension
claude
```

Claude Code lädt automatisch die `CLAUDE.md` aus dem Repo-Root — damit ist der Projekt-Kontext (Rollen, Regeln, Struktur) sofort aktiv. Außerdem werden automatisch die **Projekt-Memories** aus `~/.claude/projects/-Users-germanrauhut-com-Developer-projects-goldoni-retail-extension/memory/` geladen, in denen alle bisher gelernten Präferenzen, Entscheidungen und Konventionen stehen (Silvio-Profil, Ton-Regeln, kein Marcello, keine Hard-Wraps, Pushback-Erwartung etc.).

**Session-Start-Checkliste (sollte die Session beim ersten Tool-Call automatisch abarbeiten):**

1. **`MEMORY.md` lesen** und die referenzierten Memory-Dateien durchgehen — besonders `project_silvio_profile.md`, `project_no_marcello_persona.md`, `feedback_pushback_expected.md`, `feedback_no_hard_wraps.md`.
2. **`session-state.md`** im Repo-Root lesen — der aktuelle Stage-Fortschritt steht dort.
3. **`SESSION-PROMPT-NEXT.md`** lesen, falls sie existiert — das ist die konkrete Aufgabe für diese Session von der vorigen Session.
4. **`docs/reports/`** — jüngsten Report überfliegen, um den letzten Stand zu verstehen.
5. **`git log --oneline -10`** — die letzten Commits scannen.
6. **`gh issue list --state open`** — offene GitHub Issues für Silvio-Feedback etc. prüfen.

Wenn diese sechs Punkte abgehakt sind, hat die neue Session den vollen Kontext und kann loslegen.

**Erste Nachricht in der neuen Session:** kurz und klar. Zum Beispiel:

> "Hallo, ich hatte gestern Abend mit Silvio gesprochen. Drei neue Infos: (1) echter Nachname ist Bianchi, (2) Restaurant-Adresse ist Musterstraße 42, 70197 Stuttgart, (3) er hat schon einen Henkelman Jumbo 30 (nicht 42). Bitte die relevanten Dokumente updaten."

Die Session liest dann den Kontext wie oben beschrieben und schlägt einen Arbeitsblock vor.

## Die drei Interaktions-Modi

### 1. Auftrag (Execution)

Du hast eine klare Aufgabe, die Session arbeitet sie ab.

**Beispiel:** "Schreib Doc 02 v2 basierend auf den Findings. Nutze die echten Di-Gennaro-Preise aus Issue #7."

Ergebnis: Arbeitsblock, Commit nach jedem Block, Rückfragen nur bei echter Unklarheit.

### 2. Diskussion (Brainstorming)

Du willst eine Entscheidung durchdenken und deine Annahmen challengen lassen.

**Beispiel:** "Silvio überlegt, ob er auch eine vegetarische Linie aufbaut. Was spricht dafür, was dagegen?"

Ergebnis: Pro/Contra, aber **nichts commitet**. Erst wenn du sagst "ok, dokumentier das als neuen Doc 20", wird geschrieben.

### 3. Review (Quality Check)

Du willst ein Dokument oder eine Entscheidung aus Fachperspektiven prüfen lassen.

**Beispiel:** "Lass Marcus, Dr. Steiger und Bruno einen Review auf Doc 19 (Sortimentserweiterung) laufen."

Ergebnis: Reviews nach Standard-Format in `docs/reviews/`, pro Persona eine Datei.

**Wichtig:** Sag klar, welchen Modus du willst. Wenn du mit "ich überlege gerade..." anfängst, ist das Diskussion. Wenn du mit "mach bitte..." anfängst, ist das Auftrag. Das spart Rückfragen.

## Feedback einspeisen (der wichtigste Workflow)

Du und Silvio redet viel. Das meiste davon landet nicht sofort im Repo. Deshalb der GitHub-Issue-Kanal:

1. **Unterwegs:** Im Gespräch mit Silvio, in der Recherche, beim Spaziergang — sobald du eine neue Info hast, leg ein GitHub Issue an:
   ```bash
   gh issue create --label feedback-silvio --title "Silvio hat Henkelman Jumbo 30 (nicht 42)"
   ```
   Oder über die GitHub-Mobile-App. Oder über die Web-Oberfläche. Der Punkt ist: **sofort**, bevor du es vergisst.
2. **In der nächsten Session:** Du sagst "arbeite die offenen Issues mit Label `feedback-silvio` ab". Die Session holt sie via `gh issue list`, priorisiert, schlägt vor, welche zuerst angefasst werden.
3. **Nach der Bearbeitung:** Issues werden mit einem Commit-Ref geschlossen (`gh issue close #7 --comment "Erledigt in commit abc123"`).

**Anti-Pattern:** Feedback in einer laufenden Session einwerfen, ohne es als Issue zu sichern. Wenn die Session crashed oder der Context voll ist, ist die Info weg.

## Decisions und Architecture

Wichtige Entscheidungen werden dokumentiert, nicht nur geträfen. Alle Entscheidungen landen in `docs/findings/decisions.md` im Format:

```markdown
## D-XX: [Titel]

**Datum:** YYYY-MM-DD
**Context:** Warum musste entschieden werden?
**Entscheidung:** Was wurde entschieden?
**Rationale:** Warum so und nicht anders?
**Alternativen geprüft:** ...
**Affects:** Welche Dokumente/Pläne müssen angepasst werden?
**Revidierbar:** Ja / Nein / Nur bis [Datum]
```

Die Session schlägt Entscheidungen vor, du nickst oder überstimmst. Wenn du überstimmst, wird das Rationale im Decision-Log festgehalten — nicht stumm einlenken. (Das ist die gleiche Regel wie Pushback in der globalen CLAUDE.md: nicht blind umsetzen.)

## Session-Ende

Wenn du "Feierabend", "Schluss", "das war's" oder ähnlich sagst, passiert automatisch:

1. Letzter Commit + Push
2. Session-Report in `docs/reports/YYYY-MM-DD-goldoni.md`
3. `session-state.md` aktualisieren
4. Offene Punkte in `SESSION-PROMPT-NEXT.md` für die nächste Session dokumentieren
5. Optional: kurzer Abschluss-Kommentar (Song, Zitat, Gedankenstütze — italienisch inspiriert, wenn es passt)

Du bekommst einen kurzen Abschluss-Absatz mit "heute erledigt / nächste Schritte / Blockers".

## Was hier NICHT passiert

- **Keine Real-World-Arbeit:** Es werden keine Anrufe bei Metro gemacht, kein Vetamt-Termin vereinbart, keine E-Mails verschickt. Vorbereitung ja, Ausführung bei dir.
- **Kein Code-Produkt:** Das Repo ist docs-only. Kein Shop-System, keine App, kein Webshop-Frontend. Falls das später kommt, wird das ein separates Projekt mit eigenem Setup.
- **Keine rechtliche Zusicherung:** Die Persona "Dr. Steiger" gibt Einschätzungen, aber kein Rechtsgutachten. Vor Livegang muss ein echter Anwalt drüber schauen — das ist in jedem relevanten Doc als Disclaimer verankert.
- **Keine Steuer-Zusicherung:** Gleiche Regel für "Frau Keller". Silvios echter Steuerberater muss die MwSt-Einstufung schriftlich bestätigen.
- **Keine Ersetzung von Silvio:** Alle operativen Entscheidungen (Preise, Mengen, Lieferanten, Launch-Termin) liegen bei Silvio.

## Anti-Patterns

1. **Parallel-Sessions auf dem gleichen Repo.** Genau ein Schreibender pro Repo. Check `session-state.md` bevor du eine zweite Session öffnest.
2. **Im Dialog-Modus festhängen, ohne arbeiten zu lassen.** 45 Minuten diskutieren und nichts committen ist verschwendete Zeit. Lieber: 5 Minuten diskutieren, dann "ok, mach das so", dann Commit.
3. **Findings ignorieren.** Wenn eine Persona sagt "Doc 04 hat ein juristisches Risiko bei den Nährwerten", ist das keine Meinung, sondern ein Red Flag. Entweder lösen oder bewusst als Restrisiko dokumentieren.
4. **v2-Dokumente schreiben ohne Findings.** Die Reihenfolge ist immer: Review → Findings → Plan → v2. Nicht direkt v1 → v2 "aus dem Kopf".

## Notfälle

- **Ein Commit war Mist:** `git revert <commit>`, dann der nächsten Session sagen, was schiefgelaufen ist. Oder der aktuellen Session, wenn sie noch läuft.
- **Context voll (>60%):** Neue Session. Vorher Report schreiben lassen.
- **Session hängt in einer Fix-Schleife:** Nach 3 erfolglosen Versuchen abbrechen, Analyse verlangen ("Liste was du probiert hast, nenn 3 Alternativen"), dann Option wählen.
- **GitHub-Repo kaputt:** Das lokale Repo ist immer die Wahrheit. Zur Not neu pushen nach `git remote set-url origin ...`.

## Kontakt & Governance

- **Projekt-Owner:** German Rauhut (Gman / GmanFooFoo)
- **Zielgruppe des Projekts:** Silvio, Inhaber Ristorante Goldoni Stuttgart — Freund, kein Kunde
- **Planning-Instanz außerhalb dieses Repos:** MASCHIN (in `~/Developer/projects/OMNIXIS-planning/`) — wird konsultiert bei strukturellen Fragen oder Prozess-Änderungen, aber nicht für Tagesarbeit hier
