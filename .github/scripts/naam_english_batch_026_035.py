from pathlib import Path
import json, re

W = Path('works/naam')
T = W / 'translations'
R = T / 'records'

NEXT = (
    "Translate and verify source-numbered scenes 36–45 as the next 10-scene English batch. "
    "Preserve exact Tamil speaker labels and source delimiters as metadata; link every explicitly labelled utterance to its immutable dialogue ID exactly once; "
    "keep source-unlabelled speech unassigned; preserve source order, page provenance, cross-page units, chants and stage/narrative ownership; "
    "translate only source-visible song/performance text authorized by the reconciled seven-record song/performance layer, including `naam-perf-005` in/after scene 36 and `naam-perf-006` in scene 39, both with unresolved item-level authorship; "
    "do not alter closed Tamil or structured source layers. Continue with 10 source scenes per iteration; this is the final 10-scene translation batch."
)

def rt(p): return Path(p).read_text(encoding='utf-8')
def wt(p, s): Path(p).parent.mkdir(parents=True, exist_ok=True); Path(p).write_text(s, encoding='utf-8')
def rj(p): return json.loads(rt(p))
def wj(p, d): wt(p, json.dumps(d, ensure_ascii=False, indent=2) + '\n')

def scene_path(n): return f'works/naam/scenes/scene-{n:03d}.md'
def dialogue_path(n): return f'works/naam/dialogues/records/scene-{n:03d}.json'

# Immutable-dialogue English in exact record order.
D = {
26: [
    "Gnanam! Gnanam! Did you hear the happy news? Kumaran is finished... burned with his house and reduced to ashes."
],
27: [
    "Kumaran...",
    "Meenu... Meenu... Meenu...",
    "Hmm...... you told tales of love, love... what will you do now? There—whose love song is that we hear?",
    "Appa... what I did was wrong... forgive me, Appa...",
    "Don't cry, Prema... I struggled only because I wanted you to be happy.",
    "Appa... will he survive?",
    "Looking at you only makes me laugh.",
    "Looking at him makes me feel pity.",
    "Pity! If they had looked at pity, many frogs could never have seen mansions and lofty towers! Look at Malayappan! How did he get this luxuriant life? Because he never even thought of pity! Defeat is the first step laid toward victory! If you are to get Kumaran, Kumaran must forget Meenu. Meenu thinks Kumaran is dead.... We must not let Kumaran outside! No one else must know Kumaran is alive! Understand? At least in this, be careful!",
    "Ayyayyo...... what will happen to the puppy, sir?",
    "I'm telling you firmly... don't come to work anymore.",
    "The puppy will die, sir.",
    "Go away properly!",
    "If the puppy has to go, you must give one month's notice, sir!",
    "Say you don't like me! Don't say you don't trust me!",
    "Say you don't like me! Don't say you don't trust me! Did I give cholera medicine to a fever patient? Did I give diarrhoea medicine to a cholera patient? I know my work too! I'll start a rival hospital! Not one patient will come to you! You'll have to become the patient yourself! Doctor Sanjeevi, look forward soon to Mathirai Progressive Hospital!",
    "Poor Mathirai, Appa!",
    "I already told you about pity... Even Mathirai must not know Kumaran is alive! Now think... how completely one must forget pity!"
],
28: [
    "How did you kill his life? Ruinous fire... sacrificial fire... couldn't you at least have shown his charred corpse to my eyes? Was that much your hunger? Aunt... your beloved son is gone... he will never return, Aunt... (she cries)"
],
29: [
    "Didn't I send it to you because I thought you'd keep the will safe! Shouldn't you have gone to court with the will; instead you went to him and did my business? Yes... at least now have you kept the will safe?",
    "Will... will... life...!",
    "Yes! Life indeed... where have you kept it;",
    "The will... it must have burned in the fire and turned to ash, doctor!",
    "Look, son... you're lying even to me!",
    "Otherwise it must have fallen into Malayappan's hands.",
    "Prema...!",
    "What is it, Appa!",
    "From now on you must forget Kumaran.",
    "Why, Appa...",
    "Must I say it plainly? From now on he can't even set foot at the zamindar's doorstep! There's no use trusting him anymore! Forget him!",
    "Appa... you give explanations for sin, don't you... I'm ready to commit as many such sins as needed! It is enough if I get him!",
    "(Angrily) Tch...",
    "Aren't we the ones who won't let him go outside...",
    "We won't let him... if, despite us, they happen to meet... you must spread a false story for this.",
    "Propaganda?",
    "Yes! Say Kumaran has turned into a demon. That he roams as a ghost...",
    "Will people believe it if we call a man a demon, Appa?",
    "Many people in this world would have died merely seeing trees and plants move! Tell one woman that Kumaran has turned into a demon! That's enough—the whole world will know!",
    "It came pitch-black, they say! Couldn't see its legs! The watchman shouted, they say! It flew like the wind!"
],
30: [
    "How did this happen?",
    "He suddenly got impatient and loosened the bandage.",
    "Apply this black ointment! Go... go... even after the wound heals, disfigurement is disfigurement.",
    "Kumara, get up...",
    "Why, doctor...",
    "How many days can you suffer like this? I'm going to remove the bandages.",
    "(With delight) I won't forget your help, doctor...!",
    "Ayyo... ayyo...",
    "Kumaran! Don't panic...",
    "Chandala... you've conspired and made me a terrifying man... disfigurement... utter disfigurement... Look at my face! Sinner, I can't even bear to look at myself... why did you torture me? Tell me, cheat... you saw my face before... now look, wretch... why did you have this wicked thought? You are crueler than that fire! Where is my eye? Where is my eye? A milk-soft face... blood runs down that milk-soft face... a face more terrible than a leprosy patient's. You people cannot bear even to look at a crushed flower... who will look at a face charred, flesh torn and hanging in strips? Heartless man... merciless murderer... you could have strangled my throat and killed me... Amma... Amma... look at your Kumaran; look at the cheek you kissed... Amma",
    "Ah... Kumaran... what happened? Let me see your face."
],
31: [
    "Meenu... Meenu ..",
    "Who is it...? Kumaran...",
    "(After examining Meenu's hand) That's right...",
    "What is right...?",
    "Nothing... it's been a long time since this mansion heard a baby's prattle...",
    "Meaning?",
    "Showing little eyes—smiling a tiny smile—dispelling loneliness—speaking Tamil, crawling and playing, a grandson... or granddaughter... is going to be born to you... Meenu... is with child...",
    "You wretch...",
    "Oh God...",
    "It's all his doing.",
    "Chandali! Emblem of disgrace... you have brought scandal to me, who lived with the townspeople bowing before me. Even if I cut you limb from limb, my rage won't cool.",
    "Why... are you trembling? What has happened now?",
    "What else need happen? People of every kind lived bowing to me saying ‘Master, namaskaram’... and you have brought me disgrace... harlot!",
    "I'm not a harlot! I embraced a dream through a man I loved properly. I am growing in my womb the diamond statue he gave me.",
    "Lover... husband... Meenu...",
    "Raging zamindar... I know to whom the throne on which you sit laughing belongs.",
    "I know too, girl.",
    "You became zamindar through a villain's blindfold trick!",
    "All your lover's plans have shattered—gone to embers.",
    "Not to embers—only a dream! That will still hasn't turned to ash!",
    "It hasn't turned to ash? Where is it? Give it...",
    "‘That will still hasn't turned to ash.’ Hmm... come here...",
    "What benefit is there to you in killing Meenu? You can go to jail, that's all!",
    "How do I wipe away this disgrace?",
    "Honour? Disgrace? Do as I tell you...",
    "Tell me, I'm listening...",
    "Tell Meenu that Malayangala is the right place for childbirth—and take her to Malayangala! As soon as the baby is born, kill the baby.",
    "Kill the baby?",
    "Listen and act according to my plan! Once the baby is killed, there'll be no worry.",
    "They say she has the will...",
    "She's only saying that... Even if she does, without Kumaran what can she do with it? Do it without fear! I am here."
],
32: [
    "Don't turn back after dark anymore, man! A demon will strike you.",
    "Yes... yes... and is it some ordinary demon? A demon that knows boxing!...",
    "Hey... Kutti... stick some neem leaves into the cart... the whole village is afraid of the demon...",
    "Yes... what do we do to get rid of this demon?",
    "If we perform puja at the Amman temple and pray, it'll be set right.",
    "Last night it came on our roof and cried koo... koo...!",
    "Must have been an owl.",
    "Hey... it came down with a rustling racket and went away, man...",
    "Yes... yes... could be. Even I went out last night to get some air. Something black... heavy... stout came along! My whole body broke into a sweat! I watched... it passed! I followed it... it turned toward the doctor's house! Why is it going toward the doctor's house? Is the demon unwell... did something happen on the way... why is it going toward the doctor's house? I wouldn't leave it... I followed—Komalam from the house at the end, you know... that one... it knocked on her door! I watched... right... something was going to happen...... Komalam came lifting a lamp. I looked... know who it was? Our Amman temple priest... this fool's friend—Sangaramurthi! Get lost, you wastrels!",
    "Hey... are you mocking me?",
    "One fellow will vomit black! Another, seeing it, will say he vomited crow-coloured! Another will say... he vomited a crow... a crow!",
    "Hey! Don't believe this fellow's talk—the village will be ruined.",
    "Believe this fellow's talk—the village will prosper! Get lost!"
],
33: [
    "Doctor! I hope coming to this Malayangala isn't some trick to kill the baby...",
    "Shiva, Shiva! Infanticide... saving lives is my profession... would I even think of that destructive deed?",
    "Brother won't agree to raise the child!",
    "Here... I am here... Prema is here! Like a child born to me!",
    "Whatever... this child is Kumaran's child! Kumaran wasn't blessed to see it......",
    "Hey... he is the ghost, isn't he... that will? Shouldn't someone keep it safely?",
    "It is safe, doctor!",
    "Is it?",
    "Here......! (she gives the will)",
    "Yes... you've brought it in your hand at a time of childbirth; if it falls into your brother's hands it'll be dangerous!",
    "Hmm! No... you keep it safely yourself! Yes... if it is in my medicine box, no one will ever look!",
    "Hey... stop.",
    "Who are you?",
    "Who? You're going to throw this beautiful body into a well and die... don't you have any sense...",
    "Sir... I can't speak!",
    "Don't speak! Come with me! Don't you trust me? Look at this!",
    "Hey... let go of me... I'm determined to die."
],
34: [
    "Hey...... fools! Who is the demon?",
    "This fellow is the demon!",
    "Don't let him go!",
    "This is a demon enslaved to the zamindari! This is a demon (the priest) that deceives the people! Bigger than both is the zamindar demon!",
    "Don't believe his talk!",
    "Believe his talk! The village will prosper! Kumaran isn't a demon ..",
    "Mathirai! What's this quarrel? You prove it yourself.",
    "This man too... neither one thing nor the other. I'll prove it now, watch. (goes)",
    "He's run away...",
    "Ayyo...",
    "Why are you afraid? I am not a ghost! There is no such thing as a ghost! The traits attributed to ghosts roam only in human society! We who lived on a land where warriors moved... we who lived on the soil of rational thinkers... are we to become slaves to mere imaginary tales—to fabricated stories spun by mischief-makers? Lose our reason? Sacrifice our manhood? The one who betrayed his people for spittle-money is a ghost! The hypocrite who made his own life a pleasure-garden is a ghost! The one who lives by cheating and exploiting is a ghost! Friends... think.... Am I the ghost? Is there not even one brave person among you?"
],
35: [
    "Why... Kumara, you look troubled... won't you tell me? If you don't, I'll start spreading ghost stories again.",
    "Will they believe it?",
    "These people will believe anything, man! Even such a great Ramalinga Swami said—there are no ghosts, demons.... did they listen?"
]
}

