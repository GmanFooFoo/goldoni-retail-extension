# Findings — Doc 10 Operative Umsetzung

**Stand:** 2026-04-13 (Session 13, Thomas-Batch)
**Reviews eingeflossen:** Lead Thomas (Gastronom-Praktiker)
**Co-Reviews eingeflossen:** Küchenchef (Pietro), Lebensmittelrechtler (Dr. Steiger), Persona 11
**Co-Reviews ausstehend:** Logistiker

## Findings-Tabelle

| # | Finding | Prio | Quelle | Wer löst | Status |
|---|---|---|---|---|---|
| 1 | **Öffnungszeiten falsch** (18:00 statt 17:00). Produktionsfenster schrumpft um 1 Stunde. | P1 | Thomas F-01 | v2-Rewrite | Offen |
| 2 | **Nur 2 Produkte statt 5.** Mengenplanung, Zeitplan, Kapazität komplett unterdimensioniert. | P1 | Thomas F-02 | v2-Rewrite (Propagation Doc 02 v2) | Offen |
| 3 | **Personalaufwand 5–6 Std/Woche unrealistisch.** Für 5 Produkte eher 8–12 Std. "Kein Zusatzpersonal" widerspricht Doc 20 Szenarien A/B/C. | P1 | Thomas F-03 | v2-Rewrite + Cross-Ref Doc 20 | Offen |
| 4 | **Abkühlzeit 45 Min. physikalisch unmöglich.** Passiv ≤ 10 °C braucht 90–120 Min. Zeitplan muss gestreckt oder Schnellkühler eingeplant werden. | P1 | Thomas F-04 | v2-Rewrite (HACCP-Abgleich Doc 05 v2) | Offen |
| 5 | **Equipment-Preise veraltet.** Vakuumierer 1.200–1.800 → 2.500 € (Doc 12 v2). Kühlvitrine nicht optional. Gesamt-Lücke ~100 %. | P2 | Thomas F-05 | v2-Rewrite (Propagation Doc 12 v2) | Offen |
| 6 | **Dritte Rollout-Timeline (8 Wochen).** Weder 6 (Doc 13) noch 10–12 (Rollout-Plan). Cross-Ref: inconsistency #1. | P2 | Thomas F-06 | v2-Rewrite (Rollout-Plan führt) | Offen |
| 7 | **Keine Einschwing-Phase.** Von Soft-Launch direkt zu vollem Launch ohne Puffer. 4–6 Wochen Einschwingen mit Retro nötig. | P2 | Thomas F-07 | v2-Rewrite | Offen |
| 8 | **Delegierbarkeit nicht adressiert.** Keine Unterscheidung "muss Silvio" vs. "kann delegiert werden". | P2 | Thomas F-08 | v2-Rewrite | Offen |
| 9 | **Kein Plan B bei Lieferausfall.** Dienstag-Lieferung kommt nicht → Mittwoch-Produktion fällt aus → Vorbestellungen unerfüllt. | P2 | Thomas F-09 | v2-Rewrite | Offen |
| 10 | **MHD-Restbestand-Regel ist stark** — im v2 als bewusste Strategie ausbauen, nicht als Fußnote. | P3 | Thomas F-10 | v2-Rewrite (Aufwertung) | Offen |
| 11 | **CCP-Nummerierung ohne Doc-05-Abgleich.** CCPs müssen mit Doc 05 v2 konsistent sein für Vetamt-Dokumentation. | P2 | Thomas F-11 | v2-Rewrite (Cross-Ref Doc 05 v2) | Offen |
| 12 | **Wolt/Uber-Logistik fehlt komplett.** D-13 macht Plattform-Lieferung zum Phase-1-Kanal. Übergabe, Tablet, Preis-Differenzierung fehlen. | P1 | Thomas F-12 | v2-Rewrite | Offen |
| 13 | **Produktionsreihenfolge für 5 Produkte fehlt.** Welches Gericht zuerst? Sauce-Basis (Sugo) vor Aufbauten (Lasagne, Parmigiana). Ohne Sequenz Zeitplan-Chaos. | P1 | Pietro CF-01 | v2-Rewrite | Offen |
| 14 | **Mise-en-place-Kollision.** Retail-Vorbereitung überlappt mit Restaurant-Mise-en-place ab 15 Uhr. Zeitfenster-Konflikt nicht adressiert. | P1 | Pietro CF-02 | v2-Rewrite | Offen |
| 15 | **Chargen-Verkostung nicht eingeplant.** Jede Charge braucht Abnahme vor Vakuumierung. Zeitaufwand ~10 Min/Charge fehlt im Zeitplan. | P2 | Pietro CF-03 | v2-Rewrite | Offen |
| 16 | **Aufwärm-Anleitung muss getestet werden.** Zeiten und Temperaturen variieren pro Produkt. Ohne Test-Runde sind Beileger-Angaben Schätzwerte. | P2 | Pietro CF-04 | v2-Rewrite | Offen |
| 17 | **Rezeptur-Anpassung für Vakuum nicht berücksichtigt.** Sauce-Konsistenz, Fettgehalt, Würzung verändern sich durch Vakuumprozess. Anpassungs-Iterationen nötig. | P2 | Pietro CF-05 | v2-Rewrite | Offen |
| 18 | **Vor-Reinigung Produktionsbereich fehlt.** Dokumentierte Reinigung vor Retail-Produktion ist Voraussetzung für Chargen-Trennung. Kein Ablauf definiert. | P1 | Dr. Steiger CF-01 | v2-Rewrite | Offen |
| 19 | **Temperatur-Dokumentationsprozess fehlt.** Wer misst, wann, womit, wo wird's notiert? Kein digitales oder analoges System beschrieben. | P1 | Dr. Steiger CF-02 | v2-Rewrite (Cross-Ref Doc 05 v2) | Offen |
| 20 | **CCP-Alignment mit Doc 05 v2 unvollständig.** CCPs in Doc 10 stimmen nicht 1:1 mit Doc 05 v2 HACCP-Plan überein. Nummerierung und Grenzwerte abgleichen. | P1 | Dr. Steiger CF-03 | v2-Rewrite (Cross-Ref Doc 05 v2) | Offen |
| 21 | **Rückstellproben fehlen.** Lebensmittelrechtlich empfohlen, in Doc 10 nicht erwähnt. Pro Charge 1 Beutel zurückhalten bis MHD-Ablauf. | P1 | Dr. Steiger CF-04 | v2-Rewrite | Offen |
| 22 | **Szenario C impliziert, aber ohne Verweis auf Doc 20.** Text setzt zusätzliches Personal voraus, ohne Doc 20 Szenario C explizit zu referenzieren. | P2 | P11 CF-01 | v2-Rewrite (Cross-Ref Doc 20) | Offen |
| 23 | **Arbeitszeit vs. Minijob-Grenze.** 8–12 Std/Woche × 4 = 32–48 Std/Monat. Bei 538 €-Grenze max. ~44 Std/Monat @ 12,41 €/Std. Eng, muss gerechnet werden. | P2 | P11 CF-02 | v2-Rewrite (Cross-Ref Doc 20) | Offen |
| 24 | **Ehefrau-Vormittags-Verfügbarkeit als Planungsannahme.** Szenario B setzt vormittags-Verfügbarkeit voraus — nicht verifiziert, als Fakt dargestellt. | P2 | P11 CF-03 | v2-Rewrite → Silvio-Paket | Offen |

**Gesamt: 24 Findings** (11× P1, 10× P2, 3× P3)

## SPOF-Inhaber (Querschnitt-Finding)

Thomas' Red Flags betreffen einen Querschnitt, der nicht in einem einzelnen Finding aufgeht: **Silvio ist Single Point of Failure für Produktion, Qualitätskontrolle, Chargen-Abnahme und Bestellmanagement.** Das ist kein Doc-10-Problem allein — es betrifft Doc 01 (Übersicht), Doc 13 (Rollout), Doc 20 (Personal). Aber Doc 10 als "operative Umsetzung" müsste den SPOF zumindest benennen und auf Doc 20 verweisen.
