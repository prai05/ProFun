import cfg
import socket
import time
import sys
import re
import cfg
import commandParser
# connect

s = socket.socket()
s.connect((cfg._host, cfg._port))
s.send("PASS {}\r\n".format(cfg._pass).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg._nick).encode("utf-8"))
s.send("JOIN {}\r\n".format(cfg._chan).encode("utf-8"))

cmd_list = {}

def cmd_chat(msg, sock=s):
	return sock.send("PRIVMSG {} :{}\r\n".format(cfg._chan, msg).encode('utf-8'))
chat = cmd_chat
def cmd_addban(arg):
	print("add ban", arg[0])
	for word in arg:
		dupe = False
		for b in blacklist:
			if re.match('^' + word + '$', b, flags=re.I+re.U):
				dupe = True
				break
		if not(dupe):
			f = open('blacklist.txt', 'w')
			f.seek(0,2)
			f.write('!b' + word + '\n')
			f.close()
			blacklist.append(word)
			print(word)
			chat("added {} to blacklist".format(word))
		else:
			chat("Duplicate Keyword: {}".format(word))
	return len(arg)
def cmd_remban(arg):
	n = len(blacklist)
	for i in range(0,n):
		for word in arg:
			if re.match("^"+word+"$", blacklist[i], flags=re.U+re.I):
				chat("removed {} from blacklist".format(word))
				blacklist[i] = ""
def cmd_mimic(arg):
	_str = ""
	print("mimic received {} arguments".format(len(arg)))
	for i in arg:
		_str = _str + i + " "
	chat("{} -> {} Kappa".format(user, _str))
def cmd_blacklists(arg):
	_str = "Banned words: ["
	for i in blacklist:
		_str = _str + i + ","
	chat(_str)
def cmd_addcmd(arg):
	dupe = True
	try:
		eval("cmd_"+arg[0])
	except:
		dupe = False
	if not dupe:
		print("addCmd", arg)
		_str = ''
		print(len(arg))
		for i in range(1, len(arg)):
			_str += arg[i] + ' '
		print("add:"+_str)
		cmd_list[arg[0]] = commandParser.parse(_str)
		print(cmd_list[arg[0]])


running = True

assert(cfg._chan == "#rod41732")


f = open("blacklist.txt", "r")
f.seek(0)
blacklist = []
while True:
	line = f.readline()
	if line == '':
		break
	else:
		if re.match('^!b', line) != None:
			word = re.sub('^!b', '', line)
			word = re.sub('\n', '', word) #remove endline
			print("read: banned > " + word)
			blacklist.append(word)
f.close()
chat("Bot Connected")
while running:
	response = s.recv(4096).decode("utf-8")
	temp = response.split("\r\n")
	for line in temp:
		time.sleep(0)
		print(line)
		if "PING :tmi" in line:
			print("PONG!")
			s.send("PONG :tmi.twitch.tv\r\n")
			chat("PONG LUL") # chat
		else:
			msg = re.search('^:+\w+!+\w+@+\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :', line)
			if (msg != None):
				_msg = re.sub('^:+\w+!+\w+@+\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :', "", line)
				user = re.search("\w+", line).group(0)
				print(u'{} > {}'.format(user, _msg))
				success = False
				if re.match("^!exit", _msg, flags=re.U):
					running = False
					success = True
				elif re.match("^!\w+", _msg, flags=re.U+re.I): #maybe a command
					cmd = re.search("\w+", _msg, flags=re.U+re.I).group(0)
					args = re.findall("[^\s]+", re.sub("^!\w+", "", _msg), flags=re.U+re.I)
					success = True
					try:
						eval("cmd_{}(args)".format(cmd))
					except Exception as e:
						print(e)
						success = False
					try:
						commandParser.commandParse(cmd_list[cmd], args)
					except Exception as e:
						print(e)
				if not success:
					_msg = (' ' + _msg + ' ')
					warn = False
					for b in blacklist:
						if re.search(' '+b+' ', _msg, re.I+re.U):
							warn = True
					if warn:
						chat("{} -> blacklisted word [warning]".format(user))

print("exiting")
f = open('blacklist.txt', 'w')
f.seek(0)
for b in blacklist:
	if b:
		f.write('!b' + b + '\n')
f.truncate()
f.close()