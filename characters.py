#!/usr/bin/python
import pprint
import enum

from altereal_characters import *

########################################################################################################################
theodora = Mage("Théodora El-Yueadu", "Mage", "Euthanatos", "d8GxvpV4")
theodora.concept = "Gourou Fight Club"
theodora.paradigme = "Femme ex de confusion musulmane qui en 'rencontrer' Lucifer. Il lui a fait comprendre que ce n'etait pas l'archange Gabriel mais lui qui avait guidé les musulmans."
theodora.foci = "Séduction, ArtMartial, Rize de rue/SabotageUrbain, Méditation, DOmination sociale, Prière. Je suis l'étincelle du chaos, je montre l'exemple en démontrant les conséquences qui peuvent suivre les simples graines que je sème. Mon art martial me permet de mettre mon corps et mon moi-symbole comme exemple à suivre."
theodora.physique = "..."
theodora.attitude = "..."
theodora.setAttributes([3,3,2,4, 2,1,1,2])
theodora.setCapacities({"Manipulation":4})
theodora.setCapacities({"Arts Martiaux":3,"Subterfuge":3})
theodora.setCapacities({"Armes à feu":2,"Recherche":2,"Érudition":2})
theodora.setCapacities({"Ésotérisme":1,"Informatique":1,"Intimidation":1,"Méditation":1})
theodora.spécialité["Manipulation"] = "Politique"
theodora.spécialité["Arts Martiaux"] = "Externes"
theodora.setSpheres({Sphere.Entropie:3, Sphere.Psyché:2, Sphere.Prime:1})
theodora.setEveil(3)
theodora.xp = 500 #antago bonus
#theodora.display()

theodora.upgradeSphere(Sphere.Vie)
theodora.upgradeAttribute(Attribut.Charisme)
theodora.upgradeAttribute(Attribut.Volonté)
theodora.upgradeAttribute(Attribut.Mémoire)
theodora.upgradeAttribute(Attribut.Empathie)
theodora.upgradeCapacity("Arts Martiaux")
theodora.upgradeCapacity("Esotérisme")
theodora.upgradeCapacity("Méditation")

theodora.upgradeHistorique("Influence(Spirituel)")
theodora.upgradeHistorique("Influence(Spirituel)")

theodora.upgradeHistorique("Influence(Politique)")
theodora.upgradeHistorique("Influence(Politique)")
theodora.upgradeHistorique("Influence(Politique)")

theodora.upgradeHistorique("Influence(Médias)")
theodora.upgradeHistorique("Influence(Médias)")

theodora.upgradeHistorique("Ressources")
theodora.upgradeHistorique("Ressources")
theodora.upgradeHistorique("Ressources")
theodora.upgradeHistorique("Ressources")
theodora.upgradeHistorique("Ressources")

theodora.upgradeHistorique("Secte")
theodora.upgradeHistorique("Secte")
theodora.upgradeHistorique("Secte")

#theodora.display()
theodora.grantExp(3, "Mars 2022")

########################################################################################################################
Zhen = Mage("Zhen", "Mage", "Akashite", "mLzrQky4")
Zhen.concept = "Artiste Martial de l'harmonie,Ange gardien"
Zhen.paradigme = "Le matériel est une illusion. La volonté peut défaire ces illusions et les remodeler à sa convenance. Je peux transcender ces limites factices.L'univers est un tout.Je suis un membre d'un tout, d'une circulation d'énergie en harmonie"
Zhen.foci = "Chants tibétains, Do, Tai-Chi, Bâton de combat, Prières, Médidation, Cuisine"
Zhen.physique = "Zehn est un homme d'une trentaine d'années athlétique. Il s'habille dans un style urbain discret et porte une chevalière en argent à l'annulaire droit."
Zhen.attitude = "C'est un mec fiable et ça se sent. Zehn est sociable même si il est parfois brut dans ces propos. Il ne supporte pas l'inégalité et n'hésitera pas à intervenir pour protéger les plus faibles"

Zhen.setAttributes([4,3,2,1, 3,2,2,1])
Zhen.setCapacities({ "Do":4,"Athlétisme":3,"Méditation":3,"Érudition":2,"Ésotérisme":2,"Cuisine":2,"Conduite":1,"Intimidation":1,"Vigilance":1,"Furtivité":1})
Zhen.setSpheres({Sphere.Forces:3, Sphere.Matière:2, Sphere.Prime:1})
Zhen.setEveil(3)
Zhen.setAtouts({"Insensible à la douleur":5, "Force intérieure":2 })
Zhen.setHandicaps({"Sauveur":-3, "Sensibilité à l'alcool":-2,"Problèmes familiaux":-1})
#Zhen.display()

Zhen.upgradeSphere(Sphere.Prime)
Zhen.upgradeAttribute(Attribut.Charisme)
Zhen.upgradeAttribute(Attribut.Empathie)
Zhen.upgradeCapacity("Do")
Zhen.upgradeHistorique("Influence(Réseaux Sociaux)")
Zhen.upgradeHistorique("Culte")
Zhen.upgradeHistorique("Node")
Zhen.upgradeHistorique("Node")
Zhen.upgradeHistorique("Node")
Zhen.upgradeHistorique("Statut")
Zhen.upgradeHistorique("Statut")

