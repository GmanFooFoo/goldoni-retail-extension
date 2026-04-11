# Doc 20 — Personal-Setup Retail (Szenarien A/B/C)

> **Status:** Szenario-Ebene. Dieses Doc trifft **keine** Vorentscheidung, welches Szenario das richtige ist. Es stellt die drei realistischen Wege gegenüber, damit Silvio entscheiden kann und Persona 11 (Personal-Markt & Arbeitsrecht Retail) daran reviewen kann. Alle Markt-Daten und Stundenlohn-Annahmen sind mit `[TBD-Recherche]` markiert, bis Persona 11 den ersten Lead-Review geschrieben hat.

## Kontext

Die Vakuum-Produktion für den Retail-Strang läuft **vormittags**, zwischen ~9 und ~14 Uhr, in Silvios Restaurant-Küche, außerhalb der Service-Zeiten (Mi + Do–So 17–22 Uhr). Diese Zeitlage ist Ergebnis des Rollout-Plans (siehe `docs/plans/rollout-plan.md`) und der Küche-Tagesablauf-Logik aus den Doc-05-Findings. Die Frage "wer steht vormittags in der Küche und produziert Lasagne, Sugo, Ragù, Parmigiana vakuumiert" ist noch offen.

Das Doc führt drei Szenarien durch. Jedes Szenario hat vier tragende Spalten: **Wer produziert**, **Kosten-Rahmen**, **Rechtliche Form**, **Ausfall-Risiko**. Zusätzlich eine kurze Prosa-Einordnung, die die Haken sichtbar macht — nicht als Empfehlung, sondern als ehrliche Darstellung der Konsequenzen.

Die drei Szenarien sind **nicht exklusiv**. Ein Misch-Modell (Szenario A + C als Redundanz, oder B + C) ist in späteren Iterationen möglich. Diese Version bleibt bei den drei Reinformen, um die Unterschiede klar zu machen.

## Szenarien — Vergleichstabelle

| # | Szenario | Wer produziert vormittags | Kosten-Rahmen (Monat) | Rechtliche Form | Ausfall-Risiko |
|---|---|---|---|---|---|
| A | Ehefrau | Silvios Ehefrau, in der Restaurant-Küche, zwischen ~9 und ~14 Uhr | `[TBD-Recherche]` Ehegatten-Arbeitsvertrag bei marktüblichem Lohn, rund `[TBD-Recherche]` €/h × ~20 h/Woche | Ehegatten-Arbeitsvertrag mit Fremdvergleich, schriftlich, eigenes Lohn-Konto, regelmäßige Überweisung, IfSG-Belehrung | Hoch — Ein-Personen-Abhängigkeit, bei Ausfall (Krankheit, Familie) sofort Produktions-Stopp. Keine Redundanz im Reinform-Szenario. |
| B | Externer einfacher Koch / Hilfe | Extern angestellte Kraft (einfacher Koch oder Küchenhilfe), nicht Gesellen-Koch | `[TBD-Recherche]` rund `[TBD-Recherche]` €/h × ~20 h/Woche; bei ~20 h/Woche tendenziell über Minijob-Grenze (556 € Stand 2026 `[TBD-Recherche]`) → SV-pflichtige Teilzeit wahrscheinlich | Teilzeit-Arbeitsvertrag, SV-pflichtig. Minijob nur, wenn Arbeitszeit unter der 556-€-Grenze bleibt. **Nie als "freier Mitarbeiter auf Rechnung"** (Scheinselbständigkeits-Risiko). | Mittel — externe Kraft ist ersetzbar, aber Suche am Stuttgarter Markt dauert `[TBD-Recherche]` Wochen. Redundanz nur durch zweite Kraft, was das Kosten-Modell sprengt. |
| C | Silvio selbst | Silvio selbst, vor dem Service-Fenster | Kein zusätzlicher Personalkosten-Block, aber Opportunitäts-Kosten: Silvio hat die Vormittage nicht mehr für Einkauf, Küchenplanung, Verwaltung, Erholung | Keine arbeitsrechtliche Form nötig (Inhaber), keine Lohn-Abrechnung, kein zusätzlicher Vertrag | Sehr hoch — Ein-Personen-Abhängigkeit im Extrem. Fällt Silvio aus, fällt **Restaurant und Retail gleichzeitig** aus. Kein Puffer. Belastungs-Grenze realistisch 6–12 Monate `[TBD-Recherche]`, dann droht Burnout oder Qualitäts-Verfall. |

