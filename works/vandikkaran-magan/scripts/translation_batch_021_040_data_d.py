#!/usr/bin/env python3
DIALOGUE_TRANSLATIONS = {
36: [
"Ah! So the suspicion is cleared up! Then Vingan belongs to an ordinary family?.. He is not a son of a great household? Amma! Are you really telling the truth?",
"What more do you want—should I slap my hand and swear it to you?... Should I light camphor and put it out at the Kaliamman temple? If he were a boy from a high-status family... could he mix so naturally in Sadaiyan's house?... Would he feel like eating old rice?...",
"Then... Uma will give him to me. Her ideal... is a bridegroom whose status is no lower than hers, isn't it!..",
"Amma, what you said is really true!...",
"Tell Uma and...?",
"With her help itself I am going to arrange for the Vingan–Kokila marriage to take place!...",
"Kokila!",
"Ayyo!... Don't stop me, Amma!... I can't contain my happiness, Amma... I feel as though I'm walking upside down... I'm going, Amma!..."
],
37: [
"Uma! Uma!... I've found out the truth!... In the heads-or-flower toss, heads falling was wrong!... The flower side falling is what was correct!... You have given him to me!....",
"Uma!... What is wrong with your body?... Why are you vomiting?.. What did you eat?...",
"Kokila!... In my haste, forgetting even myself, I drank nectar!.. It has turned into poison for me, dear!....",
"What are you saying?... I don't understand anything!..",
"If I don't tell you the truth, whom else am I going to tell!...",
"Tell me, Uma!",
"When I went to see the estate.. somehow... that Vingan too... came there... Until then I had thought manliness was only a sign of courage and valour!... But in the adventure performed by his manliness, the firmness of my womanhood shattered beyond recognition, Kokila!... shattered beyond recognition!.."
],
38: [
"Oh dear, Uma.. did your forehead get scratched?... Where?...",
"(sadly) The pigeon scratched only my forehead!... But you have scratched right into my heart!...",
"That is only a small wound! Hasn't it healed yet? Our literature says that women have a special pleasure in looking again and again at such wounds and nursing a silent hurt!..",
"The result of that pleasure has driven me to the very edge of suffering!..",
"What are you saying?...",
"The mistake the two of us made..",
"There was no mistake... You were the ember!.. I was the wax!...",
"I wasn't any ember!..",
"All right.. I was the ember!.. You were the wax!..",
"(angrily and emotionally) It is because I was wax that I melted away!..",
"You melted that very day; why are you melting again now!..",
"I have not merely melted away; I am standing here carrying a life too!..",
"(normally) Uma!",
"I am pregnant.",
"Pregnant!..",
"Bravo!..."
],
39: [
"(indicating the mother and father) These are the bridegroom's mother and father!.. The bridegroom is a very suitable match for your daughter Uma! His education is I.C.S.; his post is Collector!..",
"Krishnapuram estate... Chandragiri estate... people keep coming from all those places asking for Uma's hand! I can become related only to a zamindar family like that; don't bring me collectors, tahsildars, mirasdars, mittadars and whoever else! This is the first and last time for you...",
"I'll take leave!..",
"Hmm!.....",
"Yes! What you said is one hundred percent right!... A bridegroom has come for the estate family with mansions and towers!...",
"(agitated) What? What are you saying?",
"Secretary Vingan... your future son-in-law!..",
"(slapping Kokila on the cheek) Shut your mouth! Because you failed in trying to cast your net for Vingan, are you making up a story like this to put the blame on him and have him driven away?...",
"I'm not trying to make up a story! I want to see Vingan tie the thaali around Uma's neck!..",
"Don't stand here.. go! Go away!..",
"Appa! Don't do anything to her!... She is only telling you what happened!..",
"No! She is saying what cannot happen; she is saying what must not happen!",
"(falling at his feet) Appa! Only Vingan can become my husband.. No one can stop that!..",
"What did you say?... A discarded leaf-plate sticking to the finial of a temple tower?",
"I am the discarded food now!.. I belong only to him!..",
"It will not happen even in a dream!...",
"Your family prestige will not prevail!.. I am pregnant now, Appa!...",
"Uma!..",
"Appa!.. Forgive me!.. Please marry me to him!..",
"(confused) Ayyo!.. Uma.. Uma.. You have made the honour of the zamindar family a laughing-stock in the street, child!.. Is sandalwood to be dissolved in rosewater? (Or dissolved and sprinkled in sewer water?)...",
"Zamindar ayya!.. This is not the old age!.. Fifteen years ago, a man could give an innocent woman a child and she might shrink away, unable to tell the town whose child it was. What has happened now is an entirely new story!.. A story about the chastity of a famous zamindar family! To hide this from the town and protect your honour from damage, there is only one path—the Vingan–Uma marriage!..",
"(in anguish) Do you say so too?.. We don't even know who that Vingan is?..",
"Whoever he is, what does it matter?.. From now on he is your son-in-law!..",
"(falling at his feet and holding his legs) Yes, Appa! Forgive me, Appa..",
"All right, child! Let it happen as it is written on your head!.."
],
40: [
"Kokila!.. I had built castles in my heart about seeing you in bridal dress...",
"Even if you don't see your daughter in bridal dress...? You are going to see your student... my dearest friend Uma in it, aren't you, Amma!...",
"Kokila!",
"Amma!!"
]
}