#Zhen.display()
Zhen.grantExp(6, "Mars 2022")

########################################################################################################################
ccc = Mage("Christian Rosenkreutz", "Mage", "Ordre d'Hermes", "4oMJepwm")
ccc.concept = "Quintescence de sa faction, il incarne un hubrys froid et dur de l'élitisme. D'apparence aristocratique et poli à l'outrance, rigide et exhaustif, presque méprisant avec une pédagogie cassante, mais efficace, Christian est d'attitude un noble, mais de coeur un chercheur de vérité, curieux et ouvert d'esprit, avec une certaine poésie, mais dont la voracité intellectuelle est troublante."
ccc.paradigme = "Le monde est né du Logos, de l'or parfait, il s'est brisé, détioré, mélangé à la matière et à l'esprit. Oui, bien des choses sont arrivées depuis la Création Eternelle, mais Christian sait que les avatar sont les graines éveillés du Premier des Êtres. Par là, chaque mage peut exercer sa vérité en se basant sur sa croyance et sa connaissance. Il faut affûter son esprit par milles usage, entretenir un corps sain et nourrir son âme pour créer sa Vérité et devenir à son tour, ce que certaines nomment \"Dieu.\" Ce n'est là qu'un concentré de surface des pensées de ce mage tragique et détaché des choses, sauf pour les menus plaisir de la vie."
ccc.foci = "alchimie, géométrie sacrée, symboles, gestes, incantations, outils de rituels, numérologie, sang, vrais noms, démonologie, domination sociale"
ccc.physique = "Des cheveux d'or, des yeux bleus affutés, un sourire de politesse aux lèvres, Christian incarne un autre temps. Son port altier le met toujours en valeur, que cela soit dans un tenue armani sur-mesure ou dans une chemise détendue. Pour autant, cette attitude parfaite, selon les canons de la belle société, pourrait en pertuber plus d'un en-dehors de son milieu."
ccc.attitude = ""

ccc.setAttributes([1,2,2,4, 2,3,3,1])
ccc.setCapacities({ "Esotérisme":4,"Médecine":3,"Occultisme":3,"Langue":2,"Etiquette":2,"Erudtion":2,"Commandement":1,"Subterfuge":1,"Vigilance":1,"Technologie":1})
ccc.setSpheres({Sphere.Prime:3, Sphere.Esprits:2, Sphere.Psyché:1})
ccc.setEveil(3)
ccc.setAtouts({"Chef Naturel":2, "Trait Enchanteur(Voix)":2, "Port Altier":1, "Calcul Mental":1 , "Aura ardente":1})
ccc.setHandicaps({"Hors réseaux":-3,"Echo":-1, "Marquant(Odeur Myrrhe)":-1, "Conspirateur":-1, "Diablotin":-1, "Apprenti":-1})

#ccc.display()

ccc.upgradeCapacity("Informatique")
ccc.upgradeCapacity("Commandement")
ccc.upgradeHistorique("Prodige")
ccc.upgradeHistorique("Prodige")
ccc.upgradeHistorique("Prodige")
ccc.upgradeHistorique("Prodige")
ccc.upgradeHistorique("Prodige")
ccc.upgradeHistorique("Ressources")
ccc.upgradeHistorique("Ressources")
ccc.upgradeHistorique("Ressources")
ccc.upgradeHistorique("Statut")
ccc.upgradeHistorique("Statut")
ccc.printExp()

#ccc.display()

ccc.grantExp(6, "Mars 2022")
ccc.upgradeHistorique("Node")
ccc.printExp()
#ccc.display()

########################################################################################################################
suiko = Mage("Suiko KINKO", "Mage", "Verbena", "AXKbDovm")
suiko.concept = "Tatouese/Caligraphe fanatique"
suiko.paradigme = "Les dieux existent et leurs energie se canalyse dans leur sang et modele le monde depuis la nuit des temps. En insulfant de l'intention et de la croyance dans le sang, il est possible de diriger cette energie pour modeler la realite. La force mentale se transmet dans le sang, c'est un peu le liquide de l'ame."
suiko.foci = "SK pense etre descendante d'un dieu et son pouvoir est dans ses veines. Elle peut utiliser son sang pour ecrire et en y mettant croyance et intention elle peut changer la realite. Elle dilue son sang dans l'encre en faisant une ceremonie pour rendre ses capacites a durer limite, mais en l'utilisant dans un tatoo ou en utilisant sont sang directement, elle ancre cette energie dans le corp de l'objet ou la personne"
suiko.physique = "Elle a la trentaine, percings un peu partout, on peut voire ses bras et orbites tatoue avec une encre, ainsi que son front. Son style est un melange de streetwear et de Kimono. Elle a un constant sourire qui semble plus inquietant que sympatique."
suiko.attitude = "Elle sait qu'elle est superieur et tant qu'on lui montre le respect qu'elle merite elle sera sympatique surtout si c'est pour faire affaire. Pour les gens de sa famille, sont attitude est plus maternel et protectrice"
suiko.setAttributes([1,4,3,2, 2,2,1,3])
suiko.setCapacities({ "Commandement":4})
suiko.setCapacities({"Subterfuge":3,"Médecine":3})
suiko.setCapacities({"Exp.Rue":2,"Séduction":2,"Manipulation":2})
suiko.setCapacities({"Art":1,"Langues":1,"Ésotérisme":1,"Méditation":1})
suiko.setSpheres({Sphere.Vie:3, Sphere.Matière:2, Sphere.Psyché:1})
suiko.setEveil(3)
suiko.setAtouts({"Assurance":2, "Don artistique":1, "Prestige":2 })
suiko.setHandicaps({"Délit de sale gueule":-2,"Marquant":-3})
#suiko.display()


