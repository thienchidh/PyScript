import subprocess
import time

wifi_name = "Wi-Fi"
ethernet_name = "Ethernet"


def switch_net():
    last_time = time.time()
    # Check if Wi-Fi is currently enabled
    t = subprocess.run(
        ["powershell.exe", "-Command", ("$t = Get-NetAdapter -Name '%s'; exit $t.Status -eq 'Up'" % ethernet_name)])
    print("Checking %s status..." % ethernet_name, t.returncode)
    if t.returncode == 0:
        # Wi-Fi is currently enabled, so disable it and enable Ethernet
        print("Enabling %s..." % ethernet_name)
        subprocess.Popen(["powershell.exe", "-Command", ("Enable-NetAdapter -Name '%s'" % ethernet_name)])
        subprocess.Popen(["powershell.exe", "-Command", ("Disable-NetAdapter -Name '%s' -Confirm:$false" % wifi_name)])
    else:
        # Wi-Fi is currently disabled, so disable Ethernet and enable Wi-Fi
        print("Enabling %s..." % wifi_name)
        subprocess.Popen(
            ["powershell.exe", "-Command", ("Disable-NetAdapter -Name '%s' -Confirm:$false" % ethernet_name)])
        subprocess.Popen(["powershell.exe", "-Command", ("Enable-NetAdapter -Name '%s'" % wifi_name)])

    print("Network Switched", f'{time.time() - last_time:.2f}s')


if __name__ == "__main__":
    switch_net()
