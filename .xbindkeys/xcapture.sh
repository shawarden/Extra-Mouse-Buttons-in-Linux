#!/bin/bash

rootKeyboard=$(xinput list --id-only "Virtual core keyboard")
rootMouse=$(xinput list --id-only "Virtual core pointer")


xinput \
	--test \
