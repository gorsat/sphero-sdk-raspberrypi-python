#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x19-peer_connection.json
# Device ID:          0x19
# Device Name:        connection
# Timestamp:          02/08/2019 @ 17:14:09.074040 (UTC)

from spheroboros.common.commands.connection import CommandsEnum
from spheroboros.common.devices import DevicesEnum
from spheroboros.common.parameter import Parameter


async def set_bluetooth_device_name(self, name, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.connection,
        CommandsEnum.set_bluetooth_device_name,
        target,
        timeout,
        inputs=[
            Parameter(
                name='name',
                data_type='std::string',
                index=0,
                value=name,
                size=1
            ),
        ],
    )


async def get_bluetooth_device_name(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.connection,
        CommandsEnum.get_bluetooth_device_name,
        target,
        timeout,
        outputs=[
            Parameter(
                name='name',
                data_type='std::string',
                index=0,
                size=1,
            ),
        ],
    )