EXPECTED = {26:1,27:18,28:1,29:20,30:11,31:31,32:13,33:17,34:11,35:3}

NOTES = {
    (27,9): ["`மண்டூகங்கள்` is retained as the source's frog image rather than replacing the satire with a smoother abstraction."],
    (30,3): ["`கருப்பை` is rendered conservatively as a black ointment/medicine from the immediate wound-treatment context; Tamil is unchanged."],
    (30,10): ["The source's harsh self-description, leprosy comparison and repeated bodily imagery are translated directly rather than softened."],
    (31,7): ["The verified source form around `மீனு...கொப்பம்...` is irregular; English gives only the immediate pregnancy sense without repairing Tamil."],
    (32,9): ["The long ghost-story anecdote preserves colloquial rumour, medical satire and the named Sangaramurthi reveal without normalizing source speech."],
    (34,11): ["`எச்சில் பணம்` is kept close as `spittle-money` to retain the source insult instead of silently substituting a modern political term."]
}

# Extra source units in exact scene order.
# kind, page provenance, English text, locator kind, description, occurrence id, notes
X = {
26: {
    'faint': ('stage-direction', 42, '(On hearing this, Meenu faints.)', 'scene-stage-direction', 'Meenu faints after hearing Kumaran is said to be dead.', None, []),
},
27: {
    'loc': ('narrative', 43, "Location: Sanjeevi's house.", 'scene-location', 'Source location line.', None, []),
    'knock': ('stage-direction', 43, '(Mathirai knocks on the door.)', 'scene-stage-direction', 'Mathirai knocks.', None, []),
    'u1': ('dialogue', 44, 'There... looks like Mathirai is the one coming! Stay right here!', 'source-unlabelled-speech', 'Unlabelled block `naam-s027-u001`.', None, ['The source prints no speaker label or delimiter; no speaker identity is assigned.']),
    'open': ('stage-direction', 44, '(Opening the door.)', 'scene-stage-direction', 'Sanjeevi opens the door.', None, []),
    'u2': ('dialogue', 44, "Hey! Mathirai... from today, don't come to work!", 'source-unlabelled-speech', 'Unlabelled block `naam-s027-u002`.', None, ['The source prints no speaker label or delimiter; no speaker identity is assigned.']),
    'leave': ('stage-direction', 44, '[Mathirai leaves.]', 'scene-stage-direction', 'Mathirai leaves.', None, []),
},
28: {
    'loc': ('narrative', 45, "(Location: Kumaran's burned-to-ashes hut.)", 'scene-location', 'Source location parenthetical.', None, []),
    'will': ('stage-direction', 45, '(At this moment Meenu picks up the will lying on the ground.)', 'scene-stage-direction', 'Meenu finds the will.', None, []),
},
29: {
    'loc': ('narrative', 45, "Location: Sanjeevi's house.", 'scene-location', 'Source location line.', None, []),
    'alone': ('stage-direction', 45, '[Sanjeevi and Prema are alone.]', 'scene-stage-direction', 'Sanjeevi and Prema alone.', None, []),
    'after': ('stage-direction', 46, '(After Prema leaves.)', 'scene-stage-direction', 'Prema leaves before the conscience block.', None, []),
    'u1': ('dialogue', 46, '“Prema... love... Prema must hate Kumaran! Meenu... must forget Kumaran. Where is he roaming around like a demon...”', 'source-unlabelled-speech', 'Unlabelled block `naam-s029-u001`.', None, ['Printed as a quoted inner/conscience utterance without an explicit speaker label; metadata remains unassigned.']),
    'conscience': ('narrative', 46, '(This is the physician\'s conscience.)', 'scene-narrative', 'Source parenthetical identifying the preceding text as the physician\'s conscience.', None, []),
    'u2': ('dialogue', 46, 'Hmm... Prema...', 'source-unlabelled-speech', 'Unlabelled block `naam-s029-u002`.', None, ['No source speaker label or delimiter is printed.']),
    'prema': ('stage-direction', 46, '(Prema enters.)', 'scene-stage-direction', 'Prema re-enters.', None, []),
    'u3': ('dialogue', 46, "I spoke in anger...... I don't want to destroy the love you have for Kumaran! If you are to marry Kumaran, Meenu must forget Kumaran. Isn't that so...\n\nIf Kumaran and Meenu suddenly meet...?", 'source-unlabelled-speech', 'Unlabelled block `naam-s029-u003`.', None, ['Context may suggest Sanjeevi, but the source prints no speaker label; no identity is manufactured.']),
    'change': ('stage-direction', 47, '(The scene changes.)', 'scene-stage-direction', 'Internal scene change.', None, []),
    'river': ('narrative', 47, '(Riverbank.)', 'scene-location', 'Riverbank source location.', None, []),
    'rumor': ('stage-direction', 47, '(In this way the women spread the ghost publicity.)', 'scene-stage-direction', 'Women spread the ghost rumour.', None, []),
},
30: {
    'loc': ('narrative', 47, "(Location: the physician's house.)", 'scene-location', 'Source location parenthetical.', None, []),
    'after': ('stage-direction', 47, '(After the visitor leaves, Sanjeevi thinks.)', 'scene-stage-direction', 'Visitor leaves and Sanjeevi thinks.', None, []),
    'u1': ('dialogue', 48, '“How did the wound happen...?”\n\n“He got impatient and loosened the bandage.”', 'source-unlabelled-speech', 'Unlabelled block `naam-s030-u001`.', None, ['Two quoted remembered lines are preserved together exactly as the unlabelled-block audit groups them; no speaker labels are inferred.']),
    'decide': ('narrative', 48, '(The physician decides to remove the bandages placed on Kumaran.)', 'scene-narrative', 'Source parenthetical decision.', None, []),
    'unwrap': ('stage-direction', 48, '(He removes them. As he does, the wound has not healed, and Kumaran cries out, unable to bear the pain.)', 'scene-stage-direction', 'Bandages removed before the wound heals.', None, []),
    'mirror': ('stage-direction', 48, "(Kumaran sees his burned face in a mirror. He screams like a man possessed. Kumaran's face is more terrifying than a tiger's face.)", 'scene-stage-direction', 'Kumaran sees the burned face in a mirror.', None, []),
    'prema': ('stage-direction', 49, '(Prema enters.)', 'scene-stage-direction', 'Prema enters.', None, []),
    'show': ('stage-direction', 49, '(Kumaran shows his face. Prema is shocked.)', 'scene-stage-direction', 'Kumaran reveals the face to Prema.', None, []),
    'u2': ('dialogue', 49, "Prema... look how beautiful your father has made me! Do you love me now? You spun stories about love, love!... you fell at my feet and wailed! Do you love me now? Will you kiss my face? Will you embrace and delight in this wreck? Love me! Love me! The bridegroom asks—do you like your groom? Prema... you won't want me now... you loved only beauty! There is one woman who loves my heart! She is my... Meenu... Meenu... Meenu!", 'source-unlabelled-speech', 'Unlabelled block `naam-s030-u002`.', None, ['Although the surrounding action identifies Kumaran contextually, the printed block has no explicit dialogue label; metadata remains unassigned.']),
    'exit': ('stage-direction', 49, '(Crying “Meenu... Meenu...,” Kumaran leaves the physician\'s house.)', 'scene-stage-direction', 'Kumaran exits shouting for Meenu.', None, []),
},
31: {
    'cue': ('performance-cue', 49, '(Meenu is singing.)', 'performance-cue', 'Source-visible cue for `naam-perf-004`.', 'naam-perf-004', ['Item-level authorship remains unresolved.']),
    'faint': ('stage-direction', 50, '(Meenu sees Kumaran\'s terrible face and faints—Mallayappan arrives. Kumaran stands hidden behind a screen.)', 'scene-stage-direction', 'Meenu faints; Mallayappan arrives; Kumaran hides.', None, []),
    'alone': ('stage-direction', 51, '(Sanjeevi and Mallayappan are alone.)', 'scene-stage-direction', 'Sanjeevi and Mallayappan confer alone.', None, []),
    'hear': ('stage-direction', 52, '(Kumaran hears this.)', 'scene-stage-direction', 'Kumaran overhears the plan.', None, []),
},
33: {
    'loc': ('narrative', 54, '(Location: Malayangala.)', 'scene-location', 'Source location parenthetical.', None, []),
    'give': ('stage-direction', 54, '(Meenu gives the will to the physician.)', 'scene-stage-direction', 'Meenu hands over the will.', None, []),
    'trick': ('stage-direction', 55, '(The physician speaks cunningly and gets the will from Meenu.)', 'scene-stage-direction', 'Sanjeevi secures the will by deception.', None, []),
    'days': ('stage-direction', 55, '(Many days pass.)', 'scene-stage-direction', 'Time passes.', None, []),
    'baby': ('stage-direction', 55, '(Meenu gives birth to a child. But the child is not killed according to the physician\'s plan. Kumaran carries the child away. Heartbroken, Meenu leaves Malayangala bungalow. As she is about to fall into a well and kill herself, a thief arrives.)', 'scene-stage-direction', 'Birth, rescue of the child, Meenu\'s departure and attempted suicide.', None, []),
    'jewels': ('stage-direction', 55, '(He shows the jewels he has stolen.)', 'scene-stage-direction', 'The thief displays stolen jewels.', None, []),
    'u1': ('dialogue', 55, "I'll heap all of it into your lap and around your neck and make you a queen... come with me...... we can live like a princess...", 'source-unlabelled-speech', 'Unlabelled block `naam-s033-u001`.', None, ['Context points to the thief, but the source prints no explicit speaker label; metadata stays unassigned.']),
    'arrest': ('stage-direction', 55, '(The thief pressures Meenu to come with him. She refuses. When a police party arrives between them, the thief drops the jewels and runs away. Meenu is made into the thief and dragged away by the police.)', 'scene-stage-direction', 'The thief flees and Meenu is arrested with the jewels.', None, []),
},
34: {
    'night': ('stage-direction', 56, '(Night.)', 'scene-stage-direction', 'Opening night direction.', None, []),
    'street': ('stage-direction', 56, '(While the street play is going on, Kumaran arrives. The people see his terrible face and run in fear. Mathirai\'s wife is among them! Kumaran asks Mathirai to come treat him. Mathirai refuses; Kumaran carries Mathirai away. Finally Mathirai realizes Kumaran is human and runs to the people.)', 'scene-stage-direction', 'Street-play interruption and Mathirai\'s realization.', None, []),
    'puja': ('stage-direction', 56, '(Puja is going on in the temple.)', 'scene-stage-direction', 'Temple puja.', None, []),
    'arrive': ('stage-direction', 57, '(Kumaran arrives; many are afraid.)', 'scene-stage-direction', 'Kumaran appears before the crowd.', None, []),
    'boy': ('stage-direction', 58, '(A small boy goes up to Kumaran.)', 'scene-stage-direction', 'A child approaches Kumaran.', None, []),
    'u2': ('dialogue', 58, 'We are cowards even compared with children! The loyal blood that should run in youth! Heroic blood is being sacrificed! By what? By the ghost called superstition.', 'source-unlabelled-speech', 'Unlabelled block `naam-s034-u002`.', None, ['The sentence continues Kumaran\'s argument contextually but has no repeated printed speaker label; metadata remains unassigned.']),
    'cheer': ('stage-direction', 58, '(A cry of “Long live Kumaran” rises from the crowd.)', 'scene-stage-direction', 'Crowd cheers Kumaran.', None, []),
},
35: {
    'child': ('stage-direction', 58, '(Mathirai cuddles Kumaran\'s child.)', 'scene-stage-direction', 'Mathirai plays with Kumaran\'s child.', None, []),
    'prema': ('stage-direction', 58, '(At that moment Prema comes to Kumaran, realizing her wrongdoing—and she is raising the child.)', 'scene-stage-direction', 'Prema returns after recognizing her wrongdoing.', None, []),
},
}

