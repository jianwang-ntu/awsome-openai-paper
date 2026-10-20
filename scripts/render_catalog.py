#!/usr/bin/env python3
"""Validate the bibliography and regenerate its Markdown views (standard library only)."""
import datetime as dt
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data/catalog.json').read_text())
ROWS = DATA['records']
MATH = DATA['math_manuscripts']


def validate():
    start, end = DATA['start_date'], DATA['end_date']
    assert start == '2025-10-21' and end == '2026-10-21'
    assert {r['lab'] for r in ROWS} == {'OpenAI', 'Anthropic'}
    topics = DATA['topics']
    topic_ids = [topic['id'] for topic in topics]
    assert len(topic_ids) == len(set(topic_ids)), 'Duplicate topic identifiers'
    assert all(topic['title'].strip() for topic in topics)
    seen = set()
    documents = set()
    for row in ROWS + MATH:
        date = row['date']
        assert len(date) in (7, 10), row
        dt.date.fromisoformat(date if len(date) == 10 else date + '-01')
        # Month-only dates retain the source's precision; neither boundary is guessed.
        if len(date) == 7:
            assert start[:7] < date <= end[:7], row
        else:
            assert start <= date <= end, row
        assert row['title'].strip() and row['date_basis'] and row['source_indexes'], row
        if row['kind'] in {'paper', 'report'}:
            assert row.get('primary_topic') in topic_ids, ('Missing or unknown topic', row['title'])
            summary = row.get('summary', '')
            assert 12 <= len(summary.split()) <= 60, ('Summary must be concise', row['title'])
            assert '\n' not in summary and summary[-1] in '.?!', row['title']
            assert row.get('summary_sources'), ('Missing summary evidence', row['title'])
        key = (row['lab'], row['kind'], row['title'], date, tuple(row['paper_urls']))
        assert key not in seen, ('duplicate record', row)
        seen.add(key)
        for url in [row['source_url'], *row['paper_urls'], *row['source_indexes'],
                    *row.get('summary_sources', [])]:
            assert urlsplit(url).scheme == 'https' and urlsplit(url).netloc, url
            assert not any(c.isspace() for c in url) and not url.endswith(':'), url
        if row['kind'] in {'paper', 'report', 'AI-generated mathematics manuscript'}:
            assert row['paper_urls'], row
            for url in row['paper_urls']:
                assert url not in documents, ('duplicate document', url)
                documents.add(url)
    assert len(MATH) == 719
    assert all(r['lab'] == 'OpenAI' for r in MATH)
    assert all(DATA['math_source_commit'] in r['paper_urls'][0] for r in MATH)
    assert set(topic_ids) == {r['primary_topic'] for r in ROWS if r['kind'] in {'paper', 'report'}}


def escape(text):
    return text.replace('|', '\\|').replace('\n', ' ')


def link(label, url):
    return f'[{label}]({url})'


def table(rows, show_lab=False, show_kind=False):
    headers = ['Date'] + (['Lab'] if show_lab else []) + ['Publication']
    if show_kind:
        headers += ['Type']
    headers += ['Links']
    lines = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    for row in rows:
        links = [link('Source', row['source_url'])]
        for i, url in enumerate(row['paper_urls']):
            links.append(link('Paper' if len(row['paper_urls']) == 1 else f'Paper {i + 1}', url))
        cells = [row['date']] + ([row['lab']] if show_lab else []) + [escape(row['title'])]
        if show_kind:
            cells += [row['kind']]
        cells += [' · '.join(links)]
        lines.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join(lines) + '\n'


def paper_entry(row):
    paper_links = [link('Paper' if len(row['paper_urls']) == 1 else f'Paper {i + 1}', url)
                   for i, url in enumerate(row['paper_urls'])]
    links = ' · '.join([*paper_links, link('Source', row['source_url'])])
    return (f"### {row['title']}\n\n"
            f"*{row['lab']} · {row['date']} · {row['kind']}* · {links}\n\n"
            f"{row['summary']}\n\n")


