# Rollout-Plan Phase 1 — Vakuum gekühlt

Interner Arbeitsplan für die Retail-Extension Goldoni, Phase 1. Nicht Silvio-facing. Eine Silvio-Ableitung wird ad-hoc erstellt, falls gebraucht (D-06, Variante B).

## Scope-Fixierung

Phase 1: **Vakuum, gekühlt, Haltbarkeit nominell 7 Tage ab Produktion**. Abholung im Restaurant. Start-Sortiment: Lasagne, Sugo, Ragù, Parmigiana. Tiefkühl, Schockfroster, MAP/Schutzgas, Versand, Wiederverkauf über Dritte sind bewusst ausgeschlossen (D-02).

Das Ausschluss-Argument ist doppelt: (1) Kapitalbedarf für Schockfroster 2.000–5.000 € entfällt, (2) das Vetamt-Verfahren ist signifikant einfacher, weil keine Gefrierkette, keine zusätzlichen HACCP-CCPs für Einfrier-Temperaturkurven, keine erweiterten Kennzeichnungs-Pflichten. Phase 2 (Tiefkühl) bleibt optional nach 6–12 Monaten stabilem Pilot.

## Regulatorische Stichtage 2026 (Gate-kritisch)

Zwei harte Rechts-Stichtage im zweiten Halbjahr 2026 beeinflussen Launch-Timing, Verpackung und Haftungsrahmen unmittelbar. Vor jedem dieser Stichtage gilt das alte Recht, ab dem Stichtag automatisch das neue — ohne Übergangsfrist, ohne Silvio-Entscheidung. Details in den Reviews Doc 04 (LMIV/Verpackung) und Doc 14 (Haftung/Recht).

| # | Stichtag | Regelwerk | Wirkung auf Phase 1 | Quelle |
|---|---|---|---|---|
| 1 | **12.08.2026** | **PPWR** — Verordnung (EU) 2025/40 über Verpackungen und Verpackungsabfälle | Ab Stichtag: Rezyklat-Anforderungen, Wiederverwendbarkeits-Quoten, neue Kennzeichnungs-Pflichten für Verpackungen, Minimierungs-Prinzip. Direkte Wirkung auf Beutel-Auswahl und Etiketten-Layout. Beutel, die vor dem Stichtag beschafft und danach verwendet werden, können compliant bleiben — aber nur mit Nachweis. | [Doc-04-Review Regulatorik-Nachtrag](../reviews/04-lmiv-lebensmittelrechtler.md) |
| 2 | **09.12.2026** | **ProdHaftG-Novelle** (Umsetzung EU-RL 2024/2853, BR-Drs. 775/25) | Ab Stichtag: Wegfall des 500 €-Selbstbehalts, Wegfall der 85-Mio-Cap, Beweiserleichterung bei technisch-wissenschaftlicher Komplexität, 25-Jahres-Höchstverjährung. Chargen-Dokumentation wird ab diesem Datum Zivilprozess-Beweismittel, nicht mehr nur Behörden-Unterlage. Versicherungs-Anforderungen steigen implizit. | [Doc-14-Review Regulatorik-Nachtrag](../reviews/14-recht-lebensmittelrechtler.md) |

**Launch-Timing-Entscheidung (SP-13):** Silvio hat drei Optionen — Launch vor 12.08.2026 (altes Verpackungs-Regime, altes ProdHaftG), Launch zwischen 12.08. und 09.12.2026 (PPWR greift, altes ProdHaftG), Launch nach 09.12.2026 (beide neu). Die Optionen sind nicht gleichwertig: Option 3 ist der saubere Schnitt, Option 1 der schnellste Markttest mit Umstellungsrisiko im Dezember, Option 2 ist die schlechteste Mischung. Entscheidungs-Grundlage siehe Hand-Out in `docs/silvio-paket/sp-13-launch-timing-entscheidung.md` (Session 8).

## Schritte und Abhängigkeiten

Sieben Schritte, teilweise parallelisierbar. Reihenfolge folgt technischen und prozessualen Abhängigkeiten, nicht der Wunsch-Chronologie.