suiko.upgradeHistorique("Alliés(Mon Gang)")
suiko.upgradeHistorique("Alliés(Mon Gang)")
suiko.upgradeHistorique("Alliés(Mon Gang)")
suiko.upgradeHistorique("Alliés(Mon Gang)")
suiko.upgradeHistorique("Contacts(Gangs)")
suiko.upgradeHistorique("Contacts(Gangs)")
suiko.upgradeHistorique("Contacts(Gangs)")
suiko.upgradeHistorique("Ressources")
suiko.upgradeHistorique("Ressources")
suiko.upgradeHistorique("Ressources")
suiko.upgradeHistorique("Ressources")
#suiko.display()

########################################################################################################################
kiozan = Mage("Kiōzan Mamu", "Mage", "Wu-Lung", "AgxDZJV4")
kiozan.concept = "Ex-sumo devenu yakuza faisant des combats clandestins"
kiozan.physique = "Il a gardé son physique massif de sumo mais s'est rasé le crâne depuis qu'il est arrivé aux USA. Il aime exhiber fièrement ses tatouages quand il en a l'occasion et ne retire jamais l'énorme chaîne en or qu'il porte autour du cou."
kiozan.attitude = "Il n'a peur de (presque) personne, son gabarit impressionnant aidant ; il est très fidèles aux personnes envers qui il a confiance ; généralement calme et assez stoïque, il est capable de partir dans des accès de colère et de violence qu'il a du mal à contrôler."

kiozan.paradigme = "Depuis qu'il a vu ce qu'il craint être l'Enfer, sa plus grande terreur est que ça puisse devenir la réalité. C'est pour ça que, malgré l'agréable sentiment de puissance que lui procure l'utilisation de sa magie, il s'efforce de s'en servir avec parcimonie, de peur de convoquer des forces qu'il ne maîtriserait pas"
kiozan.foci = "Par les extrémités de son corps (mains, tête, ou pieds), Mamu est capable d'augmenter la température jusqu'à enflammer ou faire bouillir les choses. Il considère sa grosse chaîne en or comme un régulateur de ce pouvoir, bien que ce soit un verrou psychologique qu'autre chose, Mamu est persuadé qu'il serait incapable de retirer sa magie s'il ne la portait pas. Il semble qu'il soit aussi capable d'influencer sur d'autres éléments ou encore sur la gravité, mais dans une bien moindre mesure."

kiozan.setAttributes([4,2,3,2, 1,1,2,3])
kiozan.setCapacities({ "Bagarre":4})
kiozan.setCapacities({"Arts Martiaux":3,"Vigiliance":3})
kiozan.setCapacities({"Exp.Rue":2,"Armes à feu":2,"Intimidation":2})
kiozan.setCapacities({"Instinct":1,"Etiquette":1,"Mêlée":1,"Survie":1})
kiozan.setSpheres({Sphere.Forces:3, Sphere.Espace:2, Sphere.Entropie:1})
kiozan.setEveil(3)
kiozan.setAtouts({"Taille gigantesque":4, "Estomac de fer":1, "Physique impressionnant":2 })
kiozan.setHandicaps({"Flash-back":-3,"SSPT":-2, "Colérique":-2})

#kiozan.display()
print("_")
kiozan.upgradeAttribute(Attribut.Force)
kiozan.upgradeCapacity("Arts Martiaux")
kiozan.upgradeCapacity("Exp.Rue")
kiozan.upgradeCapacity("Intimidation")
kiozan.upgradeHistorique("Contacts(Combats clandestins)")
kiozan.upgradeHistorique("Contacts(Combats clandestins)")
kiozan.upgradeHistorique("Influence[Economie](Industrie)")
kiozan.upgradeHistorique("Influence[Economie](Industrie)")
kiozan.upgradeHistorique("Influence[Economie](Industrie)")
kiozan.upgradeHistorique("Prodige")
print("_")
#kiozan.display()



