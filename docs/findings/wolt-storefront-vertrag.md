# Findings — Wolt Storefront-Servicevertrag (Vertragskonditionen)

**Datum:** 2026-07-13
**Quelle:** Der reale, noch **unsignierte** Wolt "Storefront-Servicevertrag Deutschland" für Ristorante Goldoni (Wolt Enterprises Deutschland GmbH × Silvio Nicola Brunetti), von German bereitgestellt. Zahlen unten stammen direkt aus dem Vertragsdokument, sofern nicht als `[TBD]` / `[Founder-Angabe]` markiert.
**Status:** Analyse — speist eine **vorgeschlagene** Entscheidung D-14 (unten, Freigabe durch German) + eine Silvio-Aktion (→ Silvio-Paket SP-27). **Keine Original-Doc-Edits** in dieser Runde (Regel #6: kein v2-Rewrite ohne Findings+Plan — dies ist der Findings-Teil).

## Kurzurteil (1 Satz)

Der Vertrag beziffert die Provisionen, die Doc 09 bisher nur als „15–30 %" annahm, und öffnet damit eine echte Kanal-Entscheidung — die **Wolt Storefront** kann der Webshop aus D-12 sein (3,5 % bei Abholung statt Shopify-Eigenbau), was Marge und Setup deutlich verbessert, aber die eine load-bearing Zahl (Servicegebühr) fehlt noch und der Vertrag ist ungezeichnet.

## 1. Die wichtigste Klärung: zwei verschiedene Wolt-Produkte

Der Vertrag betrifft **nicht** das, was D-13 unter „Wolt/Uber" meint. Es sind zwei getrennte Produkte:

| # | Produkt | Was es ist | Wofür | Provision |
|---|---|---|---|---|
| 1 | **Wolt Marketplace** (= D-13 heute) | Goldoni-Listing in der Wolt-App | Neukunden-Sichtbarkeit („italienische Gerichte Stuttgart West") | ~30 % `[Founder-Angabe; Marketplace-Vertrag liegt hier nicht vor]` |
| 2 | **Wolt Storefront** (= dieser Vertrag) | White-Label-Bestellseite (`order.site/...`), in die **eigene** Website einbindbar | Eigener Kanal für bestehende Stammgäste | siehe §2 |

Silvio ist über das Restaurant-Geschäft **bereits Wolt-Marketplace-Kunde** (verkauft Pizzen zu ~30 %) und hat ein Merchant-Tablet. Der Storefront-Vertrag ist ein **paralleler Zusatzvertrag, kein Änderungsvertrag** — der Marketplace-Deal bleibt unberührt; die Storefront *addiert* einen günstigeren eigenen Kanal.

## 2. Die bestätigten Provisionssätze (Storefront)

Aus der Vertrags-Tabelle „STANDARDGEBÜHREN" (gelten automatisch **nach der Testphase**), alle Sätze **zzgl. ggf. anfallender USt.**:

| # | Erfüllungsart | Provision | Wer liefert |
|---|---|---|---|
| 1 | Wolt-Lieferung | **16 %** | Wolt-Kurier |
| 2 | Takeaway / Self-Delivery | **3,5 %** | Abholung, oder Goldoni liefert selbst |
| 3 | In-Store | **2,5 %** | vor Ort |

Einordnung für den Retail-Kanal (D-13: Abholung + Plattform-Lieferung innerhalb Stuttgarts):
- **Abholung über die Storefront = 3,5 %** — nicht 0 % (0 % gilt nur bei einem *nicht*-Wolt-Webshop), aber ohne Shopify-Miete, ohne Stripe-Gebühr, ohne Eigenbau.
- **Lieferung per Wolt-Kurier = 16 %** — statt der in Doc 09 angenommenen 15–30 %.

## 3. Was das für den Business Case ändert

1. **Doc 09 (Verkaufsstrategie), Kanal-Vergleich (Zeile ~121–126):** Die Tabelle rechnet mit „15–30 % Provision" und sagt bei Zeile 126 selbst *„exakte Provisions-Struktur … vor Listing klären"*. Das ist jetzt geklärt (für die Storefront). Die echten Sätze gehören in die Kanal-Tabelle — **im nächsten v2-Schritt** (nicht in dieser Findings-Runde).
2. **Doc 12 (D-12 Webshop):** Doc 09 (Zeile ~107) plant den Webshop als Shopify Starter (~5 €/Mo) oder WooCommerce + Stripe (1,4 % + 0,25 €). **Die Wolt Storefront könnte dieser Webshop sein** — kein Eigenbau, Wolt macht Zahlung + Kurier, Einbettung in die Goldoni-Seite per Link/Snippet. Das ist die Kern-Abwägung (→ vorgeschlagene D-14).
3. **Doc 02 (Wirtschaftlichkeit):** Der Provisions-Kostenblock aus D-13 (15–30 % auf den Lieferungs-Anteil) ist für den Storefront-Weg deutlich niedriger anzusetzen (3,5 % Abholung / 16 % Wolt-Lieferung) — **plus** die noch unbezifferte Servicegebühr. Erst nach der Servicegebühr ist die Marge belastbar.

## 4. Die Abwägung: Storefront als Webshop — dafür / dagegen

| | Wolt Storefront als Webshop (D-12) | Eigener Webshop (Shopify/WooCommerce, Status Doc 09) |
|---|---|---|
| Abholung | 3,5 % Provision | 0 % Provision, aber ~5 €/Mo + Stripe 1,4 % + 0,25 € |
| Lieferung | 16 % (Wolt-Kurier, integriert) | selbst organisieren / separater Lieferdienst |
| Setup | kein Eigenbau, „in wenigen Tagen" | Shop bauen + pflegen |
| Zahlung/Support | Wolt/WLS wickeln ab | Silvio/Stripe |
| Kundendaten | **bleiben bei Wolt** | gehören Silvio |
| Servicegebühr | **`[TBD-Silvio]` — unbeziffert im Vertrag** | entfällt |

## 5. Vertrags-Fallstricke (die für den Retail-Kanal relevanten)

Vieles im Vertrag ist Plattform-Standard und für Silvio als Bestandskunden nicht neu (WLS-Auszahlung, Chargeback-Praxis, Haftungsdeckel). Neu bzw. beachtenswert bleiben:

1. **Servicegebühr unbeziffert (§3.2).** Wird von Wolt einseitig festgelegt, kommt *zusätzlich* auf die 3,5/2,5/16 % und steht **nicht** im Dokument. Entscheidet, ob 3,5 % real 3,5 % oder eher 8–10 % all-in sind. → SP-27.
2. **Einseitige Änderungen (§3.5).** Wolt kann Gebühren mit 6 Wochen Vorlauf ändern; Weiter-Nutzung = Zustimmung. Die 3,5 % sind nicht eingefroren.
3. **Testphase kippt automatisch (§4.1 + Gebühren-Intro).** Gratis + jederzeit kündbar; danach greifen Standardgebühren automatisch. Der richtige Ort, „läuft es auf dem vorhandenen Tablet?" **kostenlos live zu prüfen** — kein zweites Gerät kaufen (§1.7 Geräte-Finanzierung ist dann irrelevant).
4. **LMIV Art. 14 gilt weiter (Doc 04).** Für die vakuumierten Retail-Produkte müssen Allergene/Zutaten/Nährwerte auch auf der Storefront-Seite vorvertraglich verfügbar sein — Silvios Pflicht (§2.4), Wolt haftet nicht für Inhalte.
5. **DSGVO: getrennt Verantwortliche (§6).** Kein Auftragsverarbeiter-Verhältnis, kein AVV; Silvio hat eigene Informationspflichten gegenüber den Storefront-Kunden. Deckt sich mit dem WhatsApp/DSGVO-Thema aus Doc 09 F-08 / SP-15.

## 6. Vorgeschlagene Entscheidung — D-14 (zur Freigabe durch German, NICHT einseitig gesetzt)

> **Vorschlag:** Die **Wolt Storefront** als Webshop-Kanal (D-12) prüfen und — vorbehaltlich der Servicegebühr — dem Shopify/WooCommerce-Eigenbau vorziehen; der Wolt-Marketplace (D-13) bleibt als separater Neukunden-Kanal bestehen.
> **Dafür:** ein 3,5-%-Abholkanal ohne Eigenbau, integrierte Zahlung + Kurier, Silvio ist schon Wolt-Kunde (kein neuer Anbieter, voraussichtlich kein neues Gerät), Testphase kostenlos.
> **Dagegen:** Kundendaten bleiben bei Wolt (kein eigener Datenschatz wie bei Shopify); Servicegebühr könnte die 3,5 % auffressen; §3.5 erlaubt spätere Erhöhungen.
> **Tie-Breaker:** nichts wegverhandeln — nur **zwei Zahlen schriftlich sehen** (Servicegebühr + Geräte-Frage, → SP-27). Danach ist es ein No-Brainer oder man weiß, warum nicht.
> **Revidierbar:** ja. **Affects (bei Freigabe):** Doc 02 v2 (Provisions-Block), Doc 09 v2 (Kanal-Tabelle + Webshop-Kapitel), D-12 (Webshop-Träger), Doc 04 (Storefront-LMIV).

## 7. Offene Silvio-Aktion

- **→ Silvio-Paket SP-27** — vor Unterschrift die Servicegebühr + die Geräte-Frage schriftlich klären. Handout: [`../silvio-paket/sp-27-wolt-storefront-vertrag.md`](../silvio-paket/sp-27-wolt-storefront-vertrag.md).

## 8. Quellen & Cross-Refs

- Wolt Storefront-Servicevertrag Deutschland (Goldoni), 19 Seiten, unsigniert — Primärquelle für alle Provisions- und Klausel-Angaben. **Nicht ins Repo committet** (enthält Steuernummer/Adresse/Telefon — Datenminimierung); liegt bei German.
- `docs/business-case/09 – Verkaufsstrategie.md` — Kanal-Vergleich, Webshop, D-12/D-13.
- `docs/findings/decisions.md` — D-12 (Vorbestellungen), D-13 (Wolt/Uber-Kanal); D-14 hier vorgeschlagen, dort noch nicht eingetragen.
- `docs/business-case/04 – LMIV-Kennzeichnung.md` — Art. 14 Fernabsatz-Pflichtinfos.
- Intake-Herkunft (org-seitig): Discovery-Briefs in `neckarshore-planning/docs/backlog/briefs/` (2026-07-12 + 2026-07-13, Engels). Die „Vault"-Benennung dort war die ursprüngliche Namensverwirrung — gemeint ist durchgängig **Wolt**.
