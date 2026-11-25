# Overview

---
title: Claude Platform OAuth
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/overview
description: Where to start with Claude Platform OAuth and Linked billing, and how a customer's approval reaches your back end.
---

Claude Platform OAuth is a Beta Service: prerelease software provided under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Endpoints, parameters, and behavior can change during the beta. It might not be suitable for production use.

Claude Platform OAuth is how a customer approves your product to use their Claude organization. It powers [Linked billing](linked-billing.md), which lets your customers pay for the Claude usage in your product through their own Claude organization. To call Claude for your own product with your organization’s credentials, you don’t need an OAuth app: see [Authentication](../authentication.md).

To offer Linked billing, you need an OAuth app and an [identity provider](overview.md#no-client-secret) that issues tokens to your back end. Your customers need a Claude organization that pays Anthropic directly: see [Eligible customers](linked-billing.md#eligible-customers).

## How it works

A customer approves your app once. That creates a connection, which ties their Claude organization to your app until they or you end it.

A user at your customer’s company clicks the [Link your Claude organization button](linked-billing/link-button.md) in your product. Your back end sends them to Claude’s approval page on `auth.claude.com`. If they have the Admin or Billing role in the customer’s organization, they approve your app, and the browser comes back with a one-time code. Your back end exchanges the code for the connection’s ID and OAuth tokens. After that, Anthropic can bill the customer’s organization for requests that your back end makes for them.

![Sequence diagram: the person approves your app at auth.claude.com, then your back end exchanges the one-time code](https://platform.claude.com/docs/images/linked-billing-round-trip.svg)

Someone without either role can’t approve: see [What your customers see](linked-billing/what-your-customers-see.md#approving-the-link). If you know OAuth, this is the authorization code flow with PKCE.

### Your OAuth app

Your OAuth app is your product’s registration with Anthropic. An Admin of your Claude organization creates it in the Claude Console, and it gives your product a client ID. On the approval page, customers see its name, its logo, and what it asks for.

### An identity provider instead of a client secret

Every request that your back end sends to `auth.claude.com` carries a token from your identity provider, through [Workload Identity Federation](../workload-identity-federation.md). Anthropic doesn’t issue client secrets for OAuth apps. Any OpenID Connect issuer works, and there are [guides for common identity providers](../workload-identity-federation.md#identity-providers).

## Choose your path

Start with the task you have now. To build an integration, [set up your app](linked-billing/set-up-your-app.md), [link and bill a test customer](linked-billing/link-and-bill-a-customer.md), and then [test and publish your app](linked-billing/test-and-publish.md). Until your app is live, only its test users can link it, so first [add your test customer’s approver](linked-billing/test-and-publish.md#add-test-users).

**Linked billing**

Decide whether Linked billing fits your product and your customers

**Set up your app for Linked billing**

Register your app, then go on to link and bill a customer

**Manage linked customers**

Support a linked customer, check whether they’re still linked, or link them again

**Linked billing errors**

Fix an error that linking or billing returns

**What your customers see**

For product and support teams: the approval page, spend caps, and emails that your customers see

**OAuth endpoints and parameters**

Look up an exact endpoint, parameter, scope, OAuth token field, or error

---

*Copyright © Anthropic. All rights reserved.*
