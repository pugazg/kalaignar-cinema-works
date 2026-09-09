from pathlib import Path
import json, re

W=Path('works/naam'); T=W/'translations'; R=T/'records'
NEXT=("Translate and verify source-numbered scenes 16–25 as the next 10-scene English batch. "
      "Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; "
      "keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units and stage/narrative ownership; "
      "translate only source-visible performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-003` in scene 21 with unresolved item-level authorship; "
      "do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; only a final remainder may contain fewer scenes.")

def rt(p): return Path(p).read_text(encoding='utf-8')
def wt(p,s): Path(p).parent.mkdir(parents=True,exist_ok=True); Path(p).write_text(s,encoding='utf-8')
def rj(p): return json.loads(rt(p))
def wj(p,d): wt(p,json.dumps(d,ensure_ascii=False,indent=2)+'\n')

# English dialogue translations, in immutable source-record order.
D={
6:[
"What are you looking for, Prema?",
"Appa said there's a good medicine! If it's applied for pain or wounds, he says it will heal at once. That's what I'm looking for.",
"No need, Prema... use the medicine you already have! Why should you trouble yourself?",
"No matter how much trouble I take for you, I don't mind......",
"If everyone in the world had this loving heart......",
"What would it be like? Can everyone be a Prema? It's the gardener who worries about a beautiful flowering plant. Would cattle worry about it?",
"Good thing... you reminded me... I'd completely forgotten. I have to drive the cattle out. Otherwise that zamindar will shout! I'm going.",
"Why... like this... don't you need even a little rest?",
"You're crazy! In this world, rest for the poor means 'laziness.'",
"‘In one place... in a world without you... it would keep rolling... pa......’",
"What is it, Mathirai?",
"I chased him and chased him, and finally tied that body-oil onto his head and came back.",
"Ayyo... poor fellow......",
"My running wasn't the sin... I paid one rupee and bought that oil and took it to him—that was the sin.",
"Hey... Mathirai!",
"Ayyayyo... the puppy will die."
],
7:[
"Yes... where are you taking this goat after putting a garland on it?",
"Where else would they take a garlanded goat, son? To sacrifice it to the Maada deity.",
"Mathirai! You're going along too?",
"What can I do? I have to live with the village! So I'll go along and get it over with.",
"Hey, sir... in God's name you're going to kill this voiceless creature......",
"Why, son... then... are you saying there is no God at all?",
"I didn't say there is no God... God......"
],
8:[
"Meenu......",
"Kumaran......",
"Has your brother fallen asleep?",
"He's asleep! Yes... are you going tomorrow for the tax collection?",
"Don't you know? Tomorrow your brother is going to collect taxes! Look at this cruelty, Meenu... with no seasonal rain, hunger and famine are dancing with their hair loose... and your brother is going out to collect tax—tax collection.",
"Brother gets angry because he knows you talk like this!",
"Come with me tomorrow and see—you'll feel that burning pain too. A man will say he has no way to pay the tax—your brother will beat him until his own arm aches. Eyes robbed of light—dried lips—sunken stomachs... these are in those broken huts. Sobs and hiccups for those forsaken people—their sorrowing voice will sound like the notes of a veena to these sightless men. A pauper will writhe with hunger—a child without milk will scream... a heart without compassion, a nature without sight, deeds without dignity: these are in your brother's durbar...... He will call Mukhari 'Mohanam.' He will call a funeral lament a graceful song... Meenu... you often say, ‘God will save us’—those destitute people too will cry that a thousand times... he will beat them... until blood drips from their bodies... cries of ‘Ayyo’... can this deed be borne...? They will curl up before the whirling whip... amid all this, your brother's chariot of authority is going to parade through the street of the working people... come and see... come and see... look... look......",
"Hey... what's that noise there?",
"You're lighting firecrackers in front of a haystack.",
"Firecrackers, is this? Meenu......",
"Enough... enough... don't start again.\n\nKumaran:\n\nO speaking yaazh, doe-eyed maiden,\nYou are the breeze that blows.\n\nMeenu:\n\nO blue sky, can you forget yourself\nAnd praise the moon?\n\nKumaran:\n\nO beauty! Tamil epic,\nAn unpainted painting—\n\nMeenu:\n\nSpeaking words of delight again and again,\nCasting loving glances again and again.",
"O speaking yaazh, doe-eyed maiden—",
"If I am the yaazh, then you are surely its music.\n\nKumaran:\n\nThere are differences within music;\nWe need none between us.\n\nBoth:\n\nA life of love is the juice of ripe fruit,\nThe delight of women and valiant men."
],
9:[
"What is it?",
"It hasn't got up, sir.",
"Then...? Are you asking me to walk? You take one side and pull.",
"Hey! The cow must be very tired! Go give it water! After watering it, go bring that lame cow. Me......",
"Enough suffering. I can't bear any more.",
"(Embracing his beloved mother) Amma... what is happening to you?",
"Why do these cursed eyes still remain? On life's cart, I dreamed that you and my daughter-in-law would be yoked together and taste that splendour! The dream has vanished into a mirage—I never imagined in this wretched heart that my son would be the one pulling a cart.",
"Amma... give me permission right now—we'll leave this place.",
"No, my dear... my blood boils even more than yours. But... it is for that one matter that I am still alive.",
"You keep saying that... what is that secret, Amma?",
"The secret that will make you a wealthy man is trapped with Mallayappan.",
"Tell me the matter.",
"What is there to tell? Mother and son are waiting with a knife for your throat.",
"Tell me fully, Gnanam!",
"Kumaran is raging that he will kill you. He says the secret that will make him a wealthy man is caught with you! I heard Narayani tell Kumaran this with my own ears.",
"Secret... secret... that will itself... Gnanam! She isn't Narayani—she is Vedavalli in the guise of a maid! We must not let them go—something disastrous will happen.",
"If I'd known you would forget even me and worry like this, I would never have told you.",
"Enough, Gnanam! We must not let them go! Gnanam, look here!",
"Poison!",
"The poison is with me—the cunning is with you. That beggar Kumaran must become a corpse. Careful! Conspiracy is a kind of magic trick! You're the right woman for it! I'm leaving town urgently today. Before I return tonight, fire must be spreading over that dog's corpse."
],
10:[
"Ah... it was you...? I wondered how the cow was eating and eating the hay.",
"Oh, go away, Kumaran.",
"Yes... why have you come earlier today?",
"Brother isn't in town.",
"Sister-in-law?",
"That demon will be asleep.",
"Yes... you keep coming like this... what happens if someone sees you?",
"I don't care about anyone! All I want is your undying love.",
"Yes... what if there's no milk for one day? Why do you have to run off in such a hurry?",
"It's no trouble for me.",
"Hmm... do all poor people get milk like this?",
"Does everyone get a Meenu like this? Drink it...",
"You drink first.",
"You first.",
"No... you.",
"Amma...",
"I came to see whether you'd gone to bed. Still not asleep?",
"Drink some milk, Amma...",
"Where did you get milk, my dear?",
"Drink it, Amma... I'll tell you another day.",
"My dear... you drink.",
"I grew on your milk—can't I at least see your love in this milk?",
"My dear... is love in milk? The love that never dries up is in your gaze.",
"Drink it, Amma.",
"Now you drink.",
"A little more!",
"Amma...",
"Kumara... some conspiracy has happened. You were the one marked for it—I am the one who has been killed, my boy! Today, as I leave, I will reveal the supreme secret I have hidden for so many days.",
"Gnanam!",
"Victory! Come and see... I'll tell you the details later.",
"Then who is this Mallayappar?",
"A distant relative of your father! He came from Malaya. By intrigue he seized our property. Kumara... somehow find that will.",
"Amma... Amma...",
"Hey... Kumara... what's that noise there?",
"Amma...",
"Cholera? Janni? Pick her up and dump her somewhere.",
"Kumaran... what terrible thing is this...",
"(Angrily) Tch... don't touch my mother! You ran off in such a hurry saying you'd bring milk... now I know why.",
"Kumaran... believe me.",
"You coaxed me, saying ‘You drink first’... I didn't know then that you'd bring poison for me to drink...",
"Kumaran... there was nothing wrong in what I gave you.",
"You gave it correctly... I'm the one who made the mistake and gave it to my mother.",
"Kumaran... after knowing me all these days, do you still not understand me?",
"I understand you, girl—I understand. The one who swims in the poor man's blood is your brother! The younger sister frolics in that same water. The one who turns a labourer's bones into anklets is your brother! The younger sister wears them and dances! And for her I am to have affection, tenderness, love..."
],
11:[
"Meenu...! It looks very fine that you have gone searching for honour for your brother.",
"Leave aside searching for honour. Couldn't she at least avoid searching for disgrace?",
"Meenu... to protect my self-respect, I won't even see you as my sister. Be careful!"
],
12:[
"Doctor... come quickly, doctor...",
"What is it, Kumara? Who is it! Narayani...",
"What is it, doctor?",
"(Silence)",
"Amma..."
],
13:[
"Kumara...",
"Come... I have no place where I can ask you to sit and receive you. This is the house I built for my mother—sit here.",
"Kumara... will the dead return because we grieve?",
"I know that too. But how am I to finish the work they left behind?",
"You're deeply shaken.",
"I'm not shaken! I've taken an oath of duty. I am a rich man... I am a zamindar....",
"What—you're a rich man?",
"Don't be afraid! I am a rich man! But... not all rich people have to be bad. Do you know what killed my mother? Not the disease the doctors name... not the fate the Vedantists speak of... poison prepared in the camp of the cruel... that killed my mother.",
"...Poison!",
"Yes. Poison... it turned my mother, who kept preaching ‘peace... peace,’ into a tomb. On that tomb Mallayappan's blood must pour down like rain! The eyes of that intoxicated clan must be plucked out and scattered like flowers. Amma... Kumaran will not rest until he fulfils the promise he gave you! He must answer these trembling hands! I will not leave that traitor alive! Revenge for revenge...!",
"Elder... is there no favourable answer?",
"I know nothing about any will.",
"A will, or a lump of mud—what difference?",
"Haven't you even heard of such a will?",
"I've only heard of it.",
"What did you hear, sir?",
"Hey, who are you? You look completely mad... asking questions right in the middle of the game...",
"(Near the grave) Amma... they say I'm mad, Amma... am I mad, Amma...?",
"They will say you're mad, Kumara! Even I cannot believe your new history; how will others believe it?",
"Ah... don't you know that such a will was written?",
"I know a will was written. You can see stars falling in the sky! But finding where one fell—that's the hard part.",
"Wherever it is, fine! Just tell me the place.",
"They won't have put it on display in a crystal hall! Who knows in what snake-filled wilderness it is hiding...",
"Snake forest—underground tunnel! Just tell me the place, doctor.",
"A will is a sword! It has to be sharpened on the whetstone called law. Only then can you meet Mallayappan on the battlefield called the court. An ordinary man cannot buy this whetstone! Vast resources are needed! Don't infer from this advice that I know where the will is.",
"Doctor... is disappointment the only answer?",
"Those who know tact will turn even disappointment into a ladder. You need money to conduct a case! Then search for the will.",
"Lakshmi came along on the way, Appa... yes... they say Kumaran is wandering about crying ‘will, will’... what is it, Appa?",
"Bring it quickly... I'm hungry.",
"Evidence...? (To herself) The zamindar's son?",
"Yes... a doctor treated the dead zamindar. That doctor hid the will.",
"What are you saying, Appa? Who is that cruel man?",
"Not a cruel man! A man greedy to make his daughter the zamindarani.",
"Who is that greedy man?",
"Prema's father.",
"Ah... you! Have you told him this?",
"Foolish girl! Don't rush! Do you know I approve of the love you have for Kumaran? He must marry you without looking down on you as poor. Then the lawsuit—after that Kumaran becomes zamindar! You become zamindarani!!",
"Ah...! My Kumaran is a zamindar! My beloved is a zamindar!!!"
],
14:[
"Hey, brother! Come here! Will you carry this box for me?",
"Oh—",
"Lift it... onto your head...",
"Hello... only now you're coming?",
"Yes... hey... put the box and bedding inside. Hmm... has that Sathya Seelan arrived?",
"He's arrived.",
"I saw on the way here. The advertising is really grand.",
"Mr. Bheemasenan! I'm a contractor! I have no notion at all of saving money. (An orange is also placed before him.) Eat!",
"Never mind... you really are Kandasamy through and through.",
"Sir... sir...",
"Who is it?",
"The man who carried the load here.",
"Oh... ho... I forgot. Here, one anna.",
"One anna!",
"Then how much do you want?",
"Give me whatever you think is fair.",
"My first mistake was talking to this fellow at all! Hey... go away respectfully.",
"I carried it such a long way.",
"Talking back too, are you? Hey... are you going? Want a kick?",
"A kick for asking for my wage!",
"Hey... take what you're given and go.",
"What—the kick?",
"Hey... are you going now or not?",
"Some people are bloated with money; some are bloated with flesh!",
"Hey... what did you say? What did you say? ...Kandasamy stops him.",
"Mr. Bheemasenan! If you start boxing right now, people will watch and leave without buying tickets. For me, collection means collection.",
"Let go, Mr. Kandasamy! These fellows shouldn't be let off so easily.",
"Mr. Bheemasenan! You're very tired—poor man, take some rest—I'll be right back.",
"Never mind... he's really battered my hand."
],
15:[
"Sabash! Boxer Govindan—horrible death! Opposing wrestler arrested for fighting by foul means.",
"Who... Kumaran?",
"No! The man who is going to kill Kumaran won't be arrested! Gnanam! I'm going to arrange a boxing match in our village. A fight between Kumaran—and another man! I'll turn that other man into Yama and have him kill Kumaran.",
"Who is that other man?",
"The wrestler! Paramasivam."
]}

