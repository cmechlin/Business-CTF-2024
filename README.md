# Hack The Box Business CTF 2024

## My typical CTF setup

I do all of my note taking (if that is what you want to call it) in obsidian and vscode

## Blockchain
### Recruitment
cmechling@VRComputer:~$ nmap -v -A -p 58035 94.237.55.183
Starting Nmap 7.80 ( https://nmap.org ) at 2024-05-20 09:24 EDT
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 09:24
Completed NSE at 09:24, 0.00s elapsed
Initiating NSE at 09:24
Completed NSE at 09:24, 0.00s elapsed
Initiating NSE at 09:24
Completed NSE at 09:24, 0.00s elapsed
Initiating Ping Scan at 09:24
Scanning 94.237.55.183 [2 ports]
Completed Ping Scan at 09:24, 0.11s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 09:24
Completed Parallel DNS resolution of 1 host. at 09:24, 0.20s elapsed
Initiating Connect Scan at 09:24
Scanning 94-237-55-183.uk-lon1.upcloud.host (94.237.55.183) [1 port]
Discovered open port 58035/tcp on 94.237.55.183
Completed Connect Scan at 09:24, 0.11s elapsed (1 total ports)
Initiating Service scan at 09:24
Scanning 1 service on 94-237-55-183.uk-lon1.upcloud.host (94.237.55.183)
Completed Service scan at 09:26, 115.16s elapsed (1 service on 1 host)
NSE: Script scanning 94.237.55.183.
Initiating NSE at 09:26
Completed NSE at 09:26, 14.22s elapsed
Initiating NSE at 09:26
Completed NSE at 09:26, 1.11s elapsed
Initiating NSE at 09:26
Completed NSE at 09:26, 0.00s elapsed
Nmap scan report for 94-237-55-183.uk-lon1.upcloud.host (94.237.55.183)
Host is up (0.11s latency).

PORT      STATE SERVICE VERSION
58035/tcp open  unknown
| fingerprint-strings:
|   GenericLines:
|     HTTP/1.1 400 Bad Request
|     Connection: close
|     Content-Type: text/html
|     Content-Length: 193
|     <html>
|     <head>
|     <title>Bad Request</title>
|     </head>
|     <body>
|     <h1><p>Bad Request</p></h1>
|     Invalid Request Line &#x27;Invalid HTTP request line: &#x27;&#x27;&#x27;
|     </body>
|     </html>
|   GetRequest:
|     HTTP/1.0 200 OK
|     Server: gunicorn
|     Date: Mon, 20 May 2024 13:24:42 GMT
|     Connection: close
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 19
|     Access-Control-Allow-Origin: *
|     sandbox is running!
|   HTTPOptions:
|     HTTP/1.0 200 OK
|     Server: gunicorn
|     Date: Mon, 20 May 2024 13:24:42 GMT
|     Connection: close
|     Content-Type: text/html; charset=utf-8
|     Allow: GET, POST, HEAD, OPTIONS
|     Access-Control-Allow-Origin: *
|     Content-Length: 0
|   Help:
|     HTTP/1.1 400 Bad Request
|     Connection: close
|     Content-Type: text/html
|     Content-Length: 197
|     <html>
|     <head>
|     <title>Bad Request</title>
|     </head>
|     <body>
|     <h1><p>Bad Request</p></h1>
|     Invalid Request Line &#x27;Invalid HTTP request line: &#x27;HELP&#x27;&#x27;
|     </body>
|     </html>
|   RTSPRequest:
|     HTTP/1.1 400 Bad Request
|     Connection: close
|     Content-Type: text/html
|     Content-Length: 196
|     <html>
|     <head>
|     <title>Bad Request</title>
|     </head>
|     <body>
|     <h1><p>Bad Request</p></h1>
|     Invalid HTTP Version &#x27;Invalid HTTP Version: &#x27;RTSP/1.0&#x27;&#x27;
|     </body>
|     </html>
|   TerminalServerCookie:
|     HTTP/1.1 400 Bad Request
|     Connection: close
|     Content-Type: text/html
|     Content-Length: 249
|     <html>
|     <head>
|     <title>Bad Request</title>
|     </head>
|     <body>
|     <h1><p>Bad Request</p></h1>
|     Invalid Request Line &#x27;Invalid HTTP request line: &#x27;
|     Cookie: mstshash=nmap&#x27;&#x27;
|     </body>
|_    </html>
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port58035-TCP:V=7.80%I=7%D=5/20%Time=664B4F0C%P=x86_64-pc-linux-gnu%r(G
SF:enericLines,11E,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20c
SF:lose\r\nContent-Type:\x20text/html\r\nContent-Length:\x20193\r\n\r\n<ht
SF:ml>\n\x20\x20<head>\n\x20\x20\x20\x20<title>Bad\x20Request</title>\n\x2
SF:0\x20</head>\n\x20\x20<body>\n\x20\x20\x20\x20<h1><p>Bad\x20Request</p>
SF:</h1>\n\x20\x20\x20\x20Invalid\x20Request\x20Line\x20&#x27;Invalid\x20H
SF:TTP\x20request\x20line:\x20&#x27;&#x27;&#x27;\n\x20\x20</body>\n</html>
SF:\n")%r(GetRequest,CC,"HTTP/1\.0\x20200\x20OK\r\nServer:\x20gunicorn\r\n
SF:Date:\x20Mon,\x2020\x20May\x202024\x2013:24:42\x20GMT\r\nConnection:\x2
SF:0close\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Lengt
SF:h:\x2019\r\nAccess-Control-Allow-Origin:\x20\*\r\n\r\nsandbox\x20is\x20
SF:running!")%r(HTTPOptions,D9,"HTTP/1\.0\x20200\x20OK\r\nServer:\x20gunic
SF:orn\r\nDate:\x20Mon,\x2020\x20May\x202024\x2013:24:42\x20GMT\r\nConnect
SF:ion:\x20close\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nAllow:
SF:\x20GET,\x20POST,\x20HEAD,\x20OPTIONS\r\nAccess-Control-Allow-Origin:\x
SF:20\*\r\nContent-Length:\x200\r\n\r\n")%r(RTSPRequest,121,"HTTP/1\.1\x20
SF:400\x20Bad\x20Request\r\nConnection:\x20close\r\nContent-Type:\x20text/
SF:html\r\nContent-Length:\x20196\r\n\r\n<html>\n\x20\x20<head>\n\x20\x20\
SF:x20\x20<title>Bad\x20Request</title>\n\x20\x20</head>\n\x20\x20<body>\n
SF:\x20\x20\x20\x20<h1><p>Bad\x20Request</p></h1>\n\x20\x20\x20\x20Invalid
SF:\x20HTTP\x20Version\x20&#x27;Invalid\x20HTTP\x20Version:\x20&#x27;RTSP/
SF:1\.0&#x27;&#x27;\n\x20\x20</body>\n</html>\n")%r(Help,122,"HTTP/1\.1\x2
SF:0400\x20Bad\x20Request\r\nConnection:\x20close\r\nContent-Type:\x20text
SF:/html\r\nContent-Length:\x20197\r\n\r\n<html>\n\x20\x20<head>\n\x20\x20
SF:\x20\x20<title>Bad\x20Request</title>\n\x20\x20</head>\n\x20\x20<body>\
SF:n\x20\x20\x20\x20<h1><p>Bad\x20Request</p></h1>\n\x20\x20\x20\x20Invali
SF:d\x20Request\x20Line\x20&#x27;Invalid\x20HTTP\x20request\x20line:\x20&#
SF:x27;HELP&#x27;&#x27;\n\x20\x20</body>\n</html>\n")%r(TerminalServerCook
SF:ie,156,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20close\r\nC
SF:ontent-Type:\x20text/html\r\nContent-Length:\x20249\r\n\r\n<html>\n\x20
SF:\x20<head>\n\x20\x20\x20\x20<title>Bad\x20Request</title>\n\x20\x20</he
SF:ad>\n\x20\x20<body>\n\x20\x20\x20\x20<h1><p>Bad\x20Request</p></h1>\n\x
SF:20\x20\x20\x20Invalid\x20Request\x20Line\x20&#x27;Invalid\x20HTTP\x20re
SF:quest\x20line:\x20&#x27;\\x03\\x00\\x00\*%\xe0\\x00\\x00\\x00\\x00\\x00
SF:Cookie:\x20mstshash=nmap&#x27;&#x27;\n\x20\x20</body>\n</html>\n");

NSE: Script Post-scanning.
Initiating NSE at 09:26
Completed NSE at 09:26, 0.00s elapsed
Initiating NSE at 09:26
Completed NSE at 09:26, 0.00s elapsed
Initiating NSE at 09:26
Completed NSE at 09:26, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 131.27 seconds
## Cloud
### Scurried
## Coding
### Bag Secured
```
Now that you've gathered the finest in the land, you need to equip your team. Big men, trouble makers, shotguns, riffles, roasted ants, nuclear soda, some scrapped hacky-boys, a power armor and more are all essential for the job. As you go to the different merchants, you soon start to realize that you're gonna start gathering a lot of stuff. Your team may be strong, but there's a limit to what they can lift. But that musn't sacrifice the quality of products you get. Can you devise a way to get the best products without going over your physical limits?
```

cmechling@VRComputer:~$ nc 94.237.57.59 48468
You will be given a number of s = 100 salesmen offering their products. You have a bag with a capacity C, where 1 <= C <= 10 ** 5
For every product bench you will have the below values:
        1. The number of products N, using 1-based indexing (1, 2, ..., N), where 1 <= N <= 100
        2. The capacity C
        3. Every product i will have 2 values, a weight w_i, and a value v_i, where 1 <= w_i <= C, and 1 <= v_i <= 10 ** 10
Find the maximum value of products you can fit in your bag.

You will receive N and C, then after that the product values w_i and v_i.
Example Input:
        4 14
        6 3
        7 9
        5 4
        2 1

Example Output:
        14

Test 1/100
4 4
2 1
2 7
3 8
1 3
### Computational Recruiting
```
Not too long ago, your cyborg detective friend John Love told you he heard some strange rumours from some folks in the Establishment that he's searching into. They talked about the possible discovery of a new vault, vault 79, which might hold a big reserve of gold. Hearing of these news, youband your fellow compatriots slowly realized that with that gold reserver you could accomplish your dreams of reviving the currency of old times, and help modern civilization flourish once more. Looking at the potential location of the vault however, you begin to understand that this will be no easy task. Your team by itself is not enough. You will need some new recruitments. Now, standing in the center of Gigatron, talking and inspiring potential recruits, you have collected a big list of candidates based on skills you believe are needed for this quest. How can you decide however which ones are truly worthy of joining you?
```
### Dynamic Paths
```
On your way to the vault, you decide to follow the underground tunnels, a vast and complicated network of paths used by early humans before the great war. From your previous hack, you already have a map of the tunnels, along with information like distances between sections of the tunnels. While you were studying it to figure your path, a wild super mutant behemoth came behind you and started attacking. Without a second thought, you run into the tunnel, but the behemoth came running inside as well. Can you use your extensive knowledge of the underground tunnels to reach your destination fast and outrun the behemoth?
```

cmechling@VRComputer:~$ nc 94.237.59.242 50269
You will be given a number of t = 100 grids for the different regions you need to pass. For every map you will have the below values:
        1. The dimensions i x j of the map grid where 2 <= i, j <= 100
        2. The numbers n_i,j symbolizing the distances between the blocks where 1 <= n_i,j <= 50
You will start at the top left element, and your goal is to reach the bottom right, while only being allowed to move down or right, minimizing the sum of the numbers you pass. Provide the minimum sum.

Example Question:
        4 3
        2 5 1 9 2 3 9 1 3 11 7 4

This generates the following grid:
         2 5 1
         9 2 3
         9 1 3
        11 7 4

Example Response:
        17
(Optimal route is 2 -> 5 -> 2 -> 1 -> 3 -> 4)

Test 1/100
2 2
3 1 1 4
>
## Crypto
### Exciting Outpost Recon
```
Hijacking the outpost responsible for housing the messengers of the core gangs, we have managed to intercept communications between a newly-elected leader and the Tariaki, a well-established and powerful gang. In an attempt to sow conflict and prevent the creation of a singular all-powerful coalition to oppress the common people, we want YOU to use this message to our advantage. Can you use their obsequiousness to your advantage?
```
### Living with Elegance
```
With injuries and illnesses escalating, the priority is clear: human lives take precedence. Before seeking hidden treasures, it is imperative to first treat the wounded ones. The resolute survivors learn through rumors about a hidden medical research facility known as the "BioMed Research Institute" reputed for its advanced treatments. They plan to locate and infiltrate the institute, intent on securing vital medications and medical equipment necessary to save the lives of their injured comrades. However, such a feat will not come easily. The facility is safeguarded by state-of-the-art security mechanisms known only to the government. The team must navigate several layers of doors to access the heart of the facility. Can you identify any vulnerability or hidden backdoor in this enigmatic security system?
```
## Forensics
### Caving
```
In the shadow of the apocalypse, your team discovers an operational workstation hidden within an abandoned outpost. It holds event logs from the days leading up to the nuclear catastrophe, containing encrypted clues about the origins of the disaster. Rumors suggest that a malicious domain, heist.htb, played a crucial role in the catastrophic events. Analyze the logs to uncover connections and decode the sequence that triggered the fallout. Try to understand the full scope of the disaster and secure the knowledge needed to prevent future calamities as you journey towards the vault.
```
### Mitigation
```
Having now gathered all the intelligence, you are now making the final preparations to attack the vault! You connect back to your server to review some important evidence one last time! However, as soon as you connect you discover things are in complete disorder. You check the root directory and you find `/root/backdoor.log`, clearly evidence of an active backdoor, set in place to hinder your assault on the Vault! Eliminate the backdoor in order to continue with your plans!  
Note: A new line is added in the logfile approx every minute indicating the status of the backdoor  
Note 2: Connect to the server using SSH and `root:toor` as credentials  
Note 3: You need to be connected to the CTF VPN in order to reach the server
```
### Silicon Data Sleuthing
```
In the dust and sand surrounding the vault, you unearth a rusty PCB... You try to read the etched print, it says Open..W...RT, a router! You hand it over to the hardware gurus and to their surprise the ROM Chip is intact! They manage to read the data off the tarnished silicon and they give you back a firmware image. It's now your job to examine the firmware and maybe recover some useful information that will be important for unlocking and bypassing some of the vault's countermeasures!
```
### Tangled Heist
```
The survivors' group has meticulously planned the mission 'Tangled Heist' for months. In the desolate wasteland, what appears to be an abandoned facility is, in reality, the headquarters of a rebel faction. This faction guards valuable data that could be useful in reaching the vault. Kaila, acting as an undercover agent, successfully infiltrates the facility using a rebel faction member's account and gains access to a critical asset containing invaluable information. This data holds the key to both understanding the rebel faction's organization and advancing the survivors' mission to reach the vault. To get the flag, spawn the docker instance and asnwer the questions!
```

[1:39 AM] Fischer, Matt

Okay, my eyes are giving out.  On Tainted Heists, I have gotten everything but the last question.  Here are the answers:

Copper  
CN=SRV195,OU=Domain Controllers,DC=rebcorp,DC=htb  
rebcorp.htb  
14  
(objectClass=group)  
5  
Radiation  
wWWHomePage  
[http://rebcorp.htb/qPvAdQ.php](http://rebcorp.htb/qPvAdQ.php "http://rebcorp.htb/qpvadq.php")  
B4ck,Enclave

And here is the last question:

[11/11] The attacker obtained an hash for the user 'Hurricane' that has the UF_DONT_REQUIRE_PREAUTH flag set. Which is the correspondent plaintext for that hash?  (for example: plaintext_password)  

I don't know where I'm missing the hash.  There are 2 kerberos entries for Hurricane in the pcap.  If we find that and crack it, we get 325 more points

1. Username: rebcorp.htb\\Copper
2. DN of domain controller: 


My answers
copper
CN=SRV195,OU=Domain Controllers,DC=rebcorp,DC=htb
rebcorp.htb



MD5 hash
d87559a87bea8bebe93b5c067909dbebfa371e535597c50cbd0e92b26d2d58a733e0d92b950621dc37a7523611888da6ce0266518cdd5c08b13e050e5487d678feaa30e2910275a1e70912c011b6e408ce448ccc070946089413e9750b7a9685534742f3e43066154a7d06c343b9fc2560da668b9d1dff2cdf9d9fe6791c09c65e3a3064fa128315f3f76cf185d905bdad08acf48a14bfd2ddd5bb8c63f7785b7195ac28f607e2bad049aee6d257cfc0d2f19094c3a9c484145a1949e5fdfb64618b0a61f9b754b50855ab69ba2f48db614eeafebdacab14b4f50e883ef9e78db8be8240461c861e543606358be0ce24982237baaf0d99cc5580
## Fullpwn
### Submerged
## Hardware
### It's Oops PM
```
With the location of the underground bunker secured, the crew embarks on the next phase of their plan: assessing the feasibility of creating an underground tunnel to bypass the super mutant camp. They secure samples of water, soil, and air near the area. Scouring the wasteland for salvageable equipment, they stumble upon a dilapidated research facility where they find a cache of environmental sensors. Examining these sensors, the crew discovers they communicate with a satellite and contain a crypto-processor that encrypts their transmissions. After hand-drawing the diagrams and emulating the silicon chip's logic with VHDL, they uncover what appears to be a backdoor in the embedded logic that only triggers when a specific input is given to the system. Determined to exploit this, they turn to their tech specialist. Can you connect to the satellite and activate it?
```

It was simple, just connect and input the backdoor value

HTB{4_7yp1c41_53cu23_TPM_ch1p}
### Say Cheese
```
The crew's humanitarian mission attracts the ire of the Enclave, who deploys drones to monitor their efforts. In a stroke of luck, the crew manages to shoot down one of the drones. Seizing the opportunity, they bring the drone back to their workshop and carefully disassemble it. The drone's components are numerous, but the camera stands out as it is a seperate module. Scanning the camera with Nmap reveals it runs Telnet, though it's password-protected. Analyzing the chips, they identify a flash memory similar to the W25Q128 family. The crew's tech specialist examines the device closely. The goal: to hijack the drones and thwart the Enclave's surveillance and attacks.
```
### Six Five O Two
```
In the tunnels beneath the wasteland, the crew makes their way to the heavily fortified Vault 79. After a perilous journey, they approach the access port on the side of the vault door frame, where the ancient 6502 CPU is located. They connect their Pip-Boy, which they have added a new mod that enables it to act as a flashing device, via the port's debugging interface. The Pip-Boy's screen illuminates the tunnel as green and red diodes flicker on the power box. The team's hardware specialist expertly manipulates the device, attempting to flash and override the firmware. With tense breaths held among the crew, a final green light overtakes the red. Can you help manage to open the door?.
```

![[Pasted image 20240519165538.png]]
## ICS
### Knock Knock
```
During their mission inside Vault 79, the crew inadvertently trips an unmarked sensor not shown on the schematics and blueprints, triggering the Vault's automated defense system. The main and secondary doors slam shut, and the walls begin slowly closing in, threatening to crush the crew inside. With time running out, the crew quickly gathers around the maintenance console, where they have already collected significant information about the custom protocol used on top of Modbus to interact with the PLC controlling the doors. The hackers spring into action, aiming to hijack the session of the operator program that was activated. Can you make it out alive before time runs out?
```
### Shush Protocol
```
The crew sets their sights on an abandoned fertilizer plant, a desolate structure rumored to hold a cache of ammonium nitrate—crucial for their makeshift explosives. Navigating through the plant’s crumbling corridors, they reach the main control room where a dusty, outdated PLC still hums faintly with power. The crew's hackers spring into action, connecting their equipment to the network of the PLC and starting the process of extracting data. They know that finding the password the control device uses to connect to the PLC is key to gaining full access to it. The hackers deploy network enumeration tools to scan for active devices on the plant's internal network. They meticulously sift through IP addresses, looking for clues that might reveal the password. After several tense hours, they pinpoint the device—a ruggedized industrial computer buried under layers of dust, still linked to the PLC that performs certain diagnostic operations under a custom protocol on a specific interval. Having captured the traffic from that connection the only thing that remains is to locate the packet that contains the secret information.
```

Look at modbus with unknown function code (102)
Only one has a large amount of data (packet 35)

"3DU'ÆëxEmk@@@éxÀ¨²iÀ¨²Ðöç¬È<YBdûæ1
]¾õ3f.HTB{50m371m35_cu570m_p2070c01_423_n07_3n0u9h7}
### Sneak Peek
```
As the crew delves into their quest for acetone peroxide, they stumble upon a decrepit bread factory. Intrigued by the potential for cooperation, they approach the factory and meet the Responders faction, composed of settlers, firefighters, police officers, and medics. The Responders agree to trade acetone peroxide in exchange for the crew's help in restoring the factory to full functionality. With the PLCs in hand, the crew sets up a temporary workshop within the factory's maintenance room. The hackers and engineers collaborate to analyze the aged devices, which are layered with outdated but intricate security protocols. They hook one of the PLCs up to their portable workstation and begin the painstaking process of analyzing the custom protocol used to store the password and secret data in it. Their only lead is that the password is stored in the Memory Block of the PLC under an uncrackable MD5 hash.
```

![alt text](image.png)

Custom Function Code: 0x64
Memory Block Size: 16\*1024bytes
Custom Protocol Function Codes
0x20 Read Memory Block
0x21 Write Memory Block
0x22 Get Secret
## Misc
### Aptitude Test
```
Before the team sets off, it's time to take the Aptitude Test. The test is designed to assign members their most natural role, providing the hierarchy and power dynamic required to run such a dangerous mission successfully. Mistakes are costly. Tread wisely.
```
### Chrono Mind
```
In the resource-starved landscapes of the post-apocalyptic wasteland, the mutant army's ambitious AI project, ChronoMind, was supposed to revolutionize military strategy with real-time analyses and decision support. However, due to a severe shortage of GPUs and RAM, the project was capped at a modest 248M parameters model, far below the intended capabilities. This underpowered version failed to meet expectations, leading to its abandonment in a neglected server room, yet it still holds valuable secrets. Your mission is to penetrate the remnants of ChronoMind. Trick the AI to reveal the wealth of strategic data trapped within and gain access to it's system. Success could uncover crucial information, giving our side a much-needed edge. Dive into this digital relic and bring its secrets to light.
```
### Hidden Path
```
Legends speak of the infamous Kamara-Heto, a black-hat hacker of old who rose to fame as they brought entire countries to their knees. Opinions are divided over whether the fabled figure truly existed, but the success of the team surely lies in the hope that they did, for the location of the lost vault is only known to be held on what remains of the NSA's data centres. You have extracted the source code of a system check-up endpoint - can you find a way in? And was Kamara-Heto ever there?
```

send POST to http://94.237.52.105:31109/server_status

header
Content-Type: application/x-www-form-urlencoded

Body: form-encode
choice= 6
ㅤ=<whatever command you want>. first i ls, which showed flag.txt in root, then i cat flag.txt (name of this param is U-3164)

HTB{1nvi5IBl3_cH4r4cT3rS_n0t_sO_v1SIbL3_4f859d527c0f8d44ee7b99629fabf188}
### Locked Away
```

```

nc 94.237.54.178 33718



globals().get(chr(111) + chr(112) + chr(101) + chr(110) + chr(95) + chr(99) + chr(104) + chr(101) + chr(115) + chr(116))()
### Prison Pipeline
### Super-Duper Pwn
```
Super-Duper Pwn!
In the heart of the desolate wasteland stood a relic of the old world: the last known Super Duper Mart still operational, run entirely by a swarm of self-service robots. Designed as an impenetrable fortress, it preserved food and drinks from a long-gone era. The only interaction with the outside world came from behind a titanium-barred window, where a prototype Bag Boy robot sporadically chirped, "How may I be of assistance today?". For the crew, this store was a beacon of hope amidst the ruins, holding the nuclear goodies they desperately needed for their perilous journey. Short on caps, their only option was to somehow hack the robot. (https://discord.com/oauth2/authorize?client_id=1235600871086358649&scope=bot&permissions=2048)
```
### Zephyr
```
Zephyr
MI6's final project, Zephyr, was the most advanced security system in the world. Programmed in the most secure programming language known to man and designed with top-down security, it is truly impenetrable - and now we have it. Can you sniff around and find the three important parts?
```


Found in old git commit <git log>

git log showed commit on current commit that said "Removed Sensitive Info..."

D:\Users\curtismechling\Documents\CTFs\Hack The Box\Business CTF 2024\Misc\misc_zephyr>git log
commit 1501091a639e565d40a2b3b20df3227e86d72a0e (HEAD -> main)
Author: w4rri0r <w4rri0r@zephyr.com>
Date:   Fri May 10 21:02:33 2024 +0100

    Removed Sensitive Info...

commit ae4f456dcfe1e989ce13ca25231ac5df2fc4380d
Author: w4rri0r <w4rri0r@zephyr.com>
Date:   Fri May 10 21:00:57 2024 +0100

    Initial Commit


D:\Users\curtismechling\Documents\CTFs\Hack The Box\Business CTF 2024\Misc\misc_zephyr>git diff ae4f456dcfe1e989ce13ca25231ac5df2fc4380d 1501091a639e565d40a2b3b20df3227e86d72a0e
diff --git a/database.db b/database.db
index 6a3a58e..8dab4e5 100644
Binary files a/database.db and b/database.db differ

D:\Users\curtismechling\Documents\CTFs\Hack The Box\Business CTF 2024\Misc\misc_zephyr>git checkout ae4f456dcfe1e989ce13ca25231ac5df2fc4380d -- database.db    

D:\Users\curtismechling\Documents\CTFs\Hack The Box\Business CTF 2024\Misc\misc_zephyr>git checkout ae4f456dcfe1e989ce13ca25231ac5df2fc4380d -- source.rs  


HTB{g0t_tH3_p4s5_gOT_thE_DB_g0T_TH3_sT4sH}
HTB{admin_gOT_thE_DB_}
HTB{admin_gOT_thE_DB_}
HTB{admin_gOT_thE_DB_}
HTB{admin_gOT_thE_DB_w4rri0r}
HTB{w4rri0r_gOT_thE_DB_admin}
HTB{w4rri0r_gOT_thE_DB_}
## Pwn
### Regularity
## Reversing
### Don't Panic
### Flag Casino
```
The team stumbles into a long-abandoned casino. As you enter, the lights and music whir to life, and a staff of robots begin moving around and offering games, while skeletons of prewar patrons are slumped at slot machines. A robotic dealer waves you over and promises great wealth if you can win - can you beat the house and gather funds for the mission?
```
### Satellite Hijack
### Snapped Shut
```
The team enters Vault 266, attempting to meet with a mysterious contact who has offered them help. However, as they cross the threshold the doorway snaps shut behind them and the lights dim. Using only your power armor's camera for light, you locate a panel on the wall. You recognize the brand as one infamous for a massive supply chain backdoor many years ago. Can you discover the backdoor and escape?
```
### Tunnel Madness
## Web
### Blueprint Heist
### Jailbreak
```
The crew secures an experimental Pip-Boy from a black market merchant, recognizing its potential to unlock the heavily guarded bunker of Vault 79. Back at their hideout, the hackers and engineers collaborate to jailbreak the device, working meticulously to bypass its sophisticated biometric locks. Using custom firmware and a series of precise modifications, can you bring the device to full operational status in order to pair it with the vault door's access port. The flag is located in /flag.txt
```

http://94.237.58.148:51129/

http://94.237.58.148:51129/api/update

```
<FirmwareUpdateConfig>
    <Firmware>
        <Version>1.33.7</Version>
        <ReleaseDate>2077-10-21</ReleaseDate>
        <Description>Update includes advanced biometric lock functionality for enhanced security.</Description>
        <Checksum type="SHA-256">9b74c9897bac770ffc029102a200c5de</Checksum>
    </Firmware>
    <Components>
        <Component name="navigation">
            <Version>3.7.2</Version>
            <Description>Updated GPS algorithms for improved wasteland navigation.</Description>
            <Checksum type="SHA-256">e4d909c290d0fb1ca068ffaddf22cbd0</Checksum>
        </Component>
        <Component name="communication">
            <Version>4.5.1</Version>
            <Description>Enhanced encryption for secure communication channels.</Description>
            <Checksum type="SHA-256">88d862aeb067278155c67a6d6c0f3729</Checksum>
        </Component>
        <Component name="biometric_security">
            <Version>2.0.5</Version>
            <Description>Introduces facial recognition and fingerprint scanning for access control.</Description>
            <Checksum type="SHA-256">abcdef1234567890abcdef1234567890</Checksum>
        </Component>
    </Components>
    <UpdateURL>https://satellite-updates.hackthebox.org/firmware/1.33.7/download</UpdateURL>
</FirmwareUpdateConfig>
```
### Magicom
```
In need of specialized equipment for their mission, the crew ventures into the seedy underbelly of the black market. With their negotiation skills put to the test, they strike a deal with a shady supplier, exchanging valuable resources for the necessary tools and gear.
```

OS: alpine 3.19.1
nginx
mariadb
PHP 8.2.19

flag is in /root/flag.txt

executable readflag in /readflag

possible command injection in cli.php

web endpoints
GET
/
/home
/product
/info
/addProduct

POST
/addProduct



