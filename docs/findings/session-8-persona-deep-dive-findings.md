# Session-8-Persona-Deep-Dive — Findings

**Datum:** 2026-04-11
**Quelle:** Persona-Deep-Dive zwischen German und Claude in Session 8, sechs Fragerunden über Silvio als Person, seine Familie, sein Team, seine Beziehung zu German, sein Verhältnis zur Bürokratie und die geplante Übergabe-Form der Retail-Extension-Vorarbeit.
**Zweck:** Strukturierte Einordnung der Persona-Einsichten als Findings gegen das bestehende Repo. Nicht nur Silvio-Profil, sondern konkrete **Konsequenzen** für Rollout-Plan, Artefakt-Architektur und Arbeits-Priorisierung.

## Kurzbefund

Der Deep-Dive hat sechs Findings hervorgebracht, die das bisherige Repo-Modell an wesentlichen Stellen präzisieren oder korrigieren. Drei davon betreffen den **Rollout-Plan** und die darin eingebetteten Annahmen, zwei betreffen die **Silvio-facing Artefakt-Architektur** (inklusive der schon geschriebenen Session-8-Entwürfe), eines ist eine **neue Chance-Dimension**, die bisher im Repo fehlt. Keines davon ist ein Gate-Blocker — alle sind Präzisierungen, die den Weg zur sauberen Übergabe an Silvio realistischer und tonlich passender machen.

## Findings-Tabelle