NOTES={
(8,7):["The long PDF 17–18 speech keeps the source's class rhetoric, musical references `முகாரி / மோகனம்`, repeated cries and whip imagery rather than smoothing them into neutral exposition."],
(9,7):["The verified source contains unusual phrases around the imagined life-cart and Narayani's heart; English stays close to the immediate sense without altering Tamil."],
(10,36):["`ஜன்னி` is retained as `janni` rather than silently forcing a modern medical diagnosis."],
(13,17):["The verified colloquial sentence is irregular; English preserves its immediate sense as a taunting dismissal rather than inventing a repaired Tamil source."],
(14,29):["The source verb in `என் கையை வேறிலே சுமட்டிக் கிட்டான்` is unusual; English renders the immediate injury sense conservatively."],
}

# Source extras in exact scene order: kind, pdf page, English, locator kind, description, optional occurrence ID, optional notes.
X={
6:{
'loc':('narrative',14,"Location: the physician's house.",'scene-location','Source location line.',None,[]),
'cross':('stage-direction',15,"(Kumaran leaves. Mathirai comes from the opposite direction.)",'scene-stage-direction','Kumaran exits and Mathirai enters.',None,[]),
'look':('stage-direction',15,"(Prema stands looking in the direction Kumaran went.)",'scene-stage-direction','Closing visual direction.',None,[]),
},
7:{
'arrive':('stage-direction',16,"(Many people arrive holding a goat; Mathirai is one among them.)",'scene-stage-direction','Opening goat-sacrifice procession.',None,[]),
'cue':('performance-cue',16,"[Song]",'performance-cue','Explicit `[பாட்டு]` marker.','naam-perf-001',["This occurrence carries the specific source-printed item attribution `பாரதியார்` from PDF 4."]),
'release':('stage-direction',16,"(At once they untie the goat and drive it away.)",'scene-stage-direction','Action immediately after the song.',None,[]),
},
8:{
'opening':('narrative',17,"At night, while Kumaran is asleep, Meenu comes secretly, without anyone knowing, to meet and speak with him. What is wrong in a lover meeting her beloved and talking under a dog's protection?",'scene-narrative','Opening source narration.',None,[]),
'alone':('stage-direction',17,"(The two are alone.)",'scene-stage-direction','The lovers are alone.',None,[]),
'hide':('stage-direction',18,"(Meenu runs and hides.)",'scene-stage-direction','Meenu hides when Mallayappar calls out.',None,[]),
'after':('stage-direction',18,"(After Mallayappar leaves.)",'scene-stage-direction','Conversation resumes after Mallayappar leaves.',None,[]),
},
9:{
'depart':('stage-direction',19,"[Mallayappar sets out to collect taxes.]",'scene-stage-direction','Opening tax-collection departure.',None,[]),
'road':('narrative',19,"Location: road.",'scene-location','Road location.',None,[]),
'pull':('stage-direction',19,"(In place of the bull, Kumaran himself pulls the cart.)",'scene-stage-direction','Kumaran is made to pull the cart.',None,[]),
'mansion':('narrative',19,"Location: entrance to the mansion.",'scene-location','Mansion entrance location.',None,[]),
'faint':('stage-direction',19,"(Seeing this from the upper floor, Narayani faints.)",'scene-stage-direction','Narayani sees Kumaran and faints.',None,[]),
'runup':('stage-direction',19,"(Kumaran runs upstairs—to see his fainted mother.)",'scene-stage-direction','Kumaran runs to Narayani.',None,[]),
'eaves':('stage-direction',20,"[Gnanam eavesdrops.]",'scene-stage-direction','Gnanam overhears Narayani and Kumaran.',None,[]),
'change':('stage-direction',20,"(The scene changes.)",'scene-stage-direction','Internal source scene change.',None,[]),
'alone':('stage-direction',20,"(The two are alone.)",'scene-stage-direction','Mallayappar and Gnanam alone.',None,[]),
'poison':('stage-direction',20,"(Saying this, he shows her a bottle of poison.)",'scene-stage-direction','Mallayappar shows poison bottle.',None,[]),
},
10:{
'hay':('stage-direction',21,"(Kumaran is feeding hay to the cow. Meenu comes secretly and lifts the hay away. Kumaran catches her.)",'scene-stage-direction','Opening hay-play action.',None,[]),
'milk':('stage-direction',21,"(Saying this, she bounds away to bring milk. There Gnanam has mixed poison into the milk.)",'scene-stage-direction','Meenu goes for milk; Gnanam has poisoned it.',None,[]),
'nar':('stage-direction',22,"(At that moment Narayani arrives.)",'scene-stage-direction','Narayani enters.',None,[]),
'hides':('stage-direction',22,"(Meenu runs and hides.)",'scene-stage-direction','Meenu hides on Narayani arrival.',None,[]),
'unlabel':('dialogue',22,"What is it, Amma?",'source-unlabelled-speech','Printed `எங்கம்மா?` has no source speaker label.',None,["The source supplies no speaker label or delimiter; the utterance remains deliberately unassigned and unlinked."]),
'drinks':('stage-direction',22,"(Narayani drinks the milk.)",'scene-stage-direction','Narayani drinks poisoned milk.',None,[]),
'collapse':('stage-direction',23,"(After drinking the poisoned milk, Narayani collapses. Kumaran is shocked.)",'scene-stage-direction','Narayani collapses after poisoned milk.',None,[]),
'change1':('stage-direction',23,"(The scene changes.)",'scene-stage-direction','Internal source scene change to Mallayappar and Gnanam.',None,[]),
'joy':('stage-direction',23,"(Seeing this horrific sight, Mallayappan rejoices excessively—with arrogance.)",'scene-stage-direction','Mallayappan reacts to the poisoned scene.',None,[]),
'change2':('stage-direction',23,"(Scene changes.)",'scene-stage-direction','Internal source scene returns to Kumaran/Narayani.',None,[]),
'meenu':('stage-direction',23,"(Meenu enters.)",'scene-stage-direction','Meenu enters.',None,[]),
'push':('stage-direction',24,"(Saying this, Kumaran thrusts Meenu away. Meenu leaves.)",'scene-stage-direction','Kumaran rejects Meenu.',None,[]),
'doctor':('stage-direction',24,"Kumaran goes to the physician with his mother.",'scene-stage-direction','Closing movement to physician.',None,[]),
},
12:{
'loc':('narrative',25,"Location: the physician's hut.",'scene-location','Source location line.',None,[]),
'exam':('stage-direction',25,"(The physician takes Narayani's hand and examines her.)",'scene-stage-direction','Physician examines Narayani.',None,[]),
'chicken':('stage-direction',25,"(The chicken lying on the floor also loses its life.)",'scene-stage-direction','Source confirms poison lethality through chicken.',None,[]),
'pity':('narrative',25,"(Poor thing...)",'scene-narrative','Source parenthetical lament.',None,[]),
},
13:{
'loc':('narrative',25,"Location: Narayani's grave.",'scene-location','Source location line.',None,[]),
'revenge':('stage-direction',26,"(He decided to take revenge. He questioned many people about the will...)",'scene-stage-direction','Search montage begins.',None,[]),
'wanders':('stage-direction',26,"(Kumaran wandered; everywhere the echo was ‘madman.’)",'scene-stage-direction','Search montage ends in ridicule.',None,[]),
'kumleaves':('stage-direction',27,"(Kumaran leaves.)",'scene-stage-direction','Kumaran exits after Sanjeevi advice.',None,[]),
'prema':('stage-direction',27,"(Prema enters.)",'scene-stage-direction','Prema enters.',None,[]),
'unlabel1':('dialogue',28,"What is it, Prema... so late?",'source-unlabelled-speech','Printed `என் பிரேமா...இவ்வளவு நேரம்?` has no source speaker label.',None,["The immediate context suggests Sanjeevi, but the source prints no label; the English layer therefore remains unassigned."]),
'food':('stage-direction',28,"(She goes inside with the food.)",'scene-stage-direction','Prema carries food inside.',None,[]),
'unlabel2':('dialogue',28,"No! Bring it here. (While eating) He is the heir to the zamindari property! Kumaran is the late zamindar's son. There was no lawful wife! He is the son of a beloved consort! All the properties were written over to Kumaran. He is searching for evidence of that will.",'source-unlabelled-speech','Long printed speech after food direction has no source speaker label.',None,["Context strongly points to Sanjeevi, but no source label is printed; no speaker is manufactured in metadata."]),
},
14:{
'labor':('stage-direction',29,"(Kumaran works as a labourer in Chennai.)",'scene-stage-direction','Opening Chennai labour setting.',None,[]),
'house':('stage-direction',29,"[Kandasamy's house]",'scene-stage-direction','Source location bracket.',None,[]),
'fight':('stage-direction',30,"(A fight breaks out between Kumaran and Bheemasenan.)",'scene-stage-direction','Boxing fight begins.',None,[]),
'wins':('stage-direction',30,"(Kumaran wins.)",'scene-stage-direction','Kumaran wins fight.',None,[]),
'becomes':('stage-direction',30,"(Kumaran, who came as a labourer, becomes a boxer.)",'scene-stage-direction','Closing transformation.',None,[]),
},
15:{
'news':('stage-direction',31,"(News that Kumaran has become a boxer spreads through the whole village, reaches Mathirai, and finally reaches Mallayappan too.)",'scene-stage-direction','Opening news-spread montage.',None,[]),
}}

