#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import json, re

W = Path(__file__).resolve().parents[1]
T = W / 'translations'
R = T / 'records'
D = W / 'dialogues' / 'records'
S = W / 'scenes'
P = W / 'transcription' / 'pages'
N = W / 'notes'
R.mkdir(parents=True, exist_ok=True)

NEXT = (
    'Translate and verify archive scene ordinals 21–35 as the next 15-scene English batch. '
    'Preserve source order and exact Tamil label/provenance metadata; link reconciled immutable dialogue IDs exactly once; '
    'keep source-unlabelled speech unassigned; link only verified song/performance occurrences; preserve unresolved item-level '
    'authorship as unresolved; and do not modify closed Tamil, scene, dialogue-record, character-mapping or song-record authorities.'
)
BATCH_SIZE = 15
TARGET_SCENES = list(range(6, 21))
EXPECTED_SOURCE_SCENE_IDS = ['5','6','7','8','9','10','10-எ','11','12','13','14','14-எ','15','16','16-எ']

# Closed upstream authority.
didx = json.loads((W / 'dialogues' / 'index.json').read_text(encoding='utf-8'))
cidx = json.loads((W / 'characters' / 'index.json').read_text(encoding='utf-8'))
songidx = json.loads((W / 'songs' / 'index.json').read_text(encoding='utf-8'))
assert didx['status'] == 'complete-verified-reconciled' and didx['dialogue_record_count'] == 773
assert cidx['status'] == 'complete-verified' and cidx['dialogue_record_coverage'] == '773/773'
assert songidx['status'] == 'complete-verified-source-only' and songidx['mapped_source_visible_occurrences'] == 9

scene_index_obj = json.loads((S / 'index.json').read_text(encoding='utf-8'))
if isinstance(scene_index_obj, list):
    scene_rows = scene_index_obj
else:
    scene_rows = next(v for v in scene_index_obj.values() if isinstance(v, list) and v and isinstance(v[0], dict) and 'ordinal' in v[0])
scene_meta = {int(x['ordinal']): x for x in scene_rows}
assert [scene_meta[n]['scene_id'] for n in TARGET_SCENES] == EXPECTED_SOURCE_SCENE_IDS

song_inventory = json.loads((W / 'songs' / 'inventory.json').read_text(encoding='utf-8'))
perf = {x['id']: x for x in song_inventory['records']}
assert perf['vandikkaran-magan-perf-001']['source_scene_id'] == '7'
assert perf['vandikkaran-magan-perf-002']['source_scene_id'] == '10'

