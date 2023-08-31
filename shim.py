'''
https://github.com/nekowithscythe/python_exe_shim
Copyright (C) 2023  Neko_with_Scythe

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import sys
import os
if __name__ == '__main__':
    exe_partial_path = sys.argv[0]
    exe_full_path = os.path.abspath(exe_partial_path)
    exe_name = os.path.basename(exe_full_path)
    exe_base_path = os.path.dirname(exe_full_path)
    conf_name = f"{exe_name.split('.', 1)[0]}.conf"
    conf_full_path = os.path.join(exe_base_path, conf_name)
    cmd_args_len = len(sys.argv)
    
    conf_exist = False

    cmd_args = []
    cmd_frag = None
    cmd_args_str = None
    final_cmd = None

    trigger_help = False

    def debug_print():
        print("Source:: https://github.com/nekowithscythe/python_exe_shim")
        print(f"exe_partial_path:{exe_partial_path}")
        print(f"exe_full_path:{exe_full_path}")
        print(f"exe_base_path:{exe_base_path}")
        print(f"exe_name:{exe_name}")
        print(f"conf_name:{conf_name}")
        print(f"conf_full_path:{conf_full_path}")
        print(f"conf_exist:{conf_exist}")
        print(f"cmd_args_len:{cmd_args_len}")
        print(f"cmd_args:{cmd_args}")
        print(f"cmd_frag:{cmd_frag}")
        print(f"cmd_args_str:{cmd_args_str}")
        print(f"final_cmd:{final_cmd}")
        print()
        print("--- How to use ---")
        print("This is a exe shim.")
        print("The shim figures out the config file to consume based on the name of the file.")
        print("As you can see from the parameter dump above, it expects the config to be at 'conf_full_path', so be sure to create your config there.'")
        print("Inside the file, just put the actual command you want executed, with full path.")
        print("BE WARNED. NO SANITISATION IS DONE. YOU USE AT YOUR OWN RISK.")
        print("If you have '%*' in your command string, it would be replaced by the command line arguments.")
        print("If you use '--debug' or '--help' as your first argument, this would be displayed, but no execution would be done.")

    if os.path.isfile(conf_full_path):
        conf_exist = True
        with open(conf_full_path, 'r') as f:
            cmd_frag = f.read().strip()

    if cmd_args_len > 1:
        cmd_args = sys.argv[1:]
        _cmd_nibble = cmd_args[0].strip()
        if _cmd_nibble == '--debug' or _cmd_nibble == '--help':
            trigger_help = True
            if cmd_args_len > 2:
                cmd_args = cmd_args[1:]
            else:
                cmd_args = []
    
    if cmd_frag is not None:
        if len(cmd_args) > 0:
            cmd_args_str = " ".join(cmd_args)
            final_cmd = cmd_frag.replace('%*', cmd_args_str)
        else:
            final_cmd = cmd_frag.replace('%*', '')
    
    if trigger_help:
        debug_print()
    elif not conf_exist:
        debug_print()
        print()
        print(f"ERROR! Config '{conf_full_path}' does not exist.")
    else:
        os.system(final_cmd)
