#!/usr/bin/env python3

from subprocess import Popen as run, PIPE as pipe
from enum import Enum

class keyNames(Enum):
	KEY_Escape			= 9
	KEY_1				= 10
	KEY_2				= 11
	KEY_3				= 12
	KEY_4				= 13
	KEY_5				= 14
	KEY_6				= 15
	KEY_7				= 16
	KEY_8				= 17
	KEY_9				= 18
	KEY_0				= 19
	KEY_Minus			= 20
	KEY_Equal			= 21
	KEY_Backspace		= 22
	KEY_Tab				= 23
	KEY_Q				= 24
	KEY_W				= 25
	KEY_E				= 26
	KEY_R				= 27
	KEY_T				= 28
	KEY_Y				= 29
	KEY_U				= 30
	KEY_I				= 31
	KEY_O				= 32
	KEY_P				= 33
	KEY_Bracket_Right	= 34
	KEY_Bracket_Left	= 35
	KEY_Enter			= 36
	KEY_Control_Left	= 37
	KEY_A				= 38
	KEY_S				= 39
	KEY_D				= 40
	KEY_F				= 41
	KEY_G				= 42
	KEY_H				= 43
	KEY_J				= 44
	KEY_K				= 45
	KEY_L				= 46
	KEY_SemiColon		= 47
	KEY_Quote_SIngle	= 48
	KEY_Grave			= 49
	KEY_Shift_Left		= 50
	KEY_Slash_Back		= 51
	KEY_Z				= 52
	KEY_X				= 53
	KEY_C				= 54
	KEY_V				= 55
	KEY_B				= 56
	KEY_N				= 57
	KEY_M				= 58
	KEY_Comma			= 59
	KEY_Period			= 60
	KEY_Slash_Forward	= 61
	KEY_Shift_Right		= 62
	KEY_Alt_Left		= 64
	KEY_Space			= 65
	KEY_Caps_Lock		= 66
	KEY_F1				= 67
	KEY_F2				= 68
	KEY_F3				= 69
	KEY_F4				= 70
	KEY_F5				= 71
	KEY_F6				= 72
	KEY_F7				= 73
	KEY_F8				= 74
	KEY_F9				= 75
	KEY_F10				= 76
	KEY_KP_Home			= 79
	KEY_KP_7			= 79
	KEY_KP_Up			= 80
	KEY_KP_8			= 80
	KEY_KP_Page_Up		= 81
	KEY_KP_Prior		= 81
	KEY_KP_9			= 81
	KEY_KP_Left			= 85
	KEY_KP6				= 85
	KEY_KP_End			= 87
	KEY_KP_1			= 87
	KEY_KP_Down			= 88
	KEY_KP_2			= 88
	KEY_KP_Page_Down	= 89
	KEY_KP_Next			= 89
	KEY_KP_3			= 89
	KEY_F11				= 95
	KEY_F12				= 96
	KEY_Control_Right	= 105
	KEY_Print			= 107
	KEY_Alt_Right		= 108
	KEY_Home			= 110
	KEY_Up				= 111
	KEY_Arrow_Up		= 111
	KEY_Page_Up			= 112
	KEY_Left			= 113
	KEY_Arrow_Left		= 113
	KEY_Right			= 114
	KEY_Arrow_Right		= 114
	KEY_End				= 115
	KEY_Down			= 116
	KEY_Arrow_Down		= 116
	KEY_Page_Down		= 117
	KEY_Insert			= 118
	KEY_Delete			= 119
	KEY_Super			= 133
	KEY_Menu			= 135
	KEY_F13				= 191
	XF86Tools			= 191
	KEY_F14				= 192
	XF76LUanch5			= 192
	KEY_F15				= 193
	XF86Launch6			= 193
	KEY_F16				= 194
	XF86Launch7			= 194
	KEY_F17				= 195
	XF86Launch8			= 195
	KEY_F18				= 196
	XF86Launch9			= 196
	KEY_F19				= 197
	KEY_F20				= 198
	XF86AudioMicMute	= 198
	KEY_F21				= 199
	XF86TouchpadToggle	= 199
	KEY_F22				= 200
	XF86TouchpadOn		= 200
	KEY_F23				= 201
	XF86TouchpadOff		= 201
	KEY_F24				= 202

masterKeyDown=dict()

def getXinputDeviceList(seek):
	deviceList=run(
		"xinput list",
		shell=True,
		stdout=pipe
	).stdout.read().decode().split('\n')

	ids=list()

	for line in deviceList:
		if seek in line.lower():
			device=line.split('id=')[1].split('[')[0].strip()
			ids.append(device)

	return ids

def getPressedKeys(device):
	keystates=run(
		"xinput query-state "+device,
		shell=True,
		stdout=pipe
	).stdout.read().decode().split('\n')

	keysDown=list()

	for key in keystates:
		if "key[" in key:
			keyNum	=int(key.split('[')[1].split(']')[0])
			keyState=key.split('=')[1]
			if "down" in keyState:
				keysDown.append(keyNum)

	return keysDown

def isKeyDown(keyNum):
	for device in getXinputDeviceList("slave  keyboard"):
		if keyNum in getPressedKeys(device):
			return True
	return False

def isKeyUp(keyNum):
	for device in getXinputDeviceList("slave  keyboard"):
		if keyNum not in getPressedKeys(device):
			return True
	return False


def watchKeys():
	while True:
		for device in getXinputDeviceList("slave  keyboard"):
			for keysDown in getPressedKeys(device):
				print('watchKeys:', keyNames(int(keysDown)))

def waitForKeyDown(keyNum):
	if not isKeyDown(keyNum):
		print('waitForKeyDown:', keyNames(keyNum), 'is not pressed.')
	else:
		print('waitForKeyDown:', keyNames(keyNum), 'already pressed!')

	while not isKeyDown(keyNum):
		continue
	print('waitForKeyDown:', keyNames(keyNum), 'pressed!')


def waitForKeyUp(keyNum):
	if isKeyDown(keyNum):
		print('waitForKeyUp:', keyNames(keyNum), 'is pressed.')
	else:
		print('waitForKeyUp:', keyNames(keyNum), 'already released!')

	while isKeyDown(keyNum):
		continue
	print('waitForKeyUp:', keyNames(keyNum), 'released!')

#waitForKeyDown(keyNames.KEY_F23.value)
#waitForKeyUp(keyNames.KEY_F23.value)
watchKeys()
