# Contributing to Awesome AI Agents 🤖

Thank you for helping make this a useful AI agents directory! Every contribution, no matter how small, is valued and appreciated.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Adding a New Entry](#adding-a-new-entry)
- [Suggesting a New Category](#suggesting-a-new-category)
- [Reporting Issues](#reporting-issues)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Quality Standards](#quality-standards)

---

## Code of Conduct

This project follows a simple rule: **be kind, be constructive, be helpful**. We welcome contributors of all experience levels. Disrespectful or exclusionary behavior will not be tolerated.

---

## How to Contribute

1. **Fork** this repository
2. **Create** a new branch: `git checkout -b add/my-awesome-tool`
3. **Make** your changes following the guidelines below
4. **Commit** your changes: `git commit -m "Add: ToolName to Category"`
5. **Push** to your branch: `git push origin add/my-awesome-tool`
6. **Open** a Pull Request with a clear title and description

---

## Adding a New Entry

### Format

Each entry should follow this exact Markdown table format:

```markdown
| [Tool Name](https://link-to-tool.com) | One-sentence description of what this tool does and why it's useful for AI agents. | ![Stars](https://img.shields.io/github/stars/owner/repo?style=flat-square&logo=github) |
```

For tools without a public GitHub repository, use:

```markdown
| [Tool Name](https://link-to-tool.com) | One-sentence description of what this tool does and why it's useful for AI agents. | ![Stars](https://img.shields.io/badge/stars-N%2FA-lightgrey?style=flat-square) |
```

### Requirements for New Entries

- ✅ **Directly relevant** to AI agents (frameworks, tools, libraries, learning resources)
- ✅ **Working link** — points to the official homepage or repository
- ✅ **Project status** — link evidence of maintenance, or label an educational/historical or archived entry honestly
- ✅ **Honest description** — no marketing fluff; be accurate and concise (max 150 characters)
- ✅ **Correct category** — placed in the most appropriate section
- ✅ **Not a duplicate** — search the list before adding

### Where to Place Your Entry

Put new entries in the table of the most relevant category. If you're unsure, pick the closest match and mention it in your PR description — we can always move it.

---

## Suggesting a New Category

If you believe a new top-level category is needed:

1. Open an **Issue** with the title `[Category] Proposed: Your Category Name`
2. Explain what tools would belong there and why it deserves its own section
3. Include at least **5 tools** that would populate the new category
4. Allow 48 hours for community discussion before opening a PR

---

## Reporting Issues

If you find a broken link, outdated description, or incorrect information:

- Open an **Issue** with the title `[Fix] Brief description`
- Include the name of the entry, the current incorrect information, and (if applicable) the correct information
- Include the observed status or redirect and the date checked; maintainers review issues as time permits.

---

## Pull Request Guidelines

| Rule | Reason |
|------|--------|
| One PR per addition (or small batch of related additions) | Keeps reviews focused and merge conflicts minimal |
| PR title format: `Add: ToolName to CategoryName` | Makes changelog easy to read |
| Describe the tool in your PR body | Helps reviewers who aren't familiar with it |
| Link to the tool's homepage or GitHub | Required for verification |
| Don't update star count badges manually | Badges are dynamic — they self-update |

---

## Quality Standards

We prioritize accurate descriptions and useful official sources. We may decline entries that:

- ❌ Are abandoned (no activity for 2+ years)
- ❌ Duplicate an existing entry without clear differentiation
- ❌ Lack enough documentation or runnable examples to understand their purpose
- ❌ Are purely promotional (products with no technical merit)
- ❌ Have descriptions that are inaccurate, vague, or copy-pasted marketing text

---

## Recognition

All contributors are automatically recognized in the GitHub contributor graph. Significant contributors may be highlighted in the README. Thank you for making this resource better for everyone! 🙏

---

*By contributing, you agree that your contributions will be licensed under the [Apache 2.0 License](LICENSE).*

## Verify a change

Run `python scripts/check_links.py`. To check public external links too, run `python scripts/check_links.py --remote`. Explain uncertain results rather than removing a tool solely because it rate-limits automated requests. Describe actual capabilities without unsupported performance, popularity, privacy, or cost claims.
