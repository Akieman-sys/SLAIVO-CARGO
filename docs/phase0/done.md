# DONE CRITERIA — PHASE 0

## 1. Phase 0 Goal

Phase 0 is complete when SLAIVO has a clear engineering contract for V1.

No code should start before these rules are clear.

---

## 2. Completed Documents

The following files must exist:

- docs/phase0/source-of-truth.md
- docs/phase0/icp.md
- docs/phase0/wedge.md
- docs/phase0/scope.md
- docs/phase0/data-model.md
- docs/spec/status-machine.md
- docs/phase0/test-plan.md
- docs/phase0/done.md

---

## 3. Product Clarity

We can explain clearly:

- who uses SLAIVO
- who pays for SLAIVO
- what V1 does
- what V1 refuses
- why WhatsApp is the first channel
- why dossier is the source of truth
- why manager validation is required
- why partial intake is allowed
- why payment can block dispatch
- why AI must not invent agency information

---

## 4. Engineering Clarity

We know the core entities:

- client
- dossier
- shipment
- payment
- pricing rule
- agency knowledge
- manager action
- relance

We know the core flow:

Client message
→ client
→ dossier
→ qualification
→ shipment
→ pricing
→ payment
→ validation
→ tracking
→ relance

---

## 5. V1 Guardrails

V1 must not include:

- TikTok
- Gmail
- automated client payments
- advanced AI
- microservices
- Kubernetes
- advanced analytics
- mobile app

---

## 6. Safety Rules

The system must guarantee:

- no message without dossier
- no shipment without dossier
- no tracking before manager validation
- no dispatch if payment is blocking
- no AI invention for prices, addresses, schedules, or status
- no relance spam
- all critical manager actions are logged

---

## 7. Exit Criteria

Phase 0 is DONE if:

- all required docs are written
- the V1 scope is clear
- the data model is clear
- the status machine is clear
- test scenarios are defined
- we can now create the database schema
- we can now start backend implementation

---

## 8. Decision

PHASE 0 IS COMPLETE.

Next phase:

PHASE 1 — Core WhatsApp + Dossier Engine