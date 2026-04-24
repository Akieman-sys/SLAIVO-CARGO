# DATA MODEL — SLAIVO CARGO OS (FINAL)

---

# 1. CORE PHILOSOPHY

SLAIVO is a Dossier-centric system.

Everything must be linked to a dossier.

No message, shipment, payment, or action exists outside a dossier.

---

# 2. CORE ENTITIES

---

## 2.1 Client

Represents a person or entity interacting with the agency.

Fields:

- client_id
- phone (primary identifier)
- name
- email (optional)
- country
- preferred_language (FR / EN)
- created_at
- updated_at

Rules:

- Can be created with minimal info
- Can be created automatically (WhatsApp) or manually (manager)
- Identity may evolve later (multi-channel)

---

## 2.2 Dossier (CENTRAL OBJECT)

Represents a complete business case.

Fields:

- dossier_id
- client_id
- case_type (SEND_CARGO / TRANSITAIRE)
- status_global
- intake_status (PARTIAL / COMPLETE)
- validation_status (PENDING / VALIDATED)
- primary_channel (whatsapp)
- created_at
- updated_at

Relationships:

- 1 dossier → many messages
- 1 dossier → many shipments
- 1 dossier → many payments
- 1 dossier → many actions
- 1 dossier → many relances
- 1 dossier → many proofs

Rules:

- EVERYTHING must be linked to a dossier
- Can exist without shipment
- Can be PARTIAL
- NEVER deleted (audit required)

---

## 2.3 Shipment

Represents a physical or future package.

Fields:

- shipment_id
- dossier_id
- tracking_id
- origin_country
- destination_country
- cargo_mode (AIR / SEA)
- goods_type
- declared_weight_kg
- verified_weight_kg
- estimated_volume_cbm
- weight_status (UNKNOWN / ESTIMATED / VERIFIED)
- status
- pricing_rule_id
- calculated_price
- final_price
- fees_total
- fees_paid
- balance_due
- validation_status
- created_at
- updated_at

Rules:

- Can be created with partial data
- Weight can be unknown
- Tracking NOT sent before validation
- Payment may block progression
- Always linked to dossier

---

# 3. PRICING MODEL

---

## 3.1 Pricing Rule

Fields:

- pricing_rule_id
- origin_country
- destination_country
- goods_type (optional)
- pricing_mode (PER_KG / PER_CBM / FIXED)
- price_per_unit
- currency
- discount_threshold (optional)
- created_at

Rules:

- Pricing depends on route + goods
- Not hardcoded
- Configurable per agency

---

## 3.2 Pricing Logic

- price = rule * weight OR volume
- discount if threshold reached
- manager can override

---

# 4. PAYMENT MODEL

---

Fields:

- payment_id
- dossier_id
- shipment_id
- amount
- currency
- status
- recorded_by
- created_at

---

## Critical Rule:

Shipment CANNOT be dispatched if:

balance_due > 0

---

# 5. QUALIFICATION / INTAKE

---

Fields collected:

- destination_country
- origin_country
- goods_type
- estimated_weight_kg
- estimated_volume_cbm
- service_type

service_type:

- SEND_CARGO
- TRANSITAIRE
- SUPPLIER_PAYMENT
- CONSOLIDATION

---

## Rule:

If missing → dossier = PARTIAL

System asks missing info.

---

# 6. CONFIGURABLE GUIDED INTAKE

---

Agency defines required fields.

SLAIVO:

1. detects intent
2. creates dossier
3. checks missing fields
4. asks questions
5. updates progressively

---

# 7. AGENCY KNOWLEDGE BASE

---

Stores:

- pricing info
- services
- addresses
- rules
- FAQ
- conditions

---

## Rule:

SLAIVO answers ONLY from this knowledge.

If missing → ASK or ESCALATE.

---

# 8. INTERACTION MODEL

---

Modes:

- GUIDED_CONVERSATION (default)
- MENU (optional)

---

System must support:

- guided questions
- structured flow
- hybrid interaction

---

# 9. KEY INVARIANTS (CRITICAL)

- No message without dossier
- No shipment without dossier
- No tracking before validation
- No payment outside system
- No AI invention
- Payment may block shipment

---

# 10. SYSTEM PHILOSOPHY

SLAIVO must:

- accept incomplete data
- guide user progressively
- never block too early
- keep manager in control
- stay simple but powerful