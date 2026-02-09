from typing import Tuple

def route_claim(extracted: dict, missing_fields: list) -> Tuple[str, str]:
    description = (extracted.get("incidentDescription") or "").lower()
    claim_type = (extracted.get("claimType") or "").lower()

    if missing_fields:
        return "Manual review", "One or more mandatory fields are missing"

    if any(keyword in description for keyword in ["fraud", "inconsistent", "staged"]):
        return "Investigation Flag", "Suspicious keywords detected in incident description"

    if claim_type == "injury":
        return "Specialist Queue", "Claim type is injury which requires specialist handling"

    try:
        damage = int(extracted.get("estimatedDamageAmount", 0))
        if damage < 25000:
            return "Fast-track", "Estimated damage is below 25,000"
    except ValueError:
        pass

    return "Manual review", "Does not meet fast-track or specialist criteria"