########################################################################################################################
washi = Mage("Washi", "Mage", "Orphelin", "mpQM2GkA")
washi.concept = "Jeune orpheline assassin par origami"
washi.physique = "Japonaise de 1m60, plutôt athlétique au teint pâle. Ses cheveux bleu corbeaux sont long et vont jusqu’au genoux quand elle les détaches. Elle porte toujours des parures dans ses cheveux faites de fleurs en papiers.Des percings aux oreilles et un petit dans le nez.On voit sur des parties dénudés dès tatouages à l’encre rouge."
washi.attitude = "taciturne, froide, calme"

washi.paradigme = "Le monde est kamis. Je leur parle et les honore et ils me prêtent leur force pour accomplir mes desseins."
washi.foci = "Par des prières et des pliages précis, je sais doter mes oeuvres de propriétés extraordinaires comme des fleurs qui endorment, une lame de papier tranchante."

washi.setAttributes([1,3,3,2, 4,2,2,1])
washi.setCapacities({ "Art(Origami)":4})
washi.setCapacities({"Arts Martiaux":3,"Esotérisme":3})
washi.setCapacities({"Exp.Rue":2,"Occultisme":2,"Vigiliance":2})
washi.setCapacities({"Instinct":1,"Athlétisme":1,"Intimidation":1,"Survie":1})
washi.setSpheres({Sphere.Vie:3, Sphere.Matière:2, Sphere.Espace:1})
washi.setEveil(3)
washi.setAtouts({"Neuf vies":6, "Concentration":1 })
washi.setHandicaps({"Marquée":-5,"Froid":-2})

#washi.display()
#print("_")
washi.upgradeSphere(Sphere.Espace)
washi.upgradeHistorique("Fausse identité")
washi.upgradeHistorique("Fausse identité")
washi.upgradeHistorique("Fausse identité")
washi.upgradeHistorique("Rang")
washi.upgradeHistorique("Rang")
washi.upgradeHistorique("Familier")
washi.upgradeHistorique("Familier")
washi.upgradeHistorique("Familier")
#print("_")

#washi.display()

########################################################################################################################
sybille = Mage("Sybille Andernikos", "Mage", "Euthanatos: Chakravanti", "AXKylpzm")
sybille.concept = "Prêtre du destin (Parque)"

sybille.physique = " Bientôt la trentaine, Sibylle est une personne au physique androgyne qui pourrait sembler tout à fait invisible dans le monde l’entreprise. Son costume trois pièces implacablement repassé n’est perturbé que par la présence deux éléments : une broche en forme de caducée qu’elle semble toucher à chaque déplacement et le tintement des galets des galets qu’elle transporte dans les poches de son costume."
sybille.attitude = "Sibylle est de prima bord un personnage plutôt froid et dont il se dégage une étrange attitude corporatiste de par son apparence physique, son regard inquisiteurs semblent ne pas vous voir mais regarder à travers-vous pour observer quelque chose d’imperceptible, ce qui peut pour un premier contact mettre les gens mal à l’aise. Cependant après quelques échanges tentés d’un léger accent grecque, cette façade laisse place à une personne polie à l’écoute des autres et prête à leur prêter main forte s’ils ne font pas preuve d’hubris mal placé."

