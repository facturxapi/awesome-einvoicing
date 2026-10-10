# CHECKS.md

Last full check: **2026-08-18** (Europe/Paris), `2026-08-18T02:00:06Z`.  
Méthode : `curl -sI -L` (statut final) + `GET` HTML pour H1/citation ; API GitHub `license.spdx_id`, `pushed_at`, `releases/latest`. Sans `GH_TOKEN`.  
ZIP FeRD **non téléchargé**. ZIP FNFE **non ouvert** (gate e-mail).

Le nom `awesome-einvoicing/awesome-einvoicing` est **404** ce run ; search API `q=awesome-einvoicing` → `total_count: 0`. Ce dépôt publié est `facturxapi/awesome-einvoicing`.

« Vit encore ? » = release/tag/commit daté, ou page officielle datée 2026.  
Seuil d’alerte : archived, 404, README d’une ligne, last push > 18 mois.

Preuves brutes : [`_fetch/results-20260818.json`](_fetch/results-20260818.json).

---

## Table

| URL | HTTP | Date fetch | Licence | Vit encore ? | Citation courte |
|---|---|---|---|---|---|
| https://github.com/ConnectingEurope/eInvoicing-EN16931 | 200 | 18 août 2026 | EUPL 1.2 (`LICENSE.txt`) ; API `NOASSERTION` | oui — push 2026-04-14 ; stars 252 ; not archived | description API « Validation artefacts for the European eInvoicing standard EN 16931 » |
| https://raw.githubusercontent.com/ConnectingEurope/eInvoicing-EN16931/master/README.md | 200 | 18 août 2026 | (même dépôt) | oui | « This repository does not contain eInvoicing-EN16931 rules for any CIUS. » (lu 16/08 ; HEAD 200 ce run) |
| https://raw.githubusercontent.com/ConnectingEurope/eInvoicing-EN16931/master/LICENSE.txt | 200 | 18 août 2026 | EUPL 1.2 | — | « Licensed under European Union Public Licence (EUPL) version 1.2. » |
| https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.16 | 200 | 18 août 2026 | EUPL 1.2 (body) | oui — 2026-04-13 | assets `en16931-cii-1.3.16.zip`, `en16931-ubl-1.3.16.zip` |
| https://api.github.com/repos/ConnectingEurope/eInvoicing-EN16931 | 200 | 18 août 2026 | `NOASSERTION` | push 2026-04-14 ; stars 252 | idem description |
| https://fnfe-mpe.org/factur-x/ | 200 | 18 août 2026 | non publiée (gate e-mail) | oui — « Le 4 août 2026 » | « Factur-X 1.09.2 et ZUGFeRD 2.5.2 » ; « Merci de renseigner votre email pour le téléchargement » |
| https://fnfe-mpe.org/ressources/ | 200 | 18 août 2026 | n/a (page) | oui — 30 juin / 4 août 2026 | XP Z12-012 1.4.0 ; schematrons BR-FR-CTC fix03 du 4 août |
| https://www.ferd-net.de/ | 200 | 18 août 2026 | n/a (page) | oui — 04.08.2026 | « ZUGFeRD 2.5.2 veröffentlicht » ; « Eschborn \| Paris, 04.08.2026 » |
| https://www.ferd-net.de/standards/zugferd | 200 | 18 août 2026 | n/a (page) | oui | « kostenfrei verfügbares […] Datenformat » ; base « Norm EN16931 » |
| https://www.ferd-net.de/download-zugferd | 200 | 18 août 2026 | n/a ; ZIP non fetché | oui — Infopaket 04.08.2026 | Direktdownload 27.94 MB (DE) / 28.98 MB (EN) — **octets non téléchargés** |
| https://github.com/fnfempe/France_RFE | 200 | 18 août 2026 | Apache-2.0 | oui — release 2026-08-04 | tag `v1.4.0.03` ; `assets: []` |
| https://raw.githubusercontent.com/fnfempe/France_RFE/main/README.md | 200 | 18 août 2026 | (même dépôt) | oui | « Validation Artefact for France CTC e-invoicing mandate » |
| https://raw.githubusercontent.com/fnfempe/France_RFE/main/LICENSE | 200 | 18 août 2026 | Apache-2.0 | — | texte Apache 2.0 |
| https://api.github.com/repos/fnfempe/France_RFE/releases/latest | 200 | 18 août 2026 | — | oui | `FNFE_RFE_INVOICE_1.4.0.03` ; `published_at` 2026-08-04T17:59:39Z |
| https://www.boutique.afnor.org/fr-fr/norme/xp-z12012/formats-et-profils-des-messages-factures-et-statuts-de-cycle-de-vie-constit/fa301169/601641 | 200 | 18 août 2026 | copyright AFNOR | oui — « juin 2026 » « En vigueur » | « Consultation gratuite » ; corps **non relu** |
| https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees | 200 | 18 août 2026 | n/a (page .gouv) | oui — **modifié le 17/08/2026** (était 12/08 au run 16/08) | « Publié le 30/07/2024, modifié le 17/08/2026 » |
| https://www.impots.gouv.fr/professionnel/questions/dans-le-cadre-de-la-reforme-de-la-facturation-electronique-comment-devrais | 200 | 18 août 2026 | n/a | oui | « À compter du 1er septembre 2026 » ; « septembre 2027 » **absent** |
| https://entreprendre.service-public.fr/actualites/A15683 | 200 | 18 août 2026 | n/a | oui | HEAD 200 (hors fiches README) |
| https://www.getfacturx.com/ | HEAD **405** / GET **200** | 18 août 2026 | n/a | oui | CTA **« 4 utilisations gratuites par jour · Aucune carte requise »** (était 2 au 16/08) |
| https://www.getfacturx.com/validate | 200 | 18 août 2026 | n/a | oui | title « Validateur Factur-X en ligne gratuit » ; H1 « Validateur Factur-X gratuit en ligne » |
| https://facturevalide.fr/ | 200 | 18 août 2026 | n/a | oui | « Gratuit pendant le lancement » ; « Sans limite · Sans carte bancaire » |
| https://facturevalide.fr/valider-facture-electronique.html | 200 | 18 août 2026 | n/a | oui | « 10 vérifications/jour » ; « 31 points de contrôle » |
| https://facturevalide.fr/tarifs | **404** | 18 août 2026 | — | page morte | inchangé |
| https://facturevalide.fr/tarifs.html | **404** | 18 août 2026 | — | page morte | inchangé |
| https://thelawin.dev/ | 200 | 18 août 2026 | n/a | oui | H1 « The E-Invoicing Engine » ; libellés Factur-X 1.0.8 / ZUGFeRD 2.4 |
| https://thelawin.dev/pricing | 200 | 18 août 2026 | n/a | oui | Sandbox €0 ; Starter €9.50/month ; Pro €24.50/month ; « Beta pricing: 50% off » |
| https://thelawin.dev/fr/factur-x-validator | 200 | 18 août 2026 | n/a | oui | H1 « Factur-X Validator » |
| https://www.b2brouter.net/fr/factur-x-validator/ | 200 | 18 août 2026 | n/a | oui | title « […] conforme et gratuit » (leur title) |
| https://www.b2brouter.net/fr/tarifs/ | 200 | 18 août 2026 | n/a | oui | Basic 0 eur / à vie ; Professional 110 eur / an + TVA ; Business 300 eur / an + TVA |
| https://e-rechnung-api.fly.dev/ | 200 | 10 octobre 2026 | n/a | oui | H1 « ZUGFeRD & Factur-X API » ; Test 0€, Prepaid 10€ / 100 Dok. |
| https://e-rechnung-api.fly.dev/validator | 200 | 10 octobre 2026 | n/a | oui | title « Kostenloser ZUGFeRD & XRechnung Validator (EN 16931) » |
| https://formatx.fr/ | 200 | 18 août 2026 | n/a | oui | schema.org `"price":"0"` EUR |
| https://formatx.fr/api-docs | 200 | 18 août 2026 | n/a | oui | quotas v2 Free 10 / Pro 100 / Business 500 factures/mois (sans €) |
| https://facturx-validator.fr/ | 200 | 18 août 2026 | n/a ; « open source » sans lien de dépôt | oui | H1 « Vérifiez vos factures Factur-X gratuitement » ; « Outil gratuit et open source » |
| https://facturx-validator.fr/verifier | 200 | 18 août 2026 | n/a | oui | « Fichier PDF uniquement (max. 10 Mo) » ; profils Minimum, Basic, EN16931, Extended |
| https://facturxapi.com/ | 200 | 18 août 2026 | n/a | oui | H1 « Ajoutez Factur-X à votre logiciel sans remplacer votre outil de facturation. » Claims = `[CLAIM À PROUVER]`. Prix `[non-mesure]`. |
| https://www.mustangproject.org/ | 200 | 18 août 2026 | Apache-2.0 (dépôt) | oui — 05.08.2026 | « Mustangproject 2.25.0 was released on 05.08.2026 » ; support ZUGFeRD 2.5.2 |
| https://www.mustangproject.org/commandline/ | 200 | 18 août 2026 | — | oui | section Validate ; `Mustang-CLI-2.25.0.jar` |
| https://www.mustangproject.org/use/ | 200 | 18 août 2026 | — | oui | HEAD 200 |
| https://github.com/horstoeko/zugferd | 200 | 18 août 2026 | MIT | oui — push 2026-08-04 ; stars 432 | description « ZUGFeRD/XRechnung/Factur-X Library » |
| https://api.github.com/repos/horstoeko/zugferd | 200 | 18 août 2026 | MIT | oui | idem |
| https://github.com/ZUGFeRD/mustangproject | 200 | 18 août 2026 | Apache-2.0 | oui — push **2026-08-17** ; stars **451** (450 au 16/08) | description API Factur-X/ZUGFeRD |
| https://github.com/akretion/factur-x | 200 | 18 août 2026 | API `NOASSERTION` ; `LICENSE.txt` BSD 3-clause | oui — push 2026-08-08 ; stars 303 | |
| https://raw.githubusercontent.com/akretion/factur-x/master/LICENSE | **404** | 18 août 2026 | — | — | vrai fichier = `LICENSE.txt` |
| https://raw.githubusercontent.com/akretion/factur-x/master/LICENSE.txt | 200 | 18 août 2026 | BSD 3-clause | — | |
| https://github.com/pretix/python-drafthorse | 200 | 18 août 2026 | Apache-2.0 | oui — push 2026-06-02 ; stars 176 | **pas de release** (16/08 `releases/latest` 404 ; non re-appelé ce run) |
| https://github.com/stephanstapel/ZUGFeRD-csharp | 200 | 18 août 2026 | Apache-2.0 | oui — push 2026-08-05 ; stars 392 | |
| https://raw.githubusercontent.com/stephanstapel/ZUGFeRD-csharp/master/LICENSE | **404** | 18 août 2026 | — | — | vrai fichier = `LICENSE.txt` |
| https://github.com/hernaninverso/validate-einvoice-action | 200 | 18 août 2026 | Apache-2.0 | oui — push 2026-05-25 ; stars 0 | description API « backed by eleata.io » |
| https://github.com/invoicenavigator/validate-invoice | 200 | 18 août 2026 | MIT | oui — push 2026-03-02 ; stars 0 | **pas de release** (16/08) |
| https://github.com/attestwire/validate-einvoice-action | 200 | 18 août 2026 | MIT | oui — créé 2026-08-16 ; stars 0 | description API « Runs locally by default » |
| https://github.com/marketplace/actions/validate-e-invoice-en-16931 | 200 | 18 août 2026 | MIT (repo) | oui | fiche Marketplace attestwire |
| https://github.com/marketplace?type=actions&query=factur-x | 200 | 18 août 2026 | — | — | **« 1 result »** |
| https://github.com/marketplace?type=actions&query=zugferd | 200 | 18 août 2026 | — | — | **« 0 results »** / « No results » |
| https://github.com/awesome-einvoicing/awesome-einvoicing | **404** | 18 août 2026 | — | **inexistant** | pas une awesome GitHub |
| https://api.github.com/search/repositories?q=awesome-einvoicing | 200 | 18 août 2026 | — | — | `{"total_count":0}` |
| https://api.github.com/repos/awesome-einvoicing/awesome-einvoicing | **404** | 18 août 2026 | — | inexistant | — |
| https://github.com/sdras/awesome-actions | 200 | 18 août 2026 | CC0-1.0 | **stale** — last push **2024-09-01** ; stars **28140** (28130 au 16/08) | |
| https://github.com/causa-prima-ai/awesome-invoicing | 200 | 18 août 2026 | API `NOASSERTION` | oui — push 2026-07-07 ; stars 1 | |
| https://github.com/morganrcu/awesome-europe | 200 | 18 août 2026 | CC0-1.0 | oui — push 2026-03-24 ; stars 0 | |
| https://github.com/e-invoice-be/awesome-peppol | 200 | 18 août 2026 | **null** | **vide** — README 16 octets `# awesome-peppol` | stars 0 |
| https://raw.githubusercontent.com/e-invoice-be/awesome-peppol/main/README.md | 200 | 18 août 2026 | null | vide | `# awesome-peppol` |
| https://github.com/itplr-kosit/xrechnung-testsuite | 200 | 18 août 2026 | Apache-2.0 | oui — push 2026-08-14 ; stars 96 | |
| https://github.com/itplr-kosit/xrechnung-testsuite/releases/tag/v2026-01-31 | 200 | 18 août 2026 | Apache-2.0 | oui | |
| https://projekte.kosit.org/xrechnung/xrechnung-testsuite | 200 | 18 août 2026 | Apache (page GitLab) | oui | H1 `xrechnung-testsuite` |
| https://raw.githubusercontent.com/itplr-kosit/xrechnung-testsuite/master/LICENSE | 200 | 18 août 2026 | Apache-2.0 | — | |
| https://github.com/facturxapi/validate-einvoice | 200 | 18 août 2026 | API `NOASSERTION` | oui — push 2026-08-18T01:47:17Z ; stars **0** | description API « official ConnectingEurope EN16931 1.3.16 XSLT » ; tag `v1` → `8457406078fee1807c6e6604852b1764fe537c62` |
| https://api.github.com/repos/facturxapi/validate-einvoice | 200 | 18 août 2026 | `NOASSERTION` | oui | idem |
| https://api.github.com/repos/facturxapi/validate-einvoice/git/refs/tags/v1 | 200 | 18 août 2026 | — | oui | object.sha `8457406…` |
| https://github.com/facturxapi/validate-einvoice/actions/runs/32089460503 | 200 | 18 août 2026 | — | — | page run publique (non citée dans le README final — neutralité) |
| https://github.com/facturxapi/en16931-oracles | 200 | 18 août 2026 | API `NOASSERTION` | oui — push 2026-08-17T23:39:13Z ; stars **0** | description API « Reproducible EN16931 validation oracles » |
| https://api.github.com/repos/facturxapi/en16931-oracles | 200 | 18 août 2026 | `NOASSERTION` | oui | idem |
| https://github.com/facturxapi/en16931-oracles/actions/runs/32081271235 | 200 | 18 août 2026 | — | — | page run publique (non citée dans le README final) |
| https://www.itb.ec.europa.eu/invoice/upload | 200 | 18 août 2026 | n/a (Commission) | oui | H1 « eInvoice Validator » ; options `cii`/`ubl`/`credit` « release 1.3.16 » |
| https://www.itb.ec.europa.eu/vitb/rest/invoice/api/validate | HEAD **405** | 18 août 2026 | n/a | endpoint POST (HEAD refusé) | attendu pour une API REST ; non un 404 |
| https://github.com/reviewdog/action-eslint | 200 | 18 août 2026 | MIT | oui — push 2026-07-24 ; stars 260 | **exclu README** |
| https://github.com/aquasecurity/trivy-action | 200 | 18 août 2026 | Apache-2.0 | oui — push 2026-08-14 ; stars 1396 | **exclu README** |
| https://github.com/golangci/golangci-lint-action | 200 | 18 août 2026 | MIT | oui — push 2026-08-11 ; stars 1444 | **exclu README** |
| https://github.com/oxsecurity/megalinter | 200 | 18 août 2026 | AGPL-3.0 | oui — push 2026-08-17 ; stars **2558** (2557 au 16/08) | **exclu README** |