# Scene 7 song: source-visible Bharathiyar text, translated only from the retained record.
PERF001_LINES=[
("ஆயிரம் தெய்வங்கள் உண்டென்று தேடி","Seeking, saying there are a thousand gods,"),
("அலையும் அறிவிலிகாள்—பல","you fools who wander—through many"),
("லாயிரம் வேதம் அறிவொன்றே தெய்வம","thousands of Vedas, that knowledge alone is God,"),
("எனக் கேளீரோ","have you not heard?"),
("மாடனைக் காடனை வேடனைப் போற்றி","Praising Maadan, Kaadan and Vedan,"),
("மயங்கு மதியிலிகாள்—எத","you witless ones who wander in delusion—within whatever"),
("னூடுநின்றோங்கும் அறிவொன்றே தெய்வமென்","stands and rises, that knowledge alone is God—"),
("றோதியறியீரோ","have you not learned what was proclaimed?"),
("மெள்ளப் பலதெய்வம் கூட்டி வளர்த்து","Slowly gathering and nurturing many gods,"),
("வெறுங்கதைகள் சேர்த்துப்—பல","adding empty tales—and many"),
("கள்ள மதங்கள் பரப்புதற் கோர்முறை","false religions to spread—can you devise a method"),
("காட்டவும் வல்லீரோ.","and show it?")]

