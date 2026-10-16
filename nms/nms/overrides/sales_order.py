
def clear_prevdoc(doc, method=None):
    for row in doc.items:
        row.prevdoc_docname = None
        row.prevdoc_doctype = None