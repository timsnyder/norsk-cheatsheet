# Validation policy

## What CI proves

`scripts/validate.py` checks required Markdown pages, basic formatting,
line length, links to local files, and curated grammatical examples.
The MkDocs build checks that the website can be generated.

## What CI does not prove

A passing build is **not** proof that every Norwegian phrase is grammatical,
idiomatic, or accurately translated. The curated examples are regression
fixtures, not an independent Norwegian grammar engine.

## Editorial review

Before merging linguistic changes:

1. Check spelling and inflection against [Bokmålsordboka](https://ordbokene.no/).
2. Consult [Språkrådet](https://sprakradet.no/) for grammar and usage guidance.
3. Review translations for meaning, tone, and naturalness.
4. Add a regression example when correcting a previously published mistake.
5. Flag uncertain usage for human/native-speaker review.

Native-speaker review is welcome, but not an actual CI dependency.