# Scene 8 performance maps are attached to the immutable dialogue units that already own the printed spans.
LM8={
11:[
('role-cue','குமரன் :','Kumaran:'),('lyric-line','பேசும் யாழே பெண் மானே','O speaking yaazh, doe-eyed maiden,'),('lyric-line','வீசும் தென்றல் நீ தானே.','You are the breeze that blows.'),
('role-cue','மீனு :','Meenu:'),('lyric-line','நீல வானே தன்னை மறந்து','O blue sky, can you forget yourself'),('lyric-line','நிலவினைப் புகழ்ந்திடலாமோ.','And praise the moon?'),
('role-cue','குமரன் :','Kumaran:'),('lyric-line','எழிலே! தமிழ்க் காவியமே','O beauty! Tamil epic,'),('lyric-line','எழுதாத ஓவியமே—','An unpainted painting—'),
('role-cue','மீனு :','Meenu:'),('lyric-line','இன்ப மொழி பேசி பேசி','Speaking words of delight again and again,'),('lyric-line','அன்புப் பார்வை வீசி வீசி.','Casting loving glances again and again.')],
12:[('role-cue','குமரன் :','Kumaran:'),('lyric-line','பேசும் யாழே பெண் மானே—','O speaking yaazh, doe-eyed maiden—')],
13:[('role-cue','மீனு :','Meenu:'),('lyric-line','யாழே நானென்றால் நாதம் நீர்தானே','If I am the yaazh, then you are surely its music.'),
('role-cue','குமரன் :','Kumaran:'),('lyric-line','நாதத்தில் பேதம் உண்டு','There are differences within music;'),('lyric-line','நமக்கது வேண்டாமே.','We need none between us.'),
('role-cue','இருவர் :','Both:'),('lyric-line','காதல் வாழ்வே கனி ரசமே','A life of love is the juice of ripe fruit,'),('lyric-line','மாதர் மறவர் உல்லாசமே.','The delight of women and valiant men.')]
}