PERF004 = [
    (49, 'பேசும் யாழே பெண் மானே', 'O speaking yaazh, doe-eyed maiden,'),
    (49, 'வீசும் தென்றல் நீ தானே', 'You alone are the breeze that blows.'),
    (49, 'கேளேனோ இனிமேல் இதுபோல் கீதம்.... (பேசும்)', 'Shall I never again hear a song like this.... (spoken)'),
    (49, 'தளா தீச்சுழலில்', 'In the thalaa fire-whirl,'),
    (50, 'தனியாய் விழித்தீரோ', 'did you wake alone?'),
    (50, 'மீளாசோகம் மீட்டிடும் யாழானேன்', 'I became a yaazh that plays irredeemable sorrow.'),
    (50, 'மாளா காதலினால் வாழ்ந்தோமே காதல்...        (பேசும்)', 'We lived by undying love—love... (spoken)'),
    (50, 'பாழும் பேயாக பாரினில் அல்லவோ', 'As a desolate ghost upon this earth, is it not...'),
    (50, 'தீரா துன்பம் தீட்டிய ஏடானேன்', 'I became a page inscribed with endless sorrow.'),
    (50, 'மாறு பாசமதனை மறந்தீரோ நேசம்....        (பேசும்)', 'Have you forgotten that answering affection, beloved.... (spoken)'),
]

