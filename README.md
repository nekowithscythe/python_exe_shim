# python_exe_shim
A simple exe shim using python

## Prequisites

1. A working python3 installation on Windows 10 and above.
2. pyinstaller installed in your python3 environment.
3. shim.py

## Compile
To "compile" shim.py
```
python -m PyInstaller --onefile shim.py
```
The compiled shim would be in .\dist\shim.exe

## How to use
Just rename the exe to whatever command you want to mimic.
For example, shim.exe -> scp.exe

Then in the same folder where you have the exe, create a similarly named config file.

So if you have 'scp.exe', you should also have 'scp.conf'

In the config file, just fill it with the command you wanted to run. The shim will replace any '%*' it finds in the command with the arguments given to the shim.

For VS Code Remote-SSH extension to use WSL2's SCP
```
C:\Windows\system32\wsl.exe bash -ic 'scp %*'
```

## Why
VS Code's Remote-SSH extension from M$ refuses to fix/enhance their extension to accept a separate config to specify which scp to use.

That is a problem because I prefer WSL2's SSH over the windows implementation, and I've already setup my nice SSH profiles in WSL2, linked them to 1password's secrets vault, and this is the only part that refuses to play nice.

The ssh.bat trick does not work for SCP.

Other guides do mention a shim, but it's usually a GO shim. I don't want to install another environment just to create a shim. I have python, so might as well.

## For the lazy.

**YOU SHOULD NOT DOWNLOAD ANY EXE FROM A STRANGER YOU DO NOT KNOW. THIS IS PROVIDED FOR YOUR CONVENIENCE AND YOU USE IT AT YOUR OWN RISK.**

password: useatyourownrisk

https://eu2.contabostorage.com/f252b02d8a964efba50daa4aaf923681:opensource/python_exe_shim/shim.7z