---

## HTTP ≠ 200 (ce run)

| URL | HTTP | Note |
|---|---|---|
| https://github.com/awesome-einvoicing/awesome-einvoicing | 404 | liste absente |
| https://api.github.com/repos/awesome-einvoicing/awesome-einvoicing | 404 | idem |
| https://facturevalide.fr/tarifs | 404 | pas une fiche README |
| https://facturevalide.fr/tarifs.html | 404 | idem |
| https://raw.githubusercontent.com/akretion/factur-x/master/LICENSE | 404 | vrai chemin `LICENSE.txt` |
| https://raw.githubusercontent.com/stephanstapel/ZUGFeRD-csharp/master/LICENSE | 404 | vrai chemin `LICENSE.txt` |
| https://www.getfacturx.com/ | HEAD 405 / GET 200 | exception de méthode ; GET utilisé pour la citation |
| https://www.itb.ec.europa.eu/vitb/rest/invoice/api/validate | HEAD 405 | POST-only |

---

## Deltas vs 16 août 2026

| Entrée | 16/08 | 18/08 |
|---|---|---|
| Get FacturX CTA | 2 utilisations / jour | **4 utilisations / jour** |
| Get FacturX home HEAD | 200 | **405** (GET 200) |
| DGFiP plateformes | modifié le 12/08/2026 | **modifié le 17/08/2026** |
| ZUGFeRD/mustangproject | stars 450 ; push 2026-08-11 | stars **451** ; push **2026-08-17** |
| sdras/awesome-actions | stars 28130 | stars **28140** |
| oxsecurity/megalinter | stars 2557 | stars **2558** (exclu README) |
| facturxapi/validate-einvoice | absent CHECKS | public ; stars 0 ; tag `v1` = `8457406…` |
| facturxapi/en16931-oracles | absent CHECKS | public ; stars 0 |
| ITB upload | absent CHECKS | GET 200 ; release 1.3.16 affichée |