CHANT034 = [
    ('role-cue', 'கிராம வாசிகள்', 'Villagers'),
    ('chant-line', 'ஹா ஹா! வருவாய் வருவாய்......', 'Ha ha! Come, come......'),
    ('chant-line', 'வைபோக சுந்தரியே......', 'O Vaibhoga Sundari......'),
    ('chant-line', 'சைபோக செளந்தரியே!', 'Saibhoga Soundariye!'),
    ('chant-line', 'சைரந்திரியே...கண்ணே...வருவாய்...', 'O Sairandhri... dear one... come...'),
    ('chant-line', 'கீசகன் ஆசைகொண்ட கிச்சிலிப் பழமடி நீ...', 'You are the kichili fruit Kichaka desired...'),
    ('chant-line', 'காச நோய்போல வந்து காதலுக்கு மருந்தடி நீ...', 'You came like tuberculosis, yet you are medicine for love, girl...'),
    ('chant-line', 'ஆண்மகா மம்முதா ஆசைகொண்ட கீசகா!', 'Aanmagaa Mammudhaa, desire-struck Kichaka!'),
    ('chant-line', 'கீசகா! கீசகா!', 'Kichaka! Kichaka!'),
    ('chant-line', 'கீசகா...........டேய்...', 'Kichaka........... hey...'),
    ('chant-line', 'இறுக்குத்தனமாய் வந்து மீசையை', 'You monkey who came stiffly and'),
    ('chant-line', 'முறுக்கி விட்ட குரங்கே! பெரிய குரங்கே!', 'twirled your moustache! Big monkey!'),
    ('chant-line', 'எட்டுத் திக்கும் நடுநடுங்க', 'With all eight directions trembling,'),
    ('chant-line', 'முரசு கொட்டும் பீமசேனனிடம்', 'before Bhimasena whose war-drum thunders,'),
    ('chant-line', 'வாலாட்டமா...?', 'will you wag your tail...?'),
    ('chant-line', 'வாலாட்டமா...?', 'wag your tail...?'),
]

ORDER = {
26: ['d001','x:faint'],
27: ['x:loc'] + [f'd{i:03d}' for i in range(1,10)] + ['x:knock','x:u1','x:open','x:u2'] + [f'd{i:03d}' for i in range(10,17)] + ['x:leave','d017','d018'],
28: ['x:loc','d001','x:will'],
29: ['x:loc'] + [f'd{i:03d}' for i in range(1,7)] + ['x:alone'] + [f'd{i:03d}' for i in range(7,14)] + ['x:after','x:u1','x:conscience','x:u2','x:prema','x:u3','d014'] + [f'd{i:03d}' for i in range(15,20)] + ['x:change','x:river','d020','x:rumor'],
30: ['x:loc','d001','d002','d003','x:after','x:u1','x:decide','d004','d005','d006','x:unwrap','d007','x:mirror','d008','d009','d010','x:prema','d011','x:show','x:u2','x:exit'],
31: ['x:cue','p:004','d001','d002','x:faint'] + [f'd{i:03d}' for i in range(3,23)] + ['x:alone'] + [f'd{i:03d}' for i in range(23,28)] + ['x:hear'] + [f'd{i:03d}' for i in range(28,32)],
32: [f'd{i:03d}' for i in range(1,14)],
33: ['x:loc'] + [f'd{i:03d}' for i in range(1,11)] + ['x:give','d011','x:trick','x:days','x:baby'] + [f'd{i:03d}' for i in range(12,17)] + ['x:jewels','x:u1','d017','x:arrest'],
34: ['x:night','c:034','x:street','x:puja','d001','d002'] + [f'd{i:03d}' for i in range(3,11)] + ['x:arrive','d011','x:boy','x:u2','x:cheer'],
35: ['x:child','d001','d002','d003','x:prema'],
}

