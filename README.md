# Pi-Final-Project-CNA-335

### Update and Upgrade the Pi by 
```
sudo apt-get update
sudo apt-get upgrade
```
### Run the following command to install Pi-Hole

```
curl -sSL https://install.pi-hole.net | bash
```

### Pi-hole automated installer

```
This installer will transform your device into a network-wide ad   blocker!  
<Ok>
```

### Free and open source

```
The Pi-hole is free, but powered by your donations: https://pi-hole.net/donate/       
<Ok>
```

### Static IP Needed

```
The Pi-hole is a SERVER so it needs a STATIC IP ADDRESS to function properly.                                                 
In the next section, you can choose to use your current network settings (DHCP) or to manually edit them.
<Ok>
```

```
Select Upstream DNS Provider. To use your own, select Custom.
Google (ECS)
<Ok>

```

```
Pi-hole relies on third party lists in order to block ads. 
You can use the suggestion below, and/or add your own after installation                                                       
To deselect the suggested list, use spacebar
[*] StevenBlack  StevenBlack's Unified Hosts List
<Ok>
```

```
Select Protocols (press space to toggle selection)
(*) StevenBlack 
(*) MalwareDom
<Ok>
```

### Static IP Address

```
Do you want to use your current network settings as a static  address?
IP address:    192.168.0.188/24  
Gateway:       192.168.0.1  
<Ok>
```

### FYI: IP Conflict

```
It is possible your router could still try to assign this IP to a  device, which would cause a conflict.  But in most cases the      
router is smart enough to not do that.                           
If you are worried, either manually set the address, or modify the
DHCP reservation pool so it does not include the IP you want.   
It is also possible to use a DHCP reservation, but if you are    
going to do that, you might as well set a static address.
<Ok>
```

```
Do you wish to install the web admin interface?
(*) On (Recommended)                                            
( ) Off
<Ok>
```

```
Do you wish to install the web server (lighttpd) and required PHP modules? 
NB: If you disable this, and, do not have an existing web server and required PHP modules (sqlite3 xml json intl) installed, the web interface will not function. Additionally the web server user needs to be member of the "pihole" group for full functionality.
(*) On (Recommended)                                            
( ) Off
<Ok>
```

```
Do you want to log queries?
(*) On (Recommended)                                            
( ) Off
<Ok>
```

```
Select a privacy mode for FTL. 
https://docs.pi-hole.net/ftldns/privacylevels/
(*) 0  Show everything                                          
( ) 1  Hide domains                                             
( ) 2  Hide domains and clients                                 
( ) 3  Anonymous mode   
<Ok>
```

### Installation Complete!

```
•	Configure your devices to use the Pi-hole as their DNS server using:                                                                                                 
IPv4:        192.168.0.188                                         
IPv6:        Not Configured                                                                                                        
If you set a new IP address, you should restart the Pi.            
The install log is in /etc/pihole.                                 
View the web interface at http://pi.hole/admin or                  
http://192.168.0.188/admin                                         
Your Admin Webpage login password is unchanged
<Ok>
```

### Run the following command to change the Pi-Hole admin password

```
sudo pihole -a -p
```

### Adding a new adlist sources

```
https://hosts.oisd.nl/
https://firebog.net/ *
youtube-ui.l.google.com
www.youtube-nocookie.com
ttps://raw.githubusercontent.com/imkarthikk/pihole-facebook/master/pihole-facebook.txt
https://raw.githubusercontent.com/CamelCase11/UnifiedHosts/master/hosts.all

```
