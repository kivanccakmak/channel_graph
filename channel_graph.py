import sys
import os
import matplotlib.pyplot as plt

freq = {'5GHz': '5', '2GHz': '2'}

def channel_graph(search_frequency):
    os.system("iwlist wlan0 scan > wifi_details.txt")
    os.system('cat wifi_details.txt | grep -w "(Channel" > wifi_channels.txt')
    channel_info = open("wifi_channels.txt", "r")
    list = []
    
    with open("wifi_channels.txt") as f:
        for lines in f:
            line = lines.split()
            if(len(line) == 4):
                channel = line[len(line) - 1]
                channel = channel[0:len(channel)-1]
                band = line[0]
                band = band[band.find(':')+1]
                if(band == search_frequency):
                    list.append(int(channel))
                    print("channel = {}".format(list[len(list) - 1]))
    
    plt.hist(list, max(list) - min(list))
    plt.xlabel("Channels in {} GHz".format(search_frequency))
    plt.ylabel("# networks")
    plt.show()    
    
def main():
    if len(sys.argv) != 2:
        print("Usage: {} <Channel> ".format(sys.argv[0]))
        print("Example: channel_graph.py 2GHz")
        print("Example: channel_graph.py 5GHz")
        sys.exit(1)
        
    if(sys.argv[1] == "2GHz"):
        channel_graph(freq['2GHz'])
    elif(sys.argv[1] == "5GHz"):
        channel_graph(freq['5GHz'])
    else:
        print("Frequency variable can only be 2GHz or 5GHz")
        print("Example: channel_graph.py 2GHz")
        print("Example: channel_graph.py 5GHz")
        sys.exit(1)
    
if __name__ == "__main__":
    main()
