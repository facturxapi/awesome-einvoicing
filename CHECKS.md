# CHECKS.md

Last full check: **2026-10-11** (Europe/Paris), `2026-10-11T17:29:38Z`.\
Méthode : `curl -sI -L` (statut final) puis `GET` (User-Agent navigateur) pour statut, title/H1 et citations ; API GitHub en lecture (`gh api`) : `stargazers_count`, `pushed_at`, `license.spdx_id`, `releases/latest`, description, redirections.\
ZIP FeRD **non téléchargé**. ZIP FNFE **non ouvert** (gate e-mail).

Le nom `awesome-einvoicing/awesome-einvoicing` est **404** ce run ; search API `q=awesome-einvoicing` → `total_count: 1` (`facturxapi/awesome-einvoicing`, ce dépôt).

« Vit encore ? » = release/tag/commit daté, ou page officielle datée 2026.  
Seuil d’alerte : archived, 404, README d’une ligne, last push > 18 mois.

Relevé précédent : 18 août 2026 (voir « Deltas vs 18 août 2026 »).

Relevé partiel **2026-10-18** (`2026-10-18T11:01:53Z`, lignes `facturxapi` à `2026-10-18T14:04:35Z`) : lignes touchées par la publication EN16931 1.3.17 seulement (voir « Deltas vs 11 oct. 2026 »).

---

## Table

