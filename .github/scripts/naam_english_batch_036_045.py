from pathlib import Path
import json, re

W = Path('works/naam')
T = W / 'translations'
R = T / 'records'

NEXT = (
    "Run whole-work English translation reconciliation and closure QA across source scenes 1–45 before building the reader/export layer. "
    "Verify every translated unit is source-ordered and unique; all 590 immutable dialogue records are linked exactly once; source-unlabelled speech remains unassigned; "
    "all seven retained song/performance records are translated without authorship upgrades; the scene-34 chant remains a distinct chant; cross-page provenance and written-text/stage ownership are exact; "
    "no duplicate source-span ownership, synthetic scene-end prose, placeholder text, or upstream Tamil/scene/dialogue/character/song-source mutation exists. "
    "If and only if that whole-work gate passes, mark English translation complete-verified and begin Phase 10 whole-work reader/export generation."
)

def rt(p): return Path(p).read_text(encoding='utf-8')
def wt(p, s): Path(p).parent.mkdir(parents=True, exist_ok=True); Path(p).write_text(s, encoding='utf-8')
def rj(p): return json.loads(rt(p))
def wj(p, d): wt(p, json.dumps(d, ensure_ascii=False, indent=2) + '\n')
def scene_path(n): return f'works/naam/scenes/scene-{n:03d}.md'
def dialogue_path(n): return f'works/naam/dialogues/records/scene-{n:03d}.json'
def provenance(v):
    if isinstance(v, list): return [{'pdf_page':p,'printed_page':p} for p in v]
    return [{'pdf_page':v,'printed_page':v}]

D = {
36: [
    "Jeevanandar! It is wrong to cite fate as the reason and push people into poverty. Reform is to make people truly people and prevent them from becoming slaves to anything!",
    "Let us begin that work today itself.",
    "If Meenu were here, she would have been of great help.",
    "Meenu must have gone to America with the zamindar."
],
38: [
    "Hey! Annumalai! What arrogance has got into these village fellows! I've come back from America. Not one fellow is here to welcome me!",
    "What's America, sir? Even if you came from heaven, they wouldn't care! Progress is running wild! The whole populace listens only to Kumaran's words.",
    "Kumaran! Go and bring them here!",
    "Who, sir?",
    "The priest, the purohit, the physician—every one of them.",
    "People who were like frogs in a well... he ruined them by making them read newspapers and books.",
    "Once they start reading—isn't it just like starting to wake up!",
    "Fools; after leaving it alone all these days, you come complaining only now. I am here—and my money is here.",
    "Bhagavan is here too.",
    "Hey... priest... you go along too.",
    "Your command!",
    "Hey! Tear down the entrance of our mansion!",
    "Tear it down?",
    "This huge mansion isn't here merely for my status, you slack-jawed fool! Tear it down! I'm telling you.",
    "Yes, sir.",
    "Go to town and bring the police! Go by cart...... you must return quickly within two hours!"
],
39: [
    "Injustice!",
    "Friends! Remain calm! Preserve dignity, restraint and order. Violence—is a terrible disease! A pit we dig for ourselves! I will go there in person.",
    "This is that chandala, conspirator, atheist, cruel man, murderer... revolutionary......",
    "Why did you stop? Your dictionary still has thief, rogue, reviler of God, tear-drop, scoundrel and so on!",
    "With your magic tricks you ruined my zamindari; using those caught in your spell, you have had the entrance of my mansion torn down! Why... if these men hadn't come, you would have killed me yourself!",
    "Do you expect the police to believe all this? Here are those who lost their homes, those standing in the street—those whose eyes have become pools of tears. Let them count their accounts! Then let them say... who are the only sons born of violence and frenzy?",
    "Did you hear... how even his language reeks of violence?",
    "Kumaran, for the sake of peace in the village, we are arresting you!",
    "Ah!",
    "What, man, are you putting an exclamation mark!",
    "An exclamation mark indeed! Let it grow a little and it will become a question mark! Remember, there isn't much difference between a question mark and an intellectual! And when I say arivaal, I don't mean a sickle that cuts people; I mean the sickle that cuts your authority, arrogance and the tree of ignorance! Hear this! The scholar's pen itself is a sickle!",
    "Kumaran! You may be innocent. But from the evidence the zamindar has given, we have to arrest you. The truth can be proved in court. Until then, we must keep you in custody.",
    "Comrades! The police are doing their duty! Do not provoke their anger! If your anger swells, I alone may die! But... do not die for me. I am going! If I return, we shall meet!"
],
40: [
    "The people's intelligence has grown dull! It has changed to the point where they cannot tell the difference between a man and a cow! From now on Malayappar is not merely a zamindar! He is one who can rule this whole world! A man becoming God, and God becoming man, is all propaganda!",
    "Master!",
    "What is it, priest?",
    "I have a son. His name is Kali Baba! He'll be about ten. If he gives green leaves saying they're for every medicinal herb, there'll be good income.",
    "Kali Baba! Will they believe it?",
    "Didn't I tell you! God becoming man and man becoming God is all propaganda.",
    "Half that income to the Amman temple, half to the zamindar!",
    "All right! Do exactly that!"
],
41: [
    "After considering the arguments of both sides and examining the witnesses, Kumaran does not appear to be a revolutionary, an advocate of violence, or a reviler of God. Telling people to read, worshipping one God—such acts cannot make one a revolutionary or an advocate of violence! In these days when the government itself is taking steps to abolish zamindari, Kumaran has only struggled to restrain the zamindar's outrages. Therefore... Kumaran is released as not guilty.",
    "Sir...... a quarter anna...... please give, sir.",
    "Ah... whose child is this?",
    "It is my child, sir!",
    "Ayyo... my Meenu a prostitute! My Meenu a prostitute!",
    "Kumaran! Kumaran!",
    "Ah... my Kumara! Kumaran... Kumaran...",
    "Tch... don't touch my feet!",
    "Kumaran! This is not my child! Look at what is written in the letter about this child!",
    "Meenu... Sundari... Sundari... Meenu... our child—\n\nour child Muthu is with me, Meenu.",
    "Ah... my child......"
],
42: [
    "Have you seen my Meenu? She went blind so that she would not have to see this cruel face.",
    "I have become a sinner who cannot see the child's face! Muthu... what do you look like? Are you fair like your father? Looking at my disguise, do I seem like a beggar to you? I am not a beggar! A zamindar's wife! Your father is the zamindar!",
    "Meenu...... I never sought that needless crown! I wanted to make all property common property. But...... that desire fell into the fire and its life turned to ash.",
    "It has not turned to ash. It is alive.",
    "It is alive?",
    "Yes... it is with the physician.",
    "Jeevanandar! The people have got a new life!"
],
43: [
    "Where is the will? Where is the will?",
    "The will? What is there with me, man?",
    "Will you give it or not?",
    "What is it, Sanjeevi?",
    "The matter is ruined! Kumaran snatched the will from me.",
    "The will? It was with you all these days? Traitor."
],
44: [
    "Elders! Victory! We do not need the grace of this Kali Baba to drive away our `kamavinai`! My will... your life has been found."
],
45: [
    "Hey Kumara! Your final hour has drawn near.",
    "Hand over that will respectfully!",
    "Malayappa! They say a tiger told a hunter, ‘Put down that bow and arrow! Then I will hunt you.’ You are an even more ridiculous man than that!",
    "Will you give it? Or not?",
    "Who are you to ask? Who am I to give? This is the people's property!",
    "The people! Fool! They are not your people now! They are bullets flying at you from Malayappan's gun!",
    "That is exactly why I say—the gun must be smashed and thrown away.",
    "Kumara! You have laid your head on the sacrificial altar.",
    "Kill me! But, cruel man, do not think that killing a man will destroy an ideology!",
    "Your idea will be smashed to a hundred pieces!",
    "You have read only one half of history! You may have gathered the bones of those smashed to pieces—written down the accounts of those who suffered and shed tears—but you have not read the chapter of revolution that rose on the foundation of those teardrops! Not because your eyesight is defective! Because your ancestral scripture has written that reading is a sin! Set fire if you will, attack treacherously if you will! Let bees sting like scorpions if they will! Let prison open its mouth and welcome us if it will! Shave our heads if you will! Commit brutality if you will! This is a rationalist principle that cannot be destroyed! Ten-and-a-half-touch gold!",
    "Leave it! Otherwise this very house will become your cremation ground.",
    "Life ... life ... for me, who brought a charter of rights, a charter of death? Look, that day you stopped these policemen from arresting me. Today, those same policemen have come to save me from you. What harm have I done to you?",
    "As I am about to give up my life, I ask one last help from you. You have love for me.",
    "I will do anything. Kumaran!",
    "You must live.",
    "I am one who cannot live, Kumaran!",
    "Not for yourself! For the children! Jeevanandar! I make my properties the property of the people! I alone am dying. But my ideas have not died. They will not die... with that satisfaction in my heart, I leave you. Long live self-respect; may rationalism triumph."
]
}
EXPECTED={36:4,37:0,38:16,39:13,40:8,41:11,42:7,43:6,44:1,45:18}
NOTES={
    (39,11): ["The source's question-mark / அறிவாளன் / அரிவாள் wordplay is carried with `intellectual` / `sickle`; Tamil remains authoritative."],
    (41,2): ["`காலணா` is retained as the historical coin denomination `quarter anna`; no modernization to decimal currency."],
    (41,11): ["Exact Tamil source speaker label is the anomalous `உன்மீனு`; the English record does not normalize that label."],
    (44,1): ["The verified source form `காமவினை` is semantically difficult here; English retains it as `kamavinai` rather than silently repairing Tamil."],
    (45,11): ["`பத்தரை மாத்துத் தங்கம்` is retained closely as `ten-and-a-half-touch gold`, a source purity image, rather than replaced by a modern abstraction."]
}

