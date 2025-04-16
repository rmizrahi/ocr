from openai import OpenAI
from pprint import pprint
from olmocr.pipeline import build_page_query

query = 'await build_page_query("~/code/ocr/docs/The New Anthem.pdf", page=1, target_longest_image_dim=1024, target_anchor_text_len=60)'
print(query)
query['model'] = 'olmocr-7b-0225-preview'
response = client.chat.completions.create(**query)
print(response.choices[0].message.content)
# Assuming LM Studio is running locally
###client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio", timeout=60)

# Replace with your PDF path and page number
###pdf_path = "~/code/ocr/docs/The New Anthem.pdf"
###page_number = 1

# Use olmocr to build the query (simplified example)
# Note: build_page_query needs to be adapted to your olmocr version
###pdf_content = query # build_page_query(pdf_path, page_number)

# Send the query to the LM Studio model
###response = client.chat.completions.create(
###    model="olmocr-7b-0225-preview",  # Replace with your LM Studio model name
###    messages=[
###        {"role": "system", "content": "You are an OCR assistant."},
###        {"role": "user", "content": f"Extract the text from the provided PDF: {pdf_content}"}
###    ]
###)

# Extract the OCRed text from the response
ocr_text = response.choices[0].message.content
print(ocr_text)
