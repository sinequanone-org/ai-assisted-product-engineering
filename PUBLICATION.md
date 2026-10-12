# Before a public copy

Version 0.1.0 is a draft. This file does not publish the repository.

The license in [LICENSE](LICENSE) is the Apache License, Version 2.0.
There is one license. Do not add a second license file.

MIT is the other license this package can use. To switch, do all of these
before the first public copy:

1. Replace `LICENSE` with the MIT license text.
2. Replace `NOTICE` so it matches MIT. Remove the Apache notice.
3. Set `license: MIT` in every `skills/*/SKILL.md` frontmatter.
4. Update the license sentences in `README.md` and `CONTRIBUTING.md`.

After the first public copy, a license change needs the copyright holder's
decision. Do not publish under both licenses.

## Checks

1. Run `python3 scripts/check-public-ready.py`.
2. Read the tree for unpublished names, local paths, and secrets.
3. Confirm `LICENSE` and `NOTICE` name the copyright holder you intend.
4. Confirm there is still no release tag, unless you mean to cut one.
5. Change repository visibility only as a separate owner action.

This package does not install hooks and does not change GitHub settings.
