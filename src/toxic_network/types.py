from enum import Enum
from typing import List
from pydantic import BaseModel

class ArchetypeType(str, Enum):
    LeftWingMilitant = "Left-wing activist"
    RightWingMilitant = "Right-wing activist"
    Troll = "Troll"
    Moralistic = "Moralistic Conservative"
    Cold = "Cold Skeptic"
    Rebellious = "Rebellious Anti-Establishment"

class CommunicationStyle(BaseModel):
    formality: int
    aggressiveness: int
    sarcasm: int
    irony: int
    polite: int

class SocialStance(BaseModel):
    victimhood: int
    superiority: int
    moralism: int
    conspiracy: int

class Personality(BaseModel):
    archetype: ArchetypeType
    social_stance: SocialStance
    communication_style: CommunicationStyle
    say_nice_things: bool
    use_bad_language: bool
