exec { 'pkill -x killmenow':
  provider => 'shell'
}
