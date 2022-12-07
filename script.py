import os
from threading import Thread, Lock
import time
import subprocess
import random

def varia(pesi,coeff):
    ret=[0,0,0,0]
    rval=(random.random()-0.5)*coeff
    ret[0]=pesi[0]+int(rval)
    rval=(random.random()-0.5)*coeff
    ret[1]=pesi[1]+int(rval)
    rval=(random.random()-0.5)*coeff
    ret[2]=pesi[2]+int(rval)
    rval=(random.random()-0.5)*coeff
    ret[3]=pesi[3]+int(rval)
    return ret

def test(pesi1,pesi2):
    print("inizio test")
    vincitore=0;
    vincitoreritorno=0;
    s=subprocess.Popen(["java","-jar","Hadron.jar"], stdout=subprocess.PIPE)
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco\\.jdks\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\\Francesco\\IdeaProjects\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901",str(pesi1[0]),str(pesi1[1]),str(pesi1[2]),str(pesi1[3])],stdout=subprocess.DEVNULL)
    #p1=Thread(target=os.system,args=(" C:\\Users\\Francesco\\.jdks\openjdk-19.0.1\\bin\\java.exe  -classpath C:\\Users\\Francesco\\IdeaProjects\\hadron-ai\\out\\production\\hadron-ai hadron.ExperimentalPlayer 127.0.0.1 8901",pesi1[0],pesi1[1],pesi1[2],pesi1[3]))
    #Thread(os.system,(" C:\\Users\\Francesco\\.jdks\openjdk-19.0.1\\bin\\java.exe  -classpath C:\\Users\\Francesco\\IdeaProjects\\hadron-ai\\out\\production\\hadron-ai hadron.Player 127.0.0.1 8901",))
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco\\.jdks\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\\Francesco\\IdeaProjects\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901", str(pesi2[0]),str(pesi2[1]),str(pesi2[2]),str(pesi2[3])],stdout=subprocess.DEVNULL)

    output=s.stdout.read(-1).decode("utf-8")
    var1=output.find("White wins - Black loses")
    var2=output.find("Black wins - White loses")
    if var1 > 0:
        vincitore=1
    elif var2 >0:
        vincitore=2
    s.wait();
    print("cambio campo test")
    s=subprocess.Popen(["java","-jar","Hadron.jar"], stdout=subprocess.PIPE)
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco\\.jdks\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\\Francesco\\IdeaProjects\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901",str(pesi2[0]),str(pesi2[1]),str(pesi2[2]),str(pesi2[3])],stdout=subprocess.DEVNULL)
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco\\.jdks\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\\Francesco\\IdeaProjects\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901", str(pesi1[0]),str(pesi1[1]),str(pesi1[2]),str(pesi1[3])],stdout=subprocess.DEVNULL)
    output=s.stdout.read(-1).decode("utf-8")
    var1=output.find("White wins - Black loses")
    var2=output.find("Black wins - White loses")

    print("fine test")
    if var1 > 0:
        vincitoreritorno=2
    elif var2 >0:
        vincitoreritorno=2

    if(vincitore==vincitoreritorno):
        return vincitore;
    return 0;


pesi1=[1,1,1,1]
pesi2=[-1,-1,-1,-1]

pesi1=varia(pesi1,50)
pesi1=varia(pesi2,50)
coeff=50
passi=10
print("ricerca migliori pesi")
for passo in range(passi):

    val =test(pesi1, pesi2)
    vinc="nessuno"
    if val == 1:
        vinc="1"
        pesi2=varia(pesi1,coeff)
    elif  val == 2:
        vinc="2"
        pesi1=varia(pesi2,coeff)
    else :
        pesi1=varia(pesi1,coeff/2)
        pesi2=varia(pesi2,coeff/2)
    print("vincitore: "+vinc)
    print(pesi1,pesi2)
    coeff= coeff/1.2