DIALOGUE_TRANSLATIONS = {
6: [
"Who are you? Who are you?",
"Who I am can wait... If I hadn’t come and hidden here just now, you’d have fallen down and been smashed to pieces!..",
"Oh... I see!.. I was going to the bathroom, boy!...",
"Saying you were going to the bathroom, you’d have gone straight to heaven!.. This is the door for getting down, sir... the door!...",
"(laughing) Good boy!.. Very good boy!... What’s your name, little brother?..",
"Sokkalingam!..",
"Good!... Good!... Boy! How did you come here?",
"I ran away from the town where I was born!..?",
"Don’t you have a father or mother? Are you an orphan?...",
"I’m not an orphan, sir... How I ran away and hid here is a big story, sir!...",
"Oh...! Hmm.... Tell me, tell me!....",
"I’d sit in Appa’s lap!.. Amma would feed me rice!.."
],
7: [
"They say you give our zamindar’s daughter badam halwa every day... One day, bring one home and give it to our boy, won’t you!....",
"I want it, Amma, I want it! We get this old rice every day... badam halwa will come only for one day...",
"Sornam!.. Did you hear our boy talk?",
"Even when a little child speaks, it’s talk that makes you think!... For workers like us, old rice itself is badam halwa, panchamirtham, everything—isn’t it?....",
"Why say that!... If I say one word to zamindar-ayya that our boy wants badam halwa, he’ll send the whole tray of badam halwa just like that!....",
"Amma!... Appa!... I’m going to play!",
"All right, dear. Play and come back quickly... wash your hands and feet... then study, child...",
"All right, Amma!... (He gives her a kiss and runs off.)",
"(to Sadaiyan, putting away the meal things) Listen!... I too will go to the horse stable, sweep and clean it, and come back..."
],
8: [
"Hey, what shall we play today?",
"Blindman’s buff!...",
"No blindman’s buff—wedding game.",
"Then who’s the girl?... Who’s the bridegroom...?",
"You’re the girl!...",
"I won’t... Look, Uma looks like a bride!...",
"Then all right... Uma is the bride! — Sokkalingam is the groom!..",
"I won’t, da... (As he runs, one boy chases him.)",
"No! No!... You are the groom!...",
"You donkey born to that coachman fellow!... You’re going to tie a thaali around the daughter of Zamindar Jambuling Bhoopathi?...",
"Don’t come this side again! Don’t! Don’t!... (He beats him; keeps beating him...)",
"Amma! Amma!",
"Master! Master! Don’t beat him!... Master, don’t beat him!...",
"So what if I break his hand? (He twists Sokku’s arm. The boy screams.)",
"Ayyo! Let him go, master!... Don’t kill him!... The children did something for fun, as part of their game... and you... are taking it as something terrible...",
"A game? Ha!... Ha!... Uma is the daughter of Zamindar Jambuling Bhoopathi. Even her shadow—if this vagrant fellow touches even that shadow in play... I’ll cut off all ten of his fingers and play ball with them!...",
"Master! I’m very surprised, master... Every day when you meet the public... you pick up poor children, cuddle and kiss them!... You talk equality!... You mix without caste difference!..",
"(angrily) What did you say, woman? What did you say?..",
"I’m asking whether there’s one zamindar in the middle of the crowd!... and another zamindar in the horse stable!",
"(throwing Sokkalingam aside)... Ask, woman. Ask!... (He grabs her hair and is about to slap her...)",
"Master!...",
"What did you say?... Whom did you call a drunkard! Me?... Me?... (Holding her by the hair, he keeps pushing her along...)",
"Amma! Amma!...",
"Sornam...! Sornam...!",
"(covering himself) Ayyo, Sornam! You went that way!.. That’s a vicious bull!.. Who brought it and tied it in the horse stable?.. Sornam!.. Sornam!!",
"Appa! It was this zamindar who killed Amma!",
"Oh God—Sadaiya! He’s lying... He’s blaming a man for what the bull did.",
"You’re not a man!.. You’re the bull!..",
"(restraining him) You sinful brat!... Are you accusing our master?..",
"Sadaiya! This is what they mean by ‘blame in one place, sin in another’!...",
"He is like our god! If you say anything about him, your tongue will rot away!..",
"No, Appa... no!—He’s the one who killed my mother!... We mustn’t let him go!...",
"Hmm... Catch him!... Catch him!..."
],
9: [
"(The boy has tears in his eyes. Wiping them with his fingers...) My boy!.. Don’t worry!.. God himself has brought you and placed you with me.... From now on you can stay with me.... It is my responsibility to raise you and make a man of you! Is that all right?... Hmm... nod your head to say yes...",
"Very good!.. Hmm... Boy! What did you say your name was?...",
"Sokkalingam!..",
"Sukku Lingam!...",
"Uh-uh!.. Sokka... Lingam!...",
"Why the trouble... From now on I’ll simply call you Lingan!..."
],
10: [
"(to one of the women) Vanitha! (peering into the mirror) Look, two white hairs are showing here... blacken these too!...",
"You’re the zamindar of this whole town—what does it matter how you look?...",
"Leena!.. You understand nothing!.. Charm in one’s appearance—and a special skill in preaching to the town—those two are my capital!.. Shouldn’t I pay special attention to them?...",
"You’re a great man!...",
"(noticing the receiver in Leena’s hand) Leena!.. Why are you still holding the receiver in your hand...",
"Oh! I forgot!... When I look at your Cupid-like face, I forget everything!... Yes... who called?...",
"That... a white millionaire named David Durai! He said he’s sending a man called Lingan to work for me as secretary.. Nice name, isn’t it—Lingan...!",
"Good... I’m going to tell you some news too—it’ll be good for you as well!...",
"What is it, Leena?...",
"(shyly, coyly) I... now... haven’t had my period for two months!..",
"What, pregnant?... (cunningly) Leena, is there anyone outside—someone close to you—who knows any secret about me or about you?...",
"No! Apart from God, nobody knows anything!",
"If God knows, that’s all right!.. Leena... come closer!.."
],
11: [],
12: [
"(angrily) Hey! What’s wrong with you!",
"(flicking his turban) I’m perfectly fine!.. Can’t you tell by looking? You’re asking everyone walking down the street about their health... Are you a lady doctor?...",
"(even angrier) Huh?",
"Do all lady doctors make enquiries holding a whip like this?",
"Lady doctors who roam about crying for lack of patients ask like this, do they?",
"Enough of the mockery and teasing... First give me the whip!",
"Shall I give you the whip? Or shall I give you a whipping?",
"What did you say?",
"Little brother! Speak with a little respect! Whoever one may be, guard the tongue!..",
"Forget guarding the tongue—if you drive this fast, who will guard the lives of people on the street?",
"Who are you to ask that?",
"Who I am can’t be told in a single line!... If you give me a little room, I’ll sit down and explain it in detail!",
"Brother! Remember that you’re speaking to the young zamindarani of this estate!",
"Oh! The zamindarani? (astonished, to Maragatham) Who are you? Her daughter?",
"Daughter?... There you go!... Brother, are you trying to flatter me? I have a daughter as big as this myself! I’m the teacher for this little queen!",
"Oh-ho! Teacher madam! Don’t tell your student to drive the carriage so fast!.",
"I’ll drive even faster than this; who’s going to question me?",
"I’m questioning you now! Later the whole town will!",
"From now on, just watch—I’ll be terrible!...",
"Only from now on?.... Hmm!... Hmm!...."
],
13: [
"Appa! This town is getting worse and worse!... One fellow even talks back to me!...",
"(rising) What? Who is he?... Maragatham!... Who spoke to Uma like that?...",
"Some spirited young man!... Very mischievous!...",
"Hmm... the future zamindarani! He went and played mischief with the zamindarani? I’ll shoot him like a sparrow right now—my fingers are itching!... Give the order! Give the order!... Whoever he is, I’ll shoot him!... I won’t let him go!... Move.... Who is that? Move aside!...",
"Who?.... I’ve taken aim! Move over to that side!",
"David Durai has given me a letter for the zamindar!",
"Appa!... He... (She tries to say something—but does not.)",
"(looking at the letter) Oh!... So you’re Mr. Lingan?... David Durai telephoned! I already told him... from now on you are the secretary to this estate! This is Manager Kalingarayan...",
"Not just manager; all in all!...",
"Much Pleased to meet you!",
"(shaking Lingan’s hand) Mr. Lingan! May your arrival be auspicious!... Here... this is my daughter Uma!... That is, the future zamindarani... Uma...",
"Greetings.",
"(hesitantly) G...ree...tings!...",
"Here... this is...",
"Uma’s teacher madam... I know!... Greetings...",
"Greetings.",
"Uma!...",
"This is Kokila...",
"The teacher madam’s daughter!... Greetings.",
"Well, well!... You seem to know all this very well!...",
"Durai must have told him! A secretary suited to our estate!...",
"Kokila! Take Mr. Lingan around and show him our whole palace!...",
"(to Lingan) Will you come?..."
],
14: [
"Come! Come! Come! This is a tiger! Don’t think it’s a live tiger; it’s a dead tiger!... They say the people couldn’t bear the havoc this tiger caused, so they all ran to the zamindar and complained. At once the zamindar took his gun! Went to the forest!... Killed the tiger! Brought the head back and hung it here!...",
"This zamindar?...",
"You’re rushing before I finish—the father of this zamindar’s father, that is, his grandfather!... Here, a deer’s head!... The present zamindar is very clever at deer hunting!... Deer that run at a hundred miles an hour—our zamindar goes at a hundred and fifty miles an hour, hunts them down and fells them!... Come!",
"Oh!",
"This is my room.. (bringing him inside) This is the first time you’ve come to my room.. Here, have an apple!... (Lingan takes it.) A wonderful Kashmir apple!... You only know my name—Kokila! You saw my mother on the way with Uma!... The woman they introduced as Uma’s teacher—that Maragatham amma’s daughter is me! They say that as soon as I was born, my father quarrelled with Amma, boarded a ship and went abroad.. See what kind of time I was born at?... My birth star is Asvathi—Bharani—Karthigai—Rohini... there are twenty-seven stars, they say.. one of those!... And my lagna is... Mesham—Rishabam—Meenam—Kumbam—Simmam—Kadagam—Dhanusu—Viruchigam...",
"(taking a clip from the table) Enough!... Enough!... Amma... here, your lips, just a little... (puckering his own lips) hold them like this, let’s see...",
"How? Like this?",
"You keep talking on your own without letting me say even one word... Hmm!...",
"Why, don’t you like the way I talk?.. Can’t you enjoy it?...",
"No.. no.. You talk very entertainingly!... If they took you to places like Ajanta, Ellora and Mamallapuram and made you a ‘guide’... you’d explain things to the tourists there all day without taking a breath!... Now answer the question I’m asking!...",
"Ask!... Are you going to ask when this estate began? Who the first zamindar was?... his name?... and things like that?... For that, here—the whole history of this estate is in a book.. Take it! (She gives him a book.)",
"(taking the book casually) Have you started again?.. Here... the clip! I’ll put it on you!...",
"No! No!... My lip is already swollen.. If Amma asks why my lip is swollen, what am I supposed to say?... I’ll tell her it was the work of the new secretary!...",
"You really are a guileless girl!... (laughing) Yes, Kokila!... your young queen, Uma madam’s...",
"Madam?... She’s Miss Uma!... Hmm... These days even people who are forty or fifty still give themselves the title ‘Miss’!...",
"Yes—Miss Uma’s everyday pastime is driving the carriage faster than the wind, is it?...",
"That’s her evening pastime!... When she gets up in the morning...",
"She brushes her teeth!... drinks coffee!...",
"You forgot bathing!.. After bathing and getting dressed, she never goes without horse riding!",
"I see..! So she goes horse riding every morning?",
"Yes.. Here!... I can show you Uma’s riding horse from right here!.. (pulling aside the window curtain) There!.. See coachman Sadaiyan bathing it... That’s the horse!.."
],
15: [
"(running up to Vingan) Oh dear, dear!... It splashed you without my noticing... Please forgive me!",
"It’s all right!... It’s all right!..",
"Hey, fool! Sadaiya!... I told you to bathe the horse... and you bathe a man instead! Do you know who this man is?... The zamindar’s new secretary!.. Educated!.. Rich! Sorry, Mr. Vingan!.. Hey, Sadaiya!... Wipe Mr. Vingan’s boots clean!... Hmm... wipe them, da... dirty fellow!....",
"Ayyo... no!.. Look at your age and look at mine!.. You’re old enough to be my father—how can you do this work?...",
"What age, what nonsense... Every beggar comes here an old man. If we embrace every one of them crying ‘he’s my father’s age,’ what will become of us? This is why the country gets no rain and goes to ruin! Why talk so meaninglessly? We are all of the zamindar class. The zamindar is God’s representative! I am his representative!! All these are servant fellows! Are you of their caste?... Hey, Sadaiya! Why are you standing there listening to a sermon?... Wipe the boots, da! Don’t touch him—touch only the boots!",
"Right away, master...",
"No, ayya! Don’t!"
],
16: [
"Why are you drinking without opening your eyes, master! If you open your eyes a little, you can see the fish... chicken... and eat all this properly.",
"Fool!... When great sages do penance, do they open their eyes, da?",
"They don’t!",
"Do you know why?",
"Tell me!..",
"Only then does heaven appear, da!.. My lord Sokkalingam will grant me a vision!...",
"Ah, Secretary Vingan... come! come!... Kannaayiram, tell him about Sokkalingam—Secretary Vingan has come, da!... Pour for ayya!.. Whisky? Brandy? Gin? Rum?....",
"No! No!.. I’ve never even touched it with my hand!...",
"Don’t touch it!.. Just sit there with your mouth open!.. We’ll pour it in!..",
"But you’ve brought in a law saying nobody in your estate should drink!.. and you swallow it bottle after bottle!",
"The law is only for the poor! Not for those in authority. Understand? Hey Kannaayiram, you pour.",
"Ah! Ah... splendid!.. We’ve reached Indra’s heaven itself!.. Hmm!.. Urvashi, Rambha and Tilottama are all dancing!..",
"Mr. Manager!.. I’m leaving!..",
"You’re going?... Why?... Stay and watch Urvashi and Rambha dance.. Chi!.. Ah! Ayyo... They don’t even have clothes!.. Are they all dancing with just ribbons tied on them!..",
"You watch and enjoy it yourself!.. I have work to do!..",
"Hey... put it down, da!.. There’s an order that nobody in the estate should drink!... You servant dog, are you drinking?.. Are you getting secretly drunk, da?..",
"Why, da... I keep hitting you?... and you keep laughing!...",
"Nothing... I take one drop and get this much beating!... I was laughing thinking how much beating you’ll get for drinking so much!..",
"You talk back?... Donkey!... You talk back to me?.. From now on you won’t be able to laugh... you’re going to cry! I’ve dismissed you from your job. Go outside!... Get out!..",
"Thank you very much!.. I’m going...",
"Everyone who leaves curses me; this fellow alone leaves thanking me... Get lost!"
],
17: [],
18: [
"What, Manager ayya?.. Can’t you keep quiet at your age!...",
"If he cared about age, would Manmathan shoot his arrow?... Is age a barrier to love? We should both break that barrier and throw it away! What use is it when little boys fall in love these days?.. None at all. People like us are great geniuses!.. men of the old days... our love is something special!.. (He comes close and touches her.)",
"Sss!... Then I’ll be very dangerous!...",
"Dangerous is exactly what I want! Only then does it create the mood for me. If she’s innocent, she knows nothing.. like a dumb ox!",
"(angrily) Manager!...",
"(coaxingly) Teacher madam!...",
"(sternly) I’m only Uma’s teacher! Now I’m the teacher who is going to teach you the right lesson!...",
"A lesson... will you teach me? Teach me! Come... my bedroom is right nearby!.. Come; I’ll see what lesson this is that I haven’t studied until now!...",
"Manager! I’m telling you respectfully! Vacate this place immediately!—otherwise I’ll tell the zamindar!..",
"A flower shouldn’t be crushed just to smell it!... I’m a man with that kind of plan... A time will come!.. Then you’ll come and fall at my feet, begging for alms of love!... I won’t come the way everyone does..",
"How?",
"A different size! You’ll come straight, flop down and lie there!.. Then you’ll grab... my feet!.. You’ll beg, ‘Give me alms of love! Give me alms of love!’.. And I’ll say, ‘Get lost, woman!’ and stand there just like Viswamitra!",
"(laughing dismissively) You can’t even stand steadily in one place... and in this condition you’re guarding Appa!",
"Kannaayiram!.. There’s some mystery in the relationship between Maragatham amma and the zamindar, isn’t there!..",
"Is that all?... Come!... There are so many more secrets—I’ll tell you!..",
"All right... all right... come!"
],
19: [],
20: [
"Kokila! Shall we go ‘horse riding’ toward the lakeside today and come back?....",
"Oh!... As you wish!",
"Uma! Uma!::: (She screams.)",
"What? What?",
"Ayyo! Please save Uma!:::"
]
}

