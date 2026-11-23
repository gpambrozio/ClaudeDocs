# Overview

---
title: Enterprise Frontier Safeguards
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview
description: Zero Data Retention (ZDR) for eligible organizations that use Claude's most capable models, with Sealed Safety Data in your own cloud account.
---

Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.

Enterprise Frontier Safeguards (EFS) is [Zero Data Retention (ZDR)](../api-and-data-retention.md#zero-data-retention-zdr-scope) for eligible organizations that use [Claude’s most capable models](../api-and-data-retention.md#model-specific-data-retention-requirements), such as Claude Fable 5.1. Anthropic doesn’t retain your prompts and responses. Sealed Safety Data is written to storage that you own. EFS requires your own bucket. A workspace on [Anthropic-managed storage](faq.md#glossary) isn’t on EFS, because Anthropic stores encrypted copies of that workspace’s prompts and responses.

Use EFS when you want Claude’s most capable models but need to keep your Sealed Safety Data in your own cloud account. With EFS, people at your organization, not reviewers at Anthropic, review [Safety Cases](flagged-cases.md). EFS includes both:

* [Customer-owned storage](customer-owned-storage.md): A bucket that receives your Sealed Safety Data (prompts, responses, and model reasoning, encrypted in Anthropic’s format). Your team can’t read Sealed Safety Data, even in your own bucket.
* [Your team reviews Safety Cases](flagged-cases.md): Anthropic Human Review is always off, so your own team reviews flagged cases that automated safety monitoring finds.

![EFS, Anthropic managed, and Legacy ZDR compared. Enterprise Data Controls covers review and the key on Anthropic managed.](https://platform.claude.com/docs/images/efs-how-it-works-enterprise-data-controls.svg)

Anthropic doesn’t charge for EFS, and EFS doesn’t change model behavior, API pricing, or rate limits. Your cloud provider bills you for that storage as usual, including reads, writes, and data egress.

EFS covers requests to the Messages API in a workspace configured for EFS regardless of model. It does not cover data that is stored by Claude Platform features for their own use, even within a Messages API request, such as code execution containers, Files API uploads, Batch API results, and Claude Managed Agents sessions. See [Data and retention](faq.md#data-and-retention) in the FAQ.

## On Claude Platform, EFS applies to a whole workspace

Once EFS takes effect for a workspace, it applies to every request to every model in that workspace, including models that don’t require data retention.

To use EFS for only some traffic, use separate workspaces. The [API key](../workspaces.md#api-keys-and-resource-scoping) or workspace ID that you send determines which card a request uses. A new workspace leaves your existing workspaces and their API keys as they are.

## Enterprise Data Controls

On Claude Platform, accepting the [EFS and Enterprise Data Controls terms](setup-console.md#get-access) gives you both. With Enterprise Data Controls, you can [use a customer-managed key](customer-managed-keys.md) or [turn off Anthropic Human Review](human-review-and-access-transparency.md#turn-off-anthropic-human-review) on Anthropic-managed storage. With either one, [Access Transparency](human-review-and-access-transparency.md#check-access-transparency) is on for your organization.

## See also

**Set up customer-owned storage**

Keep your Sealed Safety Data in storage in your own cloud account.

**Review Safety Cases**

Receive, investigate, and respond to the Safety Cases that Anthropic sends.

**Use a customer-managed key**

Encrypt your data using a key you hold in your own key management service, with EFS or with Anthropic-managed storage.

## Next steps

**Setup guide**

Get access and set up EFS on the platform you use.

**Enterprise Frontier Safeguards FAQ**

Answers to common questions about EFS.

---

*Copyright © Anthropic. All rights reserved.*
