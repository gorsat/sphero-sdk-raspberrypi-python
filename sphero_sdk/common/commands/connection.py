#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x19-peer_connection.json
# Device ID:          0x19
# Device Name:        connection
# Timestamp:          10/10/2019 @ 21:40:31.380534 (UTC)

from sphero_sdk.common.enums.connection_enums import CommandsEnum
from sphero_sdk.common.devices import DevicesEnum
from sphero_sdk.common.parameter import Parameter
from sphero_sdk.common.sequence_number_generator import SequenceNumberGenerator


def get_bluetooth_advertising_name(target, timeout): 
    return { 
        'did': DevicesEnum.connection,
        'cid': CommandsEnum.get_bluetooth_advertising_name,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='name',
                data_type='std::string',
                index=0,
                size=1,
            ),
        ]
    }