DIALOGUE_NOTES = {
    (18, 10): [
        'The ending of the verified Tamil source line is syntactically irregular (`எல்லோரும் வார் மாதிரி வரமாட்டே..`). '
        'The English renders the apparent sense conservatively without changing the Tamil authority.'
    ]
}

ND = {
6: [
{'text':'First-class railway compartment.','locator_kind':'location-caption'},
{'text':'(David Durai sits smoking a cigarette, drinking with a liquor bottle before him. Beneath the bench where he sits, the boy Sokkalingam is hiding, sweat pouring down his face. David pours himself another glass and drinks... Staggering, he gets up and tries to go to the train compartment’s “toilet”; losing his balance, he opens the train door and is about to put one foot out. At once Sokkalingam cries out, runs up, wraps an arm around his waist and stops him from falling.)'},
{'text':'(Flashback begins.)'}
],
7: [
{'text':'Sadaiyan’s house.','locator_kind':'location-caption'},
{'text':'(Sokkalingam sits beside Sadaiyan. Sadaiyan scoops rice from the plate before him and eats. Kneeling nearby with pots and vessels, Sornam feeds rice to Sokkalingam, who is sitting on Sadaiyan’s lap....)'}
],
8: [
{'text':'Horse stable.','locator_kind':'location-caption'},
{'text':'(Five or six children play noisily. Sokkalingam is among them. Amid the children in soiled clothes, little Uma comes in wearing clothes that gleam brightly and joins them. A poor little girl cries, “Hey! Uma has come! Uma has come!”...)'},
{'text':'Dum-dum! Peep-peep!...','kind':'performance-cue','occurrence_id':'vandikkaran-magan-perf-001'},
{'text':'(Saying so, they begin playing drums and pipes. They seat Uma and Sokkalingam on a plank and chant mantras..... They tie a groom’s turban on Sokkalingam’s head. They tie a small stone to a cord and tell him to fasten it around Uma’s neck. Just as he is about to tie the cord around Uma’s neck, the zamindar’s hand knocks his hand aside and snatches the cord away...)','kind':'performance-cue','occurrence_id':'vandikkaran-magan-perf-001'},
{'text':'(At his roar, all the children, including Uma, scatter and run. Only Sokkalingam remains caught in the zamindar’s hands...)'},
{'text':'(Sornam runs in, screaming.)'},
{'text':'(The zamindar hesitates and stands holding her hair... Sornam is startled...)'},
{'text':'Master!... Have you been drinking?.. You tell the town that drink destroys a household!.. Was it in that frenzy that you behaved like this?..','kind':'source-unlabelled'},
{'text':'(The zamindar’s mind speaks.)'},
{'text':'She has seen my true face!.. Now the whole town will know it! If she stays alive any longer?... No! No! Absolutely not!','kind':'source-unlabelled'},
{'text':'(The inner voice stops...)'},
{'text':'(As Sokkalingam runs up crying “Amma!” and tries to pull the zamindar away, the zamindar pushes her onto the bull there. The bull tosses her with its sharp horns. Sornam screams in agony. Sokkalingam thunders “Amma!” Sadaiyan comes running...)'},
{'text':'(He throws a stone—the stone strikes the zamindar on the head—and Sokkan runs.)'},
{'text':'(Seeing some workers arrive, Sokkalingam runs; the workers chase him.)'}
],
9: [
{'text':'First-class railway compartment.','locator_kind':'location-caption'},
{'text':'(The flashback ends.)'},
{'text':'(Even through his sadness, Sokkalingam smiles and nods.)'},
{'text':'(Lingan nods happily.)'},
{'text':'(Years roll by.)'}
],
10: [
{'text':'Private estate palace.','locator_kind':'location-caption'},
{'text':'(The zamindar is reclining. One woman holds a mirror before him... another is applying “dye” to his hair...)'},
{'text':'(She applies dye to those hairs... Leena speaks while still holding the telephone receiver instead of putting it down.)'},
{'text':'(He tells the other women to leave, and they go. After closing the door, he grips Leena by the throat, growling “pregnant, pregnant” as he turns her into a corpse.. Leena collapses lifeless.)'}
],
11: [
{'text':'(The grown-up Lingan enters singing.)','kind':'performance-cue','occurrence_id':'vandikkaran-magan-perf-002'},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-002','lines':[
'A drama is unfolding in the land! — of it',
'I have come to tell you in song! — Some men’s',
'stage where they act, and the disguises they wear,',
'are hidden from the townspeople’s eyes! — Ah;',
'the truth is understood by no one! — A drama...'
]},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-002','lines':[
'Power comes charging in! — beside it',
'march a thousand attendants! — This',
'course it is taking',
'is not right, and',
'I will show the town',
'the sign of it! — A drama...'
]},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-002','lines':[
'Like an upright man,',
'he gives advice! — that',
'outward guise like',
'the Buddha! — If you',
'lift away the cloak',
'worn by these impostors,',
'bullying; intimidation;',
'imprisonment! — A drama...'
]},
{'kind':'song','occurrence_id':'vandikkaran-magan-perf-002','lines':[
'The poor bathe',
'in tears! — while these',
'swindlers float',
'in rosewater! — How long',
'will these cowards’ valour',
'continue',
'to fly its flag',
'in the durbar? — A drama...'
]}
],
12: [
{'text':'(Just as Lingan’s idealistic song ends, the carriage driven by Uma comes racing toward him at great speed. Lingan snatches the whip from Uma’s hand.)','notes':['This is the source-visible end/context cue for `vandikkaran-magan-perf-002`; it is translated here without creating a second performance occurrence link.']},
{'text':'(She stretches out her hand to take the whip.)'},
{'text':'(He tosses the whip; Uma catches it in her hand, angrily.)'},
{'text':'(The carriage moves away...)'}
],
13: [
{'text':'Estate palace.','locator_kind':'location-caption'},
{'text':'(The zamindar and Kalingarayan are there.... Then Maragatham and Uma arrive.)'},
{'text':'(He lifts the rifle and extends it while taking aim. At that moment Lingan comes and stands at the muzzle of the rifle.)'},
{'text':'(They shake hands.)'},
{'text':'(The zamindar is surprised... Just then Kokila comes running, calling Uma, and stops nearby...)'}
],
14: [
{'text':'Various parts of the estate palace.','locator_kind':'location-caption'},
{'text':'(The tiger head, deer head and buffalo head mounted in the hall are shown...)'},
{'text':'Kokila’s room.','locator_kind':'location-caption'},
{'text':'(She puckers her lips; Lingan then fastens the clip in his hand onto her lips.)'},
{'text':'(Kokila pleads as if saying, “It hurts, take it off.” Lingan laughs and removes the clip.)'},
{'text':'(Rubbing her lip to ease the pain.)'},
{'text':'(Vingan watches Sadaiyan bathe the horse—sadness appears on Vingan’s face.)'}
],
15: [
{'text':'Horse stable.','locator_kind':'location-caption'},
{'text':'(Sadaiyan is bathing the horse... He looks somewhat older... Vingan comes along tossing the album Kokila gave him into the air and catching it again and again... As Vingan nears the horse, Sadaiyan, not noticing him, pours a bucket of water over the horse. The water splashes Vingan’s boots and the trouser legs above them. The boots and the front of the trousers become muddy with water.)'},
{'text':'(He says this pleading humbly.)'},
{'text':'(At that moment Kalingarayan comes in shouting...)'},
{'text':'(Sadaiyan takes his towel and is about to wipe Vingan’s boots.)'},
{'text':'(Ignoring Vingan’s attempts to stop him, Sadaiyan wipes Vingan’s boots...)'},
{'text':'(Vingan’s hands are held behind him; his emotion is made clear as the album in his hand is crushed and falls to the ground in pieces. Vingan’s eyes fill with tears. Sadaiyan finishes wiping the boots and stands up.)'}
],
16: [
{'text':'Kalingarayan’s room.','locator_kind':'location-caption'},
{'text':'(Kalingarayan drinks with his eyes closed. Kannaayiram serves pieces of meat such as chicken legs onto the plate before him.)'},
{'text':'(He finishes the entire glassful from the bottle and sets it down with a sharp thud.)'},
{'text':'[At that moment Vingan comes up the steps and stands there.]'},
{'text':'(He points to his own glass—Kannaayiram pours—Kalingan drinks with his eyes closed... At that moment Vingan takes a bottle of “rum” and hides it away....)'},
{'text':'(Vingan leaves.)'},
{'text':'(While they have been talking, Kannaayiram begins drinking what remains in the bottle.)'},
{'text':'(Saying this, he angrily beats him.. Kannaayiram laughs.. Kalingan strikes him again and Kannaayiram laughs. Kalingan grabs him by the hair and shakes him.)'},
{'text':'(Kannaayiram leaves... Kalingan staggers outside, muttering something.)'}
],
17: [
{'text':'Estate palace.','locator_kind':'location-caption'},
{'text':'Outside Kalingan’s room.','locator_kind':'location-caption'},
{'text':'(As Kannaayiram, having come out, goes toward a pillar—a hand stops him and pulls him back. Kannaayiram is shocked and bewildered—it is Vingan’s hand... Vingan gestures for Kannaayiram to remain silent and hides with him behind the pillar.'},
{'text':'Then Kalingan passes the pillar where they are hiding—there are several shots of Vingan following Kalingan—and Kannaayiram follows behind Vingan.)'}
],
18: [
{'text':'A part of the estate palace.','locator_kind':'location-caption'},
{'text':'(In the darkness, amid dim lamps, Maragatham sits reading a book in the middle of a somewhat brighter circle of light. Kalingan, staggering drunk, comes up behind her and covers her eyes... Startled, she knocks his hands away and rises.)'},
{'text':'(Putting his hand into a gesture like Viswamitra driving Menaka away in disgust, Kalingan loses his balance and falls.)'},
{'text':'(She leaves. All this time Vingan and Kannaayiram have been hidden, watching what happened.)'}
],
19: [
{'text':'Horse stable.','locator_kind':'location-caption'},
{'text':'(Morning. Sadaiyan saddles the horse, sets down water and goes to the other side. Vingan is hiding with a bottle of rum... Once Sadaiyan has gone, Vingan approaches the horse, takes the rum bottle from his bag, pours it into the water, throws the bottle there and leaves.)'}
],
20: [
{'text':'Exterior of the estate house.','locator_kind':'location-caption'},
{'text':'(Uma and Kokila arrive dressed for horse riding.)'},
{'text':'(Sadaiyan brings the horses, holding their reins.'},
{'text':'Uma mounts the horse that has consumed the rum...... Before Kokila can reach the horse she is to ride, Uma’s horse turns unruly and begins racing away wildly... Uma struggles, unable to control it.... The horse runs beyond her control....)'},
{'text':'Meanwhile Vingan runs up.'},
{'text':'(Vingan mounts Kokila’s horse and rides after her.)'}
]
}

