import sys
from document_reader import read_document
from field_extractor import extract_fields
from validator import find_missing_fields
from router import route_claim
from utils import save_output

def main(input_file: str):
    text = read_document(input_file)
    extracted = extract_fields(text)
    missing_fields = find_missing_fields(extracted)
    route, reasoning = route_claim(extracted, missing_fields)

    result = {
        "extractedFields": extracted,
        "missingFields": missing_fields,
        "recommendedRoute": route,
        "reasoning": reasoning
    }

    save_output(result, "../output/sample_output.json")

    print(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    main(sys.argv[1])
