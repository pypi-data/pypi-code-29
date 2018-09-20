#coding:utf-8

import  sys
import  AutoCall.AutoDialer as adialer



#adialer.run(sys.path[0]+"/cc.conf")

adialer.run_with_queue(sys.path[0]+"/cc.conf")
#adialer.run_with_queue(sys.path[0]+"/cc_test.conf")