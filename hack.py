import subprocess

def fet():
    cmd = "Get-WmiObject Win32_PnPSignedDriver select DeviceName, DeviceVersion"
    res = subprocess.run(["powershell", "-command", cmd], capture_output = True)    

    if res.returncode != 0:
        print("Error! Check the command.")
    else:
        output = res.stdout
        out_fmt = output.decode("utf-8")

        file = open("data.txt", "w")
        file.write("output:-")
        file.write(out_fmt)
        file.close()