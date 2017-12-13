# rgrep
# Autogenerated from man page /usr/share/man/man1/rgrep.1.gz
complete -c rgrep -l help --description 'Output a usage message and exit.'
complete -c rgrep -s V -l version --description 'Output the version number of  grep and exit. SS "Matcher Selection".'
complete -c rgrep -s E -l extended-regexp --description 'Interpret  PATTERN as an extended regular expression (ERE, see below).'
complete -c rgrep -s F -l fixed-strings --description 'Interpret  PATTERN as a list of fixed strings (instead of regular expressions…'
complete -c rgrep -s G -l basic-regexp --description 'Interpret  PATTERN as a basic regular expression (BRE, see below).'
complete -c rgrep -s P -l perl-regexp --description 'Interpret the pattern as a Perl-compatible regular expression (PCRE).'
complete -c rgrep -s e -l regexp --description 'Use  PATTERN as the pattern.'
complete -c rgrep -s f -l file --description 'Obtain patterns from R FILE , one per line.'
complete -c rgrep -s i -l ignore-case --description 'Ignore case distinctions in both the  PATTERN and the input files.'
complete -c rgrep -s v -l invert-match --description 'Invert the sense of matching, to select non-matching lines.'
complete -c rgrep -s w -l word-regexp --description 'Select only those lines containing matches that form whole words.'
complete -c rgrep -s x -l line-regexp --description 'Select only those matches that exactly match the whole line.'
complete -c rgrep -s y --description 'Obsolete synonym for  -i . SS "General Output Control".'
complete -c rgrep -s c -l count --description 'Suppress normal output; instead print a count of matching lines for each inpu…'
complete -c rgrep -l color -l colour --description 'Surround the matched (non-empty) strings, matching lines, context lines, file…'
complete -c rgrep -s L -l files-without-match --description 'Suppress normal output; instead print the name of each input file from which …'
complete -c rgrep -s l -l files-with-matches --description 'Suppress normal output; instead print the name of each input file from which …'
complete -c rgrep -s m -l max-count --description 'Stop reading a file after  NUM matching lines.'
complete -c rgrep -s o -l only-matching --description 'Print only the matched (non-empty) parts of a matching line, with each such p…'
complete -c rgrep -s q -l quiet -l silent --description 'Quiet; do not write anything to standard output.'
complete -c rgrep -s s -l no-messages --description 'Suppress error messages about nonexistent or unreadable files.'
complete -c rgrep -s b -l byte-offset --description 'Print the 0-based byte offset within the input file before each line of outpu…'
complete -c rgrep -s H -l with-filename --description 'Print the file name for each match.'
complete -c rgrep -s h -l no-filename --description 'Suppress the prefixing of file names on output.'
complete -c rgrep -l label --description 'Display input actually coming from standard input as input coming from file R…'
complete -c rgrep -s n -l line-number --description 'Prefix each line of output with the 1-based line number within its input file.'
complete -c rgrep -s T -l initial-tab --description 'Make sure that the first character of actual line content lies on a tab stop,…'
complete -c rgrep -s u -l unix-byte-offsets --description 'Report Unix-style byte offsets.'
complete -c rgrep -s Z -l null --description 'Output a zero byte (the \\s-1ASCII\\s0  NUL character) instead of the character…'
complete -c rgrep -s A -l after-context --description 'Print  NUM lines of trailing context after matching lines.'
complete -c rgrep -s B -l before-context --description 'Print  NUM lines of leading context before matching lines.'
complete -c rgrep -s C -l context --description 'Print  NUM lines of output context.'
complete -c rgrep -s a -l text --description 'Process a binary file as if it were text; this is equivalent to the  --binary…'
complete -c rgrep -l binary-files --description 'If the first few bytes of a file indicate that the file contains binary data,…'
complete -c rgrep -s D -l devices --description 'If an input file is a device, FIFO or socket, use  ACTION to process it.'
complete -c rgrep -s d -l directories --description 'If an input file is a directory, use  ACTION to process it.'
complete -c rgrep -l exclude --description 'Skip files whose base name matches  GLOB (using wildcard matching).'
complete -c rgrep -l exclude-from --description 'Skip files whose base name matches any of the file-name globs read from  FILE…'
complete -c rgrep -l exclude-dir --description 'Exclude directories matching the pattern  DIR from recursive searches.'
complete -c rgrep -s I --description 'Process a binary file as if it did not contain matching data; this is equival…'
complete -c rgrep -l include --description 'Search only files whose base name matches  GLOB (using wildcard matching as d…'
complete -c rgrep -s r -l recursive --description 'Read all files under each directory, recursively, following symbolic links on…'
complete -c rgrep -s R -l dereference-recursive --description 'Read all files under each directory, recursively.'
complete -c rgrep -l line-buffered --description 'Use line buffering on output.  This can cause a performance penalty.'
complete -c rgrep -s U -l binary --description 'Treat the file(s) as binary.'
complete -c rgrep -s z -l null-data --description 'Treat the input as a set of lines, each terminated by a zero byte (the ASCII …'

