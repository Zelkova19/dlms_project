from libs.GXSettings import GXSettings
from libs.GXDLMSReader import GXDLMSReader
import os
import sys
import traceback
from gurux_serial import GXSerial
from gurux_net import GXNet
from gurux_dlms.enums import ObjectType
from gurux_dlms.objects.GXDLMSObjectCollection import GXDLMSObjectCollection
from libs.GXSettings import GXSettings
from libs.GXDLMSReader import GXDLMSReader
from gurux_dlms.GXDLMSClient import GXDLMSClient
from gurux_common.GXCommon import GXCommon
from gurux_dlms.enums.DataType import DataType
import locale
from gurux_dlms.GXDateTime import GXDateTime
from gurux_dlms.internal._GXCommon import _GXCommon
from gurux_dlms import GXDLMSException, GXDLMSExceptionResponse, GXDLMSConfirmedServiceError, GXDLMSTranslator
from gurux_dlms import GXByteBuffer, GXDLMSTranslatorMessage, GXReplyData
from gurux_dlms.enums import RequestTypes, Security, InterfaceType
from gurux_dlms.secure.GXDLMSSecureClient import GXDLMSSecureClient

# импорт пакетов
try:
    import pkg_resources
    # pylint: disable=broad-except
except Exception:
    # It's OK if this fails.
    print("pkg_resources not found")

# вывод информации о пакетах
try:
    print("gurux_dlms version: " + pkg_resources.get_distribution("gurux_dlms").version)
    print("gurux_net version: " + pkg_resources.get_distribution("gurux_net").version)
    print("gurux_serial version: " + pkg_resources.get_distribution("gurux_serial").version)
except Exception:
    # It's OK if this fails.
    print("pkg_resources not found")

# args: the command line arguments
reader = None
settings = GXSettings()
ret = settings.getParameters("COM", "COM3", password="1597531234567890", authentication="High", serverAddress=7602,
                             logicalAddress=1, clientAddress=48)
if not isinstance(settings.media, (GXSerial, GXNet)):
    raise Exception("Unknown media type.")
reader = GXDLMSReader(settings.client, settings.media, settings.trace, settings.invocationCounter)

settings.media.open()