sybille.paradigme = "Ordre divin chaos terrestre/des dieux et des monstres. De Chaos vient la création et de ses entrailles jaillirent les premiers titans qui façonnèrent la terre avant de trahir leur père, perpétuant le chaos, puis leurs fils trahirent les titans, plongeant de nouveau le monde dans le chaos. Mais il est un ordre caché dans ce spectacle chaotique, l’ordre du destin, nul ne peut y échapper, ni homme, ni dieu. Tous se voient offert leur lot avant que les Moires ne frappent pour vous faire rejoindre le cycle. Le seul espoir des hommes est d’être exceptionnels, de dépasser leurs potentiels sans sombrer dans l’hubris, ils pourront alors accéder aux champs Élysées et quitter le grand cycle. Pour les esclaves de l’hubris, leur destin est d’être broyé par la roue du destin et d’être renvoyé en Hadès pour réintégrer le cycle une fois qu’ils seront purifiés. Il faut donc pousser l’humanité à se surpasser et ne pas se piéger elle-même dans la stagnation."
sybille.foci = "Instruments: Bénédictions et malédictions, potions et décoctions, alignement céleste, nourriture et boissons, jeux, rites de groupes, herbes et plantes, offrandes et sacrifices, prières et invocations, symboles, baguettes et bâtons."
sybille.foci += "Bénédiction et malédictions: Les Moires dictent le début et la fin de votre vie, mais le reste de votre vie est dicté par les bénédictions et les malédictions des dieux sur ta maison. Comprends les mots secrets et leur art pour manipuler les fils du destin avant qu’ils ne soient coupés."
sybille.foci += "Potions et décoctions: Transformer une chose en une autre est un secret qui a été transmis des dieux aux hommes. Transformer le doux raison en une boisson enivrante capable de briser votre perceptions et vos inhibitions n’est qu’un exemple parmi tant d’autre. L’art d’Hécate est à manier avec précautions car les arts magiques peuvent être aussi être une source de mort."
sybille.foci += "Alignement céleste: Le katasterismoi s’étend dans le ciel nocturne comme un héritage des dieux et de leurs accomplissements. Le passé, présent et futur est caché dans le ciel et l’ont peut en tirer du pouvoir."
sybille.foci += "Nourriture et boisson: Les hommes et les dieux ont besoin de substance pour survivre. Donnes leur de la nourriture pour montrer ta dévotion, mange et partage la nourriture avec tes convives pour être unifiés sous l’œil des dieux. A moins de rendre hommage aux khthonios, laisse la nourriture et la boisson pour eux et eux seuls."
sybille.foci += "Jeux: Les dieux ont donner vie et pouvoirs aux hommes. Les jeux nous permettent d’honorer ces dons en montrant notre force, notre détermination et notre intelligence attirent l’œil des dieux."
sybille.foci += "Rites de groupes: Vénérer les dieux est une activité sociale où tous prennent part pour montrer aux dieux qu’ils ne sont pas oubliés. Ce sont nos liens qui montrent notre foi envers eux."
sybille.foci += "Herbes et plantes: la flore a toujours eut une place particulière dans l’histoire humaine, comme source de vie, de merveille et de mort. De nombreuses plantes sont le produit des dieux par jalousie, colère ou par tragédie."
sybille.foci += "Offrandes et sacrifices: Donnes aux dieux et les dieux t’entendrons, donnes leurs le produit de la terre et les animaux pour alimenter ton appel aux immortels."
sybille.foci += "Prières et invocations: honore les dieux de tes mots et prières, chante leurs noms pour les atteindre en Hadès ou sur Olympes, mais pèses tes mots car les immortels sont capricieux."
sybille.foci += "Symboles: Ils ont un sens pour les dieux et nous rappellent leurs présences et leurs pouvoirs dans le monde des hommes. La chouette symbole d’Athéna nous rappelle sa sagesse, la flamme de Prométhée nous rappel le pouvoir de la création. Nous utilisons ces symboles comme une inspiration de pouvoir."
sybille.foci += "Baguettes et bâtons: les baguettes et bâtons ont de tout temps symbolisé la puissance du magicien, c’est la baguette de Circé qui a transformé les compagnons d’Ulysse en animaux, c’est le caducée d’Hermès qui focalise son pouvoir de guérison. Ces outils sont une part indéniable du pouvoir du mage."

sybille.setAttributes([1,2,4,2, 3,3,2,1])
sybille.setCapacities({"Occultisme":4})
sybille.setCapacities({"Ésotérisme":3,"Investigation":3})
sybille.setCapacities({"Recherche":2,"Instinct":2,"Armes à feu":2})
sybille.setCapacities({"Droit":1,"Vigiliance":1,"Haut-Rituel":1,"Langues":1})
sybille.setSpheres({Sphere.Esprits:3, Sphere.Entropie:2, Sphere.Espace:1})
sybille.setEveil(3)
sybille.setAtouts({"Messager respecté":3, "Concentration":1, "Medium":2 }) #Medium:2, Affinité céleste, Sagesse du juge, Mentor prestigieux, Messager respecté.
sybille.setHandicaps({"Tics":-1,"Curiosité":-2,"Echos":-1, "Regression":-2})
#sybille.display()


sybille.upgradeCapacity("Etiquette")
sybille.upgradeCapacity("Athlétisme")
sybille.upgradeCapacity("Haut-Rituel")
sybille.upgradeHistorique("Ressources")
sybille.upgradeHistorique("Ressources")
sybille.upgradeHistorique("Ressources")
sybille.upgradeHistorique("Rang")
sybille.upgradeHistorique("Influence(Politique)")#Juridique
sybille.upgradeHistorique("Influence(Politique)")#Législatif
sybille.upgradeHistorique("Culte") #Paganisme, grec. Action culturelle, mais avec vénération religieuse. Tissu social.
sybille.upgradeHistorique("Culte")
sybille.upgradeHistorique("Node")
sybille.upgradeHistorique("Node")
sybille.upgradeHistorique("Allié")
sybille.upgradeHistorique("Allié")
sybille.upgradeHistorique("Allié")
sybille.upgradeHistorique("Mentor")

#sybille.display()

########################################################################################################################
salome = Mage("Salomé Morin", "Mage", "Culte de l'extase", "mLNvOR84")
salome.concept = "Reine de la nuit et derviche de l'extase"

