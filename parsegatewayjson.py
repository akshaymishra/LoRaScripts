#!/usr/bin/python
#Decode json for dspworks BLE+LoRa payload. This assumes a kerlink Gateway. This takes in data in fixed format as available from the Kruxworks BLE Module

import json

jsonfile = open('datastr.json')
parsedstring = json.load(jsonfile)
print('DEVEUI '+ parsedstring['DevEUI_uplink']['DevEUI'])

bssidcount=0
for elem in ( parsedstring['DevEUI_uplink']['payload_hex'][1 : : 22]):
    if(elem != '0'):
        bssidcount += 1

print('Total MACs found', bssidcount)
for bssids in range(bssidcount):
    print('BSSID  ', bssids, parsedstring['DevEUI_uplink']['payload_hex'][2+(bssids*22):14+(bssids*22)])
    hexdata = parsedstring['DevEUI_uplink']['payload_hex'][14+bssids*22:16+bssids*22]
    decdata = int(hexdata,16)
    decdata = -(decdata & 0x80) | (decdata & 0x7F)
    print('BSSID', bssids, 'RSSI', decdata)
