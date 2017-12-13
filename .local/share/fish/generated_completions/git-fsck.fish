# git-fsck
# Autogenerated from man page /usr/share/man/man1/git-fsck.1.gz
complete -c git-fsck -l unreachable --description 'Print out objects that exist but that aren\\(cqt reachable from any of the ref…'
complete -c git-fsck -l dangling --description 'Print objects that exist but that are never directly used (default).'
complete -c git-fsck -l root --description 'Report root nodes.'
complete -c git-fsck -l tags --description 'Report tags.'
complete -c git-fsck -l cache --description 'Consider any object recorded in the index also as a head node for an unreacha…'
complete -c git-fsck -l no-reflogs --description 'Do not consider commits that are referenced only by an entry in a reflog to b…'
complete -c git-fsck -l full --description 'Check not just objects in GIT_OBJECT_DIRECTORY ($GIT_DIR/objects), but also t…'
complete -c git-fsck -l connectivity-only --description 'Check only the connectivity of tags, commits and tree objects.'
complete -c git-fsck -l strict --description 'Enable more strict checking, namely to catch a file mode recorded with g+w bi…'
complete -c git-fsck -l verbose --description 'Be chatty.'
complete -c git-fsck -l lost-found --description 'Write dangling objects into . git/lost-found/commit/ or .'
complete -c git-fsck -l progress --description 'Progress status is reported on the standard error stream by default when it i…'
complete -c git-fsck -l no-dangling --description 'can be used to omit this information from the output.'