def provenance(v):
    if isinstance(v, list): return [{'pdf_page':p,'printed_page':p} for p in v]
    return [{'pdf_page':v,'printed_page':v}]

def d_unit(n, di, uid, src):
    r = src[di-1]
    assert r['id'] == f'naam-s{n:03d}-d{di:03d}'
    return {
        'id': uid, 'kind': 'dialogue', 'status': 'verified', 'target_language': 'en',
        'scene_id': f'naam-s{n:03d}', 'scene_ordinal': n, 'source_scene_number': n,
        'source': {
            'source_path': dialogue_path(n), 'canonical_scene_path': scene_path(n),
            'source_record_id': r['id'], 'source_occurrence_id': None, 'source_locator': None,
            'speaker_label': r['speaker_label'], 'speaker_label_origin': 'source-explicit',
            'source_delimiter': r['source_delimiter'], 'page_provenance': r['page_provenance']
        },
        'translation': {'english_text': D[n][di-1], 'mode': 'prose-faithful', 'notes': list(NOTES.get((n,di), []))}
    }

def x_unit(n, key, uid):
    kind, pages, eng, locator_kind, desc, occ, notes = X[n][key]
    return {
        'id': uid, 'kind': kind, 'status': 'verified', 'target_language': 'en',
        'scene_id': f'naam-s{n:03d}', 'scene_ordinal': n, 'source_scene_number': n,
        'source': {
            'source_path': scene_path(n), 'canonical_scene_path': scene_path(n),
            'source_record_id': None, 'source_occurrence_id': occ,
            'source_locator': {'kind': locator_kind, 'ordinal': 1, 'description': desc},
            'speaker_label': None, 'speaker_label_origin': None, 'source_delimiter': None,
            'page_provenance': provenance(pages)
        },
        'translation': {'english_text': eng, 'mode': 'prose-faithful', 'notes': notes}
    }

def perf004_unit(uid):
    lm = [{'ordinal':i+1,'kind':'lyric-line','pdf_page':p,'tamil':t,'english':e} for i,(p,t,e) in enumerate(PERF004)]
    return {
        'id': uid, 'kind': 'song', 'status': 'verified', 'target_language': 'en',
        'scene_id': 'naam-s031', 'scene_ordinal': 31, 'source_scene_number': 31,
        'source': {
            'source_path': 'works/naam/songs/records/naam-perf-004.md',
            'canonical_scene_path': scene_path(31), 'source_record_id': None,
            'source_occurrence_id': 'naam-perf-004',
            'source_locator': {'kind':'retained-performance-record','ordinal':1,'description':'Full source-visible scene-31 lyrical body.'},
            'speaker_label': None, 'speaker_label_origin': None, 'source_delimiter': None,
            'page_provenance': [{'pdf_page':49,'printed_page':49},{'pdf_page':50,'printed_page':50}]
        },
        'translation': {
            'english_lines': [e for _,_,e in PERF004], 'line_map': lm,
            'mode': 'semantic-poetic-source-faithful',
            'notes': [
                'Translated only from the source-visible Tamil retained in `naam-perf-004`.',
                'Item-level authorship remains unresolved; the broad PDF-4 credit is not promoted.',
                'The difficult verified source form `தளா` is retained by transliteration as `thalaa` rather than silently repaired.',
                'Embedded `(பேசும்)` cues are retained as `(spoken)` inside the corresponding mapped lyric lines.'
            ]
        }
    }

def chant034_unit(uid):
    lm=[]
    for i,(kind,t,e) in enumerate(CHANT034,1):
        lm.append({'ordinal':i,'kind':kind,'pdf_page':56,'tamil':t,'english':e})
    return {
        'id': uid, 'kind': 'chant', 'status': 'verified', 'target_language': 'en',
        'scene_id': 'naam-s034', 'scene_ordinal': 34, 'source_scene_number': 34,
        'source': {
            'source_path': scene_path(34), 'canonical_scene_path': scene_path(34),
            'source_record_id': None, 'source_occurrence_id': None,
            'source_locator': {'kind':'source-unlabelled-chant','ordinal':1,'description':'Unlabelled audit block `naam-s034-u001`; villagers/street-play chant.'},
            'speaker_label': None, 'speaker_label_origin': None, 'source_delimiter': None,
            'page_provenance': [{'pdf_page':56,'printed_page':56}]
        },
        'translation': {
            'english_lines': [e for _,_,e in CHANT034], 'line_map': lm,
            'mode': 'semantic-poetic-source-faithful',
            'notes': [
                'The processing guide requires chants to remain distinct from full songs and ordinary dialogue.',
                'This scene-local street-play chant is not one of the seven retained song/performance occurrence records; no `naam-perf-*` ID or authorship claim is invented.',
                'Names and difficult forms such as `வைபோக`, `சைபோக`, and `ஆண்மகா மம்முதா` are kept by conservative transliteration rather than Tamil repair.'
            ]
        }
    }

# Align translation schema with the processing guide's existing rule that chants are a distinct unit kind.
schema_path = T / 'schema.json'
schema = rj(schema_path)
unit_enum = schema['$defs']['unit']['properties']['kind']['enum']
if 'chant' not in unit_enum:
    unit_enum.append('chant')
line_enum = schema['$defs']['line_map']['properties']['kind']['enum']
if 'chant-line' not in line_enum:
    line_enum.append('chant-line')
wj(schema_path, schema)

records=[]
for n in range(26,36):
    src = rj(W / f'dialogues/records/scene-{n:03d}.json')
    assert len(src) == EXPECTED[n] == len(D[n])
    units=[]
    for token in ORDER[n]:
        uid=f'naam-en-s{n:03d}-u{len(units)+1:03d}'
        if token.startswith('d'):
            units.append(d_unit(n, int(token[1:]), uid, src))
        elif token.startswith('x:'):
            units.append(x_unit(n, token[2:], uid))
        elif token == 'p:004':
            units.append(perf004_unit(uid))
        elif token == 'c:034':
            units.append(chant034_unit(uid))
        else:
            raise AssertionError(token)
    rec={'work_id':'naam','target_language':'en','scene_id':f'naam-s{n:03d}','scene_ordinal':n,'source_scene_number':n,'scene_status':'verified','unit_count':len(units),'units':units}
    wj(R / f'scene-{n:03d}.json', rec)
    records.append(rec)

