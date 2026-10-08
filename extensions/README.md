# Extension definitions

Third-party schema additions must be isolated from GIANTS source files.

Each integration should record: upstream mod name and version, documentation source, supported XML paths, attribute types/defaults, examples, and test cases.

Interactive Control is the first integration. Vehicle Years is provisional until its own documentation is reviewed.

Avoid adding all possible attributes to a generated XML completion block: XML schemas describe valid structure, while the separate MGS completion extension provides minimal, practical insertion templates.