**Produktions-Zeitfenster:** Alle produzierenden Schritte (Rezeptur-Tests, Pilot-Verkauf, Regelbetrieb) laufen **vormittags zwischen ~9 und ~14 Uhr**, vor dem Service-Fenster des Restaurants (Mi + Do–So 17–22 Uhr). Das Fenster ist Produktions-Zeit-Annahme, nicht Verhandlungs-Ergebnis, und folgt der Küchen-Tagesablauf-Logik aus den Doc-05-Findings. Wer in diesem Fenster produziert — Silvios Ehefrau, eine externe Kraft, oder Silvio selbst — ist **nicht** in diesem Plan entschieden, sondern wird in [`docs/plans/20-personal-setup-retail.md`](20-personal-setup-retail.md) (Szenarien A/B/C) aufgeschlagen und von Persona 11 reviewed. Die drei Szenarien unterscheiden sich in Kosten, rechtlicher Form und Ausfall-Risiko; die Entscheidung fällt Silvio, nicht dieser Plan.

| # | Schritt | Dauer | Abhängt von | Kann parallel zu | Fail-Bedingung |
|---|---|---|---|---|---|
| 1 | Silvio-Entscheidung. MwSt-Teil dieses Schritts ist durch Steueränderungsgesetz 2025 aufgelöst (7 % auf Speisen seit 01.01.2026); Silvio-Verifikation beim Steuerberater bleibt als Routine-Check. | 1–2 Wochen | — | — | MwSt-Frage nicht mehr als Stopp-Grund; Silvio-Nein zur Gesamt-Idee bleibt Stopp |
| 2 | Vetamt-Voranfrage (informell) | 2–4 Wochen Vorlauf | 1 | 3, 5 | Vetamt verlangt Küchen-Umbau > wirtschaftliche Schwelle → Stopp oder Scope-Reduktion |
| 3 | Vakuumierer-Beschaffung (2–3 Angebote, Bestellung, Lieferung) | 2–6 Wochen | 1 | 2, 5 | Budget-Überschreitung > 3.500 € ohne Gegenwert → Re-Eval |
| 4 | Rezeptur- und Haltbarkeits-Tests (4 Gerichte, je 7-Tage-Verlauf) | 2–3 Wochen | 3 | 5 | Gericht nicht 7 Tage lagerfähig → Gericht streichen oder Haltbarkeit verkürzen |
| 5 | LMIV-konforme Etiketten inkl. echter Nährwert-Laboranalysen | 1–2 Wochen + Labor-Lauf | 4 (Rezeptur final) | — | Laborwerte außerhalb Erwartung (z.B. Salz, kcal) → Rezept-Revision |
| 6 | Pilot-Verkauf an Stammgäste, begrenztes Volumen | 2–3 Wochen | 2, 3, 4, 5 | — | Feedback vernichtend (Beutel-Schäden, Aufwärm-Enttäuschung) → Iteration statt Launch |
| 7 | Regelbetrieb | offen | 6 erfolgreich | — | — |

Schritt 2 startet **sofort nach Schritt 1**, weil er der längste kritische Pfad ist (Termin-Vorlauf Behörde). Schritt 3 läuft parallel, weil Gerätebestellung ebenfalls Lieferzeit hat. Schritt 4 beginnt erst mit Gerät vor Ort.

## Kosten einmalig (Schätzung)

| Posten | Kosten | Quelle / Status |
|---|---|---|
| Vakuumiergerät (Profi, Kammer, Gastro-Größe) | 1.500 – 3.500 € | `[TBD-Recherche]` — 2–3 konkrete Angebote fehlen |
| Rezeptur-Testchargen (Ware + Beutel) | 100 – 200 € | Annahme, Abhängig von Test-Umfang |
| Labor-Nährwertanalysen (3–4 Gerichte × 150–300 €) | 450 – 1.200 € | Marktpreis-Spanne, `[TBD-Recherche]` konkreter Labor-Anbieter |
| Kleinmaterial: Etikettendrucker, Waage, Probe-Beutelchargen | 300 – 600 € | Schätzung |
| **Summe einmalig** | **2.350 – 5.500 €** | |

