#!/usr/bin/env python3
DIALOGUE_TRANSLATIONS = {
46: [
"Here!... The bunch of keys to the hoarding granary whose contents were going to turn into money on the black market! The bunch of keys that will help distribute to the townspeople the food grains imprisoned in the great granary instead of serving the people!... Come with me!..."
],
47: [
"Your husband's command, child?.. You took the granary key and gave it to him!..",
"What is wrong with that, Appa?...",
"There is nothing wrong, child!.. Nothing wrong!.. Ha! Ha! Ha! Ha!...."
],
48: [],
49: [
"There, you can see it! That is... the hoarding warehouse of that daylight masquerader!... Inside are hundreds of thousands' worth of what belongs to you!... Come; I will take out and give you the food grain you need!...",
"Kalinga! Give each person as much as they need!... What am I going to do keeping all this? Today is my birthday!",
"(looking sharply at the zamindar) Don't tell them outside which birthday it is!.. The whole year is your birthday—give generously to everyone—eat well, bless him and go! Come, everyone... take everything... come... take whatever is being given and praise our master as the great benefactor Pari before you go! Why are you standing there? Come...",
"What, son-in-law!... Have you ever at least read a story in which a goat played in front of a tiger?",
"The time will come!.. The disguise will fall away! I will defeat you!...",
"Ha! Ha! Ha! Poor fellow, you are trying to bend the sky into a bow!... Impossible, son-in-law... impossible!...",
"We shall see!...",
"Hmm!... We shall see!... This is my birthday vow!.. This Zamindar Aimpuling Bhoopathi will not lose to anyone—will never lose!"
],
50: [
"Giving thanks to almighty God, at this birthday celebration I declare that, as always, I stand before you as a man of noble character, a generous heart and disciplined conduct, labouring for your sake!... Long live the name of God!",
"The name!...",
"Long live!..",
"The name!..",
"Long live!..",
"For Zamindar Aimpuling Bhoopathi—",
"Victory!",
"(opening his eyes wide) Kalinga! Who is that?..",
"Our cymbal-beating poet!... He takes Tamil and beats it just like that. (gesturing as though playing jalra cymbals)",
"Oh.. the poet?.. Are you well?...",
"Greetings. May you live many years!... I have come into your presence seeking a birthday gift!...",
"Oh.. is that so? (looking at Poongodi) Who is this?",
"Don't you recognize her? Ten or fifteen years ago! My daughter Poongodi, whom I brought here as a green little baby!...",
"Have you forgotten? Back then that baby was nice and plump. Tiny.. You would hold her chest to chest and play with her for fun!... She'd wipe her running nose on me!... You've forgotten... She was little then! Now she's grown into a young woman!...",
"She has now become a woman of marriageable age!... You yourself must take the initiative and arrange her marriage....",
"I will conduct it! There is no obstacle... Kalinga! The whole earth knows the regard we show poets!... Take the poet and child Poongodi away and... (signals with his eyes) give them proper hospitality...",
"I understand, my lord... I understand! Poet, come!... Child Poongodi, come!... You are a lucky girl! The zamindar's gaze has fallen on you.. What comes next is still ahead—come!...",
"What is it, Uma?",
"Appa!... On Aththan's behalf, I present you this birthday gift!...",
"The bridegroom gave it?.. Thank you very much, child! Uma, where is the bridegroom?",
"He'll be here shortly, Appa!...",
"Aha... a very beautiful painting! But the place where this belongs is Sadaiyan's house.. Sadaiya!... Sambandhi! A gift from my son-in-law Vingan!... Hang it in your own house! It looks very good, doesn't it!... Here!"
]
}

DIALOGUE_NOTES = {
(49,4): ['`வேங்கை` is a tiger and `வெள்ளாடு` a goat; the source uses the predator/prey image as a warning.'],
(49,6): ['`வானத்தை வில்லாவளைக்க` is a hyperbolic image of attempting the impossible; English preserves the bow image.'],
(50,9): ['`ஜால்ரா` is both a pair of hand cymbals and a colloquial image for sycophantic praise; the source explicitly makes the gesture, so English preserves both senses.']
}

ND = {
46: [
{'text':'Town public hall.','locator_kind':'location-caption'},
{'text':'(The townspeople are gathered... Kannaayiram is there too.)'}
],
47: [
{'text':'Estate palace.','locator_kind':'location-caption'},
{'text':'(He laughs loudly, clapping his hands....)'}
],
48: [
{'kind':'performance-cue','occurrence_id':'vandikkaran-magan-perf-006','text':'(Vingan sings among the townspeople.)'},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-006','lines':['Working people!','My siblings!','Come along with me! — In broad','daylight, the tiger','that prowls the town—','I will show it; come and see!']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-006','lines':['Among human beings some','appear upon this earth','as though they were holy!','Like a mirage','that enchants the eyes','of deer! — Working people']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-006','lines':['Turning the ledger,','I will ask the selfish man','a question every day! — To','open his lock','and show you what lies there,','I have the key!']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-006','lines':['The goat that thinks this man','is its shepherd — if','a human being','blessed with sixfold reason','were to be the same,','the country would laugh! — Working people']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-006','lines':['By the light','of a firefly','you cannot see the road in darkness! — Hey;','just because it glitters,','a lump of salt','does not become a diamond!']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-006','lines':['When the pride of lions','lies asleep,','the little fox wags its tail! — When','that sleep is broken,','what will happen?','History will tell on that day! — Working people']}
],
49: [
{'text':'Hoarding warehouse.','locator_kind':'location-caption'},
{'text':'(Vingan arrives there with the crowd following him.)'},
{'text':'(He walks forward, taking out the key.)'},
{'text':'(There, amid another crowd, stand the zamindar and Kalingan, distributing rice, wheat and other grains by the armful. Vingan stops in astonishment at the sight...)'},
{'text':'(The friends behind Vingan run toward Kalingan... Vingan stands alone. The zamindar comes near him...)'}
],
50: [
{'text':'Estate palace.','locator_kind':'location-caption'},
{'text':'(Townspeople and men of rank are gathered in the hall. Maragatham, Kokila, Uma, Kalingarayan and Sadaiyan are also present.)'},
{'text':'(The poet stands with Poongodi.)'},
{'kind':'source-unlabelled','text':'Praise! Praise!...\nPraise to the holy one!...\nPraise to the virtuous one!...\nPraise to the honourable one!..\nPraise to the one who surpassed\nthe last seven great benefactors!...\nPraise to the Kali-age Maharaja Karna!...'},
{'kind':'source-unlabelled','text':'For my lord, the god\nof the poor, Aimpuling\nBhoopathi... may many more\nbirthday celebrations\ncome!..'},
{'kind':'source-unlabelled','text':'May he celebrate\nhis hundredth birthday,\nand may this humble servant too receive\nthe blessing of coming and praising him then!!'},
{'text':'(Kalingan leads away the poet’s daughter Poongodi. Many others present various costly gifts.)'},
{'text':'(The zamindar unwraps the paper around the gift. It is a painting of a woman being gored to death by a bull.)'},
{'text':'(Sadaiyan takes it and looks at it.)'}
]
}

DIALOGUE_OCCURRENCE_LINKS = {}
