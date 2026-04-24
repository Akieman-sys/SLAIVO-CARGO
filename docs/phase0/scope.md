# SCOPE V1 — SLAIVO CARGO OS

## 1. Allowed (We DO)

### Core System

- WhatsApp message ingestion
- message normalization
- message deduplication
- client auto-creation
- client manual creation

### Dossier System

- dossier creation (auto + manual)
- dossier as source of truth
- partial dossier support
- missing fields tracking

### Shipment System

- shipment creation
- tracking_id handling
- unknown / estimated / verified weight
- manager validation required

### Status Machine

- basic status transitions
- controlled transitions
- status history

### Manager Actions

- validate shipment
- update weight
- update price
- send tracking
- manual message
- notes
- proof

### Relance System

- arrival relance
- pickup relance
- drop-off relance
- balance relance
- stop conditions
- anti-spam rules

### Payment System (manual)

- fees_total
- fees_paid
- balance_due
- manual recording
- correction tracking

### Dashboard

- inbox
- dossier list
- shipment validation queue
- balances due
- actions to do

---

## 2. Explicitly NOT Allowed (We REFUSE)

### Channels

- TikTok
- Gmail
- multi-channel ingestion

### Payments

- mobile money
- card payments
- automated payments

### AI

- advanced AI reasoning
- LLM orchestration
- prediction systems

### Architecture

- microservices
- Kubernetes
- distributed systems

### Product

- mobile app
- analytics advanced
- multi-agency SaaS
- RBAC complex

---

## 3. Grey Zone (Allowed only if necessary)

- simple caching
- simple background jobs
- minimal logging
- simple retry mechanisms

ONLY if required for stability

---

## 4. Rule of Decision

Before adding anything:

Ask:

1. Does it improve tracking?
2. Does it improve relance?
3. Does it improve dossier clarity?
4. Is it required for stability?

If NO → reject

---

## 5. Engineering Constraint

- simple code > smart code
- explicit logic > magic
- reliability > features
- clarity > performance