Laufende Kosten (Rohware, Beutel, Etiketten) sind variabel mit dem Absatz und nicht im Launch-Kapital enthalten.

**Personalkosten-Annahme für die laufenden Kosten:** Die Personal-Basis für die Vormittags-Produktion ist **ein einfacher Koch oder eine Küchenhilfe**, nicht ein zweiter Gesellen-/Chef-Koch. Diese Annahme trägt alle Kosten-Rechnungen, die sich auf die Retail-Produktionsstunde beziehen (Doc 02 Wirtschaftlichkeitsrechnung, Doc 07 Preisgestaltung). Der Stundenlohn-Rahmen, die rechtliche Form (Minijob vs. SV-pflichtige Teilzeit) und die konkreten Szenarien (Ehefrau / externe Kraft / Silvio selbst) sind in [`docs/plans/20-personal-setup-retail.md`](20-personal-setup-retail.md) mit `[TBD-Recherche]`-Markern dokumentiert und werden von Persona 11 gefüllt. Die Annahme "einfacher Koch statt zweiter Chef" folgt den Findings 4 und 5 aus `docs/findings/session-8-persona-deep-dive-findings.md`.

Risiko-Kapital-Bewertung: Obergrenze 5.500 €. Bei Abbruch nach Schritt 6 ist der Vakuumierer auf dem Gebrauchtmarkt mit 50–70 % Restwert liquidierbar. Max. versunkener Betrag ≈ 2.500–3.000 €. Das ist ein überschaubarer Lernverlust — aber es ist **echter Verlust**, und das muss Silvio klar sein, bevor Schritt 3 ausgelöst wird.

## Offene Annahmen und Risiken

- ~~**MwSt-Satz (7 % vs. 19 %)** ist die mit Abstand größte offene Frage.~~ **Aufgelöst 2026-04-11:** Steueränderungsgesetz 2025 (Bundestag 04.12.2025, Inkrafttreten 01.01.2026) legt 7 % dauerhaft für Speisen in der Gastronomie fest, einschließlich Retail-Mitnahme. Keine rückwirkende Umstufung auf 19 % mehr möglich. Silvio-Verifikation beim Steuerberater als Routine-Check offen, kein Gate-Blocker mehr. Siehe [Nachtrag im Doc-15-Review](../reviews/15-steuer-steuerberaterin.md) und inconsistencies.md #5.
- **Vetamt-Haltung** ist unbekannt. Stuttgart ist grundsätzlich gesprächsbereit, aber die lokale Auslegung von "gewerblicher Herstellung verpackter Lebensmittel" schwankt. Vorgespräch in Schritt 2 ist nicht verhandelbar — kein Antragsstellen auf Verdacht.
- **7-Tage-Haltbarkeit ist Hypothese**, kein Fakt. Besonders Lasagne mit Béchamel ist empfindlich (Wasser-Abgabe, Textur-Verlust). Schritt 4 muss die Haltbarkeit pro Gericht **validieren**, nicht annehmen. Wenn ein Gericht nur 4 Tage trägt, wird es entweder gestrichen oder mit reduziertem MHD verkauft — nicht geschönt.
- **Küchen-Durchsatz Mo/Di**: es gibt bisher keinen validierten Zahlenwert, wie viele Beutel Silvio an einem produktiven Mo oder Di physisch schafft, ohne die normale Restaurant-Vorbereitung zu beeinträchtigen. `[TBD-Silvio]` — im Gespräch klären.
- **Bestands-Vakuumierer**: Silvio hat laut erster Info einen Henkelman im Bestand. Typ, Alter, Kammer-Größe, Beutel-Kompatibilität `[TBD-Silvio]`. Falls das Gerät ausreicht, entfällt Schritt 3 komplett.
- **Kühlraum-Kapazität**: wie viele Beutel kann der bestehende Kühlraum zusätzlich aufnehmen, ohne die normale Restaurantlogistik zu stören? `[TBD-Silvio]`.
- **Personal-Reaktion**: kein operativer Blocker, aber ein kultureller. `[TBD-Silvio]` ob es Vorbehalte im Team gibt.

