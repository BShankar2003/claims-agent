import re

def extract_fields(text: str) -> dict:
    def find(pattern):
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1).strip() if match else None

    # ✅ FIX: extract asset ID BEFORE dictionary
    asset_match = re.search(r"(VIN|Vehicle Number)[:\-]?\s*(.+)", text, re.IGNORECASE)
    asset_id = asset_match.group(2).strip() if asset_match else None

    extracted = {
        "policyNumber": find(r"Policy Number[:\-]?\s*(.+)"),
        "policyholderName": find(r"Policyholder Name[:\-]?\s*(.+)"),
        "policyEffectiveDates": find(r"Policy Effective Dates[:\-]?\s*(.+)"),

        "incidentDate": find(r"Incident Date[:\-]?\s*(.+)"),
        "incidentTime": find(r"Incident Time[:\-]?\s*(.+)"),
        "incidentLocation": find(r"Incident Location[:\-]?\s*(.+)"),
        "incidentDescription": find(r"Incident Description[:\-]?\s*(.+)"),

        "claimant": find(r"Claimant[:\-]?\s*(.+)"),
        "thirdParties": find(r"Third Parties[:\-]?\s*(.+)"),
        "contactDetails": find(r"Contact Details[:\-]?\s*(.+)"),

        "assetType": find(r"Asset Type[:\-]?\s*(.+)"),
        "assetId": asset_id,

        "estimatedDamageAmount": find(r"Estimated Damage Amount[:\-]?\s*(\d+)"),
        "claimType": find(r"Claim Type[:\-]?\s*(.+)"),
        "attachments": find(r"Attachments[:\-]?\s*(.+)"),
        "initialEstimate": find(r"Initial Estimate[:\-]?\s*(\d+)")
    }

    return extracted
