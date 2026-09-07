-- Persist WhatsApp LID -> phone-number identities learned by the linked-device
-- gateway. A LID is a technical identifier and must never be displayed as a
-- customer phone number.
-- Safe and idempotent after 112_pilot_whatsapp_inbox_media.sql.

create table if not exists whatsapp_qr_identity_map (
  connection_id uuid not null references whatsapp_qr_connections(id) on delete cascade,
  org_id text not null references organizations(id),
  lid_jid text not null,
  phone_jid text not null,
  phone_number text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (connection_id, lid_jid),
  constraint ck_whatsapp_qr_identity_lid check (lid_jid like '%@lid'),
  constraint ck_whatsapp_qr_identity_phone_jid check (
    phone_jid like '%@s.whatsapp.net' or phone_jid like '%@c.us'
  ),
  constraint ck_whatsapp_qr_identity_phone_number check (
    phone_number ~ '^\+[1-9][0-9]{6,14}$'
  )
);

create index if not exists idx_whatsapp_qr_identity_phone
  on whatsapp_qr_identity_map(org_id, phone_number, updated_at desc);

revoke all on whatsapp_qr_identity_map from public;

comment on table whatsapp_qr_identity_map is
  'Durable WhatsApp LID to real E.164 phone mapping learned from signed device events.';