X={
36:{
 'loc':('narrative',58,'(Location: road.)','scene-location','Source location line.',None,[]),
 'cue':('performance-cue',59,'(Kumaran and Jeevanandar engage in village service.)','performance-cue','Nearby source-visible cue for `naam-perf-005`.','naam-perf-005',['The cue is linked to the retained two-block performance occurrence; item-level authorship remains unresolved.'])
},
37:{
 'all':('stage-direction',60,"(After being released from prison, Meenu is about to kill herself when she hears a child's cry and lifts the child. Storm, thunder, lightning and rain all arrive together. Both of Meenu's eyes strike the spear that stood before the temple.)",'scene-stage-direction','Entire zero-dialogue source scene.',None,[])
},
38:{
 'leave1':('stage-direction',61,'(Annumalai leaves.)','scene-stage-direction','Annumalai leaves to summon the others.',None,[]),
 'dismantle':('stage-direction',61,'(By the villain\'s order, the reading room and the school are dismantled.)','scene-stage-direction','Reading room and school dismantled.',None,[]),
 'leave2':('stage-direction',62,'(Annumalai leaves.)','scene-stage-direction','Annumalai leaves to bring the police.',None,[])
},
39:{
 'change':('stage-direction',62,'(The scene changes.)','scene-stage-direction','Internal scene change.',None,[]),
 'loc':('narrative',62,"(Location: entrance to Malayappan's mansion.)",'scene-location','Source location parenthetical.',None,[]),
 'arrest':('stage-direction',63,'(Kumaran is arrested.)','scene-stage-direction','Kumaran is arrested.',None,[]),
 'protest':('stage-direction',63,'(The people protest.)','scene-stage-direction','Crowd protests the arrest.',None,[]),
 'cue':('performance-cue',64,'Background song','performance-cue','Source marker `பின்னணிப் பாடல்`.','naam-perf-006',['Item-level authorship remains unresolved.']),
 'vanakkam':('narrative',64,'Vanakkam.','source-unlabelled-text','Standalone source block `naam-s039-u004` following the background song.',None,['Retained as a standalone source line; no speaker or performance authorship is inferred.']),
 'after':('stage-direction',64,'(The rationalist languished in prison; lovers of the old order turned the people away from a new life. The innocent people now hate the very Kumaran through whom they had found happiness.)','scene-stage-direction','Post-song source parenthetical.',None,[])
},
41:{
 'opening':('narrative',65,'("Kumaran case verdict. Kumaran\'s forceful argument. The people are eager to know the verdict.")','scene-narrative','Opening quoted source synopsis.',None,[]),
 'release':('stage-direction',66,'(As Kumaran comes out after his release... blind Meenu appears as a beggar.)','scene-stage-direction','Kumaran exits court and encounters blind Meenu.',None,[]),
 'letter':('written-text',66,'“Compassionate hearts who see this letter... fulfill the last wish of a woman abandoned after trusting the love of an upper-caste man. Somehow save this child.” Thus—Sundari.','written-text','Source cue `கடிதத்தில் :-` and quoted letter body.',None,['The cue is written-text, not a speaker label; no dialogue ID or character is invented.']),
 'take':('stage-direction',66,'(Kumaran takes Meenu away.)','scene-stage-direction','Kumaran leads Meenu away.',None,[])
},
42:{
 'run':('stage-direction',67,'(Kumaran runs to the physician to seize the will.)','scene-stage-direction','Kumaran runs to recover the will.',None,[])
},
43:{
 'loc':('narrative',67,'(Location—road.)','scene-location','Source location line.',None,[]),
 'seize':('stage-direction',68,'(Kumaran seizes the will from the physician.)','scene-stage-direction','Kumaran takes the will.',None,[]),
 'come':('stage-direction',68,'(Sanjeevi comes to Malayappan.)','scene-stage-direction','Sanjeevi reports to Malayappan.',None,[]),
 'kill':('stage-direction',68,'(Sanjeevi is killed by Malayappan.)','scene-stage-direction','Malayappan kills Sanjeevi.',None,[])
},
44:{
 'open':('stage-direction',68,'(Puja is going on in the temple. Kumaran arrives with the will.)','scene-stage-direction','Temple puja; Kumaran arrives with will.',None,[]),
 'attack':('stage-direction',68,'(Kumaran is attacked by the people—in the temple.)','scene-stage-direction','Crowd attacks Kumaran in temple.',None,[])
},
45:{
 'assault':('stage-direction',68,'(Malayappan is humiliating Meenu—while Meenu is being assaulted in the house—Kumaran arrives.)','scene-stage-direction','Opening assault and Kumaran arrival.',None,[]),
 'carry':('stage-direction',68,'(Kumaran carries Meenu outside.)','scene-stage-direction','Kumaran takes Meenu out.',None,[]),
 'fight':('stage-direction',70,"(A fight breaks out between them. The priest standing outside runs away. Kumaran carries the child and comes out. Malayappan, struck by Kumaran, collapses. This is Kumaran's last breath.)",'scene-stage-direction','Fight, child rescue and fatal collapse.',None,[]),
 'meenu':('stage-direction',70,'(Meenu enters.)','scene-stage-direction','Meenu comes to dying Kumaran.',None,[]),
 'death':('stage-direction',71,'(Kumaran loses his life.)','scene-stage-direction','Kumaran dies.',None,[]),
 'final':('dialogue',71,'“Is this the end for all the noble people who reform the world?”\n\nWho will reshape this?','source-unlabelled-speech','Source-unlabelled block `naam-s045-u001`.',None,['The closing rhetorical questions have no explicit source speaker label or delimiter; no speaker identity is inferred.']),
 'title':('written-text',71,'Naam (We)','closing-title','Closing source title `நாம்`.',None,['Retained as closing title text; no synthetic “Scene ends” prose is added.'])
}
}

