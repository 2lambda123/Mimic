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

mission_name = None

# Find all instances of the "flagicon" template
for template in wikicode.filter_templates():
    if template.name.matches("flagicon"):
        print(template.get("1").value)

# Loop over each template in the Wikicode
for template in wikicode.filter_templates():
    # Check if the template is the "People currently in space" template
    if template.name.matches("navbox"):
        # Extract the crew names and Wikipedia links
        for param in template.params:
            if param.name.strip() == "list1":
                crew_list = param.value.strip()
                crew_wikilinks = [str(x.title) for x in mwparserfromhell.parse(crew_list).filter_wikilinks()]
                crew_names = [str(x.title.split('|')[-1]).strip() for x in mwparserfromhell.parse(crew_list).filter_wikilinks()]
                for i in range(len(crew_names)):
                    if 'Soyuz' in crew_names[i] or 'SpaceX' in crew_names[i] or 'Boeing' in crew_names[i] or 'Shenzhou' in crew_names[i]:
                        mission_name = crew_names[i]
                        print(f"Mission name: {mission_name}")
                    else:
                        print(f"Crew member name: {crew_names[i]}")
                    print(f"Wiki link: https://en.wikipedia.org/wiki/{crew_wikilinks[i]}")
                mission_name = None