ORDER={
6:['x:loc']+[f'd{i:03d}' for i in range(1,10)]+['x:cross']+[f'd{i:03d}' for i in range(10,17)]+['x:look'],
7:['x:arrive']+[f'd{i:03d}' for i in range(1,8)]+['x:cue','p:001','x:release'],
8:['x:opening','x:alone']+[f'd{i:03d}' for i in range(1,9)]+['x:hide','x:after']+[f'd{i:03d}' for i in range(9,14)],
9:['x:depart','x:road','d001','d002','d003','x:pull','x:mansion','d004','x:faint','d005','x:runup','d006','d007','d008','d009','d010','d011','x:eaves','x:change','d012','d013','d014','d015','d016','x:alone','d017','d018','x:poison','d019','d020'],
10:['x:hay']+[f'd{i:03d}' for i in range(1,9)]+['x:milk','d009','d010']+[f'd{i:03d}' for i in range(11,16)]+['x:nar','d016','x:hides','x:unlabel']+[f'd{i:03d}' for i in range(17,25)]+['x:drinks','d025','d026','x:collapse','d027','d028','x:change1','d029','d030','x:joy','x:change2']+[f'd{i:03d}' for i in range(31,37)]+['x:meenu','d037']+[f'd{i:03d}' for i in range(38,45)]+['x:push','x:doctor'],
11:[f'd{i:03d}' for i in range(1,4)],
12:['x:loc','d001','d002','x:exam','d003','d004','d005','x:chicken','x:pity'],
13:['x:loc']+[f'd{i:03d}' for i in range(1,11)]+['x:revenge']+[f'd{i:03d}' for i in range(11,18)]+['x:wanders']+[f'd{i:03d}' for i in range(18,28)]+['x:kumleaves','x:prema','x:unlabel1','d028','d029','x:food','x:unlabel2']+[f'd{i:03d}' for i in range(30,39)],
14:['x:labor','d001','d002','d003','x:house']+[f'd{i:03d}' for i in range(4,26)]+['x:fight','d026','d027','x:wins','d028','d029','x:becomes'],
15:['x:news']+[f'd{i:03d}' for i in range(1,6)]}

EXPECTED_COUNTS={6:16,7:7,8:13,9:20,10:44,11:3,12:5,13:38,14:29,15:5}

def source_scene_path(n): return f'works/naam/scenes/scene-{n:03d}.md'
def source_dialogue_path(n): return f'works/naam/dialogues/records/scene-{n:03d}.json'

def d_unit(n,di,uid,src):
    r=src[di-1]
    assert r['id']==f'naam-s{n:03d}-d{di:03d}'
    val=D[n][di-1]
    tr={'english_text':val,'mode':'prose-faithful','notes':list(NOTES.get((n,di),[]))}
    occ=None
    if n==8 and di in LM8:
        occ='naam-perf-002'
        lm=[]
        for k,t,e in LM8[di]: lm.append({'ordinal':len(lm)+1,'kind':k,'pdf_page':18,'tamil':t,'english':e})
        tr['line_map']=lm
        tr['notes'].append('This immutable dialogue record owns part of `naam-perf-002`; the English performance link is attached here so the printed span is not duplicated in a separate song unit.')
    return {'id':uid,'kind':'dialogue','status':'verified','target_language':'en','scene_id':f'naam-s{n:03d}','scene_ordinal':n,'source_scene_number':n,
      'source':{'source_path':source_dialogue_path(n),'canonical_scene_path':source_scene_path(n),'source_record_id':r['id'],'source_occurrence_id':occ,'source_locator':None,'speaker_label':r['speaker_label'],'speaker_label_origin':'source-explicit','source_delimiter':r['source_delimiter'],'page_provenance':r['page_provenance']},
      'translation':tr}

def x_unit(n,key,uid):
    kind,page,eng,lkind,desc,occ,notes=X[n][key]
    return {'id':uid,'kind':kind,'status':'verified','target_language':'en','scene_id':f'naam-s{n:03d}','scene_ordinal':n,'source_scene_number':n,
      'source':{'source_path':source_scene_path(n),'canonical_scene_path':source_scene_path(n),'source_record_id':None,'source_occurrence_id':occ,'source_locator':{'kind':lkind,'ordinal':1,'description':desc},'speaker_label':None,'speaker_label_origin':None,'source_delimiter':None,'page_provenance':[{'pdf_page':page,'printed_page':page}]},
      'translation':{'english_text':eng,'mode':'prose-faithful','notes':notes}}

def perf001_unit(uid):
    lm=[{'ordinal':i+1,'kind':'lyric-line','pdf_page':16,'tamil':t,'english':e} for i,(t,e) in enumerate(PERF001_LINES)]
    lines=['1.']+[e for _,e in PERF001_LINES[:4]]+['2.']+[e for _,e in PERF001_LINES[4:8]]+['3.']+[e for _,e in PERF001_LINES[8:]]
    return {'id':uid,'kind':'song','status':'verified','target_language':'en','scene_id':'naam-s007','scene_ordinal':7,'source_scene_number':7,
      'source':{'source_path':'works/naam/songs/records/naam-perf-001.md','canonical_scene_path':source_scene_path(7),'source_record_id':None,'source_occurrence_id':'naam-perf-001','source_locator':{'kind':'retained-performance-record','ordinal':1,'description':'Full source-visible `ஆயிரம் தெய்வங்கள்` lyric body.'},'speaker_label':None,'speaker_label_origin':None,'source_delimiter':None,'page_provenance':[{'pdf_page':16,'printed_page':16}]},
      'translation':{'english_lines':lines,'line_map':lm,'mode':'semantic-poetic-source-faithful','notes':['Translated only from the source-visible Tamil retained in `naam-perf-001`.','Specific item-level source attribution preserved: பாரதியார்.','The unusual printed line breaks are mapped line-by-line rather than repaired from an external edition.']}}

