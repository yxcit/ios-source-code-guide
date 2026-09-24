# iOS source-code project guide

[简体中文指南](README.zh-CN.md)

A practical guide to evaluating an iOS source-code package before you build on it.

Maintained by **YXC Code**, a commercial app source-code store. This is a free educational resource; it contains no paid application source. Explore the [YXC Code catalog](https://app.yxcit.com/en?utm_source=github&utm_medium=referral&utm_campaign=source_code_guide).

## Start with evidence

A polished screenshot proves that an interface was captured. It does not establish that the delivered project builds on your machine, includes every asset, or works without a seller's private service. Evaluate those separately.

| Question | Evidence to request | What to record |
|---|---|---|
| Can I build it? | Exact Xcode version, deployment target, dependency instructions | A clean build using a fresh copy |
| What is included? | File inventory, documentation, assets, backend requirements | Included versus separately purchased components |
| What can I change? | A small customization walkthrough | Where branding, sample data and configuration live |
| What happens to data? | Storage and backup explanation | Local/cloud storage, export and restore behavior |
| What may I ship? | The actual package license and third-party notices | Permitted uses and redistribution limits |
| What happens after purchase? | Support scope and update policy | Contact method, supported versions and response expectations |

## Before purchase

- Compare the feature list with the screenshots and demo. Ask about anything that appears in one but not the other.
- Ask for the supported Xcode and iOS versions, dependency manager, and any required service accounts.
- Separate an app's App Store listing from the source-code package. Confirm which source version is delivered.
- Check whether images, fonts, sample data and other assets are included for your intended use.
- Read the actual usage terms. Do not assume that purchasing a package transfers the original app listing or permits reselling its source.
- Record the download window and keep a copy of the package and purchase documentation.

## First run

Keep an untouched copy of the delivered archive. Read its setup instructions before running installation scripts. Follow the documented build procedure and note any required credentials or external services.

Test a complete user flow: create a record, edit it, close and reopen the app, then confirm the record remains. For an app that advertises backup support, test both export and restore using disposable data.

Use your own signing configuration and service accounts for your product. A successful local build is a useful milestone, not a guarantee of acceptance by any app store.

## A reusable evaluation note

Copy [EVALUATION.md](EVALUATION.md) for each package. Record observations rather than marking a feature as verified solely because it appears in marketing copy.

## Guides

<!-- guides:start -->
- [A clean first-build checklist](articles/first-build-checklist.md)
<!-- guides:end -->

## Contributing

Suggestions that make the checklist more concrete are welcome. Describe the problem and the evidence that would help evaluate it. Please do not post account credentials, customer data or paid source archives in issues.

## About this resource

The guide is maintained by the team behind [YXC Code](https://app.yxcit.com/en?utm_source=github&utm_medium=referral&utm_campaign=source_code_guide). Content was prepared with AI assistance. It is general evaluation guidance, not a claim that every product in our catalog has passed every check.

Unless otherwise stated, the original text and templates in this repository are available under the MIT license in [LICENSE](LICENSE). That license does not apply to products sold through the store.
