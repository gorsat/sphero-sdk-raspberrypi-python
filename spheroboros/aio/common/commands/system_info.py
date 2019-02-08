#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x11-system_info.json
# Device ID:          0x11
# Device Name:        system_info
# Timestamp:          02/08/2019 @ 17:14:09.074599 (UTC)

from spheroboros.common.commands.system_info import CommandsEnum
from spheroboros.common.devices import DevicesEnum
from spheroboros.common.parameter import Parameter


async def get_main_application_version(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_main_application_version,
        target,
        timeout,
        outputs=[
            Parameter(
                name='major',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
            Parameter(
                name='minor',
                data_type='uint16_t',
                index=1,
                size=1,
            ),
            Parameter(
                name='revision',
                data_type='uint16_t',
                index=2,
                size=1,
            ),
        ],
    )


async def get_bootloader_version(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_bootloader_version,
        target,
        timeout,
        outputs=[
            Parameter(
                name='major',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
            Parameter(
                name='minor',
                data_type='uint16_t',
                index=1,
                size=1,
            ),
            Parameter(
                name='revision',
                data_type='uint16_t',
                index=2,
                size=1,
            ),
        ],
    )


async def get_board_revision(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_board_revision,
        target,
        timeout,
        outputs=[
            Parameter(
                name='revision',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ],
    )


async def get_mac_address(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_mac_address,
        target,
        timeout,
        outputs=[
            Parameter(
                name='mac_address',
                data_type='std::string',
                index=0,
                size=1,
            ),
        ],
    )


async def get_nordic_temperature(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_nordic_temperature,
        target,
        timeout,
        outputs=[
            Parameter(
                name='temperature',
                data_type='int32_t',
                index=0,
                size=2,
            ),
        ],
    )


async def on_application_ready_notify(self, target, handler=None, timeout=None):
    await self._dal.on_command(
        DevicesEnum.system_info,
        CommandsEnum.application_ready_notify,
        target,
        handler,
        timeout,
        outputs=[
            Parameter(
                name='application_index',
                data_type='uint8_t',
                index=0,
                size=1
            ),
        ],
    )


async def get_stats_id(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_stats_id,
        target,
        timeout,
        outputs=[
            Parameter(
                name='stats_id',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
        ],
    )


async def on_application_alive_notify(self, target, handler=None, timeout=None):
    await self._dal.on_command(
        DevicesEnum.system_info,
        CommandsEnum.application_alive_notify,
        target,
        handler,
        timeout,
        outputs=[
            Parameter(
                name='application_index',
                data_type='uint8_t',
                index=0,
                size=1
            ),
        ],
    )


async def get_processor_name(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_processor_name,
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


async def get_boot_reason(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_boot_reason,
        target,
        timeout,
        outputs=[
            Parameter(
                name='reason',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ],
    )


async def get_last_error_info(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_last_error_info,
        target,
        timeout,
        outputs=[
            Parameter(
                name='file_name',
                data_type='uint8_t',
                index=0,
                size=32,
            ),
            Parameter(
                name='line_number',
                data_type='uint16_t',
                index=1,
                size=1,
            ),
            Parameter(
                name='data',
                data_type='uint8_t',
                index=2,
                size=12,
            ),
        ],
    )


async def request_l1_diagnostics(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.request_l1_diagnostics,
        target,
        timeout,
    )


async def write_config_block(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.write_config_block,
        target,
        timeout,
        outputs=[
            Parameter(
                name='is_success',
                data_type='bool',
                index=0,
                size=1,
            ),
        ],
    )


async def get_config_block(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_config_block,
        target,
        timeout,
        outputs=[
            Parameter(
                name='meta_data_version',
                data_type='uint32_t',
                index=0,
                size=1,
            ),
            Parameter(
                name='config_block_version',
                data_type='uint32_t',
                index=1,
                size=1,
            ),
            Parameter(
                name='application_data',
                data_type='uint8_t',
                index=2,
                size=255,
            ),
        ],
    )


async def set_config_block(self, meta_data_version, config_block_version, application_data, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.set_config_block,
        target,
        timeout,
        inputs=[
            Parameter(
                name='meta_data_version',
                data_type='uint32_t',
                index=0,
                value=meta_data_version,
                size=1
            ),
            Parameter(
                name='config_block_version',
                data_type='uint32_t',
                index=1,
                value=config_block_version,
                size=1
            ),
            Parameter(
                name='application_data',
                data_type='uint8_t',
                index=2,
                value=application_data,
                size=255
            ),
        ],
    )


async def erase_config_block(self, magic_safety_number, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.erase_config_block,
        target,
        timeout,
        inputs=[
            Parameter(
                name='magic_safety_number',
                data_type='uint32_t',
                index=0,
                value=magic_safety_number,
                size=1
            ),
        ],
    )


async def get_swd_locking_status(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_swd_locking_status,
        target,
        timeout,
        outputs=[
            Parameter(
                name='is_locked',
                data_type='bool',
                index=0,
                size=1,
            ),
        ],
    )


async def set_swd_locking(self, is_locked, unlocking_key, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.set_swd_locking,
        target,
        timeout,
        inputs=[
            Parameter(
                name='is_locked',
                data_type='bool',
                index=0,
                value=is_locked,
                size=1
            ),
            Parameter(
                name='unlocking_key',
                data_type='uint32_t',
                index=1,
                value=unlocking_key,
                size=1
            ),
        ],
    )


async def get_manufacturing_date(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_manufacturing_date,
        target,
        timeout,
        outputs=[
            Parameter(
                name='year',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
            Parameter(
                name='month',
                data_type='uint8_t',
                index=1,
                size=1,
            ),
            Parameter(
                name='day',
                data_type='uint8_t',
                index=2,
                size=1,
            ),
        ],
    )


async def set_manufacturing_date(self, year, month, day, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.set_manufacturing_date,
        target,
        timeout,
        inputs=[
            Parameter(
                name='year',
                data_type='uint16_t',
                index=0,
                value=year,
                size=1
            ),
            Parameter(
                name='month',
                data_type='uint8_t',
                index=1,
                value=month,
                size=1
            ),
            Parameter(
                name='day',
                data_type='uint8_t',
                index=2,
                value=day,
                size=1
            ),
        ],
    )


async def set_sku(self, sku, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.set_sku,
        target,
        timeout,
        inputs=[
            Parameter(
                name='sku',
                data_type='std::string',
                index=0,
                value=sku,
                size=1
            ),
        ],
    )


async def get_sku(self, target, timeout=None):
    return await self._dal.send_command(
        DevicesEnum.system_info,
        CommandsEnum.get_sku,
        target,
        timeout,
        outputs=[
            Parameter(
                name='sku',
                data_type='std::string',
                index=0,
                size=1,
            ),
        ],
    )
