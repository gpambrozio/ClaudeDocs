# Flagged Cases

---
title: Review Safety Cases
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases
description: How your team receives, investigates, and responds to the Safety Cases that Anthropic sends, and where to get help.
---

Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.

Automated safety monitoring checks your prompts and responses for signs of serious misuse, such as attempts to develop offensive cyber or biological capabilities. Enterprise Frontier Safeguards requires [Anthropic Human Review](human-review-and-access-transparency.md#turn-off-anthropic-human-review) to be off. With it off, a potential violation of Anthropic’s Usage Policy that automated safety monitoring finds can become a Safety Case that your own team reviews. Anthropic expects Safety Cases to be rare for most organizations.

## How Safety Case review works

1. **[Anthropic sends you a Safety Case](flagged-cases.md#where-cases-arrive).**
2. **[You review it](flagged-cases.md#read-a-case)** to see which messages it covers and what kind of risk it reports.
3. **[You investigate](flagged-cases.md#investigate)**, with your own logs and the Transcripts.
4. **[You respond](flagged-cases.md#respond-to-a-case)** to confirm that you investigated.
5. **[Anthropic closes the Safety Case](flagged-cases.md#after-you-respond).**

## Get Safety Cases

Safety Cases can reach you in two ways: as files in your own storage and through the API.

On Claude Platform, keep the [Compliance API](../compliance-api-access.md#set-up-the-compliance-api) on. A request that you send while it’s off has no Transcript in your [Case bucket](faq.md#glossary) or through the Safety Cases API. Without a Case bucket, you also get no Safety Cases while it’s off.

### In your own storage

Anthropic writes readable Safety Cases and Transcripts to a [bucket in your own cloud account](customer-owned-storage.md#what-is-stored). To select one:

1. Read [Transcripts and Safety Cases in your bucket](external-storage.md#case-and-transcript-bucket) before you select a bucket. Not every Amazon S3 bucket can receive Safety Cases.
2. For each workspace, select the bucket under **Safety Case and Transcript storage** in the Claude Console.

When Anthropic sends you a Safety Case, it adds [Safety Case files](safety-case-files.md) to your storage.

Two limits apply:

* You get Safety Case files only for a workspace that has a [safety data bucket](faq.md#glossary) (see [Set up customer-owned storage](external-storage.md)). That bucket holds Sealed Safety Data, which your team can’t read. You select it under **Sealed Safety Data storage**, which is a separate setting from **Safety Case and Transcript storage**.
* On Claude Platform, you also get Safety Case files only for messages that you send after the workspace starts using its safety data bucket.

### Through the API

The [Safety Cases API](safety-cases-api.md) serves the same Safety Cases over HTTP. It lets you read and respond to Safety Cases. It’s available only on Claude Platform. It is in beta.

Whether you also need a Case bucket depends on your platform:

* **Claude Platform:** You can also select a Case bucket for each workspace under **Safety Case and Transcript storage**. Without one, you get no Safety Cases for messages with a user profile.
* **Claude Models on Google Cloud (Anthropic managed) and Claude Platform on AWS:** Safety Cases can reach your team only through a Case bucket. Monitor that bucket, because the 7 days to respond start when Anthropic sends a Safety Case.

### How you know when a Safety Case is created

Anthropic doesn’t notify you automatically when it creates a Safety Case. Monitor your storage or [poll the API](safety-cases-api.md#poll) for Safety Cases, so that you can respond quickly. See [Alerts for new files](safety-case-files.md#alerts) for ways to send an alert to your SIEM or ticketing system based on storage updates.

## Review a Safety Case

### What a Safety Case includes

Each Safety Case includes:

* Its ID
* The policy category, such as `cyber` or `bio`
* The ID of each message, and where to find its Transcript
* The workspace that sent the messages, and sometimes the user profiles that sent them

In your bucket, a Safety Case is a JSON file. [Safety Case file](safety-case-files.md#safety-case-file) describes its fields.

Through the API, [list your Safety Cases](safety-cases-api.md#poll), then [read each message](safety-cases-api.md#read-a-message). The API also returns the user or API key that Anthropic recorded for a message.

### Investigate a Safety Case

Most Safety Cases come down to one of four outcomes:

| What you find | What to do |
| ----- | ----- |
| **Authorized work.** For example, your red team ran a penetration test under the Cyber Verification Program. | Confirm it with the team that owns the work. Respond with `no_violation`. |
| **An employee or user acting on their own, against policy.** They broke your policies or Anthropic’s Usage Policy without your organization’s approval. | Remove their access and follow your own process. Respond with `violation`. |
| **An external user or a stolen credential.** | Block the user or rotate the key. Respond with `violation`. |
| **A false positive.** Automated safety monitoring misread the intent or the content. | Nothing to fix. Respond with `no_violation`. |

Who you involve, including HR, legal, or a manager, is up to your own process.

Be careful when you put these Transcripts into Claude or another AI model. They can lead to another Safety Case.

## Respond to a Safety Case

Respond within 7 calendar days of the Safety Case’s `created_at`, the time when Anthropic sent it. By responding, you confirm that you have investigated and identified the cause and, if there was a violation, taken steps to ensure it does not happen again.

Your Safety Case Response says whether you found a violation. You don’t need to share names, evidence, or Transcripts with Anthropic. Any information you choose to share with Anthropic as part of your response becomes part of the Safety Case. A response closes the Safety Case, so you can’t change it or add to it later.

You can respond in either of two ways. Use one of them for each Safety Case, because Anthropic counts the first response.

### Option 1: Write a response file

Write a [response file](safety-case-files.md#response-file) to the bucket that holds your Safety Cases. Its path depends on your storage provider:

* **Amazon S3:** `review-responses/<case_id>.json`
* **Google Cloud Storage bucket connected in the Claude Console:** `<organization ID>/review-responses/<case_id>.json`

Check the file against [Rules for a valid file](safety-case-files.md#response-file-rules), because only a valid file counts.

### Option 2: Respond through the API

Send one request to [respond to the Safety Case](safety-cases-api.md#respond).

### After you respond

When Anthropic reads a valid response, it closes the Safety Case. A close reason of `responded` confirms that Anthropic has received your response. Through the API, the Safety Case closes at once. If a Safety Case is still open a day after you wrote a file, see [Why a Safety Case stays open](safety-case-files.md#still-open).

If Anthropic needs more information from you about your response, it sends a Safety Notice (see [Poll for Safety Notices](safety-cases-api.md#poll-for-notices)), or your Anthropic account team contacts you.

## If Anthropic takes action

Enterprise Frontier Safeguards doesn’t change Anthropic’s [Usage Policy](https://www.anthropic.com/legal/aup) or the standard for enforcing it. Anthropic reserves enforcement for clear, intentional harm.

### If you don’t respond

Responding promptly can help keep your account in good standing. If 7 calendar days pass with no valid response, Anthropic closes the Safety Case. If a Safety Case stays unanswered, Anthropic may suspend access.

### If Anthropic suspends access

In the rare case that automated safety monitoring finds clear, intentional harm, Anthropic can suspend access to limit further harm while you investigate. A suspension can be as narrow as one user or user profile. The Safety Case can name the user profile if you send one. To ask for access back, contact your Anthropic account team. If the Safety Case is open, also respond to it. While your whole organization is suspended, the Safety Cases API refuses your key.

## Best practices

* **Log message IDs.** To trace a message to its sender, Anthropic recommends logging the `id` (`msg_...`) of each Messages API response with your own user ID. It often makes sense to start on this early, because your logs only cover requests from then on. You can also set `metadata.user_id` to an opaque ID, which comes back in the Transcript.
* **Save the Transcripts you need.** Transcripts expire (see [What’s in the bucket](safety-case-files.md#whats-in-the-bucket)).

## Reach out for help

Your Anthropic account team is your contact for Safety Cases. Quote the Safety Case’s ID so that Anthropic can find the right Safety Case. You do not need to quote or provide a Transcript.

With no Anthropic Human Review, the people at Anthropic who handle a Safety Case see limited details, such as its ID, its category, and any proposed action. They can’t read your Transcripts.

* **You need more time:** Tell your Anthropic account team before the 7 days end. The Safety Case still closes on time.
* **You think a Safety Case is wrong:** Respond with `no_violation`.

## Questions and troubleshooting

**Does your team need 24/7 coverage?**

Anthropic doesn’t ask for 24/7 coverage for Safety Cases. Anthropic expects them to be rare, and you have days, not hours, to respond. Send alerts to a queue that someone checks every working day.

**Can you test the process before a real Safety Case arrives?**

Ask your Anthropic account team whether a test Safety Case is available for your organization.

**Does Anthropic send webhooks for Safety Cases?**

No. [Monitor your bucket](flagged-cases.md#set-up-alerts) or [poll the Safety Cases API](safety-cases-api.md#poll) instead.

**Who reviews when Anthropic Human Review is on?**

A small, specialized team at Anthropic can review what automated safety monitoring finds. You can keep Anthropic Human Review on only for a workspace on Anthropic-managed storage. Enterprise Frontier Safeguards requires it to be off.

## Next steps

**Check your setup**

On Claude Platform, check that your setup works before you start production use.

**Set up customer-owned storage**

Keep your Sealed Safety Data in storage in your own cloud account.

**Human Review and Access Transparency**

See who at Anthropic reviews your data, and what record you get.

---

*Copyright © Anthropic. All rights reserved.*
