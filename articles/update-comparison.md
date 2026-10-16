# Review a source-package update without losing your changes

Treat a new vendor archive as a new input, not a replacement for your working copy.

## Preserve both versions

Keep the original package and the updated package separately. Record their versions and retain the customization commits you have made. Read any included release notes before merging files.

## Compare deliberately

Inspect changes to project configuration, dependencies, data models, assets, and your customized screens. A small-looking configuration change can still require a different setup step, so test the updated environment independently.

## Integrate in small steps

Apply a coherent group of changes, build, and repeat the relevant user flow. When both versions modify the same behavior, decide explicitly how the final behavior should work rather than selecting one side of every conflict.

## Recheck stored data

Use disposable copies of representative data to test the documented upgrade path. Keep backup and restore checks separate from a successful build. Record any migration assumptions in the project's setup notes.

---

Part of the [iOS source-code project guide](../README.md), maintained by [YXC Code](https://app.yxcit.com/en?utm_source=github&utm_medium=referral&utm_campaign=source_code_guide). Prepared with AI assistance.
