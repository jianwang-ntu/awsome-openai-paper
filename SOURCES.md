# Sources and coverage

Snapshot checked on **21 October 2026**. Eligible public release dates: **21 October 2025 through 21 October 2026**, inclusive. There is no numerical limit on papers.

## Source inventory

The collection was assembled from the complete available source inventories, rather than just their first visible pages:

- [OpenAI publication index](https://openai.com/research/index/publication/), [research sitemap](https://openai.com/sitemap.xml/research/), [publication sitemap](https://openai.com/sitemap.xml/publication/), and [full news RSS feed](https://openai.com/news/rss.xml). The research and publication sitemap URLs were reconciled against the full feed. Research-related entries in other feed categories were also inspected.
- [OpenAI Alignment research blog](https://alignment.openai.com/), including its individual dated research pages.
- [OpenAI Deployment Safety Hub](https://deploymentsafety.openai.com/), including the full embedded item inventory beyond the eight initially visible cards.
- [Anthropic research index](https://www.anthropic.com/research), including its full embedded publication list: 94 entries in the requested window, before excluding announcements and merging paper aliases.
- [Anthropic Alignment Science Blog](https://alignment.anthropic.com/), [Safeguards Blog](https://safeguards.anthropic.com/), and [Transformer Circuits](https://transformer-circuits.pub/).
- [Anthropic system-card directory](https://www.anthropic.com/system-cards), [Anthropic Institute economic scenarios](https://www.anthropic.com/institute/econ-scenarios), and linked technical reports.
- Primary paper records on [arXiv](https://arxiv.org/), [bioRxiv](https://www.biorxiv.org/), and the labs' own document servers, for paper titles, dates, affiliations, and direct links. Forty-two arXiv records were checked during the date audit; additional primary papers were found through targeted searches.
- The [OpenAI mathematics manuscript map](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/CONTENTS.md), pinned to commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. Its 719 active PDF paths were matched against the complete, non-truncated `preprints/` Git tree. A recursively fetched repository-root tree was truncated, so it was not used to certify those paths.

Each entry in [data/catalog.json](data/catalog.json) retains its lab, title, date, document type, source URL, direct paper URLs, source index, and date basis. Related announcement aliases are retained where applicable. Research articles without a separately verified paper are kept in [RESEARCH_NOTES.md](RESEARCH_NOTES.md), outside the standalone-paper count.

The README groups the 101 papers and reports into eight primary topics. Every entry has an editorial summary grounded in its abstract, full paper, or official research description; `summary_sources` records the supporting URLs. Summaries paraphrase contributions and reported findings without implying independent verification. Cross-cutting papers appear once, under their main contribution, and retain their lab labels. Topic assignments and summaries are stored in the catalog so regeneration preserves them. The separate mathematics appendix and other supplementary collections retain their existing scope.

## Inclusion and date rules

1. Include original papers, preprints, formal HTML papers, and technical or empirical reports released by either lab, including verified collaborations and research published through the Anthropic Fellows Program.
2. Separate system/model cards, informal research articles, and the model-generated mathematics collection from the main papers-and-reports list.
3. Use the earliest verified public date found among the official announcement and the paper record. Use the first arXiv submission, not a later version or conference date. A report's month is retained when the source does not specify a day.
4. Exclude a paper first released before the cutoff even when an in-window post links to it. The date audit excluded *Agentic Property-Based Testing* (10 October 2025), *Stress-Testing Model Specs* (9 October 2025), and *Believe It or Not* (20 October 2025).
5. Merge duplicate paper links and announcement aliases. Separate distinct companion papers. Count mirrored copies of a content-addressed PDF once.
6. Exclude ordinary product launches, grant/fellowship announcements, customer marketing, and unrelated third-party papers that merely evaluate OpenAI or Anthropic models. A citation in a research article alone is not evidence that the cited paper was produced by that lab.
7. Keep the inherited historical bibliography in [archive/](archive/README.md), outside the current date-filtered lists. The archive is intentionally not constrained to the new window.

## Verification and limits

The direct-document link check returned **134 HTTP 200 responses and two HTTP 403 responses**, with no HTTP 404 responses, across 136 distinct document URLs. The two blocked URLs are bioRxiv records; their titles and OpenAI affiliations were verified through primary indexed pages. A 403 is not treated as a successful HTTP check. The saved [link audit](data/link-audit.json) records the results. Mathematics PDF paths were checked through Git objects rather than downloading hundreds of manuscripts.

This bibliography aims to include all eligible works discoverable from the checked sources. **It is not a certified inventory of every paper coauthored by every employee of either company.** Unindexed preprints, outside collaborations, or papers absent from the public source inventories may still be missing. Source indexes can also omit items or disagree on dates. The recorded date basis makes those choices inspectable.

The mathematics appendix records the collection's official public announcement date, not internal dates embedded in directory names. Its manuscript count is separate from the main bibliography; some results may overlap with earlier mathematical announcement papers. The source repository records three withdrawn manuscripts, which are not counted in its active 719-manuscript list. Inclusion does not endorse or independently verify any manuscript's claims.

This is a fixed snapshot, not an automated monitor. To refresh it, repeat discovery and verification, update the data and date window, and regenerate the views. Running the renderer alone does not establish that newly released papers have been found.