salome.physique = "Femme approchant de la trentaine au physique athlétique, Salomé est une personne à l'allure envoutante mise en valeur par un corps couvert de tatouages formant de complexes motifs géométriques semblant se mouvoir au rythme de ses gestes."
salome.attitude = "A première vue Salomé peut sembler désinvolte, provocatrice. Et elle l’est sans le moindre doute face à la banalité du quotidien. Amicale, séductrice et chaleureuse, elle ne porte aucun jugement sur les individus, veillant elle-même à mener une vie débridée comme bon lui semble. Mais derrière ce masque de surface se dissimule une rigueur et une intransigeance à son égard et à l'égard de ceux qu’elle estime. Les apparats n’ont aucune importance de la même manière que les paroles, seuls les actes semblent avoir de la valeur à ses yeux pour ceux qui apprennent."
salome.paradigme = "En tant qu’extatique, Salomé s’inscrit ne serait-ce qu’en partie dans le paradigme de son culte. Mais en opposition avec la tradition du culte, elle trouve l’extase avant tout à travers la sexualité, la souffrance, la saturation des sens et l’épuisement physique. Elle obtient la  véritable jouissance à travers ces état, par cette jouissance atteint ce qu’elle considère comme une véritable extase et, par cette extase manifeste pleinement son égo. Et par son égo elle permet à sa réalité de s’imposer à celle du monde."
salome.foci = "Les foci principaux de Salomé sont les pratiques sexuelles extrêmes (sadomasochisme, bondage, shibari), la consommation de drogues couplée à l’écoute de musique (à des volumes assourdissant), la fête débridée sans aucune retenue, la danse jusqu’à épuisement mais aussi la méditation et la pratique du yoga. Les pratiques traditionnelles du culte de l’extase sont quant à elles secondaires et ne servent qu’aux actes de magye mineures ou utilitaires"

salome.setAttributes([1,3,2,3, 4,1,2,2])
salome.setCapacities({"performer extreme (sexe)":4})
salome.setCapacities({"Art":3,"Athlétisme":3})
salome.setCapacities({"Séduction":2,"Méditation":2,"Ésotérisme":2})
salome.setCapacities({"Exp.Rue":1,"Instinct":1,"Vigilance":1,"Édudition":1})
salome.setSpheres({Sphere.Temps:3, Sphere.Vie:2, Sphere.Psyché:1})
salome.setEveil(3)
salome.setAtouts({"Souplesse du serpent":1, "Tolérance à l'alcool/drogues":2, "Traits enchanteurs":2, "Initié d'une sous-culture":2})
salome.setHandicaps({"Apprenti":-1, "Ennemi":-1, "Curiosité":-2, "Pratiques sexuelles extrêmes":-3})
#salome.display()
#print("_")

salome.upgradeAttribute(Attribut.Force)
salome.upgradeAttribute(Attribut.Logique)
salome.upgradeCapacity("Langues")
salome.upgradeCapacity("Occultisme")
salome.upgradeSphere(Sphere.Prime)
salome.upgradeHistorique("Renommée")
salome.upgradeHistorique("Node")
salome.upgradeHistorique("Culte")
salome.upgradeHistorique("Culte")
salome.upgradeHistorique("Ressources")
salome.upgradeHistorique("Ressources")
salome.upgradeHistorique("Ressources")
salome.upgradeHistorique("Rang")
salome.upgradeHistorique("Rang")
salome.upgradeHistorique("Rang")
#print("_")
#salome.display()
salome.printExp()

########################################################################################################################
john = Mage("John", "Mage", "???", "4kxXOERd")
john.concept = "Meta Psyché Evangeliste"

john.physique = "Personne non genrée, dans la trentaine. Peut être vu en homme, en femme, en androgyne. Environ 1,70m, plutôt fin."
john.attitude = "Véritable animal social qui adore se mêler dans la foule. Air aimable et souriant. S'adapte beaucoup à son interlocuteur, peut aussi bien être un moulin à paroles qu'une bonne oreille pour écouter."

john.paradigme = "John voit la fluidité ultime entre les êtres comme un retour vers le Lifestream originel [si tu penses à un meilleur mot, fais-moi signe], qui alimentait toute chose. Ainsi, tout se qui se trouvait sur Terre formait l'Un, toute action de toute chose de déroulait de façon naturelle, un peu comme un être vivant respire sans y penser, ou comme les rouages d'un mécanisme bien huilé. Mais les êtres humains sont devenus faibles, ils ont cédés à une volonté d'individualité et de dominance, ce qui a créé des séparations entre eux et avec les autres êtres selon plusieurs critères (plus fort VS plus faible, plus riche VS plus pauvre, plus intelligent VS plus bête, humain VS animal, etc.). Tout cela a brisé le Lifestream/l'Un, et bien qu'il reste en chacun d'entre nous, il ne peut pas se reformer tel quel, tant que les humains seront individus, séparés."
john.foci = "Discours analytique, captation video et observation language corporel, drogues psychotropes, séduction voir sexe."

john.setAttributes([1,2,2,3, 3,1,2,4])
john.setCapacities({"Expression":4})
john.setCapacities({"Manipulation":3,"Séduction":3})
john.setCapacities({"Art()":2,"Etiquette":2,"Langues":2})
john.setCapacities({"Esotérisme":1,"Occultisme":1,"Technologie":1,"Commandement":1})
john.setSpheres({Sphere.Psyché:3, Sphere.Espace:2, Sphere.Prime:1})
john.setEveil(3)
#john.setAtouts({"Souplesse du serpent":1, "Tolérance à l'alcool/drogues":2, "Traits enchanteurs":2, "Initié d'une sous-culture":2})
#john.setHandicaps({"Apprenti":-1, "Ennemi":-1, "Curiosité":-2, "Pratiques sexuelles extrêmes":-3})
#john.display()



