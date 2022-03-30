import Builders

rosc = Builders.NPC(name="Rosc", entry_ID="rosc", age=2178, job="Dream Weever", group="neutral (formally Chemist)", relationship=7, home_location="South_City")

mushi = Builders.NPC(name="Tanaka Mushimoto", entry_ID="mushi", job="Leader of Yakuza", group="Yakuza", relationship=9, home_location="South_City", congress_member=True)

skeeter = Builders.NPC(name="Skeeter", entry_ID="skeeter", job="Drone Pilot", group="Klinques", relationship=4, home_location="South_City")

met_NPCs ={
  "rosc": rosc,
  "mushi": mushi,
  "skeeter": skeeter
}

