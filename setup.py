import sys
import time
from argparse import ArgumentParser
import subprocess


def startappiumserver():
    pathtonode = "start node.exe \"C:\\Program Files (x86)\\Appium\\node_modules\\appium\\lib\\server\\main.js\""
    parser = ArgumentParser()
    parser.add_argument("-a", "--address", dest="address_ip", default="127.0.0.1", help="ip address")
    parser.add_argument("-b", "--port", dest="port_num", default="4723")
    parser.add_argument("-c", "--app", dest="app_path", help="app_path",
                        default="C:\ShyamaAPK\player-release-2.1.0.2138.apk")
    parser.add_argument("-d", "--platform-name", dest="platform_name", default="Android")
    parser.add_argument("-e", "--platform-version", dest="platform_version", default="19")
    parser.add_argument("-f", "--automation-name", dest="automation_name", default="Appium")
    parser.add_argument("-g", "--device-name", dest="device_name", default="Z110P3016B00410")

    try:
        args = parser.parse_args()
        command = '{0} --address {1}'.format(pathtonode, args.address_ip)  # Added address_ip
        command += ' --port {0}'.format(args.port_num)  # Added port number
        command += ' --app {0}'.format(args.app_path)  # Added path
        command += ' --platform-name {0}'.format(args.platform_name)  # Added platform name
        command += ' --platform-version {0}'.format(args.platform_version)  # Added platform verison
        command += ' --automation-name {0}'.format(args.automation_name)  # Added automation name
        command += ' --device-name \"{0}\"'.format(args.device_name)  # Added device name
        command += ' --log-no-color'  # hardcoded log-no-color
    except Exception as e:
        parser.error("{0}".format(e))
        sys.exit(0)
    subprocess.Popen(command, shell=True)
    time.sleep(10)
