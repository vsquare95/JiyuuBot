def current(self, lel):
    self.require("format_song_details")
    currentTrack = self.conman.mpc.currentsong()
    if type(currentTrack) == list:
        currentTrack = currentTrack[0]
    tosend = self.run_func("format_song_details", [currentTrack["file"]])
    if thread_types[threading.current_thread().ident] == "HTTP":
        import math
        currentTrack["elapsed"] = math.floor(float(self.conman.mpc.status()["elapsed"]))
        tosend = json.dumps(currentTrack, sort_keys=True, indent=4, separators=(',', ': '))
    self.conman.gen_send(tosend)

self._map("command", "current", current)
self._map("http", "current", current)
self._map("help", "current", ".current - displays current track info")
