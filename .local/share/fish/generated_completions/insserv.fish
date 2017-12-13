# insserv
# Autogenerated from man page /usr/share/man/man8/insserv.8.gz
complete -c insserv -s v -l verbose --description 'Write out what is currently going on.'
complete -c insserv -o 'c<config>' -l 'config<config>' --description 'Specify path to the insserv. conf file and the insserv. conf. d directory.'
complete -c insserv -o 'o<path>' -l 'override<path>' --description 'LSB comment headers found in this path will override existing LSB comment hea…'
complete -c insserv -o 'p<path>' -l 'path<path>' --description 'Specify path to init. d directory.   Useful for testing.'
complete -c insserv -s n -l dryrun --description 'Do not update symlinks.'
complete -c insserv -s r -l remove --description 'Remove the listed scripts from all runlevels.'
complete -c insserv -s d -l default --description 'Use default runlevels as defined in the scripts.'
complete -c insserv -s f -l force --description 'Ignore if a required service is missed.'
complete -c insserv -o 'u<path>' -l 'upstart-job<path>' --description 'Path to replace existing upstart job path.'
complete -c insserv -s s -l showall --description 'Output runlevel and sequence information.  Do not update symlinks.'
complete -c insserv -s c -l config --description 'Specify path to the insserv. conf file and the insserv. conf. d directory.'
complete -c insserv -s o -l override --description 'LSB comment headers found in this path will override existing LSB comment hea…'
complete -c insserv -s p -l path --description 'Specify path to init. d directory.   Useful for testing.'
complete -c insserv -s u -l upstart-job --description 'Path to replace existing upstart job path.'
complete -c insserv -s h -l help --description 'Print out short usage message.'