batch_units=sum(r['unit_count'] for r in records)
batch_links=sum(1 for r in records for u in r['units'] if u['source']['source_record_id'])
unlabelled=[u['id'] for r in records for u in r['units'] if u['kind']=='dialogue' and u['source']['source_record_id'] is None]
occ=[]; song_maps=0; chant_maps=0; cross=[]
for r in records:
    for u in r['units']:
        o=u['source']['source_occurrence_id']
        if o and o not in occ: occ.append(o)
        if o == 'naam-perf-004': song_maps += len(u['translation'].get('line_map', []))
        if u['kind'] == 'chant': chant_maps += len(u['translation'].get('line_map', []))
        if len(u['source']['page_provenance']) > 1: cross.append(u['id'])
assert batch_links == 126, batch_links
assert batch_units == 179, batch_units
assert unlabelled == [
    'naam-en-s027-u012','naam-en-s027-u014',
    'naam-en-s029-u017','naam-en-s029-u019','naam-en-s029-u021',
    'naam-en-s030-u006','naam-en-s030-u020',
    'naam-en-s033-u023','naam-en-s034-u018'
], unlabelled
assert occ == ['naam-perf-004'], occ
assert song_maps == 10, song_maps
assert chant_maps == 16, chant_maps
assert cross == ['naam-en-s030-u016','naam-en-s031-u002'], cross

scene_results=[]
for r in records:
    n=r['source_scene_number']
    linked=sum(1 for u in r['units'] if u['source']['source_record_id'])
    unl=sum(1 for u in r['units'] if u['kind']=='dialogue' and u['source']['source_record_id'] is None)
    perfs=[]
    for u in r['units']:
        o=u['source']['source_occurrence_id']
        if o and o not in perfs: perfs.append(o)
    scene_results.append({
        'scene_id':r['scene_id'],'source_scene_number':n,'translation_units':r['unit_count'],
        'immutable_dialogue_records_expected':EXPECTED[n],'immutable_dialogue_records_linked':linked,
        'missing_dialogue_links':0,'duplicate_dialogue_links':0,
        'source_unlabelled_speech_units':unl,'performance_occurrences_linked':perfs,
        'chant_units':sum(1 for u in r['units'] if u['kind']=='chant')
    })

qa={
    'work_id':'naam','phase':'english-translation-batch-026-035-qa','status':'PASS','source_scenes':list(range(26,36)),
    'translation_units':batch_units,'immutable_dialogue_records_expected':126,'immutable_dialogue_records_linked':126,
    'dialogue_coverage':'126/126 exactly once','missing_dialogue_links':0,'duplicate_dialogue_links':0,
    'exact_tamil_speaker_labels_preserved':True,'source_delimiters_preserved_as_metadata':True,
    'source_unlabelled_speech_units':len(unlabelled),'source_unlabelled_unit_ids':unlabelled,'inferred_unlabelled_speakers':0,
    'performance_occurrences_expected':['naam-perf-004'],'performance_occurrences_linked':['naam-perf-004'],'performance_coverage':'1/1',
    'performance_line_cue_mappings':song_maps,'naam_perf_004_authorship':'unresolved-item-level',
    'source_chant_units':1,'source_chant_line_cue_mappings':chant_maps,
    'source_chant_inventory_relation':'scene-local street-play chant; distinct chant unit, no song/performance occurrence ID or authorship inferred',
    'cross_page_translation_units':cross,'scene_results':scene_results,
    'authorship_status_changed_by_translation':False,'external_or_unprinted_lyrics_imported':False,
    'canonical_tamil_modified':0,'scene_text_modified':0,'dialogue_records_modified':0,'character_entity_mappings_modified':0,'song_source_records_modified_by_translation':0,
    'translation_schema_refinement':'added chant unit kind and chant-line map kind to match existing processing-guide rule',
    'next_gate':'scenes 36-45 translation batch ready; final 10-scene English batch'
}
wj(T / 'batch-026-035-qa.json', qa)

idx=rj(T/'index.json')
assert idx['status']=='in-progress-verified-through-scene-025' and idx['verified_scenes']==25
assert idx['translation_units_verified']==501 and idx['immutable_dialogue_links_verified']==380
idx['status']='in-progress-verified-through-scene-035'
idx['verified_scenes']=35
idx['verified_scene_ids']=[f'naam-s{i:03d}' for i in range(1,36)]
idx['translation_units_verified']=501+batch_units
idx['immutable_dialogue_links_verified']=380+batch_links
idx['stage_or_narrative_units_verified']=idx.get('stage_or_narrative_units_verified',105)+sum(1 for r in records for u in r['units'] if u['kind'] in ('narrative','stage-direction'))
idx['performance_cue_units_verified']=idx.get('performance_cue_units_verified',3)+sum(1 for r in records for u in r['units'] if u['kind']=='performance-cue')
idx['song_units_verified']=idx.get('song_units_verified',3)+sum(1 for r in records for u in r['units'] if u['kind']=='song')
idx['source_chant_units_verified']=idx.get('source_chant_units_verified',0)+1
idx['source_chant_line_cue_mappings_verified']=idx.get('source_chant_line_cue_mappings_verified',0)+chant_maps
idx['retained_performance_records_translated']=5
idx['translated_performance_record_ids']=['naam-perf-007','naam-perf-001','naam-perf-002','naam-perf-003','naam-perf-004']
idx['song_line_cue_mappings_verified']=74+song_maps
idx['source_unlabelled_speech_units_verified']=idx.get('source_unlabelled_speech_units_verified',10)+len(unlabelled)
idx['cross_page_translation_units']=list(dict.fromkeys(idx.get('cross_page_translation_units',[])+cross))
idx['batch_026_035_review']='BATCH_026_035_REVIEW.md'
idx['batch_026_035_qa']='batch-026-035-qa.json'
idx['iteration_scene_batch_size']=10
idx['next_activity']=NEXT
wj(T/'index.json',idx)

