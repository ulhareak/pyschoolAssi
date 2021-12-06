# In unix system, the '/etc/hosts' file contains the mappings of IP addresses to host names. Each entry is an
# individual line with the IP address on the first column followed by the corresponding host name. Comments in the
# file are preceded by '#'. Sample /etc/hosts

# Write a function that reads the /etc/hosts and return the hostname, given the ip address.
def gethostname(ip_address):
    f = open('/etc/hosts')
    for i in f.readlines():
        if(len(i.split('\t')) == 2 and ip_address == i.split('\t')[0]):
            return i.split('\t')[0]
        else:
            return "Unknown host"


if __name__ == "__main__":
    print(gethostname('127.0.0.1'))
    print(gethostname('192.168.2.253'))
    print(gethostname('192.168.2.254'))
