#!/bin/sh
# Generates the Visual-dialog public API documentation from the source code.
# Writes documentation in plain text in visualdialog-documentation.txt and in
# HTML in visualdialog.core.html.


pydoc3 visualdialog.box >> visualdialog-doc.txt
pydoc3 visualdialog.dialog >> visualdialog-doc.txt

echo "wrote visualdialog-doc.txt"
pydoc3 -w visualdialog.core
mv visualdialog.core.html visualdialog-doc.html
pydoc3 -w visualdialog.dialog >> visualdialog-doc.html

echo "done."
