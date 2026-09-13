# Awesome e-Invoicing [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Sourced map / curated list of **e-invoicing** specs, docs, validators, libraries and corpora — not a ranking (EN 16931, Factur-X, ZUGFeRD, XRechnung, BR-FR).

> **Inclusion ≠ endorsement.** A line here does not mean a tool is compliant, official, better, or recommended.
>
> Each line is **factual** (what the page or GitHub API said this run). Prices only if they appear in the HTML ; otherwise `[non-mesure]`. Words like “valide / conforme / répare” are the site’s, not ours.

HTTP / licenses / liveness: [`CHECKS.md`](CHECKS.md). Redistribute vs pointer: [`LICENSE-NOTES.md`](LICENSE-NOTES.md). Frame: [`NOTICE.md`](NOTICE.md). How to add a line: [`CONTRIBUTING.md`](CONTRIBUTING.md). List text: [CC0 1.0](LICENSE).

## Which FacturX repo should I use?

- [validate-einvoice](https://github.com/facturxapi/validate-einvoice) — GitHub Action that runs the official ConnectingEurope EN16931 1.3.16 XSLT artefacts (CII/UBL).
- [en16931-oracles](https://github.com/facturxapi/en16931-oracles) — Replayable fixtures, receipts and mutants for that same 1.3.16 pin.
- [awesome-einvoicing](https://github.com/facturxapi/awesome-einvoicing) — Sourced map of specs, validators, libraries and corpora. Inclusion is not a ranking.

---

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

- [fnfempe/France_RFE](https://github.com/fnfempe/France_RFE) — France CTC / BR-FR validation artefacts (XP Z12-012 / 014) ; tag `v1.4.0.03` (`published_at` 2026-08-04T17:59:39Z) ; API license Apache-2.0 ; release `assets: []` this run.

## Official docs

- [AFNOR XP Z12-012 (shop)](https://www.boutique.afnor.org/fr-fr/norme/xp-z12012/formats-et-profils-des-messages-factures-et-statuts-de-cycle-de-vie-constit/fa301169/601641) — « XP Z12-012 juin 2026 » « En vigueur » « Consultation gratuite ». Body of the standard **not read** (`[non-mesure]`).

- [DGFiP — accredited platforms](https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees) — « Je consulte la liste des plateformes agréées » ; « Publié le 30/07/2024, modifié le 17/08/2026 ».

- [DGFiP — reform FAQ](https://www.impots.gouv.fr/professionnel/questions/dans-le-cadre-de-la-reforme-de-la-facturation-electronique-comment-devrais) — « À compter du 1er septembre 2026 , toutes les entreprises assujetties à la TVA […] devront être en capacité de recevoir des factures électroniques ». « septembre 2027 » **absent** from the HTML this run.

- [European Commission — Registry of supporting artefacts to implement EN16931](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108974/Registry+of+supporting+artefacts+to+implement+EN16931) — official DIGITAL registry: EN 16931 validation artefacts (UBL 2.1 + CII 16b, latest **1.3.16**, published 16/04/26), EAS and VATEX code lists, CIUS/Extensions registry, and the bi-annual release schedule.

- [FeRD — Download ZUGFeRD](https://www.ferd-net.de/download-zugferd) — « Infopaket für das E-Rechnungsformat ZUGFeRD 2.5.2 vom 04.08.2026 » ; Direktdownload 27.94 MB (DE) / 28.98 MB (EN). **ZIP not downloaded**.

- [FeRD — Was ist ZUGFeRD?](https://www.ferd-net.de/standards/zugferd) — « ZUGFeRD ist ein kostenfrei verfügbares, branchenübergreifendes Datenformat […] » ; cited base: Norm EN16931.

- [FNFE-MPE — Ressources](https://fnfe-mpe.org/ressources/) — « 30 juin 2026 : Publication des nouvelles versions des normes XP Z12 -012, 013, 014 » ; « XP Z12-012 (30/06/2026) 1.4.0 » ; schematrons BR-FR-CTC fix03 du 4 août.

## Validators

Tools that present themselves as a validator, converter or API. **Not a ranking.**

- [B2Brouter — Factur-X validator](https://www.b2brouter.net/fr/factur-x-validator/) — title « Factur-X validator : en ligne, conforme et gratuit » (their title) ; platform [pricing](https://www.b2brouter.net/fr/tarifs/) HTML: Basic `0 eur / à vie` ; Professional `110 eur / an + TVA` ; Business `300 eur / an + TVA`.

- [FactureValide](https://facturevalide.fr/) — H1 « Votre facture valide en 2 minutes. Point. » ; « Gratuit pendant le lancement » ; « Sans limite · Sans carte bancaire ». Validator [`/valider-facture-electronique.html`](https://facturevalide.fr/valider-facture-electronique.html): « 10 vérifications/jour » ; « 31 points de contrôle ». `/tarifs` and `/tarifs.html` = **404**.

- [facturx-validator.fr](https://facturx-validator.fr/) — H1 « Vérifiez vos factures Factur-X gratuitement » ; footer « Outil gratuit et open source. » [`/verifier`](https://facturx-validator.fr/verifier): « Fichier PDF uniquement (max. 10 Mo) » ; profiles Minimum, Basic, EN16931, Extended. Euro price `[non-mesure]`. No repo link on the pages opened (`[non-mesure]` repo).

- [FacturX API](https://facturxapi.com/) — H1 « Ajoutez Factur-X à votre logiciel sans remplacer votre outil de facturation. » Euro price `[non-mesure]`. Home only. Claims: theirs, not restated.

- [FormatX](https://formatx.fr/) — title « FormatX - Convertir PDF en Factur-X gratuitement » ; schema.org `"price":"0","priceCurrency":"EUR"`. [`/api-docs`](https://formatx.fr/api-docs): v2 quotas without euros — Free 10 / Pro 100 / Business 500 invoices/month.

- [Get FacturX](https://www.getfacturx.com/) — H1 « La boîte à outils Factur-X qui complète votre Plateforme Agréée » ; CTA « 4 utilisations gratuites par jour · Aucune carte requise ». [`/validate`](https://www.getfacturx.com/validate) title « Validateur Factur-X en ligne gratuit ». Euro tariff `[non-mesure]`. Home HEAD = 405, GET = 200.

- [ITB — Commission eInvoice Validator](https://www.itb.ec.europa.eu/invoice/upload) — H1 « eInvoice Validator » ; types `cii` / `ubl` / `credit` labelled « release 1.3.16 ». REST `POST https://www.itb.ec.europa.eu/vitb/rest/invoice/api/validate` (HEAD 405). Not a GitHub repo.

- [Mustangproject — CLI validate](https://www.mustangproject.org/commandline/) — home: « Mustangproject 2.25.0 was released on 05.08.2026 » ; « Support for ZUGFeRD 2.5.2 (=Factur-X 1.09.2, #1216) ». CLI page: Validate + `Mustang-CLI-2.25.0.jar`. CLI **not executed** this run (`[non-mesure]` runtime).

- [NormAPI](https://normapi.de/en/validator) — German CIUS: XRechnung (UBL + CII) and ZUGFeRD PDF, checked « against the official KoSIT rule set » ; title « XRechnung & ZUGFeRD validator — free online check » ; H1 « Validate an e-invoice » ; « Your file is processed in memory and discarded immediately. » Footer stamp « Ruleset v2026-08-31 ». [Pricing](https://normapi.de/en/pricing) HTML: Validator `€0` « Free forever », Starter `€49 per month`, Business `€149 per month`.

- [thelawin.dev](https://thelawin.dev/) — H1 « The E-Invoicing Engine » ; site labels « Factur-X 1.0.8 », « ZUGFeRD 2.4 » (FNFE/FeRD pack this day = 1.09.2 / 2.5.2). [Pricing](https://thelawin.dev/pricing): Sandbox `€0`, Starter `€9.50 /month`, Pro `€24.50 /month`, « Beta pricing: 50% off all paid plans ».

## GitHub Actions

Marketplace this run (2026-08-24): [`factur-x`](https://github.com/marketplace?type=actions&query=factur-x) lists at least two EN16931 Action cards: [Validate E-Invoice (EN 16931)](https://github.com/marketplace/actions/validate-e-invoice-en-16931) = `attestwire/validate-einvoice-action`, and [Validate EN16931 e-invoice](https://github.com/marketplace/actions/validate-en16931-e-invoice) = `facturxapi/validate-einvoice`. [`zugferd`](https://github.com/marketplace?type=actions&query=zugferd) → **« 0 results »** on 2026-08-18 check.

- [attestwire/validate-einvoice-action](https://github.com/attestwire/validate-einvoice-action) — created 2026-08-16 ; API description « Validate EN 16931 e-invoices (UBL, CII, Factur-X PDF) in CI. Runs locally by default — no API key, no network. » MIT. **`stargazers_count` = 0**. Tag `v1.0.0`. Marketplace card above. Claims: theirs, not restated.

- [facturxapi/validate-einvoice](https://github.com/facturxapi/validate-einvoice) — API description « GitHub Action and CLI: official ConnectingEurope EN16931 1.3.16 XSLT (CII/UBL) on XML invoices. » File license EUPL 1.2 (API `NOASSERTION`). **`stargazers_count` = 2** (2026-08-24). Tag `v1` and `v1.1.0` → `b364f7c3175c357eec30ad074b8e57844d976d3d` (Windows-safe tree). Marketplace card: https://github.com/marketplace/actions/validate-en16931-e-invoice.

- [hernaninverso/validate-einvoice-action](https://github.com/hernaninverso/validate-einvoice-action) — composite Action ; `action.yml` name `Validate EU e-Invoice` ; `format` includes `factur-x` ; default `api-base` `https://api.eleata.io`. Apache-2.0. **`stargazers_count` = 0**. Last push 2026-05-25. Claims: theirs, not restated.

- [invoicenavigator/validate-invoice](https://github.com/invoicenavigator/validate-invoice) — Action `node20` ; API description « GitHub Action to validate EU e-invoices against EN 16931, Peppol, XRechnung, and ZUGFeRD ». MIT. **`stargazers_count` = 0**. Last push 2026-03-02. **No release**. **Not a Marketplace card.**

## Libraries

- [akretion/factur-x](https://github.com/akretion/factur-x) — Python Factur-X / Order-X / UBL. API `license.spdx_id` = **`NOASSERTION`** ; `LICENSE.txt` = BSD 3-clause. **`stargazers_count` = 303**. Last push / tag `6.7` (2026-08-08).

- [horstoeko/zugferd](https://github.com/horstoeko/zugferd) — PHP ZUGFeRD / XRechnung / Factur-X. MIT. **`stargazers_count` = 432**. Last push 2026-08-04 ; release `v1.0.124` (2026-07-10).

- [pretix/python-drafthorse](https://github.com/pretix/python-drafthorse) — « low-level python implementation of the ZUGFeRD XML format ». Apache-2.0. **`stargazers_count` = 176**. Last push 2026-06-02. **No GitHub release**.

- [stephanstapel/ZUGFeRD-csharp](https://github.com/stephanstapel/ZUGFeRD-csharp) — C# ZUGFeRD read / write. Apache-2.0 (`LICENSE.txt`). **`stargazers_count` = 392**. Last push 2026-08-05 ; release `18.0.0` (2026-03-25).

- [ZUGFeRD/mustangproject](https://github.com/ZUGFeRD/mustangproject) — Java library / CLI to read, write, convert and validate Factur-X/ZUGFeRD and XRechnung. Apache-2.0. **`stargazers_count` = 451**. Last push 2026-08-17 ; release `core-2.25.0` (2026-08-05).

## Corpora

Only publicly licensed, still-living example sets. FNFE ZIP (email gate) and FeRD Infopaket are **not** redistributable corpora here.

- [ConnectingEurope — EN 16931 v1.3.16 examples](https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.16) — release « EN16931 Validation artefacts v1.3.16 » ; body: examples in folder `"examples"` ; EUPL 1.2 ; assets `en16931-cii-1.3.16.zip`, `en16931-ubl-1.3.16.zip`.

- [facturxapi/en16931-oracles](https://github.com/facturxapi/en16931-oracles) — API description « Reproducible EN16931 validation oracles — official CEN 1.3.16 fixtures, SVRL receipts, mutants, and documented blind spots of the official Schematron ». API `NOASSERTION`. **`stargazers_count` = 2** (2026-08-24). Weekly upstream-drift green after adding `vendor/upstream.json`.

- [itplr-kosit/xrechnung-testsuite](https://github.com/itplr-kosit/xrechnung-testsuite) — GitHub mirror of KoSIT ([GitLab](https://projekte.kosit.org/xrechnung/xrechnung-testsuite) HTTP 200). Apache-2.0. Last push 2026-08-14. Release `v2026-01-31`: asset `xrechnung-3.0.2-testsuite-2026-01-31.zip`.

## Related lists

- [causa-prima-ai/awesome-invoicing](https://github.com/causa-prima-ai/awesome-invoicing) — « curated list of invoicing and e-invoicing tools […] EN 16931, XRechnung, ZUGFeRD, Peppol BIS, Factur-X ». File `LICENSE` = CC0 1.0 (API `NOASSERTION`). Last push 2026-07-07 ; **`stargazers_count` = 1**.

- [e-invoice-be/awesome-peppol](https://github.com/e-invoice-be/awesome-peppol) — repo exists (HTTP 200) but **empty**: README = one line `# awesome-peppol` (16 bytes) ; `license`: **null**. Last push 2026-06-12 ; **`stargazers_count` = 0**.

- [morganrcu/awesome-europe](https://github.com/morganrcu/awesome-europe) — OSS « for Europe » (CC0-1.0), *Electronic Invoicing* section. Last push 2026-03-24 ; **`stargazers_count` = 0**.

- [sdras/awesome-actions](https://github.com/sdras/awesome-actions) — GitHub Actions list (CC0-1.0). **`stargazers_count` = 28140**. **Last push 2024-09-01** (> 18 months at 18 Aug 2026). README: **no** Factur-X / ZUGFeRD / e-invoice / EN 16931 occurrence (checked 16/08 ; repo HEAD still 200).

---

## Out of scope

Generic lint / scan Actions (reviewdog/eslint, trivy, golangci-lint, megalinter) are **not** e-invoicing entries — see [`LICENSE-NOTES.md`](LICENSE-NOTES.md).

*Last full check: 2026-08-18, see [CHECKS.md](CHECKS.md).*
