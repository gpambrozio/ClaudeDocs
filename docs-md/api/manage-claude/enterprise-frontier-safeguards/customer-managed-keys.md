# Customer Managed Keys

---
title: Use a customer-managed key
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/customer-managed-keys
description: Encrypt your data using a key you hold in your own key management service.
---

Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.

With a customer-managed key (CMEK), Anthropic encrypts your data using a key that you hold in your own key management service: AWS KMS, Google Cloud KMS, or Azure Key Vault. Within about an hour of [disabling your key](customer-managed-keys.md#revoke-your-key), Anthropic can no longer decrypt data your key protects.

In the Claude Console, you attach your key to each [workspace](../workspaces.md) that uses it, and get access through [Enterprise Frontier Safeguards](overview.md) (EFS) or [Enterprise Data Controls](overview.md#enterprise-data-controls).

## Before you attach a key

You need to be an Organization Admin to attach keys.

Your organization also needs access to customer-managed keys. To get access with EFS, follow the “Get access” section of [Set up Enterprise Frontier Safeguards on Claude Platform](setup-console.md#get-access). To get access without EFS, contact your Anthropic account team, as [Who can use CMEK](../cmek.md#availability) describes.

Attaching your first key turns on [Access Transparency](../access-transparency.md#access-transparency-with-customer-managed-keys) for your whole organization, unless it’s already on. You can’t turn it off. With Access Transparency on, your organization can’t [call the Claude API directly from a browser](../authentication.md#browser-based-applications).

A key turns off some features, and [attaching a key is permanent](customer-managed-keys.md#attach-a-customer-managed-key), so Anthropic recommends reading these parts of the customer-managed encryption keys guide first:

* [What changes with a key](../cmek-coverage-claude-platform.md#turned-off-or-changed): the features a key turns off.
* [What a key covers](../cmek-coverage-claude-platform.md#encrypted-with-your-key): what your key encrypts.
* [What revoking a key means](../cmek-key-lifecycle.md#what-each-action-does): what revoking or disabling your key does. You can’t undo deleting your key.

### If you use customer-owned storage

A workspace that uses both customer-owned storage and a customer-managed key has two separate keys:

| Key | Where it’s created | What it does |
| ----- | ----- | ----- |
| Your bucket’s key | With your bucket, when you [create the bucket and roles](external-storage.md#create-the-bucket-and-roles) | Encrypts your bucket. |
| Your customer-managed key | In your key management service, following the guides later on this page | Encrypts your data. It’s the key you attach to a workspace. |

Don’t use the same key for both. Which keys encrypt what’s in your bucket depends on the type of data:

* **Sealed Safety Data:** Anthropic encrypts the content under your customer-managed key before writing it to your bucket, and your storage service encrypts the stored object again under your bucket’s key. Once your customer-managed key stops working, Anthropic can’t decrypt that stored content, whatever happens to your bucket’s key.
* **Transcripts and Safety Cases:** Only your bucket’s key encrypts them.

## Attach a customer-managed key

Attaching a key is permanent. You can’t detach the key or swap it for a different one. Rotating the key material within the same key is supported. On Claude Platform, the workspace can’t switch to **Legacy ZDR**, and you create a new workspace to use a different key.

**Create and register your key**

Follow the guide for your key management service to create your key and register it with Anthropic, then come back here to attach it.

* [AWS KMS](../cmek-aws-kms.md)
* [Google Cloud KMS](../cmek-google-cloud-kms.md)
* [Azure Key Vault](../cmek-azure-key-vault.md)

**Attach your key**

Attach your key before the workspace serves traffic, because the key can take up to a day to take effect on a workspace that already does.

If the workspace will use customer-owned storage, first [connect a storage destination](external-storage.md) to your organization under **Storage destinations**. If it uses EFS, follow the steps in [Set up Enterprise Frontier Safeguards on Claude Platform](setup-console.md).

To attach your key, follow these steps for each workspace that will use it:

1. Go to the [Data retention](https://platform.claude.com/settings/privacy) page in the Claude Console and select the workspace at the top.
2. Select your key under **Encryption key** and save.

If the workspace uses Anthropic-managed storage, there’s nothing more to do.

To set up a key on Claude Platform on AWS, follow the steps in [Set up CMEK on Claude Platform on AWS](../cmek-claude-platform-on-aws.md).

To set up a key on Claude Models on Google Cloud (Anthropic managed), [open the Claude Console](setup-claude-models-on-google-cloud-anthropic-managed.md#before-you-begin) from the Google Cloud console. Then, follow the steps for your own key in [Add cloud resources](setup-claude-models-on-google-cloud-anthropic-managed.md#add-cloud-resources). You need `roles/claude.admin` instead of Organization Admin. You don’t need a bucket to use a key.

## Revoke your key

On Claude Platform, once your key has [taken effect](../cmek-how-it-works.md#when-your-key-takes-effect), requests to the workspace start failing up to an hour after you revoke or disable it. Within about an hour of disabling your key, Anthropic can no longer decrypt data your key protects. A small set of records [stays outside your key](../cmek-data-retention.md#limited-preservation-outside-your-key). Revoking or disabling your key doesn’t delete data or undo reads that have already happened.

Before you revoke your key, read [what revoking means and what can’t be undone](../cmek-key-lifecycle.md#what-each-action-does). For what happens to your requests and who’s told, see [If your key stops working](customer-managed-keys.md#if-your-key-stops-working).

## If your key stops working

The following table shows what happens on Claude Platform when a workspace can’t use your key, and what to do about it.

| Event | Requests | Your data | Who’s told | What to do |
| ----- | ----- | ----- | ----- | ----- |
| Your key is revoked or disabled | If your key has taken effect, requests can keep succeeding for up to an hour. After that, requests to the workspace fail. | Once your key stops working, Anthropic can’t decrypt what your key protects until you re-enable your key or restore Anthropic’s access to the key. You can’t undo deleting your key. | Anthropic usually emails the members of your organization who can manage encryption keys. On Claude Models on Google Cloud (Anthropic managed) and Claude Platform on AWS, Anthropic instead usually emails the person who completed your organization’s setup. | Re-enable your key, or restore Anthropic’s access to it. Requests that failed in the meantime aren’t retried, and retention periods keep running. See [what comes back when you re-enable a key](../cmek-key-lifecycle.md#restore-access). |
| Your key management service can’t be reached | Can keep succeeding for up to an hour. After that, requests to the workspace fail. On the Messages API, they return a [503 error with the code `cmek_key_unreachable`](../cmek-key-lifecycle.md#unreachable-key), and you can retry them. The Message Batches API retries them for you until your key is available or the batch expires. | What’s already stored is unchanged. Once your key stops working, Anthropic can’t decrypt what your key protects until your key management service can be reached again. Records Anthropic can’t encrypt during the outage aren’t kept. | No one. | Restore access to your key management service. |

If the workspace also uses customer-owned storage, see [If your bucket stops working](external-storage-manage.md#if-your-bucket-stops-working).

## Rotate or replace your key

You can rotate the key material within the same key without changing anything in the Claude Console.

On Claude Platform, to use a different key, create a new workspace with the new key and move your traffic to it, because [attaching a key is permanent](customer-managed-keys.md#attach-a-customer-managed-key).

## Next steps

**Set up Enterprise Frontier Safeguards on Claude Platform**

For a workspace on EFS, attach your key, then check your setup.

**Set up customer-owned storage**

Keep your Sealed Safety Data in storage in your own cloud account.

**Customer-managed encryption keys**

What a key covers, what it turns off, and what revoking it means.

---

*Copyright © Anthropic. All rights reserved.*
