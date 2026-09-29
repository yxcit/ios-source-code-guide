# Plan your first customization before changing code

Choose one small change that makes the project recognizably yours, such as a title, color, or sample record. Avoid changing the data model, dependency versions, and navigation at the same time.

## Establish a baseline

Build and run the original project using its instructions. Capture the relevant screen and record the steps that produced it. A baseline lets you compare the result of your change.

## Map the change

Identify the file or configuration entry controlling the value you want to modify. Check whether the same value also appears in localization files, test fixtures, or generated assets. Prefer the project's existing pattern rather than introducing a second configuration system.

## Exercise the flow

After the change, repeat the original steps. Check narrow and wide layouts, long labels, and any other supported language affected by the edit. Save the change separately in version control.

## Keep a short customization log

Record the changed files, why they changed, and what you checked. This becomes useful when incorporating a seller's future update without overwriting your own work.

---

Part of the [iOS source-code project guide](../README.md), maintained by [YXC Code](https://app.yxcit.com/en?utm_source=github&utm_medium=referral&utm_campaign=source_code_guide). Prepared with AI assistance.
