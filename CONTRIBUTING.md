# Contributing

This is a sourced list, not a ranking and not an endorsement.

**Inclusion ≠ endorsement.** A line here does not mean an tool is compliant, official, recommended, or better.

## Pull requests

1. One entry per PR.
2. The URL must return HTTP 200 on a GET (or a documented method exception: HEAD 405 + GET 200, POST-only REST).
3. Use the same format and roughly the same length as neighbouring entries: `[Name](url) — one factual sentence from the page or GitHub API this run.`
4. Do not invent prices, star counts, volumes, or pass/fail rates. If the page does not show a euro amount, write `[non-mesure]`.
5. Quote the site’s own words for “valide / conforme / répare”. Do not repeat them as our verdict.
6. Put the entry in the existing category, **alphabetically** by display name.
7. Update [`CHECKS.md`](CHECKS.md) with the fetch date, HTTP status, license, and a short citation.
8. Do not attach ZIPs, XML fixtures, or vendor binaries.

## Self-authored tools

If you maintain a listed project, the line must match the format and length of the others in that section. Extra CI run IDs, topic dumps, or marketing claims will be trimmed.

## What we will not list

- Generic linters / scanners that are not e-invoicing tools
- Dead URLs (404) except as a documented negative check
- Copies of AFNOR / FNFE / FeRD example packs (pointer only)

See [`LICENSE-NOTES.md`](LICENSE-NOTES.md) for redistribute vs pointer.
