# This manifest kills a process
exec { 'killmenow':
command => 'pkill -f "killmenow"',
}