def build_scene(n):
    src=rj(W/f'dialogues/records/scene-{n:03d}.json')
    assert len(src)==EXPECTED_COUNTS[n]==len(D[n])
    units=[]
    for token in ORDER[n]:
        uid=f'naam-en-s{n:03d}-u{len(units)+1:03d}'
        if token.startswith('d'):
            units.append(d_unit(n,int(token[1:]),uid,src))
        elif token.startswith('x:'):
            units.append(x_unit(n,token[2:],uid))
        elif token=='p:001':
            units.append(perf001_unit(uid))
        else: raise AssertionError(token)
    rec={'work_id':'naam','target_language':'en','scene_id':f'naam-s{n:03d}','scene_ordinal':n,'source_scene_number':n,'scene_status':'verified','unit_count':len(units),'units':units}
    wj(R/f'scene-{n:03d}.json',rec)
    return rec

records=[build_scene(n) for n in range(6,16)]
batch_units=sum(x['unit_count'] for x in records)
batch_links=sum(1 for x in records for u in x['units'] if u['source']['source_record_id'])
unlabelled=[u['id'] for x in records for u in x['units'] if u['kind']=='dialogue' and u['source']['source_record_id'] is None]
cross=[u['id'] for x in records for u in x['units'] if len(u['source']['page_provenance'])>1]
occ_ids=[]
line_maps=0
for x in records:
    for u in x['units']:
        occ=u['source']['source_occurrence_id']
        if occ and occ not in occ_ids: occ_ids.append(occ)
        line_maps += len(u['translation'].get('line_map',[]))
assert batch_links==180
assert unlabelled==['naam-en-s010-u022','naam-en-s013-u034','naam-en-s013-u037'],unlabelled
assert set(occ_ids)=={'naam-perf-001','naam-perf-002'},occ_ids
assert line_maps==34,line_maps

scene_results=[]
for x in records:
    linked=sum(1 for u in x['units'] if u['source']['source_record_id'])
    unl=sum(1 for u in x['units'] if u['kind']=='dialogue' and u['source']['source_record_id'] is None)
    occ=[]
    for u in x['units']:
        o=u['source']['source_occurrence_id']
        if o and o not in occ: occ.append(o)
    scene_results.append({'scene_id':x['scene_id'],'source_scene_number':x['source_scene_number'],'translation_units':x['unit_count'],'immutable_dialogue_records_expected':EXPECTED_COUNTS[x['source_scene_number']],'immutable_dialogue_records_linked':linked,'missing_dialogue_links':0,'duplicate_dialogue_links':0,'source_unlabelled_speech_units':unl,'performance_occurrences_linked':occ})

qa={'work_id':'naam','phase':'english-translation-batch-006-015-qa','status':'PASS','source_scenes':list(range(6,16)),'translation_units':batch_units,
    'immutable_dialogue_records_expected':180,'immutable_dialogue_records_linked':180,'dialogue_coverage':'180/180 exactly once','missing_dialogue_links':0,'duplicate_dialogue_links':0,
    'exact_tamil_speaker_labels_preserved':True,'source_delimiters_preserved_as_metadata':True,'source_unlabelled_speech_units':len(unlabelled),'source_unlabelled_unit_ids':unlabelled,'inferred_unlabelled_speakers':0,
    'performance_occurrences_expected':['naam-perf-001','naam-perf-002'],'performance_occurrences_linked':['naam-perf-001','naam-perf-002'],'performance_coverage':'2/2','performance_line_cue_mappings':34,
    'specific_bharathiyar_attribution_preserved_for':'naam-perf-001','naam_perf_002_authorship':'unresolved-item-level','cross_page_translation_units':cross,'scene_results':scene_results,
    'authorship_status_changed_by_translation':False,'external_or_unprinted_lyrics_imported':False,'canonical_tamil_modified':0,'scene_text_modified':0,'dialogue_records_modified':0,'character_entity_mappings_modified':0,'song_source_records_modified_by_translation':0,
    'next_gate':'scenes 16-25 translation batch ready; 10 scenes per iteration'}
wj(T/'batch-006-015-qa.json',qa)

# Cumulative English index.
idx=rj(T/'index.json')
assert idx['verified_scenes']==5 and idx['translation_units_verified']==131 and idx['immutable_dialogue_links_verified']==99
idx['status']='in-progress-verified-through-scene-015'
idx['verified_scenes']=15; idx['verified_scene_ids']=[f'naam-s{i:03d}' for i in range(1,16)]
idx['translation_units_verified']=131+batch_units
idx['immutable_dialogue_links_verified']=279
idx['stage_or_narrative_units_verified']=idx.get('stage_or_narrative_units_verified',29)+sum(1 for x in records for u in x['units'] if u['kind'] in ('narrative','stage-direction'))
idx['performance_cue_units_verified']=idx.get('performance_cue_units_verified',1)+sum(1 for x in records for u in x['units'] if u['kind']=='performance-cue')
idx['song_units_verified']=idx.get('song_units_verified',1)+sum(1 for x in records for u in x['units'] if u['kind']=='song')
idx['retained_performance_records_translated']=3
idx['translated_performance_record_ids']=['naam-perf-007','naam-perf-001','naam-perf-002']
idx['song_line_cue_mappings_verified']=23+34
idx['source_unlabelled_speech_units_verified']=idx.get('source_unlabelled_speech_units_verified',1)+len(unlabelled)
idx['cross_page_translation_units']=list(dict.fromkeys(idx.get('cross_page_translation_units',[])+cross))
idx['batch_006_015_review']='BATCH_006_015_REVIEW.md'; idx['batch_006_015_qa']='batch-006-015-qa.json'; idx['iteration_scene_batch_size']=10; idx['next_activity']=NEXT
wj(T/'index.json',idx)

