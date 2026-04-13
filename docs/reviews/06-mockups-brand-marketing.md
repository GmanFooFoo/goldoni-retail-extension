# Review: Doc 06 — Mockups

**Reviewer:** Jana (Brand & Marketing, Persona 08)
**Datum:** 2026-04-13
**Doc-Version:** v1

## Kurzurteil (1 Satz)

Kein Mockup-Dokument, sondern eine technische Inhaltsangabe einer HTML-Datei — ohne visuellen Entwurf, ohne Markenführung, ohne Design-System, und mit einem fiktiven Namen, der nie auf ein echtes Etikett gehört.

## Scoring (1–5)

- Fachliche Korrektheit: 2 — Was beschrieben wird (LMIV-Pflichtfelder, Chargenprotokoll), ist fachlich nicht falsch, aber für nur 1 Produkt und mit falschen Musterdaten
- Vollständigkeit: 1 — Kein visuelles Mockup im Repo, keine Design-Richtlinien, keine Markentransfer-Logik, nur 1 von 5 Produkten
- Umsetzbarkeit: 2 — Eine HTML-Datei, die "als separater Download bereitgestellt" wurde, aber im Repo nicht vorhanden ist, hilft niemandem
- Risiko-Abdeckung: 1 — "Marco Antonelli" auf dem Etikett ist ein Platzhalter-Risiko. fddb.info statt Labor ist ein Ablehnungsgrund beim Vetamt

## Red Flags

- **"Marco Antonelli"** statt Silvios echtem Namen. Inconsistency #4 seit Session 1. Das ist nicht nur ein Platzhalter-Problem — wenn jemand dieses Mockup als Vorlage nimmt, steht ein falscher Name auf dem Etikett.
- **fddb.info für Nährwerte** (Zeile 22): Der Behördenkontrolleur hat das in Doc 03 und Doc 05 als **sofortigen Ablehnungsgrund** bewertet. Nährwerte müssen aus einer Laboranalyse kommen (SP-11), nicht aus einer Consumer-App.
- **HTML-Datei nicht im Repo.** Das Dokument beschreibt etwas, das man nicht sehen kann. Ein Mockup-Dokument, das kein Mockup enthält, ist ein Inhaltsverzeichnis.

## Fundierte Kritikpunkte

### F-01 — Kein visuelles Etikett-Mockup im Repo

Doc 06 beschreibt eine HTML-Datei, die "als separater Download bereitgestellt" wurde. Im Repo ist sie nicht vorhanden. Für einen Brand-Review brauche ich etwas, das ich **sehen** kann: Typografie, Farbschema, Logo-Platzierung, Schriftgrößen, Lesbarkeit auf dem Beutel. Ohne visuelles Mockup kann ich die Markenkonsistenz nicht beurteilen. Mindestens eine Skizze (ASCII, SVG, oder Bild) muss im Repo sein.

### F-02 — Nur 1 Produkt (Lasagne al Forno) statt 5

Das Mockup existiert nur für Lasagne. Die 5 Phase-1-Produkte haben unterschiedliche Anforderungen: Sugo braucht ein anderes Format (350g Glas oder Beutel?), Parmigiana hat andere Allergene, Ragù ein anderes Gramm-Format. Ein Etikett-System muss alle 5 abdecken — mit konsistentem Design, aber produktspezifischen Varianten.

### F-03 — Keine Design-Richtlinien / Brand Guidelines

Kein Wort zu: Farbpalette, Typografie, Logo-Verwendung, Bildsprache. Doc 08 (Verpackungsstrategie) erwähnt "Dunkel/Creme-Farbschema" und "kein Hochglanz" — aber das gehört hierher, ins Mockup-Dokument, als verbindliche Design-Grundlage. Ohne Guidelines produziert jeder Etikett-Entwurf ein anderes Goldoni.

### F-04 — LMIV-Pflichtfelder nicht gegen Doc 04 v2 validiert

Doc 04 v2 hat eine erweiterte Pflichtangaben-Checkliste: QUID, Primärzutat-Herkunft (DVO 2018/775), Los-Kennzeichnung (LKV), vollständige Anschrift, Pflichtsprache Deutsch. Das Mockup listet "Allergene fett + unterstrichen" und "MHD pro Charge" — aber die erweiterten Pflichtfelder aus dem Lead-Review fehlen. Cross-Ref: inconsistency #10.

### F-05 — HACCP-Dokument-Mockup: Aufbewahrungsfrist falsch

"Alle Protokolle 3 Jahre aufbewahren" — Doc 14 v2 differenziert: HACCP 3 Jahre, aber Chargen-Doku bis 25 Jahre ab ProdHaftG-Novelle (9.12.2026), Steuer 10 Jahre. "3 Jahre für alles" ist zu kurz für die Hälfte der Dokumente.

### F-06 — Registrierungs-Nummer als Platzhalter ohne Erklärung

"DE-BW-08111-001-XXXXX" steht im Mockup. Wo kommt die echte Nummer her? Wann? (Antwort: vom Vetamt nach der Registrierung, Schritt 2 im Rollout-Plan.) Das muss als Abhängigkeit markiert sein — das Etikett ist erst druckfertig, wenn die Reg.-Nr. da ist.

### F-07 — Kein Aufwärm-Hinweis auf dem Etikett

Die Aufwärm-Anleitung ist das wichtigste Stück Kundenkommunikation auf dem ganzen Beutel. "Ofen 180 °C, 20 Min." oder "Pfanne bei mittlerer Hitze, 8 Min." — je nach Produkt verschieden. Doc 04 v2 (LMIV) fordert eine Zubereitungsempfehlung, wenn das Produkt ohne sie nicht bestimmungsgemäß verwendet werden kann. Auf dem Mockup: kein Wort davon.

## Was fehlt

1. **Visuelles Etikett-Mockup** (im Repo, nicht als externer Download)
2. **Design-Richtlinien** (Farbe, Typo, Logo, Bildsprache)
3. **Mockups für alle 5 Phase-1-Produkte**
4. **Aufwärm-Anleitung** pro Produkt auf dem Etikett
5. **LMIV-Pflichtfeld-Validierung** gegen Doc 04 v2
6. **Korrekte Aufbewahrungs-Fristen** im HACCP-Mockup

## Empfehlung

- [ ] Freigabe
- [ ] Freigabe mit Auflagen
- [x] Rework erforderlich
- [ ] Stopp — geht so nicht live

**Begründung:** Doc 06 ist ein Platzhalter, kein Mockup-Dokument. Es beschreibt eine nicht vorhandene Datei, enthält falsche Musterdaten und keine Markenführung. Der v2 muss echte visuelle Entwürfe enthalten (mindestens Etikett-Skizzen), gegen Doc 04 v2 validiert sein und alle 5 Produkte abdecken.
