import os
from threading import Thread, Lock
import time
import subprocess
import random

risultati =[0,0,0,0]

def varia(pesi,coeff):
    ret=[0,0,0,0,0]
    rval=(random.random()-0.5)*coeff
    ret[0]=pesi[0]+int(rval)
    rval=(random.random()-0.5)*coeff
    ret[1]=pesi[1]+int(rval)
    rval=(random.random()-0.5)*coeff
    ret[2]=pesi[2]+int(rval)
    rval=(random.random()-0.5)*coeff
    ret[3]=pesi[3]+int(rval)
    rval=(random.random()-0.5)*coeff
    ret[4]=pesi[4]+int(rval)
    return ret

def test(pesi1,pesi2):
    print("inizio test")
    print("Pesi :"+str(pesi1)+" VS " +str(pesi2) )
    vincitore=0;
    vincitoreritorno=0;
    s=subprocess.Popen(["java","-jar","Hadron.jar"], stdout=subprocess.PIPE)
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901",str(pesi1[0]),str(pesi1[1]),str(pesi1[2]),str(pesi1[3]),str(pesi1[4])],stdout=subprocess.DEVNULL)
    #p1=Thread(target=os.system,args=(" C:\\Users\\Francesco\\.jdks\openjdk-19.0.1\\bin\\java.exe  -classpath C:\\Users\\Francesco\\IdeaProjects\\hadron-ai\\out\\production\\hadron-ai hadron.ExperimentalPlayer 127.0.0.1 8901",pesi1[0],pesi1[1],pesi1[2],pesi1[3]))
    #Thread(os.system,(" C:\\Users\\Francesco\\.jdks\openjdk-19.0.1\\bin\\java.exe  -classpath C:\\Users\\Francesco\\IdeaProjects\\hadron-ai\\out\\production\\hadron-ai hadron.Player 127.0.0.1 8901",))
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901",str(pesi2[0]),str(pesi2[1]),str(pesi2[2]),str(pesi2[3]),str(pesi2[4])],stdout=subprocess.DEVNULL)

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
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901",str(pesi2[0]),str(pesi2[1]),str(pesi2[2]),str(pesi2[3]),str(pesi2[4])],stdout=subprocess.DEVNULL)
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901",str(pesi1[0]),str(pesi1[1]),str(pesi1[2]),str(pesi1[3]),str(pesi1[4])],stdout=subprocess.DEVNULL)
    output=s.stdout.read(-1).decode("utf-8")
    var1=output.find("White wins - Black loses")
    var2=output.find("Black wins - White loses")

    print("fine test")
    if var1 > 0:
        vincitoreritorno=2
    elif var2 >0:
        vincitoreritorno=1

    if(vincitore==vincitoreritorno):
        return vincitore;
    return 0;

def test_zero(pesi1):

    print("inizio zero test")
    vincitore=0;
    vincitoreritorno=0;
    s=subprocess.Popen(["java","-jar","Hadron.jar"], stdout=subprocess.PIPE)
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901",str(pesi1[0]),str(pesi1[1]),str(pesi1[2]),str(pesi1[3]),str(pesi1[4])],stdout=subprocess.DEVNULL)
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.DummyPlayer","127.0.0.1","8901"],stdout=subprocess.DEVNULL)

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
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.DummyPlayer","127.0.0.1","8901"],stdout=subprocess.DEVNULL)
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901",str(pesi1[0]),str(pesi1[1]),str(pesi1[2]),str(pesi1[3]),str(pesi1[4])],stdout=subprocess.DEVNULL)
    output=s.stdout.read(-1).decode("utf-8")
    var1=output.find("White wins - Black loses")
    var2=output.find("Black wins - White loses")

    print("fine test")
    if var1 > 0:
        vincitoreritorno=2
    elif var2 >0:
        vincitoreritorno=1

    if(vincitore==vincitoreritorno):
        return vincitore;
    return 0;

def test_random(pesi1):

    print("inizio random test")

    vincitore=0;
    vincitoreritorno=0;
    s=subprocess.Popen(["java","-jar","Hadron.jar"], stdout=subprocess.PIPE)
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901",str(pesi1[0]),str(pesi1[1]),str(pesi1[2]),str(pesi1[3]),str(pesi1[4])],stdout=subprocess.DEVNULL)
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.RandomPlayer","127.0.0.1","8901"],stdout=subprocess.DEVNULL)

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
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.RandomPlayer","127.0.0.1","8901"],stdout=subprocess.DEVNULL)
    time.sleep(0.5)
    subprocess.Popen(["C:\\Users\\Francesco De Luca\\.jdks\\openjdk-19.0.1\\bin\\java.exe","-classpath","C:\\Users\Francesco De Luca\\Documents\\GitHub\\hadron-ai\\out\\production\\hadron-ai","hadron.ExperimentalPlayer","127.0.0.1","8901",str(pesi1[0]),str(pesi1[1]),str(pesi1[2]),str(pesi1[3]),str(pesi1[4])],stdout=subprocess.DEVNULL)
    output=s.stdout.read(-1).decode("utf-8")
    var1=output.find("White wins - Black loses")
    var2=output.find("Black wins - White loses")

    print("fine test")
    if var1 > 0:
        vincitoreritorno=2
    elif var2 >0:
        vincitoreritorno=1

    if(vincitore==vincitoreritorno):
        return vincitore;
    return 0;

