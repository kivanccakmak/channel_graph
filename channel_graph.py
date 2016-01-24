#!/usr/bin/python
import sys
import subprocess
import os
import matplotlib.pyplot as plt

FREQ = {'5GHz': '5', '2GHz': '2'}
INTERFACE = "wlan0"
SCAN_CMD = 'iwlist {interf} | grep -w ("Channel"'
SCAN_CMD = SCAN_CMD.format(interf=INTERFACE)

def channel_graph(search_frequency):
    """ plots network histogram
    :search_frequency: str
        '5GHz or 2GHZ'
    """
    chan_list = []
    proc = subprocess.Popen([SCAN_CMD], stdout=subprocess.PIPE,
            shell=True)
    (out, err) = proc.communicate()
    lines = out.split('\n')

    for line in lines:
        if len(line) == 4:
            channel = line[len(line) - 1]
            channel = channel[0:len(channel)-1]
            band = line[0]
            band = band[band.find(':')+1]
            if band == search_frequency:
                chan_list.append(int(channel))

    plt.hist(chan_list, max(chan_list) - min(chan_list))
    plt.xlabel("Channels in {} GHz".format(search_frequency))
    plt.ylabel("# networks")
    plt.show()

def main():
    """
    main to run from console
    """
    if len(sys.argv) != 2:
        print "Usage: {} <Channel> ".format(sys.argv[0])
        print "Example: channel_graph.py 2GHz"
        print "Example: channel_graph.py 5GHz"
        sys.exit(1)

    if sys.argv[1] == "2GHz":
        channel_graph(FREQ['2GHz'])
    elif sys.argv[1] == "5GHz":
        channel_graph(FREQ['5GHz'])
    else:
        print "Frequency variable can only be 2GHz or 5GHz"
        print "Example: channel_graph.py 2GHz"
        print "Example: channel_graph.py 5GHz"
        sys.exit(1)

if __name__ == "__main__":
    main()