assert set(DIALOGUE_TRANSLATIONS) == set(TARGET_SCENES)
assert set(ND) == set(TARGET_SCENES)
expected_counts = {n: int(didx['scene_record_counts'][f'vandikkaran-magan-s{n:03d}']) for n in TARGET_SCENES}
for n in TARGET_SCENES:
    assert len(DIALOGUE_TRANSLATIONS[n]) == expected_counts[n], (n, len(DIALOGUE_TRANSLATIONS[n]), expected_counts[n])
assert sum(expected_counts.values()) == 186


def norm(s: str) -> str:
    s = s.replace('\r\n', '\n').replace('\r', '\n')
    s = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)
    s = re.sub(r'^[#]+\s*', '', s, flags=re.M)
    s = s.replace('**', '')
    return re.sub(r'\s+', ' ', s).strip()


def source_blocks(n: int):
    text = (S / f'scene-{n:03d}.md').read_text(encoding='utf-8')
    parts = [b.strip() for b in re.split(r'\n[ \t]*\n', text) if b.strip()]
    out = []
    for b in parts:
        if b.startswith('<!-- derivative provenance:'):
            continue
        if b.startswith('## '):
            continue
        if b == '★':
            continue
        out.append(b)
    return out

page_cache = {}
def page_norm(p):
    if p not in page_cache:
        page_cache[p] = norm((P / f'{p:03d}.md').read_text(encoding='utf-8'))
    return page_cache[p]