def genera_pesi_random():
    coeff=200
    ret=[0,0,0,0,0]
    rval=(random.random()-0.5)*coeff
    ret[0]=int(rval)
    rval=(random.random()-0.5)*coeff
    ret[1]=int(rval)
    rval=(random.random()-0.5)*coeff
    ret[2]=int(rval)
    rval=(random.random()-0.5)*coeff
    ret[3]=int(rval)
    rval=(random.random()-0.5)*coeff
    ret[4]=int(rval)
    return ret

def genera_pesi(n, pesi):
    coeff=100
    ret=[0,0,0,0,0]
    rval=(random.random()-0.5)*coeff
    ret[0]=pesi[0]+int(rval)
    rval=(random.random()-0.5)*coeff
    ret[1]=pesi[1]+int(rval)
    rval=(random.random()-0.5)*coeff
    ret[2]=pesi[2]+int(rval)
    rval=(random.random()-0.5)*coeff
    ret[3]=pesi[3]+int(rval)
    rval=(random.random()-0.5)*coeff
    ret[4]=pesi[4]+int(rval)
    for i in range(n):
        index=random.randint(0,n+1)
        while ret[index]==0:
            index=random.randint(0,n+1)
        ret[index]=0
    return ret

def vittoria(pesi,coeff,risultati):
    print("Vittoria heu\n")
    risultati[3]+=1
    risultati[0] +=1
    if random.random()>0.96:
        return varia(pesi, coeff)
    return pesi

def sconfitta(pesi,coeff,n,risultati):

    if n==0:
        print("Sconfitta contro Dummy")
    elif n==1:
        print("Sconfitta contro Random")
    elif n==2:
        print("Sconfitta contro pesi random")
    elif n==3:
        print("Sconfitta contro pesi mancanti random")
    else :
        print("Sconfitta")
    print("\n")
    risultati[3]=0
    risultati[1]+=1
    coeff=coeff*1.2
    return varia(pesi,coeff)

def pareggio(pesi,coeff,n,risultati):
    if n==0:
        print("Pareggio contro Dummy")

    elif n==1:
        print("Pareggio contro Random")
    elif n==2:
        print("Pareggio contro pesi random")
    elif n==3:
        print("Pareggio contro pesi mancanti random")
    else:
        print("Pareggio")
    risultati[3]=0
    risultati[2]+=1
    coeff=coeff*1.1
    return varia(pesi,coeff)

def statistica(risultati):
    return "\nVittorie: "+str(risultati[0])+"\nSconfitte: "+ str(risultati[1])+"\nPareggi: "+str(risultati[2])+"\nSerie: "+str(risultati[3])+"\n"


pesi1=[10 , -10 , -1000 , 500, -500]

coeff=10
passi=150
alfa=0.95
print("ricerca migliori pesi")
print(pesi1)
for passo in range(passi):
    type = int(random.uniform(0, 7))

    if type == 1:
        val =test_random(pesi1)
        if val == 1:
            pesi1=vittoria(pesi1,coeff,risultati)
        elif  val == 2:
            pesi1=sconfitta(pesi1,coeff,1,risultati)
        else:
            pesi1=pareggio(pesi1,coeff,1,risultati)

    if type == 0:
        val =test_zero(pesi1)
        if val == 1:
            pesi1=vittoria(pesi1,coeff,risultati)
        elif  val == 2:
            pesi1=sconfitta(pesi1,coeff,0,risultati)
        else:
            pesi1=pareggio(pesi1,coeff,0,risultati)

    if type == 2:
        val =test(pesi1,genera_pesi_random())
        if val == 1:
            pesi1=vittoria(pesi1,coeff,risultati)
        elif  val == 2:
            pesi1=sconfitta(pesi1,coeff,2,risultati)
        else:
            pesi1=pareggio(pesi1,coeff,2,risultati)


    if type == 3:
        val =test(pesi1,genera_pesi(0,pesi1))
        if val == 1:
            pesi1=vittoria(pesi1,coeff,risultati)
        elif  val == 2:
            pesi1=sconfitta(pesi1,coeff,3,risultati)
        else:
            pesi1=pareggio(pesi1,coeff,3,risultati)

    if type == 4:
        val =test(pesi1,genera_pesi(1,pesi1))
        if val == 1:
            pesi1=vittoria(pesi1,coeff,risultati)
        elif  val == 2:
            pesi1=sconfitta(pesi1,coeff,4,risultati)
        else:
            pesi1=pareggio(pesi1,coeff,4,risultati)

    if type == 5:
        val =test(pesi1,genera_pesi(2,pesi1))
        if val == 1:
            pesi1=vittoria(pesi1,coeff,risultati)
        elif  val == 2:
            pesi1=sconfitta(pesi1,coeff,5,risultati)
        else:
            pesi1=pareggio(pesi1,coeff,5,risultati)

    if type == 6:
        val =test(pesi1,genera_pesi(3,pesi1))
        if val == 1:
            pesi1=vittoria(pesi1,coeff,risultati)
        elif  val == 2:
            pesi1=pesi1=sconfitta(pesi1,coeff,6,risultati)
        else:
            pesi1=pareggio(pesi1,coeff,6,risultati)
    print(statistica(risultati))
