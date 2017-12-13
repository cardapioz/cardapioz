# git-config
# Autogenerated from man page /usr/share/man/man1/git-config.1.gz
complete -c git-config -l replace-all --description 'Default behavior is to replace at most one line.'
complete -c git-config -l add --description 'Adds a new line to the option without altering any existing values.'
complete -c git-config -l get --description 'Get the value for a given key (optionally filtered by a regex matching the va…'
complete -c git-config -l get-all --description 'Like get, but does not fail if the number of values for the key is not exactl…'
complete -c git-config -l get-regexp --description 'Like --get-all, but interprets the name as a regular expression and writes ou…'
complete -c git-config -l get-urlmatch --description 'When given a two-part name section. key, the value for section. <url>.'
complete -c git-config -l global --description 'For writing options: write to global ~/.'
complete -c git-config -l system --description 'For writing options: write to system-wide $(prefix)/etc/gitconfig rather than…'
complete -c git-config -l local --description 'For writing options: write to the repository . git/config file.'
complete -c git-config -s f -l file --description 'Use the given config file instead of the one specified by GIT_CONFIG.'
complete -c git-config -l blob --description 'Similar to --file but use the given blob instead of a file.  E. g.'
complete -c git-config -l remove-section --description 'Remove the given section from the configuration file.'
complete -c git-config -l rename-section --description 'Rename the given section to a new name.'
complete -c git-config -l unset --description 'Remove the line matching the key from config file.'
complete -c git-config -l unset-all --description 'Remove all lines matching the key from config file.'
complete -c git-config -s l -l list --description 'List all variables set in config file, along with their values.'
complete -c git-config -l bool --description 'git config will ensure that the output is "true" or "false".'
complete -c git-config -l int --description 'git config will ensure that the output is a simple decimal number.'
complete -c git-config -l bool-or-int --description 'git config will ensure that the output matches the format of either --bool or…'
complete -c git-config -l path --description 'git-config will expand leading ~ to the value of $HOME, and ~user to the home…'
complete -c git-config -s z -l null --description 'For all options that output values and/or keys, always end values with the nu…'
complete -c git-config -l name-only --description 'Output only the names of config variables for --list or --get-regexp.'
complete -c git-config -l get-colorbool --description 'Find the color setting for name (e. g.  color.'
complete -c git-config -l get-color --description 'Find the color configured for name (e. g.  color. diff.'
complete -c git-config -s e -l edit --description 'Opens an editor to modify the specified config file; either --system, --globa…'
complete -c git-config -l includes --description 'Respect include. * directives in config files when looking up values.'
complete -c git-config -l 'replace-all.' --description '.'
complete -c git-config -l 'get-regexp.' --description '.'
complete -c git-config -s u --description 'option to git-status(1) when the command takes more than 2 seconds to enumera…'
complete -c git-config -l work-tree --description 'command-line option.'
complete -c git-config -o 'c.' --description 'LV with another value or setting core. pager to lv +c.  core. whitespace.'
complete -c git-config -o 'trailing-space):' --description 'oc o 2. 3.'
complete -c git-config -l ignore-errors --description 'option of git-add(1).  add.'
complete -c git-config -l 'keep-cr.' --description '\\r from lines ending with \\r\\n.  Can be overridden by giving.'
complete -c git-config -l no-keep-cr --description 'from the command line.  See git-am(1), git-mailsplit(1).  am. threeWay.'
complete -c git-config -l 3way --description 'option from the command line).  Defaults to false.  See git-am(1).  apply.'
complete -c git-config -l ignore-space-change --description 'option.'
complete -c git-config -l whitespace --description 'option.  See git-apply(1).  branch. autoSetupMerge.'
complete -c git-config -l track --description 'and.'
complete -c git-config -l no-track --description 'options.'
complete -c git-config -l preserve-merges --description 'along to git rebase so that locally committed merge commits will not be flatt…'
complete -c git-config -s w --description 'option in git-help(1)) or a working repository in gitweb (see git-instaweb(1)…'
complete -c git-config -l color --description 'option.  color. diff. <slot>.'
complete -c git-config -s A --description '.'
complete -c git-config -s B --description '.'
complete -c git-config -s C --description 'filename.'
complete -c git-config -s h --description 'function.'
complete -c git-config -s p --description 'linenumber.'
complete -c git-config -s n --description 'match.'
complete -c git-config -l cleanup --description 'option in git commit.  See git-commit(1) for details.'
complete -c git-config -l dirstat --description 'parameters specifying the default behavior of the.'
complete -c git-config -l '*stat' --description 'options.  files.'
complete -c git-config -s O --description 'option to git-diff(1).  diff. renameLimit.'
complete -c git-config -o 'l.' --description 'diff. renames.'
complete -c git-config -l prune --description 'option was given on the command line.  See also remote. <name>. prune.'
complete -c git-config -l in-reply-to --description 'deep threading makes every mail a reply to the previous one.'
complete -c git-config -o s/--signoff --description 'option of format-patch by default.'
complete -c git-config -s k --description 'modes to use.  If the attributes force Git to treat a file as text, the.'
complete -c git-config -o kb --description 'mode, which suppresses any newline munging the client might otherwise do.'
complete -c git-config -o 'kb.' --description 'core. autocrlf.  gitcvs. dbName.'
complete -c git-config -l basic-regexp --description '.'
complete -c git-config -l extended-regexp --description '.'
complete -c git-config -l fixed-strings --description '.'
complete -c git-config -l perl-regexp --description 'option accordingly, while the value default will return to the default matchi…'
complete -c git-config -l patch --description 'mode of git-add(1), git-checkout(1), git-commit(1), git-reset(1), and git-sta…'
complete -c git-config -l 'abbrev-commit.' --description '.'
complete -c git-config -l 'no-abbrev-commit.' --description 'log. date.'
complete -c git-config -l date --description 'option.  See git-log(1) for details.  log. decorate.'
complete -c git-config -l decorate --description 'option.  log. follow.'
complete -c git-config -l follow --description 'option was used when a single <path> is given.'
complete -c git-config -l 'use-mailmap.' --description 'mailinfo. scissors.'
complete -c git-config -l no-ff --description 'option from the command line).'
complete -c git-config -l ff-only --description 'option from the command line).  merge. branchdesc.'
complete -c git-config -l output --description 'option.  Git will attempt to detect whether meld supports.'
complete -c git-config -l 'output.' --description 'mergetool. keepBackup.'
complete -c git-config -l max-pack-size --description 'option of git-repack(1).  The minimum size allowed is limited to 1 MiB.'
complete -c git-config -l paginate --description 'or.'
complete -c git-config -l no-pager --description 'is specified on the command line, it takes precedence over this option.'
complete -c git-config -l follow-tags --description 'option by default.'
complete -c git-config -l 'no-follow-tags.' --description 'push. gpgSign.'
complete -c git-config -l signed --description 'is passed to git-push(1).'
complete -c git-config -l recurse-submodules --description 'rebase. stat.'
complete -c git-config -l autosquash --description 'option by default.  rebase. autoStash.'
complete -c git-config -l mirror --description 'option was given on the command line.  remote. <name>. skipDefaultUpdate.'
complete -c git-config -l pack-kept-objects --description 'was passed.  See git-repack(1) for details.'
complete -c git-config -l write-bitmap-index --description 'or repack. writeBitmaps).  repack. writeBitmaps.'
complete -c git-config -l quiet --description 'was used for the fetch, pack-objects will output nothing at all until the pac…'