#Ici se tiendra l'historique complet de l'évolution de votre fiche

#Distribution mensuelle d'xp:
theodora.grantExp(3, "Avril 2022")
Zhen.grantExp(6, "Avril 2022")
ccc.grantExp(6, "Avril 2022")
suiko.grantExp(6, "Avril 2022")
kiozan.grantExp(6, "Avril 2022")
washi.grantExp(6, "Avril 2022")
sybille.grantExp(6, "Avril 2022")
salome.grantExp(6, "Avril 2022")
john.grantExp(6, "Avril 2022")

kiozan.display()

sybille.upgradeHistorique("Influence(Religion)")

washi.upgradeHistorique("Influence(Rue)")
washi.display()


ccc.upgradeHistorique("Node")



# Mai

#Distribution mensuelle d'xp:
#theodora.grantExp(3, "Mai 2022")
#Zhen.grantExp(6, "Mai 2022")
ccc.grantExp(6, "Mai 2022")
suiko.grantExp(6, "Mai 2022")
#kiozan.grantExp(6, "Mai 2022")
washi.grantExp(6, "Mai 2022")
sybille.grantExp(6, "Mai 2022")
#salome.grantExp(6, "Mai 2022")
john.grantExp(6, "Mai 2022")

washi.upgradeHistorique("Influence(Rue)")

suiko.upgradeHistorique("Influence(Politique)")
suiko.upgradeHistorique("Influence(Rue)")













ava = Mage("Ava", "Mage", "Disparate", "Oprheline")
ava.concept = "La mort n'est qu'une étape, la biologie, l'intelligence artificielle est la voie pour l'apogée finale de tous dans le transhumanisme."

ava.physique = "Jeune femme d'une 20aine d'années, toujours avec tu matos informatique dernier cris, toujours afublée de lunettes très cyber et d'une combinaison moulante à LED. Elle a aussi un tatouage représentant une sorte de matrice sur le torse."
ava.attitude = "Réservée, discrète, plus à l'aise derrière un clavier qu'en contact avec les gens."

ava.paradigme = "Pour moi le monde est une immense toile numérique, cette toile est modifiable, malléable, altérable avec la magie."
ava.foci = "Mon art Magyque s'exprime à travers les réseaux quels qu'ils soient, informatique, électrique, un cours d'eau, un câble électrique, tout est connexion.\
Mes focus sont ma console informatique, ma combinaison, un data jack, le wifi/blutooth, mes lunettes, on peut aussi inclure des tracés sur support comme mon tatouage sur le torse."

ava.setAttributes([1,2,2,2, 3,3,4,1])
ava.setCapacities({"Informatique":4})
ava.setCapacities({"Technologie":3,"BioTechnologie":3})
ava.setCapacities({"'Furtivité":2,"Recherche":2,"Sciences":2})
ava.setCapacities({"Exp.Rue":1,"Vigilance":1,"HyperTechnologie":1,"Médecine":1})
ava.setSpheres({Sphere.Espace:3, Sphere.Forces:2, Sphere.Prime:1})
ava.setEveil(3)
ava.setAtouts({"Sens du danger":3, "Officiellement mort":2, "Bosse de l'informatique":1, "Quelconque":1})
ava.setHandicaps({"Dégénérescence":-3, "Assemblage":-2, "Ennemi":-2})

ava.display()


ava.upgradeHistorique("Fausse identité")
ava.upgradeHistorique("Fausse identité")
ava.upgradeHistorique("Fausse identité")

ava.upgradeHistorique("Culte")

ava.upgradeHistorique("Prodige")
ava.upgradeHistorique("Prodige")
ava.upgradeHistorique("Prodige")

ava.upgradeHistorique("Allié")
ava.upgradeHistorique("Allié")
ava.upgradeHistorique("Allié")

ava.upgradeCapacity("Vigilance")
ava.upgradeCapacity("Exp.Rue")
ava.upgradeCapacity("Médecine")
ava.upgradeCapacity("Sport")
ava.upgradeCapacity("Arme à feu")
#ava.display()













Mac = Mage("Victor Lacroix(Mac)", "Mage", "Fils de l'Ether", None)
Mac.concept = "Un héros du quotidien qui cherche à briser la glace malgré sa timidité (calmer des tensions, faire la paix, 'soigner les peurs' liées aux clichés, …"

Mac.physique = "- Jeune homme de 28 ans, les cheveux en bataille, possédant une sorte de ceinture de sac-banane qui dénote concernant la mode des jeunes d'aujourd'hui, qui lui sert principalement de boite à outils.\
- 1m75, d'une carrure relativement moyenne, il ne possède pas un charisme qui le caractérise d'une manière particulière. Physiquement, on pourrait l'appeler monsieur-tout-le-monde.\
- Pour quelqu'un le voyant tous les jours, on pourra remarquer que les yeux de Victor semblent changer d'un jour à l'autre (couleur et l'œil droit n'est pas forcément de la même couleur que l'œil gauche)"
Mac.attitude = "Plutôt à l'aise quand il s'agit de parler devant un oratoire acquis, mais assez nerveux quand il s'agit d'une conversation directe ou d'un rendez-vous. Quand il commence à patienter seul à un endroit, s'il est en pleine réflexion, Victor se laissera absorber par sa pensée et on pourrait croire qu'il a le regard dans le vide, si par contre il attend quelqu'un ses doigts de la main droite s'agitent comme si Victor était en train de composer une mélodie sur un piano. Elevé par des parents français, on pourra dénoter un accent de métropolitain même s'il n'est jamais sorti de San Francisco."

