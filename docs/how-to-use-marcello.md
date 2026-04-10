# How to use Marcello

> Leitfaden für den menschlichen Projekt-Owner (German) — wie man mit
> Marcello (Claude Code als Goldoni-Chief-of-Staff) effizient arbeitet.

## Wer ist Marcello?

Marcello ist eine **Claude-Code-Session-Persona**, spezialisiert auf das
Goldoni-Retail-Extension-Projekt. Er ist nicht MASCHIN (das ist die
Planning-Instanz für OMNIXIS) und nicht Sensei (private Projekte). Er ist
Marcello: italienischer Business-Berater mit McKinsey-Schärfe und
Gastronomie-Verständnis.

Marcello lebt nur in diesem Repo. Er kennt die 19 Business-Case-Dokumente,
die 9 Review-Personas, und die bisherigen Findings. Er kennt Silvio vom
Namen her, aber nicht persönlich — alle Fakten über Silvio und das
Restaurant kommen vom menschlichen Projekt-Owner.

## Wann Marcello starten?

**Gute Gelegenheiten:**

- Nach einem Gespräch mit Silvio: Feedback einspeisen, Annahmen validieren,
  offene Fragen aus GitHub Issues abarbeiten
- Nach einer Recherche (Metro-Preise, Vetamt-Auskunft, Lieferanten-Angebote):
  echte Zahlen in die Dokumente einpflegen
- Wenn neue Findings aus Reviews in v2-Dokumente überführt werden sollen
- Für Ad-hoc-Fragen ("Was wäre wenn Silvio zusätzlich Pizza-Kits anbietet?")
- Vor einem Silvio-Meeting: Gesprächsleitfaden generieren

**Schlechte Gelegenheiten:**

- Zwischendurch "nur mal schauen" ohne konkretes Ziel — Marcello ist kein
  Chatbot, er ist ein Arbeitspferd. Gib ihm einen Auftrag.
- Parallel zu einer anderen laufenden Session auf dem gleichen Repo —
  erzeugt Merge-Konflikte

## Session starten

```bash
cd ~/Developer/projects/goldoni-retail-extension
claude
```

Claude Code lädt automatisch die `CLAUDE.md` aus dem Repo-Root — damit ist
die Marcello-Persona aktiv. Kein Extra-Prompt nötig.

**Erste Nachricht in der Session:** kurz und klar. Zum Beispiel:

> "Hallo Marcello. Ich hatte gestern Abend ein Gespräch mit Silvio. Hier
> die drei neuen Infos: (1) echter Nachname ist Bianchi, (2) Restaurant-
> Adresse ist Musterstraße 42, 70197 Stuttgart, (3) er hat schon einen
> Henkelman Jumbo 30 (nicht 42). Bitte die relevanten Dokumente updaten."

Marcello liest dann den Kontext (CLAUDE.md, session-state, letzte Reports,
offene Issues) und schlägt einen Arbeitsblock vor.

## Die drei Interaktions-Modi

### 1. Auftrag (Execution)

Du hast eine klare Aufgabe, Marcello arbeitet sie ab.

**Beispiel:** "Schreib Doc 02 v2 basierend auf den Findings. Nutze die
echten Di-Gennaro-Preise aus Issue #7."

Marcello arbeitet, commitet nach jedem Block, fragt nur zurück wenn
wirklich unklar.

### 2. Diskussion (Brainstorming)

Du willst eine Entscheidung durchdenken, Marcello challenge deine
Annahmen.

**Beispiel:** "Silvio überlegt, ob er auch eine vegetarische Linie
aufbaut. Was spricht dafür, was dagegen?"

Marcello antwortet mit Pro/Contra, aber **commitet nichts**. Erst wenn
du sagst "ok, dokumentier das als neuen Doc 20" wird geschrieben.

### 3. Review (Quality Check)

Du willst ein Dokument oder eine Entscheidung prüfen lassen.

**Beispiel:** "Lass Marcus, Dr. Steiger und Bruno einen Review auf
Doc 19 (Sortimentserweiterung) laufen."

Marcello schlüpft in die Personas und liefert Reviews nach Standard-
Format in `docs/reviews/`.

**Wichtig:** Sag klar, welchen Modus du willst. Marcello ist nicht
hellseherisch. Wenn du mit "ich überlege gerade..." anfängst, ist das
Diskussion. Wenn du mit "mach bitte..." anfängst, ist das Auftrag.

## Feedback einspeisen (der wichtigste Workflow)

Silvio und du reden viel. Das meiste davon landet nicht sofort in Marcello.
Deshalb der GitHub-Issue-Kanal:

1. **Unterwegs**: Im Gespräch mit Silvio, in der Recherche, beim Spaziergang
   — sobald du eine neue Info hast, leg ein GitHub Issue an.
   ```bash
   gh issue create --label feedback-silvio --title "Silvio hat Henkelman Jumbo 30 (nicht 42)"
   ```
   Oder über die GitHub-Mobile-App. Oder über die Web-Oberfläche. Der Punkt
   ist: **sofort**, bevor du es vergisst.

2. **In der nächsten Marcello-Session**: Du sagst "Hallo Marcello, arbeite
   die offenen Issues mit Label `feedback-silvio` ab". Marcello holt sie
   via `gh issue list`, priorisiert, schlägt vor, welche er zuerst anpackt.

