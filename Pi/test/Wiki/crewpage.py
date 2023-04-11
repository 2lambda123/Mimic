import mwparserfromhell
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty
from kivy.lang import Builder


class CrewMember(BoxLayout):
    name = StringProperty('')
    country = StringProperty('')
    title = StringProperty('')
    pic = StringProperty('')
    days_in_space = StringProperty('')
    mission = StringProperty('')
    craft = StringProperty('')
    wikilink = StringProperty('')


class CrewList(BoxLayout):
    members = ListProperty([])
    title = StringProperty('Current ISS Crew')

    def __init__(self, **kwargs):
        super(CrewList, self).__init__(**kwargs)
        self.get_crew_data()

    def get_crew_data(self):
        url = "https://en.wikipedia.org/w/api.php?action=parse&page=Template:People_currently_in_space&prop=wikitext&format=json"

        def on_success(req, data):

            # Parse the wikitext using mwparserfromhell
            wikicode = mwparserfromhell.parse(data["parse"]["wikitext"]["*"])

            iss_expedition = wikicode.nodes[0].get("group1").value.nodes[4].title
            self.title = str(iss_expedition) + " - Current ISS Crew"

            iss_vehicles_lists = []
            iss_vehicles = []
            iss_group = None

            # Protecting against bigger number of groups in the future
            groups = ["group1", "group2", "group3", "group4", "group5", "group6", "group7", "group8", "group9",
                      "group10",
                      "group11"]

            # Find the group that contains the ISS crew members
            for group in groups:
                try:
                    wikicode.nodes[0].get(group).value
                except:
                    pass
                else:
                    if "International Space Station" in wikicode.nodes[0].get(group).value:
                        iss_group = group

            if iss_group:
                # Get the list of crew members
                crew_list = None
                for i, group in enumerate(groups):
                    try:
                        wikicode.nodes[0].get("list1").value.nodes[1].get(group)
                    except:
                        pass
                    else:
                        iss_vehicles_lists.append("list" + str(i + 1))
                        iss_vehicles.append(
                            str(wikicode.nodes[0].get("list1").value.nodes[1].get(group).value.nodes[1].title))

                spacecraft_crews = {}

                # Get crew per vehicle
                for i, lists in enumerate(iss_vehicles_lists):
                    count = 0
                    for j in range(0, 7 * 6, 6):
                        try:
                            wikicode.nodes[0].get("list1").value.nodes[1].get(lists).value.nodes[j + 5]
                        except:
                            pass
                        else:
                            count += 1
                    spacecraft_crews.update({str(iss_vehicles[i]): count})

                # Get information for each crew member
                for i in range(0, len(iss_vehicles_lists)):
                    for j in range(0, spacecraft_crews[iss_vehicles[i]] * 6, 6):
                        name_node = \
                            wikicode.nodes[0].get("list1").value.nodes[1].get(iss_vehicles_lists[i]).value.nodes[j + 5]
                        flag_node = \
                            wikicode.nodes[0].get("list1").value.nodes[1].get(iss_vehicles_lists[i]).value.nodes[j + 3]

                        # Get the spacecraft that the crew member arrived on
                        spacecraft = iss_vehicles[i]

                        # Get the crew member's name and link to their wikipedia page
                        try:
                            name = name_node.text.strip()
                        except:
                            name = name_node.title.strip()

                        link = str(name_node.title).replace(' ', '_')

                        # Get the country of the crew member
                        country = flag_node.get("1").value.strip()

                        crew_member = CrewMember(
                            name=name,
                            title='Flight Engineer',
                            country=country,
                            days_in_space='103',
                            mission=spacecraft,
                            wikilink = link
                        )

                        print(crew_member.name)
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

        # Make a request to the Wikipedia API to get the wikitext of the template page
        req = UrlRequest(url, on_success, on_redirect, on_failure, on_error, timeout=1)


class ISSApp(App):
    def build(self):
        # Builder.load_file('iss.kv')
        return CrewList()


if __name__ == '__main__':
    ISSApp().run()

