# Awesome e-Invoicing [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Sourced map / curated list of **e-invoicing** specs, docs, validators, libraries and corpora — not a ranking (EN 16931, Factur-X, ZUGFeRD, XRechnung, BR-FR).

> **Inclusion ≠ endorsement.** A line here does not mean a tool is compliant, official, better, or recommended.
>
> Each line is **factual** (what the page or GitHub API said this run). Prices only if they appear in the HTML ; otherwise `[non-mesure]`. Words like “valide / conforme / répare” are the site’s, not ours.

Maintained by the team behind FacturX API (a commercial product, not listed here). Its open-source projects follow the same rules as every other entry and are marked *(list maintainer's project)*.

HTTP / licenses / liveness: [`CHECKS.md`](CHECKS.md). Redistribute vs pointer: [`LICENSE-NOTES.md`](LICENSE-NOTES.md). Frame: [`NOTICE.md`](NOTICE.md). How to add a line: [`CONTRIBUTING.md`](CONTRIBUTING.md). List text: [CC0 1.0](LICENSE).

## Contents

- [Specs](#specs)
- [Official docs](#official-docs)
- [Validators](#validators)
- [GitHub Actions](#github-actions)
- [Libraries](#libraries)
- [Corpora](#corpora)
- [Related lists](#related-lists)

---

## Specs

- [ConnectingEurope/eInvoicing-EN16931](https://github.com/ConnectingEurope/eInvoicing-EN16931) — official EN 16931 Schematron artefacts (UBL + CII) ; latest UBL & CII **v1.3.17** (2026-10-12) ; README: « This repository does not contain eInvoicing-EN16931 rules for any CIUS. » File `LICENSE.txt` EUPL 1.2 (API `license.spdx_id` = `NOASSERTION`).

- [FeRD — ZUGFeRD / Factur-X](https://www.ferd-net.de/) — Forum elektronische Rechnung Deutschland ; home: « ZUGFeRD 2.5.2 veröffentlicht » ; « Eschborn | Paris, 04.08.2026 ».

- [FNFE-MPE — Factur-X](https://fnfe-mpe.org/factur-x/) — « Le 4 août 2026, le FNFE-MPE et le FERD publient la dernière release, à savoir: Factur-X 1.09.2 et ZUGFeRD 2.5.2 » ; « Techniquement, Factur-X et ZUGFeRD sont identiques. » ZIP behind an email field.

- [fnfempe/France_RFE](https://github.com/fnfempe/France_RFE) — France CTC / BR-FR validation artefacts (XP Z12-012 / 014) ; release `v1.4.0.04` « FNFE_RFE_INVOICE_1.4.0.04 » (`published_at` 2026-09-04T22:42:01Z) ; API license Apache-2.0 ; no uploaded release assets (source archives only).

## Official docs

- [AFNOR XP Z12-012 (shop)](https://www.boutique.afnor.org/fr-fr/norme/xp-z12012/formats-et-profils-des-messages-factures-et-statuts-de-cycle-de-vie-constit/fa301169/601641) — « XP Z12-012 juin 2026 » « En vigueur » « Consultation gratuite ». Body of the standard **not read** (`[non-mesure]`).

- [DGFiP — accredited platforms](https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees) — « Je consulte la liste des plateformes agréées » ; « Publié le 30/07/2024, modifié le 22/09/2026 ».

- [DGFiP — reform FAQ](https://www.impots.gouv.fr/professionnel/questions/dans-le-cadre-de-la-reforme-de-la-facturation-electronique-comment-devrais) — « À compter du 1er septembre 2026 , toutes les entreprises assujetties à la TVA […] devront être en capacité de recevoir des factures électroniques ». « septembre 2027 » **absent** from the HTML this run.

- [European Commission — Registry of supporting artefacts to implement EN16931](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108974/Registry+of+supporting+artefacts+to+implement+EN16931) — official DIGITAL registry: EN 16931 validation artefacts (UBL 2.1 + CII 16b, latest **1.3.17**, published 12/10/26, effective 15/11/26), EAS and VATEX code lists, CIUS/Extensions registry, and the bi-annual release schedule.

- [FeRD — Download ZUGFeRD](https://www.ferd-net.de/download-zugferd) — « Infopaket für das E-Rechnungsformat ZUGFeRD 2.5.2 vom 04.08.2026 » ; Direktdownload 27.94 MB (DE) / 28.98 MB (EN). **ZIP not downloaded**.

- [FeRD — Was ist ZUGFeRD?](https://www.ferd-net.de/standards/zugferd) — « ZUGFeRD ist ein kostenfrei verfügbares, branchenübergreifendes Datenformat […] » ; cited base: Norm EN16931.

- [FNFE-MPE — Ressources](https://fnfe-mpe.org/ressources/) — « 30 juin 2026 : Publication des nouvelles versions des normes XP Z12 -012, 013, 014 » ; « XP Z12-012 (30/06/2026) 1.4.0 » ; « Version 1.4.0 des schematrons » (fix04 du 4 septembre), file `2026_09_04_FNFE_SCHEMATRONS_FR_CTC_V1.4.0.04.zip`.

## Validators

Tools that present themselves as a validator, converter or API. **Not a ranking.**

- [Annehmbar](https://annehmbar.com/) — H1 « XRechnung und ZUGFeRD prüfen: Wird Ihre Rechnung angenommen? » ; « KoSIT-Konfiguration v2026-08-31 und ZUGFeRD 2.5.2 » ; REST `POST /api/validate` (CII/UBL XML, `X-Api-Key`) ; public update log [`/log`](https://annehmbar.com/log) + Atom feed. Page: « Regeländerungs-Alarm 0 € bis 31.12.2026, danach 19 € / Monat ». Submitted by the operator.

- [B2Brouter — Factur-X validator](https://www.b2brouter.net/fr/factur-x-validator/) — title « Factur-X validator : en ligne, conforme et gratuit » (their title) ; platform [pricing](https://www.b2brouter.net/fr/tarifs/) HTML: Basic `0 eur / à vie` ; Professional `110 eur / an + TVA` ; Business `300 eur / an + TVA`.

- [CheckXRechnung](https://checkxrechnung.com/) — H1 « XRechnung & ZUGFeRD prüfen – kostenlos » ; page lists XRechnung XML (UBL/CII), ZUGFeRD PDF with embedded XML, and « KoSIT Validator + offizielle XRechnung-Konfiguration » ; REST `POST /v1/validate`. Price: « kostenlos (50 pro IP und UTC-Tag) » ; « API / Batch ab €79/Monat » is a waitlist, not a live plan (« Batch und höheres Volumen bleiben eine Warteliste ab €79/Monat. »). Submitted by the operator.

- [Coretool — E-Rechnung prüfen](https://coretool.de/e-rechnung-pruefen) — title « E-Rechnung prüfen & ansehen – kostenloser XRechnung & ZUGFeRD Validator und Viewer » ; page states « Kostenlos · ohne Anmeldung · Datei wird nicht gespeichert ». API page [`/e-rechnung-api`](https://coretool.de/e-rechnung-api): title « E-Rechnungs-API für Entwickler – XRechnung & ZUGFeRD per API prüfen » ; « 3 Prüfungen kostenlos je Konto ». Pricing on the validator page: « 3 Rechnungen pro Monat gratis » ; « Solo-Tarif 9 €/Monat inkl. MwSt. ». Submitted by the operator.

- [E-Invoice Check](https://einvoicecheck.com/en/validator) — H1 « Validate an XRechnung against an identified ruleset » ; title « XRechnung Validator for reproducible technical checks ». Home [FAQ](https://einvoicecheck.com/en): « Only the XRechnung XML configurations explicitly listed in the interface for UBL 2.1 or CII D16B. This page does not promise ZUGFeRD PDF or end-to-end Peppol validation. » [Terms](https://einvoicecheck.com/en/terms): « The service is free technical validation » ; « free validation phase with no account, no checkout, no payment and no subscription ». Price [non-mesure].

- [E-Invoice Conformance Lab — self-check](https://kobima6813.github.io/einvoice-conformance-matrix/check.html) — H1 « Check one e-invoice » ; title « Free e-invoice self-check — E-Invoice Conformance Lab » ; page states « It is checked locally in your browser and is never uploaded » ; scope: « A subset of EN 16931 business rules » ; « A clean result here does not mean the invoice passes KoSIT, CEN or Peppol validation ». Paid audits ([pricing](https://kobima6813.github.io/einvoice-conformance-matrix/pricing.html)): One-time check `290 €` ; Vendor audit `790 €`. Same author as the `einvoice-conformance-matrix` entry under Corpora.

- [e-invoice-be/peppol-cli](https://github.com/e-invoice-be/peppol-cli) — Go CLI (binary `peppol`) ; API description « CLI for the e-invoice.be Peppol API ». MIT. **`stargazers_count` = 3**. Release `v0.0.7` (2026-10-14). `internal/cli/validate.go`: `validate ubl` and `validate json` « against Peppol BIS Billing 3.0 », sent to `https://api.e-invoice.be` with an API key (not run locally). [Landing page](https://e-invoice.be/peppol-cli): « Requires an e-invoice.be account. » ; « You only pay for the invoices you send or receive, from €0.18. »

- [E-Rechnung API](https://e-rechnung-api.fly.dev/) — H1 « ZUGFeRD & Factur-X API » ; title « ZUGFeRD & Factur-X API | E-Rechnungen leicht gemacht ». Validator [`/validator`](https://e-rechnung-api.fly.dev/validator): title « Kostenloser ZUGFeRD & XRechnung Validator (EN 16931) » ; drag-and-drop validation for PDF/A-3 and XML without registration. Pricing: Test `0€`, Prepaid `10€ / 100 Dok.`, Starter `29€ / Monat`.

- [einvoicevalidator.eu](https://einvoicevalidator.eu/en) — H1 « E-invoice validator. Free, no sign-up. » ; title « E-Invoice Validator: check XRechnung & ZUGFeRD free » ; page states « Check XRechnung, ZUGFeRD/Factur-X, Peppol BIS 3.0 and UBL 2.1 against EN 16931 ». UI in 8 languages. Price [non-mesure].

- [Factur-X Validator & Generator (Apify Actor `rigel/facturx-toolkit`)](https://apify.com/rigel/facturx-toolkit) — H1 « Factur-X Validator & Generator: ZUGFeRD, EN 16931, FR 2026 » ; description « Validate Factur-X/ZUGFeRD invoices (XSD, official schematrons, French 2026 BR-FR rules, PDF/A-3), extract them to JSON, generate PDF/A-3 Factur-X with totals and French legal notes, or convert a plain PDF invoice (OCR included). » ; page states « Not an approved platform (PA) ». Pricing: « Pay per event, in USD. » ; `document-validated` « $0.015 ». *(submitted by the Actor's author)*

- [FactureValide](https://facturevalide.fr/) — H1 « Votre facture valide en 2 minutes. Point. » ; « Gratuit pendant le lancement » ; « Sans limite · Sans carte bancaire ». Validator [`/valider-facture-electronique.html`](https://facturevalide.fr/valider-facture-electronique.html): « 10 vérifications/jour » ; « 31 points de contrôle ». `/tarifs` and `/tarifs.html` = **404**.

- [facturx-validator.fr](https://facturx-validator.fr/) — H1 « Vérifiez vos factures Factur-X gratuitement » ; footer « Outil gratuit et open source. » [`/verifier`](https://facturx-validator.fr/verifier): « Fichier PDF uniquement (max. 10 Mo) » ; profiles Minimum, Basic, EN16931, Extended. Euro price `[non-mesure]`. No repo link on the pages opened (`[non-mesure]` repo).

- [Factusur](https://factusur.com/) — H1 « Transformez votre facture PDF en Factur-X, en 2 minutes » ; page states « téléchargez un PDF Factur-X (profil EN 16931) avec son XML embarqué » and « Factusur n'est pas une plateforme agréée (PA) et ne transmet pas vos factures ». Validator [`/verifier-factur-x`](https://factusur.com/verifier-factur-x): « Gratuit, sans inscription » ; « PDF uniquement · 10 Mo max. ». [Pricing](https://factusur.com/tarifs), 5 tiers: Gratuit `0 €` (« 3 conversions / mois ») ; Starter `3,90 € /mois` (« 10 conversions / mois ») ; Essentiel `6,90 € /mois` (« 30 conversions / mois ») ; Pro `13,90 € /mois` (« 100 conversions / mois ») ; Business `26,90 € /mois` (« 500 conversions / mois ») ; « Tous les prix sont indiqués en euros TTC ». Submitted by the editor.

- [FormatX](https://formatx.fr/) — title « FormatX - Convertir PDF en Factur-X gratuitement | Facture électronique conforme » ; schema.org `"price":"0","priceCurrency":"EUR"`. [`/api-docs`](https://formatx.fr/api-docs): « Accès libre pendant la phase de pré-commercialisation. Aucun quota mensuel, aucune facturation. » ; « Un rate limit technique de 60 requêtes/minute reste en place pour la stabilité du service. » ; « Une grille tarifaire sera mise en place à terme. »

- [Get FacturX](https://www.getfacturx.com/) — H1 « Créez, envoyez et recevez vos factures Factur-X, sans ERP » ; title « Facturation Factur-X en ligne et gratuite | Get Factur-X ». [`/validate`](https://www.getfacturx.com/validate) title « Factur-X Validator : validateur Factur-X gratuit en ligne » ; « La validation de base est gratuite pour une facture à la fois. » Euro tariff `[non-mesure]`. Home HEAD = 200, GET = 200.

- [InvoiceIn](https://invoicein.peculiar.systems/) — tagline « Every e-invoice you receive, as one JSON. » ; accepts « XRechnung, ZUGFeRD, Factur-X, Peppol BIS 3, FatturaPA, KSeF » ; [API reference](https://invoicein-api.peculiar.systems/docs). Pricing on page (« Beta pricing »): Free `100 invoices` (30 days) ; Starter `29 eur / 250 invoices` ; Growth `99 eur / 1,000` ; Scale `399 eur / 5,000`. Claims: theirs, not restated.

- [ITB — Commission eInvoice Validator](https://www.itb.ec.europa.eu/invoice/upload) — H1 « eInvoice Validator » ; types `cii` / `ubl` / `credit` labelled « release 1.3.17 ». REST `POST https://www.itb.ec.europa.eu/vitb/rest/invoice/api/validate` (HEAD 405). Not a GitHub repo.

- [Kontevia — E-Rechnung prüfen](https://kontevia.de/tools/e-rechnung-pruefen) — H1 « E-Rechnung prüfen: XRechnung und ZUGFeRD Validator online, ohne Upload » ; page states « Kostenlos, ohne Anmeldung » and « Die Prüfung läuft in Ihrem Browser, die Datei wird nicht hochgeladen » ; « Der Prüfer ist keine Schematron-Validierung ». Price [non-mesure].

- [Mustangproject — CLI validate](https://www.mustangproject.org/commandline/) — home: « Mustangproject 2.26.0 was released on 25.08.2026 » ; « Support for ZUGFeRD 2.5.2 (=Factur-X 1.09.2, #1216) » (2.25.0 note). CLI page: Validate + `Mustang-CLI-2.26.0.jar`. CLI **not executed** this run (`[non-mesure]` runtime).

- [phax/phive](https://github.com/phax/phive) — Java validation engine ; API description « Generic business document validation engine » ; README: rules are in a separate repository. Apache-2.0. **`stargazers_count` = 77**. Last push 2026-10-08 ; release `v12.2.0` (2026-09-28).

- [phax/phive-rules](https://github.com/phax/phive-rules) — preconfigured rule sets for phive ; API description « eInvoice Validation rules for the phive engine - for many different countries and jurisdictions » ; README lists modules `phive-rules-en16931`, `phive-rules-xrechnung` and `phive-rules-zugferd` (« German ZuGFERD and French Factur-X (XML part only) ») ; EN 16931 rules 1.3.17 noted as added. API `license.spdx_id` = `NOASSERTION` ; README: « The Java code in this project is licensed under the Apache 2 license. » ; validation artefacts may carry other licences. **`stargazers_count` = 52**. Last push 2026-10-17 ; release `v4.6.3` (2026-09-30).

- [phax/phorm](https://github.com/phax/phorm) — API description « Phorm - Business Document Validation Service » ; README: « a simple, standalone validation service (Phorm) accessible by API only », based on phive and phive-rules. Apache-2.0. **`stargazers_count` = 32**. Last push 2026-10-18 ; release `v2.2.11` (2026-09-30).

- [thelawin.dev](https://thelawin.dev/) — H1 « The E-Invoicing Engine » ; site labels « Factur-X 1.0.8 », « ZUGFeRD 2.4 » (FNFE/FeRD pack this day = 1.09.2 / 2.5.2). [Pricing](https://thelawin.dev/pricing): Sandbox `€0`, Starter `€9.50 /month`, Pro `€24.50 /month`, « Beta pricing: 50% off all paid plans ».

- [Valinvo](https://valinvo.bmk-hub.com/) — H1 « XRechnung and Peppol e-invoices from one JSON call » ; FAQ: « The online validator on this page is free and needs no account or API key. Your file is processed in memory and not stored. » and « ZUGFeRD / Factur-X is coming ». Page badge « Beta · XRechnung 3.0.2 · Peppol BIS 3.0.21 ». Pricing on page: Free `€0 / month` (« 2 invoices / day to try the API, no key needed ») ; Starter `€29 / month` (« 1,000 documents / month ») ; Growth `€99 / month` (« 10,000 documents / month ») ; Business `€299 / month` (« 50,000 documents / month ») ; « For business customers only. Prices in EUR, excluding VAT. » Paid plans are not open yet: « Paid plans open after the beta — write to us for early access. » Submitted by the operator.

- [xmlvalid](https://xmlvalid.com/schematron-validator) — H1 « Schematron validator for e-invoices » ; « EN 16931 1.3.17 […] on the EN 16931 profiles », « Peppol, XRechnung and the French profiles run 1.3.16 » ; « Nothing is uploaded ». [Pricing](https://xmlvalid.com/pricing): Free `$0 forever`, Pro `$290 per year`.

## GitHub Actions

Marketplace search on 2026-10-11, results in the order GitHub displayed them: [`factur-x`](https://github.com/marketplace?type=actions&query=factur-x) → « 5 results »: `validate-en16931-e-invoice`, `validate-e-invoice-en-16931`, `prufix`, `beliq-e-invoice-validate`, `invowerk-api`. [`zugferd`](https://github.com/marketplace?type=actions&query=zugferd) → « 3 results »: `validate-en16931-e-invoice`, `beliq-e-invoice-validate`, `invowerk-api`. [`en16931`](https://github.com/marketplace?type=actions&query=en16931) → « 1 result »: `validate-en16931-e-invoice`. Search results are listed here, not added as entries.

- [attestwire/validate-einvoice-action](https://github.com/attestwire/validate-einvoice-action) — created 2026-08-16 ; API description « Validate EN 16931 e-invoices (UBL, CII, Factur-X PDF) in CI. Runs locally by default — no API key, no network. » MIT. **`stargazers_count` = 0**. Release `v1.10.0` « v1.10.0: engine 0.14.1 » (2026-10-04). Marketplace card: Validate E-Invoice (EN 16931). Claims: theirs, not restated.

- [eleata/validate-einvoice-action](https://github.com/eleata/validate-einvoice-action) — formerly `hernaninverso/validate-einvoice-action` (old URL redirects) ; API description « Validate EU e-invoices (Peppol BIS, EN 16931, XRechnung, Factur-X, UBL, CII) in CI — backed by eleata.io, with plain-English fix hints per error. » Composite Action ; `action.yml` name `Validate EU e-Invoice` ; `format` includes `factur-x` ; default `api-base` `https://api.eleata.io`. Apache-2.0. **`stargazers_count` = 0**. Last push 2026-05-25. Claims: theirs, not restated.

- [facturxapi/validate-einvoice](https://github.com/facturxapi/validate-einvoice) — API description « GitHub Action that runs the official ConnectingEurope EN16931 XSLT artefacts (CII/UBL): 1.3.16 by default, 1.3.17 opt-in. » EUPL 1.2 (API `NOASSERTION`). **`stargazers_count` = 4**. Release `v1.2.0` (2026-10-18). *(list maintainer's project)*

- [invoicenavigator/validate-invoice](https://github.com/invoicenavigator/validate-invoice) — Action `node20` ; API description « GitHub Action to validate EU e-invoices against EN 16931, Peppol, XRechnung, and ZUGFeRD ». MIT. **`stargazers_count` = 0**. Last push 2026-03-02. **No release**. **Not a Marketplace card.**

- [wsystemdev/einvoice-validate-action](https://github.com/wsystemdev/einvoice-validate-action) — created 2026-10-26 ; API description « GitHub Action: validate UBL, CII and ZUGFeRD/Factur-X e-invoices against EN 16931 and XRechnung rules in CI » ; composite Action ; `action.yml` name `EU e-invoice validator (EN 16931, XRechnung)` ; default `api-url` `https://api.wsystem.dev` (files are sent to that API) ; `api-key` input: « free key: 500 units a month, no card » ; « Without one, each runner IP gets 20 free calls a day. » MIT. **`stargazers_count` = 0**. Release `v1.0.0` (2026-10-26). **Not a Marketplace card.** Claims: theirs, not restated.

## Libraries

- [akretion/factur-x](https://github.com/akretion/factur-x) — Python Factur-X / Order-X / UBL. API `license.spdx_id` = **`NOASSERTION`** ; `LICENSE.txt` = BSD 3-clause. **`stargazers_count` = 310**. Last push / release `7.5` (2026-10-09).

- [attestwire/en16931](https://github.com/attestwire/en16931) — TypeScript EN 16931 validator and generator ; description API « EN 16931 e-invoice validator and generator for TypeScript. XRechnung, Peppol BIS, Factur-X, UBL and CII. Zero deps. » MIT. **`stargazers_count` = 1**. Last push 2026-10-04 ; release `v0.14.1` (`published_at` 2026-10-06 ; notes « Released 2026-10-04 »).

- [horstoeko/zugferd](https://github.com/horstoeko/zugferd) — PHP ZUGFeRD / XRechnung / Factur-X. MIT. **`stargazers_count` = 437**. Last push 2026-10-02 ; release `v1.0.132` (2026-08-30). README names [horstoeko/invoicesuite](https://github.com/horstoeko/invoicesuite) as « The official successor and primary focus of future development ».

- [kadour-ia/Facturx-lire](https://github.com/kadour-ia/Facturx-lire) — API description « Lire en clair une facture électronique reçue (Factur-X, ZUGFeRD, CII, UBL) — gratuit, 100% local. Réforme 2026. » MIT. **`stargazers_count` = 0**. Last push 2026-10-11. **No GitHub release**. README: written and maintained by an autonomous AI agent (declared). Claims: theirs, not restated.

- [phax/en16931-cii2ubl](https://github.com/phax/en16931-cii2ubl) — API description « Converter for EN16931 invoices from CII to UBL » ; README: EN 16931:2017 CII D16B → UBL 2.1, EN 16931:2026 CII D25A → UBL 2.5. Apache-2.0. **`stargazers_count` = 47**. Last push 2026-10-08 ; release `v4.0.2` (2026-10-07).

- [phax/en16931-purifier](https://github.com/phax/en16931-purifier) — API description « Remove all extended elements from EN 16931 Invoices (CII and UBL) » ; README: input syntax is also output syntax, « this project is not a converter ». Apache-2.0. **`stargazers_count` = 1**. Last push 2026-10-08 ; release `v1.1.0` (2026-09-06).

- [phax/en16931-ubl2cii](https://github.com/phax/en16931-ubl2cii) — API description « Converter for EN 16931 invoices from UBL 2.1 to CII D16B » ; README: EN 16931:2017 UBL 2.1 → CII D16B, EN 16931:2026 UBL 2.5 → CII D25A. Apache-2.0. **`stargazers_count` = 10**. Last push 2026-10-08 ; release `v3.0.1` (2026-10-07).

- [phax/kaltblut](https://github.com/phax/kaltblut) — API description « Java library helping you to handle ZUGFeRD invoices » ; README: detects the flavour of hybrid PDFs, extracts the embedded XML and validates carrier-side rules incl. PDF/A-3 via veraPDF ; « XML-side business rules […] are out of scope ». Apache-2.0. **`stargazers_count` = 6**. Last push 2026-10-18 ; release `v0.9.5` (2026-08-09).

- [phax/ph-cii](https://github.com/phax/ph-cii) — API description « Java Wrapper for the UN/CEFACT Cross Industry Invoice » ; README: D16A.1 and D16B for EN 16931:2017, D22B for ZUGFeRD 2.3+, D25A for EN 16931:2026. Apache-2.0. **`stargazers_count` = 15**. Last push 2026-10-08 ; release `v4.1.3` (2026-09-22).

- [phax/ph-redact](https://github.com/phax/ph-redact) — API description « Simple eInvoice Anonymizer » ; README: XSLT-based XML anonymiser for UBL and CII (EN 16931:2017 UBL 2.1 / CII D16B, EN 16931:2026 UBL 2.5 / CII D25A) that keeps structure, monetary and tax values. Apache-2.0. **`stargazers_count` = 3**. Last push 2026-10-09 ; release `v1.1.0` (2026-09-08).

- [phax/ph-ubl](https://github.com/phax/ph-ubl) — API description « Java library for reading and writing UBL 2.0, 2.1, 2.2, 2.3, 2.4 and 2.5 documents ». Apache-2.0. **`stargazers_count` = 141**. Last push 2026-10-17 ; release `v10.2.1` (2026-08-27).

- [pretix/python-drafthorse](https://github.com/pretix/python-drafthorse) — API description « Pure-python ZUGFeRD implementation ». Apache-2.0. **`stargazers_count` = 179**. Last push 2026-06-02. **No GitHub release**.

- [stephanstapel/ZUGFeRD-csharp](https://github.com/stephanstapel/ZUGFeRD-csharp) — C# ZUGFeRD read / write. Apache-2.0 (`LICENSE.txt`). **`stargazers_count` = 395**. Last push / release `18.0.1` (2026-10-09). README: « My maintenance of this project will end on November 30, 2026. » ; names FactoorSharp as « the commercial successor ».

- [ZUGFeRD/mustangproject](https://github.com/ZUGFeRD/mustangproject) — Java library / CLI to read, write, convert and validate Factur-X/ZUGFeRD and XRechnung. Apache-2.0. **`stargazers_count` = 480**. Last push 2026-10-10 ; release `core-2.26.0` (2026-08-25).

## Corpora

Only publicly licensed, still-living example sets. FNFE ZIP (email gate) and FeRD Infopaket are **not** redistributable corpora here.

- [ConnectingEurope — EN 16931 v1.3.17 examples](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17) — release « EN16931 Validation artefacts v1.3.17 » ; body: examples in folder `"examples"` ; EUPL 1.2 ; assets `en16931-cii-1.3.17.zip`, `en16931-ubl-1.3.17.zip`.

- [facturxapi/en16931-oracles](https://github.com/facturxapi/en16931-oracles) — API description « Reproducible EN16931 validation oracles — ConnectingEurope 1.3.17 fixtures, SVRL receipts, and mutants. » API `NOASSERTION`. **`stargazers_count` = 4**. Release `v1.1.0` « v1.1.0 — BR-FR Flux2 oracles (France_RFE v1.4.0.x) » (2026-08-21). *(list maintainer's project)*

- [itplr-kosit/xrechnung-testsuite](https://github.com/itplr-kosit/xrechnung-testsuite) — GitHub mirror of KoSIT ([GitLab](https://projekte.kosit.org/xrechnung/xrechnung-testsuite) HTTP 200). Apache-2.0. Last push 2026-09-08. Release `v2026-08-31` « Testsuite release in version 2026-08-31 compatible with XRechnung 3.0 » (2026-09-02): asset `xrechnung-3.0.2-testsuite-2026-08-31.zip`.

- [kobima6813/einvoice-conformance-matrix](https://github.com/kobima6813/einvoice-conformance-matrix) — API description « Reproducible cross-validator conformance matrix for EN 16931 e-invoice generators (KoSIT/XRechnung, CEN, Peppol BIS, due-vs-charged), with a GitHub Action. » Apache-2.0. **`stargazers_count` = 0**. Last push 2026-10-20 ; **No release**.

## Related lists

- [causa-prima-ai/awesome-invoicing](https://github.com/causa-prima-ai/awesome-invoicing) — « curated list of invoicing and e-invoicing tools […] EN 16931, XRechnung, ZUGFeRD, Peppol BIS, Factur-X ». File `LICENSE` = CC0 1.0 (API `NOASSERTION`). Last push 2026-07-07 ; **`stargazers_count` = 1**.

- [e-invoice-be/awesome-peppol](https://github.com/e-invoice-be/awesome-peppol) — repo exists (HTTP 200) but **empty**: README = one line `# awesome-peppol` (16 bytes) ; `license`: **null**. Last push 2026-06-12 ; **`stargazers_count` = 0**.

- [morganrcu/awesome-europe](https://github.com/morganrcu/awesome-europe) — OSS « for Europe » (CC0-1.0), *Electronic Invoicing* section. Last push 2026-03-24 ; **`stargazers_count` = 0**.

- [sdras/awesome-actions](https://github.com/sdras/awesome-actions) — GitHub Actions list (CC0-1.0). **`stargazers_count` = 28306**. **Last push 2024-09-01** (> 18 months at 11 Oct 2026). README: **no** Factur-X / ZUGFeRD / e-invoice / EN 16931 occurrence (checked 11/10).

---

## Out of scope

Generic lint / scan Actions (reviewdog/eslint, trivy, golangci-lint, megalinter) are **not** e-invoicing entries — see [`LICENSE-NOTES.md`](LICENSE-NOTES.md).

*Last full check: 2026-10-11, see [CHECKS.md](CHECKS.md).*
