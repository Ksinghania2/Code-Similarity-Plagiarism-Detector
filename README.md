# Static Code Plagiarism and Similarity Detector

A static analysis utility engineered in Python to parse source code documents and quantify their structural similarity using set tokenization algorithms.

The engine normalizes source files to eliminate surface modifications such as formatting differences, whitespace shifts, and comment additions. It evaluates structural overlap by computing the mathematical Jaccard Similarity Coefficient, exposing algorithmic copying even when variable identifiers are altered.
## Example

If a student copies an assignment line-by-line, it is easy to catch. But if they change a few variable names or add extra spaces, a simple word-by-word comparison fails. This project builds a smart engine that ignores those surface changes and detects the actual structural copying.

## Algorithmic Framework

1. Lexical Normalization: Parses raw text inputs to strip single-line comments and strip non-alphanumeric formatting components. Text streams are lowercased to achieve architectural uniformity.

2. Set Tokenization: Maps the normalized text tokens into discrete mathematical set structures. This removes token count overhead and focuses exclusively on the presence of distinct logical elements.

3. Jaccard Coefficient Metric: Evaluates the exact size of the intersection set (matching tokens) divided by the union set (total unique tokens combined). This produces a standardized similarity footprint ranging between 0% and 100%.

## Deployment and Verification

Execute the standalone analysis loop via the command line interface:

```bash
python3 plagiarism_detector.py