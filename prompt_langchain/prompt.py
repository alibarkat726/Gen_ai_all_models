from langchain_core.prompts import PromptTemplate


template  = PromptTemplate(
    template = """
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation style: "{style_input}"
Explanation length: "{length_input}"
1. Mathematical Details:
   - Include relevant mathematical equatons if present in the paper,
   - Explain the mathematical concepts using simple, intuitive code snippets wher applicable.
2. Analogies:
   - Userelatable analogies to simplify coplex ideas.
if certain is not available int the paper ,respond with : "Insufficient information available"
instead of guessing.
Ensure the summary is accurate,clear and aligned with the provided styleand length.
""",
input_variables=['paper_input','style_input','length_input'],
validate_template=True 
)
template.save('template.json')