| # | Finding | Prio | Effort | Wer | Blocker? | Status | Impact |
|---|---|---|---|---|---|---|---|
| 1 | **Silvio ist am 10.4. im Chance-Modus, nicht im Sorge-Modus — Informations-Asymmetrie.** Silvio hat in dem Gespräch, das die Projekt-Genese war, **keine einzige Sorge** ausgesprochen. Die Regulatorik-Last hat German später beim Tauchgang durch die Business-Case-Docs entdeckt. Die Silvio-facing Artefakte müssen deshalb als **Unterricht-ohne-Belehrung** funktionieren: German zeigt Silvio, was er gesehen hat, ohne die Chance-Stimmung zu zerstören. Die Session-8-Entwürfe (Silvio-Paket-1-Briefing, SP-05/13/15 Hand-Outs) sind in die Falle gelaufen, die volle Sorgen-Last auf einmal zu entfalten — das ist das Gegenteil von dem, was Silvio in diesem Moment braucht. | P1 | M | Projekt-Owner (Ton-Regie) | — | Offen | Direkt wirksam auf Rework der Session-8-Artefakte und auf alle künftigen Silvio-facing Texte. |
| 2 | **Slides als Übergabeformat, nicht Dokument zum Lesen.** Germans geplanter nächster Schritt mit Silvio ist ein **persönliches Gespräch** an einem Ruhetag (Mo/Di) oder Mittwoch-Nachmittag 16–17 Uhr, mit **Slides** zum gemeinsamen Durchgehen — eventuell auf Italienisch. Kein Dokument zum allein-Lesen, keine Präsentation im fertigen Sinne. Alles, was aktuell in `docs/silvio-derivatives/` liegt, ist damit **Rohmaterial für Slides**, nicht fertiges Silvio-Artefakt. Erstellung der Slides erfolgt erst, wenn das Repo komplett durchgefräst ist, voraussichtlich über den Claude-PowerPoint-Skill. | P2 | — | — | — | Offen | Verändert den Zielpunkt aller künftigen Silvio-facing Arbeit. Formatierung, Länge und Struktur der Artefakte sind darauf zuzuschneiden. |
| 3 | **Bürokratie-Angst ist konkret, nicht abstrakt — Image-Bedrohung statt Strafe-Angst.** Silvios tiefster Schmerz bei Behörden-Kontakten ist nicht das Bußgeld, sondern die **öffentliche Bloßstellung vor Gästen** im 4,7-Sterne-Lokal (konkrete Szene: Gewerbeaufsichtsamt schickt junge Polizisten zur Service-Zeit für Jugendschutz-Aushangprüfung). Jeder Silvio-facing Text zu Behörden-Themen muss explizit die **Gegenteil-Garantie** mitführen: Vetamt-Termine sind angemeldet, terminiert, diskret, außerhalb des Service-Fensters. Ohne diese Unterton-Garantie triggert der Text die falsche Schublade. | P1 | XS | Projekt-Owner (Ton-Regie) | — | Offen | Wirkt auf alle Behörden-Kapitel: Doc 03 (Vetamt), Doc 05 (HACCP/Gesundheitsamt), Doc 14 (Krisen-Prozess), Silvio-Paket SP-01/04. |
| 4 | **Produktions-Fenster ist vormittags, nicht "nebenbei neben dem Service" — rollout-plan.md Annahme präzisieren.** Bisherige implizite Annahme im `rollout-plan.md` war, dass Silvio die Retail-Produktion in seinem bestehenden Tagesablauf unterbringt, ohne konkrete Uhrzeit. Präzisierung aus dem Deep-Dive: Retail-Produktion passt strukturell in das **Vormittags-Fenster** (zwischen ~9 und ~14 Uhr), außerhalb von Service-Vorbereitung und -Abwicklung. Das ist auch das Fenster, in dem die **Ehefrau** (nach Kinder-Schul-Bring-Zeit) oder ein **einfacher Zweit-Koch** verfügbar sein könnten. Damit wird die rollout-plan-Kostenrechnung tragfähiger, weil keine Service-Team-Überlastung angenommen werden muss. | P1 | S | CFO (rollout-plan-Überarbeitung) | — | Offen | Rollout-Plan Schritt 4 und 6 profitieren von präzisen Produktions-Slot-Annahmen. Kostenrechnung (Doc 02) muss Vormittags-Personalkosten statt Service-Team-Überlastung einplanen. |
| 5 | **Einfacher Koch statt zweiter Chefkoch — Kosten-Entlastung.** Retail-Produkte Phase 1 (Lasagne, Sugo, Ragù, Parmigiana) sind **keine Chefkoch-Gerichte**. Ein weniger qualifizierter Koch mit Vormittags-Kapazität kann sie vorbereiten. Bisherige Annahme, Retail würde Silvio selbst oder einen zweiten kreativen Chef binden, war überzogen. Koch-Kosten-Schätzung für rollout-plan.md muss entsprechend auf **Koch-Gehilfen-Niveau** (nicht Chef-Niveau) angesetzt werden, falls Ehefrau-Option nicht genutzt wird. **Personal-Entscheidung ist zu 100 % Silvios Revier**, German ist 0,0 involviert — das Repo darf die Option nur benennen, nie setzen. | P2 | S | CFO (Kostenrechnung) + Küchenchef (Validierung) | — | Offen | Entspannt die Wirtschaftlichkeits-Rechnung erheblich und macht das Projekt realistischer für die Slide-Übergabe. |
| 6 | **Fördermittel-Strang fehlt komplett im Repo.** German hat während des Tauchgangs erkannt, dass es staatliche Fördermittel (billige Kredite, Zuschüsse für Beratungskosten) für Diversifikations-Projekte wie diese Retail-Extension geben kann. Bisher ist das **im Repo nirgends adressiert** — weder als Recherche-Aufgabe, noch als Chance-Dimension in den Silvio-facing Artefakten, noch als Bestandteil der Finanzierungs-Seite in Doc 02. Das ist eine **echte Chance-Dimension**, die die bisherige Sorgen-lastige Regulatorik-Last im ersten Silvio-Gespräch ausbalancieren kann. | P2 | M | Logistiker oder neuer "Förder-Scout" + Projekt-Owner | — | Offen | Recherche ergibt konkrete Förder-Programme (Baden-Württemberg, KfW, IHK-Förderberatung, L-Bank), die als neues Doc oder Kapitel ins Repo kommen. |

## Gruppen-Logik

Analog zu den bestehenden Findings-Dateien (`03-findings.md` etc.):

