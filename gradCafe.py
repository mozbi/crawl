import urllib
import re

#htmlfile = urllib.urlopen("http://thegradcafe.com/survey/index.php?q=berkeley+ieor&t=a&o=d&pp=250")
htmlfile = urllib.urlopen("http://thegradcafe.com/survey/index.php?q=mit+mechanical+engineering&t=a&o=d&pp=250")
#htmlfile = urllib.urlopen("http://thegradcafe.com/survey/index.php?q=mit+mechanical+engineering&t=a&o=d&pp=250")
#htmlfile = urllib.urlopen("http://thegradcafe.com/survey/index.php?q=berkeley+computer+science&t=a&o=d&pp=250")
#htmlfile = urllib.urlopen("http://thegradcafe.com/survey/index.php?q=urbana+champaign+computer+science&t=a&o=d&pp=250")
#htmlfile = urllib.urlopen("http://thegradcafe.com/survey/index.php?q=princeton+finance&t=a&o=d&pp=250")
#htmlfile = urllib.urlopen("http://thegradcafe.com/survey/index.php?q=mit+finance&t=a&o=d&pp=250")
#htmlfile = urllib.urlopen("http://thegradcafe.com/survey/index.php?q=columbia+financial+engineering&t=a&o=d")
#htmlfile = urllib.urlopen("http://thegradcafe.com/survey/index.php?q=stanford+management+science&t=a&pp=250&o=d&p=1")

htmltext = htmlfile.read()
#print htmltext

regex = "<td class=\"instcol\">(.+?)\W*GRE Subject</strong>"

pattern = re.compile(regex)
entry = re.findall(pattern, htmltext)

for i in entry:
    i= i.replace("<td>", " ")
    i= i.replace("</td>", " ")
    i= i.replace("<span class=\"dAccepted\">", "\n")
    i= i.replace("<span class=\"dRejected\">", "\n")
    i= i.replace("</span>", " ")
    i= i.replace("<a class=\"extinfo\" href=\"#\"><span><strong>Under", "")
    i= i.replace("<br/><strong>", "\n")
    i= i.replace("</strong>", "")
    i= i.replace("<br/><strong", "")
    print i
    print "\n"

