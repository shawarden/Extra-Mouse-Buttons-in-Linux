# Linux with Extra Mouse Buttons

Because losing config files kinda sucks!

Generally non-usable mouse buttons are configured as F13+ keys via windows driver or `input-remapper` then bound to scripts via `autkey`.

1. Logitech Trackman Optical (Set via `input-remapper`)
	- Scroll Up (Left Edge Fore):		F21
	- Scroll Down (Left Edge Mid):	F22
	- App/Lock (Left Edge Back):		F23
2. Elecom HUGE (Set via `input-remapper`)
	- FN1 (Left Edge Fore):			F21
	- FN2 (Left Edge Back):			F22
	- FN3 (Right Edge):				F23
3. SteelSeries Rival 500 ([Set via windows driver](https://old.reddit.com/r/linux_gaming/comments/pns050/any_fellow_steelseries_and_linux_enjoyers_out/))
	- 6 (Thumb Bottom Fore):			F16
	- 7 (Thumb Bottom):				F17
	- 8 (Thumb Middle):				F18
	- 9 (Thumb Back):					F20 // F19 doesn't work with AutoKey?
	- 10 (DPI):						DPI switch
	- 11 (Left Edge Fore):			F21
	- 12 (Left Edge Back):			F22
	- 13 (Right Edge):				F23

## Issues:

`xbindkeys` and `autokey` have issues with button release events that some games don't like. They press the button over and over or the release event doesn't trigger properly. If different things can happen on a button press, tap or hold, `autokey` and `xbindkeys` doesn't work. Python and shell scrips allow for better tracking but `autokey` shifts application focus somehow, not sure how/why and responsiveness is problematic.

## Usage:

1. Clone somewhere
2. Softlink `~/.config/autokey` to `.../Linux_EMB/autokey`
3. Softlink `~/.xbindkeys` to `.../Linux_EMB/.xbindkeys`
4. Softlink `~/.xbindkeysrc` to `~/.xbindkeys/.xbindkeysrc`
