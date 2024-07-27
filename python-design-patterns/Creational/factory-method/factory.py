from abc import ABC, abstractmethod
# Step 1: Defining the product
class Localizer(ABC):
    """Abstract method: Represents translations for specific languages."""
    @abstractmethod
    def localize(self, msg):
        """Translate the given message"""
        pass

#Step 2: Defining concrete product
class FrenchLocalizer(Localizer):
    """Concrete Product: Represents translations for French."""
    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }
    def localize(self, msg):
        """Translate the messgae to french"""    
        return self.translations.get(msg, msg)

class SpanishLocalizer(Localizer):
    """Concrete Product: Represents translations for Spanish."""
    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }  
    # Localizer for creating 
    def localize(self, msg):
        """Translates the message to Spanish"""
        return self.translations.get(msg, msg)

class EnglishLocalizer(Localizer):
    """Concrete Product: Represents translations for English."""
    def localize(self, msg):
        """Translates the message to English"""
        return msg 

# Step 3: Defining the creator
# class LocalizerFactory(language= "English"):
#     """Abstract Creator: Defines the Factory method to create localizers."""
#     @abstractmethod
#     def create_localizers(self):
#         """Factory method: Create a localizer instance"""
#         pass

# Step 3 and 4: Creating factory method
def create_localizer(language="English"):
    """
    Faction to create a localizer for a specified language
    Args:
       language (str): Language for which localizer needs to be created
    Returns:
       Localizer: A localizer instance for the specified language    
    """
    localizers ={
        "English": "EnglishLocalizer",
        "Spanish": "SpanishLocalizer",
        "French": "FrenchLocalizer",
    }
    return localizers[language]()
   
# Constructor using the factory method
if __name__ == "__main__":
    f = create_localizer("French")
    s = create_localizer("Spanish")
    e = create_localizer("English")
    message = ["car", "bike", "cycle"]
    for msg in message:
        # Print the translated message
        print(f.localize(msg))
        print(s.localize(msg))
        print(e.localize(msg))


"""

Volunteered to mentor university students, and initiated a hackathon.
Technical personal projects and initiatve to speak in events sharing 
current knowledge.

(Shared current product to other departments to collborate)
"""