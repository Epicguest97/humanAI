import nbformat

# Load the notebook
notebook_path = "Yolo_finetuning3.ipynb"
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

# Remove problematic metadata
if 'widgets' in nb['metadata']:
    del nb['metadata']['widgets']

# Save the cleaned notebook
fixed_path = "Yolo_finetuning_cleaned.ipynb"
with open(fixed_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Cleaned notebook saved as {fixed_path}")