DIALOGUE_NOTES = {
(38,3): ['The source invokes a literary commonplace about repeatedly contemplating wounds and an `ஊமைப் புண்` (silent/hidden hurt); English stays close to that figurative sense.'],
(39,14): ['The source uses the caste/status image `எச்சில் இலை கோபுரத்துக் கலசத்தில் ஒட்டிக்கொள்வதா?`; English preserves the discarded-leaf/temple-finial metaphor without softening its contempt.'],
(39,15): ['The source continues the degrading `எச்சில்` metaphor with `எச்சில் பண்டம்`; English preserves the image rather than normalizing it.'],
(39,20): ['The parenthetical contrast between rosewater and sewer water is preserved as printed; the source sentence itself is rhetorically irregular.']
}

ND = {
36: [
{'text':'Kokila’s room.','locator_kind':'location-caption'},
{'text':'(She opens the desk drawer, takes out the coin and tosses it heads-or-flower. The “flower” side falls...)'},
{'kind':'source-unlabelled','text':'I will go right now.. tell Uma this news and..'},
{'text':'(Kokila runs out, tossing the coin in her hand and catching it.)'}
],
37: [
{'text':'Uma’s room.','locator_kind':'location-caption'},
{'text':'(Kokila comes in joyfully, tossing the coin in her hand and catching it.)'},
{'text':'(Before Kokila can finish speaking, she sees Uma vomiting into the washbasin and is shocked...)'},
{'text':'(Kokila is stunned. The coin in her hand falls and rolls, coming to rest with the head side showing.)'}
],
38: [
{'text':'Garden pond.','locator_kind':'location-caption'},
{'text':'(Vingan catches one of the pigeons, brings it close to his face and admires it—then tosses it up and lets it fly. Carried by the force of the throw, the flying pigeon scratches with its claw the forehead of Uma, who is arriving wearing cooling glasses. She pushes the pigeon away and feels her forehead.)'},
{'text':'(He examines her forehead, holding her face in both hands.)'},
{'text':'(He laughs—a great laugh, a laugh of victory. At the sound, pigeons, birds and ducks flap noisily and scatter. The sound of his laughter and the noise of the scattering birds mingle together. Kokila watches all this from hiding.)'},
{'text':'(Interval.)','locator_kind':'structural-caption'}
],
39: [
{'text':'Estate palace.','locator_kind':'location-caption'},
{'text':"(The marriage broker and the prospective bridegroom's family are present; the zamindar sits bristling with severity.)"},
{'text':'(They leave. The zamindar turns; Kokila enters.)'},
{'kind':'source-unlabelled','text':'Did you hear, Kokila... Some Collector’s family, it seems, came asking for Uma’s hand—a Collector! I spoke firmly and sent them away.. I told them that only from an estate family with mansions and towers could a bridegroom come for her! What, was I right?...'},
{'text':'(He grabs her by the hair and pushes her away; at that moment Uma runs in...)'},
{'text':'(Maragatham enters.)'}
],
40: [
{'text':'Kokila’s room.','locator_kind':'location-caption'},
{'text':'(Kokila comes running in tears; Maragatham enters.)'},
{'text':'(Both embrace each other with tears in their eyes.)'}
]
}