## Szenario A — Ehefrau

Silvios Ehefrau übernimmt die Vormittags-Produktion. Sie kennt das Restaurant, die Rezepturen, die Abläufe, und ist rechtlich-organisatorisch bereits im Betrieb verankert. Der Weg ist operativ einfach, weil keine externe Person eingelernt werden muss.

Der kritische Punkt ist die rechtliche Form. Eine "hilft eben mit"-Konstruktion ohne schriftlichen Arbeitsvertrag, ohne Lohn-Konto und ohne Fremdvergleich wird steuerlich und sozialversicherungsrechtlich nicht anerkannt — mit der Folge, dass im Schadenfall (Verletzung in der Küche, Hygiene-Vorfall) kein Versicherungsschutz greift und bei einer Prüfung Nachzahlungen drohen. Der saubere Weg ist: schriftlicher Ehegatten-Arbeitsvertrag, marktüblicher Lohn, eigenes Lohn-Konto, regelmäßige Überweisung, IfSG-Belehrung wie bei jeder anderen Küchenkraft. Die Kriterien stehen im Lead-Review von Persona 11.

Die zweite offene Frage — ob Silvios Ehefrau diese Rolle überhaupt annehmen will, und wie sich Doppelrolle Restaurant + Retail auf die familiäre Belastung auswirkt — ist **nicht Gegenstand dieses Docs und nicht Gegenstand der Persona-11-Review**. Das ist Silvios Revier, und es gehört in Silvios persönliche Entscheidung, nicht in eine Fach-Review.

Das Ausfall-Risiko ist in Reinform hoch, weil es keine zweite Person gibt, die einspringen kann. Eine Redundanz-Option (zweite Kraft auf Minijob als Backup, oder Silvio selbst als Backup für einzelne Tage) verringert das Risiko, macht das Szenario aber teurer und gehört in eine spätere Iteration.

## Szenario B — Externer einfacher Koch / Küchenhilfe

Silvio stellt eine externe Kraft an, die vormittags die Vakuum-Produktion übernimmt. Nicht zwingend ein Gesellen-Koch — eine angelernte Kraft mit Lebensmittel-Hygiene-Grundlagen und der Bereitschaft, sich auf die Rezepturen einzuarbeiten, reicht für die geplante Produktionstiefe (vier Gerichte in konstanter Qualität, nicht Drei-Sterne-Innovation). Der Kandidaten-Pool ist in Stuttgart `[TBD-Recherche]` — Persona 11 muss beurteilen, ob der Markt einen solchen Kandidaten hergibt und zu welchem Stundenlohn.

Der rechtliche Rahmen entscheidet sich an der Arbeitszeit. Bei ~20 Stunden pro Woche und ~15–18 €/h `[TBD-Recherche]` liegt das Monatsbrutto über der Minijob-Grenze von 556 € (Stand 2026 `[TBD-Recherche]`), damit ist ein SV-pflichtiger Teilzeit-Vertrag wahrscheinlich. Die Konstruktion "freier Mitarbeiter auf Rechnung" ist **nicht zulässig** — bei festen vormittäglichen Zeiten, Weisungsgebundenheit, Eingliederung in den Betrieb und einem einzigen Auftraggeber erfüllt sie alle Merkmale der Scheinselbständigkeit, mit Nachzahlungs-Risiko bis vier Jahre zurück. Der saubere Weg ist Teilzeit mit Lohnabrechnung, IfSG-Belehrung, schriftlichem Vertrag.

Das Ausfall-Risiko ist mittel. Externe Kräfte sind theoretisch ersetzbar, aber die Suche dauert, und während der Suche steht die Produktion. Die Haltbarkeit der Vakuumware ist endlich, der Kunden-Vertrag (Abholung zu einem zugesagten Termin) nicht einfach verschiebbar. Eine zweite Kraft als Backup würde das Risiko lösen, verdoppelt aber den Personalkosten-Block. Diese Abwägung gehört in Doc 02 Wirtschaftlichkeitsrechnung.

## Szenario C — Silvio selbst

Silvio produziert die Vakuum-Ware vormittags selbst, vor dem Service-Fenster um 17 Uhr. Kein zusätzlicher Personalkosten-Block, keine arbeitsrechtlichen Fragen, keine Einlern-Zeit. Auf dem Papier das schlankste Szenario.