| URL | HTTP | Date fetch | Licence | Vit encore ? | Citation courte |
|---|---|---|---|---|---|
| https://github.com/ConnectingEurope/eInvoicing-EN16931 | 200 | 18 oct. 2026 | EUPL 1.2 (`LICENSE.txt`) ; API `NOASSERTION` | oui — push 2026-10-12 ; stars 261 ; not archived | description API « Validation artefacts for the European eInvoicing standard EN 16931 » ; `releases/latest` = `validation-1.3.17` (2026-10-12T12:28:45Z) |
| https://raw.githubusercontent.com/ConnectingEurope/eInvoicing-EN16931/master/README.md | 200 | 18 oct. 2026 | (même dépôt) | oui | « This repository does not contain eInvoicing-EN16931 rules for any CIUS. » |
| https://raw.githubusercontent.com/ConnectingEurope/eInvoicing-EN16931/master/LICENSE.txt | 200 | 18 oct. 2026 | EUPL 1.2 | — | « Licensed under European Union Public Licence (EUPL) version 1.2. » |
| https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.17 | 200 | 18 oct. 2026 | EUPL 1.2 (body) | oui — 2026-10-12 ; `releases/latest` | assets `en16931-cii-1.3.17.zip`, `en16931-ubl-1.3.17.zip` ; notes : #499 à #525, dont #519 (renommage IGIC `BR-AF` / IPSI `BR-AG` ; mesuré sur les XSLT : IGIC → `BR-IP` en CII mais `BR-IG` en UBL, IPSI l'inverse) |
| https://github.com/ConnectingEurope/eInvoicing-EN16931/releases/tag/validation-1.3.16 | 200 | 18 oct. 2026 | EUPL 1.2 (body) | oui — 2026-04-13 ; plus `releases/latest` | assets `en16931-cii-1.3.16.zip`, `en16931-ubl-1.3.16.zip` |
| https://api.github.com/repos/ConnectingEurope/eInvoicing-EN16931 | 200 | 18 oct. 2026 | `NOASSERTION` | push 2026-10-12 ; stars 261 | idem description |
| https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108974/Registry+of+supporting+artefacts+to+implement+EN16931 | 200 | 18 oct. 2026 | n/a (page Commission) | oui | « (latest versions) – EN16931 Validation artefacts for UBL 2.1 - version 1.3.17 – EN16931 Validation artefacts for CII 16b - version 1.3.17 » ; « 15 /11/26 \| Published: 12/10/26 » |
| https://fnfe-mpe.org/factur-x/ | 200 | 11 oct. 2026 | non publiée (gate e-mail) | oui — « Le 4 août 2026 » | « Factur-X 1.09.2 et ZUGFeRD 2.5.2 » ; « Merci de renseigner votre email pour le téléchargement » |
| https://fnfe-mpe.org/ressources/ | 200 | 11 oct. 2026 | n/a (page) | oui — 30 juin / 4 septembre 2026 | XP Z12-012 1.4.0 ; « Version 1.4.0 des schematrons » (fix04 du 4 septembre) ; fichier `2026_09_04_FNFE_SCHEMATRONS_FR_CTC_V1.4.0.04.zip` |
| https://www.ferd-net.de/ | 200 | 11 oct. 2026 | n/a (page) | oui — 04.08.2026 | « ZUGFeRD 2.5.2 veröffentlicht » ; « Eschborn \| Paris, 04.08.2026 » |
| https://www.ferd-net.de/standards/zugferd | 200 | 11 oct. 2026 | n/a (page) | oui | « kostenfrei verfügbares […] Datenformat » ; base « Norm EN16931 » |
| https://www.ferd-net.de/download-zugferd | 200 | 11 oct. 2026 | n/a ; ZIP non fetché | oui — Infopaket 04.08.2026 | Direktdownload 27.94 MB (DE) / 28.98 MB (EN) — **octets non téléchargés** |
| https://github.com/fnfempe/France_RFE | 200 | 11 oct. 2026 | Apache-2.0 | oui — release 2026-09-04 ; push 2026-09-04 | release `v1.4.0.04` ; aucun asset déposé (archives source seulement) |
| https://raw.githubusercontent.com/fnfempe/France_RFE/main/README.md | 200 | 11 oct. 2026 | (même dépôt) | oui | « Validation Artefact for France CTC e-invoicing mandate » |
| https://raw.githubusercontent.com/fnfempe/France_RFE/main/LICENSE | 200 | 11 oct. 2026 | Apache-2.0 | — | texte Apache 2.0 |
| https://api.github.com/repos/fnfempe/France_RFE/releases/latest | 200 | 11 oct. 2026 | — | oui | `FNFE_RFE_INVOICE_1.4.0.04` ; `published_at` 2026-09-04T22:42:01Z ; notes « V1.4.0.04 - Fix04 - corrections (made also on Schematrons « Warning » when present): » |
| https://www.boutique.afnor.org/fr-fr/norme/xp-z12012/formats-et-profils-des-messages-factures-et-statuts-de-cycle-de-vie-constit/fa301169/601641 | 200 | 11 oct. 2026 | copyright AFNOR | oui — « juin 2026 » « En vigueur » | « Consultation gratuite » ; corps **non relu** |
| https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees | 200 | 11 oct. 2026 | n/a (page .gouv) | oui — **modifié le 22/09/2026** (17/08 au run 18/08) | « Publié le 30/07/2024, modifié le 22/09/2026 » |
| https://www.impots.gouv.fr/professionnel/questions/dans-le-cadre-de-la-reforme-de-la-facturation-electronique-comment-devrais | 200 | 11 oct. 2026 | n/a | oui | « À compter du 1er septembre 2026 » ; « septembre 2027 » **absent** |
| https://entreprendre.service-public.fr/actualites/A15683 | 301 → 200 | 11 oct. 2026 | n/a | oui | redirige vers `entreprendre.service-public.gouv.fr` (hors fiches README) |
| https://www.getfacturx.com/ | 200 (HEAD et GET) | 11 oct. 2026 | n/a | oui | H1 « Créez, envoyez et recevez vos factures Factur-X, sans ERP » ; CTA « 4 utilisations gratuites par jour » **absent** ce run |
| https://www.getfacturx.com/validate | 200 | 11 oct. 2026 | n/a | oui | title « Factur-X Validator : validateur Factur-X gratuit en ligne » ; H1 « Validateur Factur-X gratuit en ligne » |
| https://facturevalide.fr/ | 200 | 11 oct. 2026 | n/a | oui | « Gratuit pendant le lancement » ; « Sans limite · Sans carte bancaire » |
| https://facturevalide.fr/valider-facture-electronique.html | 200 | 11 oct. 2026 | n/a | oui | « 10 vérifications/jour » (meta description) ; « 31 points de contrôle » |
| https://facturevalide.fr/tarifs | **404** | 11 oct. 2026 | — | page morte | inchangé |
| https://facturevalide.fr/tarifs.html | **404** | 11 oct. 2026 | — | page morte | inchangé |
| https://thelawin.dev/ | 200 | 11 oct. 2026 | n/a | oui | H1 « The E-Invoicing Engine » ; libellés Factur-X 1.0.8 / ZUGFeRD 2.4 |
| https://thelawin.dev/pricing | 200 | 11 oct. 2026 | n/a | oui | Sandbox €0 ; Starter €9.50/month ; Pro €24.50/month ; « Beta pricing: 50% off » |
| https://thelawin.dev/fr/factur-x-validator | 200 | 11 oct. 2026 | n/a | oui | H1 « Factur-X Validator » |
| https://xmlvalid.com/schematron-validator | 200 | 21 oct. 2026 | n/a | oui | H1 « Schematron validator for e-invoices » ; « EN 16931 1.3.17 » ; « Nothing is uploaded » ; entrée proposée par son auteur (#20) |
| https://xmlvalid.com/pricing | 200 | 21 oct. 2026 | n/a | oui | Free « $0 forever » ; Pro « $290 per year » |
| https://annehmbar.com/ | 200 | 24 oct. 2026 | n/a | oui — config v2026-08-31 | H1 « XRechnung und ZUGFeRD prüfen: Wird Ihre Rechnung angenommen? » ; marque « Annehmbar » ; « Regeländerungs-Alarm 0 € bis 31.12.2026, danach 19 € / Monat » ; `/api/rules` → `"config": "v2026-08-31"` ; ancienne adresse `xrechnung.jestr.ai` → 301 ; entrée proposée par son opérateur (#7) |
| https://www.b2brouter.net/fr/factur-x-validator/ | 200 | 11 oct. 2026 | n/a | oui | title « […] conforme et gratuit » (leur title) |
| https://www.b2brouter.net/fr/tarifs/ | 200 | 11 oct. 2026 | n/a | oui | Basic 0 eur / à vie ; Professional 110 eur / an + TVA ; Business 300 eur / an + TVA |
| https://checkxrechnung.com/ | 200 (GET) | 28 oct. 2026 | n/a (service web) | oui | description JSON-LD « Kostenloser XRechnung und ZUGFeRD Validator mit offiziellen KoSIT-Regeln » ; H1 « XRechnung & ZUGFeRD prüfen – kostenlos » ; `POST /v1/validate` ; « kostenlos (50 pro IP und UTC-Tag) » ; « API / Batch ab €79/Monat » = liste d’attente (« Batch und höheres Volumen bleiben eine Warteliste ab €79/Monat. ») ; entrée proposée par son opérateur (#27) |
| https://coretool.de/e-rechnung-pruefen | 200 | 28 oct. 2026 | n/a | oui | « Kostenlos · ohne Anmeldung · Datei wird nicht gespeichert » ; « 3 Rechnungen pro Monat gratis » ; « Solo-Tarif 9 €/Monat inkl. MwSt. » ; entrée proposée par son opérateur (#28) |
| https://coretool.de/e-rechnung-api | 200 | 28 oct. 2026 | n/a | oui | title « E-Rechnungs-API für Entwickler – XRechnung & ZUGFeRD per API prüfen » ; « 3 Prüfungen kostenlos je Konto » |
| https://e-rechnung-api.fly.dev/ | HEAD **405** / GET **200** | 11 oct. 2026 | n/a | oui | H1 « ZUGFeRD & Factur-X API für Entwickler » ; Test 0€, Prepaid 10€ / 100 Dok. |
| https://e-rechnung-api.fly.dev/validator | HEAD **405** / GET **200** | 11 oct. 2026 | n/a | oui | title « Kostenloser ZUGFeRD & XRechnung Validator (EN 16931) \| E-Rechnung online prüfen » |
| https://factusur.com/ | 200 (HEAD et GET) | 26 oct. 2026 | n/a | oui | title « Factur-X gratuit : convertir une facture PDF en Factur-X » ; H1 « Transformez votre facture PDF en Factur-X, en 2 minutes » ; « Factusur n'est pas une plateforme agréée (PA) et ne transmet pas vos factures » ; entrée proposée par son éditeur (#25) |
| https://factusur.com/verifier-factur-x | 200 (HEAD et GET) | 26 oct. 2026 | n/a | oui | title « Vérifier un Factur-X gratuitement — Factusur » ; « Gratuit, sans inscription » ; « PDF uniquement · 10 Mo max. » |
| https://factusur.com/tarifs | 200 (HEAD et GET) | 28 oct. 2026 | n/a | oui | 5 paliers : Gratuit « 0 € » « 3 conversions / mois » ; Starter « 3,90 € /mois » « 10 conversions / mois » ; Essentiel « 6,90 € /mois » « 30 conversions / mois » ; Pro « 13,90 € /mois » « 100 conversions / mois » ; Business « 26,90 € /mois » « 500 conversions / mois » ; « Tous les prix sont indiqués en euros TTC (TVA 20 % incluse). » |
| https://formatx.fr/ | 200 | 11 oct. 2026 | n/a | oui | title « FormatX - Convertir PDF en Factur-X gratuitement \| Facture électronique conforme » ; schema.org `"price":"0"` EUR |
| https://formatx.fr/api-docs | 200 | 11 oct. 2026 | n/a | oui | « Aucun quota mensuel, aucune facturation. » ; « 60 requêtes/minute » ; quotas Free 10 / Pro 100 / Business 500 **absents** |
| https://facturx-validator.fr/ | 200 | 11 oct. 2026 | n/a ; « open source » sans lien de dépôt | oui | H1 « Vérifiez vos factures Factur-X gratuitement » ; « Outil gratuit et open source » |
| https://facturx-validator.fr/verifier | 200 | 11 oct. 2026 | n/a | oui | « Fichier PDF uniquement (max. 10 Mo) » ; profils Minimum, Basic, EN16931, Extended |
| https://invoicein.peculiar.systems/ | 200 | 11 oct. 2026 | service : non publiée ; exemples MIT (github.com/peculiar-systems/invoicein-examples) | oui — page « Beta pricing » | « Every e-invoice you receive, as one JSON. » ; Free €0 100 invoices ; Starter €29 ; Growth €99 ; Scale €399 |
| https://invoicein-api.peculiar.systems/docs | HEAD **405** / GET **200** | 11 oct. 2026 | n/a | oui | référence API (lien README) |
| https://valinvo.bmk-hub.com/ | 200 | 29 oct. 2026 | n/a (service web) | oui | H1 « XRechnung and Peppol e-invoices from one JSON call » ; « The online validator on this page is free and needs no account or API key. » ; Free « 2 invoices / day to try the API, no key needed » ; Starter « €29 / month » ; entrée proposée par son opérateur (#31) |
| https://www.mustangproject.org/ | 200 | 11 oct. 2026 | Apache-2.0 (dépôt) | oui — 25.08.2026 | « Mustangproject 2.26.0 was released on 25.08.2026 » ; support ZUGFeRD 2.5.2 (note 2.25.0) |
| https://www.mustangproject.org/commandline/ | 200 | 11 oct. 2026 | — | oui | section Validate ; `Mustang-CLI-2.26.0.jar` |
| https://www.mustangproject.org/use/ | 200 | 11 oct. 2026 | — | oui | HEAD 200 |
| https://github.com/horstoeko/zugferd | 200 | 11 oct. 2026 | MIT | oui — push 2026-10-02 ; stars 437 ; release `v1.0.132` (2026-08-30) | description « ZUGFeRD/XRechnung/Factur-X Library » ; README names `horstoeko/invoicesuite` as « The official successor » |
| https://api.github.com/repos/horstoeko/zugferd | 200 | 11 oct. 2026 | MIT | oui | idem |
| https://github.com/kadour-ia/Facturx-lire | 200 | 11 oct. 2026 | MIT (`LICENSE`, ajouté le 11/10 ; API `license.spdx_id` = `MIT`) | oui — push 2026-10-11 ; stars 0 ; not archived ; pas de release (`releases/latest` 404) | description API « Lire en clair une facture électronique reçue (Factur-X, ZUGFeRD, CII, UBL) — gratuit, 100% local. Réforme 2026. » ; README « Transparence » : écrit et maintenu par un agent d'IA autonome (déclaré) |
| https://github.com/ZUGFeRD/mustangproject | 200 | 11 oct. 2026 | Apache-2.0 | oui — push **2026-10-10** ; stars **480** ; release `core-2.26.0` (2026-08-25) | description API Factur-X/ZUGFeRD |
| https://github.com/akretion/factur-x | 200 | 11 oct. 2026 | API `NOASSERTION` ; `LICENSE.txt` BSD 3-clause | oui — push 2026-10-09 ; stars 310 ; release `7.5` (2026-10-09) |  |
| https://raw.githubusercontent.com/akretion/factur-x/master/LICENSE | **404** | 11 oct. 2026 | — | — | vrai fichier = `LICENSE.txt` |
| https://raw.githubusercontent.com/akretion/factur-x/master/LICENSE.txt | 200 | 11 oct. 2026 | BSD 3-clause | — |  |
| https://github.com/pretix/python-drafthorse | 200 | 11 oct. 2026 | Apache-2.0 | oui — push 2026-06-02 ; stars 179 | description API « Pure-python ZUGFeRD implementation » ; **pas de release** (`releases/latest` 404) |
| https://github.com/stephanstapel/ZUGFeRD-csharp | 200 | 11 oct. 2026 | Apache-2.0 | oui — push 2026-10-09 ; stars 395 ; release `18.0.1` (2026-10-09) | README « My maintenance of this project will end on November 30, 2026. » ; FactoorSharp « the commercial successor » |
| https://raw.githubusercontent.com/stephanstapel/ZUGFeRD-csharp/master/LICENSE | **404** | 11 oct. 2026 | — | — | vrai fichier = `LICENSE.txt` |
| https://github.com/phax/phive | 200 | 18 oct. 2026 | Apache-2.0 | oui — push 2026-10-08 ; stars 77 ; release `v12.2.0` (2026-09-28) ; not archived | description API « Generic business document validation engine » ; README : règles dans un dépôt séparé |
| https://github.com/phax/phive-rules | 200 | 18 oct. 2026 | API `NOASSERTION` ; README « The Java code in this project is licensed under the Apache 2 license. » | oui — push 2026-10-17 ; stars 52 ; release `v4.6.3` (2026-09-30) ; not archived | modules `phive-rules-en16931`, `phive-rules-xrechnung`, `phive-rules-zugferd` ; artefacts de validation sous licences propres (`NOTICE` par module) |
| https://github.com/phax/phorm | 200 | 18 oct. 2026 | Apache-2.0 | oui — push 2026-10-18 ; stars 32 ; release `v2.2.11` (2026-09-30) ; not archived | description API « Phorm - Business Document Validation Service » ; README « accessible by API only » |
| https://github.com/phax/en16931-cii2ubl | 200 | 18 oct. 2026 | Apache-2.0 | oui — push 2026-10-08 ; stars 47 ; release `v4.0.2` (2026-10-07) | CII D16B → UBL 2.1 ; CII D25A → UBL 2.5 |
| https://github.com/phax/en16931-purifier | 200 | 18 oct. 2026 | Apache-2.0 | oui — push 2026-10-08 ; stars 1 ; release `v1.1.0` (2026-09-06) | « this project is not a converter » |
| https://github.com/phax/en16931-ubl2cii | 200 | 18 oct. 2026 | Apache-2.0 | oui — push 2026-10-08 ; stars 10 ; release `v3.0.1` (2026-10-07) | UBL 2.1 → CII D16B ; UBL 2.5 → CII D25A |
| https://github.com/phax/kaltblut | 200 | 18 oct. 2026 | Apache-2.0 | oui — push 2026-10-18 ; stars 6 ; release `v0.9.5` (2026-08-09) ; not archived | description API « Java library helping you to handle ZUGFeRD invoices » ; PDF/A-3 via veraPDF ; XML-side rules hors périmètre |
| https://github.com/phax/ph-cii | 200 | 18 oct. 2026 | Apache-2.0 | oui — push 2026-10-08 ; stars 15 ; release `v4.1.3` (2026-09-22) | D16A.1, D16B, D22B, D25A |
| https://github.com/phax/ph-redact | 200 | 18 oct. 2026 | Apache-2.0 | oui — push 2026-10-09 ; stars 3 ; release `v1.1.0` (2026-09-08) | description API « Simple eInvoice Anonymizer » ; anonymiseur XSLT UBL / CII |
| https://github.com/phax/ph-ubl | 200 | 18 oct. 2026 | Apache-2.0 | oui — push 2026-10-17 ; stars 141 ; release `v10.2.1` (2026-08-27) | UBL 2.0 à 2.5 |
| https://github.com/hernaninverso/validate-einvoice-action | 301 → 200 | 11 oct. 2026 | Apache-2.0 | oui — push 2026-05-25 ; stars 0 ; release `v1` (2026-05-25) | redirige vers `eleata/validate-einvoice-action` (API `full_name`) ; description API « backed by eleata.io » ; `action.yml` default `api-base` `https://api.eleata.io` |
| https://github.com/invoicenavigator/validate-invoice | 200 | 11 oct. 2026 | MIT | oui — push 2026-03-02 ; stars 0 | **pas de release** (`releases/latest` 404) |
| https://github.com/wsystemdev/einvoice-validate-action | 200 | 28 oct. 2026 | MIT | oui — dépôt créé le 2026-10-26 (`created_at` 2026-10-26T10:50:52Z), push 2026-10-26 ; stars 0 ; release `v1.0.0` (2026-10-26) | description API « validate UBL, CII and ZUGFeRD/Factur-X e-invoices against EN 16931 and XRechnung rules in CI » ; `action.yml` default `api-url` `https://api.wsystem.dev` ; `api-key` « free key: 500 units a month, no card » ; « Without one, each runner IP gets 20 free calls a day. » ; entrée proposée par son éditeur (#26) |
| https://github.com/attestwire/validate-einvoice-action | 200 | 11 oct. 2026 | MIT | oui — push 2026-10-04 ; stars 0 ; release `v1.10.0` (2026-10-04) | description API « Runs locally by default » ; release « v1.10.0: engine 0.14.1 » |
| https://github.com/marketplace/actions/validate-e-invoice-en-16931 | 200 | 11 oct. 2026 | MIT (repo) | oui | fiche Marketplace attestwire |
| https://github.com/marketplace/actions/validate-en16931-e-invoice | 200 | 18 oct. 2026 | EUPL 1.2 (repo ; API `NOASSERTION`) | oui | fiche Marketplace `facturxapi/validate-einvoice` ; latest release affichée `v1.2.0` (`v1.1.2` au 11/10) |
| https://github.com/attestwire/en16931 | 200 | 11 oct. 2026 | MIT (API `license.spdx_id`) | oui — push 2026-10-04 ; release `v0.14.1` (`published_at` 2026-10-06) ; stars 1 ; not archived | notes de release « Released 2026-10-04 » |
| https://github.com/marketplace?type=actions&query=factur-x | 200 | 11 oct. 2026 | — | — | **« 5 results »** : `validate-en16931-e-invoice`, `validate-e-invoice-en-16931`, `prufix`, `beliq-e-invoice-validate`, `invowerk-api` (avant la release `v1.1.2` le même jour : « 4 results », sans `validate-en16931-e-invoice`) |
| https://github.com/marketplace?type=actions&query=zugferd | 200 | 11 oct. 2026 | — | — | **« 3 results »** : `validate-en16931-e-invoice`, `beliq-e-invoice-validate`, `invowerk-api` (avant la release `v1.1.2` le même jour : « 2 results ») |
| https://github.com/marketplace?type=actions&query=en16931 | 200 | 11 oct. 2026 | — | — | **« 1 result »** : `validate-en16931-e-invoice` |
| https://github.com/awesome-einvoicing/awesome-einvoicing | **404** | 11 oct. 2026 | — | **inexistant** | pas une awesome GitHub |
| https://api.github.com/search/repositories?q=awesome-einvoicing | 200 | 11 oct. 2026 | — | — | `total_count: 1` (`facturxapi/awesome-einvoicing`) |
| https://api.github.com/repos/awesome-einvoicing/awesome-einvoicing | **404** | 11 oct. 2026 | — | inexistant | — |
| https://github.com/sdras/awesome-actions | 200 | 11 oct. 2026 | CC0-1.0 | **stale** — last push **2024-09-01** ; stars **28306** | README : aucune occurrence Factur-X / ZUGFeRD / e-invoice / EN 16931 |
| https://github.com/causa-prima-ai/awesome-invoicing | 200 | 11 oct. 2026 | API `NOASSERTION` | oui — push 2026-07-07 ; stars 1 |  |
| https://github.com/morganrcu/awesome-europe | 200 | 11 oct. 2026 | CC0-1.0 | oui — push 2026-03-24 ; stars 0 |  |
| https://github.com/e-invoice-be/awesome-peppol | 200 | 11 oct. 2026 | **null** | **vide** — README 16 octets `# awesome-peppol` | stars 0 ; push 2026-06-12 |
| https://raw.githubusercontent.com/e-invoice-be/awesome-peppol/main/README.md | 200 | 11 oct. 2026 | null | vide | `# awesome-peppol` |
| https://github.com/itplr-kosit/xrechnung-testsuite | 200 | 11 oct. 2026 | Apache-2.0 | oui — push 2026-09-08 ; stars 99 | release `v2026-08-31` (2026-09-02) ; asset `xrechnung-3.0.2-testsuite-2026-08-31.zip` |
| https://github.com/itplr-kosit/xrechnung-testsuite/releases/tag/v2026-01-31 | 200 | 11 oct. 2026 | Apache-2.0 | oui (n’est plus `releases/latest`) |  |
| https://projekte.kosit.org/xrechnung/xrechnung-testsuite | 200 | 11 oct. 2026 | Apache (page GitLab) | oui | H1 `xrechnung-testsuite` |
| https://raw.githubusercontent.com/itplr-kosit/xrechnung-testsuite/master/LICENSE | 200 | 11 oct. 2026 | Apache-2.0 | — |  |
| https://github.com/kobima6813/einvoice-conformance-matrix | 200 | 20 oct. 2026 | Apache-2.0 (API `license.spdx_id`) | oui — push 2026-10-20 ; stars 0 ; not archived ; 0 release | description API « Reproducible cross-validator conformance matrix for EN 16931 e-invoice generators (KoSIT/XRechnung, CEN, Peppol BIS, due-vs-charged), with a GitHub Action. » ; entrée proposée par son auteur (#19) |
| https://kobima6813.github.io/einvoice-conformance-matrix/check.html | 200 | 26 oct. 2026 | Apache-2.0 (repo) | oui | title « Free e-invoice self-check — E-Invoice Conformance Lab » ; H1 « Check one e-invoice » ; « It is checked locally in your browser and is never uploaded » ; « A subset of EN 16931 business rules » ; « A clean result here does not mean the invoice passes KoSIT, CEN or Peppol validation » ; entrée proposée par son auteur (#24) |
| https://kobima6813.github.io/einvoice-conformance-matrix/pricing.html | 200 | 26 oct. 2026 | n/a | oui | H1 « Pricing » ; One-time check « 290 € » ; Vendor audit « 790 € » |
| https://github.com/facturxapi/validate-einvoice | 200 | 18 oct. 2026 | API `NOASSERTION` | oui — push 2026-10-18T13:55:16Z ; dernier commit `main` 2026-10-18 (`172c8b82`) ; stars **4** | description API « GitHub Action that runs the official ConnectingEurope EN16931 XSLT artefacts (CII/UBL): 1.3.16 by default, 1.3.17 opt-in. » ; `releases/latest` = `v1.2.0` (2026-10-18T13:55:32Z) ; tags `v1` et `v1.2.0` → `172c8b82…` (`v1.1.2` → `a805a904…`) |
| https://api.github.com/repos/facturxapi/validate-einvoice | 200 | 18 oct. 2026 | `NOASSERTION` | oui | idem |
| https://api.github.com/repos/facturxapi/validate-einvoice/git/refs/tags/v1 | 200 | 18 oct. 2026 | — | oui | object.sha `172c8b824316f94459741e4cb9f1f348eb052a02` (`a805a904…` au 11/10, `8457406…` au 18/08) |
| https://github.com/facturxapi/validate-einvoice/actions/runs/32089460503 | 200 | 11 oct. 2026 | — | — | page run publique (non citée dans le README) |
| https://github.com/facturxapi/en16931-oracles | 200 | 18 oct. 2026 | API `NOASSERTION` | oui — push 2026-10-18T14:03:57Z ; dernier commit `main` 2026-10-18 (`75541afc`) ; stars **4** ; release `v1.1.0` (2026-08-21) | description API « Reproducible EN16931 validation oracles — ConnectingEurope 1.3.17 fixtures, SVRL receipts, and mutants. » ; workflow upstream-drift : run manuel 2026-10-18 sur `main` `success` (« No drift », pin `validation-1.3.17`) |
| https://api.github.com/repos/facturxapi/en16931-oracles | 200 | 18 oct. 2026 | `NOASSERTION` | oui | idem |
| https://github.com/facturxapi/en16931-oracles/actions/runs/32081271235 | 200 | 11 oct. 2026 | — | — | page run publique (non citée dans le README) |
| https://www.itb.ec.europa.eu/invoice/upload | 200 | 18 oct. 2026 | n/a (Commission) | oui | H1 « eInvoice Validator » ; options `cii`/`ubl`/`credit` « release 1.3.17 » |
| https://www.itb.ec.europa.eu/vitb/rest/invoice/api/validate | HEAD **405** / GET **405** | 11 oct. 2026 | n/a | endpoint POST (HEAD/GET refusés) | attendu pour une API REST ; non un 404 |
| https://einvoicevalidator.eu/en | 200 | 14 oct. 2026 | n/a (service web ; dépôt privé) | oui | title « E-Invoice Validator: check XRechnung & ZUGFeRD free » ; H1 « E-invoice validator. Free, no sign-up. » |
| https://kontevia.de/tools/e-rechnung-pruefen | 200 | 12 oct. 2026 | n/a | oui | title « E-Rechnung prüfen: XRechnung, ZUGFeRD Validator \| Kontevia » ; « Kostenlos, ohne Anmeldung » |
| https://einvoicecheck.com/en/validator | 200 (HEAD et GET) | 18 oct. 2026 | n/a (outil hébergé commercial ; entrée proposée par son mainteneur, #15) | oui | title « XRechnung Validator for reproducible technical checks » ; H1 « Validate an XRechnung against an identified ruleset » ; `/en` 200, FAQ : « Only the XRechnung XML configurations explicitly listed in the interface for UBL 2.1 or CII D16B. This page does not promise ZUGFeRD PDF or end-to-end Peppol validation. » ; `/en/terms` 200 : « The service is free technical validation » ; « free validation phase with no account, no checkout, no payment and no subscription » ; aucun prix dans le HTML |
| https://github.com/e-invoice-be/peppol-cli | 200 | 14 oct. 2026 | MIT (API `license.spdx_id`) | oui ; push 2026-10-14 ; stars 3 ; release `v0.0.7` (2026-10-14) ; not archived | description API « CLI for the e-invoice.be Peppol API » ; `internal/cli/validate.go` : `validate ubl` / `validate json` « against Peppol BIS Billing 3.0 » ; `internal/client/client.go` : POST `/api/validate/ubl` et `/api/validate/json` sur `https://api.e-invoice.be`, clé API requise |
| https://e-invoice.be/peppol-cli | 200 | 14 oct. 2026 | n/a | oui | title « Peppol CLI \| Open-Source E-Invoicing Tool \| e-invoice.be » ; « Requires an e-invoice.be account. » ; « You only pay for the invoices you send or receive, from €0.18. » |
| https://docs.e-invoice.be/cli | 200 | 14 oct. 2026 | n/a | oui | H1 « peppol CLI » ; « The CLI calls the single API host https://api.e-invoice.be » |
| https://github.com/reviewdog/action-eslint | 200 | 11 oct. 2026 | MIT | oui — push 2026-10-08 ; stars 259 | **exclu README** |
| https://github.com/aquasecurity/trivy-action | 200 | 11 oct. 2026 | Apache-2.0 | oui — push 2026-10-07 ; stars 1436 | **exclu README** |
| https://github.com/golangci/golangci-lint-action | 200 | 11 oct. 2026 | MIT | oui — push 2026-10-01 ; stars 1450 | **exclu README** |
| https://github.com/oxsecurity/megalinter | 200 | 11 oct. 2026 | AGPL-3.0 | oui — push 2026-10-11 ; stars 2611 | **exclu README** |
| https://apify.com/rigel/facturx-toolkit | 200 | 21 oct. 2026 | propriétaire (service hébergé, pas de dépôt public) | oui — build `0.1.7` (2026-10-17) | H1 « Factur-X Validator & Generator: ZUGFeRD, EN 16931, FR 2026 » ; « Not an approved platform (PA). » ; « Pay per event, in USD. » ; `document-validated` « $0.015 » ; build `0.1.7` lu via l’API publique Apify (`taggedBuilds.latest`) ; entrée proposée par son auteur (#21) |

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
| https://e-rechnung-api.fly.dev/ | HEAD 405 / GET 200 | exception de méthode ; GET utilisé pour la citation |
| https://e-rechnung-api.fly.dev/validator | HEAD 405 / GET 200 | idem |
| https://invoicein-api.peculiar.systems/docs | HEAD 405 / GET 200 | idem |
| https://www.itb.ec.europa.eu/vitb/rest/invoice/api/validate | HEAD 405 / GET 405 | POST-only |
| https://api.eleata.io | GET 502 (2 essais) | racine seulement ; valeur par défaut `api-base` de `eleata/validate-einvoice-action`, pas un lien README ; endpoints de l’API non appelés |

