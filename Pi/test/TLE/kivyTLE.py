from kivy.app import App
from kivy.clock import Clock
from tle_fetcher import get_tles
import asyncio

class TLEFetcherApp(App):
    global tles
    tles = {
        "ISS": None,
        "TDRS 12": None,
        "TDRS 11": None,
        "TDRS 10": None,
        "TDRS 7": None,
        "TDRS 6": None,
    }

    def build(self):
        # Schedule the get_tles() function to be called every hour
        Clock.schedule_interval(self.fetch_tles, 10)
        Clock.schedule_interval(self.orbitUpdate, 20)
        return

    def fetch_tles(self, dt):
        global tles
        # Call the get_tles() function to fetch the TLEs
        tles = asyncio.run(get_tles())
        # Do something with the tles dictionary
        # For example, print the TLEs for the ISS and TDRS 12 satellites

    def orbitUpdate(self, dt):
        global tles
        if tles["ISS"] is not None:
            print(tles["ISS"])
        else:
            print("None")

if __name__ == "__main__":
    TLEFetcherApp().run()

