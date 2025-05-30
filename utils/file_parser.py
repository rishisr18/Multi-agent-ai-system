import json
import fitz  # PyMuPDF

def parse_input(input_data):
    # Try parsing as JSON
    try:
        parsed_json = json.loads(input_data)
        return {"type": "json", "content": parsed_json}
    except json.JSONDecodeError:
        # Check for typical email-like indicators
        if (
            "email:" in input_data.lower() and
            ("name:" in input_data.lower() or "from:" in input_data.lower()) and
            ("project" in input_data.lower() or "skills" in input_data.lower())
        ):
            return {"type": "email", "content": input_data}

        # Fallback
        return {"type": "unknown", "content": input_data}

def parse_pdf(file_path):
    doc = fitz.open(file_path)
    text = "\n".join([page.get_text() for page in doc])
    return {"type": "pdf", "content": text}
