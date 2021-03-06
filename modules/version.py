def version(self, command):
    import datetime
    import time
    import math
    gitlogf = open(os.getcwd() + os.sep + ".git/logs/refs/remotes/origin/master", "r")
    gitlog = gitlogf.read()
    gitlogf.close()
    gitlog = gitlog.split("\n")[-2].split(" ")
    commit = gitlog[1]
    timeg = int(gitlog[4])
    if thread_types[threading.current_thread().ident] == "HTTP":
        import calendar
        values = {"commithash": commit, "lastpull": calendar.timegm(time.gmtime(timeg))}
        self.conman.gen_send(json.dumps(values, sort_keys=True, indent=4, separators=(',', ': ')))
    else:
        vers = "http://github.com/JiyuuProject/JiyuuBot - Commit hash: %s - Last pull: %s (%s ago)" % (commit, time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime(timeg)), datetime.timedelta(seconds=math.floor(time.time()-timeg)))
        self.conman.gen_send(vers)

self._map("command", "version", version)
self._map("http", "version", version)
self._map("help", "version", ".version - Prints commit hash and last git pull")
