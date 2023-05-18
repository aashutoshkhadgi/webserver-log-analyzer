from nbformat import read, write
def Remove_Output(Book):
    for cell in Book.cells:
        if hasattr(cell, "outputs"):
            cell.outputs = []
        if hasattr(cell, "prompt_number"):
            del cell["prompt_number"]
Book = read(open("log-analyzer.py.ipynb"), 4)
Remove_Output(Book)
write(Book, open("new-log-analyzer.py.ipynb", "w"), 4)
