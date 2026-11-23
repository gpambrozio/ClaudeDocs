# Faq

---
title: Enterprise Frontier Safeguards FAQ
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq
description: Short answers to common questions about Enterprise Frontier Safeguards, with links to the details.
---

Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.

To set up [Enterprise Frontier Safeguards](overview.md) (EFS), see [Setup guide](setup-console.md).

## Data and retention

**What is Enterprise Frontier Safeguards (EFS)?**

[Enterprise Frontier Safeguards](overview.md) (EFS) is Zero Data Retention (ZDR) for eligible organizations that use [Claude’s most capable models](../api-and-data-retention.md#model-specific-data-retention-requirements). Anthropic doesn’t retain your prompts and responses. Sealed Safety Data is written to storage that you own. EFS includes both [customer-owned storage](external-storage.md) and [review of Safety Cases](flagged-cases.md) by people at your organization. A workspace that uses [Anthropic-managed storage](faq.md#glossary) isn’t on EFS, because Anthropic stores encrypted copies of that workspace’s prompts and responses.

**What is the difference between Enterprise Data Controls and EFS?**

The main difference is where your Sealed Safety Data is stored. With EFS, it’s written to storage that you own, so EFS is Zero Data Retention (ZDR). With [Enterprise Data Controls](overview.md#enterprise-data-controls), a workspace stays on Anthropic-managed storage. On Claude Platform, you can still [use a customer-managed key](customer-managed-keys.md) and [turn off Anthropic Human Review](human-review-and-access-transparency.md#turn-off-anthropic-human-review) for additional control over your data.

**Does EFS apply only to models that require data retention?**

No. On Claude Platform, EFS applies to every request to every model in a workspace where you enable EFS. That includes models that don’t require data retention. One workspace can’t use EFS for some models and not for others. To use EFS for only some traffic, [use separate workspaces](overview.md#workspace-scope) and choose the workspace by API key or workspace ID.

**Do I have to turn on EFS for my whole organization?**

No. On Claude Platform, getting access to EFS doesn’t turn EFS on for any workspace. Selecting EFS for one workspace doesn’t change your other workspaces. Access Transparency is an exception: once it’s on, it’s on for your whole organization, and you can’t turn it off. See [Check Access Transparency](human-review-and-access-transparency.md#check-access-transparency). If your organization has a Legacy ZDR arrangement, workspaces on **Legacy ZDR** stay there. To use EFS, create a new workspace and use it instead of your Legacy ZDR workspace.

A request from a workspace on **Legacy ZDR** to a model that [requires 30-day data retention](../api-and-data-retention.md#model-specific-data-retention-requirements) fails with a 400 error unless Anthropic has authorized your organization to use it under Legacy ZDR. Send those requests from a workspace that uses EFS or Anthropic-managed storage instead.

**What data does EFS cover?**

EFS covers requests to the Messages API in a workspace configured for EFS regardless of model. It does not cover data that is stored by Claude Platform features for their own use, even within a Messages API request, such as code execution containers, Files API uploads, Batch API results, and Claude Managed Agents sessions. See [API and data retention](../api-and-data-retention.md#feature-eligibility) for each feature.

EFS applies from the time the configuration takes effect. Data written earlier remains where it was written until it expires.

**Does EFS support the Batch API?**

No, because the [Batch API](../../build-with-claude/batch-processing.md) keeps no Transcript for your team to review. Send each request on its own through the Messages API instead, or send batches from a workspace that isn’t on EFS and has Anthropic Human Review on.

**Does EFS support Anthropic’s Claude Managed Agents service?**

No. Every workspace on EFS has [Anthropic Human Review](human-review-and-access-transparency.md#turn-off-anthropic-human-review) off. Anthropic’s Claude Managed Agents service doesn’t run sessions or [dreams](../../managed-agents/dreams.md) in a workspace with Anthropic Human Review off. A session that already exists in such a workspace stops accepting new messages. To run sessions or dreams, create them in a workspace that has Anthropic Human Review on.

**Does EFS apply to traffic from before I set it up?**

No. EFS applies once your setup takes effect. See [How long changes take](faq.md#how-long-changes-take).

**Does Anthropic train on my data?**

Anthropic does not train Claude models on enterprise data without explicit permission.

## Access and review

**Who at Anthropic reviews my data?**

Automated safety monitoring checks your traffic, and no person sees your content at that step. With EFS, Anthropic Human Review is always off. On Anthropic-managed storage, with Anthropic Human Review on, a small, specialized team at Anthropic can review what automated safety monitoring finds. See [when automated safety monitoring accesses your data](human-review-and-access-transparency.md#who-at-anthropic-can-access-your-data).

**How do I know if Anthropic personnel access my data?**

Access Transparency records access to your data by Anthropic personnel, for everything [Access Transparency covers](../access-transparency.md#what-access-transparency-covers). On Claude Platform, it has no record for data in customer-owned storage. See [Check Access Transparency](human-review-and-access-transparency.md#check-access-transparency).

**Can I add my own classifiers?**

No. Anthropic’s automated safety monitoring checks your traffic.

## Storage and keys

**Which cloud providers does customer-owned storage support?**

Your bucket’s provider depends on where you use Claude:

* **Claude Platform:** Amazon S3 or Google Cloud Storage.
* **[Claude Platform on AWS](../../build-with-claude/claude-platform-on-aws.md):** Amazon S3.
* **[Claude Models on Google Cloud (Anthropic managed)](../../build-with-claude/claude-models-on-google-cloud/anthropic-managed.md):** Google Cloud Storage.

See [Set up customer-owned storage](external-storage.md) or [Set up customer-owned storage on Google Cloud Storage](external-storage.md#google-cloud-storage).

**Can I change what’s in my bucket?**

Only to write your team’s [response files](safety-case-files.md#response-file), if your bucket receives [Safety Cases](faq.md#glossary). Don’t write anything else to your bucket, and leave the rest of its contents as they are. For an Amazon S3 bucket, see [Give your team access to the bucket](external-storage.md#let-your-team-read-the-bucket) and [What removes data from your bucket](external-storage-manage.md#what-removes-data).

**Can several Anthropic organizations share an AWS account?**

Yes. See [Create and connect your bucket](external-storage.md#create-the-bucket-and-roles).

Each organization needs a bucket of its own, with [its own KMS key](customer-managed-keys.md#if-you-use-your-own-bucket), and using a bucket [ties it to one organization](external-storage.md#before-you-begin).

**Can I connect more than one bucket in the same AWS account?**

Yes. Each bucket needs its own CloudFormation stack or its own Terraform folder. See [Create and connect your bucket](external-storage.md#create-the-bucket-and-roles).

**Can each workspace use its own bucket?**

On Claude Platform and Claude Platform on AWS, yes. Select each workspace’s bucket in the Claude Console. For Google Cloud Storage, talk to your Anthropic account team first, because [Anthropic limits the number of buckets and workspaces](external-storage.md#gcs-use-your-bucket-in-a-workspace).

**Can I keep Transcripts and Safety Cases in a different bucket from my Sealed Safety Data?**

Plan on one bucket for both. If a workspace uses both [**Sealed Safety Data storage** and **Safety Case and Transcript storage**](customer-owned-storage.md#the-two-storage-settings), select the same bucket for each. If you select a different bucket, it might not receive Transcripts and Safety Cases, even if the save succeeds. See [Transcripts and Safety Cases in your bucket](external-storage.md#case-and-transcript-bucket).

**What happens to my data if I stop using customer-owned storage?**

EFS requires customer-owned storage, so a workspace that stops using it leaves EFS. For what happens to your data and the order of the steps, see [Change or stop using your bucket](external-storage-manage.md#change-or-stop-using-your-bucket).

After you [stop using a bucket](external-storage-manage.md#change-or-stop-using-your-bucket), [delete its storage destination](external-storage-manage.md#delete-a-storage-destination) if you can. If you can’t, talk to your Anthropic account team before you remove Anthropic’s access to the bucket. This applies even once everything in it is past the retention period.

**What changes when I attach a customer-managed key?**

[Attaching a key](customer-managed-keys.md#attach-a-customer-managed-key) turns off some features and is permanent. First, check [what’s turned off](../cmek-coverage-claude-platform.md#turned-off-or-changed) and read [Before you attach a key](customer-managed-keys.md#before-you-attach-a-key).

## EFS on Claude Platform on AWS

To set up EFS on Claude Platform on AWS, follow [Set up Enterprise Frontier Safeguards on Claude Platform on AWS](setup-claude-platform-on-aws.md). Customer-managed encryption keys are available there with AWS KMS.

## EFS on Claude Models on Google Cloud (Anthropic managed)

To set up EFS on [Claude Models on Google Cloud (Anthropic managed)](../../build-with-claude/claude-models-on-google-cloud/anthropic-managed.md), follow [Set up Enterprise Frontier Safeguards on Claude Models on Google Cloud (Anthropic managed)](setup-claude-models-on-google-cloud-anthropic-managed.md). Your bucket is in Google Cloud Storage, and your customer-managed encryption keys are in Google Cloud KMS. For the keys, see [Set up CMEK with Google Cloud KMS](../cmek-google-cloud-kms.md).

## If your key or bucket stops working

On Claude Platform, if your key is revoked or disabled after [it has taken effect](../cmek-how-it-works.md#when-your-key-takes-effect), requests can keep succeeding for up to an hour. After that, requests to the workspace fail. To recover, see [If your key stops working](customer-managed-keys.md#if-your-key-stops-working).

If Anthropic can’t write to your bucket, see [If your bucket stops working](external-storage-manage.md#if-your-bucket-stops-working). For a Google Cloud Storage bucket, see [If your Cloud Storage bucket stops working](external-storage.md#gcs-if-your-bucket-stops-working).

## How long changes take

Plan your checks and your move to production around these times:

| Change | How long it takes |
| ----- | ----- |
| A new workspace, or one that uses Anthropic-managed storage, [starts using customer-owned storage](external-storage.md#how-long-changes-take) | Usually within 10 minutes, but it can take longer. Once the first new object arrives in your bucket, wait 10 more minutes. |
| [Access Transparency starts recording](human-review-and-access-transparency.md#check-access-transparency) after it turns on | Within 2 hours |
| An Access Transparency event arrives in your Activity Feed | Within 2 business days of the access it records |
| A [customer-managed key](customer-managed-keys.md#attach-a-customer-managed-key) takes effect on a workspace that already serves traffic | Up to a day |
| A change to [Anthropic Human Review](human-review-and-access-transparency.md#turn-off-anthropic-human-review) applies | Up to 2 hours |

## Glossary

| Term | Meaning |
| ----- | ----- |
| Claude Platform | The Claude API, set up in the Claude Console. |
| Automated safety monitoring | Automated systems that look for patterns of misuse across many requests. With EFS, they analyze data stored in your cloud account, and your team reviews any findings. |
| Sealed Safety Data | Prompts, responses, and model reasoning, encrypted in Anthropic’s format. Your team can’t read it, even in your own bucket. See [What’s stored, and where](customer-owned-storage.md#what-is-stored). |
| Transcript | A readable copy of a prompt and response, for your team to read. |
| Safety Correspondence | Safety Cases, Safety Notices, and your Safety Case Responses. Never prompts and responses. |
| Safety data bucket | The bucket in your own cloud account that a workspace uses for Sealed Safety Data. You select it under **Sealed Safety Data storage** on the workspace’s [Data retention](https://platform.claude.com/settings/privacy) page. EFS requires one. |
| Case bucket | The bucket where Anthropic sends a workspace’s Transcripts and Safety Cases, in a form that your team can read. You select it under [**Safety Case and Transcript storage**](customer-owned-storage.md#the-two-storage-settings). EFS requires one on Claude Models on Google Cloud (Anthropic managed) and Claude Platform on AWS. One bucket can be both the Safety data bucket and the Case bucket, so plan to use one for both. |
| Legacy ZDR | [ZDR](../api-and-data-retention.md) with real-time safeguards but without automated safety monitoring. Anthropic doesn’t store prompts or responses after the API response is returned, except where needed to comply with law or combat misuse. |
| Anthropic-managed storage | Storage that Anthropic runs, used by workspaces on the **Anthropic managed** card. |
| Anthropic managed | A card in the Claude Console for workspaces that use Anthropic-managed storage. It’s the default for the Claude models that [require 30-day data retention](../api-and-data-retention.md#model-specific-data-retention-requirements). |
| Enterprise Data Controls | A set of features for EFS eligible workspaces that use Anthropic-managed storage instead of EFS. You can use a customer-managed key (CMEK) and, on Claude Platform, turn off Anthropic Human Review. Anthropic still stores your Sealed Safety Data, so this setup isn’t EFS and isn’t ZDR. See [Enterprise Data Controls](overview.md#enterprise-data-controls). |
| Customer-owned storage | Storing your Sealed Safety Data in a bucket in your own cloud account. See [Set up customer-owned storage](external-storage.md) or [Set up customer-owned storage on Google Cloud Storage](external-storage.md#google-cloud-storage). |
| Customer-managed key | An encryption key in your own key management service that encrypts your data. Also called CMEK. See [Use a customer-managed key](customer-managed-keys.md). |
| Human Review | Also called Anthropic Human Review. On Claude Platform with Anthropic-managed storage, if the Claude Console shows **Who reviews flagged cases?**, **Anthropic** turns it on and **My organization** turns it off. With it on, a small, specialized team at Anthropic can review what automated safety monitoring finds. With EFS, it’s always off. See [where you can turn off Anthropic Human Review](human-review-and-access-transparency.md#turn-off-anthropic-human-review). |
| Access Transparency | A record, through the Compliance API, of access to your data by Anthropic personnel, for everything [Access Transparency covers](../access-transparency.md#what-access-transparency-covers). |
| Safety Case | A record that Anthropic may open when automated safety monitoring finds a potential violation of Anthropic’s Usage Policy in a workspace without Anthropic Human Review. It lists the related Transcripts by identifier. [Review Safety Cases](flagged-cases.md) says which workspaces get one. |
| Storage destination | A bucket that you connect under **Storage destinations** on the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console. You select one for a workspace under **Sealed Safety Data storage** or **Safety Case and Transcript storage**. |
| Anthropic-managed key | The key Anthropic uses to encrypt your data when you don’t attach your own. |

## Reference

For API details, see [Customer-managed keys in the Admin API](../../api/organization/external_keys.md), the [Compliance API](../compliance-api.md), and [Access Transparency](../access-transparency.md).

---

*Copyright © Anthropic. All rights reserved.*