PERF005=[
 ('role-cue',59,'7    குமரன், கிராமவாசிகள்','7    Kumaran, villagers'),
 ('lyric-line',59,'புதியதோர் பாதை வகுப்போம்—நாம்—கெட்ட','Let us lay out a new path—we—'),
 ('lyric-line',59,'போரிடும் பாதையை சாய்ப்போம் நாம்......','let us bring down the evil path of conflict......'),
 ('lyric-line',59,'நித்தம் உழைத்தே உயர்வோம் நாம்—','Let us rise through daily labour—'),
 ('lyric-line',59,'நெறி தவறாமல் வாழ்வோம் நாம்—','Let us live without straying from the path—'),
 ('lyric-line',59,'அருஞ்ஞானப் பாரம் வெளியையே—நல்','The burden of rare wisdom, out in the field—at the good'),
 ('lyric-line',59,'அறிவாகும் ஏர் முனையிலே...','ploughshare that is knowledge...'),
 ('lyric-line',59,'அறிவாகும் ஏர் முனையிலே...','at the ploughshare that is knowledge...'),
 ('lyric-line',59,'விஞ்ஞானப் பேரறிவினில்—உழுதே','ploughing with the great knowledge of science—'),
 ('lyric-line',59,'மெய்ஞ்ஞானம் காண்பவர்கள் நாம்!','we are those who discover true wisdom!'),
 ('role-cue',59,'8    மாத்திரை','8    Mathirai'),
 ('lyric-line',59,'வாழ்க வாழ்க வாழ்க வாழ்கவே','Long live, long live, long live, long live!'),
 ('lyric-line',59,'அருமை மிகுந்த எங்கள் அறிஞர்','Our precious scholar,'),
 ('lyric-line',59,'அண்ணா வாழ்கவே','long live Anna!'),
 ('lyric-line',59,'குமர அண்ணா வாழ்கவே.','Long live brother Kumara!'),
 ('lyric-line',59,'பெருமை பேசும் மனிதரெல்லாம்','All the men who speak of greatness,'),
 ('lyric-line',59,'எதற்கெடுத்தாலும் எருமை போல','at everything, like buffaloes,'),
 ('lyric-line',59,'தலையசைப்பதை உரிமைக்காக','their head-nodding—for rights,'),
 ('lyric-line',59,'எதிர்த்து நிற்கும்','he stands opposing it;'),
 ('lyric-line',59,'அண்ணா வாழ்கவே','long live Anna!'),
 ('lyric-line',59,'எங்கள் அண்ணா வாழ்கவே.','Long live our Anna!'),
 ('lyric-line',60,'புழுவாகத் துடிக்கின்ற ஏழை','The poor man writhing like a worm,'),
 ('lyric-line',60,'கழுகாகப் பறக்கின்ற சீமான்—இந்தப்','the lord who flies like an eagle—these'),
 ('lyric-line',60,'பொல்லாத பேதங்கள் எல்லாம்','wicked distinctions, all of them,'),
 ('lyric-line',60,'இல்லாத பொன்னுடைமைச் செய்தார்—அந்த','he made into a golden commonwealth without them—that'),
 ('lyric-line',60,'அண்ணா வாழ்கவே','Anna, long live!'),
 ('lyric-line',60,'குமர அண்ணா வாழ்கவே-','Long live brother Kumara—'),
 ('lyric-line',60,'எலியாக வாழ்கின்ற விதவை','the widow who lives like a mouse,'),
 ('lyric-line',60,'புலியாக தருகின்ற இளமை','youth that gives like a tiger,'),
 ('lyric-line',60,'புலியாக பாய்கின்ற பழமை','old tradition that pounces like a tiger,'),
 ('lyric-line',60,'மலிவாகப் போன இக்கொடுமை','this cruelty that has become commonplace,'),
 ('lyric-line',60,'மாற்றிடும் அண்ணா வாழ்கவே !','long live the Anna who will change it!'),
 ('lyric-line',60,'குமர அண்ணா வாழ்கவே.','Long live brother Kumara!'),
 ('lyric-line',60,'சில சில இடங்களில் பணத்தோட்டம்—அது','In a few places, `Panathottam`—that'),
 ('lyric-line',60,'செல்வக் குமரி...கோட்டம்! இப்படிப்','`Selvak Kumari... Kottam!` Like this,'),
 ('lyric-line',60,'பலபல கருத்துக்கள் சொல்லும் தேனாறு','a honey-stream speaking many, many ideas,'),
 ('lyric-line',60,'பகுத்தறிவூட்டும் லட்சிய வரலாறு—','an idealist history that nourishes rationalism—'),
 ('lyric-line',60,'அண்ணா வாழ்கவே','long live Anna!'),
 ('lyric-line',60,'குமர அண்ணா வாழ்கவே.','Long live brother Kumara!')
]
PERF006=[
 ('lyric-line',64,'எதையும் தாங்கும் இதயம் வேண்டும்','A heart is needed that can bear anything,'),
 ('lyric-line',64,'பகையும் பழியும் பாம்பெனத் தீண்டும்—உலகில்','in this world where enmity and blame sting like snakes—'),
 ('lyric-line',64,'எதையும் தாங்கும் இதயம் வேண்டும்','a heart is needed that can bear anything.'),
 ('lyric-line',64,'சிறையா வதையா இன்னும்........ (எதையும்)','Prison or torture, what more........ (anything)'),
 ('lyric-line',64,'சாக்ரடீஸ் வாழ்வினைப் பார்','Look at the life of Socrates;'),
 ('lyric-line',64,'சாகாத காந்தி முடிவையுமே பார்','look too at the end of the undying Gandhi.'),
 ('lyric-line',64,'வேதனையாலே வீழாதே','Do not fall because of pain;'),
 ('lyric-line',64,'சோதனையாலே வாடாதே—நீ வாடாதே','do not wither under trials—you, do not wither;'),
 ('lyric-line',64,'சோதனையாலே வாடாதே—வரும்...... (எதையும்)','do not wither under trials—whatever comes...... (anything)'),
 ('lyric-line',64,'தேனினும் வாழ்வே தேளாய் மாறும்','Life sweeter than honey can turn into a scorpion;'),
 ('lyric-line',64,'போர்முனைச் சாவே பொதுவாழ்வில் இன்பம்','death at the battlefront is joy in public life.'),
 ('lyric-line',64,'ஆணவம் சீறலாம், ராணுவம் பாயலாம்','Arrogance may rage, the army may charge;'),
 ('lyric-line',64,'சீற்றத்தைக் கண்டு சிதறாதே—உளம் சிதறாதே','do not scatter before fury—let the heart not shatter;'),
 ('lyric-line',64,'தூற்றலைக் கேட்டுத் துவளாதே—பகை.........','do not wilt on hearing slander—enmity.........'),
 ('lyric-line',64,'(எதையும்)','(anything)')
]

