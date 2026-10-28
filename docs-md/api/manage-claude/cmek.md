# Cmek

---
title: Customer-managed encryption keys
url: https://platform.claude.com/docs/en/manage-claude/cmek
description: Use a key you hold in your own cloud to encrypt data that Claude stores.
---

Ask Claude Code about this feature

```text
/claude-api tell me about customer-managed encryption keys
```

With customer-managed encryption keys (CMEK), you create a key in your own AWS KMS, Google Cloud KMS, or Azure Key Vault. Anthropic uses it to encrypt certain data at rest. The key stays under your control, so you can rotate it, audit its use, and remove Anthropic’s access.

## Choose your setup page

Choose the service that holds your key. Claude Platform on AWS, which also uses AWS KMS, has its own page.

**AWS KMS**

For Claude Platform and Claude Enterprise.

**Google Cloud KMS**

For Claude Platform and Claude Enterprise.

**Azure Key Vault**

For Claude Platform and Claude Enterprise.

**Claude Platform on AWS**

For organizations whose Claude Console sidebar shows **Account managed by AWS**.

On Claude Platform, you can also add and attach your key [with the Admin API](cmek-admin-api.md).

## Understand CMEK before you set it up

Which product you use decides what your key encrypts, what stays under Anthropic’s key, and which features turn off or change.

**How CMEK works**

How your key protects data, when it takes effect, and what you can see.

**CMEK, data retention, and ZDR**

Using a key with zero data retention (ZDR), and what Anthropic can preserve outside your key.

**What CMEK covers on Claude Platform**

Look up a feature or a kind of data.

**What CMEK covers on Claude Enterprise**

Look up a feature, and see what your users will notice.

## What you commit to

* Once you attach a key, you [can’t remove or replace it](cmek-key-lifecycle.md#what-each-action-does).
* Your key protects only data written [after it takes effect](cmek-how-it-works.md#when-your-key-takes-effect).
* If your key is deleted, Anthropic can’t recover the data it protects. [While the key is disabled](cmek-key-lifecycle.md#restore-access), Claude can’t read that data.
* On Claude Platform, a workspace with a key [must retain data](cmek-data-retention.md#data-retention).

## Who can use CMEK

CMEK is optional. To turn it on for an eligible organization, contact your Anthropic account team. You need one of these roles to set it up:

* Claude Platform: Organization Admin
* Claude Platform on AWS: Admin
* Claude Enterprise: Owner or Primary Owner

## After setup

* [What happens when you rotate, disable, or delete your encryption key](cmek-key-lifecycle.md)
* [Troubleshoot CMEK](cmek-troubleshooting.md)

---

*Copyright © Anthropic. All rights reserved.*
