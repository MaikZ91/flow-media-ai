/* Rezeptdaten. Quellen: IBA-Rezepte (Daten via github.com/rasmusab/iba-cocktails, CC BY 4.0), Fotos Wikimedia Commons (Lizenzen je Bild). */
window.KATEGORIEN = [
 {
  "id": "klassiker",
  "name": "Klassiker",
  "text": "Zeitlose Drinks, die jede Bar beherrscht."
 },
 {
  "id": "modern",
  "name": "Modern",
  "text": "Neue Klassiker der letzten Jahrzehnte."
 },
 {
  "id": "exotisch",
  "name": "Exotisch & Tiki",
  "text": "Rum, Früchte und Urlaubsgefühl."
 },
 {
  "id": "longdrink",
  "name": "Highballs & Longdrinks",
  "text": "Lang, kühl und unkompliziert."
 },
 {
  "id": "alkoholfrei",
  "name": "Alkoholfrei",
  "text": "Voller Geschmack, ganz ohne Alkohol."
 }
];
window.REZEPTE = [
 {
  "id": "old-fashioned",
  "name": "Old Fashioned",
  "kategorie": "klassiker",
  "glas": "Tumbler (Rocks)",
  "technik": "Bauen",
  "staerke": 4,
  "zeit": 3,
  "geschmack": [
   "herb",
   "würzig"
  ],
  "beschreibung": "Der Urahn aller Cocktails: Whiskey, Zucker und Bitters. Ruhig, kräftig, zeitlos.",
  "garnitur": "Orangenzeste",
  "zutaten": [
   {
    "m": 45,
    "e": "ml",
    "n": "Bourbon oder Rye Whiskey",
    "v": 40
   },
   {
    "m": 1,
    "e": "Stk",
    "n": "Zuckerwürfel",
    "v": 0,
    "ml": 0
   },
   {
    "m": 3,
    "e": "Dash",
    "n": "Angostura Bitters",
    "v": 44.7,
    "ml": 0.6
   },
   {
    "m": 2,
    "e": "Dash",
    "n": "Wasser",
    "v": 0,
    "ml": 0.6
   }
  ],
  "schritte": [
   {
    "t": "Zuckerwürfel ins Glas geben und mit Bitters tränken.",
    "z": [
     1,
     2
    ]
   },
   {
    "t": "Wasser dazugeben und den Zucker zerdrücken, bis er sich löst.",
    "z": [
     3
    ]
   },
   {
    "t": "Glas mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Whiskey eingießen.",
    "z": [
     0
    ]
   },
   {
    "t": "Sanft rühren, bis das Glas außen beschlägt.",
    "z": []
   },
   {
    "t": "Orangenzeste über dem Drink ausdrücken und hineingeben.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/old-fashioned.jpg",
  "credit": {
   "datei": "Whiskey Old Fashioned1.jpg",
   "autor": "Erich Wagner (www.eventografie.de)",
   "lizenz": "CC BY-SA 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Whiskey_Old_Fashioned1.jpg"
  },
  "profil": {
   "suess": 1,
   "bitter": 1,
   "herb": 3,
   "wuerzig": 2
  },
  "basis": [
   "whiskey"
  ],
  "stil": [
   "klassiker"
  ]
 },
 {
  "id": "negroni",
  "name": "Negroni",
  "kategorie": "klassiker",
  "glas": "Tumbler (Rocks)",
  "technik": "Bauen",
  "staerke": 4,
  "zeit": 2,
  "geschmack": [
   "bitter",
   "herb"
  ],
  "beschreibung": "Drei gleiche Teile, ein Weltklassiker aus Florenz. Bitter, süß, tief rot.",
  "garnitur": "Orangenscheibe",
  "zutaten": [
   {
    "m": 30,
    "e": "ml",
    "n": "Gin",
    "v": 40
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Campari",
    "v": 25
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Roter Wermut",
    "v": 15
   }
  ],
  "schritte": [
   {
    "t": "Tumbler mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Gin, Campari und Wermut direkt ins Glas gießen.",
    "z": [
     0,
     1,
     2
    ]
   },
   {
    "t": "Sanft umrühren.",
    "z": []
   },
   {
    "t": "Mit einer Orangenscheibe garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/negroni.jpg",
  "credit": {
   "datei": "Negroni (cocktail).png",
   "autor": "Matthias Friedlein (www.augustine-bar.de)",
   "lizenz": "CC BY-SA 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Negroni_(cocktail).png"
  },
  "profil": {
   "suess": 1,
   "bitter": 3,
   "herb": 2,
   "wuerzig": 1
  },
  "basis": [
   "gin",
   "bitter",
   "wermut"
  ],
  "stil": [
   "klassiker"
  ]
 },
 {
  "id": "dry-martini",
  "name": "Dry Martini",
  "kategorie": "klassiker",
  "glas": "Martiniglas",
  "technik": "Rühren",
  "staerke": 5,
  "zeit": 3,
  "geschmack": [
   "herb",
   "trocken"
  ],
  "beschreibung": "Klar, kalt und kompromisslos: Gin und ein Hauch trockener Wermut.",
  "garnitur": "Zitronenzeste oder Olive",
  "zutaten": [
   {
    "m": 60,
    "e": "ml",
    "n": "Gin",
    "v": 40
   },
   {
    "m": 10,
    "e": "ml",
    "n": "Trockener Wermut",
    "v": 18
   }
  ],
  "schritte": [
   {
    "t": "Martiniglas mit Eis vorkühlen.",
    "z": []
   },
   {
    "t": "Rührglas mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Gin und Wermut hinzugeben.",
    "z": [
     0,
     1
    ]
   },
   {
    "t": "Etwa 30 Sekunden gut kalt rühren.",
    "z": []
   },
   {
    "t": "Eis aus dem Martiniglas entfernen und den Drink hineinseihen.",
    "z": []
   },
   {
    "t": "Mit Zitronenzeste oder Olive garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/dry-martini.jpg",
  "credit": {
   "datei": "Dry martini.jpg",
   "autor": "Arnaud 25",
   "lizenz": "CC BY-SA 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Dry_martini.jpg"
  },
  "profil": {
   "herb": 3,
   "wuerzig": 1
  },
  "basis": [
   "gin"
  ],
  "stil": [
   "klassiker"
  ]
 },
 {
  "id": "daiquiri",
  "name": "Daiquiri",
  "kategorie": "klassiker",
  "glas": "Cocktailschale",
  "technik": "Shaken",
  "staerke": 3,
  "zeit": 3,
  "geschmack": [
   "sauer",
   "frisch"
  ],
  "beschreibung": "Rum, Limette, Zucker: drei Zutaten, die perfekt balanciert alles sagen.",
  "garnitur": "Limettenscheibe (optional)",
  "zutaten": [
   {
    "m": 60,
    "e": "ml",
    "n": "Weißer Rum",
    "v": 40
   },
   {
    "m": 20,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   },
   {
    "m": 2,
    "e": "BL",
    "n": "Feinzucker",
    "v": 0,
    "ml": 4
   }
  ],
  "schritte": [
   {
    "t": "Cocktailschale kühlen.",
    "z": []
   },
   {
    "t": "Alle Zutaten in den Shaker geben und kurz rühren, bis sich der Zucker löst.",
    "z": [
     0,
     1,
     2
    ]
   },
   {
    "t": "Mit Eis füllen und kräftig shaken.",
    "z": []
   },
   {
    "t": "In die gekühlte Schale abseihen.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/daiquiri.jpg",
  "credit": {
   "datei": "Classic Daiquiri in Cocktail Glass.jpg",
   "autor": "Will Shenton",
   "lizenz": "CC BY-SA 3.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Classic_Daiquiri_in_Cocktail_Glass.jpg"
  },
  "profil": {
   "sauer": 3,
   "suess": 1,
   "fruchtig": 1
  },
  "basis": [
   "rum"
  ],
  "stil": [
   "klassiker"
  ]
 },
 {
  "id": "whiskey-sour",
  "name": "Whiskey Sour",
  "kategorie": "klassiker",
  "glas": "Cocktailschale oder Tumbler",
  "technik": "Shaken",
  "staerke": 3,
  "zeit": 4,
  "geschmack": [
   "sauer",
   "cremig"
  ],
  "beschreibung": "Bourbon trifft Zitrone, mit Eiweiß wird er samtig und bekommt eine feine Schaumkrone.",
  "garnitur": "Orangenscheibe und Cocktailkirsche",
  "zutaten": [
   {
    "m": 45,
    "e": "ml",
    "n": "Bourbon",
    "v": 40
   },
   {
    "m": 25,
    "e": "ml",
    "n": "Frischer Zitronensaft",
    "v": 0
   },
   {
    "m": 20,
    "e": "ml",
    "n": "Zuckersirup",
    "v": 0
   },
   {
    "m": 20,
    "e": "ml",
    "n": "Eiweiß (optional)",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Bourbon, Zitronensaft, Zuckersirup und Eiweiß in den Shaker geben.",
    "z": [
     0,
     1,
     2,
     3
    ]
   },
   {
    "t": "Zuerst ohne Eis kräftig shaken (Dry Shake), damit der Schaum entsteht.",
    "z": []
   },
   {
    "t": "Eis hinzufügen und nochmals shaken.",
    "z": []
   },
   {
    "t": "In die Schale abseihen, auf Eis in einen Tumbler.",
    "z": []
   },
   {
    "t": "Mit Orangenscheibe und Kirsche garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/whiskey-sour.jpg",
  "credit": {
   "datei": "Whiskey Sour Served Up.jpg",
   "autor": "Will Shenton",
   "lizenz": "CC BY-SA 3.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Whiskey_Sour_Served_Up.jpg"
  },
  "profil": {
   "sauer": 2,
   "suess": 2,
   "cremig": 1
  },
  "basis": [
   "whiskey"
  ],
  "stil": [
   "klassiker"
  ]
 },
 {
  "id": "margarita",
  "name": "Margarita",
  "kategorie": "klassiker",
  "glas": "Margaritaglas",
  "technik": "Shaken",
  "staerke": 4,
  "zeit": 4,
  "geschmack": [
   "sauer",
   "frisch",
   "salzig"
  ],
  "beschreibung": "Tequila, Orangenlikör und Limette mit Salzrand: der Partyklassiker aus Mexiko.",
  "garnitur": "Salzrand, Limettenspalte",
  "zutaten": [
   {
    "m": 50,
    "e": "ml",
    "n": "Tequila (100 % Agave)",
    "v": 40
   },
   {
    "m": 20,
    "e": "ml",
    "n": "Triple Sec",
    "v": 30
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Glasrand mit Limette befeuchten und in Salz drehen (optional).",
    "z": []
   },
   {
    "t": "Alle Zutaten in den Shaker geben.",
    "z": [
     0,
     1,
     2
    ]
   },
   {
    "t": "Mit Eis füllen und kräftig shaken.",
    "z": []
   },
   {
    "t": "In das gekühlte Glas abseihen.",
    "z": []
   },
   {
    "t": "Mit Limettenspalte garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/margarita.jpg",
  "credit": {
   "datei": "MargaritaReal.jpg",
   "autor": "Akke Monasso",
   "lizenz": "CC BY-SA 3.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:MargaritaReal.jpg"
  },
  "profil": {
   "sauer": 3,
   "salzig": 2,
   "suess": 1,
   "fruchtig": 1
  },
  "basis": [
   "tequila",
   "likoer"
  ],
  "stil": [
   "klassiker",
   "exotisch"
  ]
 },
 {
  "id": "cosmopolitan",
  "name": "Cosmopolitan",
  "kategorie": "klassiker",
  "glas": "Martiniglas",
  "technik": "Shaken",
  "staerke": 4,
  "zeit": 3,
  "geschmack": [
   "fruchtig",
   "sauer"
  ],
  "beschreibung": "Pink, elegant und frisch, der Stadtcocktail der Neunziger.",
  "garnitur": "Limettenzeste",
  "zutaten": [
   {
    "m": 40,
    "e": "ml",
    "n": "Zitronenwodka",
    "v": 40
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Cointreau",
    "v": 40
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Cranberrysaft",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Martiniglas kühlen.",
    "z": []
   },
   {
    "t": "Alle Zutaten in den Shaker geben.",
    "z": [
     0,
     1,
     2,
     3
    ]
   },
   {
    "t": "Mit Eis füllen und gut shaken.",
    "z": []
   },
   {
    "t": "In das Glas abseihen.",
    "z": []
   },
   {
    "t": "Mit Limettenzeste garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/cosmopolitan.jpg",
  "credit": {
   "datei": "Cosmopolitan - CrystalMixer.jpg",
   "autor": "CrystalMixer - CrystalMixer.com",
   "lizenz": "CC BY 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Cosmopolitan_-_CrystalMixer.jpg"
  },
  "profil": {
   "fruchtig": 2,
   "sauer": 2,
   "suess": 1
  },
  "basis": [
   "wodka",
   "likoer"
  ],
  "stil": [
   "klassiker"
  ]
 },
 {
  "id": "espresso-martini",
  "name": "Espresso Martini",
  "kategorie": "modern",
  "glas": "Martiniglas",
  "technik": "Shaken",
  "staerke": 3,
  "zeit": 4,
  "geschmack": [
   "kaffee",
   "süß"
  ],
  "beschreibung": "Wach und dunkel: Wodka, Kaffeelikör und ein frischer Espresso mit cremiger Krone.",
  "garnitur": "3 Kaffeebohnen",
  "zutaten": [
   {
    "m": 50,
    "e": "ml",
    "n": "Wodka",
    "v": 40
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Kahlúa",
    "v": 20
   },
   {
    "m": 10,
    "e": "ml",
    "n": "Zuckersirup",
    "v": 0
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Frischer Espresso",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Espresso zubereiten und kurz abkühlen lassen.",
    "z": [
     3
    ]
   },
   {
    "t": "Wodka, Kahlúa, Sirup und Espresso in den Shaker geben.",
    "z": [
     0,
     1,
     2,
     3
    ]
   },
   {
    "t": "Mit viel Eis sehr kräftig shaken, das gibt die Crema.",
    "z": []
   },
   {
    "t": "In das gekühlte Martiniglas abseihen.",
    "z": []
   },
   {
    "t": "Mit drei Kaffeebohnen garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/espresso-martini.jpg",
  "credit": {
   "datei": "Espresso martini - November 2024 - Sarah Stierch.jpg",
   "autor": "Missvain",
   "lizenz": "CC0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Espresso_martini_-_November_2024_-_Sarah_Stierch.jpg"
  },
  "profil": {
   "kaffee": 3,
   "suess": 2,
   "cremig": 1
  },
  "basis": [
   "wodka",
   "likoer"
  ],
  "stil": [
   "modern"
  ]
 },
 {
  "id": "penicillin",
  "name": "Penicillin",
  "kategorie": "modern",
  "glas": "Tumbler (Rocks)",
  "technik": "Shaken",
  "staerke": 4,
  "zeit": 5,
  "geschmack": [
   "rauchig",
   "würzig"
  ],
  "beschreibung": "Moderner Klassiker von Sam Ross: Ingwer, Honig, Zitrone und eine Rauchnote vom Islay-Whisky.",
  "garnitur": "Kandierter Ingwer",
  "zutaten": [
   {
    "m": 60,
    "e": "ml",
    "n": "Blended Scotch",
    "v": 40
   },
   {
    "m": 7.5,
    "e": "ml",
    "n": "Islay Single Malt (z. B. Lagavulin 16)",
    "v": 43
   },
   {
    "m": 22.5,
    "e": "ml",
    "n": "Frischer Zitronensaft",
    "v": 0
   },
   {
    "m": 22.5,
    "e": "ml",
    "n": "Honigsirup",
    "v": 0
   },
   {
    "m": 3,
    "e": "Scheiben",
    "n": "Frischer Ingwer",
    "v": 0,
    "ml": 0
   }
  ],
  "schritte": [
   {
    "t": "Ingwerscheiben im Shaker zerdrücken.",
    "z": [
     4
    ]
   },
   {
    "t": "Scotch, Zitronensaft und Honigsirup dazugeben, den Islay-Whisky noch nicht.",
    "z": [
     0,
     2,
     3
    ]
   },
   {
    "t": "Mit Eis füllen und shaken.",
    "z": []
   },
   {
    "t": "Doppelt abseihen in einen Tumbler mit frischem Eis.",
    "z": []
   },
   {
    "t": "Den rauchigen Islay-Whisky obenauf schwimmen lassen.",
    "z": [
     1
    ]
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/penicillin.jpg",
  "credit": {
   "datei": "Penicillin Cocktail.png",
   "autor": "Matthias Friedlein (www.augustine-bar.de)",
   "lizenz": "CC BY-SA 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Penicillin_Cocktail.png"
  },
  "profil": {
   "wuerzig": 3,
   "rauchig": 3,
   "sauer": 1,
   "suess": 1
  },
  "basis": [
   "whiskey"
  ],
  "stil": [
   "modern"
  ]
 },
 {
  "id": "paper-plane",
  "name": "Paper Plane",
  "kategorie": "modern",
  "glas": "Cocktailschale",
  "technik": "Shaken",
  "staerke": 3,
  "zeit": 3,
  "geschmack": [
   "bitter",
   "sauer",
   "herb"
  ],
  "beschreibung": "Vier gleiche Teile, ausgewogen bitter, zitronig und leicht kräuterig. Ein moderner Klassiker.",
  "garnitur": "Keine",
  "zutaten": [
   {
    "m": 30,
    "e": "ml",
    "n": "Bourbon",
    "v": 40
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Amaro Nonino",
    "v": 35
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Aperol",
    "v": 11
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Frischer Zitronensaft",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Alle Zutaten in den Shaker geben.",
    "z": [
     0,
     1,
     2,
     3
    ]
   },
   {
    "t": "Mit Eis füllen und kräftig shaken.",
    "z": []
   },
   {
    "t": "In eine gekühlte Schale abseihen.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/paper-plane.jpg",
  "credit": {
   "datei": "Taub Family Outpost - June 11 2021 - Sarah Stierch 02.jpg",
   "autor": "Missvain",
   "lizenz": "CC BY 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Taub_Family_Outpost_-_June_11_2021_-_Sarah_Stierch_02.jpg"
  },
  "profil": {
   "bitter": 2,
   "sauer": 2,
   "suess": 1,
   "wuerzig": 1
  },
  "basis": [
   "bitter",
   "whiskey"
  ],
  "stil": [
   "modern"
  ]
 },
 {
  "id": "bramble",
  "name": "Bramble",
  "kategorie": "modern",
  "glas": "Tumbler (Rocks)",
  "technik": "Shaken",
  "staerke": 3,
  "zeit": 4,
  "geschmack": [
   "fruchtig",
   "sauer"
  ],
  "beschreibung": "Brombeere auf Crushed Ice, ein britischer Moderne-Klassiker von Dick Bradsell.",
  "garnitur": "Brombeeren und Zitronenscheibe",
  "zutaten": [
   {
    "m": 50,
    "e": "ml",
    "n": "Gin",
    "v": 40
   },
   {
    "m": 25,
    "e": "ml",
    "n": "Frischer Zitronensaft",
    "v": 0
   },
   {
    "m": 12.5,
    "e": "ml",
    "n": "Zuckersirup",
    "v": 0
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Crème de Mûre (Brombeerlikör)",
    "v": 16
   }
  ],
  "schritte": [
   {
    "t": "Tumbler mit Crushed Ice füllen.",
    "z": []
   },
   {
    "t": "Gin, Zitronensaft und Zuckersirup in den Shaker geben.",
    "z": [
     0,
     1,
     2
    ]
   },
   {
    "t": "Mit Eis füllen und shaken.",
    "z": []
   },
   {
    "t": "Über das Crushed Ice abseihen.",
    "z": []
   },
   {
    "t": "Brombeerlikör in kreisender Bewegung darübergießen.",
    "z": [
     3
    ]
   },
   {
    "t": "Mit Brombeeren und Zitrone garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/bramble.jpg",
  "credit": {
   "datei": "Bramble Cocktail2.jpg",
   "autor": "Erich Wagner (www.eventografie.de)",
   "lizenz": "CC BY-SA 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Bramble_Cocktail2.jpg"
  },
  "profil": {
   "fruchtig": 2,
   "sauer": 2,
   "suess": 1
  },
  "basis": [
   "gin"
  ],
  "stil": [
   "modern"
  ]
 },
 {
  "id": "pina-colada",
  "name": "Piña Colada",
  "kategorie": "exotisch",
  "glas": "Großes Glas",
  "technik": "Mixen",
  "staerke": 2,
  "zeit": 4,
  "geschmack": [
   "cremig",
   "fruchtig",
   "süß"
  ],
  "beschreibung": "Kokos, Ananas und Rum: der Urlaubsklassiker aus Puerto Rico, eiskalt und cremig.",
  "garnitur": "Ananasscheibe und Cocktailkirsche",
  "zutaten": [
   {
    "m": 50,
    "e": "ml",
    "n": "Weißer Rum",
    "v": 40
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Kokoscreme",
    "v": 0
   },
   {
    "m": 50,
    "e": "ml",
    "n": "Frischer Ananassaft",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Alle Zutaten mit einer Tasse Crushed Ice in den Mixer geben.",
    "z": [
     0,
     1,
     2
    ]
   },
   {
    "t": "Cremig mixen, bis keine Eisstücke mehr da sind.",
    "z": []
   },
   {
    "t": "In ein großes Glas gießen.",
    "z": []
   },
   {
    "t": "Mit Ananas und Kirsche garnieren, Strohhalme dazu.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/pina-colada.jpg",
  "credit": {
   "datei": "Pina Colada (Cocktail).jpg",
   "autor": "Martin Asche",
   "lizenz": "CC BY-SA 3.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Pina_Colada_(Cocktail).jpg"
  },
  "profil": {
   "suess": 3,
   "cremig": 3,
   "fruchtig": 3
  },
  "basis": [
   "rum"
  ],
  "stil": [
   "exotisch"
  ]
 },
 {
  "id": "mai-tai",
  "name": "Mai Tai",
  "kategorie": "exotisch",
  "glas": "Tumbler (Rocks)",
  "technik": "Shaken",
  "staerke": 4,
  "zeit": 4,
  "geschmack": [
   "fruchtig",
   "nussig",
   "sauer"
  ],
  "beschreibung": "Tiki-Legende von Trader Vic: Rum, Limette und Mandelsirup. Vielschichtig und frisch.",
  "garnitur": "Minze und Limettenhälfte",
  "zutaten": [
   {
    "m": 30,
    "e": "ml",
    "n": "Jamaika-Rum (amber)",
    "v": 40
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Rhum Martinique",
    "v": 40
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Orangenlikör (Curaçao)",
    "v": 30
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Orgeat (Mandelsirup)",
    "v": 0
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   },
   {
    "m": 7.5,
    "e": "ml",
    "n": "Zuckersirup",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Alle Zutaten in den Shaker geben.",
    "z": [
     0,
     1,
     2,
     3,
     4,
     5
    ]
   },
   {
    "t": "Mit Eis füllen und shaken.",
    "z": []
   },
   {
    "t": "In einen Tumbler mit Crushed Ice gießen.",
    "z": []
   },
   {
    "t": "Mit Minzzweig und Limette garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/mai-tai.jpg",
  "credit": {
   "datei": "Mai Tai 4.JPG",
   "autor": "Achim Schleuning (E-Mail: comander02_de@yahoo.de)",
   "lizenz": "CC BY-SA 3.0 de",
   "quelle": "https://commons.wikimedia.org/wiki/File:Mai_Tai_4.JPG"
  },
  "profil": {
   "fruchtig": 2,
   "sauer": 2,
   "suess": 2,
   "wuerzig": 1
  },
  "basis": [
   "rum",
   "likoer"
  ],
  "stil": [
   "exotisch"
  ]
 },
 {
  "id": "zombie",
  "name": "Zombie",
  "kategorie": "exotisch",
  "glas": "Hohes Glas (Tumbler)",
  "technik": "Mixen",
  "staerke": 5,
  "zeit": 6,
  "geschmack": [
   "fruchtig",
   "würzig",
   "stark"
  ],
  "beschreibung": "Der berüchtigte Tiki-Klassiker von Don the Beachcomber: drei Rums, Zitrus, Gewürze. Vorsicht, stark.",
  "garnitur": "Minze, Ananasstück",
  "zutaten": [
   {
    "m": 45,
    "e": "ml",
    "n": "Dunkler Jamaika-Rum",
    "v": 43
   },
   {
    "m": 45,
    "e": "ml",
    "n": "Goldener Rum",
    "v": 40
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Demerara-Rum",
    "v": 43
   },
   {
    "m": 20,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Falernum",
    "v": 11
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Donn's Mix (2 Teile Grapefruit, 1 Teil Zimtsirup)",
    "v": 0
   },
   {
    "m": 1,
    "e": "TL",
    "n": "Grenadine",
    "v": 0,
    "ml": 5
   },
   {
    "m": 1,
    "e": "Dash",
    "n": "Angostura Bitters",
    "v": 44.7,
    "ml": 0.6
   },
   {
    "m": 6,
    "e": "Tropfen",
    "n": "Pernod",
    "v": 40,
    "ml": 0.05
   }
  ],
  "schritte": [
   {
    "t": "Alle Zutaten mit 170 g Crushed Ice in den Mixer geben.",
    "z": [
     0,
     1,
     2,
     3,
     4,
     5,
     6,
     7,
     8
    ]
   },
   {
    "t": "Nur wenige Sekunden kurz mixen.",
    "z": []
   },
   {
    "t": "In ein hohes Glas gießen.",
    "z": []
   },
   {
    "t": "Mit Minze und Ananas garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/zombie.jpg",
  "credit": {
   "datei": "Zombie Cocktail.jpg",
   "autor": "Matthias Friedlein (www.augustine-bar.de)",
   "lizenz": "CC BY-SA 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Zombie_Cocktail.jpg"
  },
  "profil": {
   "fruchtig": 2,
   "sauer": 1,
   "wuerzig": 3,
   "suess": 1
  },
  "basis": [
   "rum"
  ],
  "stil": [
   "exotisch"
  ]
 },
 {
  "id": "singapore-sling",
  "name": "Singapore Sling",
  "kategorie": "exotisch",
  "glas": "Hurricane-Glas",
  "technik": "Shaken",
  "staerke": 3,
  "zeit": 5,
  "geschmack": [
   "fruchtig",
   "süß",
   "kräuterig"
  ],
  "beschreibung": "Der berühmte Gin-Cocktail aus dem Raffles Hotel: rosa, fruchtig und leicht kräuterig.",
  "garnitur": "Ananasscheibe und Kirsche",
  "zutaten": [
   {
    "m": 30,
    "e": "ml",
    "n": "Gin",
    "v": 40
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Kirschlikör",
    "v": 24
   },
   {
    "m": 7.5,
    "e": "ml",
    "n": "Cointreau",
    "v": 40
   },
   {
    "m": 7.5,
    "e": "ml",
    "n": "Bénédictine",
    "v": 40
   },
   {
    "m": 120,
    "e": "ml",
    "n": "Frischer Ananassaft",
    "v": 0
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   },
   {
    "m": 10,
    "e": "ml",
    "n": "Grenadine",
    "v": 0
   },
   {
    "m": 1,
    "e": "Dash",
    "n": "Angostura Bitters",
    "v": 44.7,
    "ml": 0.6
   }
  ],
  "schritte": [
   {
    "t": "Alle Zutaten in den Shaker geben.",
    "z": [
     0,
     1,
     2,
     3,
     4,
     5,
     6,
     7
    ]
   },
   {
    "t": "Mit Eiswürfeln füllen und gut shaken.",
    "z": []
   },
   {
    "t": "In ein Hurricane-Glas abseihen.",
    "z": []
   },
   {
    "t": "Mit Ananas und Kirsche garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/singapore-sling.jpg",
  "credit": {
   "datei": "Singapore Sling Cocktail.jpg",
   "autor": "James Cridland",
   "lizenz": "CC BY 2.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Singapore_Sling_Cocktail.jpg"
  },
  "profil": {
   "fruchtig": 3,
   "suess": 2,
   "wuerzig": 1
  },
  "basis": [
   "gin",
   "likoer"
  ],
  "stil": [
   "exotisch"
  ]
 },
 {
  "id": "sex-on-the-beach",
  "name": "Sex on the Beach",
  "kategorie": "exotisch",
  "glas": "Highball",
  "technik": "Bauen",
  "staerke": 2,
  "zeit": 2,
  "geschmack": [
   "fruchtig",
   "süß"
  ],
  "beschreibung": "Fruchtig, bunt und mild, der Strandklassiker mit Pfirsich, Orange und Cranberry.",
  "garnitur": "Orangenscheibe und Kirsche",
  "zutaten": [
   {
    "m": 40,
    "e": "ml",
    "n": "Wodka",
    "v": 40
   },
   {
    "m": 20,
    "e": "ml",
    "n": "Pfirsichlikör",
    "v": 20
   },
   {
    "m": 40,
    "e": "ml",
    "n": "Frischer Orangensaft",
    "v": 0
   },
   {
    "m": 40,
    "e": "ml",
    "n": "Cranberrysaft",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Highball mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Wodka und Pfirsichlikör eingießen.",
    "z": [
     0,
     1
    ]
   },
   {
    "t": "Orangensaft und Cranberrysaft dazugeben.",
    "z": [
     2,
     3
    ]
   },
   {
    "t": "Kurz umrühren und garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/sex-on-the-beach.jpg",
  "credit": {
   "datei": "Sex On The Beach Recipe.jpg",
   "autor": "CrystalMixer - CrystalMixer.com",
   "lizenz": "CC BY-SA 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Sex_On_The_Beach_Recipe.jpg"
  },
  "profil": {
   "suess": 3,
   "fruchtig": 3
  },
  "basis": [
   "wodka",
   "likoer"
  ],
  "stil": [
   "exotisch"
  ]
 },
 {
  "id": "tequila-sunrise",
  "name": "Tequila Sunrise",
  "kategorie": "exotisch",
  "glas": "Highball",
  "technik": "Bauen",
  "staerke": 2,
  "zeit": 2,
  "geschmack": [
   "fruchtig",
   "süß"
  ],
  "beschreibung": "Der Sonnenaufgang im Glas: Orange oben, Grenadine unten, ein Farbverlauf zum Genießen.",
  "garnitur": "Orangenscheibe, Kirsche",
  "zutaten": [
   {
    "m": 45,
    "e": "ml",
    "n": "Tequila",
    "v": 40
   },
   {
    "m": 90,
    "e": "ml",
    "n": "Frischer Orangensaft",
    "v": 0
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Grenadine",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Highball mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Tequila und Orangensaft direkt eingießen.",
    "z": [
     0,
     1
    ]
   },
   {
    "t": "Grenadine langsam am Rand einlaufen lassen, nicht rühren. So entsteht der Sonnenaufgang.",
    "z": [
     2
    ]
   },
   {
    "t": "Mit Orangenscheibe garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/tequila-sunrise.jpg",
  "credit": {
   "datei": "Tequila Sunrise 2013.JPG",
   "autor": "stavros1",
   "lizenz": "CC BY 3.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Tequila_Sunrise_2013.JPG"
  },
  "profil": {
   "suess": 3,
   "fruchtig": 3
  },
  "basis": [
   "tequila"
  ],
  "stil": [
   "exotisch"
  ]
 },
 {
  "id": "caribbean-summer",
  "name": "Caribbean Summer",
  "kategorie": "exotisch",
  "glas": "Hurricane-Glas oder Highball",
  "technik": "Shaken",
  "staerke": 3,
  "zeit": 4,
  "geschmack": [
   "fruchtig",
   "cremig",
   "frisch"
  ],
  "beschreibung": "Karibischer Sommerdrink in Türkis: Kokosrum, Ananas und Blue Curaçao.",
  "garnitur": "Ananasblatt, Minze, Kirsche",
  "zutaten": [
   {
    "m": 40,
    "e": "ml",
    "n": "Kokosrum",
    "v": 21
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Blue Curaçao",
    "v": 20
   },
   {
    "m": 60,
    "e": "ml",
    "n": "Frischer Ananassaft",
    "v": 0
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   },
   {
    "m": 10,
    "e": "ml",
    "n": "Zuckersirup",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Glas mit Eis füllen.",
    "z": []
   },
   {
    "t": "Kokosrum, Blue Curaçao, Ananassaft, Limette und Sirup in den Shaker geben.",
    "z": [
     0,
     1,
     2,
     3,
     4
    ]
   },
   {
    "t": "Kräftig shaken.",
    "z": []
   },
   {
    "t": "In das Glas auf frisches Eis abseihen.",
    "z": []
   },
   {
    "t": "Mit Ananasblatt, Minze und Kirsche garnieren.",
    "z": []
   }
  ],
  "quelle": "Hausrezept",
  "hinweis": "Eigenes Rezept in Anlehnung an Blue-Caribbean-Varianten, kein feststehender Standard.",
  "bild": "bilder/caribbean-summer.jpg",
  "credit": {
   "datei": "BlueLagoon copier.jpg",
   "autor": "Franzarthurmacelhone",
   "lizenz": "CC BY-SA 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:BlueLagoon_copier.jpg"
  },
  "profil": {
   "suess": 2,
   "fruchtig": 3,
   "cremig": 2
  },
  "basis": [
   "rum",
   "likoer"
  ],
  "stil": [
   "exotisch"
  ]
 },
 {
  "id": "aloha-ice-jam",
  "name": "Aloha Ice Jam",
  "kategorie": "exotisch",
  "glas": "Hohes Glas",
  "technik": "Mixen",
  "staerke": 3,
  "zeit": 4,
  "geschmack": [
   "fruchtig",
   "eisig",
   "süß"
  ],
  "beschreibung": "Eisige Hawaii-Variante: Rum, Wodka und Blue Curaçao frozen mit Ananas.",
  "garnitur": "Ananasscheibe, Cocktailschirmchen",
  "zutaten": [
   {
    "m": 30,
    "e": "ml",
    "n": "Weißer Rum",
    "v": 40
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Wodka",
    "v": 40
   },
   {
    "m": 20,
    "e": "ml",
    "n": "Blue Curaçao",
    "v": 20
   },
   {
    "m": 60,
    "e": "ml",
    "n": "Frischer Ananassaft",
    "v": 0
   },
   {
    "m": 20,
    "e": "ml",
    "n": "Frischer Zitronensaft",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Alle Zutaten mit einer Tasse Crushed Ice in den Mixer geben.",
    "z": [
     0,
     1,
     2,
     3,
     4
    ]
   },
   {
    "t": "Mixen, bis eine feine, eisige Konsistenz entsteht.",
    "z": []
   },
   {
    "t": "In ein hohes Glas füllen.",
    "z": []
   },
   {
    "t": "Mit Ananas und Schirmchen garnieren.",
    "z": []
   }
  ],
  "quelle": "Hausrezept",
  "hinweis": "Zu dem Namen gibt es kein bekanntes Standardrezept. Das ist ein Vorschlag, bitte bei Bedarf austauschen.",
  "bild": "bilder/aloha-ice-jam.jpg",
  "credit": {
   "datei": "Koh Lipe & Blue Hawaii 💚💙.jpg",
   "autor": "Sharon Hahn Darlin",
   "lizenz": "CC BY 2.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Koh_Lipe_%26_Blue_Hawaii_%F0%9F%92%9A%F0%9F%92%99.jpg"
  },
  "profil": {
   "suess": 2,
   "fruchtig": 3,
   "sauer": 1
  },
  "basis": [
   "rum",
   "wodka",
   "likoer"
  ],
  "stil": [
   "exotisch"
  ]
 },
 {
  "id": "mojito",
  "name": "Mojito",
  "kategorie": "longdrink",
  "glas": "Highball",
  "technik": "Bauen",
  "staerke": 2,
  "zeit": 4,
  "geschmack": [
   "frisch",
   "minzig",
   "sauer"
  ],
  "beschreibung": "Kubas Sommerdrink: Minze, Limette, Rum und Soda. Leicht, erfrischend, unverwüstlich.",
  "garnitur": "Minzzweig, Limettenspalte",
  "zutaten": [
   {
    "m": 45,
    "e": "ml",
    "n": "Weißer Rum",
    "v": 40
   },
   {
    "m": 20,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   },
   {
    "m": 6,
    "e": "Zweige",
    "n": "Minze",
    "v": 0,
    "ml": 0
   },
   {
    "m": 2,
    "e": "TL",
    "n": "Rohrzucker",
    "v": 0,
    "ml": 5
   },
   {
    "m": null,
    "e": "",
    "n": "Sodawasser zum Auffüllen",
    "v": 0,
    "ml": 60
   }
  ],
  "schritte": [
   {
    "t": "Minze, Zucker und Limettensaft im Glas vorsichtig andrücken, nicht zerreißen.",
    "z": [
     1,
     2,
     3
    ]
   },
   {
    "t": "Einen Schuss Sodawasser dazugeben.",
    "z": []
   },
   {
    "t": "Glas mit Eis füllen und den Rum eingießen.",
    "z": [
     0
    ]
   },
   {
    "t": "Mit Sodawasser auffüllen.",
    "z": [
     4
    ]
   },
   {
    "t": "Einmal kurz umrühren, mit Minze garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/mojito.jpg",
  "credit": {
   "datei": "Fresh Mojito Premium.jpg",
   "autor": "Rjcastillo",
   "lizenz": "CC BY-SA 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Fresh_Mojito_Premium.jpg"
  },
  "profil": {
   "sauer": 2,
   "wuerzig": 2,
   "suess": 1
  },
  "basis": [
   "rum"
  ],
  "stil": [
   "longdrink",
   "exotisch"
  ]
 },
 {
  "id": "caipirinha",
  "name": "Caipirinha",
  "kategorie": "longdrink",
  "glas": "Tumbler (Doppel-Rocks)",
  "technik": "Bauen",
  "staerke": 4,
  "zeit": 3,
  "geschmack": [
   "sauer",
   "frisch"
  ],
  "beschreibung": "Brasiliens Nationaldrink: Cachaça, Limette und Zucker auf Eis.",
  "garnitur": "Limettenspalte",
  "zutaten": [
   {
    "m": 60,
    "e": "ml",
    "n": "Cachaça",
    "v": 40
   },
   {
    "m": 1,
    "e": "Stk",
    "n": "Limette, in Spalten",
    "v": 0,
    "ml": 25
   },
   {
    "m": 4,
    "e": "TL",
    "n": "Weißer Rohrzucker",
    "v": 0,
    "ml": 5
   }
  ],
  "schritte": [
   {
    "t": "Limettenspalten und Zucker ins Glas geben und leicht andrücken.",
    "z": [
     1,
     2
    ]
   },
   {
    "t": "Glas mit Crushed Ice füllen.",
    "z": []
   },
   {
    "t": "Cachaça darübergießen.",
    "z": [
     0
    ]
   },
   {
    "t": "Sanft umrühren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/caipirinha.jpg",
  "credit": {
   "datei": "Caipirinha on ice cubes.jpg",
   "autor": "Cocktailmarler",
   "lizenz": "CC BY-SA 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Caipirinha_on_ice_cubes.jpg"
  },
  "profil": {
   "sauer": 3,
   "suess": 1
  },
  "basis": [
   "cachaca"
  ],
  "stil": [
   "longdrink",
   "exotisch"
  ]
 },
 {
  "id": "long-island",
  "name": "Long Island Iced Tea",
  "kategorie": "longdrink",
  "glas": "Highball",
  "technik": "Bauen",
  "staerke": 5,
  "zeit": 3,
  "geschmack": [
   "stark",
   "frisch",
   "süß"
  ],
  "beschreibung": "Fünf Spirituosen, die nach Eistee aussehen und deutlich stärker sind, als sie schmecken.",
  "garnitur": "Zitronenscheibe",
  "zutaten": [
   {
    "m": 15,
    "e": "ml",
    "n": "Wodka",
    "v": 40
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Tequila",
    "v": 40
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Weißer Rum",
    "v": 40
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Gin",
    "v": 40
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Cointreau",
    "v": 40
   },
   {
    "m": 30,
    "e": "ml",
    "n": "Frischer Zitronensaft",
    "v": 0
   },
   {
    "m": 20,
    "e": "ml",
    "n": "Zuckersirup",
    "v": 0
   },
   {
    "m": null,
    "e": "",
    "n": "Cola zum Auffüllen",
    "v": 0,
    "ml": 80
   }
  ],
  "schritte": [
   {
    "t": "Highball mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Alle Spirituosen, Zitronensaft und Sirup eingießen.",
    "z": [
     0,
     1,
     2,
     3,
     4,
     5,
     6
    ]
   },
   {
    "t": "Mit Cola auffüllen.",
    "z": [
     7
    ]
   },
   {
    "t": "Sanft umrühren und mit Zitrone garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/long-island.jpg",
  "credit": {
   "datei": "Long Island Iced Tea with Lemon and Straw.jpg",
   "autor": "Alisdair McDiarmid from Glasgow, United Kingdom",
   "lizenz": "CC BY 2.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Long_Island_Iced_Tea_with_Lemon_and_Straw.jpg"
  },
  "profil": {
   "suess": 2,
   "sauer": 2
  },
  "basis": [
   "wodka",
   "tequila",
   "rum",
   "gin",
   "likoer"
  ],
  "stil": [
   "longdrink"
  ]
 },
 {
  "id": "moscow-mule",
  "name": "Moscow Mule",
  "kategorie": "longdrink",
  "glas": "Kupferbecher",
  "technik": "Bauen",
  "staerke": 3,
  "zeit": 2,
  "geschmack": [
   "würzig",
   "frisch",
   "scharf"
  ],
  "beschreibung": "Wodka, Ginger Beer und Limette im kalten Kupferbecher.",
  "garnitur": "Limettenspalte, Minze",
  "zutaten": [
   {
    "m": 45,
    "e": "ml",
    "n": "Wodka",
    "v": 40
   },
   {
    "m": 120,
    "e": "ml",
    "n": "Ginger Beer",
    "v": 0
   },
   {
    "m": 10,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Kupferbecher mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Wodka und Ginger Beer eingießen.",
    "z": [
     0,
     1
    ]
   },
   {
    "t": "Limettensaft dazugeben und sanft umrühren.",
    "z": [
     2
    ]
   },
   {
    "t": "Mit Limette und Minze garnieren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/moscow-mule.jpg",
  "credit": {
   "datei": "Moscow Mule.jpg",
   "autor": "edseloh",
   "lizenz": "CC BY-SA 2.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Moscow_Mule.jpg"
  },
  "profil": {
   "wuerzig": 3,
   "sauer": 1,
   "suess": 1
  },
  "basis": [
   "wodka"
  ],
  "stil": [
   "longdrink"
  ]
 },
 {
  "id": "cuba-libre",
  "name": "Cuba Libre",
  "kategorie": "longdrink",
  "glas": "Highball",
  "technik": "Bauen",
  "staerke": 2,
  "zeit": 2,
  "geschmack": [
   "süß",
   "frisch"
  ],
  "beschreibung": "Rum, Cola und ein Spritzer Limette: simpel und überall beliebt.",
  "garnitur": "Limettenspalte",
  "zutaten": [
   {
    "m": 50,
    "e": "ml",
    "n": "Weißer Rum",
    "v": 40
   },
   {
    "m": 120,
    "e": "ml",
    "n": "Cola",
    "v": 0
   },
   {
    "m": 10,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Highball mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Rum und Limettensaft eingießen.",
    "z": [
     0,
     2
    ]
   },
   {
    "t": "Mit Cola auffüllen.",
    "z": [
     1
    ]
   },
   {
    "t": "Einmal umrühren, Limettenspalte dazu.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/cuba-libre.jpg",
  "credit": {
   "datei": "15-09-26-RalfR-WLC-0056.jpg",
   "autor": "Ralf Roletschek",
   "lizenz": "CC BY-SA 3.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:15-09-26-RalfR-WLC-0056.jpg"
  },
  "profil": {
   "suess": 3,
   "sauer": 1
  },
  "basis": [
   "rum"
  ],
  "stil": [
   "longdrink",
   "exotisch"
  ]
 },
 {
  "id": "paloma",
  "name": "Paloma",
  "kategorie": "longdrink",
  "glas": "Highball",
  "technik": "Bauen",
  "staerke": 2,
  "zeit": 2,
  "geschmack": [
   "herb",
   "frisch",
   "salzig"
  ],
  "beschreibung": "Mexikos meistgetrunkener Tequila-Drink: Grapefruit, Limette und eine Prise Salz.",
  "garnitur": "Grapefruit- oder Limettenscheibe",
  "zutaten": [
   {
    "m": 50,
    "e": "ml",
    "n": "Tequila (100 % Agave)",
    "v": 40
   },
   {
    "m": 5,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   },
   {
    "m": 1,
    "e": "Prise",
    "n": "Salz",
    "v": 0,
    "ml": 0
   },
   {
    "m": 100,
    "e": "ml",
    "n": "Pink-Grapefruit-Soda",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Tequila ins Highball gießen und Limettensaft dazupressen.",
    "z": [
     0,
     1
    ]
   },
   {
    "t": "Eis und eine Prise Salz hinzufügen.",
    "z": [
     2
    ]
   },
   {
    "t": "Mit Grapefruit-Soda auffüllen.",
    "z": [
     3
    ]
   },
   {
    "t": "Sanft umrühren.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/paloma.jpg",
  "credit": {
   "datei": "Paloma Cocktail2.jpg",
   "autor": "Erich Wagner (www.eventografie.de)",
   "lizenz": "CC BY-SA 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Paloma_Cocktail2.jpg"
  },
  "profil": {
   "sauer": 2,
   "salzig": 2,
   "bitter": 1,
   "fruchtig": 1
  },
  "basis": [
   "tequila"
  ],
  "stil": [
   "longdrink",
   "exotisch"
  ]
 },
 {
  "id": "spritz",
  "name": "Spritz Veneziano",
  "kategorie": "longdrink",
  "glas": "Weinglas",
  "technik": "Bauen",
  "staerke": 1,
  "zeit": 2,
  "geschmack": [
   "bitter",
   "frisch",
   "spritzig"
  ],
  "beschreibung": "Italienischer Aperitivo: Prosecco, Aperol und Soda auf Eis.",
  "garnitur": "Orangenscheibe",
  "zutaten": [
   {
    "m": 90,
    "e": "ml",
    "n": "Prosecco",
    "v": 11
   },
   {
    "m": 60,
    "e": "ml",
    "n": "Aperol",
    "v": 11
   },
   {
    "m": null,
    "e": "",
    "n": "Schuss Sodawasser",
    "v": 0,
    "ml": 30
   }
  ],
  "schritte": [
   {
    "t": "Weinglas mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Prosecco eingießen, dann Aperol.",
    "z": [
     0,
     1
    ]
   },
   {
    "t": "Einen Schuss Sodawasser dazugeben.",
    "z": [
     2
    ]
   },
   {
    "t": "Sanft umrühren, Orangenscheibe dazu.",
    "z": []
   }
  ],
  "quelle": "IBA",
  "hinweis": "",
  "bild": "bilder/spritz.jpg",
  "credit": {
   "datei": "Aperol Spritz - July 2024 - Sarah Stierch.jpg",
   "autor": "Missvain",
   "lizenz": "CC0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Aperol_Spritz_-_July_2024_-_Sarah_Stierch.jpg"
  },
  "profil": {
   "bitter": 2,
   "suess": 2,
   "fruchtig": 1
  },
  "basis": [
   "schaumwein",
   "bitter"
  ],
  "stil": [
   "longdrink"
  ]
 },
 {
  "id": "virgin-colada",
  "name": "Virgin Colada",
  "kategorie": "alkoholfrei",
  "glas": "Großes Glas",
  "technik": "Mixen",
  "staerke": 0,
  "zeit": 4,
  "geschmack": [
   "cremig",
   "fruchtig",
   "süß"
  ],
  "beschreibung": "Die Piña Colada ohne Rum: Ananas und Kokos, eiskalt und cremig gemixt.",
  "garnitur": "Ananasscheibe und Cocktailkirsche",
  "zutaten": [
   {
    "m": 120,
    "e": "ml",
    "n": "Frischer Ananassaft",
    "v": 0
   },
   {
    "m": 40,
    "e": "ml",
    "n": "Kokoscreme",
    "v": 0
   },
   {
    "m": 10,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Alle Zutaten mit einer Tasse Crushed Ice in den Mixer geben.",
    "z": [
     0,
     1,
     2
    ]
   },
   {
    "t": "Cremig mixen, bis keine Eisstücke mehr da sind.",
    "z": []
   },
   {
    "t": "In ein großes Glas gießen.",
    "z": []
   },
   {
    "t": "Mit Ananas und Kirsche garnieren.",
    "z": []
   }
  ],
  "quelle": "Standardrezept",
  "hinweis": "Alkoholfreie Variante nach gängigem Standardrezept, Mengen redaktionell festgelegt.",
  "bild": "bilder/virgin-colada.jpg",
  "credit": {
   "datei": "Virgin Colada - Enzo's 2026-05-05.jpg",
   "autor": "Andy Li",
   "lizenz": "CC0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Virgin_Colada_-_Enzo%27s_2026-05-05.jpg"
  },
  "profil": {
   "suess": 3,
   "cremig": 3,
   "fruchtig": 3
  },
  "basis": [],
  "stil": [
   "alkoholfrei",
   "exotisch"
  ]
 },
 {
  "id": "virgin-mojito",
  "name": "Virgin Mojito",
  "kategorie": "alkoholfrei",
  "glas": "Highball",
  "technik": "Bauen",
  "staerke": 0,
  "zeit": 3,
  "geschmack": [
   "frisch",
   "minzig",
   "sauer"
  ],
  "beschreibung": "Minze, Limette und Soda wie beim Mojito, nur ohne Rum. Der Klassiker unter den Alkoholfreien.",
  "garnitur": "Minzzweig, Limettenspalte",
  "zutaten": [
   {
    "m": 25,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   },
   {
    "m": 8,
    "e": "Zweige",
    "n": "Minze",
    "v": 0,
    "ml": 0
   },
   {
    "m": 2,
    "e": "TL",
    "n": "Rohrzucker",
    "v": 0,
    "ml": 5
   },
   {
    "m": null,
    "e": "",
    "n": "Sodawasser zum Auffüllen",
    "v": 0,
    "ml": 120
   }
  ],
  "schritte": [
   {
    "t": "Minze, Zucker und Limettensaft im Glas vorsichtig andrücken.",
    "z": [
     0,
     1,
     2
    ]
   },
   {
    "t": "Glas mit Crushed Ice füllen.",
    "z": []
   },
   {
    "t": "Mit Sodawasser auffüllen.",
    "z": [
     3
    ]
   },
   {
    "t": "Einmal umrühren, mit Minze und Limette garnieren.",
    "z": []
   }
  ],
  "quelle": "Standardrezept",
  "hinweis": "Alkoholfreie Variante nach gängigem Standardrezept, Mengen redaktionell festgelegt. Das Foto zeigt einen Mojito, der genauso aussieht.",
  "bild": "bilder/virgin-mojito.jpg",
  "credit": {
   "datei": "Mojito, Mazatlán, 30 de noviembre de 2022.jpg",
   "autor": "El Nuevo Doge",
   "lizenz": "CC0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Mojito,_Mazatl%C3%A1n,_30_de_noviembre_de_2022.jpg"
  },
  "profil": {
   "sauer": 2,
   "wuerzig": 2,
   "suess": 1
  },
  "basis": [],
  "stil": [
   "alkoholfrei",
   "exotisch"
  ]
 },
 {
  "id": "shirley-temple",
  "name": "Shirley Temple",
  "kategorie": "alkoholfrei",
  "glas": "Highball",
  "technik": "Bauen",
  "staerke": 0,
  "zeit": 2,
  "geschmack": [
   "süß",
   "fruchtig",
   "spritzig"
  ],
  "beschreibung": "Der berühmteste Mocktail der Welt: Ginger Ale mit Grenadine und einer Kirsche.",
  "garnitur": "Cocktailkirsche, Limettenscheibe",
  "zutaten": [
   {
    "m": 150,
    "e": "ml",
    "n": "Ginger Ale",
    "v": 0
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Grenadine",
    "v": 0
   },
   {
    "m": 10,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   }
  ],
  "schritte": [
   {
    "t": "Highball mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Ginger Ale und Limettensaft eingießen.",
    "z": [
     0,
     2
    ]
   },
   {
    "t": "Grenadine langsam darüberlaufen lassen.",
    "z": [
     1
    ]
   },
   {
    "t": "Mit Kirsche und Limette garnieren.",
    "z": []
   }
  ],
  "quelle": "Standardrezept",
  "hinweis": "Alkoholfreie Variante nach gängigem Standardrezept, Mengen redaktionell festgelegt.",
  "bild": "bilder/shirley-temple.jpg",
  "credit": {
   "datei": "Canadia-style Shirley Temple.jpg",
   "autor": "Ryan Forsythe (fweez)",
   "lizenz": "CC BY-SA 2.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Canadia-style_Shirley_Temple.jpg"
  },
  "profil": {
   "suess": 3,
   "fruchtig": 1,
   "wuerzig": 1
  },
  "basis": [],
  "stil": [
   "alkoholfrei"
  ]
 },
 {
  "id": "virgin-margarita",
  "name": "Virgin Margarita",
  "kategorie": "alkoholfrei",
  "glas": "Tumbler oder Margaritaglas",
  "technik": "Shaken",
  "staerke": 0,
  "zeit": 3,
  "geschmack": [
   "sauer",
   "frisch",
   "salzig"
  ],
  "beschreibung": "Limette, Orange und ein Hauch Agave mit Salzrand. Schmeckt nach Margarita, ganz ohne Tequila.",
  "garnitur": "Salzrand, Limettenscheibe",
  "zutaten": [
   {
    "m": 30,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   },
   {
    "m": 40,
    "e": "ml",
    "n": "Frischer Orangensaft",
    "v": 0
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Agavendicksaft",
    "v": 0
   },
   {
    "m": null,
    "e": "",
    "n": "Schuss Sodawasser",
    "v": 0,
    "ml": 30
   }
  ],
  "schritte": [
   {
    "t": "Glasrand mit Limette befeuchten und in Salz drehen.",
    "z": []
   },
   {
    "t": "Limettensaft, Orangensaft und Agavendicksaft in den Shaker geben.",
    "z": [
     0,
     1,
     2
    ]
   },
   {
    "t": "Mit Eis füllen und kräftig shaken.",
    "z": []
   },
   {
    "t": "Auf Eis ins Glas abseihen und mit einem Schuss Soda toppen.",
    "z": [
     3
    ]
   }
  ],
  "quelle": "Standardrezept",
  "hinweis": "Alkoholfreie Variante nach gängigem Standardrezept, Mengen redaktionell festgelegt.",
  "bild": "bilder/virgin-margarita.jpg",
  "credit": {
   "datei": "Mocktail Margarita - Food for Friends 2026-03-09.jpg",
   "autor": "Andy Li",
   "lizenz": "CC0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Mocktail_Margarita_-_Food_for_Friends_2026-03-09.jpg"
  },
  "profil": {
   "sauer": 3,
   "salzig": 2,
   "fruchtig": 1,
   "suess": 1
  },
  "basis": [],
  "stil": [
   "alkoholfrei",
   "exotisch"
  ]
 },
 {
  "id": "apfel-holunder-fizz",
  "name": "Apfel-Holunder-Fizz",
  "kategorie": "alkoholfrei",
  "glas": "Highball",
  "technik": "Bauen",
  "staerke": 0,
  "zeit": 2,
  "geschmack": [
   "fruchtig",
   "frisch",
   "spritzig"
  ],
  "beschreibung": "Apfelsaft und Holunderblüte, aufgefüllt mit Soda. Leicht, blumig und erfrischend.",
  "garnitur": "Apfelscheibe oder getrocknete Zitrone",
  "zutaten": [
   {
    "m": 80,
    "e": "ml",
    "n": "Naturtrüber Apfelsaft",
    "v": 0
   },
   {
    "m": 20,
    "e": "ml",
    "n": "Holunderblütensirup",
    "v": 0
   },
   {
    "m": 10,
    "e": "ml",
    "n": "Frischer Zitronensaft",
    "v": 0
   },
   {
    "m": null,
    "e": "",
    "n": "Sodawasser zum Auffüllen",
    "v": 0,
    "ml": 80
   }
  ],
  "schritte": [
   {
    "t": "Highball mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Apfelsaft, Holunderblütensirup und Zitronensaft eingießen.",
    "z": [
     0,
     1,
     2
    ]
   },
   {
    "t": "Mit Sodawasser auffüllen.",
    "z": [
     3
    ]
   },
   {
    "t": "Sanft umrühren und garnieren.",
    "z": []
   }
  ],
  "quelle": "Standardrezept",
  "hinweis": "Alkoholfreie Variante nach gängigem Standardrezept, Mengen redaktionell festgelegt.",
  "bild": "bilder/apfel-holunder-fizz.jpg",
  "credit": {
   "datei": "Apple & Elderflower Fizz - Petit Pois Restaurant 2024-07-11.jpg",
   "autor": "Andy Li",
   "lizenz": "CC0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Apple_%26_Elderflower_Fizz_-_Petit_Pois_Restaurant_2024-07-11.jpg"
  },
  "profil": {
   "fruchtig": 2,
   "suess": 2,
   "sauer": 1,
   "wuerzig": 1
  },
  "basis": [],
  "stil": [
   "alkoholfrei"
  ]
 },
 {
  "id": "maracuja-spritz",
  "name": "Maracuja Spritz",
  "kategorie": "alkoholfrei",
  "glas": "Highball",
  "technik": "Bauen",
  "staerke": 0,
  "zeit": 2,
  "geschmack": [
   "fruchtig",
   "exotisch",
   "spritzig"
  ],
  "beschreibung": "Exotisch und prickelnd: Maracuja und Limette mit einem Schuss Grenadine, aufgefüllt mit Soda.",
  "garnitur": "Getrocknete Orangenscheibe",
  "zutaten": [
   {
    "m": 60,
    "e": "ml",
    "n": "Maracujasaft",
    "v": 0
   },
   {
    "m": 15,
    "e": "ml",
    "n": "Frischer Limettensaft",
    "v": 0
   },
   {
    "m": 10,
    "e": "ml",
    "n": "Grenadine",
    "v": 0
   },
   {
    "m": null,
    "e": "",
    "n": "Sodawasser zum Auffüllen",
    "v": 0,
    "ml": 100
   }
  ],
  "schritte": [
   {
    "t": "Highball mit Eiswürfeln füllen.",
    "z": []
   },
   {
    "t": "Maracujasaft und Limettensaft eingießen.",
    "z": [
     0,
     1
    ]
   },
   {
    "t": "Grenadine dazugeben.",
    "z": [
     2
    ]
   },
   {
    "t": "Mit Sodawasser auffüllen, sanft umrühren und garnieren.",
    "z": [
     3
    ]
   }
  ],
  "quelle": "Standardrezept",
  "hinweis": "Hausrezept, inspiriert von alkoholfreien Passionsfrucht-Spritz-Drinks.",
  "bild": "bilder/maracuja-spritz.jpg",
  "credit": {
   "datei": "Passionola Spritz - Mocktail at High Hat Cafe, New Orleans.jpg",
   "autor": "Paul Lowry",
   "lizenz": "CC BY 4.0",
   "quelle": "https://commons.wikimedia.org/wiki/File:Passionola_Spritz_-_Mocktail_at_High_Hat_Cafe,_New_Orleans.jpg"
  },
  "profil": {
   "fruchtig": 3,
   "sauer": 2,
   "suess": 2
  },
  "basis": [],
  "stil": [
   "alkoholfrei",
   "exotisch"
  ]
 }
];
