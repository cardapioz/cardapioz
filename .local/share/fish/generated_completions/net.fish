# net
# Autogenerated from man page /usr/share/man/man8/net.8.gz
complete -c net -s '?' -l help --description 'Print a summary of command line options.'
complete -c net -s k -l kerberos --description 'Try to authenticate with kerberos.'
complete -c net -s w -l workgroup --description 'Sets target workgroup or domain.'
complete -c net -s W -l myworkgroup --description 'Sets client workgroup or domain.'
complete -c net -s U -l user --description 'User name to use.'
complete -c net -s I -l ipaddress --description 'IP address of target server to use.'
complete -c net -s p -l port --description 'Port on the target server to connect to (usually 139 or 445).'
complete -c net -s n -l netbiosname --description 'This option allows you to override the NetBIOS name that Samba uses for itsel…'
complete -c net -s s -l configfile --description 'The file specified contains the configuration details required by the server.'
complete -c net -s S -l server --description 'Name of target server.'
complete -c net -s l -l long --description 'When listing data, give more information on each item.'
complete -c net -s v -l verbose --description 'When listing data, give more verbose information on each item.'
complete -c net -s f -l force --description 'Enforcing a net command.'
complete -c net -s P -l machine-pass --description 'Make queries to the external server using the machine account of the local se…'
complete -c net -l request-timeout --description 'Let client requests timeout after 30 seconds the default is 10 seconds.'
complete -c net -s t -l timeout --description 'Set timeout for client operations to 30 seconds.'
complete -c net -l use-ccache --description 'Try to use the credentials cached by winbind.'
complete -c net -s i -l stdin --description 'Take input for net commands from standard input.'
complete -c net -l tallocreport --description 'Generate a talloc report while processing a net command.'
complete -c net -s T -l test --description 'Only test command sequence, dry-run.'
complete -c net -s F -l flags --description 'Pass down integer flags to a net subcommand.'
complete -c net -s C -l comment --description 'Pass down a comment string to a net subcommand.'
complete -c net -l myname --description 'Use MYNAME as a requester name for a net subcommand.'
complete -c net -s c -l container --description 'Use a specific AD container for net ads operations.'
complete -c net -s M -l maxusers --description 'Fill in the maxusers field in net rpc share operations.'
complete -c net -s r -l reboot --description 'Reboot a remote machine after a command has been successfully executed (e. g.'
complete -c net -l force-full-repl --description 'When calling "net rpc vampire keytab" this option enforces a full re-creation…'
complete -c net -l single-obj-repl --description 'When calling "net rpc vampire keytab" this option allows to replicate just a …'
complete -c net -l clean-old-entries --description 'When calling "net rpc vampire keytab" this option allows to cleanup old entri…'
complete -c net -l db --description 'Define dbfile for "net idmap" commands.'
complete -c net -l lock --description 'Activates locking of the dbfile for "net idmap check" command.'
complete -c net -s a -l auto --description 'Activates noninteractive mode in "net idmap check".'
complete -c net -l repair --description 'Activates repair mode in "net idmap check".'
complete -c net -l acls --description 'Includes ACLs to be copied in "net rpc share migrate".'
complete -c net -l attrs --description 'Includes file attributes to be copied in "net rpc share migrate".'
complete -c net -l timestamps --description 'Includes timestamps to be copied in "net rpc share migrate".'
complete -c net -s X -l exclude --description 'Allows to exclude directories when copying with "net rpc share migrate".'
complete -c net -l destination --description 'Defines the target servername of migration process (defaults to localhost).'
complete -c net -s L -l local --description 'Sets the type of group mapping to local (used in "net groupmap set").'
complete -c net -s D -l domain --description 'Sets the type of group mapping to domain (used in "net groupmap set").'
complete -c net -s N -l ntname --description 'Sets the ntname of a group mapping (used in "net groupmap set").'
complete -c net -s R -l rid --description 'Sets the rid of a group mapping (used in "net groupmap set").'
complete -c net -l reg-version --description 'Assume database version {n|1,2,3} (used in "net registry check").'
complete -c net -s o -l output --description 'Output database file (used in "net registry check").'
complete -c net -l wipe --description 'Create a new database from scratch (used in "net registry check").'
complete -c net -l precheck --description 'Defines filename for database prechecking (used in "net registry import").'
complete -c net -s e -l encrypt --description 'This command line parameter requires the remote server support the UNIX exten…'
complete -c net -s d -l debuglevel --description 'level is an integer from 0 to 10.'
complete -c net -s V -l version --description 'Prints the program version number.'
complete -c net -l log-basename --description 'Base directory name for log/debug files.  The extension ".'
complete -c net -l option --description 'Set the smb. conf(5) option "<name>" to value "<value>" from the command line.'

