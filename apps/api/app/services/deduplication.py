seen_dedupe_keys: set[str] = set()


def is_duplicate(dedupe_key: str) -> bool:
    return dedupe_key in seen_dedupe_keys


def mark_as_seen(dedupe_key: str) -> None:
    seen_dedupe_keys.add(dedupe_key)