ORDER={
36:['x:loc','d001','d002','d003','d004','x:cue','p:005'],
37:['x:all'],
38:['d001','d002','d003','d004','d005','x:leave1','d006','d007','d008','d009','d010','d011','x:dismantle','d012','d013','d014','d015','d016','x:leave2'],
39:['d001','d002','x:change','x:loc']+[f'd{i:03d}' for i in range(3,13)]+['x:arrest','x:protest','d013','x:cue','p:006','x:vanakkam','x:after'],
40:[f'd{i:03d}' for i in range(1,9)],
41:['x:opening','d001','x:release']+[f'd{i:03d}' for i in range(2,10)]+['x:letter','d010','d011','x:take'],
42:[f'd{i:03d}' for i in range(1,8)]+['x:run'],
43:['x:loc','d001','d002','d003','x:seize','x:come','d004','d005','d006','x:kill'],
44:['x:open','d001','x:attack'],
45:['x:assault','d001','x:carry']+[f'd{i:03d}' for i in range(2,13)]+['x:fight','d013','x:meenu']+[f'd{i:03d}' for i in range(14,19)]+['x:death','x:final','x:title']
}

def d_unit(n,di,uid,src):
    r=src[di-1]; assert r['id']==f'naam-s{n:03d}-d{di:03d}'
    return {'id':uid,'kind':'dialogue','status':'verified','target_language':'en','scene_id':f'naam-s{n:03d}','scene_ordinal':n,'source_scene_number':n,
      'source':{'source_path':dialogue_path(n),'canonical_scene_path':scene_path(n),'source_record_id':r['id'],'source_occurrence_id':None,'source_locator':None,'speaker_label':r['speaker_label'],'speaker_label_origin':'source-explicit','source_delimiter':r['source_delimiter'],'page_provenance':r['page_provenance']},
      'translation':{'english_text':D[n][di-1],'mode':'prose-faithful','notes':list(NOTES.get((n,di),[]))}}

