# A clean first-build checklist

Start by separating three questions: whether the delivered project is complete, whether your environment matches its requirements, and whether its runtime behavior fits your needs.

## Preserve the original

Keep the downloaded archive unchanged and work from a separate copy. Record the version and download date. This makes it possible to distinguish a delivery problem from a later customization.

## Reproduce the documented environment

Check the Xcode version, iOS deployment target, dependency instructions, and any required configuration files. Open the workspace or project specified in the documentation. If dependencies cannot be resolved, preserve the first useful error message before attempting unrelated upgrades.

Avoid changing several toolchain or dependency versions at once. A successful build after multiple simultaneous changes can be difficult to reproduce.

## Use disposable data

Build for a supported simulator or test device. Follow one ordinary user flow from beginning to end: create an item, edit it, leave the screen, relaunch the app, and confirm the expected state. Use sample data while you learn where the app stores information.

## Record what remains unverified

A build is not a complete acceptance test. Networking, notifications, purchases, device-only features and backups may need separate checks. Write those down instead of treating a launch screen as proof that every feature works.

Use the [evaluation template](../EVALUATION.md) to keep these findings together.
