import nbformat

# Load the notebook
notebook_path = "Generate_Images.ipynb"
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

# Remove problematic metadata
if 'widgets' in nb['metadata']:
    del nb['metadata']['widgets']

# Save the cleaned notebook
fixed_path = "Generate_Images1.ipynb"
with open(fixed_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Cleaned notebook saved as {fixed_path}")
