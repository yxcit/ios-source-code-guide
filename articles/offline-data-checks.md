# Check an offline app with disposable data

An offline claim is easier to evaluate with a small test plan. Use disposable information until you understand the storage behavior.

## Start with a complete lifecycle

Create two records with distinct names, edit one, remove the other, then close and reopen the app. Record whether the expected state returns. Repeat with an empty collection and with longer text.

## Observe network dependence

Follow the advertised offline flows with connectivity disabled. Note which features continue working and which display a clear explanation. Do not infer network behavior only from the absence of a login screen.

## Separate persistence from recovery

Data surviving an app restart does not demonstrate that a backup can restore it. If export or backup is advertised, save a sample export and test the documented restore procedure in a disposable environment.

## Document limits

Write down what was tested, the device and app versions, and what remains unknown. Avoid using your only copy of important data for experiments with resets, migration, or restoration.

---

Part of the [iOS source-code project guide](../README.md), maintained by [YXC Code](https://app.yxcit.com/en?utm_source=github&utm_medium=referral&utm_campaign=source_code_guide). Prepared with AI assistance.
