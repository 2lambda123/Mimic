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

# nodes[0] has overall template
# we are assuming that group1 of nodes[0] is the ISS. If so, list1 has all of the crew info
# nodes[1] of list1 is the collction of navboxes
# group1 of nodes[1] has the mission that launched crew
# list1 has the crew members on that mission. crew data appears to be mod 6
# value 5 mod 6 has the crew member name and wiki link. text attribute may or may not be present
# value 3 mod 6 has the flagcode template. unnamed param "1" has the country
# Checks to be done: make sure list1 really is ISS.
#                    May have between one and nine spacecraft.
#                    May have a bunch of crew or even none?
print(wikicode.nodes[0].get("list1").value.nodes[1].get("group1").value.nodes[1].title)
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list1").value.nodes[3].get("1"))
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list1").value.nodes[5].text)
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list1").value.nodes[9].get("1"))
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list1").value.nodes[11].title)
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list1").value.nodes[15].get("1"))
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list1").value.nodes[17].text)

print(wikicode.nodes[0].get("list1").value.nodes[1].get("group2").value.nodes[1].title)
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list2").value.nodes[3].get("1"))
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list2").value.nodes[5].title)
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list2").value.nodes[9].get("1"))
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list2").value.nodes[11].title)
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list2").value.nodes[15].get("1"))
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list2").value.nodes[17].title)
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list2").value.nodes[21].get("1"))
print(wikicode.nodes[0].get("list1").value.nodes[1].get("list2").value.nodes[23].title)

#tokens = [node for node in wikicode.filter()]


#print(tokens[23])

#for token in tokens:
#    print(token)
#    print("::::::::")