3. **Nach der Bearbeitung**: Marcello schließt die Issues mit einem Commit-
   Ref (`gh issue close #7 --comment "Erledigt in commit abc123"`).

**Anti-Pattern:** Feedback in einer laufenden Session einwerfen, ohne es
als Issue zu sichern. Wenn die Session crashed oder der Context voll ist,
ist die Info weg.

## Decisions und Architecture

Marcello ist ein Berater, kein Alleinentscheider. Wichtige Entscheidungen
triffst du gemeinsam mit ihm (oder überstimmst ihn, wenn du einen Grund
hast).

Alle Entscheidungen landen in `docs/findings/decisions.md` im Format:

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

Marcello schlägt Entscheidungen vor, du nickst oder überstimmst. Wenn du
ihn überstimmst, muss er dich **warum** fragen und das Rationale im
Decision-Log festhalten — nicht stumm einlenken.

## Session-Ende

Wenn du "Feierabend", "Schluss", "das war's" oder ähnlich sagst, macht
Marcello automatisch:

1. Letzten Commit + Push
2. Session-Report in `docs/reports/YYYY-MM-DD-marcello-goldoni.md`
3. `session-state.md` aktualisieren
4. Offene Punkte in `SESSION-PROMPT-NEXT.md` für die nächste Session
5. Session Close Easter Egg (Song, Quote, Poster Prompt — italienisch
   inspiriert)

Du bekommst einen kurzen Abschluss-Absatz mit "heute erledigt / nächste
Schritte / Blockers".

## Was Marcello NICHT tut

- **Keine Real-World-Arbeit:** Er ruft nicht bei Metro an, terminiert kein
  Vetamt-Gespräch, schickt keine E-Mails. Er bereitet vor, du führst aus.
- **Kein Code-Produkt:** Das Repo ist docs-only. Marcello schreibt kein
  Shop-System, keine App, kein Webshop-Frontend. (Wenn das später kommt,
  wird das ein separates Projekt mit anderer Persona.)
- **Keine rechtliche Zusicherung:** Dr. Steiger (Persona) gibt Einschätzungen,
  aber kein Rechtsgutachten. Vor Livegang muss ein echter Anwalt drüber
  schauen — das ist in jedem relevanten Doc als Disclaimer verankert.
- **Keine Steuer-Zusicherung:** Gleiche Regel für Frau Keller. Silvios
  echter Steuerberater muss die MwSt-Einstufung schriftlich bestätigen.
- **Keine Ersetzung von Silvio:** Marcello kann vieles annehmen, aber alle
  operativen Entscheidungen (Preise, Mengen, Lieferanten, Launch-Termin)
  liegen bei Silvio.

## Anti-Patterns (was du vermeiden solltest)

1. **Parallel-Sessions auf dem gleichen Repo.** Genau einen Schreibenden
   pro Repo. Check `session-state.md` bevor du eine zweite Session öffnest.
2. **Marcello im Dialog-Modus halten, ohne ihn arbeiten zu lassen.** 45 min
   diskutieren und nichts committen ist Verschwendung. Lieber: 5 min
   diskutieren, dann "ok, mach das so", dann er commitet.
3. **Findings ignorieren.** Wenn eine Persona sagt "Doc 04 hat ein
   juristisches Risiko bei den Nährwerten", ist das keine Meinung, das
   ist ein Red Flag. Entweder lösen oder bewusst als Restrisiko
   dokumentieren.
4. **Die Reader-Site nicht mit Silvio teilen.** Der ganze Aufwand ist
   umsonst wenn Silvio die URL nie bekommt. Sobald Stufe 1 fertig ist:
   URL + Passwort an Silvio, kurze Einführung ("hier siehst du den Stand,
   hier kannst du mir Feedback geben").
5. **v2-Dokumente schreiben ohne Findings.** Die Reihenfolge ist immer:
   Review → Findings → Plan → v2. Nicht direkt v1 → v2 "aus dem Kopf".

## Notfälle

- **Marcello hat Mist geschrieben und commited:** `git revert <commit>`,
  dann der nächsten Session sagen was schief lief. Oder der aktuellen
  Session, wenn sie noch läuft.
- **Context voll (>60%):** Neue Session. Vorher Report schreiben lassen.
- **Marcello bleibt hängen in einer Fix-Schleife:** Nach 3 erfolglosen
  Versuchen abbrechen, Analyse verlangen ("Liste was du probiert hast,
  nenn 3 Alternativen"), dann Option wählen.
- **GitHub-Repo kaputt:** Das lokale Repo ist immer die Wahrheit. Zur Not
  neu pushen nach `git remote set-url origin ...`.

## Kontakt & Governance

- **Projekt-Owner:** German Rauhut (Gman / GmanFooFoo)
- **Kunde:** Silvio [TBD-Nachname], Goldoni Stuttgart
- **Marcello's Chef:** MASCHIN (in `~/Developer/projects/OMNIXIS-planning/`)
  — wird konsultiert bei strukturellen Fragen oder Prozess-Änderungen

---

*Buona fortuna. Und vergiss nicht: Silvio hat ein Restaurant zu führen,
nicht ein Git-Repo zu pflegen. Alles was wir hier machen, muss am Ende
in seiner Welt funktionieren — nicht in unserer.*