fallbacks = []
def infer_pages(n, block, cursor_page):
    pages = list(scene_meta[n]['pdf_pages'])
    b = norm(block)
    exact = [p for p in pages if b and b in page_norm(p)]
    if exact:
        return [exact[0]], exact[0]
    # For a source block that crosses a page break, locate beginning and end independently.
    first = b[:80] if len(b) > 80 else b
    last = b[-80:] if len(b) > 80 else b
    first_hits = [p for p in pages if first and first in page_norm(p)]
    last_hits = [p for p in pages if last and last in page_norm(p)]
    if first_hits and last_hits:
        a, z = first_hits[0], last_hits[-1]
        span = [p for p in pages if a <= p <= z]
        return span, z
    # Conservative fallback is retained explicitly for QA; batch closure requires zero fallbacks.
    p = cursor_page if cursor_page in pages else pages[0]
    fallbacks.append({'scene_ordinal': n, 'block': b[:120], 'fallback_pdf_page': p})
    return [p], p


def page_prov(pages):
    return [{'pdf_page': int(p), 'printed_page': int(p)-1} for p in pages]


def match_dialogue(block, row):
    prefix = f"{row['speaker_label']}{row['source_delimiter']}"
    if not block.startswith(prefix):
        return False
    remainder = block[len(prefix):].strip()
    return norm(remainder) == norm(row['text'])


def make_dialogue_unit(n, sid, unit_no, row, english, notes):
    return {
        'id': f'vandikkaran-magan-en-s{n:03d}-u{unit_no:03d}',
        'kind': 'dialogue', 'status': 'verified', 'target_language': 'en',
        'scene_id': f'vandikkaran-magan-s{n:03d}', 'scene_ordinal': n, 'source_scene_id': sid,
        'source': {
            'source_path': f'works/vandikkaran-magan/dialogues/records/scene-{n:03d}.json',
            'canonical_scene_path': f'works/vandikkaran-magan/scenes/scene-{n:03d}.md',
            'source_record_id': row['id'], 'source_occurrence_id': None, 'source_locator': None,
            'speaker_label': row['speaker_label'], 'speaker_label_origin': 'source-explicit',
            'source_delimiter': row['source_delimiter'], 'page_provenance': row['page_provenance']
        },
        'translation': {'english_text': english, 'mode': 'prose-faithful', 'notes': notes}
    }


def make_nd_unit(n, sid, unit_no, block, spec, locator_no, pages):
    skind = spec.get('kind', 'stage')
    occurrence_id = spec.get('occurrence_id')
    locator_kind = spec.get('locator_kind') or ('source-unlabelled-speech' if skind == 'source-unlabelled' else ('song-body' if skind == 'song' else ('performance-cue' if skind == 'performance-cue' else 'stage-direction')))
    notes = list(spec.get('notes', []))
    if occurrence_id:
        occ = perf[occurrence_id]
        if occ['authorship_status'] == 'unresolved-item-level':
            notes.append('Item-level lyric authorship remains unresolved; the film-level `பாடல்கள்: கவிஞர் வாலி` credit is not promoted to this occurrence.')
        elif occ['authorship_status'] == 'not-applicable-non-lyric-performance':
            notes.append('Linked source occurrence is non-lyric performance material; lyric authorship is not applicable.')
    if skind == 'source-unlabelled':
        notes.append('The source prints no speaker label for this spoken unit; no speaker or immutable dialogue ID is inferred.')
    source = {
        'source_path': f'works/vandikkaran-magan/scenes/scene-{n:03d}.md',
        'canonical_scene_path': f'works/vandikkaran-magan/scenes/scene-{n:03d}.md',
        'source_record_id': None, 'source_occurrence_id': occurrence_id,
        'source_locator': {'kind': locator_kind, 'ordinal': locator_no, 'description': f'Source block {locator_no}: {norm(block)[:140]}'},
        'speaker_label': None,
        'speaker_label_origin': 'source-unlabelled' if skind == 'source-unlabelled' else None,
        'source_delimiter': None,
        'page_provenance': page_prov(pages)
    }
    kind = 'dialogue' if skind == 'source-unlabelled' else ('song' if skind == 'song' else ('performance-cue' if skind == 'performance-cue' else 'stage-direction'))
    tr = {'mode': 'semantic-poetic-source-faithful' if skind == 'song' else 'prose-faithful', 'notes': notes}
    if skind == 'song':
        lines = spec['lines']
        source_line_count = len([x for x in block.splitlines() if x.strip()])
        assert len(lines) == source_line_count, (n, locator_no, len(lines), source_line_count, block)
        tr['english_lines'] = lines
    else:
        tr['english_text'] = spec['text']
    return {
        'id': f'vandikkaran-magan-en-s{n:03d}-u{unit_no:03d}',
        'kind': kind, 'status': 'verified', 'target_language': 'en',
        'scene_id': f'vandikkaran-magan-s{n:03d}', 'scene_ordinal': n, 'source_scene_id': sid,
        'source': source, 'translation': tr
    }

new_scene_objects = []
for n in TARGET_SCENES:
    sid = scene_meta[n]['scene_id']
    rows = json.loads((D / f'scene-{n:03d}.json').read_text(encoding='utf-8'))
    blocks = source_blocks(n)
    dtrs = DIALOGUE_TRANSLATIONS[n]
    nds = ND[n]
    ri = di = ni = 0
    cursor = int(scene_meta[n]['pdf_pages'][0])
    units = []
    locator_no = 0
    for block in blocks:
        if ri < len(rows) and match_dialogue(block, rows[ri]):
            row = rows[ri]
            notes = list(DIALOGUE_NOTES.get((n, di+1), []))
            units.append(make_dialogue_unit(n, sid, len(units)+1, row, dtrs[di], notes))
            for pp in row['page_provenance']:
                cursor = max(cursor, int(pp['pdf_page']))
            ri += 1; di += 1
            continue
        if ni >= len(nds):
            raise AssertionError(f'scene {n}: no non-dialogue translation spec left for source block: {block}')
        spec = nds[ni]
        locator_no += 1
        if spec.get('occurrence_id'):
            pages = list(perf[spec['occurrence_id']]['source_pdf_pages'])
            cursor = max(cursor, max(pages))
        else:
            pages, cursor = infer_pages(n, block, cursor)
        units.append(make_nd_unit(n, sid, len(units)+1, block, spec, locator_no, pages))
        ni += 1
    assert ri == len(rows), (n, 'dialogue records unconsumed', ri, len(rows), rows[ri]['id'] if ri < len(rows) else None)
    assert di == len(dtrs), (n, 'dialogue translations unconsumed', di, len(dtrs))
    assert ni == len(nds), (n, 'non-dialogue specs unconsumed', ni, len(nds))
    obj = {
        'work_id':'vandikkaran-magan','target_language':'en','scene_id':f'vandikkaran-magan-s{n:03d}',
        'scene_ordinal':n,'source_scene_id':sid,'scene_status':'verified','unit_count':len(units),'units':units
    }
    (R / f'scene-{n:03d}.json').write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    new_scene_objects.append(obj)

assert not fallbacks, json.dumps(fallbacks, ensure_ascii=False, indent=2)