rows='\n'.join(
    f"| {r['source_scene_number']} | {r['translation_units']} | {r['immutable_dialogue_records_linked']}/{r['immutable_dialogue_records_expected']} | {r['source_unlabelled_speech_units']} | {', '.join(r['performance_occurrences_linked']) or '0'} | {r['chant_units']} |"
    for r in scene_results
)
review=f'''# நாம் — English batch review / scenes 26–35

**Batch:** source scenes `காட்சி 26`–`காட்சி 35`  
**Status:** **VERIFIED**  
**Units:** **{batch_units}**  
**Immutable dialogue links:** **126/126 exactly once**

## Review result

This 10-scene iteration translates and verifies source-numbered scenes 26–35 in exact source order. All **126/126** immutable explicitly labelled dialogue records are linked exactly once with exact Tamil speaker labels, source delimiters and PDF provenance retained as metadata. Nine source speech blocks printed without explicit dialogue labels remain deliberately unassigned; no speaker identity is manufactured.

Scene 31 translates retained performance `naam-perf-004` across PDF 49–50 with **10/10** Tamil→English lyric-line mappings. The source-visible Meenu singing cue is linked to the same occurrence. Item-level authorship remains **unresolved**. The verified anomalous form `தளா` is not repaired and is carried conservatively as `thalaa`.

Scene 34 exposes a separate source-structure case already anticipated by the processing guide: a villagers' street-play **chant** is printed in the screenplay but is not one of the seven retained standalone song/performance occurrence records. It is therefore translated as a distinct `chant` unit with **16** role/chant line mappings, no `naam-perf-*` occurrence ID and no authorship inference. The translation schema is synchronized to permit the guide's existing `chant` / `chant-line` distinction.

## Scene counts

| Scene | Units | Immutable dialogue links | Unlabelled speech | Performance links | Chant units |
|---|---:|---:|---:|---|---:|
{rows}
| **Batch** | **{batch_units}** | **126/126** | **{len(unlabelled)}** | **1 unique record** | **1** |

## Fidelity decisions

- Scene 27 keeps Sanjeevi's frog/mansion satire and Mathirai's medicine/hospital wordplay; the two unlabelled commands around Mathirai's dismissal remain unassigned.
- Scene 29 preserves the quoted conscience text and the subsequent unlabelled plotting speech as three separate audited source blocks without manufacturing Sanjeevi labels.
- Scene 30 preserves the source's severe burn/disfigurement rhetoric and its cross-page PDF 48→49 utterance; the two remembered quoted lines and Kumaran's later unlabelled address to Prema remain source-unlabelled.
- Scene 31 preserves the pregnancy/disgrace confrontation and the source-irregular `கொப்பம்` context without Tamil repair; `naam-perf-004` remains authorship-unresolved.
- Scene 32 keeps the ghost-rumour escalation, medical satire and Sangaramurthi reveal in colloquial register.
- Scene 33 keeps the infanticide plot, will deception, attempted suicide, thief encounter and wrongful arrest; the thief-context speech without an explicit source label remains unassigned.
- Scene 34 keeps the street-play chant distinct from the seven-record song inventory, preserves culturally loaded names/forms by transliteration, and retains Kumaran's anti-superstition rhetoric including the source insult `எச்சில் பணம்` as `spittle-money`.
- Scene 35 retains Mathirai's Ramalinga Swami reference as printed and adds no external explanation to the translation record.

## Integrity checks

- expected / linked immutable dialogue records: **126 / 126**;
- missing / duplicate immutable links: **0 / 0**;
- source-unlabelled speeches: **{len(unlabelled)}**, inferred speakers: **0**;
- song/performance records expected / linked: **1 / 1 — `naam-perf-004`**;
- new song/performance line mappings: **{song_maps}**;
- source-local chant units / mappings: **1 / {chant_maps}**;
- new cross-page units: **2 — {', '.join(cross)}**;
- authorship upgrades: **0**;
- external/unprinted lyric imports: **0**;
- canonical Tamil / scene / dialogue / character / song-source modifications: **0 / 0 / 0 / 0 / 0**.

## Cumulative English checkpoint

After scenes 1–35: **35/45 source scenes**, **{idx['translation_units_verified']} verified English units**, **{idx['immutable_dialogue_links_verified']} immutable dialogue links**, **{idx['source_unlabelled_speech_units_verified']} source-unlabelled speech units retained without inferred labels**, **5/7 performance records translated**, **{idx['song_line_cue_mappings_verified']} Tamil→English song/performance line-cue mappings**, plus **1 scene-local chant / {chant_maps} chant mappings**.

## Iteration rule

Continue with **10 source scenes per iteration**. The remaining scenes 36–45 form the final 10-scene translation batch.

## Next batch

{NEXT}
'''
wt(T/'BATCH_026_035_REVIEW.md',review)

# Translation README.
p=T/'README.md'; s=rt(p)
s=re.sub(r'\*\*Status:\*\* \*\*.*?\*\*',f"**Status:** **verified through source scene 35 / 45; {idx['translation_units_verified']} units**",s,count=1)
s=re.sub(r'## Next batch\n\n.*?(?=\n##|\Z)',f"## Next batch\n\n{NEXT}\n",s,flags=re.S)
if '## Verified batch — scenes 26–35' not in s:
    s += f'''\n## Verified batch — scenes 26–35\n\n- source scenes: **10 / scenes 26–35**;\n- units: **{batch_units}**;\n- immutable dialogue links: **126/126**;\n- source-unlabelled speech: **{len(unlabelled)} / inferred speakers 0**;\n- performance occurrence: **1/1 — `naam-perf-004`**;\n- new song/performance mappings: **{song_maps}**;\n- scene-local chant: **1 unit / {chant_maps} mappings / no song occurrence or authorship inference**;\n- upstream rewrites: **0**.\n'''
wt(p,s)

# Work metadata.
p=W/'metadata.yaml'; s=rt(p)
for pat,repl in [
    (r'(?m)^  english_translation: .+$','  english_translation: in-progress-verified-35-of-45'),
    (r'(?m)^  english_translation_verified_scenes: \d+$','  english_translation_verified_scenes: 35'),
    (r'(?m)^  english_translation_unit_count: \d+$',f"  english_translation_unit_count: {idx['translation_units_verified']}"),
    (r'(?m)^  english_dialogue_links_verified: \d+$',f"  english_dialogue_links_verified: {idx['immutable_dialogue_links_verified']}"),
    (r'(?m)^  english_performance_records_translated: \d+$','  english_performance_records_translated: 5'),
    (r'(?m)^  english_song_line_cue_mappings_verified: \d+$',f"  english_song_line_cue_mappings_verified: {idx['song_line_cue_mappings_verified']}")]:
    s=re.sub(pat,repl,s,count=1)
if '  english_chant_units_verified:' not in s:
    anchor=f"  english_song_line_cue_mappings_verified: {idx['song_line_cue_mappings_verified']}"
    s=s.replace(anchor,anchor+f"\n  english_chant_units_verified: 1\n  english_chant_line_cue_mappings_verified: {chant_maps}",1)
else:
    s=re.sub(r'(?m)^  english_chant_units_verified: \d+$','  english_chant_units_verified: 1',s,count=1)
    s=re.sub(r'(?m)^  english_chant_line_cue_mappings_verified: \d+$',f'  english_chant_line_cue_mappings_verified: {chant_maps}',s,count=1)
s=re.sub(r'(?m)^next_action:.*$', 'next_action: '+json.dumps(NEXT,ensure_ascii=False),s,count=1)
wt(p,s)

