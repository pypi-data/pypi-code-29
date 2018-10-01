from botworks.chat.Response import Response
from botworks.chat.InteractionDefinition import InteractionDefinition, Or

messages = [
    InteractionDefinition(
        trigger_definition=Or("spoiler"),
        mod_exempt=False,
        cooldown_duration_seconds=3600,
        response=Response(
            text=["Rosebud was his sled", "Snape kills Dumbledore",
                  "Bruce Willis was dead the whole time", "Water kills the aliens",
                  "Vader is Luke's father", "Leeloo is the fifth element",
                  "Jack dies", "Mission Possible", "Harry kills Voldemort",
                  "Tyler Durden is not real", "299 Die", "Neo is the one. Also maybe Jesus.",
                  "Orion is the cat, the galaxy is a marble", "Leonard killed his own wife",
                  "http://i.imgur.com/BrV6KJT.jpg", "The village is in a modern nature preserve",
                  "Soylent green is made of people", "Judge Doom framed Roger Rabbit",
                  "Borden had an identical twin disguised as Fallon",
                  "Andy used the poster to hide a hole he was digging",
                  "Elijah caused the train crash to see if superheros were real",
                  "Il Duce is Conner and Murphy's father, Agent Smecker joins their cause",
                  "It was all part of the Rekall package",
                  "Grace and her children are the ghosts", "Leia is Luke's sister",
                  "Sergean Howie was lured to the island as a sacrifice", "Deckard was a replicant... maybe",
                  "Everyone on the island is dead and trapped in some sort of time-travelling purgatory"])
    ),
    InteractionDefinition(
        trigger_definition=Or("night king", "nightking"),
        mod_exempt=False,
        cooldown_duration_seconds=0,
        response=Response(emoji="nightking")
    )
]