- **Gruppe A — Aktionen im Silvio-Paket:** keine. Dieser Deep-Dive hat keine neuen SP-Einträge erzeugt, weil die Findings strukturell sind (Rollout, Ton, Format, Fördermittel) und nicht durch Silvio-Aktionen aufgelöst werden, sondern durch Repo-interne Arbeit.
- **Gruppe B — Eigenständige Arbeits-Blöcke im Repo:**
  1. **Rollout-Plan-Präzisierung** (Findings 4 + 5) — Produktions-Fenster vormittags, Koch-Anforderung herabsetzen, Kostenrechnung anpassen. Arbeit für CFO und Küchenchef, mit Projekt-Owner als Auftraggeber.
  2. **Fördermittel-Recherche** (Finding 6) — neues Doc oder Kapitel in Doc 02, strukturiert nach Programm, Voraussetzung, Aufwand, Zeithorizont.
  3. **Silvio-facing Ton-Rework** (Findings 1 + 3) — Rework der Session-8-Artefakte unter dem neuen Leitfaden "Chance-Modus respektieren, Kontroll-Szene respektieren, nicht alle Sorgen auf einmal". Operativ: Briefing-Notiz und drei Hand-Outs neu schreiben.
- **Gruppe C — Doc-Rewrite-Arbeit:** keine direkte Doc-Ebene betroffen; die Findings wirken auf übergreifende Struktur (Rollout-Plan, Silvio-facing Artefakte, ggf. neues Förder-Doc), nicht auf konkrete der 19 Business-Case-Docs.

## Folge-Aktionen, priorisiert

1. **[Session 9 Start]** Rollout-Plan um Vormittags-Fenster-Annahme und einfachen-Koch-Annahme präzisieren. XS-Arbeitsblock.
2. **[Session 9]** Session-8-Artefakte (Briefing-Notiz + 3 Hand-Outs) neu kalibrieren unter dem Chance-Modus-Leitfaden. M-Arbeitsblock.
3. **[Session 9 oder 10]** Fördermittel-Recherche starten und als neues Doc anlegen. M-Arbeitsblock mit WebSearch-Komponente.
4. **[Später]** Wenn Repo durchgefräst ist (Co-Reviews, v2-Rewrites), Slide-Erstellung über Claude-PowerPoint-Skill. L-Arbeitsblock, voraussichtlich mehrere Sessions.

## Was dieser Deep-Dive **nicht** geklärt hat (offene Punkte)

- **Steuerberater-Beziehung:** Wie ist Silvios bestehende Steuerberater-Beziehung (Name, Nähe, Sprache, Frequenz)? Das ist für die Ton-Kalibrierung der SP-05-Mail entscheidend, aber im Deep-Dive nicht abgedeckt. → Folge-Runde in Session 9 oder später.
- **Anwalts-/Versicherungs-Beziehungen:** Hat Silvio bestehende Kontakte? Oder wäre das alles neu? → gleiche Kategorie wie oben.
- **Silvios Digital-Grad:** Nutzt er WhatsApp, E-Mail, digitale Kasse, Buchhaltungs-Software? Das informiert die Silvio-Paket-Aktionen direkt (z. B. ob "Formular online ausfüllen" realistisch ist). → offen.
- **Silvios konkrete Investitions-Bereitschaft:** Wie geht er mit 2.500–5.500 € Invest um? Rücklagen, Kredit, Gebraucht-Markt? → offen, braucht eventuell direktes Gespräch mit Silvio.
- **Sein typischer Tagesablauf in Uhrzeiten:** Zum Dimensionieren des Vormittags-Fensters wäre ein genauerer Blick auf Silvios Tagesstruktur hilfreich. → offen.

Diese Lücken sind bewusst stehen gelassen — sie würden den Deep-Dive in Richtung "vollständiges Interview" verlängern, was nicht das Ziel war. Folge-Runden können sie adressieren, wenn es für konkrete Artefakt-Arbeit nötig wird.
