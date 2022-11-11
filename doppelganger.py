import glob, subprocess

print ("Searching for Firefox profiles")
firefox = glob.glob('/home/**/.mozilla/firefox/**/cookies.sqlite', recursive=True)
firefox += glob.glob('/run/media/*/*/Users/*/AppData/*/Mozilla/Firefox/Profiles/*/cookies.sqlite', recursive=True)

for i in range(len(firefox)):
    print("%s | firefox: %s" % (i, firefox[i]))

profile = firefox[int(input("Select profile: "))][:-14]
subprocess.run(['firefox -profile "%s"' % (profile)], shell=True)
