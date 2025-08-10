# ADGM Corporate Agent - Document Intelligence (MVP)

**An AI-powered document analysis tool for corporate legal documents, focusing on ADGM company incorporation processes.**


## Features

- Upload multiple corporate documents (.docx) for AI-based analysis.
- Detect document types based on keywords.
- Identify missing required documents for company incorporation.
- Detect legal "red flags" or issues within documents.
- Generate annotated `.docx` files with review comments.
- Produce a detailed JSON summary report.



## Getting Started

### Prerequisites

- Python 3.8+
- Install dependencies:


pip install -r requirements.txt

Running the App
Place your .docx corporate documents in a folder (e.g., examples/).

Run the backend analysis script to test:

python -c "from agent_core import analyze_and_run; import json; result = analyze_and_run(['examples/sample1.docx'], 'examples/output'); print(json.dumps(result['json'], indent=2))"

Launch the Gradio web app:

python app.py

Open the URL displayed (e.g., http://127.0.0.1:7860) in your browser.

Upload your corporate documents and click "Analyze" to get instant insights.