def x_unit(n,key,uid):
    kind,pages,eng,lk,desc,occ,notes=X[n][key]
    return {'id':uid,'kind':kind,'status':'verified','target_language':'en','scene_id':f'naam-s{n:03d}','scene_ordinal':n,'source_scene_number':n,
      'source':{'source_path':scene_path(n),'canonical_scene_path':scene_path(n),'source_record_id':None,'source_occurrence_id':occ,'source_locator':{'kind':lk,'ordinal':1,'description':desc},'speaker_label':None,'speaker_label_origin':None,'source_delimiter':None,'page_provenance':provenance(pages)},
      'translation':{'english_text':eng,'mode':'prose-faithful','notes':notes}}

def song_unit(n,uid,pid,lines,pages):
    lm=[{'ordinal':i+1,'kind':k,'pdf_page':p,'tamil':ta,'english':en} for i,(k,p,ta,en) in enumerate(lines)]
    notes=[f'Translated only from source-visible Tamil retained in `{pid}`.','Item-level authorship remains unresolved; the broad PDF-4 credit is not promoted.']
    if pid=='naam-perf-005':
        notes += ['The two source-numbered role blocks remain one retained performance occurrence; role cues 7 and 8 are mapped explicitly.', 'Source-irregular or title-like forms such as `அருஞ்ஞானப் பாரம்`, `புலியாக தருகின்ற இளமை`, `பணத்தோட்டம்`, and `செல்வக் குமரி...கோட்டம்` are translated conservatively or transliterated rather than repaired.']
    if pid=='naam-perf-006':
        notes += ['The source refrain cue `(எதையும்)` is retained in line mapping; no external lyric or soundtrack wording is imported.']
    return {'id':uid,'kind':'song','status':'verified','target_language':'en','scene_id':f'naam-s{n:03d}','scene_ordinal':n,'source_scene_number':n,
      'source':{'source_path':f'works/naam/songs/records/{pid}.md','canonical_scene_path':scene_path(n),'source_record_id':None,'source_occurrence_id':pid,'source_locator':{'kind':'retained-performance-record','ordinal':1,'description':'Complete source-visible retained performance body.'},'speaker_label':None,'speaker_label_origin':None,'source_delimiter':None,'page_provenance':provenance(pages)},
      'translation':{'english_lines':[en for _,_,_,en in lines],'line_map':lm,'mode':'semantic-poetic-source-faithful','notes':notes}}

records=[]
for n in range(36,46):
    src=rj(W/f'dialogues/records/scene-{n:03d}.json')
    assert len(src)==EXPECTED[n]==len(D.get(n,[]))
    units=[]
    for token in ORDER[n]:
        uid=f'naam-en-s{n:03d}-u{len(units)+1:03d}'
        if token.startswith('d'): units.append(d_unit(n,int(token[1:]),uid,src))
        elif token.startswith('x:'): units.append(x_unit(n,token[2:],uid))
        elif token=='p:005': units.append(song_unit(36,uid,'naam-perf-005',PERF005,[59,60]))
        elif token=='p:006': units.append(song_unit(39,uid,'naam-perf-006',PERF006,64))
        else: raise AssertionError(token)
    rec={'work_id':'naam','target_language':'en','scene_id':f'naam-s{n:03d}','scene_ordinal':n,'source_scene_number':n,'scene_status':'verified','unit_count':len(units),'units':units}
    wj(R/f'scene-{n:03d}.json',rec); records.append(rec)

batch_units=sum(r['unit_count'] for r in records)
batch_links=sum(1 for r in records for u in r['units'] if u['source']['source_record_id'])
unlabelled=[u['id'] for r in records for u in r['units'] if u['kind']=='dialogue' and u['source']['source_record_id'] is None]
occ=[]; maps=0; cross=[]; written=[]
for r in records:
    for u in r['units']:
        o=u['source']['source_occurrence_id']
        if o and o not in occ: occ.append(o)
        if o in ('naam-perf-005','naam-perf-006'): maps += len(u['translation'].get('line_map',[]))
        if len(u['source']['page_provenance'])>1: cross.append(u['id'])
        if u['kind']=='written-text': written.append(u['id'])
assert batch_links==84
assert batch_units==117
assert unlabelled==['naam-en-s045-u024']
assert occ==['naam-perf-005','naam-perf-006']
assert maps==53
assert cross==['naam-en-s036-u007','naam-en-s039-u017','naam-en-s041-u002','naam-en-s045-u013','naam-en-s045-u022']
assert written==['naam-en-s041-u012','naam-en-s045-u025']

scene_results=[]
for r in records:
    n=r['source_scene_number']; linked=sum(1 for u in r['units'] if u['source']['source_record_id']); unl=sum(1 for u in r['units'] if u['kind']=='dialogue' and u['source']['source_record_id'] is None)
    perfs=[]
    for u in r['units']:
        o=u['source']['source_occurrence_id']
        if o and o not in perfs: perfs.append(o)
    scene_results.append({'scene_id':r['scene_id'],'source_scene_number':n,'translation_units':r['unit_count'],'immutable_dialogue_records_expected':EXPECTED[n],'immutable_dialogue_records_linked':linked,'missing_dialogue_links':0,'duplicate_dialogue_links':0,'source_unlabelled_speech_units':unl,'performance_occurrences_linked':perfs,'written_text_units':sum(1 for u in r['units'] if u['kind']=='written-text')})