# Batch QA.
new_units = [u for s in new_scene_objects for u in s['units']]
new_links = [u['source']['source_record_id'] for u in new_units if u['source']['source_record_id']]
new_unlabelled = [u for u in new_units if u['source']['speaker_label_origin'] == 'source-unlabelled']
new_perf_ids = sorted({u['source']['source_occurrence_id'] for u in new_units if u['source']['source_occurrence_id']})
assert len(new_links) == 186 and len(set(new_links)) == 186
assert len(new_unlabelled) == 2
assert new_perf_ids == ['vandikkaran-magan-perf-001','vandikkaran-magan-perf-002']
new_counts = Counter(u['kind'] for u in new_units)
qa = {
    'work_id':'vandikkaran-magan','phase':'english-translation-batch-006-020','status':'PASS',
    'batch_size_scenes':15,'scene_ordinals':TARGET_SCENES,'source_scene_ids':EXPECTED_SOURCE_SCENE_IDS,
    'verified_scenes':15,'verified_units':len(new_units),'unit_kind_counts':dict(sorted(new_counts.items())),
    'immutable_dialogue_records_expected':186,'immutable_dialogue_records_linked':186,
    'source_unlabelled_spoken_units':2,'inferred_speaker_assignments':0,
    'performance_occurrence_ids_linked':new_perf_ids,'unique_performance_occurrence_links':2,
    'source_page_provenance_fallbacks':0,
    'checks': {
        'all_15_target_scenes_present_in_source_order': True,
        'all_batch_immutable_dialogue_records_linked_exactly_once': True,
        'source_unlabelled_speech_kept_unassigned_and_unlinked': True,
        'scene_7_mock_wedding_performance_linked_to_verified_perf_001_only': True,
        'scene_10_idealistic_song_linked_to_verified_perf_002_only': True,
        'scene_10_song_lineation_mapped_one_english_line_per_visible_tamil_line': True,
        'item_level_song_authorship_left_unresolved_for_perf_002': True,
        'structural_star_translated_as_prose': False,
        'synthetic_scene_end_prose_added': False,
        'closed_tamil_scene_dialogue_character_song_records_modified_by_translation': False
    },
    'next_activity': NEXT
}
(T / 'batch-006-020-qa.json').write_text(json.dumps(qa, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

(T / 'BATCH_006_020_REVIEW.md').write_text(f'''# வண்டிக்காரன் மகன் — English scenes 6–20 review

Status: **PASS / VERIFIED**

This iteration follows the work-specific **15-scene English batch** rule requested by the user.

- archive scene ordinals: **6–20 / 15 scenes**;
- source scene IDs: `{', '.join(EXPECTED_SOURCE_SCENE_IDS)}`;
- verified translation units: **{len(new_units)}**;
- immutable dialogue records linked: **186/186 exactly once**;
- source-unlabelled spoken units: **2**, retained without speaker inference;
- verified performance occurrences linked: **2 unique IDs** — `vandikkaran-magan-perf-001` and `vandikkaran-magan-perf-002`;
- item-level authorship of the source-scene-10 song remains **unresolved-item-level**;
- page-provenance fallback assignments: **0**;
- upstream canonical Tamil / scene text / immutable dialogue records / character mappings / song records rewritten: **0**.

Scene 7’s children’s mock-wedding music/mantra activity is translated only from the source-visible cue and remains non-lyric. Source scene 10’s complete printed song is translated in source stanza/line order and linked to its already-verified performance occurrence; the film-level `பாடல்கள்: கவிஞர் வாலி` credit is not promoted to item-level authorship.

**Next:** {NEXT}
''', encoding='utf-8')

# Rebuild cumulative translation index through scene 20.
all_scene_objs = []
for n in range(1, 21):
    p = R / f'scene-{n:03d}.json'
    assert p.exists(), p
    obj = json.loads(p.read_text(encoding='utf-8'))
    assert obj['scene_status'] == 'verified' and obj['scene_ordinal'] == n
    all_scene_objs.append(obj)
all_units = [u for s in all_scene_objs for u in s['units']]
all_counts = Counter(u['kind'] for u in all_units)
all_links = [u['source']['source_record_id'] for u in all_units if u['source']['source_record_id']]
all_unlabelled = [u for u in all_units if u['source']['speaker_label_origin'] == 'source-unlabelled']
all_perf_units = [u for u in all_units if u['source']['source_occurrence_id']]
all_perf_ids = sorted({u['source']['source_occurrence_id'] for u in all_perf_units})
assert len(all_links) == len(set(all_links))
assert len(all_links) == 65 + 186 == 251
assert len(all_unlabelled) == 4
assert all_perf_ids == ['vandikkaran-magan-perf-001','vandikkaran-magan-perf-002']
cross_page_units = sum(1 for u in all_units if len(u['source']['page_provenance']) > 1)
idx = {
    'work_id':'vandikkaran-magan','target_language':'en','status':'verified-through-scene-020',
    'total_scene_derivatives':72,'verified_scenes':20,'verified_scene_ordinals':list(range(1,21)),
    'verified_source_scene_ids':[scene_meta[n]['scene_id'] for n in range(1,21)],
    'translation_units':len(all_units),'unit_kind_counts':dict(sorted(all_counts.items())),
    'immutable_dialogue_records_linked':len(all_links),'source_unlabelled_spoken_units':len(all_unlabelled),
    'performance_linked_units':len(all_perf_units),'performance_occurrence_links':len(all_perf_ids),
    'performance_occurrence_ids_linked':all_perf_ids,'cross_page_units':cross_page_units,
    'batch_size_scenes':15,'schema':'schema.json','records_directory':'records/','pilot_qa':'pilot-qa.json',
    'latest_batch_qa':'batch-006-020-qa.json','latest_batch_review':'BATCH_006_020_REVIEW.md',
    'next_activity':NEXT
}
(T / 'index.json').write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

T_README = f'''# வண்டிக்காரன் மகன் — English translation

**Status:** **VERIFIED THROUGH ARCHIVE SCENE 020 / QA PASS**

- verified scenes: **20/72**;
- verified archive scene ordinals: **1–20**;
- cumulative translation units: **{len(all_units)}**;
- unit kinds: **{', '.join(f'{k}={v}' for k,v in sorted(all_counts.items()))}**;
- immutable dialogue links: **{len(all_links)}**;
- source-unlabelled spoken units: **{len(all_unlabelled)}**, with **0 inferred speakers**;
- unique song/performance occurrence links: **{len(all_perf_ids)}** — `{', '.join(all_perf_ids)}`;
- current production batch size: **15 scenes per iteration**;
- latest batch: **archive scenes 6–20 / PASS / 186 of 186 immutable dialogue records linked exactly once**;
- upstream source-layer mutations caused by translation: **0**.

See `batch-006-020-qa.json`, `BATCH_006_020_REVIEW.md`, `records/scene-006.json` through `records/scene-020.json`, and `index.json`.

## Next

{NEXT}
'''
(T / 'README.md').write_text(T_README, encoding='utf-8')

# Synchronize active layer next-activity pointers without rewriting immutable records.
def update_json_pointer(rel, key, value, extra=None):
    p = W / rel
    if not p.exists(): return
    obj = json.loads(p.read_text(encoding='utf-8'))
    obj[key] = value
    if extra:
        obj.update(extra)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

update_json_pointer('dialogues/index.json','next_action',NEXT)
update_json_pointer('characters/index.json','next_activity',NEXT)
update_json_pointer('songs/index.json','next_activity',NEXT, {'english_translation_gate':'in-progress-verified-through-scene-020'})
update_json_pointer('notes/character-index-qa.json','next_activity',NEXT)
update_json_pointer('notes/song-performance-qa.json','next_activity',NEXT)
if (N/'dialogue-index-qa.json').exists():
    dq = json.loads((N/'dialogue-index-qa.json').read_text(encoding='utf-8'))
    if 'next_activity' in dq: dq['next_activity'] = NEXT
    if 'next_action' in dq: dq['next_action'] = NEXT
    (N/'dialogue-index-qa.json').write_text(json.dumps(dq,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Work metadata: replace the active English block only.
mp = W / 'metadata.yaml'
m = mp.read_text(encoding='utf-8')
english_block = f'''  english_translation: verified-through-scene-020
  english_translation_index_path: works/vandikkaran-magan/translations/index.json
  english_translation_verified_scenes: 20
  english_translation_batch_size_scenes: 15
  english_translation_units: {len(all_units)}
  english_translation_unit_kind_counts: {','.join(f'{k}={v}' for k,v in sorted(all_counts.items()))}
  english_translation_immutable_dialogue_links: {len(all_links)}
  english_translation_source_unlabelled_spoken_units: {len(all_unlabelled)}
  english_translation_performance_occurrence_links: {len(all_perf_ids)}
  english_translation_latest_batch_qa_path: works/vandikkaran-magan/translations/batch-006-020-qa.json
  english_translation_latest_batch_review_path: works/vandikkaran-magan/translations/BATCH_006_020_REVIEW.md
'''
m, nsub = re.subn(r'  english_translation:.*?\n  reader_export:', english_block + '  reader_export:', m, count=1, flags=re.S)
assert nsub == 1
m, nsub = re.subn(r'^next_action: .*$', 'next_action: ' + json.dumps(NEXT, ensure_ascii=False), m, count=1, flags=re.M)
assert nsub == 1
mp.write_text(m, encoding='utf-8')

# Work-local current-status mirrors.
(W/'README.md').write_text(f'''# வண்டிக்காரன் மகன்

Source-led archival workspace for the 1978 first-edition dialogue/screenplay booklet **`வண்டிக்காரன் மகன்`**.

## Source authority

Controlling source: `TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`**. The image-only scan is canonical authority.

## Current verified state

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 unresolved**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogue authority: **773 records / 38 exact labels / QA PASS** — **744/744 legacy IDs preserved + 29 append-only repairs**;
- character/entity index: **32 entities — 15 characters / 14 roles / 3 collectives / 38/38 labels / 773/773 records / QA PASS**;
- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS** — 6 bounded Tamil bodies + 3 cue-only;
- item-level lyric authorship: **0 source-attributed / 6 unresolved**; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only;
- English translation: **20/72 scenes VERIFIED / QA PASS — {len(all_units)} units / {len(all_links)} immutable dialogue links / {len(all_unlabelled)} source-unlabelled spoken units / {len(all_perf_ids)} verified performance occurrences linked / 0 inferred speakers**;
- English production cadence: **15 scenes per iteration**;
- reader/export / Reading Room: **BLOCKED pending English closure**.

## Exact next activity

> **{NEXT}**
''', encoding='utf-8')

(W/'PROJECT_HANDOVER.md').write_text(f'''# வண்டிக்காரன் மகன் — Project Handover

Repository: `pugazg/kalaignar-cinema-works`  
Branch: `main`  
Work: `works/vandikkaran-magan/`

**LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — **90 PDF pages / 26,391,039 bytes / SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253` / first edition 1978 / image-only**.

## Durable closed state

- canonical source: **87/87 COMPLETE-VERIFIED / 0 uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS — 82/82 screenplay pages / 0 gaps / 0 overlaps**;
- dialogue authority: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**; legacy IDs **744/744 preserved**, append-only repairs **29**, action-only exclusions **2**;
- character/entity: **32 entities / 38/38 labels / 773/773 dialogue records / QA PASS**;
- song/performance: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**; 6 bounded bodies / 3 cue-only / 0 source-attributed + 6 unresolved item-level lyric authorships;
- English scene 1 pilot: **PASS — 40 units / 31 immutable links / 1 source-unlabelled speech**;
- English scenes 2–5: **PASS — 48 units / 34 immutable links / 1 source-unlabelled speech**;
- English scenes 6–20: **PASS — {len(new_units)} units / 186 immutable links / 2 source-unlabelled spoken units / 2 verified performance occurrences linked**;
- cumulative English: **20/72 scenes / {len(all_units)} units / {len(all_links)} immutable links / {len(all_unlabelled)} source-unlabelled spoken units / 0 inferred speakers**;
- English batch policy: **15 scenes per iteration**;
- reader/export and Reading Room: **BLOCKED pending English closure**.

Do not reopen or rewrite closed Tamil, scene, immutable dialogue-record, character-mapping or song-record authorities without new direct contradictory source evidence. Historical 744 counts refer only to the preserved pre-reconciliation ID set.

## Exact next activity

> **{NEXT}**
''', encoding='utf-8')

(W/'NEXT_CHAT_PROMPT.md').write_text(f'''# Next Chat Prompt — வண்டிக்காரன் மகன் / English scenes 21–35

Continue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/vandikkaran-magan/`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` — 90 pages, 26,391,039 bytes, SHA-256 `03579030ad0a082062d907c1ac12cb4eb497a261836d676a8fa46cd5c0c86253`, first edition 1978, image-only.

## Durable state

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogues: **773 / 38 exact labels / QA PASS** — 744 legacy IDs preserved + 29 append-only repairs;
- characters/entities: **32 / 38/38 labels / 773/773 records / QA PASS**;
- song/performance: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- English translation: **20/72 scenes VERIFIED / QA PASS — {len(all_units)} units / {len(all_links)} immutable dialogue links / {len(all_unlabelled)} source-unlabelled spoken units / {len(all_perf_ids)} verified performance occurrences linked**;
- verified archive scene ordinals: **1–20**;
- latest English batch QA: `translations/batch-006-020-qa.json` — **PASS**;
- production batch size: **15 scenes per iteration**.

Do not reopen or rewrite closed canonical Tamil, scene derivatives, reconciled immutable dialogue records, character/entity mappings, or song/performance records without new direct contradictory source evidence.

## Translation rules

Follow `docs/CINEMA_WORKS_PROCESSING_GUIDE.md` Phase 13 and `docs/SONG_TRANSLATION_GUIDE.md` for verified performance material. Translate only verified source units. Preserve source order, PDF/printed provenance, exact Tamil speaker labels as metadata and immutable dialogue-ID linkage. Source-unlabelled speech remains unassigned. Keep stage directions, written text, songs/performance cues and source-unlabelled speech structurally distinct. Do not invent speakers, missing lyrics, item-level authorship, or synthetic scene-end prose.

## Exact next activity

> **{NEXT}**
''', encoding='utf-8')

(W/'transcription'/'README.md').write_text(f'''# வண்டிக்காரன் மகன் — canonical Tamil transcription

The rendered scan is the controlling source. The canonical source layer is closed.

## Closed checkpoint

- transcription scope: **PDF 4–90 / 87 pages**;
- first pass / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;
- final-pass corrections: **0**;
- unresolved glyph holds / open uncertainty markers: **0 / 0**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**.

## Downstream state

The reconciled immutable dialogue authority is **773 records / 38 exact source labels / QA PASS**, preserving all **744/744** legacy IDs and adding **29** append-only repaired IDs. Character/entity coverage is **773/773**; song/performance is **9/9** source-only QA PASS; English translation is verified through archive scene **20/72** at **{len(all_units)} units**. Canonical Tamil remains unchanged.

**Production cadence:** English translation proceeds in **15-scene iterations**.

**Next:** {NEXT}
''', encoding='utf-8')

# Tail replacements in active layer READMEs/mapping.
def replace_tail(rel, heading, body):
    p = W / rel
    s = p.read_text(encoding='utf-8')
    pattern = re.escape(heading) + r'.*$'
    s, n = re.subn(pattern, heading + '\n\n' + body.strip() + '\n', s, count=1, flags=re.S)
    if n == 0:
        s = s.rstrip() + '\n\n' + heading + '\n\n' + body.strip() + '\n'
    p.write_text(s, encoding='utf-8')

replace_tail('dialogues/README.md','## Next',f'English translation is verified through archive scene **20/72**. {NEXT}')
replace_tail('characters/README.md','## Next',f'English translation is verified through archive scene **20/72**. {NEXT}')
replace_tail('songs/README.md','## Next',f'English translation is verified through archive scene **20/72**. Item-level authorship states remain unchanged. {NEXT}')
replace_tail('scenes/README.md','## Downstream gate',f'''Scene-text derivatives remain **COMPLETE-VERIFIED**. Downstream dialogue authority is **773 records / COMPLETE-VERIFIED-RECONCILED / QA PASS**; character/entity coverage is **773/773 / QA PASS**; song/performance is **9/9 source-only QA PASS**; English translation is **20/72 VERIFIED / QA PASS** at **{len(all_units)} units**.

**Next:** {NEXT}''')
replace_tail('mapping.md','## Exact next activity',f'''English translation is now **20/72 VERIFIED / QA PASS** with a **15-scene iteration** cadence.

**{NEXT}**''')

# Source transcription index has a current next-action pointer; update only control metadata.
tip = W/'transcription'/'index.json'
ti = json.loads(tip.read_text(encoding='utf-8'))
ti['dialogue_index'] = 'complete-verified-reconciled'
ti['next_action'] = NEXT
tip.write_text(json.dumps(ti,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')

# data/works.json.
data_path = W.parents[1] / 'data' / 'works.json'
data = json.loads(data_path.read_text(encoding='utf-8'))
entry = next(x for x in data if x['id'] == 'vandikkaran-magan')
sd = entry['structured_derivatives']
sd.update({
    'dialogue_index':'complete-verified-reconciled','dialogue_records':773,
    'character_dialogue_record_coverage':'773/773',
    'english_translation':'verified-through-scene-020','translation_index_path':'works/vandikkaran-magan/translations/index.json',
    'translation_scenes_verified':20,'translation_units':len(all_units),'translation_verified_units':len(all_units),
    'translation_unit_kind_counts':dict(sorted(all_counts.items())),
    'translation_dialogue_source_records_linked':len(all_links),
    'translation_source_unlabelled_spoken_units':len(all_unlabelled),
    'translation_performance_occurrence_links':len(all_perf_ids),
    'translation_batch_size_scenes':15,
    'translation_latest_batch_qa_path':'works/vandikkaran-magan/translations/batch-006-020-qa.json',
    'next_structured_derivative':'english-translation-scenes-021-035'
})
entry['next_action'] = NEXT
data_path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Root README: replace only the active Vandikkaran Magan section.
root = W.parents[1] / 'README.md'
s = root.read_text(encoding='utf-8')
section = f'''## வண்டிக்காரன் மகன் status

`TVA_BOK_0062961_வண்டிக்காரன்_மகன்.pdf` is the current active cinema-work source.

- canonical Tamil: **87/87 COMPLETE-VERIFIED / 0 open uncertainties**;
- scenes: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogues: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 773/773 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance gate: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- item-level lyric authorship: **0 source-attributed / 6 unresolved**; PDF 88 `பாடல்கள்: கவிஞர் வாலி` remains film-level metadata only;
- English translation: **20/72 scenes VERIFIED / QA PASS — {len(all_units)} units / {len(all_links)} dialogue links / {len(all_unlabelled)} source-unlabelled spoken units / {len(all_perf_ids)} unique performance occurrence links**;
- English production cadence: **15 scenes per iteration**;
- reader/export and Reading Room: **gated downstream**.

**Next:** {NEXT}

'''
s, nsub = re.subn(r'## வண்டிக்காரன் மகன் status\n.*?(?=\n## நாம் status)', section.rstrip(), s, count=1, flags=re.S)
assert nsub == 1
root.write_text(s, encoding='utf-8')

# Master handover targeted current bullet/active-summary update.
hp = W.parents[1] / 'docs' / 'HANDOVER_KALAIGNAR_CINEMA_WORKS.md'
h = hp.read_text(encoding='utf-8')
line = f'- **Vandikkaran Magan / வண்டிக்காரன் மகன்** — canonical Tamil **87/87 COMPLETE-VERIFIED**; scenes **72/72 / boundary QA PASS**; dialogues **773 / 38 labels / QA PASS-RECONCILED**; characters **32 / 38/38 / 773/773 / QA PASS**; song/performance **9/9 source-only QA PASS**; English **20/72 VERIFIED / {len(all_units)} units / {len(all_links)} dialogue links / {len(all_perf_ids)} performance occurrences**; production batches **15 scenes each**.'
h, nsub = re.subn(r'^- \*\*Vandikkaran Magan / வண்டிக்காரன் மகன்\*\* — .*$', line, h, count=1, flags=re.M)
assert nsub == 1
h = re.sub(r'Ammayappan and Naam remain closed at their recorded checkpoints\. \*\*The current active production work is வண்டிக்காரன் மகன்:.*?\*\*',
           f'Ammayappan and Naam remain closed at their recorded checkpoints. **The current active production work is வண்டிக்காரன் மகன்: English translation is verified through archive scene 20/72 at {len(all_units)} units, with 15-scene production batches; source/Tamil, scene, reconciled dialogue, character and song/performance authorities remain closed.**', h, count=1)
hp.write_text(h, encoding='utf-8')

# Repository status audit: current row, result, dedicated Vandi checkpoint, conclusion.
sp = W.parents[1] / 'docs' / 'STATUS_CONSISTENCY_AUDIT.md'
s = sp.read_text(encoding='utf-8')
s = re.sub(r'\*\*PASS for the current repository-wide checkpoint\.\*\* Vandikkaran Magan.*?\n\n',
           f'**PASS for the current repository-wide checkpoint.** Vandikkaran Magan English translation is now **20/72 scenes VERIFIED / QA PASS** at **{len(all_units)} units / {len(all_links)} immutable dialogue links / {len(all_unlabelled)} source-unlabelled spoken units / {len(all_perf_ids)} unique verified performance occurrence links**. Translation production now proceeds in **15-scene iterations**. All closed Tamil/scene/dialogue/character/song authorities remain unchanged.\n\n', s, count=1, flags=re.S)
row = f'| Vandikkaran Magan / வண்டிக்காரன் மகன் | **87/87 canonical source pages complete-verified; 0 unresolved** | **72/72 scenes; 773 dialogues / 38 labels; 32 entities; song/performance 9/9 QA PASS** | **20/72 VERIFIED / {len(all_units)} units / {len(all_links)} dialogue links / {len(all_perf_ids)} performance occurrences** | not-started |'
s, nsub = re.subn(r'^\| Vandikkaran Magan / வண்டிக்காரன் மகன் \|.*$', row, s, count=1, flags=re.M)
assert nsub == 1
block = f'''## Vandikkaran Magan current checkpoint

- canonical Tamil / visual / historical-glyph / final visual: **87/87 / 87/87 / 87/87 / 87/87 COMPLETE-PASS**;
- scene derivatives: **72/72 COMPLETE-VERIFIED / boundary QA PASS**;
- reconciled immutable dialogue index: **773 / 38 exact labels / COMPLETE-VERIFIED-RECONCILED / QA PASS**;
- character/entity index: **32 entities / 38/38 labels / 773/773 records / COMPLETE-VERIFIED / QA PASS**;
- song/performance layer: **9/9 COMPLETE-VERIFIED-SOURCE-ONLY / QA PASS**;
- item-level source-attributed lyricists: **0**; unresolved item-level lyric authorships: **6**;
- English translation: **20/72 VERIFIED / QA PASS — {len(all_units)} units / {len(all_links)} immutable dialogue links / {len(all_unlabelled)} source-unlabelled spoken units / {len(all_perf_ids)} unique performance occurrence links**;
- English batch size: **15 scenes per iteration**;
- upstream canonical Tamil / scene / dialogue-record / character-mapping / song-record mutation from this translation batch: **0**.

**Next production phase:** {NEXT}

'''
s, nsub = re.subn(r'## Vandikkaran Magan current checkpoint\n.*?(?=## Naam current checkpoint)', block, s, count=1, flags=re.S)
assert nsub == 1
s = re.sub(r'Vandikkaran Magan is the active production work\. Its canonical Tamil/source gates and \*\*72/72 scene derivatives remain COMPLETE-VERIFIED\*\*;.*?(?=\n\n<!-- Naam song gate)',
           f'Vandikkaran Magan is the active production work. Its source/Tamil, 72-scene, reconciled 773-dialogue, 32-entity and 9-occurrence song/performance authorities remain closed. English translation is **20/72 VERIFIED / QA PASS** at **{len(all_units)} units**, using **15-scene iterations**. **Next: archive scene ordinals 21–35.**', s, count=1, flags=re.S)
sp.write_text(s, encoding='utf-8')

# Final active-pointer sanity.
assert 'scene ordinals 21–35' in (W/'README.md').read_text(encoding='utf-8')
assert '20/72 scenes VERIFIED' in (W/'README.md').read_text(encoding='utf-8')
assert '15 scenes per iteration' in (W/'NEXT_CHAT_PROMPT.md').read_text(encoding='utf-8')
print(json.dumps({
    'status':'PASS','batch_scenes':'6-20','batch_size':15,'batch_units':len(new_units),'batch_dialogue_links':186,
    'cumulative_scenes':20,'cumulative_units':len(all_units),'cumulative_dialogue_links':len(all_links),
    'source_unlabelled_spoken_units':len(all_unlabelled),'performance_occurrence_links':len(all_perf_ids),
    'next':'21-35'
}, ensure_ascii=False))
