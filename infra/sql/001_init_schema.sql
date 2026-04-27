create table if not exists clients (
    id uuid primary key default gen_random_uuid(),
    phone text unique,
    name text,
    email text,
    country text,
    preferred_language text default 'FR',
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create table if not exists dossiers (
    id uuid primary key default gen_random_uuid(),
    client_id uuid references clients(id),
    case_type text default 'SEND_CARGO',
    status_global text default 'LEAD',
    intake_status text default 'PARTIAL',
    validation_status text default 'PENDING',
    primary_channel text default 'whatsapp',
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create table if not exists message_events_raw (
    id uuid primary key default gen_random_uuid(),
    provider text not null default 'whatsapp',
    provider_message_id text,
    raw_payload jsonb not null,
    dedupe_key text unique not null,
    received_at timestamptz not null default now()
);

create table if not exists messages (
    id uuid primary key default gen_random_uuid(),
    dossier_id uuid references dossiers(id),
    client_id uuid references clients(id),
    provider_message_id text,
    from_phone text not null,
    to_phone text,
    text_body text,
    message_type text default 'text',
    source_channel text default 'whatsapp',
    direction text default 'inbound',
    dedupe_key text unique not null,
    received_at timestamptz not null,
    created_at timestamptz not null default now()
);

create table if not exists dossier_timeline_events (
    id uuid primary key default gen_random_uuid(),
    dossier_id uuid references dossiers(id),
    event_type text not null,
    event_payload jsonb,
    created_at timestamptz not null default now()
);