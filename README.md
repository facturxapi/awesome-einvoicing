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

- [ConnectingEurope/eInvoicing-EN16931](https://github.com/ConnectingEurope/eInvoicing-EN16931) — official EN 16931 Schematron artefacts (UBL + CII) ; latest UBL & CII **v1.3.16** (2026-04-10) ; README: « This repository does not contain eInvoicing-EN16931 rules for any CIUS. » File `LICENSE.txt` EUPL 1.2 (API `license.spdx_id` = `NOASSERTION`).

- [FeRD — ZUGFeRD / Factur-X](https://www.ferd-net.de/) — Forum elektronische Rechnung Deutschland ; home: « ZUGFeRD 2.5.2 veröffentlicht » ; « Eschborn | Paris, 04.08.2026 ».

- [FNFE-MPE — Factur-X](https://fnfe-mpe.org/factur-x/) — « Le 4 août 2026, le FNFE-MPE et le FERD publient la dernière release, à savoir: Factur-X 1.09.2 et ZUGFeRD 2.5.2 » ; « Techniquement, Factur-X et ZUGFeRD sont identiques. » ZIP behind an email field.

- [fnfempe/France_RFE](https://github.com/fnfempe/France_RFE) — France CTC / BR-FR validation artefacts (XP Z12-012 / 014) ; release `v1.4.0.04` « FNFE_RFE_INVOICE_1.4.0.04 » (`published_at` 2026-09-04T22:42:01Z) ; API license Apache-2.0 ; no uploaded release assets (source archives only).

## Official docs

- [AFNOR XP Z12-012 (shop)](https://www.boutique.afnor.org/fr-fr/norme/xp-z12012/formats-et-profils-des-messages-factures-et-statuts-de-cycle-de-vie-constit/fa301169/601641) — « XP Z12-012 juin 2026 » « En vigueur » « Consultation gratuite ». Body of the standard **not read** (`[non-mesure]`).

- [DGFiP — accredited platforms](https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees) — « Je consulte la liste des plateformes agréées » ; « Publié le 30/07/2024, modifié le 22/09/2026 ».

- [DGFiP — reform FAQ](https://www.impots.gouv.fr/professionnel/questions/dans-le-cadre-de-la-reforme-de-la-facturation-electronique-comment-devrais) — « À compter du 1er septembre 2026 , toutes les entreprises assujetties à la TVA […] devront être en capacité de recevoir des factures électroniques ». « septembre 2027 » **absent** from the HTML this run.

- [European Commission — Registry of supporting artefacts to implement EN16931](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108974/Registry+of+supporting+artefacts+to+implement+EN16931) — official DIGITAL registry: EN 16931 validation artefacts (UBL 2.1 + CII 16b, latest **1.3.16**, published 16/04/26), EAS and VATEX code lists, CIUS/Extensions registry, and the bi-annual release schedule.

- [FeRD — Download ZUGFeRD](https://www.ferd-net.de/download-zugferd) — « Infopaket für das E-Rechnungsformat ZUGFeRD 2.5.2 vom 04.08.2026 » ; Direktdownload 27.94 MB (DE) / 28.98 MB (EN). **ZIP not downloaded**.

- [FeRD — Was ist ZUGFeRD?](https://www.ferd-net.de/standards/zugferd) — « ZUGFeRD ist ein kostenfrei verfügbares, branchenübergreifendes Datenformat […] » ; cited base: Norm EN16931.

- [FNFE-MPE — Ressources](https://fnfe-mpe.org/ressources/) — « 30 juin 2026 : Publication des nouvelles versions des normes XP Z12 -012, 013, 014 » ; « XP Z12-012 (30/06/2026) 1.4.0 » ; « Version 1.4.0 des schematrons » (fix04 du 4 septembre), file `2026_09_04_FNFE_SCHEMATRONS_FR_CTC_V1.4.0.04.zip`.

## Validators

Tools that present themselves as a validator, converter or API. **Not a ranking.**

- [B2Brouter — Factur-X validator](https://www.b2brouter.net/fr/factur-x-validator/) — title « Factur-X validator : en ligne, conforme et gratuit » (their title) ; platform [pricing](https://www.b2brouter.net/fr/tarifs/) HTML: Basic `0 eur / à vie` ; Professional `110 eur / an + TVA` ; Business `300 eur / an + TVA`.

- [e-invoice-be/peppol-cli](https://github.com/e-invoice-be/peppol-cli) — Go CLI (binary `peppol`) ; API description « CLI for the e-invoice.be Peppol API ». MIT. **`stargazers_count` = 3**. Release `v0.0.7` (2026-10-14). `internal/cli/validate.go`: `validate ubl` and `validate json` « against Peppol BIS Billing 3.0 », sent to `https://api.e-invoice.be` with an API key (not run locally). [Landing page](https://e-invoice.be/peppol-cli): « Requires an e-invoice.be account. » Price `[non-mesure]`.

- [E-Rechnung API](https://e-rechnung-api.fly.dev/) — H1 « ZUGFeRD & Factur-X API » ; title « ZUGFeRD & Factur-X API | E-Rechnungen leicht gemacht ». Validator [`/validator`](https://e-rechnung-api.fly.dev/validator): title « Kostenloser ZUGFeRD & XRechnung Validator (EN 16931) » ; drag-and-drop validation for PDF/A-3 and XML without registration. Pricing: Test `0€`, Prepaid `10€ / 100 Dok.`, Starter `29€ / Monat`.

- [FactureValide](https://facturevalide.fr/) — H1 « Votre facture valide en 2 minutes. Point. » ; « Gratuit pendant le lancement » ; « Sans limite · Sans carte bancaire ». Validator [`/valider-facture-electronique.html`](https://facturevalide.fr/valider-facture-electronique.html): « 10 vérifications/jour » ; « 31 points de contrôle ». `/tarifs` and `/tarifs.html` = **404**.

- [facturx-validator.fr](https://facturx-validator.fr/) — H1 « Vérifiez vos factures Factur-X gratuitement » ; footer « Outil gratuit et open source. » [`/verifier`](https://facturx-validator.fr/verifier): « Fichier PDF uniquement (max. 10 Mo) » ; profiles Minimum, Basic, EN16931, Extended. Euro price `[non-mesure]`. No repo link on the pages opened (`[non-mesure]` repo).

- [FormatX](https://formatx.fr/) — title « FormatX - Convertir PDF en Factur-X gratuitement | Facture électronique conforme » ; schema.org `"price":"0","priceCurrency":"EUR"`. [`/api-docs`](https://formatx.fr/api-docs): « Accès libre pendant la phase de pré-commercialisation. Aucun quota mensuel, aucune facturation. » ; « Un rate limit technique de 60 requêtes/minute reste en place pour la stabilité du service. » ; « Une grille tarifaire sera mise en place à terme. »

- [Get FacturX](https://www.getfacturx.com/) — H1 « Créez, envoyez et recevez vos factures Factur-X, sans ERP » ; title « Facturation Factur-X en ligne et gratuite | Get Factur-X ». [`/validate`](https://www.getfacturx.com/validate) title « Factur-X Validator : validateur Factur-X gratuit en ligne » ; « La validation de base est gratuite pour une facture à la fois. » Euro tariff `[non-mesure]`. Home HEAD = 200, GET = 200.

- [InvoiceIn](https://invoicein.peculiar.systems/) — tagline « Every e-invoice you receive, as one JSON. » ; accepts « XRechnung, ZUGFeRD, Factur-X, Peppol BIS 3, FatturaPA, KSeF » ; [API reference](https://invoicein-api.peculiar.systems/docs). Pricing on page (« Beta pricing »): Free `100 invoices` (30 days) ; Starter `29 eur / 250 invoices` ; Growth `99 eur / 1,000` ; Scale `399 eur / 5,000`. Claims: theirs, not restated.

- [ITB — Commission eInvoice Validator](https://www.itb.ec.europa.eu/invoice/upload) — H1 « eInvoice Validator » ; types `cii` / `ubl` / `credit` labelled « release 1.3.16 ». REST `POST https://www.itb.ec.europa.eu/vitb/rest/invoice/api/validate` (HEAD 405). Not a GitHub repo.

- [Kontevia — E-Rechnung prüfen](https://kontevia.de/tools/e-rechnung-pruefen) — H1 « E-Rechnung prüfen: XRechnung und ZUGFeRD Validator online, ohne Upload » ; page states « Kostenlos, ohne Anmeldung » and « Die Prüfung läuft in Ihrem Browser, die Datei wird nicht hochgeladen » ; « Der Prüfer ist keine Schematron-Validierung ». Price [non-mesure].

- [Mustangproject — CLI validate](https://www.mustangproject.org/commandline/) — home: « Mustangproject 2.26.0 was released on 25.08.2026 » ; « Support for ZUGFeRD 2.5.2 (=Factur-X 1.09.2, #1216) » (2.25.0 note). CLI page: Validate + `Mustang-CLI-2.26.0.jar`. CLI **not executed** this run (`[non-mesure]` runtime).

- [thelawin.dev](https://thelawin.dev/) — H1 « The E-Invoicing Engine » ; site labels « Factur-X 1.0.8 », « ZUGFeRD 2.4 » (FNFE/FeRD pack this day = 1.09.2 / 2.5.2). [Pricing](https://thelawin.dev/pricing): Sandbox `€0`, Starter `€9.50 /month`, Pro `€24.50 /month`, « Beta pricing: 50% off all paid plans ».

## GitHub Actions

Marketplace search on 2026-10-11, results in the order GitHub displayed them: [`factur-x`](https://github.com/marketplace?type=actions&query=factur-x) → « 5 results »: `validate-en16931-e-invoice`, `validate-e-invoice-en-16931`, `prufix`, `beliq-e-invoice-validate`, `invowerk-api`. [`zugferd`](https://github.com/marketplace?type=actions&query=zugferd) → « 3 results »: `validate-en16931-e-invoice`, `beliq-e-invoice-validate`, `invowerk-api`. [`en16931`](https://github.com/marketplace?type=actions&query=en16931) → « 1 result »: `validate-en16931-e-invoice`. Search results are listed here, not added as entries.

- [attestwire/validate-einvoice-action](https://github.com/attestwire/validate-einvoice-action) — created 2026-08-16 ; API description « Validate EN 16931 e-invoices (UBL, CII, Factur-X PDF) in CI. Runs locally by default — no API key, no network. » MIT. **`stargazers_count` = 0**. Release `v1.10.0` « v1.10.0: engine 0.14.1 » (2026-10-04). Marketplace card: Validate E-Invoice (EN 16931). Claims: theirs, not restated.

- [eleata/validate-einvoice-action](https://github.com/eleata/validate-einvoice-action) — formerly `hernaninverso/validate-einvoice-action` (old URL redirects) ; API description « Validate EU e-invoices (Peppol BIS, EN 16931, XRechnung, Factur-X, UBL, CII) in CI — backed by eleata.io, with plain-English fix hints per error. » Composite Action ; `action.yml` name `Validate EU e-Invoice` ; `format` includes `factur-x` ; default `api-base` `https://api.eleata.io`. Apache-2.0. **`stargazers_count` = 0**. Last push 2026-05-25. Claims: theirs, not restated.

- [facturxapi/validate-einvoice](https://github.com/facturxapi/validate-einvoice) — API description « GitHub Action that runs the official ConnectingEurope EN16931 1.3.16 XSLT artefacts (CII/UBL). » EUPL 1.2 (API `NOASSERTION`). **`stargazers_count` = 4**. Release `v1.1.2` (2026-10-11). *(list maintainer's project)*

- [invoicenavigator/validate-invoice](https://github.com/invoicenavigator/validate-invoice) — Action `node20` ; API description « GitHub Action to validate EU e-invoices against EN 16931, Peppol, XRechnung, and ZUGFeRD ». MIT. **`stargazers_count` = 0**. Last push 2026-03-02. **No release**. **Not a Marketplace card.**

## Libraries

- [akretion/factur-x](https://github.com/akretion/factur-x) — Python Factur-X / Order-X / UBL. API `license.spdx_id` = **`NOASSERTION`** ; `LICENSE.txt` = BSD 3-clause. **`stargazers_count` = 310**. Last push / release `7.5` (2026-10-09).

- [attestwire/en16931](https://github.com/attestwire/en16931) — TypeScript EN 16931 validator and generator ; description API « EN 16931 e-invoice validator and generator for TypeScript. XRechnung, Peppol BIS, Factur-X, UBL and CII. Zero deps. » MIT. **`stargazers_count` = 1**. Last push 2026-10-04 ; release `v0.14.1` (`published_at` 2026-10-06 ; notes « Released 2026-10-04 »).

- [horstoeko/zugferd](https://github.com/horstoeko/zugferd) — PHP ZUGFeRD / XRechnung / Factur-X. MIT. **`stargazers_count` = 437**. Last push 2026-10-02 ; release `v1.0.132` (2026-08-30). README names [horstoeko/invoicesuite](https://github.com/horstoeko/invoicesuite) as « The official successor and primary focus of future development ».

- [kadour-ia/Facturx-lire](https://github.com/kadour-ia/Facturx-lire) — API description « Lire en clair une facture électronique reçue (Factur-X, ZUGFeRD, CII, UBL) — gratuit, 100% local. Réforme 2026. » MIT. **`stargazers_count` = 0**. Last push 2026-10-11. **No GitHub release**. README: written and maintained by an autonomous AI agent (declared). Claims: theirs, not restated.

- [pretix/python-drafthorse](https://github.com/pretix/python-drafthorse) — API description « Pure-python ZUGFeRD implementation ». Apache-2.0. **`stargazers_count` = 179**. Last push 2026-06-02. **No GitHub release**.

- [stephanstapel/ZUGFeRD-csharp](https://github.com/stephanstapel/ZUGFeRD-csharp) — C# ZUGFeRD read / write. Apache-2.0 (`LICENSE.txt`). **`stargazers_count` = 395**. Last push / release `18.0.1` (2026-10-09). README: « My maintenance of this project will end on November 30, 2026. » ; names FactoorSharp as « the commercial successor ».

- [ZUGFeRD/mustangproject](https://github.com/ZUGFeRD/mustangproject) — Java library / CLI to read, write, convert and validate Factur-X/ZUGFeRD and XRechnung. Apache-2.0. **`stargazers_count` = 480**. Last push 2026-10-10 ; release `core-2.26.0` (2026-08-25).

## Corpora

Only publicly licensed, still-living example sets. FNFE ZIP (email gate) and FeRD Infopaket are **not** redistributable corpora here.

- [ConnectingEurope — EN 16931 v1.3.16 examples](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.16) — release « EN16931 Validation artefacts v1.3.16 » ; body: examples in folder `"examples"` ; EUPL 1.2 ; assets `en16931-cii-1.3.16.zip`, `en16931-ubl-1.3.16.zip`.

- [facturxapi/en16931-oracles](https://github.com/facturxapi/en16931-oracles) — API description « Reproducible EN16931 validation oracles — ConnectingEurope 1.3.16 fixtures, SVRL receipts, and mutants. » API `NOASSERTION`. **`stargazers_count` = 4**. Release `v1.1.0` « v1.1.0 — BR-FR Flux2 oracles (France_RFE v1.4.0.x) » (2026-08-21). *(list maintainer's project)*

- [itplr-kosit/xrechnung-testsuite](https://github.com/itplr-kosit/xrechnung-testsuite) — GitHub mirror of KoSIT ([GitLab](https://projekte.kosit.org/xrechnung/xrechnung-testsuite) HTTP 200). Apache-2.0. Last push 2026-09-08. Release `v2026-08-31` « Testsuite release in version 2026-08-31 compatible with XRechnung 3.0 » (2026-09-02): asset `xrechnung-3.0.2-testsuite-2026-08-31.zip`.

## Related lists

- [causa-prima-ai/awesome-invoicing](https://github.com/causa-prima-ai/awesome-invoicing) — « curated list of invoicing and e-invoicing tools […] EN 16931, XRechnung, ZUGFeRD, Peppol BIS, Factur-X ». File `LICENSE` = CC0 1.0 (API `NOASSERTION`). Last push 2026-07-07 ; **`stargazers_count` = 1**.

- [e-invoice-be/awesome-peppol](https://github.com/e-invoice-be/awesome-peppol) — repo exists (HTTP 200) but **empty**: README = one line `# awesome-peppol` (16 bytes) ; `license`: **null**. Last push 2026-06-12 ; **`stargazers_count` = 0**.

- [morganrcu/awesome-europe](https://github.com/morganrcu/awesome-europe) — OSS « for Europe » (CC0-1.0), *Electronic Invoicing* section. Last push 2026-03-24 ; **`stargazers_count` = 0**.

- [sdras/awesome-actions](https://github.com/sdras/awesome-actions) — GitHub Actions list (CC0-1.0). **`stargazers_count` = 28306**. **Last push 2024-09-01** (> 18 months at 11 Oct 2026). README: **no** Factur-X / ZUGFeRD / e-invoice / EN 16931 occurrence (checked 11/10).

---

## Out of scope

Generic lint / scan Actions (reviewdog/eslint, trivy, golangci-lint, megalinter) are **not** e-invoicing entries — see [`LICENSE-NOTES.md`](LICENSE-NOTES.md).

*Last full check: 2026-10-11, see [CHECKS.md](CHECKS.md).*
