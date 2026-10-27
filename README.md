# Token-Based Code Similarity Demo

A small Python script that compares two files by lowercasing their text, extracting word-like tokens, converting them to sets, and calculating Jaccard similarity. It is a simple lexical overlap demonstration, not a plagiarism detector that can determine authorship or intent.

## Run

```bash
python plagiarism_detector.py
```

The script creates `student_a.py` and `student_b.py` in the current directory and compares them. Run it from a disposable directory if those filenames already contain files you want to keep.

## Scope and limitations

This is not syntax-aware: it does not parse an abstract syntax tree, and identifier names remain part of the token sets, so renaming variables can change the score. Comment removal is a simple regular expression rather than a language-aware parser. A similarity percentage is only a signal for manual review and must not be used by itself to decide plagiarism.
