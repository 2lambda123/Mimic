from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty
from kivy.lang import Builder


class CrewMember(BoxLayout):
    def __init__(self, **kwargs):
        print("CrewMember init")
        super(CrewMember, self).__init__(**kwargs)

    name = StringProperty('')
    country = StringProperty('')
    title = StringProperty('')
    #pic = StringProperty('')
    days_in_space = StringProperty('')
    mission = StringProperty('')
    craft = StringProperty('')


class CrewList(BoxLayout):
    members = ListProperty([])
    #title = StringProperty('Current ISS Crew')

    def __init__(self, **kwargs):
        super(CrewList, self).__init__(**kwargs)
        self.get_crew_data()

    def get_crew_data(self):
        url = 'http://api.open-notify.org/astros.json'

        def on_success(req, data):
            num_peeps = int(data['number'])

            for num in range(num_peeps):
                if str(data['people'][num]['craft']) == "ISS":
                    crew_member = CrewMember(
                        name=data['people'][num]['name'],
                        craft=data['people'][num]['craft'],
                        title='Engineer',
                        country='Murica',
                        days_in_space='103',
                        mission='SpaceX-3'
                    )
                    #print(crew_member.name)
                    self.members.append(crew_member)

                    # Add the crew member to the widget
                    self.ids.crew_members.add_widget(crew_member)

        def on_redirect(req, result):
            print("Warning - checkCrew JSON failure (url redirect)")
            print(result)

        def on_failure(req, result):
            print("Warning - checkCrew JSON failure (url failure)")
            print(result)

        def on_error(req, result):
            print("Warning - checkCrew JSON failure (url error)")
            print(result)

        req = UrlRequest(url, on_success, on_redirect, on_failure, on_error, timeout=1)


class ISSApp(App):
    def build(self):
        #Builder.load_file('iss.kv')
        return CrewList()


if __name__ == '__main__':
    ISSApp().run()

