#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Constants for the Tuya integration."""

DOMAIN = "tuya_v2"

CONF_PROJECT_TYPE = "tuya_project_type"
CONF_ENDPOINT = "endpoint"
CONF_ACCESS_ID = "access_id"
CONF_ACCESS_SECRET = "access_secret"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_COUNTRY_CODE = "country_code"
CONF_APP_TYPE = "tuya_app_type"

TUYA_DISCOVERY_NEW = "tuya_discovery_new_{}"
TUYA_DEVICE_MANAGER = "tuya_device_manager"
TUYA_HA_TUYA_MAP = 'tuya_ha_tuya_map'
TUYA_HA_DEVICES = 'tuya_ha_devices'

TUYA_ENDPOINT = {
    "https://openapi.tuyaus.com": "America",
    "https://openapi.tuyacn.com": "China",
    "https://openapi.tuyaeu.com": "Europe",
    "https://openapi.tuyain.com": "India",
    "https://openapi-ueaz.tuyaus.com": "EasternAmerica",
    "https://openapi-weaz.tuyaeu.com": "WesternEurope"
}

TUYA_PROJECT_TYPE = {
    1: "Custom Development",
    0: "Smart Home PaaS"
}

TUYA_APP_TYPE = {
    'tuyaSmart': 'TuyaSmart',
    'smartlife': 'Smart Life'
}

TUYA_SUPPORT_HA_TYPE = [
    'switch',
    'fan',
    'cover',
    'climate',
    'light',
    'sensor',
    'binary_sensor',
    'humidifier'
    # 'alarm_control_panel'
]