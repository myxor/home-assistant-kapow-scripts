#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   @date 2020-02-12
#   @author Marco H (myxor)
#
#   Examples:
#   * python3 hdd.py error /dev/sda
#   * python3 hdd.py temp /dev/sda

import re
import sys
import subprocess
from os import path

if len(sys.argv) > 2:

    mode = sys.argv[1]
    device = sys.argv[2]

    if not path.exists(device):
        print('Device "%s" does not exist.' % device, file=sys.stderr)
        exit(1)

    if mode == "error":
        result = subprocess.run(['smartctl', '-d', 'sat', '-a', device, '--nocheck', 'standby', '--nocheck', 'sleep'],
                                stdout=subprocess.PIPE)
        resultText = result.stdout.decode('utf-8')

        regEx = r"Raw_Read_Error_Rate.*([0-9]+)$"
        matchObj = re.search(regEx, resultText, re.MULTILINE)
        if matchObj:
            errorRate = matchObj.group(1)
            print(errorRate)

    elif mode == "temp":
        result = subprocess.run(['smartctl', '-d', 'sat', '-a', device, '--nocheck', 'standby', '--nocheck', 'sleep'],
                                stdout=subprocess.PIPE)
        resultText = result.stdout.decode('utf-8')

        regEx = r"Temperature_Celsius.*?([0-9]+)(\s+\(Min\/Max .*\))?$"
        matchObj = re.search(regEx, resultText, re.MULTILINE)
        if matchObj:
            temp = matchObj.group(1)
            print(temp)
    else:
        print('Unknown mode', file=sys.stderr)
        exit(1)

else:
    print("Please give a valid mode and device as parameters.", file=sys.stderr)
    exit(1)
