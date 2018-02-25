---
title: Hackintosh installation process logging
date: 2018-01-20 20:19:14
tags:
---

### The first problem
- Stuck at Attempting System Restart... MACH Reboot
- solution: DSDT, fix header checked.

### "000000.841844 AppleUSBLegacyRoot@: AppleUSBLegacyRoot::init: enabling legacy matching" while trying

- stuck here
- solution: this has to do with the USB. Set `Devices > fixownership: true & injectUSB: true`. The in the `kxta` folder, add the injectALLUSB.ketx file.


### post installation

- Can't boot stucked in `screenlock`
- that's because there is no enough `.kext` file in the `others` directory. just replace the EFI folder with the one in installation driver. That's done.

### Only 7m virtual RAM for HD4600
- I have tried a lot of methods, such as try all possible `ig-platform-id` listed in `clover-wiki`. But I didn't try inject FackID.
- solution:
    + first, add `0x0a260006` as ig-platform-id in `/graphics/`
    + then, add `0x04128086` as `IntelGFX`
    + then, add a bunch of kext to the EFI. It includes 





### log
- with connection to ARM video card, if the setting of video in bios is `AUTO` and clover without inject both `intel` and `ATI`, i can boot the OS from USB and SSD. But if the BIOS setting of `video` were changed to `AMD`, it won't get boot.