Aucun dépôt de la liste principale n’est `archived`.

---

## « Vit encore ? » — alertes

| Entrée | Alerte |
|---|---|
| `awesome-einvoicing/awesome-einvoicing` | 404 |
| `e-invoice-be/awesome-peppol` | README d’une ligne |
| `sdras/awesome-actions` | last push 2024-09-01 (> 18 mois) |
| `invoicenavigator/validate-invoice` | 0 stars, 0 release |
| `hernaninverso` / `attestwire` / `facturxapi/*` | 0 stars |
| Pack FNFE | ZIP derrière e-mail |
| Pack FeRD | ZIP non mesuré |

---

## Licences (synthèse API / fichier)

| SPDX / constat | Entrées |
|---|---|
| EUPL 1.2 (fichier ; API NOASSERTION) | ConnectingEurope/eInvoicing-EN16931 ; facturxapi/validate-einvoice (NOTICE) |
| Apache-2.0 | France_RFE, mustangproject, python-drafthorse, ZUGFeRD-csharp, xrechnung-testsuite, hernaninverso, trivy-action |
| MIT | horstoeko/zugferd, invoicenavigator, attestwire, reviewdog/action-eslint, golangci-lint-action |
| CC0-1.0 | sdras/awesome-actions, morganrcu/awesome-europe ; **texte de cette liste** |
| CC0 1.0 (fichier ; API NOASSERTION) | causa-prima-ai/awesome-invoicing |
| BSD 3-clause (fichier ; API NOASSERTION) | akretion/factur-x |
| AGPL-3.0 | oxsecurity/megalinter (exclu README) |
| `licence: null` | e-invoice-be/awesome-peppol |
| n/a | sites validateurs, FNFE gate, FeRD Infopaket, boutique AFNOR, pages .gouv, ITB |

---

*Fin des checks 18 août 2026.*
