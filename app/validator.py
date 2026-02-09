
MANDATORY_FIELDS = [
    "claimType",
    "attachments",
    "initialEstimate"
]

def find_missing_fields(extracted: dict) -> list:
    missing = []
    for field in MANDATORY_FIELDS:
        if not extracted.get(field):
            missing.append(field)
    return missing