---

## Deltas vs 11 oct. 2026

Relevé partiel du 18 oct. 2026, limité à la publication EN16931 1.3.17 et à l'entrée E-Invoice Check (#15).

| Entrée | 11/10 | 18/10 |
|---|---|---|
| ConnectingEurope/eInvoicing-EN16931 | branche `validation-1.3.17` fusionnée, sans tag ni release ; stars 259 | release **`validation-1.3.17`** (2026-10-12T12:28:45Z), `releases/latest` ; stars 261 |
| Registre EC EN16931 | dernière version 1.3.16 (16/04/26) | **1.3.17**, « Published: 12/10/26 », date d'effet 15/11/26 |
| ITB eInvoice Validator | « release 1.3.16 » | « release 1.3.17 » |
| ConnectingEurope examples (Corpora) | release `validation-1.3.16` | release **`validation-1.3.17`** |
| facturxapi/validate-einvoice | description « … 1.3.16 XSLT … » ; release `v1.1.2` ; `v1` → `a805a904` | description « … 1.3.16 by default, 1.3.17 opt-in » ; release **`v1.2.0`** ; `v1` → `172c8b82` |
| facturxapi/en16931-oracles | description « … 1.3.16 fixtures … » | description « … 1.3.17 fixtures … » ; release inchangée `v1.1.0` |
| E-Invoice Check (Validators) | absent | ajouté (#15, proposé par son mainteneur) ; remesuré 2026-10-18T21:34:11Z : title, H1, FAQ `/en` et Terms cités, prix `[non-mesure]` |

## Deltas vs 18 août 2026

| Entrée | 18/08 | 11/10 |
|---|---|---|
| fnfempe/France_RFE | `v1.4.0.03` (2026-08-04) | **`v1.4.0.04`** (`published_at` 2026-09-04T22:42:01Z) ; aucun asset déposé |
| DGFiP plateformes | modifié le 17/08/2026 | **modifié le 22/09/2026** |
| FNFE-MPE Ressources | schematrons BR-FR-CTC fix03 du 4 août | **fix04 du 4 septembre** (`…V1.4.0.04.zip`) |
| ConnectingEurope/eInvoicing-EN16931 | push 2026-04-14 ; stars 252 | push **2026-10-11** (fusion branche `validation-1.3.17`, sans tag ni release) ; stars 259 |
| Registre EC EN16931 | 1.3.16 | 1.3.16 (publication automne annoncée « next 09 Oct 2026 », rien de listé au 11/10) |
| FacturX API | prix `[non-mesure]` | **retiré** (produit commercial du mainteneur de la liste) |
| FormatX title | « FormatX - Convertir PDF en Factur-X gratuitement » | « … \| Facture électronique conforme » |
| FormatX `/api-docs` | Free 10 / Pro 100 / Business 500 factures/mois | « Aucun quota mensuel, aucune facturation. » ; 60 requêtes/minute |
| Get FacturX home | H1 « La boîte à outils Factur-X qui complète votre Plateforme Agréée » ; CTA 4 utilisations / jour ; HEAD 405 | H1 « Créez, envoyez et recevez vos factures Factur-X, sans ERP » ; CTA **absent** ; HEAD **200** |
| Get FacturX `/validate` title | « Validateur Factur-X en ligne gratuit » | « Factur-X Validator : validateur Factur-X gratuit en ligne » |
| Mustangproject site | 2.25.0 (05.08.2026) ; `Mustang-CLI-2.25.0.jar` | **2.26.0** (25.08.2026) ; `Mustang-CLI-2.26.0.jar` |
| Marketplace `factur-x` | « 1 result » | « 5 results » (facturxapi après `v1.1.2`, attestwire, prufix, beliq, invowerk) |
| Marketplace `zugferd` | « 0 results » | « 3 results » (facturxapi après `v1.1.2`, beliq, invowerk) |
| Marketplace `en16931` | non relevé dans ce fichier | « 1 result » (`facturxapi/validate-einvoice`) |
| attestwire/validate-einvoice-action | tag `v1.0.0` | release **`v1.10.0`** (2026-10-04) |
| facturxapi/validate-einvoice | stars 0 ; tag `v1` = `8457406…` | stars **4** ; description changée ; `releases/latest` `v1.1.2` ; tags `v1`, `v1.1.2` = `a805a904…` |
| hernaninverso/validate-einvoice-action | dépôt à ce nom | **redirige vers `eleata/validate-einvoice-action`** ; description API changée |
| akretion/factur-x | stars 303 ; `6.7` (2026-08-08) | stars **310** ; release **`7.5`** (2026-10-09) |
| attestwire/en16931 | push 2026-08-18 ; tag `v0.7.3` (relevé 17 sept.) | push 2026-10-04 ; release **`v0.14.1`** |
| horstoeko/zugferd | stars 432 ; push 2026-08-04 ; `v1.0.124` | stars **437** ; push 2026-10-02 ; **`v1.0.132`** (2026-08-30) ; README names `horstoeko/invoicesuite` as successor |
| pretix/python-drafthorse | stars 176 | stars **179** ; description API « Pure-python ZUGFeRD implementation » |
| stephanstapel/ZUGFeRD-csharp | stars 392 ; push 2026-08-05 ; `18.0.0` | stars **395** ; push 2026-10-09 ; **`18.0.1`** ; README announces end of maintenance on November 30, 2026, names FactoorSharp as successor |
| ZUGFeRD/mustangproject | stars 451 ; push 2026-08-17 ; `core-2.25.0` | stars **480** ; push 2026-10-10 ; **`core-2.26.0`** (2026-08-25) |
| itplr-kosit/xrechnung-testsuite | push 2026-08-14 ; `v2026-01-31` ; stars 96 | push 2026-09-08 ; **`v2026-08-31`** (2026-09-02) ; stars 99 |
| facturxapi/en16931-oracles | stars 0 | stars **4** ; description changée ; release `v1.1.0` (2026-08-21) |
| sdras/awesome-actions | stars 28140 | stars **28306** |
| E-Rechnung API (`/`, `/validator`) | ajouté le 10 oct. 2026 (HTTP 200) | HEAD **405** / GET 200 |
| entreprendre.service-public.fr/actualites/A15683 | HEAD 200 | 301 → `entreprendre.service-public.gouv.fr` (200) |
| exclus README (eslint / trivy / golangci / megalinter) | stars 260 / 1396 / 1444 / 2558 | stars 259 / 1436 / 1450 / 2611 |

Aucun dépôt de la liste principale n’est `archived`.

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
| `eleata` (ex-`hernaninverso`) / `attestwire/validate-einvoice-action` | 0 stars |
| `stephanstapel/ZUGFeRD-csharp` | README : « My maintenance of this project will end on November 30, 2026. » |
| `horstoeko/zugferd` | README names `horstoeko/invoicesuite` as « The official successor » |
| Pack FNFE | ZIP derrière e-mail |
| Pack FeRD | ZIP non mesuré |

---

## Licences (synthèse API / fichier)

| SPDX / constat | Entrées |
|---|---|
| EUPL 1.2 (fichier ; API NOASSERTION) | ConnectingEurope/eInvoicing-EN16931 ; facturxapi/validate-einvoice (NOTICE) |
| Apache-2.0 | France_RFE, mustangproject, phax/phive, phax/phorm, phax/kaltblut, phax/en16931-cii2ubl, phax/en16931-purifier, phax/en16931-ubl2cii, phax/ph-cii, phax/ph-redact, phax/ph-ubl, python-drafthorse, ZUGFeRD-csharp, xrechnung-testsuite, eleata (ex-hernaninverso), trivy-action |
| MIT | horstoeko/zugferd, invoicenavigator, wsystemdev/einvoice-validate-action, attestwire (Action + en16931), reviewdog/action-eslint, golangci-lint-action |
| CC0-1.0 | sdras/awesome-actions, morganrcu/awesome-europe ; **texte de cette liste** |
| CC0 1.0 (fichier ; API NOASSERTION) | causa-prima-ai/awesome-invoicing |
| BSD 3-clause (fichier ; API NOASSERTION) | akretion/factur-x |
| API `NOASSERTION` ; README Apache 2 (code Java) | phax/phive-rules |
| AGPL-3.0 | oxsecurity/megalinter (exclu README) |
| `licence: null` | e-invoice-be/awesome-peppol |
| n/a | sites validateurs, FNFE gate, FeRD Infopaket, boutique AFNOR, pages .gouv, ITB |

---

*Fin des checks 11 oct. 2026.*
