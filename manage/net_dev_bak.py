#!/usr/bin/python

# -*- coding: utf-8 -*-

import re
import logging
import paramiko  # 引入ssh模块，该模块需要单独安装。
import time
import threading


class RuiJeiSW:

	def __init__(self, hostname, ip, port, user, password):
		self.hostname = hostname
		self.ip = ip
		self.port = port
		self.user = user
		self.password = password
		self.client = None
		self.sshconnect = None

	def new_sshconnect(self):
		self.client = paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
			self.client.connect(self.ip, self.port, self.user, self.password, timeout=5)
			self.sshconnect = self.client.invoke_shell()
		except Exception as e:
			logger.info("主机%s连接失败，失败原因：%s", self.hostname, e)
			exit()

	def del_sshconnect(self):
		self.client.close()
		logger.info("端口关闭成功")

	def to_enable(self):
		self.sshconnect.send('enable\n')
		time.sleep(1)
		out = self.sshconnect.recv(1024).decode()
		if "Password:" in out:
			self.sshconnect.send('wangluo123\n')
			time.sleep(1)
			out = self.sshconnect.recv(1024).decode()
			if "Password:" in out:
				print("enable 密码错误~！")
			elif "Ruijie#" in out:
				print("enable 密码正确")

	def show_run(self):
		out = self.sshconnect.recv(1024).decode()
		print(out)
		print("11")
		self.sshconnect.send('ls \n')
		time.sleep(1)
		out = self.sshconnect.recv(1024).decode()
		conf = out
		while "Ruijie#" not in out:
			self.sshconnect.send('  ')
			out = self.sshconnect.recv(1024).decode()
			conf = conf + out
		print(conf)

	def show_mac(self):
		self.sshconnect.send('show mac \n')
		time.sleep(1)
		out = self.sshconnect.recv(1024).decode()
		conf = out
		while "Ruijie#" not in out:
			self.sshconnect.send('  ')
			out = self.sshconnect.recv(1024).decode()
			conf = conf + out
		print(conf)

	def show_arp(self):
		self.sshconnect.send('show arp \n')
		time.sleep(1)
		out = self.sshconnect.recv(1024).decode()
		conf = out
		while "Ruijie#" not in out:
			self.sshconnect.send('  ')
			out = self.sshconnect.recv(1024).decode()
			conf = conf + out
		print(conf)


class H3cSW:

	def __init__(self, hostname, ip, port, user, password):
		self.hostname = hostname
		self.ip = ip
		self.port = port
		self.user = user
		self.password = password
		self.client = None
		self.sshconnect = None

	def new_sshconnect(self):
		self.client = paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
			self.client.connect(self.ip, self.port, self.user, self.password, timeout=5)
			self.sshconnect = self.client.invoke_shell()
		except Exception as e:
			logger.info("主机%s连接失败，失败原因：%s", self.hostname, e)
			exit()

	def del_sshconnect(self):
		self.client.close()
		logger.info("端口关闭成功")

	def to_systemview(self):
		self.sshconnect.send('systemview\n')
		time.sleep(1)
		out = self.sshconnect.recv(1024).decode()
		if "Password:" in out:
			self.sshconnect.send('wangluo123\n')
			time.sleep(1)
			out = self.sshconnect.recv(1024).decode()
			if "Password:" in out:
				print("enable 密码错误~！")
			elif "Ruijie#" in out:
				print("enable 密码正确")

	def display_cu(self):
		out = self.sshconnect.recv(1024).decode()
		print(out)
		print("11")
		self.sshconnect.send('display cu \n')
		time.sleep(1)
		out = self.sshconnect.recv(1024).decode()
		conf = out
		while "Ruijie#" not in out:
			self.sshconnect.send('  ')
			out = self.sshconnect.recv(1024).decode()
			conf = conf + out
		print(conf)

	def display_mac(self):
		self.sshconnect.send('display mac \n')
		time.sleep(1)
		out = self.sshconnect.recv(1024).decode()
		conf = out
		while "Ruijie#" not in out:
			self.sshconnect.send('  ')
			out = self.sshconnect.recv(1024).decode()
			conf = conf + out
		print(conf)

	def show_arp(self):
		self.sshconnect.send('display arp \n')
		time.sleep(1)
		out = self.sshconnect.recv(1024).decode()
		conf = out
		while "Ruijie#" not in out:
			self.sshconnect.send('  ')
			out = self.sshconnect.recv(1024).decode()
			conf = conf + out
		print(conf)

	def conf_bak(self):

		self.new_sshconnect()
		out = self.sshconnect.recv(1024).decode()
		self.sshconnect.send('back up \n')
		time.sleep(2)
		out = self.sshconnect.recv(1024).decode()
		reout = re.search("(\[(.*?)\][#|$]+)(?P<num>(.*)+)(\[(.*?)\][#|$]+) ", out, re.S)

		print(reout.group('num'))


		self.del_sshconnect()


# 日志配置
logger = logging.getLogger()
logger.setLevel(logging.INFO)
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] -%(funcName)s- %(levelname)s: %(message)s")
sh.setFormatter(formatter)
logger.addHandler(sh)

hostname = '127.0.0.1'
ip = "172.16.210.166"
port = 22
username = 'root'
password = '1'

lt = H3cSW(hostname, ip, port, username, password)
bakthread = threading.Thread(target=lt.conf_bak)
bakthread.start()

