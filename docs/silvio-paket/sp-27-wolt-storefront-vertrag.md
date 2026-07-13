# SP-27 — Wolt Storefront: zwei Fragen vor der Unterschrift

**SP-Eintrag:** [SP-27 in `offene-fragen.md`](offene-fragen.md#block-9--plattform-verträge-wolt-storefront)
**Gespeist aus:** [findings/wolt-storefront-vertrag.md](../findings/wolt-storefront-vertrag.md)
**Stand:** 2026-07-13
**Form:** Kurz-Handout, Silvio-Voice — zwei Fragen, kein Vertrags-Deutsch.

> **Hinweis interne Ebene:** Der Vertrag ist noch **nicht unterschrieben** (leere Signatur-Felder). Das ist gut — die zwei Fragen unten sind Hebel, die *vor* der Unterschrift ziehen. Kein Grund zur Eile, aber vor dem Unterschreiben einmal nachfragen.

---

## Slide 1 — Worum es geht

Silvio, mit der **Wolt Storefront** bekommst du eine eigene Bestellseite, die wir in deine Goldoni-Website einbauen können. Deine Stammgäste bestellen dann direkt bei dir statt über die teure Wolt-App. Der Clou: bei **Abholung** zahlst du nur **3,5 %** statt der ~30 % aus der App. Holt Wolt mit dem Kurier, sind es **16 %** — immer noch die Hälfte.

Das ist ein guter Deal. Zwei Dinge sollten wir aber vor deiner Unterschrift kurz nachfragen — sonst kaufst du die Katze im Sack.

---

## Slide 2 — Die zwei Fragen an Wolt

| # | Frag Wolt | Warum es zählt |
|---|---|---|
| 1 | **„Wie hoch ist die Servicegebühr für die Storefront?"** | Die kommt *oben drauf* auf die 3,5 % und steht nirgends im Vertrag. Wenn sie klein ist, bleiben 3,5 % ein Traum-Satz. Wenn sie groß ist, sind es in Wahrheit eher 8–10 %. Diese eine Zahl entscheidet, ob sich der ganze Weg lohnt. |
| 2 | **„Läuft die Storefront auf meinem jetzigen Tablet?"** | Du hast schon ein Wolt-Gerät. Zwei Tablets ergeben keinen Sinn. Falls Wolt ein zweites will, steigen wir in der (kostenlosen) Testphase einfach wieder aus. |

---

## Slide 3 — Was danach passiert

- Kommen beide Antworten und die Servicegebühr ist okay → wir bauen die Storefront in deine Website ein (kleiner Aufwand, ein paar Tage).
- Die **Wolt-App bleibt** wie sie ist — das hier ist ein *zusätzlicher*, billigerer Weg, kein Ersatz. Du verlierst nichts.
- Deine bestehenden App-Bestellungen kannst du nicht rückwirkend billiger machen — der günstige Satz gilt nur für Gäste, die du auf deine eigene Seite lenkst (Website-Knopf, QR-Code am Tisch, Google-Profil).

---

## Für German (nicht Silvio-facing)

- Sobald Silvio die Servicegebühr + Geräte-Antwort bringt: Ergebnis in SP-27 eintragen, dann `findings/wolt-storefront-vertrag.md` §4/§6 aktualisieren und D-14 zur Entscheidung vorlegen.
- Die Website-Umsetzung (Storefront-Einbau) läuft org-seitig über Linus (`goldoni-website`) und hängt nur an der Live-`order.site`-URL — unabhängig von der Gebührenfrage.
