import requests
import mwparserfromhell

# Define the URL of the template page
template_url = "https://en.wikipedia.org/w/api.php?action=parse&page=Template:People_currently_in_space&prop=wikitext&format=json"

# Make a request to the Wikipedia API to get the wikitext of the template page
response = requests.get(template_url)
data = response.json()

# Parse the wikitext using mwparserfromhell
wikitext = data["parse"]["wikitext"]["*"]
wikicode = mwparserfromhell.parse(wikitext)

iss_group = None

# protecting against bigger number of groups in the future
groups = ["group1", "group2", "group3", "group4", "group5", "group6", "group7", "group8", "group9", "group10",
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

iss_expedition = wikicode.nodes[0].get("group1").value.nodes[4].title

iss_vehicles_lists = []
iss_vehicles = []

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
            iss_vehicles.append(str(wikicode.nodes[0].get("list1").value.nodes[1].get(group).value.nodes[1].title))

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
        for j in range(0, spacecraft_crews[iss_vehicles[i]]*6, 6):
            name_node = wikicode.nodes[0].get("list1").value.nodes[1].get(iss_vehicles_lists[i]).value.nodes[j + 5]
            flag_node = wikicode.nodes[0].get("list1").value.nodes[1].get(iss_vehicles_lists[i]).value.nodes[j + 3]

            spacecraft = iss_vehicles[i]

            # Get the crew member's name and link to their wikipedia page

            try:
                name = name_node.text.strip()
            except:
                name = name_node.title.strip()

            link = str(name_node.title).replace(' ', '_')

            # Get the country of the crew member
            country = flag_node.get("1").value.strip()

            # Get the spacecraft that the crew member arrived on

            # Print the information for the crew member
            print(f"Name: {name}")
            print(f"Link: https://en.wikipedia.org/wiki/{link}")
            print(f"Country: {country}")
            print(f"Spacecraft: {spacecraft}")
            print()
else:
    print("Could not find the International Space Station crew members.")
