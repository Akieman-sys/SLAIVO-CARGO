# TEST PLAN — SLAIVO CARGO OS

---

# 1. OBJECTIVE

Validate that SLAIVO works in real agency scenarios.

---

# 2. CORE SCENARIOS

---

## 2.1 New WhatsApp Client

Input:

"Hello, I want to ship from China"

Expected:

- client created
- dossier created
- intent detected
- system asks for missing info

---

## 2.2 Partial Intake

Input:

"Send from China"

Expected:

- dossier = PARTIAL
- missing fields identified
- system asks:

  - destination
  - goods type
  - weight/volume

---

## 2.3 Guided Conversation

Input:

Client gives info step by step

Expected:

- system updates dossier progressively
- no duplicate dossier
- missing fields reduce

---

## 2.4 Manual Client (Office)

Action:

Manager creates client manually

Expected:

- client exists without WhatsApp
- dossier linked correctly

---

## 2.5 Transitaire Flow

Input:

"I want to buy from China"

Expected:

- case_type = TRANSITAIRE
- system asks supplier info
- waits for supplier deposit
- manager confirms

---

## 2.6 Supplier Deposit

Action:

Manager confirms supplier delivered

Expected:

- shipment state = RECEIVED_AT_ORIGIN
- photos can be added

---

## 2.7 Weight Unknown

Input:

Client does not know weight

Expected:

- dossier still created
- shipment weight_status = UNKNOWN
- system does NOT block

---

## 2.8 Manager Weighs Package

Action:

Manager sets weight

Expected:

- weight_status = VERIFIED
- shipment updated

---

## 2.9 Pricing Calculation

Action:

Manager or system calculates price

Expected:

- price stored
- balance_due updated

---

## 2.10 Payment Partial

Action:

Manager records partial payment

Expected:

- fees_paid updated
- balance_due correct

---

## 2.11 Payment Blocking

Condition:

balance_due > 0

Expected:

- shipment cannot move to DISPATCHED

---

## 2.12 Manager Validation

Action:

Manager validates shipment

Expected:

- validation_status = VALIDATED
- tracking can now be sent

---

## 2.13 Tracking Sent

Expected:

- tracking sent ONLY after validation
- never before

---

## 2.14 Shipment Progression

Expected:

States move correctly:

- CREATED
- RECEIVED
- WEIGHED
- PRICED
- DISPATCHED
- IN_TRANSIT
- ARRIVED

---

## 2.15 Arrival Relance

Event:

ARRIVED_DESTINATION

Expected:

- message sent
- pickup reminder scheduled

---

## 2.16 Pickup Relance

Event:

READY_FOR_PICKUP

Expected:

- message sent
- no spam duplication

---

## 2.17 Relance Stop

Condition:

Client replies before relance

Expected:

- relance marked as SATISFIED
- not sent again

---

## 2.18 Balance Relance

Condition:

balance_due > 0

Expected:

- reminder sent
- not spammed

---

## 2.19 Unknown Intent

Input:

unclear message

Expected:

- system does NOT invent answer
- escalation triggered

---

## 2.20 Manager Override

Action:

Manager corrects:

- price
- weight
- status

Expected:

- change applied
- audit recorded

---

# 3. FAILURE SCENARIOS

---

## 3.1 Duplicate Message

Expected:

- no duplicate dossier
- no duplicate action

---

## 3.2 Missing Data

Expected:

- system asks
- no crash

---

## 3.3 Wrong Linking

Expected:

- message linked to correct dossier

---

## 3.4 Tracking Sent Too Early

Expected:

- impossible

---

## 3.5 Payment Inconsistency

Expected:

- balance always correct

---

## 3.6 Relance Spam

Expected:

- prevented by stop conditions

---

# 4. SUCCESS CRITERIA

---

System is valid if:

- no message lost
- no duplicate dossiers
- correct status transitions
- no early tracking
- relances behave correctly
- manager control preserved
- system usable daily by agency