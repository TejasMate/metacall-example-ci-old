spawn("metacall")
sleep(1)
sendln("load rb examples/string-manipulation/str.rb")
sleep(1)
sendln("call longest_repetition(\"bbbaaabaaaa\")")
sleep(1)
sendln("exit")