Der versteckte Preis sind die Opportunitäts-Kosten. Silvios Vormittage sind heute nicht leer — sie werden für Einkauf, Lieferanten-Gespräche, Küchenplanung, Verwaltung, Reservierungen, Personal-Themen, und für die Erholungs-Zeit gebraucht, die einen Gastronomen durch die Abend-Service-Belastung trägt. Fällt die Vormittags-Erholung weg, steigt die Belastungs-Grenze sichtbar, und die Qualität im Abend-Service ist das erste, was darunter leidet. Das ist kein Burnout-Alarmismus, sondern eine nüchterne Alltags-Rechnung für einen 25-Jahre-Gastronom.

Das Ausfall-Risiko ist in diesem Szenario am höchsten, auch wenn das auf den ersten Blick paradox wirkt. Wenn Silvio vormittags produziert und abends den Service führt, ist er der einzige Produktions-Punkt des Restaurants — fällt er aus, fallen Restaurant und Retail gleichzeitig aus. Eine Ein-Personen-Abhängigkeit im Extrem, ohne jeden Puffer.

Szenario C ist realistisch als **Pilot-Phase-Lösung** für wenige Wochen (erster Monat Produktion, Testbetrieb, Rezeptur-Feinschliff), nicht als Dauer-Modell. Der Wechsel zu A oder B muss als Meilenstein im Rollout-Plan eingeplant sein, nicht als "sehen wir dann".

## Non-Goals dieses Docs

- **Will Silvios Ehefrau Szenario A?** — nicht Gegenstand, Silvios Revier.
- **Emotionale Familien-Belastung, Beziehungs-Dynamik, Rollen-Verteilung im Haushalt.** — nicht Gegenstand.
- **Welche konkrete Person könnte Szenario B füllen?** — nicht Gegenstand. Persona 11 liefert Markt-Rahmen, nicht Einzel-Empfehlung.
- **Küchen-Handwerks-Eignung einer konkreten Person für Rezeptur-Qualität.** — Persona 07 Küchenchef.
- **Team-Dynamik Restaurant-Küchenteam ↔ Retail-Produktions-Kraft.** — Persona 06 Gastronom-Praktiker, wenn relevant.
- **Entscheidung.** Dieses Doc trifft keine Wahl. Die Entscheidung fällt Silvio nach Persona-11-Review und nach einer Silvio-Paket-Rückmeldung.

## Offene `[TBD-Recherche]`-Marker

1. Stundenlohn-Spanne 2026 für einfache Küchenkräfte / Küchenhilfen im Stuttgarter Markt (vormittags-Verfügbarkeit).
2. Minijob-Monats-Grenze 2026 (nach aktuellem Kenntnisstand 556 €, zu bestätigen).
3. Durchschnittliche Suchdauer Stuttgart für eine Teilzeit-Küchenhilfe mit Vormittags-Verfügbarkeit über IHK-Jobbörse, Arbeitsagentur, Community-Kanäle.
4. Marktüblicher Fremdvergleichs-Lohn für einen Ehegatten-Arbeitsvertrag in derselben Rolle (Bezugspunkt für die steuerliche Anerkennung).
5. Belastungs-Grenze für Szenario C — welcher Zeitraum ist realistisch, bevor Qualität oder Gesundheit kippen? Keine medizinische Aussage, sondern erfahrungsbasierter Rahmen.
6. Minijob-Pauschalabgaben und Arbeitgeber-Brutto-Belastungs-Quote 2026 (für Kosten-Rechnung Szenario B bei Minijob-Variante).

## Verweise

- `docs/personas/Persona 11 – Personal-Markt & Arbeitsrecht Retail.md` — Lead-Review-Persona für dieses Doc.
- `docs/plans/rollout-plan.md` — Vormittags-Fenster und Personal-Annahme werden dort in Session 9 nachgezogen.
- `docs/business-case/02 – Wirtschaftlichkeitsrechnung.md` — Personalkosten-Block muss die drei Szenarien als Sensitivitäts-Fälle aufnehmen, sobald Persona 11 die `[TBD-Recherche]`-Marker aufgelöst hat.
- `docs/business-case/10 – Operative Umsetzung.md` — Tagesablauf-Sektion muss das Vormittags-Fenster explizit ausweisen.
- `docs/business-case/13 – 6-Wochen-Rollout-Plan.md` — Meilenstein "Wechsel von Szenario C zu A oder B" gehört rein, falls die Pilot-Phase mit Szenario C läuft.
- `docs/findings/session-8-persona-deep-dive-findings.md` — Findings 4 und 5 (Vormittags-Fenster, einfacher Koch statt zweiter Chef) sind die Grundlage für dieses Doc.
