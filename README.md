# Autonomous Insurance Claims Processing Agent

## Project Overview

This project implements a lightweight Autonomous Insurance Claims Processing Agent that processes FNOL (First Notice of Loss) documents and automates initial claim triaging.

The agent:
- Reads FNOL documents in TXT or PDF format
- Extracts key insurance claim fields
- Identifies missing mandatory information
- Applies predefined business rules to classify and route claims
- Outputs a structured JSON response with a clear routing explanation

---

## Problem Statement

Insurance FNOL documents often arrive in unstructured formats and require manual review.  
This system automates the initial claims intake process, reducing manual effort and improving routing accuracy.

---

## Supported Input Formats

- TXT
- PDF

FNOL documents may include policy information, incident details, involved parties, and asset damage information.

---

## Fields Extracted

### Policy Information
- Policy Number  
- Policyholder Name  
- Policy Effective Dates  

### Incident Information
- Incident Date  
- Incident Time  
- Incident Location  
- Incident Description  

### Involved Parties
- Claimant  
- Third Parties  
- Contact Details  

### Asset Details
- Asset Type  
- Asset ID (VIN / Vehicle Number)  
- Estimated Damage Amount  

### Mandatory Fields
- Claim Type  
- Attachments  
- Initial Estimate  

---

## Business Routing Rules

The claim is routed based on the following rules:

| Condition | Route |
|---------|-------|
Estimated damage < 25,000 | Fast-track |
Any mandatory field missing | Manual review |
Description contains “fraud”, “inconsistent”, or “staged” | Investigation Flag |
Claim type = injury | Specialist Queue |

---

## Output Format

The system returns a strict JSON output:

```json
{
  "extractedFields": {},
  "missingFields": [],
  "recommendedRoute": "",
  "reasoning": ""
}

## Project Structure

claims-agent/
├── app/
│ ├── main.py
│ ├── document_reader.py
│ ├── field_extractor.py
│ ├── validator.py
│ ├── router.py
│ └── utils.py
│
├── sample_inputs/
│ └── sample_fnol.txt
│
├── output/
│ └── sample_output.json
│
├── requirements.txt
└── README.md


---

## Technologies Used

- Python 3
- pdfplumber
- Regular Expressions
- Standard Python libraries

---

## Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
How to Run
Run the application from the project root directory:

python app/main.py sample_inputs/sample_fnol.txt
For PDF input:

python app/main.py sample_inputs/sample_fnol.pdf
Example Output
{
  "extractedFields": {
    "policyNumber": "POL123456",
    "policyholderName": "Rahul Sharma",
    "policyEffectiveDates": "01-01-2024 to 31-12-2024",
    "incidentDate": "15-01-2024",
    "incidentTime": "14:30",
    "incidentLocation": "Bangalore",
    "incidentDescription": "Rear-end collision, minor damage",
    "claimant": "Rahul Sharma",
    "thirdParties": "None",
    "contactDetails": "9876543210",
    "assetType": "Car",
    "assetId": "KA01AB1234",
    "estimatedDamageAmount": "18000",
    "claimType": "vehicle",
    "attachments": "photos, FIR",
    "initialEstimate": "18000"
  },
  "missingFields": [],
  "recommendedRoute": "Fast-track",
  "reasoning": "Estimated damage is below 25,000"
}
Validation & Error Handling
Unsupported file formats are rejected

Mandatory fields are validated

Output directory is auto-created if missing

Defensive checks prevent runtime errors

Submission Notes
This repository satisfies all requirements of the Autonomous Insurance Claims Processing Agent assessment:

End-to-end working solution

Deterministic routing logic

Strict JSON output compliance

Clean and readable code structure



Clean and readable code structure

Author
Shankar Singh

