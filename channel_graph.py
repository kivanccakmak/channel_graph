#!/usr/bin/python
import sys
import os
import matplotlib.pyplot as plt

FREQ = {'5GHz': '5', '2GHz': '2'}
FILE_NAME = "wifi_detals.txt"
SCAN_CMD = "iwlist wlan0 scan > {f_name}.txt"
SCAN_CMD = SCAN_CMD.format(f_name=FILE_NAME)
GREP_CMD = 'cat {f_name} | grep -w ("Channel"' +\
        ' > {f_name}'
GREP_CMD = GREP_CMD.format(f_name=FILE_NAME)

def channel_graph(search_frequency):
    """ plots network histogram
    :search_frequency: str
        '5GHz or 2GHZ'
    """
    os.system(SCAN_CMD)
    os.system(GREP_CMD)
    chan_list = []

    with open("wifi_channels.txt") as f_ptr:
        for lines in f_ptr:
            line = lines.split()
            if len(line) == 4:
                channel = line[len(line) - 1]
                channel = channel[0:len(channel)-1]
                band = line[0]
                band = band[band.find(':')+1]
                if band == search_frequency:
                    chan_list.append(int(channel))
                    print "channel = {}".format(list[len(list) - 1])

    plt.hist(list, max(list) - min(list))
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
