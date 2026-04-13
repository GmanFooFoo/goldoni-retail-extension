# Co-Review: Doc 13 — 6-Wochen-Rollout-Plan

**Reviewer:** Thomas (Gastronom-Praktiker, Persona 06) — Co-Review zu Marcus/CFO (Lead, Stopp-Urteil)
**Datum:** 2026-04-13
**Doc-Version:** v1

## Perspektive

Der CFO hat ein Stopp-Urteil gegeben (9 Findings, 6-Wochen-Timeline physisch unmöglich). Thomas prüft die Alternative — den Gate-basierten 10–12-Wochen-Plan in `docs/plans/rollout-plan.md` — auf Praxis-Tauglichkeit.

## Ergänzende Findings

### CF-01 — 10–12 Wochen sind realistisch, aber nur mit parallelen Streams

Der Rollout-Plan zeigt 7 Schritte, teilweise parallelisierbar. Aus Praxis-Sicht: die **kritischste Parallelisierung** ist Schritt 2 (Vetamt, 2–4 Wochen) + Schritt 3 (Vakuumierer, 2–6 Wochen). Wenn beides seriell läuft → 16 Wochen. Wenn parallel → 10 Wochen. Die Parallelisierung setzt voraus, dass Silvio den Vakuumierer bestellt, **bevor** das Vetamt grünes Licht gibt. Das ist ein kalkuliertes Risiko: wenn das Vetamt "Nein" sagt, sitzt Silvio auf einem Vakuumierer ohne Verwendung. Bei einem Restwert von 50–70 % (Doc 12 v2) ist das Risiko überschaubar — aber Silvio muss es bewusst eingehen.

### CF-02 — Schritt 4 (Rezeptur-/Haltbarkeitstests) ist der unterschätzte Engpass

"2–3 Wochen" für Haltbarkeitstests klingt kurz. In der Praxis: **eine Testrunde = 7 Tage warten** (bis MHD-Ende), dann verkosten. Wenn das Ergebnis nicht passt (Textur, Geschmack, Wasserabscheidung) → Rezeptur anpassen → nochmal 7 Tage warten. Zwei Iterationen = 3 Wochen. Drei Iterationen (nicht unüblich bei 5 Produkten) = 4–5 Wochen. Der Rollout-Plan unterschätzt die Iteration-Loops.

### CF-03 — Pilot-Phase braucht ein klares Abbruch-Kriterium

"Feedback vernichtend → Iteration statt Launch" steht im Rollout-Plan. Aber: **was ist "vernichtend"?** 1 Beschwerde von 20 Kunden? 5 von 20? Beutel-Schäden bei 10 % der Produkte? Silvio braucht ein konkretes Gate-Kriterium, z.B.: "Weniger als 3 von 10 Kunden würden nachkaufen → Iteration. Mehr als 2 Beutel-Schäden pro Charge → Beutel-Wechsel vor Launch."

### CF-04 — Personal-Meilenstein fehlt im Rollout

Wenn Silvio mit Szenario C (selbst produzieren) als Pilot startet und nach 4–6 Wochen auf A oder B wechseln will (Doc 20), muss die Personalsuche **in Woche 1–2 starten**, nicht nach dem Pilot. Suchdauer Stuttgart: 4–8 Wochen (Persona 11). Das heißt: Personalsuche läuft parallel zum Vetamt und zur Geräte-Beschaffung. Der Rollout-Plan hat keinen Personal-Schritt.

## Bestätigung CFO-Findings

- **Stopp-Urteil "6 Wochen unrealistisch":** Vollständig bestätigt. Auch 8 Wochen (Doc 10) sind zu knapp. 10–12 Wochen sind die Untergrenze, 14–16 Wochen realistischer bei Iterationsschleifen.
- **fddb.info statt Labor:** Aus Praxis-Sicht bestätigt. Kein Vetamt akzeptiert fddb.info als Nährwert-Quelle.

## Empfehlung

Doc 13 v2 muss den Gate-basierten Rollout-Plan aus `docs/plans/rollout-plan.md` als Basis nehmen, nicht die 6-Wochen-Timeline. Ergänzungen: Personal-Meilenstein parallel, Haltbarkeitstest-Iterationen realistisch einplanen (3–5 Wochen statt 2–3), Pilot-Abbruch-Kriterien quantifizieren.