def render():
    core = [r for r in ROWS if r['kind'] in {'paper', 'report'}]
    cards = [r for r in ROWS if r['kind'] == 'system card']
    notes = [r for r in ROWS if r['kind'] in {'research article', 'research note'}]
    counts = Counter(r['lab'] for r in core)
    topic_counts = Counter(r['primary_topic'] for r in core)
    topic_links = '\n'.join(
        f"- [{topic['title']}](#topic-{topic['id']}) — {topic_counts[topic['id']]}"
        for topic in DATA['topics'])
    text = f'''# Awesome OpenAI and Anthropic Papers

Research papers and technical reports from **OpenAI and Anthropic**, released during **21 October 2025–21 October 2026**, inclusive. Last checked: **21 October 2026**. There is **no paper-count limit**.

The main bibliography below contains **{len(core)} papers and reports**: **{counts['OpenAI']} OpenAI** and **{counts['Anthropic']} Anthropic**. Papers are grouped by their primary topic, with the lab, date, source links, and a short summary for every entry. Within each topic, entries run from newest to oldest. Cross-cutting papers appear once, under their main contribution.

{topic_links}

Additional collections:

- [System cards and addenda](SYSTEM_CARDS.md) — {len(cards)}
- [Additional research articles and notes](RESEARCH_NOTES.md) — {len(notes)}; these are not counted as standalone papers
- [OpenAI mathematics manuscripts](OPENAI_MATH_MANUSCRIPTS.md) — {len(MATH)} model-generated manuscripts, indexed individually and separately
- [Sources, date rules, and coverage](SOURCES.md)
- [Machine-readable bibliography](data/catalog.json)
- [Historical upstream archive](archive/README.md) — outside the current bibliography

Dates use the earliest verified public release found in the checked sources: an official announcement, a paper's first arXiv submission, or the date printed on a report. Month-only dates preserve the source's precision. A new blog post or conference appearance does not make an older paper eligible. See [coverage notes](SOURCES.md) for the limits of the source inventory.

Summaries describe the linked papers' contributions and reported findings; they are not independent replications. Their supporting URLs are retained in the machine-readable bibliography. The separately indexed mathematics manuscripts remain in their own appendix.

'''
    for topic in DATA['topics']:
        text += f'<a id="topic-{topic["id"]}"></a>\n\n## {topic["title"]}\n\n'
        entries = [r for r in core if r['primary_topic'] == topic['id']]
        entries.sort(key=lambda r: (r['date'], r['title']), reverse=True)
        text += ''.join(paper_entry(row) for row in entries)
    text += '''
## Updating the collection

Add verified entries to `data/catalog.json`, retaining their publication date, lab, source URL, paper URL, and date basis. For each paper or report, also supply a `primary_topic` from the top-level `topics` list, a concise `summary`, and the supporting `summary_sources`. Then run:

```sh
python3 scripts/render_catalog.py
```

The command checks dates, duplicate records, duplicate document links, topic assignments, summary coverage, required metadata, and URL syntax before regenerating the Markdown files. It does not perform a new literature search or automatically advance the snapshot window.

Originally forked from [chenxingqiang/awsome-openai-paper](https://github.com/chenxingqiang/awsome-openai-paper). Its original files are preserved under `archive/`.
'''
    (ROOT / 'README.md').write_text(text)
    (ROOT / 'SYSTEM_CARDS.md').write_text(
        '# System cards and addenda\n\n'
        'Window: **2025-10-21–2026-10-21**. These technical safety documents are listed separately from research papers. Month-only dates come from the official Anthropic system-card directory.\n\n'
        + table(cards, show_lab=True) + '\n[Back to the bibliography](README.md)\n')
    (ROOT / 'RESEARCH_NOTES.md').write_text(
        '# Additional research articles and notes\n\n'
        'Window: **2025-10-21–2026-10-21**. These official empirical articles, research notes, tool descriptions, and preliminary findings do not have a separately verified standalone paper link in this inventory. They are **not included in the paper count**. A linked article may discuss an already-listed paper. Program announcements and ordinary product launches are excluded.\n\n'
        + table(notes, show_lab=True) + '\n[Back to the bibliography](README.md)\n')
    (ROOT / 'OPENAI_MATH_MANUSCRIPTS.md').write_text(
        '# OpenAI mathematics manuscripts\n\n'
        f'This appendix indexes all **{len(MATH)} active manuscripts** in the [official manuscript map](https://github.com/openai/math/blob/{DATA["math_source_commit"]}/CONTENTS.md), pinned to commit `{DATA["math_source_commit"]}`. Every listed PDF path was checked against the complete `preprints/` Git tree at that commit.\n\n'
        'The date below is the **6 October 2026 public collection announcement**, not a date inferred from an internal manuscript filename. These works were produced by an internal OpenAI model. Their verification status varies; listing a manuscript does not certify its mathematical claims. The source repository supplies revisions, citations, and available Lean proofs.\n\n'
        'These manuscript entries are separate from the main AI-paper count. Some mathematical results may also appear in earlier announcement papers, so counts across the two lists should not be added as a count of distinct results.\n\n'
        'The source history also records three withdrawals: *Algebraicity of Weil classes on split abelian eightfolds*, *Algebraicity of Kuga–Satake Correspondences for K3 Surfaces*, and *The rational Hodge conjecture for products of K3 surfaces*. They are excluded from the active list below; see the [withdrawal notices](https://github.com/openai/math/blob/' + DATA['math_source_commit'] + '/history.md).\n\n'
        + table(MATH) + '\n[Back to the bibliography](README.md)\n')
    print(f'Validated and rendered: {len(core)} papers/reports, {len(cards)} system cards, '
          f'{len(notes)} research articles/notes, {len(MATH)} mathematics manuscripts.')


if __name__ == '__main__':
    validate()
    render()