qa={'work_id':'naam','phase':'english-translation-batch-036-045-qa','status':'PASS','source_scenes':list(range(36,46)),'translation_units':batch_units,'immutable_dialogue_records_expected':84,'immutable_dialogue_records_linked':84,'dialogue_coverage':'84/84 exactly once','missing_dialogue_links':0,'duplicate_dialogue_links':0,'exact_tamil_speaker_labels_preserved':True,'source_delimiters_preserved_as_metadata':True,'source_unlabelled_speech_units':1,'source_unlabelled_unit_ids':unlabelled,'inferred_unlabelled_speakers':0,'performance_occurrences_expected':['naam-perf-005','naam-perf-006'],'performance_occurrences_linked':['naam-perf-005','naam-perf-006'],'performance_coverage':'2/2','performance_line_cue_mappings':53,'naam_perf_005_authorship':'unresolved-item-level','naam_perf_006_authorship':'unresolved-item-level','written_text_units':written,'cross_page_translation_units':cross,'scene_results':scene_results,'authorship_status_changed_by_translation':False,'external_or_unprinted_lyrics_imported':False,'canonical_tamil_modified':0,'scene_text_modified':0,'dialogue_records_modified':0,'character_entity_mappings_modified':0,'song_source_records_modified_by_translation':0,'translation_scene_layer_complete':True,'whole_work_translation_reconciliation_pending':True,'next_gate':'whole-work English translation reconciliation and closure QA before reader/export'}
wj(T/'batch-036-045-qa.json',qa)

idx=rj(T/'index.json')
assert idx['status']=='in-progress-verified-through-scene-035' and idx['verified_scenes']==35
assert idx['translation_units_verified']==680 and idx['immutable_dialogue_links_verified']==506
assert idx['source_unlabelled_speech_units_verified']==19 and idx['retained_performance_records_translated']==5 and idx['song_line_cue_mappings_verified']==84
idx['status']='scene-layer-complete-verified-45-of-45-whole-work-reconciliation-next'
idx['verified_scenes']=45
idx['verified_scene_ids']=[f'naam-s{i:03d}' for i in range(1,46)]
idx['translation_units_verified']=680+batch_units
idx['immutable_dialogue_links_verified']=590
idx['stage_or_narrative_units_verified']=idx.get('stage_or_narrative_units_verified',146)+26
idx['performance_cue_units_verified']=idx.get('performance_cue_units_verified',4)+2
idx['song_units_verified']=idx.get('song_units_verified',4)+2
idx['retained_performance_records_translated']=7
idx['translated_performance_record_ids']=['naam-perf-007','naam-perf-001','naam-perf-002','naam-perf-003','naam-perf-004','naam-perf-005','naam-perf-006']
idx['song_line_cue_mappings_verified']=84+maps
idx['source_unlabelled_speech_units_verified']=20
idx['cross_page_translation_units']=list(dict.fromkeys(idx.get('cross_page_translation_units',[])+cross))
idx['written_text_units_verified_final_batch']=2
idx['batch_036_045_review']='BATCH_036_045_REVIEW.md'
idx['batch_036_045_qa']='batch-036-045-qa.json'
idx['iteration_scene_batch_size']=10
idx['whole_work_reconciliation_status']='ready-next'
idx['next_activity']=NEXT
wj(T/'index.json',idx)
assert idx['translation_units_verified']==797
assert idx['song_line_cue_mappings_verified']==137