# Work README.
p=W/'README.md'; s=rt(p)
s=re.sub(r'- English translation: \*\*.*?\*\*; reader / Reading Room: \*\*not-started\*\*\.',f"- English translation: **35/45 VERIFIED — {idx['translation_units_verified']} units / {idx['immutable_dialogue_links_verified']} dialogue links / 5 of 7 performance records / {idx['song_line_cue_mappings_verified']} performance mappings / 1 chant ({chant_maps} mappings)**; reader / Reading Room: **not-started**.",s,count=1)
s=re.sub(r'\*\*Next:\*\* Translate and verify source-numbered scenes [^\n]*','**Next:** '+NEXT,s)
if '## English scenes 26–35 checkpoint' not in s:
    s += f'''\n\n## English scenes 26–35 checkpoint\n\n- English scenes verified: **35/45 cumulative**;\n- cumulative units: **{idx['translation_units_verified']}**;\n- immutable dialogue links: **{idx['immutable_dialogue_links_verified']}**;\n- source-unlabelled speech retained without inferred labels: **{idx['source_unlabelled_speech_units_verified']}**;\n- translated performance records: **5/7**;\n- performance line/cue mappings: **{idx['song_line_cue_mappings_verified']}**;\n- source-local chants: **1 / {chant_maps} mappings**;\n- closed upstream-layer changes: **0**.\n\n**Next:** {NEXT}\n'''
wt(p,s)

# Next chat prompt.
wt(W/'NEXT_CHAT_PROMPT.md',f'''# Next Chat Prompt — நாம்\n\nContinue directly in `pugazg/kalaignar-cinema-works`, branch `main`, active work `works/naam/`. **Live `main` is authoritative.**\n\nCanonical Tamil is **67/67 COMPLETE-VERIFIED**; scenes **45/45 COMPLETE-VERIFIED**; dialogue index **590 immutable records / QA PASS**; character/entity layer **28 entities / 45/45 labels / 590/590 records / QA PASS**; song/performance gate **7/7 COMPLETE-VERIFIED-SOURCE-ONLY — RECONCILED**.\n\nEnglish translation is **VERIFIED THROUGH SOURCE SCENE 35**: **35/45 scenes**, **{idx['translation_units_verified']} units**, **{idx['immutable_dialogue_links_verified']} immutable dialogue links**, **{idx['source_unlabelled_speech_units_verified']} source-unlabelled speech units with 0 inferred speaker labels**, **5/7 performance records translated**, **{idx['song_line_cue_mappings_verified']} performance line/cue mappings**, and **1 source-local chant / {chant_maps} chant mappings**. `naam-perf-001` retains the specific source attribution **பாரதியார்**; `naam-perf-002`, `naam-perf-003`, and `naam-perf-004` remain unresolved at item level.\n\nUser directive: **process 10 source scenes in each English-translation iteration**. Scenes 36–45 are the final 10-scene translation batch.\n\nThe scene-34 villagers' street-play block is a **chant**, not a new `naam-perf-*` record: keep it distinct and do not infer authorship.\n\nCurrent English files include `translations/BATCH_026_035_REVIEW.md`, `translations/batch-026-035-qa.json`, and `translations/records/scene-001.json` through `scene-035.json`.\n\nDo not alter closed Tamil or structured source layers except for later direct source-supported corrections.\n\n## Exact next activity\n\n> **{NEXT}**\n''')

# Project handover.
p=W/'PROJECT_HANDOVER.md'; s=rt(p)
tag='## English scenes 26–35 closure checkpoint'
if tag not in s:
    s += f'''\n\n{tag}\n\n- cumulative verified English scenes: **35/45**;\n- cumulative units: **{idx['translation_units_verified']}**;\n- immutable dialogue links: **{idx['immutable_dialogue_links_verified']}**;\n- source-unlabelled speech retained: **{idx['source_unlabelled_speech_units_verified']} / inferred labels 0**;\n- performance records translated: **5/7**;\n- performance line/cue mappings: **{idx['song_line_cue_mappings_verified']}**;\n- source-local chant: **1 / {chant_maps} mappings**, no song/performance ID or authorship inference;\n- upstream source-layer changes caused by English: **0**.\n\n## Current exact next activity\n\n> **{NEXT}**\n'''
wt(p,s)

# Repository data mirror.
p=Path('data/works.json'); data=rj(p); n=next(x for x in data if x.get('id')=='naam'); sd=n.setdefault('structured_derivatives',{})
sd.update({
    'english_translation':'in-progress-verified-through-scene-035','english_translation_verified_scenes':35,
    'english_translation_units':idx['translation_units_verified'],'english_dialogue_links_verified':idx['immutable_dialogue_links_verified'],
    'english_source_unlabelled_speech_units':idx['source_unlabelled_speech_units_verified'],'english_performance_records_translated':5,
    'english_song_line_cue_mappings_verified':idx['song_line_cue_mappings_verified'],'english_chant_units_verified':1,
    'english_chant_line_cue_mappings_verified':chant_maps,'english_iteration_scene_batch_size':10,
    'english_translation_index_path':'works/naam/translations/index.json'
})
n['next_action']=NEXT; wj(p,data)

# Root README and repository-wide status mirrors.
p=Path('README.md'); s=rt(p)
s=re.sub(r'- English translation: \*\*.*?\*\*\.',f"- English translation: **35/45 VERIFIED — {idx['translation_units_verified']} units / {idx['immutable_dialogue_links_verified']} dialogue links / 5 of 7 performance records / {idx['song_line_cue_mappings_verified']} mappings / 1 chant**.",s,count=1)
s=re.sub(r'\*\*Next:\*\* Translate and verify source-numbered scenes [^\n]*','**Next:** '+NEXT,s)
mark='<!-- Naam English scenes 26-35 current -->'
if mark not in s:
    s += f'''\n\n{mark}\n**Naam current English checkpoint:** **35/45 source scenes VERIFIED**, **{idx['translation_units_verified']} units**, **{idx['immutable_dialogue_links_verified']} immutable dialogue links**, **5/7 performance records translated**, **{idx['song_line_cue_mappings_verified']} performance mappings**, **1 source-local chant / {chant_maps} mappings**, **0 upstream rewrites**. **Next:** {NEXT}\n'''
wt(p,s)

for p in [Path('docs/HANDOVER_KALAIGNAR_CINEMA_WORKS.md'),Path('docs/STATUS_CONSISTENCY_AUDIT.md')]:
    s=rt(p); mark='<!-- Naam English scenes 26-35 current -->'
    if mark not in s:
        s += f'''\n\n{mark}\n**Naam English scenes 26-35 current:** English **35/45 verified / {idx['translation_units_verified']} units / {idx['immutable_dialogue_links_verified']} dialogue links / 5 of 7 performances / {idx['song_line_cue_mappings_verified']} performance mappings / 1 chant ({chant_maps} mappings)**; source-unlabelled speech remains unassigned; upstream rewrites **0**. **Next:** {NEXT}\n'''
    wt(p,s)

print(json.dumps({
    'status':'PASS','scenes':'26-35','batch_units':batch_units,'batch_dialogue_links':batch_links,
    'batch_unlabelled':len(unlabelled),'performance_records':['naam-perf-004'],'song_maps_added':song_maps,
    'chant_units':1,'chant_maps':chant_maps,'cumulative_scenes':35,'cumulative_units':idx['translation_units_verified'],
    'cumulative_dialogue_links':idx['immutable_dialogue_links_verified'],'next':'36-45'
},ensure_ascii=False,indent=2))