Mac.paradigme = "Victor pense que notre monde physique n'est qu'une partie de ce que nous sommes. Quand nous dormons, humains (comme les autres êtres) rêvons et pouvons mieux nous comprendre à travers notre rêverie qui circulerait à travers l'Ether qui est la surcouche de notre Univers Physique. Fondamentalement, la physique (et possiblement l'informatique) nous permet de transcender l'état de la Réalité telle que nous la voyons. La clef de l'Illumination est cachée quelque part de l'autre côté, celui où seuls les élus osent regarder ou se rendre."
Mac.foci = "1 - Pour la sphère de la Matière, il pourrait s'agir de résidus de poudre de la même nature que les matériaux que j'aimerai manipuler (poudre de fer pour des métaux, poudre d'ossement pour un corps sans vie, …)\
2 - Des assemblages complexes (un peu comme un outils d'un technocrate, style un pistolet d'où je canaliserais un tir) pourraient être nécessaires pour réaliser des artifices issus de la sphère de Force.\
3 - Des équations complexes peuvent être à tracer sur le sol à la craie concernant les Arts de la Correspondance.\
4 - L'art de la numérologie et des mathématiques (pas le tarot ou la divination mais plutôt les calculs et les assemblages d'analyste) me permettrait de juxtaposer ma définition du Temps et des maths.\
5 - Des manipulations chimiques (me permettant de fabriquer des drogues, …) peuvent être la clef d'utilisation de la Psyché.\
6 - L'utilisation de livres dédiés aux recherches sur les théories de Lorentz servira à manipuler la sphère d'Esprit.\
7 - Etant un être Eveillé (qui a donc accès en partie à l'Ether selon mon point de vue), une utilisation de mon sang (ou de celui d'un être éveillé) me permettrait d'accéder à la sphère de Prime."


Mac.setAttributes([1,2,2,1, 3,3,4,2])
Mac.setCapacities({"Sciences":4})
Mac.setCapacities({"Artisanats":3,"Éridition":3})
Mac.setCapacities({"Recherche":2,"Langues":2,"Technologie":2})
Mac.setCapacities({"Informatique":1,"Étiquette":1,"Droit":1,"Médecine":1})
Mac.setSpheres({Sphere.Matière:3, Sphere.Prime:2, Sphere.Psyché:1})
Mac.setEveil(3)
Mac.setAtouts({"Hyper/attention":3, "Don pour les langues":2, "Quelconque":1, "Boss de la mécanique":1})
Mac.setHandicaps({"Phobie administrative":-4, "Mauvaise vue":-2, "Infamie":-1})

Mac.display()

Mac.upgradeAttribute(Attribut.Force)
Mac.upgradeCapacity("Vigilance")
Mac.upgradeCapacity("Subterfuge")

Mac.upgradeSphere(Sphere.Esprits)
Mac.upgradeSphere(Sphere.Psyché)
Mac.upgradeAttribute(Attribut.Charisme)

Mac.upgradeHistorique("Culte")
Mac.upgradeHistorique("Influence(Scientifique)")
Mac.upgradeHistorique("Influence(Scientifique)")
Mac.upgradeHistorique("Influence(Politique)")
Mac.upgradeHistorique("Influence(Politique)")
Mac.upgradeHistorique("Influence(Media)")
Mac.upgradeHistorique("Influence(Economie)")
Mac.upgradeHistorique("Mentor")
Mac.upgradeHistorique("Ressouces")




Mac.display()

#Mac.setEveil(4)

#john.display()
















# Juin 2022

#Distribution mensuelle d'xp:
#theodora.grantExp(3, "Juin 2022")
Zhen.grantExp(6, "Juin 2022")
ccc.grantExp(6, "Juin 2022")
suiko.grantExp(6, "Juin 2022")
#kiozan.grantExp(6, "Juin 2022")
washi.grantExp(6, "Juin 2022")
sybille.grantExp(6, "Juin 2022")
#salome.grantExp(6, "Juin 2022")
john.grantExp(6, "Juin 2022")

ava.grantExp(3, "Juin 2022")
Mac.grantExp(3, "Juin 2022")


washi.upgradeHistorique("Influence(Rue)")




Zhen.grantExp(3, "Juillet 2022")
suiko.grantExp(3, "Juillet 2022")
washi.grantExp(3, "Juillet 2022")
sybille.grantExp(3, "Juillet 2022")
john.grantExp(3, "Juillet 2022")
ava.grantExp(3, "Juillet 2022")
Mac.grantExp(3, "Juillet 2022")
