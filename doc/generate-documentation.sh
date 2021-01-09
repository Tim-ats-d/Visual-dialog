#!/bin/sh
# Generates the Visual-dialog public API documentation from the source code.
# Writes documentation in plain text in visualdialog-documentation.txt and in
# HTML in visualdialog.core.html.


pydoc3 visualdialog.box >> visualdialog-doc.txt
pydoc3 visualdialog.__init__ >> visualdialog-doc.txt

echo "wrote visualdialog-doc.txt"
pydoc3 -w visualdialog.core

echo "done."
