#!/usr/bin/env python3

import sys
sys.path.insert(1, '../../surface-aggregator-module/scripts/ssam/')
import libssam

from irp_display import Battery_GetBatteryProp, Tc

def hfmt(b):
    if type(b) is int:
        return f"{b:0>2x}"
    return " ".join(f"{x:0>2x}" for x in b)

def sam_cmd(ctrl, tc, cid, data, hasresp):
	print('TC %02x CID %02x:' % (tc, cid), hfmt(data) if data else None)
	req = libssam.Request(tc, 1, cid, 1, libssam.REQUEST_HAS_RESPONSE if hasresp else 0, data)
	resp = ctrl.request(req)
	print('\t=>', hfmt(resp) if resp else None)
	return resp

def bat_cmd(ctrl):
    cid = 0x22
    return sam_cmd(ctrl, Tc.BAT._value_, cid, [], True)




if __name__ == '__main__':
   
    if len(sys.argv) == 1:
        with libssam.Controller() as c:
            z = Battery_GetBatteryProp.read(bytes(bat_cmd(c)))
            print(z)
            # print(speed_bytes.rpm)
