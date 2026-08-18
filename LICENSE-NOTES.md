# LICENSE-NOTES.md

**Date de lecture :** 18 août 2026 (Europe/Paris).  
**Objet :** ce qu’on peut **redistribuer** vs ce qu’on ne fait que **pointer**.  
**Ce pack** ne joint aucun ZIP, aucun XML d’exemple, aucun Schematron.

Doctrine : on ne cite que des textes **effectivement lus** ce run. On n’invente
pas un « oui on peut ».

Licence du *texte* de cette liste : **CC0 1.0** (`LICENSE`) — GO de principe
founder, consigné par l’auditeur sur ol_17569.

---

## 1. Redistribuable (sous la licence amont, avec notices)

| Source | SPDX / texte lu | Quoi | Condition |
|---|---|---|---|
| [ConnectingEurope/eInvoicing-EN16931](https://github.com/ConnectingEurope/eInvoicing-EN16931) release `validation-1.3.16` | EUPL 1.2 (`LICENSE.txt` + body de release). API `license.spdx_id` = `NOASSERTION` | ZIP CII/UBL : Schematron, XSLT, dossier `examples` | Attribution + joindre l’EUPL 1.2 + copyleft art. 5. Copies non modifiées. **Non joint ici.** |
| [itplr-kosit/xrechnung-testsuite](https://github.com/itplr-kosit/xrechnung-testsuite) tag `v2026-01-31` | Apache-2.0 (API + fichier `LICENSE`) | ZIP `xrechnung-3.0.2-testsuite-2026-01-31.zip` + instances | Apache-2.0 § 4. **Non joint ici.** |
| [fnfempe/France_RFE](https://github.com/fnfempe/France_RFE) | Apache-2.0 | Artefacts de **validation** (XSD / Schematron) du dépôt | Apache-2.0. **Ne couvre pas** les annexes d’exemples AFNOR. Assets de release vides ce run (`assets: []`). |
| [horstoeko/zugferd](https://github.com/horstoeko/zugferd) | MIT | Code de la bibliothèque | MIT. |
| [ZUGFeRD/mustangproject](https://github.com/ZUGFeRD/mustangproject) | Apache-2.0 | Code / CLI | Apache-2.0. |
| [pretix/python-drafthorse](https://github.com/pretix/python-drafthorse) | Apache-2.0 | Code Python | Apache-2.0. |
| [stephanstapel/ZUGFeRD-csharp](https://github.com/stephanstapel/ZUGFeRD-csharp) | Apache-2.0 (`LICENSE.txt`) | Code C# | Apache-2.0. |
| [akretion/factur-x](https://github.com/akretion/factur-x) | API `NOASSERTION` ; `LICENSE.txt` = BSD 3-clause | Code Python | Pointer le dépôt. SPDX GitHub non classé → **À-TRANCHER** si on vendore. |
| [hernaninverso/validate-einvoice-action](https://github.com/hernaninverso/validate-einvoice-action) | Apache-2.0 | Code de l’Action | Apache-2.0. |
| [invoicenavigator/validate-invoice](https://github.com/invoicenavigator/validate-invoice) | MIT | Code de l’Action | MIT. |
| [attestwire/validate-einvoice-action](https://github.com/attestwire/validate-einvoice-action) | MIT | Code de l’Action | MIT. Claims runtime non vérifiés. |
| [facturxapi/validate-einvoice](https://github.com/facturxapi/validate-einvoice) | API `NOASSERTION` ; README / `LICENSE-EUPL-1.2.txt` = EUPL 1.2 | Code Action / CLI | Pointer. SPDX API non classé. |
| [facturxapi/en16931-oracles](https://github.com/facturxapi/en16931-oracles) | API `NOASSERTION` ; NOTICE du dépôt : EUPL 1.2 sur fixtures/XSLT ConnectingEurope | Receipts / mutants | Pointer. Pas de republication des ZIP CEN depuis ce pack. |
| [sdras/awesome-actions](https://github.com/sdras/awesome-actions) | CC0-1.0 | Texte de la liste | CC0. Dernier push 2024-09-01 (> 18 mois). |
| [morganrcu/awesome-europe](https://github.com/morganrcu/awesome-europe) | CC0-1.0 | Texte de la liste | CC0. |
| [causa-prima-ai/awesome-invoicing](https://github.com/causa-prima-ai/awesome-invoicing) | API `NOASSERTION` ; fichier `LICENSE` = CC0 1.0 (lu 16/08) | Texte de la liste | Pointer. SPDX API non classé. |

---

## 2. Pointer seulement — ne pas redistribuer depuis ce pack

| Source | Pourquoi |
|---|---|
| Pack FNFE Factur-X 1.09.2 (page [fnfe-mpe.org/factur-x](https://fnfe-mpe.org/factur-x/)) | Gate e-mail. ZIP **non ouvert**. |
| Infopaket FeRD ZUGFeRD 2.5.2 (page [download-zugferd](https://www.ferd-net.de/download-zugferd)) | ZIP **non téléchargé** (~28 Mo). |
| Texte AFNOR XP Z12-012 (boutique) | Corps **non relu**. Copyright AFNOR. |
| Annexes d’exemples XP Z12-012 / 014 | Copyright AFNOR ; **pas** couvertes par Apache-2.0 de France_RFE. |
| Sites validateurs + ITB Commission | On pointe. On ne copie pas leur UI ni leurs règles. |
| Pages DGFiP / impots.gouv.fr | On pointe, on ne republie pas les XLSX/PDF. |
| `e-invoice-be/awesome-peppol` | `license`: **null**. README d’une ligne. |

---

## 3. Exclus (lint générique)

Pas des fiches e-invoicing — **absents du README** :

`reviewdog/action-eslint` (MIT) · `aquasecurity/trivy-action` (Apache-2.0) · `golangci/golangci-lint-action` (MIT) · `oxsecurity/megalinter` (AGPL-3.0).

Vérifiés HTTP 200 / API ce run ; last push 2026.

---

## 4. Ce que cette note ne décide pas

- Republication des exemples FNFE / FeRD Infopaket : **À-TRANCHER** (gate ou disclaimer).
- SPDX d’akretion/factur-x, causa-prima-ai/awesome-invoicing, facturxapi/* : fichiers ou NOTICE lus, API `NOASSERTION`.
- Publication GitHub du *dépôt* : `facturxapi/awesome-einvoicing` (CC0), après GO conditionnel auditeur 18/08.
