# Contributing

This is a sourced list, not a ranking and not an endorsement.

**Inclusion ≠ endorsement.** A line here does not mean an tool is compliant, official, recommended, or better.

## Pull requests

1. One entry per PR.
2. The URL must return HTTP 200 on a GET (or a documented method exception: HEAD 405 + GET 200, POST-only REST).
3. Use the same format and roughly the same length as neighbouring entries: `[Name](url) — one factual sentence from the page or GitHub API this run.`
4. Do not invent prices, star counts, volumes, or pass/fail rates. Quote prices in the currency shown; if the page shows none, write `[non-mesure]`.
5. Quote the site’s own words for “valide / conforme / répare”. Do not repeat them as our verdict.
6. Put the entry in the existing category, **alphabetically** by display name.
7. Update [`CHECKS.md`](CHECKS.md) with the fetch date, HTTP status, license, and a short citation.
8. Do not attach ZIPs, XML fixtures, or vendor binaries.

## Self-authored tools

If you maintain a listed project, the line must match the format and length of the others in that section. Extra CI run IDs, topic dumps, or marketing claims will be trimmed.

The same rule applies to the list maintainer's own projects: they sit at their alphabetical place, never first, and are marked *(list maintainer's project)*. The maintainer's commercial product is not listed.

## Operator submissions

If you run or sell the tool you are adding:

1. Say so in the PR description. The entry ends with `Submitted by the operator.`
2. The site must have a legal notice or Impressum that names an identifiable operator (company or person name, and address). Maintainers check it before merging.
3. If you quote a price, also quote what the page shows with it: quotas, a beta label, a waiting list or “paid plans not open yet”, and any restriction on who can buy (for example business customers only).
4. One entry per operator. For another product from the same operator, update the existing entry instead of adding a new one.
5. Maintainers may edit the entry to add these details before merging.

## What we will not list

- Generic linters / scanners that are not e-invoicing tools
- Dead URLs (404) except as a documented negative check
- Copies of AFNOR / FNFE / FeRD example packs (pointer only)

See [`LICENSE-NOTES.md`](LICENSE-NOTES.md) for redistribute vs pointer.
