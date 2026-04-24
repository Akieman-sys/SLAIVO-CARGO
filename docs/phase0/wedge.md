# WEDGE V1 — SLAIVO CARGO OS

## 1. Core Idea

SLAIVO V1 is:

WhatsApp → Dossier → Shipment → Validation → Tracking → Relance

This is the minimal system that must work perfectly.

## 2. What V1 DOES

### WhatsApp Intake

- receive messages
- normalize messages
- deduplicate messages
- link message to dossier

### Client Creation

- auto-create client from WhatsApp
- manual client creation by manager

### Dossier System

- create dossier automatically
- create dossier manually
- link everything to dossier
- support partial dossier
- show missing information

### Shipment System

- create shipment
- support unknown weight
- support estimated weight
- support verified weight
- tracking_id exists
- tracking sent ONLY after validation

### Status System

- PARTIAL
- WAITING_FOR_DROP_OFF
- PENDING_VALIDATION
- VALIDATED
- IN_TRANSIT
- ARRIVED_DESTINATION
- READY_FOR_PICKUP

### Manager Control

- validate shipment
- update weight
- update price
- send tracking
- send manual message
- add notes
- add proof

### Relance System (basic)

- arrival notification
- pickup reminder
- drop-off reminder
- balance reminder

### Payment (manual only)

- fees_total
- fees_paid
- balance_due
- manual recording

### Dashboard (basic)

- inbox messages
- dossiers list
- shipments to validate
- balances due
- actions to do

## 3. What V1 REFUSES

- TikTok integration
- Gmail integration
- automated payments
- AI advanced reasoning
- multi-agency system
- analytics advanced
- mobile app
- Kubernetes
- microservices

## 4. Success Criteria

V1 is successful if:

- no message is lost
- every message is linked to a dossier
- manager can validate shipment
- tracking is sent correctly
- relances work without spam
- balance is visible
- agency can operate daily with SLAIVO

## 5. Failure Criteria

V1 fails if:

- messages are lost
- wrong dossier linking
- tracking sent too early
- relances spam clients
- manager loses control