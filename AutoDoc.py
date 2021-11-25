# Welcome page, basically only directs

import autodocdef as ad

ret1  = ad.readbin('ruleset.bin')
ret2  = ad.readbin('ruleset2.bin')
if ret1['initiate'] == 0:
    ad.log('Initiated Auto Doc first time or after reset')
    ad.os.system('ad_command.py')
else:
     ad.log('Auto Doc opened')
     if ret2['ad_type'] ==2:
         ad.os.system('ad_home_private.py')
     else:
         ad.os.system('ad_home_personal.py')