rows='\n'.join(f"| {r['source_scene_number']} | {r['translation_units']} | {r['immutable_dialogue_records_linked']}/{r['immutable_dialogue_records_expected']} | {r['source_unlabelled_speech_units']} | {', '.join(r['performance_occurrences_linked']) or '0'} | {r['written_text_units']} |" for r in scene_results)
review=f'''# நாம் — English final batch review / scenes 36–45

**Batch:** source scenes `காட்சி 36`–`காட்சி-45`  
**Status:** **VERIFIED — FINAL 10-SCENE BATCH**  
**Units:** **{batch_units}**  
**Immutable dialogue links:** **84/84 exactly once**

## Review result

This final 10-scene iteration translates and verifies source-numbered scenes 36–45 in exact source order. All **84/84** remaining immutable dialogue records are linked exactly once, bringing cumulative immutable-dialogue linkage to **590/590**. The single closing source-unlabelled rhetorical block remains deliberately unassigned; no speaker identity is manufactured.

Both remaining retained performance structures are translated source-only. `naam-perf-005` preserves its two source-numbered role blocks (`7    குமரன், கிராமவாசிகள்` and `8    மாத்திரை`) across PDF 59–60. `naam-perf-006` preserves the PDF-64 `பின்னணிப் பாடல்`. Together they add **53** Tamil→English role/lyric mappings. Both remain **unresolved at item-level authorship**; the broad PDF-4 credit is not promoted.

Scene 41 preserves the `கடிதத்தில் :-` passage as **written text**, not a speaker-labelled dialogue. Scene 43 preserves Sanjeevi's lone `:` delimiter exactly as metadata. Scene 45 preserves both long cross-page Kumaran speeches as single logical dialogue units and retains the final rhetorical questions unlabelled. The closing `நாம்` is represented as written closing-title text; no synthetic “Scene ends” prose is introduced.

## Scene counts

| Scene | Units | Immutable dialogue links | Unlabelled speech | Performance links | Written text |
|---|---:|---:|---:|---|---:|
{rows}
| **Batch** | **{batch_units}** | **84/84** | **1** | **2 unique records** | **2** |

## Fidelity decisions

- Scene 36 keeps reform/common-service rhetoric and treats the two numbered poetic blocks only through retained `naam-perf-005`.
- Scene 37 remains a legitimate zero-dialogue scene: the storm, child and blinding action is one verified stage-direction unit, with no manufactured dialogue.
- Scene 38 preserves reading-room/school suppression, frog-in-a-well satire and colloquial authority speech without smoothing the politics.
- Scene 39 preserves the anti-violence argument, question-mark/intellectual/sickle wordplay, arrest speech and source-only background song `naam-perf-006`.
- Scene 40 preserves the propaganda/Kali Baba satire and revenue-sharing scheme without adding modern explanatory commentary.
- Scene 41 keeps the judge's cross-page verdict as one logical dialogue unit, `காலணா` as the historical quarter-anna denomination, the em-dash Jeevanandar turn exactly as metadata, `உன்மீனு` as the exact anomalous source label, and the letter as written text.
- Scene 44 leaves the difficult verified `காமவினை` as transliterated `kamavinai` rather than silently repairing Tamil.
- Scene 45 preserves the hunter/tiger analogy, revolutionary history rhetoric, `பத்தரை மாத்துத் தங்கம்` purity image, the rights/death-charter contrast, self-respect/rationalism closing, and source-unlabelled final questions.

## Integrity checks

- expected / linked immutable dialogue records: **84 / 84**;
- cumulative immutable dialogue linkage after this batch: **590 / 590**;
- missing / duplicate immutable links in batch: **0 / 0**;
- source-unlabelled speech in batch: **1**, inferred speakers: **0**;
- performance records expected / linked: **2 / 2 — `naam-perf-005`, `naam-perf-006`**;
- new performance mappings: **53**;
- cumulative performance records translated: **7/7**;
- cumulative performance line/cue mappings: **137**;
- source-local chant remains **1 unit / 16 mappings** and is not promoted into the seven-record performance inventory;
- new cross-page units: **5 — {', '.join(cross)}**;
- written-text units in this batch: **2 — {', '.join(written)}**;
- authorship upgrades: **0**;
- external/unprinted lyric imports: **0**;
- canonical Tamil / scene / dialogue / character / song-source modifications: **0 / 0 / 0 / 0 / 0**.

## Cumulative English scene-layer checkpoint

After scenes 1–45: **45/45 source scenes**, **797 verified English units**, **590/590 immutable dialogue links**, **20 source-unlabelled speech units retained without inferred labels**, **7/7 performance records translated**, **137 Tamil→English song/performance line-cue mappings**, plus **1 source-local chant / 16 chant mappings**.

The **scene-sharded translation layer is complete**, but final English status is intentionally not promoted to `complete-verified` until whole-work reconciliation checks all 45 scenes together for duplicate source ownership, full unit ordering, cross-page provenance, unlabelled speech, performance/chant disposition, written text, placeholder leakage and upstream integrity.

## Exact next activity

{NEXT}
'''
wt(T/'BATCH_036_045_REVIEW.md',review)

# Translation README
p=T/'README.md'; s=rt(p)
s=re.sub(r'\*\*Status:\*\* \*\*.*?\*\*',"**Status:** **scene layer 45/45 verified; whole-work reconciliation ready-next**",s,count=1)
s=re.sub(r'## Next batch\n\n.*?(?=\n##|\Z)',f"## Next gate\n\n{NEXT}\n",s,flags=re.S)
if '## Verified final batch — scenes 36–45' not in s:
    s += f'''\n## Verified final batch — scenes 36–45\n\n- source scenes: **10 / scenes 36–45**;\n- units: **117**;\n- immutable dialogue links: **84/84**; cumulative **590/590**;\n- source-unlabelled speech: **1 / inferred speakers 0**; cumulative **20**;\n- performance occurrences: **2/2 — `naam-perf-005`, `naam-perf-006`**; cumulative **7/7**;\n- new performance mappings: **53**; cumulative **137**;\n- written text: **2 units**;\n- upstream rewrites: **0**.\n\nThe scene-sharded English layer is **45/45 complete**. Whole-work translation reconciliation must PASS before final `complete-verified` status or reader/export generation.\n'''
wt(p,s)

# Work metadata
p=W/'metadata.yaml'; s=rt(p)
for pat,repl in [
 (r'(?m)^  english_translation: .+$','  english_translation: scene-layer-complete-verified-45-of-45-whole-work-reconciliation-next'),
 (r'(?m)^  english_translation_verified_scenes: \d+$','  english_translation_verified_scenes: 45'),
 (r'(?m)^  english_translation_unit_count: \d+$','  english_translation_unit_count: 797'),
 (r'(?m)^  english_dialogue_links_verified: \d+$','  english_dialogue_links_verified: 590'),
 (r'(?m)^  english_performance_records_translated: \d+$','  english_performance_records_translated: 7'),
 (r'(?m)^  english_song_line_cue_mappings_verified: \d+$','  english_song_line_cue_mappings_verified: 137')]: s=re.sub(pat,repl,s,count=1)
if '  english_whole_work_reconciliation:' in s:
    s=re.sub(r'(?m)^  english_whole_work_reconciliation: .+$','  english_whole_work_reconciliation: ready-next',s,count=1)
else:
    anchor='  english_song_line_cue_mappings_verified: 137'; s=s.replace(anchor,anchor+'\n  english_whole_work_reconciliation: ready-next',1)
s=re.sub(r'(?m)^next_action:.*$','next_action: '+json.dumps(NEXT,ensure_ascii=False),s,count=1)
wt(p,s)