## Abweichungen zum ursprünglichen Business-Case

Der Business-Case (Doc-Satz in `docs/business-case/`) hat ursprünglich einen parallelen Launch von gekühlt **und** tiefgekühlt und eine Zeitleiste von 6 Wochen bis Launch angenommen. Dieser Plan weicht bewusst ab:

- **Nur gekühlt** (D-02). Reduziert Kapitalbedarf, Behördenaufwand und Test-Komplexität.
- **Keine feste Launch-Woche.** Kritischer Pfad ist Schritt 2 (Vetamt, 2–4 Wochen Vorlauf), gefolgt von Schritt 4 (Haltbarkeits-Tests, 2–3 Wochen). Realistischer Frühest-Launch: **10–12 Wochen** nach Schritt-1-Entscheidung, unter der Annahme, dass Schritt 2 und Schritt 4 keine Nacharbeit erzwingen.
- **Pilot (Schritt 6) ist Pflicht.** Der Business-Case sah einen direkten Launch vor. Das ist unverantwortlich angesichts der 7-Tage-Haltbarkeits-Hypothese und der fehlenden realen Kunden-Feedback-Schleife.

Diese Abweichungen werden im Deep Review der 19 Docs (Stufe 3, Backlog) adressiert.

## Go / No-Go Gates

Harte Abbruch-Punkte, die vor Weiterarbeit erreicht sein müssen:

- **Gate nach Schritt 1:** ~~MwSt verbindlich geklärt.~~ **Gesetzlich erledigt durch Steueränderungsgesetz 2025 (7 % auf Speisen in der Gastronomie dauerhaft seit 01.01.2026, gilt auch für Retail-Mitnahme). Silvio-Verifikation beim Steuerberater als Routine-Check empfohlen, aber kein Stopp-Grund mehr.** Das Gate reduziert sich damit auf die Silvio-Grundsatz-Entscheidung (Ja/Nein zur Idee).
- **Gate nach Schritt 2:** Vetamt-Aussage ist "grundsätzlich machbar mit diesen Auflagen". Ist die Aussage "Küchenumbau erforderlich" oder "Zulassung als Produktionsstätte nötig", wird das Projekt gestoppt oder massiv im Scope reduziert.
- **Gate nach Schritt 4:** Mindestens zwei der vier Zielgerichte tragen verlässlich 7 Tage (sensorisch und mikrobiologisch). Sonst Scope-Schnitt auf die tragfähigen Gerichte oder Haltbarkeits-Reduktion auf z.B. 5 Tage mit angepasster Preislogik.
- **Gate nach Schritt 6:** Pilot-Feedback ist netto positiv (Wiederkauf-Signal, keine Beutelschäden in Serie, Aufwärm-Anleitung funktioniert). Sonst Iteration statt Launch.

Jedes Gate ist ein expliziter Entscheidungspunkt, kein Formal-Check.

## Phase 2 — Tiefkühl (nicht im Scope, aber verfolgen)

Tiefkühl bleibt auf der Roadmap, aber erst nach 6–12 Monaten stabilem Phase-1-Betrieb. Voraussetzungen für Phase 2: (a) positive Unit Economics in Phase 1, (b) nachgewiesene Nachfrage über das Stammgäste-Volumen hinaus, (c) Schockfroster-Invest rechtfertigbar, (d) erweiterte Vetamt-Abstimmung. Details im Business-Case, werden im Deep Review überprüft.

## Nicht in diesem Plan

- Marketing-Strategie, Preisgestaltung, Markenführung — separate Dokumente im Business-Case.
- Lieferdienst oder externe Vertriebskanäle — außerhalb Phase 1.
- Sortimentserweiterung (vegetarisch, saisonal) — frühestens nach Schritt 7 diskutierbar.
- Operative Ausführungsarbeit (Anrufe, Terminvereinbarungen) — erfolgt außerhalb des Repos durch German.
