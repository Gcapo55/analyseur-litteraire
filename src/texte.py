from collections import Counter

class Texte:
    def __init__(self, titre: str, auteur: str, annee: int, contenu: str):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.contenu = contenu
    @property
    def titre(self) -> str :
        return self._titre
    
    @titre.setter
    def titre(self, nouveau: str):
        if nouveau == "":
            raise ValueError("Le nom est vide.")
        self._titre = nouveau
    
    def nombre_mots(self) -> int:
        return len(self.contenu.split())
    def mots_uniques(self) -> set[str]:
        return set(self.contenu.split())
    def frequences(self) -> dict[str, int]:
        return Counter(self.contenu.split())

bovary = Texte("Madame Bovary", "Gustave Flaubert", 1856, """
WE WERE IN study-hour, when the Headmaster entered, followed by a new boy dressed in his everyday clothes and by a classroom servant carrying a big desk. Those who were asleep woke up, and each of us rose as if caught working.

The Headmaster nodded at us to resume our seats; then, turning to the usher:

‘Monsieur Roger,’ he said to him in a near-whisper, ‘here is a pupil I entrust to you, he will start in the fifth class. If his work and behaviour are deserving, he may go up to the seniors, as befits his age.’

Remaining in the corner, behind the door, so much so that we could scarcely make him out, the new boy was a country lad, about fifteen years of age, and taller than any of us. His hair was cut straight across the forehead, like a village cantor, and he looked sound enough and exceedingly embarrassed. He was not broad-shouldered, but his short green woollen coat with its black buttons must have been tight at the armpits and revealed, through the slits in the back of its cuffs, red wrists used to being exposed. His legs, in blue stockings, emerged from yellowish trousers hitched up tight by the braces. He was wearing stout shoes, poorly polished and studded with nails.

We started reciting our lessons. He was all ears, as if attending to a sermon, not daring even to cross his legs or lean on his elbow, and when the bell went, at two o’clock, he had to be alerted by the usher to join us as we lined up.

It was our trick, on coming into class, to toss our caps on the floor so as to have our hands freer afterwards; right from the doorway, you had to hurl them under the bench, so that they hit the wall and made lots of dust: that was the thing.

But, whether he had failed to notice this stratagem or had not dared succumb to it, when prayers were over the new boy was still holding his cap on his lap. It was one of those composite types of headdress, which hints at bearskin, chapka,1 round hat, otterskin hat and cotton bonnet; one of those sorry contraptions whose dumb ugliness has certain expressive depths, like the face of an imbecile. Egg-shaped and bulging with whalebone, it began with three circular sausage-shapes; then came alternate lozenges of velvet and rabbit-skin separated from each other by a red band, followed by a sort of bag ending in a pasteboard polygon covered with a complicated piece of braid, and from which hung, at the end of a long and too-slender string, a little criss-cross of gold thread by way of a tassel. It was brand-new; the peak shone.

‘Stand up,’ said the teacher.

He stood up; his cap fell off. The whole class started to laugh.

He bent down to retrieve it. A neighbour made it fall with a jab of the elbow, he picked it up yet again.

‘Do get rid of your helmet,’ said the teacher, who was a witty fellow.

A loud burst of laughter from the pupils disconcerted the poor boy, so much so that he had no idea whether he should keep hold of his cap, leave it on the floor or put it on his head. He sat down again and placed it on his lap.

‘Stand up,’ resumed the teacher, ‘and tell me your name.’

The new boy pronounced, mumbling, an unintelligible name.

‘Again!’

The same mumble of syllables could be heard, showered with hoots from the class.

‘Louder!’ the master shouted, ‘louder!’

The new boy, coming then to a drastic decision, opened an enormous mouth and hurled forth at the top of his voice, as if calling out for someone, this word: Charbovari.

A roar shot up, rose in a crescendo on bursts of high-pitched shrieks (we yelled, we barked, we stamped our feet, we repeated: Charbovari! Charbovari!), then kept itself going on single notes, dying down with great difficulty, only to revive at times all of a sudden along a bench’s row, where it gushed forth here and there in a stifled laugh, like an ill-snuffed firework.

Nevertheless, beneath a rain of extra lines, order was restored bit by bit in the classroom, and the teacher, managing to understand the name Charles Bovary by having it dictated, spelt out and reread, ordered the poor devil to go and sit on the idlers’ bench, at the foot of the rostrum. He started to move, but, before heading off, hesitated.

‘What are you looking for?’ asked the teacher.

‘My ca …’ said the new boy, casting worried eyes around him.

‘Five hundred lines for the whole class!’ – delivered in a furious voice – quelled, like the Quos ego,2 a new squall. ‘So now keep quiet!’ the indignant teacher continued, and wiping his forehead with a handkerchief that he had just drawn from beneath his headpiece: ‘As for you, new boy, you will copy out for me, twenty times, the verb ridiculus sum.’3

Then, in a softer voice, ‘Well now, you’ll find your cap, it hasn’t been stolen.’

All calmed down once more. Heads bent to books and for two hours the new boy behaved in an exemplary fashion, even if, from time to time, the odd paper pellet launched from a pen nib splattered his face. But he wiped himself with his hand, and remained completely still, eyes cast down.

In the evening, at study-time, he pulled his sleeve-guards from his desk, set his little pile of belongings in order, painstakingly ruled his paper. We could see him working hard, looking up every word in the dictionary and going to great trouble. Thanks, no doubt, to the willingness he showed, he avoided dropping down a class; because, though he knew his rules of grammar tolerably well, he had scarce any elegance in his turn of phrase. It was his village priest who had started him in Latin; his parents, for reasons of thrift, sending him to college only at the last possible moment.

His father, Monsieur Charles-Denis-Bartholomé Bovary, former assistant-surgeon-major, compromised around 1812 in some conscription scandal and forced at about that time to leave the service, had then turned his personal attractions to advantage by grabbing as it passed a dowry of sixty thousand francs, which presented itself in the shape of a bonnet merchant’s daughter, who had fallen in love with his bearing. A handsome man, boastful, loudly ringing his spurs, sporting side whiskers that met his moustache, fingers forever bristling with rings, dressed in gaudy colours, he had the look of a gallant, with the facile gusto of a commercial traveller. Once he was married, he spent two or three years living off his wife’s fortune, dining well, rising late, smoking large porcelain pipes, coming back in the evening only after the theatre and forever in and out of the cafés. The father-in-law died and left hardly a thing; he was furious, launched out into fabrics, lost some money there, then retired to the country, where he wished to exploit the land. But, as he knew scarcely more about cultivation than about printed calico, and rode his horses rather than turning them out to plough, drank his cider in bottles rather than selling it in the cask, ate the finest poultry from his yard and greased his hunting boots with the lard of his pigs, he soon saw that it would be better to give up all speculation.

Averaging two hundred francs a year, he then found, on the borders of the Caux and Picardy country, a dwelling that was a kind of half-farm, half-mansion; and – despondent, gnawed by regrets, blaming the heavens and envious of everyone – he shut himself up from the age of forty-five, disgusted by men, as he put it, and determined to live in peace.

His wife had doted on him once upon a time; she had loved him with innumerable cringings4 that had weaned him from her all the more. Previously cheerful, out-going and entirely loving, on growing older she had (in the way a stale wine turns vinegary) become testy, screechy, nervous. She had suffered so, without at first complaining, when she saw him running after all the village strumpets and that a score of disreputable places sent him back to her in the evening, worn out with pleasures and reeking of drunkenness! Then her pride had revolted. So she had kept quiet, swallowing her rage in a mute stoicism that she kept to the day she died. She was endlessly out shopping and on business. She went to the solicitors’ office, to the tribunal president, remembered to settle bills, won delays; and, at the house, she ironed, sewed, laundered, watched over the workers, settled the memorandums; so much so that, without worrying about a thing, Monsieur, perpetually benumbed in a sullen stupor from which he only stirred to say unkind words to her, stayed puffing in the chimney corner, hawking on the cinders.

When she bore a child, it had to be put out to a wet nurse. Returned home, the brat was spoilt like a prince. His mother fed him jams; his father let him run around without shoes, and, acting the philosopher, even said that he could go about naked, like the young of animals. To counter any maternal leanings, he had in his head a certain virile ideal of childhood by which he endeavoured to mould his son, wanting him to be brought up the hard way, in the Spartan manner, to give him a sound constitution. He sent him to bed without a fire, taught him to take great swigs of rum and to insult the church processions. But, being naturally easy-going, the child responded poorly to his efforts. His mother was always dragging him after her; she would cut up pasteboard boxes for him, tell him stories, converse with him in unending monologues, full of melancholic gaieties and babbling blandishments. In the loneliness of her life, she transferred onto this child’s head all her scattered, broken vanities. She dreamed of high positions, she saw him as already tall, handsome, witty, established in civil engineering or in the magistracy. She taught him to read, and even, on an old piano of hers, to sing two or three sentimental ballads. But, to all this, Monsieur Bovary, who cared little for the arts, objected that it was not worth it! Would they ever have what was needed to support him at a government school, buy him a practice or a business? Besides, if he has the cheek, a fellow always succeeds in the world. Madame Bovary bit her lip, and the child roamed the village.

He followed the ploughmen and, with clods of earth, would drive off the crows that flew away. He ate blackberries all along the ditches, kept watch over the turkeys with a stick, tossed the hay at harvest, ran in the woods, played hopscotch in the church porch on rainy days, and, during the main festivals, would beg the verger to let him ring the bells, so that he could hang full length from the great rope and feel its peals carry him away.

And he shot up like an oak. He acquired strong hands, a healthy bloom.

When he was twelve, his mother was finally allowed to start him on his studies. They assigned these to the priest. But the lessons were so brief and so poorly followed, that they could serve little purpose. They were given at spare moments, in the sacristy, standing up, in a rush, between a baptism and a burial; or else the priest would send for his pupil after the evening Angelus, if he had not to go out. You went up to his room, you settled down: the midges and the moths swirled around the tallow. It was hot, the child fell asleep; and the old fellow, dozing off with his hands on his belly, was soon snoring, mouth agape. At other times, when Monsieur le Curé, returning from giving the eucharist to some sick person or other in the neighbourhood, spotted Charles up to mischief in the open fields, he would call him over, give him a good talking-to for a quarter of an hour and use the opportunity to make him conjugate his verbs at the foot of a tree. Rain would come to interrupt them, or an acquaintance passing by. Yet he was always pleased with him, even saying that the young fellow had an ample memory.

Charles could not stop there. Madame was insistent. Ashamed, or weary rather, Monsieur yielded without resistance, and they waited one more year until the boy had made his first communion.

Another six months went by; and, the following year, Charles was sent for good to school in Rouen, taken there personally by his father, towards the end of October, at the time of the Saint-Romain fair.

It would be impossible now for any of us to remember a thing about him.5 He was an even-tempered boy, who played at break-time, worked in the study-hour, listened in class, sleeping well in the dormitory and eating well in the refectory. He had a wholesale ironmonger in the Rue Ganterie as guardian, who took him out once a month, on Sundays, after his shop was shut, would send him off to walk around the harbour to look at the boats, then take him back to school as soon as it was seven o’clock, before supper. Each Thursday evening, he wrote a long letter to his mother using red ink and three bars of sealing wax; then he would go over his history exercise books, or read an old volume of Anacharsis6 lying about in the school-room. On walks, he chatted with the servant, who was from the country just like him.

By dint of application, he always remained around the middle of the class; once, he even gained a first certificate of merit in natural history. But at the end of his fourth year, his parents took him out of school to have him study medicine, convinced that he could make his own way up to the baccalauréat.

His mother chose a room for him, on the fourth floor, along the Eau-de-Robec, with a dyer of her acquaintance. She concluded the arrangements for his board and lodging, bought some furniture, a table and two chairs, had an old cherrywood bed sent from home, and in addition bought a little cast-iron stove, with a supply of wood to keep her poor child warm. Then she left at the end of the week, after innumerable recommendations to behave well, now that he was to be left to his own devices.

The curriculum, which he read on the noticeboard, made him feel giddy: lectures in anatomy, lectures in pathology, lectures in physiology, lectures in pharmacology, lectures in chemistry, in botany, and in clinical and therapeutic medicine, not to mention hygiene and materia medica, all names of whose etymologies he was ignorant and which were like so many sanctuary doors full of august shades.

He understood nothing; he listened in vain, he did not grasp it. Yet he worked, he had well-bound notebooks, he would follow all the lectures, he missed not a single ward round. He performed his little daily task like a mill horse, that turns on the same spot blindfold, ignorant of what it is crushing.

To spare him expense, his mother sent him, each week, by messenger, a piece of roast veal, on which he would breakfast in the morning, when he returned from the hospital, all the while beating his feet against the wall to warm them. Then he had to run to classes, to the amphitheatre, to the hospice, and come back home, right across town. In the evening, after his landlord’s meagre dinner, he went up again to his room and got back down to work, in wet clothes that steamed on his body, before the glowing stove.

On beautiful summer evenings, when the warm streets are empty and the servant girls play battledore on the front step, he would open the window and lean on his elbows. The river,7 which made a vile little Venice of this area of Rouen, flowed below, right beneath him, yellow, violet or blue between its bridges and its railings. Workers, crouched by the edge, washed their arms in the water. On poles protruding from the lofts, hanks of cotton dried in the open air. Opposite, beyond the rooves, the great pure sky stretched, with a red setting sun. How good it must be over there! How cool under the beech grove! And he opened his nostrils wide to breathe in the good smells of the countryside, which did not reach him.

He thinned out, he grew taller, and his face took on a sort of doleful expression which made it almost interesting.

Naturally, out of indolence, he began to release himself from all the resolutions he had made. Once, he skipped a ward round, the next day his lecture, and, savouring the laziness, little by little, returned there no more.

He became a tavern-regular, developing a passion for dominoes. Shutting himself up every evening in a squalid public bar, tapping the little black-dotted sheep-bones on marble tables, seemed to him a precious act of liberty, which gave him back his self-esteem. It was his initiation into the world, his admittance into forbidden pleasures; and, on entering, he would place his hand upon the door-knob with a joy that was almost sensual. Then a lot of things that were squeezed in him began to expand; he learnt little songs by heart that he sang at the initiation drinks, was infatuated with Béranger,8 learnt how to make punch and knew what love was at last.

Thanks to these preparatory labours, he completely failed his medical officer’s exam. They were waiting for him that very evening at the house to celebrate his success!

He set off on foot and stopped at the entrance to the village, where he sent for his mother, told her everything. She forgave him, shifting blame onto the unfairness of the examiners, and stiffened his resolve a little, taking it upon herself to sort things out. It was another five years before Monsieur Bovary knew the truth; it was hoary old news, he accepted it, not being able to imagine, anyway, that his male issue could be a dunce.

So Charles went back to work and revised for his exams without a break, learning all the questions in advance by heart. He passed with quite a good mark. What a wonderful day for his mother! They gave a huge dinner.

Where would he go to practise his skills? To Tostes. There was only an old doctor there. For a long time Madame Bovary had been on the watch for his death, and the gentleman had not yet turned up his toes when Charles was installed opposite, as his successor.

But it was not enough to have raised her son, to have had him study medicine and to have found a practice for him in Tostes: he needed a wife. She found him one: the widow of a Dieppe bailiff, who was forty-five and worth twelve hundred livres a year.

Although she was ugly, thin as a rake and pimply as a goose, it has to be said that Madame Dubuc did not lack for choice when it came to a match. To achieve her ends, Mère Bovary had to oust them all, and she foiled – and very skilfully too – the intrigues of a pork butcher who was backed by the priests.

Charles had dimly envisaged in the marriage the advent of a better life, imagining that he would be freer and could have at his disposal her person and her money. But his wife was the master; in front of people he must say this, must not say that, had to abstain from meat on Fridays, dress as she thought fit, harass on her instructions those clients who were not settling up. She unsealed his letters, spied on his every move, and put her ear to the partition wall as he was giving consultations in his surgery, when there were women.

She must have her hot chocolate every morning, and his never-ending attentions. She would complain ceaselessly of her nerves, her chest, her fluids. The noise of footsteps gave her pains; you went away, and the solitude grew hateful to her; you came back to her side, and it was to watch her die, no doubt. In the evening, when Charles returned, she produced her long, scrawny arms from under the sheet, slipped them around his neck, and, having made him sit on the edge of the bed, set about telling him her sorrows: he was forgetting her, he loved another! People had indeed told her she would be unhappy; and she ended up asking him for a syrup for her health and a little bit more love.

II
ONE NIGHT, AT about eleven o’clock, they were woken by the noise of a horse which stopped just in front of the door. The maid opened the attic skylight and argued things over for some time with the man still down below, in the street. He had come looking for a doctor; he had a letter. Nastasie descended the steps shivering, and went to open the lock and slip the bolts, one after the other. The man left his horse and, following the maid, appeared behind her all of a sudden. From his grey-tasselled cotton bonnet he pulled out a letter wrapped in a piece of rag, and daintily presented it to Charles, who leaned his elbow on the pillow to read it. Nastasie, near the bed, held the light. Madame, out of a sense of decency, stayed with her back turned, facing the wall.

This letter, sealed with a little seal of blue wax, begged Monsieur Bovary to go immediately to the farm at Les Bertaux, to set a broken leg. Now, between Tostes and Les Bertaux, there are a good eighteen miles to cross, by way of Longueville and Saint-Victor. The night was black. Madame Bovary the younger was fearful of accidents befalling her husband. So it was decided that the stable boy should set off first. Charles would leave three hours later, when the moon rose. They would send a child to meet him, in order to show him the way to the farm and open the gates ahead.

At about four o’clock, Charles, wrapped up well in his cloak, set off for Les Bertaux. Still drowsy from the warmth of sleep, he let himself be lulled by the peaceful trot of his beast. Whenever it stopped of its own accord before those thorn-wreathed holes they dig on the boundaries of ploughed fields, Charles, waking up with a start, would remember the broken leg, and endeavour to remind himself of all the fractures he knew. The rain was no longer falling; day was breaking, and, on the leafless apple trees, the birds stayed motionless, ruffling their little feathers in the cold morning wind. The flat country stretched out as far as the eye could see, and the clumps of trees around the farms made, at rare intervals, deep violet patches on this vast grey surface that fused at the horizon with the gloomy tint of the sky. Charles, from time to time, opened his eyes; then, his mind wearying and sleep returning of its own accord, he soon slipped into a kind of slumber where, his recent feelings merging with his memories, he perceived himself in duplicate, both student and married man, lying in his bed as he had been just now, crossing an operating room as in the past. The hot smell of poultices blended in his head with the fresh scent of the dew; he heard the beds’ iron rings trundling on their curtain-rods and his wife sleeping … As he came through Vassonville, he noticed, on the edge of a ditch, a young boy seated on the grass.

‘Are you the doctor?’ the child asked.

And, at Charles’s reply, he took his clogs in his hands and began to run ahead.

Along the way, the medical officer9 understood from the chatter of his guide that Monsieur Rouault must be among the better-off farmers. He had a good house, a good stable, a good farmyard, and a good barn. He had a lot of land, and his wife was a good""")

print(bovary.frequences())