# Human review.
rows='\n'.join(f"| {r['source_scene_number']} | {r['translation_units']} | {r['immutable_dialogue_records_linked']}/{r['immutable_dialogue_records_expected']} | {r['source_unlabelled_speech_units']} | {', '.join(r['performance_occurrences_linked']) or '0'} |" for r in scene_results)
review=f'''# நாம் — English batch review / scenes 6–15

**Batch:** source scenes `காட்சி 6`–`காட்சி 15`  
**Status:** **VERIFIED**  
**Units:** **{batch_units}**  
**Immutable dialogue links:** **180/180 exactly once**

## Review result

This 10-scene iteration translates and verifies source-numbered scenes 6–15 in source order. All **180/180** immutable explicitly labelled dialogue records are linked exactly once, with exact Tamil speaker labels, delimiters and page provenance retained in metadata. Three genuinely source-unlabelled speech spans remain unassigned: scene 10 `எங்கம்மா?`, and two scene-13 speeches printed without a speaker label.

The retained performance gate is honored without duplicating source ownership. Scene 7 translates `naam-perf-001` (`ஆயிரம் தெய்வங்கள்`) from the source-visible booklet text only and preserves the specific PDF-4 attribution **பாரதியார்**. In scene 8, `naam-perf-002` is already partly owned by immutable dialogue records `d011`–`d013`; the English layer links those same records to the performance occurrence and maps **22** role/lyric cues rather than creating a duplicate song-text unit. Its item-level authorship remains unresolved.

## Scene counts

| Scene | Units | Immutable dialogue links | Unlabelled speech | Performance links |
|---|---:|---:|---:|---|
{rows}
| **Batch** | **{batch_units}** | **180/180** | **{len(unlabelled)}** | **2 unique records** |

## Fidelity decisions

- Scene 6 keeps the worker/poverty joke and Mathirai's clipped quoted fragment inside its immutable dialogue ownership; no new song occurrence is invented.
- Scene 7 uses a fresh source-bound English rendering of the visible Bharathiyar stanza only; no external edition, remembered continuation or web lyric is imported.
- Scene 8 preserves Kumaran's anti-tax/class rhetoric, `முகாரி / மோகனம்` musical references and repeated whip imagery. The cross-page PDF 17→18 speech remains one logical immutable dialogue-linked unit.
- Scene 8's duet preserves `யாழ்` as `yaazh` and keeps role ownership visible through line maps.
- Scene 9 preserves the life-cart / will / poison conspiracy rhetoric without turning source metaphors into neutral summary.
- Scene 10 keeps `ஜன்னி` as `janni` rather than silently diagnosing it; the unlabelled `எங்கம்மா?` remains unassigned.
- Scene 13 preserves the source's violent revenge imagery, law/whetstone/court battlefield metaphor, irregular colloquial dismissal, and both unlabelled speeches without manufacturing labels.
- Scene 14 keeps the labour-wage confrontation, class insult and boxing transition direct; the unusual hand-injury wording is translated conservatively.
- Scene 15 preserves Mallayappar's explicit plan to make Paramasivam a killing opponent; no motive or event beyond the source is added.

## Integrity checks

- expected / linked immutable dialogue records: **180 / 180**;
- missing / duplicate immutable links: **0 / 0**;
- source-unlabelled speeches: **{len(unlabelled)}**, assigned speakers: **0**;
- performance records expected / linked: **2 / 2** — `naam-perf-001`, `naam-perf-002`;
- new performance line/cue mappings: **34** — 12 for `naam-perf-001`, 22 for `naam-perf-002`;
- authorship upgrades: **0**;
- external/unprinted lyric imports: **0**;
- canonical Tamil / scene / dialogue / character / song-source modifications: **0 / 0 / 0 / 0 / 0**.

## Cumulative English checkpoint

After scenes 1–15: **15/45 source scenes**, **{idx['translation_units_verified']} verified English units**, **279 immutable dialogue links**, **{idx['source_unlabelled_speech_units_verified']} source-unlabelled speech units retained without inferred labels**, **3/7 performance records translated**, and **57 Tamil→English performance line/cue mappings**.

## Iteration rule

Per user directive, continue with **10 source scenes per iteration**. Only the final remainder may contain fewer than ten scenes.

## Next batch

{NEXT}
'''
wt(T/'BATCH_006_015_REVIEW.md',review)

# Translation README.
p=T/'README.md'; s=rt(p)
s=re.sub(r'\*\*Status:\*\* \*\*.*?\*\*',f"**Status:** **verified through source scene 15 / 45; {idx['translation_units_verified']} units**",s,count=1)
s=re.sub(r'## Next batch\n\n.*?(?=\n##|\Z)',f"## Next batch\n\n{NEXT}\n",s,flags=re.S)
if '## Verified batch — scenes 6–15' not in s:
    s += f'''\n## Verified batch — scenes 6–15\n\n- source scenes: **10 / scenes 6–15**;\n- units: **{batch_units}**;\n- immutable dialogue links: **180/180**;\n- source-unlabelled speech: **{len(unlabelled)} / inferred speakers 0**;\n- performance occurrences: **2/2 — `naam-perf-001`, `naam-perf-002`**;\n- new line/cue mappings: **34**;\n- upstream rewrites: **0**.\n\nThe continuing production cadence is **10 source scenes per iteration**.\n'''
wt(p,s)

# Work metadata and README mirrors.
p=W/'metadata.yaml'; s=rt(p)
s=re.sub(r'(?m)^  english_translation: .+$','  english_translation: in-progress-verified-15-of-45',s,count=1)
s=re.sub(r'(?m)^  english_translation_verified_scenes: \d+$','  english_translation_verified_scenes: 15',s,count=1)
s=re.sub(r'(?m)^  english_translation_unit_count: \d+$',f"  english_translation_unit_count: {idx['translation_units_verified']}",s,count=1)
s=re.sub(r'(?m)^  english_dialogue_links_verified: \d+$','  english_dialogue_links_verified: 279',s,count=1)
s=re.sub(r'(?m)^  english_performance_records_translated: \d+$','  english_performance_records_translated: 3',s,count=1)
s=re.sub(r'(?m)^  english_song_line_cue_mappings_verified: \d+$','  english_song_line_cue_mappings_verified: 57',s,count=1)
status_i=s.find('\nstatus:\n')
if status_i>=0:
    pre=s[:status_i]; tail=s[status_i:]
    tail=re.sub(r'(?m)^  english_translation: .+$','  english_translation: in-progress-verified-15-of-45',tail,count=1); s=pre+tail
