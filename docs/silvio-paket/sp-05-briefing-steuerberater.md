# SP-05 — Briefing Steuerberater

**SP-Eintrag:** [SP-05 in `offene-fragen.md`](offene-fragen.md#block-2--steuerberater--kasse)
**Gespeist aus:** [Doc-15-Findings](../findings/15-findings.md) F1, F5, F8, F10, F11
**Zweck:** Silvio schickt diese E-Mail an seinen Steuerberater. Vier Antworten reichen aus, damit der Steuer- und Buchführungs-Teil des Projekts für Phase 1 durchgeplant ist.

---

## Silvio, so geht das

1. Kopier den Text unten in eine neue E-Mail an deinen Steuerberater.
2. Füll die drei Klammern aus (Gerätepreis, Team-Größe, Startmonat). Wenn du einen Wert noch nicht hast, schreib einfach "folgt".
3. Schick sie ab. Fertig.
4. Die Antwort leitest du mir weiter (oder liest sie mir vor) — ich baue sie dann in den Plan ein.

Was er dir in der Antwort voraussichtlich sagt: dass die 7 % in Ordnung sind, welchen Zeitraum er für die Abschreibung nimmt (wahrscheinlich 7 Jahre), wo er den neuen Umsatz in deiner Buchhaltung ablegen möchte, und wie er den Verderb verbucht. Wenn er eine **verbindliche Auskunft** vom Finanzamt empfiehlt (Frage 5), sag mir Bescheid — ich erkläre dir dann, was das kostet und ob es sich lohnt.

---

## E-Mail-Text zum Kopieren

> **Betreff:** Retail-Erweiterung Goldoni — vier Fragen zur steuerlichen Einordnung
>
> Lieber Herr / Liebe Frau [Name],
>
> ich plane, im Ristorante Goldoni zusätzlich zum Restaurant-Betrieb vakuumierte Gerichte (Lasagne, Sugo, Ragù, Parmigiana) in kleiner Menge für den Verkauf über die Theke herzustellen. Das Restaurant bleibt wie gehabt, der Retail-Verkauf wird eine zusätzliche Umsatz-Quelle. Bevor ich loslege, möchte ich vier Punkte mit dir klären, damit ich die Buchhaltung und die Kasse von Anfang an sauber aufsetze.
>
> **Frage 1 — Umsatzsteuersatz.** Nach dem Steueränderungsgesetz 2025 gilt ab 01.01.2026 der ermäßigte Steuersatz von 7 % dauerhaft auf Speisen in der Gastronomie, einschließlich Außer-Haus-Verkauf. Trifft das auch für mein Vorhaben (verpackte Vakuum-Ware zur Mitnahme) zu, oder siehst du eine Einordnung, die eher Einzelhandel und damit 19 % wäre? Ich gehe nach dem Gesetzestext von 7 % aus, möchte aber deine Bestätigung, bevor ich die Preise kalkuliere.
>
> **Frage 2 — Abschreibung Vakuumiergerät.** Ich beschaffe einen Profi-Vakuumierer, voraussichtlicher Anschaffungswert [Gerätepreis einsetzen, z. B. 2.500 € netto]. Welche Nutzungsdauer und welche jährliche Abschreibung setzt du dafür an? Kann ich die Vorsteuer aus der Rechnung direkt ziehen?
>
> **Frage 3 — Trennung der Erlöskonten.** Ich möchte den Restaurant-Umsatz (Tisch-Verkauf) und den Retail-Umsatz (Vakuum-Ware über die Theke) in der Buchhaltung sauber trennen, auch wenn beide mit 7 % laufen. Welche Konten im SKR 03 oder SKR 04 schlägst du dafür vor? Reicht die Trennung innerhalb der Erlöskonten, oder empfiehlst du eine separate Kostenstelle?
>
> **Frage 4 — Buchung von Verderb und Entsorgung.** Bei Haltbarkeits-Tests und im späteren Betrieb wird es Chargen geben, die nicht verkauft werden und entsorgt werden müssen. Wie buche ich diesen Verderb korrekt — als Wareneinsatz mit Entsorgungs-Nachweis, als außerplanmäßige Abschreibung oder anders? Muss ich dafür eine eigene Dokumentation führen?
>
> **Frage 5 — Verbindliche Auskunft nach § 89 Abs. 2 AO.** Hältst du für einen der vier Punkte — besonders für Frage 1 — eine verbindliche Auskunft beim Finanzamt für sinnvoll, oder reichen deine Einschätzung und die Gesetzeslage aus?
>
> **Zum Hintergrund:** Das Projekt ist Phase 1, nur gekühlt, 7 Tage Haltbarkeit, Verkauf ausschließlich im Restaurant. Team ist mein bestehendes [Team-Größe einsetzen, z. B. Küchen-Team plus ich selbst]. Start voraussichtlich [Startmonat einsetzen, z. B. Herbst 2026]. Ich kalkuliere mit 20–30 Stück pro Woche im Pilot, also kein Massen-Geschäft.
>
> Über eine kurze schriftliche Rückmeldung zu den vier Fragen würde ich mich freuen — damit ich deine Antworten als Grundlage für die Planung verwenden kann. Ein Termin in den nächsten Wochen wäre zusätzlich hilfreich, wenn du Kapazität hast.
>
> Vielen Dank und beste Grüße,
> Silvio [Nachname]
> Ristorante Goldoni

---

## Was danach passiert

Sobald die Antwort da ist, zieht die nächste Session die Ergebnisse in folgende Stellen:

- Doc 15 v2 (Steuer-Doc) — 7 %-Bestätigung, AfA-Rechnung, Kontenrahmen-Anker, Verderb-Buchung
- Rollout-Plan Schritt 1 — MwSt-Verifikation als erledigt markieren
- SP-05 Status auf `Erledigt` mit Commit-Ref
- Bei Bedarf neue Findings oder Decisions, falls der Steuerberater einen Punkt anders bewertet

Falls der Steuerberater eine verbindliche Auskunft empfiehlt, wird das als separater Arbeits-Block mit Kosten-Nutzen-Abwägung aufgesetzt (Gebühr ~300–500 €, Dauer 3–6 Monate).
