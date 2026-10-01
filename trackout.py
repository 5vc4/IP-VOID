import urllib.request,json
A="http://ip-api.com/json/"
F="status,message,query,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,hosting"
R="\033[91m";Y="\033[93m";B="\033[96m";W="\033[97m";Z="\033[0m"

def check(ip=""):
 try:
  d=json.load(urllib.request.urlopen(A+ip+"?fields="+F,timeout=8))
  if d.get("status")!="success": print(R+"[!] "+d.get("message","Error")+Z);return
  print(R+"\n"+"="*35+Z)
  print(Y+"IP VOID"+Z)
  print(R+"="*35+Z)
  for k,v in d.items():
   if k not in ("status","message"): print(f"{W}{k:12}{Z}: {v}")
 except Exception as e: print(R+"[!] "+str(e)+Z)

def multi():
 try:
  for ip in open(input("Plik: ")):
   if ip.strip(): check(ip.strip())
 except Exception as e: print(R+"[!] "+str(e)+Z)

while 1:
 print(R+"\n╔════════════════════════════╗")
 print(Y+"║          IP VOID            ║")
 print(R+"╠════════════════════════════╣")
 print(W+"║ "+B+"[1]"+W+" IP / DOMAIN            ║")
 print("║ "+B+"[2]"+W+" MY IP                  ║")
 print("║ "+B+"[3]"+W+" MULTI IP               ║")
 print("║ "+B+"[0]"+W+" EXIT                   ║")
 print(R+"╚════════════════════════════╝"+Z)
 c=input(W+"> "+Z)
 if c=="0":break
 if c=="1":check(input("IP/domain: "))
 elif c=="2":check()
 elif c=="3":multi()