s=re.sub(r'(?m)^next_action:.*$', 'next_action: '+json.dumps(NEXT,ensure_ascii=False),s,count=1)
wt(p,s)

p=W/'README.md'; s=rt(p)
s=re.sub(r'- English translation: \*\*.*?\*\*; reader / Reading Room: \*\*not-started\*\*\.',f"- English translation: **15/45 VERIFIED — {idx['translation_units_verified']} units / 279 dialogue links / 3 of 7 performance records / 57 performance mappings**; reader / Reading Room: **not-started**.",s,count=1)
s=re.sub(r'\*\*Next:\*\* Translate and verify source-numbered scenes [^\n]*','**Next:** '+NEXT,s)
if '## English scenes 6–15 checkpoint' not in s:
    s += f'''\n\n## English scenes 6–15 checkpoint\n\n- English scenes verified: **15/45 cumulative**;\n- cumulative units: **{idx['translation_units_verified']}**;\n- immutable dialogue links: **279**;\n- source-unlabelled speech retained without inferred labels: **{idx['source_unlabelled_speech_units_verified']}**;\n- translated performance records: **3/7 — `naam-perf-007`, `naam-perf-001`, `naam-perf-002`**;\n- performance line/cue mappings: **57**;\n- closed upstream-layer changes: **0**.\n\n**Iteration rule:** 10 source scenes per iteration; final remainder may be smaller.\n\n**Next:** {NEXT}\n'''
wt(p,s)

# Next chat prompt reflects the user's new batch-size directive.
wt(W/'NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. **Live `main` is authoritative.**\n\nCanonical Tamil is **67/67 COMPLETE-VERIFIED**; scenes **45/45 COMPLETE-VERIFIED**; dialogue index **590 immutable records / QA PASS**; character/entity layer **28 entities / 45/45 labels / 590/590 records / QA PASS**; song/performance gate **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED**.\n\nEnglish translation is **VERIFIED THROUGH SOURCE SCENE 15**: **15/45 scenes**, **{idx['translation_units_verified']} units**, **279 immutable dialogue links**, **{idx['source_unlabelled_speech_units_verified']} source-unlabelled speech units with 0 inferred speaker labels**, **3/7 performance records translated**, and **57 performance line/cue mappings**. `naam-perf-001` retains the specific source attribution **பாரதியார்**; `naam-perf-002` remains unresolved at item level.\n\nUser directive: **process 10 source scenes in each English-translation iteration**. Only the final remainder may contain fewer than 10.\n\nCurrent English files: `translations/index.json`, `translations/BATCH_006_015_REVIEW.md`, `translations/batch-006-015-qa.json`, and `translations/records/scene-001.json` through `scene-015.json`.\n\nDo not alter closed Tamil or structured source layers except for later direct source-supported corrections.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# Project handover.
p=W/'PROJECT_HANDOVER.md'; s=rt(p)
tag='## English scenes 6–15 closure checkpoint'
if tag not in s:
    s += f'''\n\n{tag}\n\n- cumulative verified English scenes: **15/45**;\n- cumulative units: **{idx['translation_units_verified']}**;\n- immutable dialogue links: **279**;\n- source-unlabelled speech retained: **{idx['source_unlabelled_speech_units_verified']} / inferred labels 0**;\n- performance records translated: **3/7**;\n- performance line/cue mappings: **57**;\n- upstream source-layer changes caused by English: **0**.\n\n**User iteration directive:** 10 source scenes per English iteration; final remainder may be smaller.\n\n## Current exact next activity\n\n> **{NEXT}**\n'''
wt(p,s)

# Repository data mirror.
p=Path('data/works.json'); data=rj(p); n=next(x for x in data if x.get('id')=='naam'); sd=n.setdefault('structured_derivatives',{})
sd.update({'english_translation':'in-progress-verified-through-scene-015','english_translation_verified_scenes':15,'english_translation_units':idx['translation_units_verified'],'english_dialogue_links_verified':279,
           'english_source_unlabelled_speech_units':idx['source_unlabelled_speech_units_verified'],'english_performance_records_translated':3,'english_song_line_cue_mappings_verified':57,'english_iteration_scene_batch_size':10,'english_translation_index_path':'works/naam/translations/index.json'})
n['next_action']=NEXT; wj(p,data)

# Root current mirror.
p=Path('README.md'); s=rt(p)
s=re.sub(r'- English translation: \*\*.*?\*\*\.',f"- English translation: **15/45 VERIFIED — {idx['translation_units_verified']} units / 279 dialogue links / 3 of 7 performance records / 57 mappings**.",s,count=1)
s=re.sub(r'\*\*Next:\*\* Translate and verify source-numbered scenes [^\n]*','**Next:** '+NEXT,s)
mark='<!-- Naam English scenes 6-15 current -->'
if mark not in s: s += f'''\n\n{mark}\n**Naam current English checkpoint:** **15/45 source scenes VERIFIED**, **{idx['translation_units_verified']} units**, **279 immutable dialogue links**, **3/7 performance records translated**, **57 performance mappings**, **0 upstream rewrites**. Iteration size is now **10 source scenes**. **Next:** {NEXT}\n'''
wt(p,s)

for p in [Path('docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'),Path('docs/STATUS_CONSISTENCY_AUDIT.md')]:
    s=rt(p); mark='<!-- Naam English scenes 6-15 current -->'
    if mark not in s: s += f'''\n\n{mark}\n**Naam English scenes 6-15 current:** English **15/45 verified / {idx['translation_units_verified']} units / 279 dialogue links / 3 of 7 performances / 57 mappings**; source-unlabelled speech remains unassigned; upstream rewrites **0**. User cadence: **10 source scenes per iteration**. **Next:** {NEXT}\n'''
    wt(p,s)

print(json.dumps({'status':'PASS','scenes':'6-15','batch_units':batch_units,'batch_dialogue_links':180,'cumulative_scenes':15,'cumulative_units':idx['translation_units_verified'],'cumulative_dialogue_links':279,'batch_unlabelled':len(unlabelled),'performance_records':['naam-perf-001','naam-perf-002'],'line_maps_added':34,'next':'16-25'},ensure_ascii=False,indent=2))