# Work README
p=W/'README.md'; s=rt(p)
s=re.sub(r'- English translation: \*\*.*?\*\*; reader / Reading Room: \*\*not-started\*\*\.',"- English translation: **45/45 SCENE LAYER VERIFIED — 797 units / 590/590 dialogue links / 7 of 7 performance records / 137 performance mappings / 1 chant (16 mappings); whole-work reconciliation READY-NEXT**; reader / Reading Room: **blocked until reconciliation PASS**.",s,count=1)
s=re.sub(r'\*\*Next:\*\* .*?(?=\n|$)','**Next:** '+NEXT,s,count=1)
if '## English scenes 36–45 final-batch checkpoint' not in s:
    s += f'''\n\n## English scenes 36–45 final-batch checkpoint\n\n- English scene layer: **45/45 VERIFIED**;\n- cumulative units: **797**;\n- immutable dialogue links: **590/590**;\n- source-unlabelled speech retained without inferred labels: **20**;\n- translated performance records: **7/7**;\n- performance line/cue mappings: **137**;\n- source-local chant: **1 / 16 mappings**;\n- whole-work reconciliation: **READY-NEXT**;\n- closed upstream-layer changes: **0**.\n\n**Next:** {NEXT}\n'''
wt(p,s)

# Next prompt
wt(W/'NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. **Live `main` is authoritative.**\n\nCanonical Tamil is **67/67 COMPLETE-VERIFIED**; scenes **45/45 COMPLETE-VERIFIED**; dialogue index **590 immutable records / QA PASS**; character/entity layer **28 entities / 45/45 labels / 590/590 records / QA PASS**; song/performance gate **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED**.\n\nEnglish scene-sharded translation is **45/45 VERIFIED**: **797 units**, **590/590 immutable dialogue links**, **20 source-unlabelled speech units with 0 inferred speaker labels**, **7/7 retained performance records translated**, **137 performance line/cue mappings**, and **1 source-local chant / 16 chant mappings**.\n\nImportant: **do not yet label the whole English phase `complete-verified`**. Whole-work English reconciliation is **READY-NEXT** and must PASS before reader/export generation.\n\n`naam-perf-001` retains the specific source attribution **பாரதியார்**. The other six retained performance records remain unresolved at item level; translation has made **0 authorship upgrades**.\n\nThe scene-34 villagers' street-play remains a distinct **chant**, not a new `naam-perf-*` record. Scene 41 `கடிதத்தில் :-` remains **written text**, not a speaker. Scene 41 `ஜீவானந்தர் —` keeps its source em dash; `உன்மீனு` remains the exact source label. Scene 45's final rhetorical questions remain source-unlabelled.\n\nCurrent English files include `translations/BATCH_036_045_REVIEW.md`, `translations/batch-036-045-qa.json`, and `translations/records/scene-001.json` through `scene-045.json`.\n\nDo not alter closed Tamil or structured source layers except for later direct source-supported corrections.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# Project handover
p=W/'PROJECT_HANDOVER.md'; s=rt(p); tag='## English scenes 36–45 final-batch checkpoint'
if tag not in s:
    s += f'''\n\n{tag}\n\n- English scene layer: **45/45 VERIFIED**;\n- cumulative units: **797**;\n- immutable dialogue links: **590/590**;\n- source-unlabelled speech retained: **20 / inferred labels 0**;\n- performance records translated: **7/7**;\n- performance line/cue mappings: **137**;\n- scene-local chant: **1 / 16 mappings**;\n- whole-work English reconciliation: **READY-NEXT**;\n- upstream source-layer changes caused by English: **0**.\n\n## Current exact next activity\n\n> **{NEXT}**\n'''
wt(p,s)

# Data mirror
p=Path('data/works.json'); data=rj(p); n=next(x for x in data if x.get('id')=='naam'); sd=n.setdefault('structured_derivatives',{})
sd.update({'english_translation':'scene-layer-complete-verified-45-of-45-whole-work-reconciliation-next','english_translation_verified_scenes':45,'english_translation_units':797,'english_dialogue_links_verified':590,'english_source_unlabelled_speech_units':20,'english_performance_records_translated':7,'english_song_line_cue_mappings_verified':137,'english_chant_units_verified':1,'english_chant_line_cue_mappings_verified':16,'english_iteration_scene_batch_size':10,'english_whole_work_reconciliation':'ready-next','english_translation_index_path':'works/naam/translations/index.json'})
n['next_action']=NEXT; wj(p,data)

# Root and repository-wide mirrors
p=Path('README.md'); s=rt(p)
s=re.sub(r'- English translation: \*\*.*?\*\*\.',"- English translation: **45/45 scene layer VERIFIED — 797 units / 590/590 dialogue links / 7 of 7 performance records / 137 mappings / 1 chant; whole-work reconciliation READY-NEXT**.",s,count=1)
s=re.sub(r'\*\*Next:\*\* .*?(?=\n|$)','**Next:** '+NEXT,s,count=1)
mark='<!-- Naam English scenes 36-45 current -->'
if mark not in s: s += f'''\n\n{mark}\n**Naam current English checkpoint:** **45/45 source scenes VERIFIED**, **797 units**, **590/590 immutable dialogue links**, **7/7 performance records translated**, **137 performance mappings**, **1 source-local chant / 16 mappings**, **whole-work reconciliation READY-NEXT**, **0 upstream rewrites**. **Next:** {NEXT}\n'''
wt(p,s)
for p in [Path('docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'),Path('docs/STATUS_CONSISTENCY_AUDIT.md')]:
    s=rt(p); mark='<!-- Naam English scenes 36-45 current -->'
    if mark not in s: s += f'''\n\n{mark}\n**Naam English scenes 36-45 current:** scene-sharded English **45/45 verified / 797 units / 590/590 dialogue links / 7 of 7 performances / 137 performance mappings / 1 chant (16 mappings)**; source-unlabelled speech remains unassigned; whole-work English reconciliation **READY-NEXT**; upstream rewrites **0**. **Next:** {NEXT}\n'''
    wt(p,s)

print(json.dumps({'status':'PASS','scenes':'36-45','batch_units':batch_units,'batch_dialogue_links':batch_links,'batch_unlabelled':len(unlabelled),'performance_records':['naam-perf-005','naam-perf-006'],'performance_maps_added':maps,'cumulative_scenes':45,'cumulative_units':797,'cumulative_dialogue_links':590,'cumulative_performance_records':'7/7','cumulative_performance_maps':137,'next':'whole-work English reconciliation'},ensure_ascii=False,indent=2))
