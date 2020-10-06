import paramiko
import sys




client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.load_system_host_keys()

output=""

try :

    client.connect("10.14.48.60" , username="toor4nsn", password="oZPS0POrRieRtu", port= 22)
    print ("connection established")
except Exception as e:
    print("connection failed")

stdin, stdout, stderr = client.exec_command('chk adet')

stdout = stdout.readlines()

client.close()

for line in stdout:

    output = output + line

assert output != ""

#assert "failed : 0" in output , "ABIO not ready"

if "failed : 0" in output :
    print("ABIO is ready")


with open("ABIO_status.txt", "w") as ABIO_status:
    ABIO_status.write(output)







#if output != "":
    #print (output)
#else:
    #print("no status back")

#stdin, stdout, stderr = client.exec_command('reboot')



#try:
        #client.ssh.exec_command('ls', timeout=5)

#except Exception as e:
        #print ("Connection lost")
