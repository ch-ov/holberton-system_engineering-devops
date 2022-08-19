# Kills a process named killmenow

exec { 'pkill -x killmenow':
  provider => 'shell'
}
