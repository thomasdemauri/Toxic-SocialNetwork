from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import random

from toxic_network.types import ArchetypeType, CommunicationStyle, Personality, SocialStance


class BuildPersonality(BaseTool):
    name: str = "BuildPersonality"
    description: str = (
        "Build user's personality"
    )

    def _run(self, argument: str) -> Personality:
        archetype = random.choice(list(ArchetypeType)).value
        
        victimhood = random.randint(0, 5)
        superiority = random.randint(0, 5)
        moralism = random.randint(0, 5)
        conspiracy = random.randint(0, 5)

        social_stance = SocialStance(
            victimhood=victimhood,
            superiority=superiority,
            moralism=moralism,
            conspiracy=conspiracy
        )

        formality = random.randint(0, 5)
        agressiveness = random.randint(0, 5)
        sarcasm = random.randint(0, 5)
        irony = random.randint(0, 5)
        polite = random.randint(0, 5)

        communication_style = CommunicationStyle(
            formality=formality,
            aggressiveness=agressiveness,
            sarcasm=sarcasm,
            irony=irony,
            polite=polite
        )

        say_nice_things = random.choice([True, False])
        use_bad_language = random.choice([True, False])

        personality = personality = Personality(
            archetype=archetype,
            social_stance=social_stance,
            communication_style=communication_style,
            say_nice_things=say_nice_things,
            use_bad_language=use_bad_language
        )

        return personality
