#!/usr/bin/env python3
DIALOGUE_TRANSLATIONS = {
56: [
"Aththan!... A word to Appa,...",
"Take leave of Appa! Do not ask permission!....",
"(approaching) What is this, son-in-law?.. What is all this strange business?...",
"I am leaving because I cannot bear these outrages!... Bid farewell to your daughter and send her with me!...",
"Sadaiya!... Did you see?.. A girl raised in such wealth.. born and brought up in this palace of status and luxury, with a hundred servants ready at the flick of a finger and carrying out every command without refusal.. and the bridegroom says he will take her away to a mud hut... Is that fair?...",
"Why, son, have you gone mad? Why are you doing all this? Why are you causing such great pain in master's heart?.. And you say you'll take away a woman who is carrying a child!...",
"Uma! Set out!...",
"Uma!....",
"Appa! Forgive me! Wherever he is—that is heaven for me!.. I am going!.. (to Vingan) Shall we go?...",
"(to the zamindar) I'm going!... We haven't gone very far away, so we won't lose touch... (to Sadaiyan) Appa! It may look as though I'm doing wrong!... But... as time passes the truth will become clear!.. Forgive me! Shall I go?... Uma!.. Come!...",
"(falling at the zamindar's feet) Master.. forgive me!...",
"(with hatred in his heart) Hmm!.. You mustn't fall at my feet!.. Sambandhi... you must remain my sambandhi!...."
],
57: [
"What, Uma!... Is cooking difficult?... Is that why you're shedding tears?...",
"I'm not shedding tears; I can't bear the stove smoke!...",
"Here the stove is smoking, so tears are pouring from your eyes!... Do you know how many mothers in poor homes shed tears because they have no means even to make their stoves smoke?... All right!... All right!.... You eat... rest your eyes a little!... I'll take care of the cooking!...",
"Uh-uh... no... no... Once I get used to all this smoke it will be fine... You stay!.. I'll take care of it myself!..."
],
58: [
"Bull!... Bull! I've brought the mayilai bull...",
"Bravo, Kannaayiram!.. The right bull! You brought it just as I had in mind...",
"Uma!... Every day you must perform puja to this bull!...",
"Puja to a bull?... People perform cow worship only for Bhagavan!....",
"This is no ordinary bull—a bull that is going to be raised in our house for an ideal!... It will be fitting only if you perform puja to it!",
"If you say so, all right...",
"You must not perform the puja for my sake! You must worship it with the power of your own heart!...."
],
59: [
"Excellent! That's it!.... Kannaayiram!.. The bull has learned!... Now comes the next lesson it has to learn!....",
"Anna! Anna!... Uma akka has given birth to a baby!... The baby...",
"Ah!..... (joy)"
],
60: [
"Little அணிப்புள்ளே; little coconut-palm one;",
"A little child\ncarried in a mother's lap! — touch it\nand your hand will smell sweet—\na colourful little child!",
"—"
]
}

DIALOGUE_NOTES = {
(60,1): ['The opening folk endearments (`அணிப்புள்ளே; தென்னம் புள்ளே; கிளிப்புள்ளே; கிரிப்புள்ளே`) are highly idiomatic. English preserves the cumulative folk-call pattern and leaves the first opaque term in Tamil script rather than inventing a false meaning.'],
(60,3): ['The immutable dialogue record contains only Vingan’s printed turn marker `—`; the lyric body that follows is translated as source-linked song units.']
}

ND = {
56: [
{'text':'Estate palace.','locator_kind':'location-caption'},
{'text':'(Vingan and Uma are preparing to leave the house. As the zamindar approaches from the opposite direction, Uma looks at Vingan.)'},
{'text':'(Sadaiyan arrives.)'},
{'text':'(The two leave... The zamindar stands watching them. Pain shows on Sadaiyan’s face.)'}
],
57: [
{'text':'Hut.','locator_kind':'location-caption'},
{'text':'(The stove smokes... Uma cooks while rubbing her eyes. Unable to bear the smoke, tears stream from her eyes as she sits. Vingan, seated on a rope cot, watches her.)'},
{'text':'(He gets up... Uma catches his hand and stops him.)'}
],
58: [
{'text':'Exterior.','locator_kind':'location-caption'},
{'text':'Street adjoining the hut settlement.','locator_kind':'location-caption'},
{'text':'(Kannaayiram brings the bull.)'},
{'kind':'source-unlabelled','text':'(Turning toward the hut).... Uma! Uma!..... Come outside and look for a moment, Uma!...'},
{'text':'(Uma comes out of the hut; meanwhile several residents of the settlement gather around.)'},
{'text':'(Uma smiles and nods to say yes.)'}
],
59: [
{'text':'An enclosed ground.','locator_kind':'location-caption'},
{'text':'(Vingan and Kannaayiram train the bull... The bull charges fiercely, is urged forward by them and runs ahead... It gores a figure. It is not the zamindar, but a dummy resembling the zamindar.)'},
{'text':'(He laughs.) Ha! Ha! Ha! Ha!....'},
{'text':'(At that moment a little girl runs in....)'},
{'text':'(Vingan runs off.)'}
],
60: [
{'text':'Hut settlement.','locator_kind':'location-caption'},
{'text':'(People of the hut settlement, Vingan, Uma and others celebrate the child with song and dance...'},
{'text':'In the middle of the song Sadaiyan drives in the carriage, bringing the zamindar and Kalingan...'},
{'text':'The entire settlement is in festival dress.... Young women and young men all sing and dance, blessing the child.)'},
{'kind':'performance-cue','occurrence_id':'vandikkaran-magan-perf-008','text':'(Song.)'},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['To reform the town — a','child has been born! — To keep his father’s','name alive — he opened','both his eyes!','Beat the brass and drums,','girls! — Clap your','hands without missing','the beat, girls!']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['— To reform the town']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['Little parrot; little hill one;','Above all of them,','What kind of child is this?','Tell the child to dance!']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['— To reform the town']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['Like cucumber seeds','the child smiles, girl! — the child','is like a bright sesame','flower, girl!']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['The lotus has liquor within;','the jasmine lives in the wild—','in the thorn-filled settlement','this child was born! — Here','every hut in the settlement','knows it!']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['— To reform the town']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['The mother who bore him','is a rich woman! — The','fortunate father','is a worker!']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['To bring the high place and the low place','together in one place,','this child came','as the cause! — This','deed no one else','has done!']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['— To reform the town']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['Honey of delight!','My precious son!','Listen, da, to what','I am going to tell you! — Put','what is good into','your ears, da!']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['The worker who labours','in the factory! — The','farmer who gives you','rice!','The load-man who carries','the sack! — These','three are our comrades!']},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-008','lines':['— Honey of delight']}
]
}

DIALOGUE_OCCURRENCE_LINKS = {
    (60, 'vandikkaran-magan-s060-d001'): 'vandikkaran-magan-perf-008',
    (60, 'vandikkaran-magan-s060-d002'): 'vandikkaran-magan-perf-008'
}
