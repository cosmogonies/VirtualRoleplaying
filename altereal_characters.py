#!/usr/bin/python
import pprint
import enum

def prettify(_str):
   return str(_str).replace('[\'','').replace('\']','').replace('\'','')


# Using enum class create enumerations
class Nature(enum.Enum):
   Humain = 0
   Mage = 1
   Technocrate = 2
   Misc = 3
# printing all enum members using loop
#print ("The enum members are : ")
#for weekday in (Days):
#   print(weekday)


class Attribut(enum.Enum):
   Force = 1
   Dextérité = 2
   Perception = 3
   Charisme = 4

   Volonté = 5
   Logique = 6
   Mémoire = 7
   Empathie = 8


class Sphere(enum.Enum):
   Prime = 0
   Forces = 1
   Matière = 2

   Espace = 3
   Temps = 4

   Vie = 5
   Entropie = 6

   Psyché = 7
   Esprits = 8


class Character:
   'Common base class for all characters'
   name = "No0ne"
   player = None

   #nature = Nature.Humain
   faction = ""#Mage
   affiliation = "" #Tradition
   concept = ""
   physique = ""
   attitude = ""

   xp = 200

   attributs = {}
   capacités = {}
   spécialité = {}
   historique = {}
   #spheres = {}
#   eveil = 0
   atouts = {}
   handicaps = {}

   def __init__(self, name, _player=None): #, nature):
      self.name = name
      self.player = _player

      self.attributs = {}
      self.capacités = {}
      self.spécialité = {}
      self.historique = {}
      self.atouts = {}
      self.handicaps = {}

      #Attributs
      self.attributs[Attribut.Force] = 1
      self.attributs[Attribut.Dextérité] = 1
      self.attributs[Attribut.Perception] = 1
      self.attributs[Attribut.Charisme] = 1

      self.attributs[Attribut.Volonté] = 1
      self.attributs[Attribut.Logique] = 1
      self.attributs[Attribut.Mémoire] = 1
      self.attributs[Attribut.Empathie] = 1

      #Talents
      self.capacités["Art"] = 0
      self.capacités["Sport"] = 0
      self.capacités["Bagarre"] = 0
      self.capacités["Commandement"] = 0
      self.capacités["Empathie"] = 0
      self.capacités["Expérience de la rue"] = 0
      self.capacités["Intimidation"] = 0
      self.capacités["Subterfuge"] = 0
      self.capacités["Vigilance"] = 0

      #Compétences
      self.capacités["Armes à feu"] = 0
      self.capacités["Artisanats"] = 0
      self.capacités["Arts martiaux"] = 0
      self.capacités["Conduite"] = 0
      self.capacités["Etiquette"] = 0
      self.capacités["Furtivité"] = 0
      self.capacités["Méditation"] = 0
      self.capacités["Mêlée"] = 0
      self.capacités["Recherche"] = 0
      self.capacités["Survie"] = 0
      self.capacités["Technologie"] = 0

      #Connaissances
      self.capacités["Érudition"] = 0
      self.capacités["Ésotérisme"] = 0
      self.capacités["Informatique"] = 0
      self.capacités["Investigation"] = 0
      self.capacités["Droit"] = 0
      self.capacités["Médecine"] = 0
      self.capacités["Occultisme"] = 0
      self.capacités["Manipulation"] = 0
      self.capacités["Sciences"] = 0


   def setAttributes(self, _list):
      for key in self.attributs:
         self.attributs[key] = _list[0]
         _list = _list[1:]
   def upgradeAttribute(self, _attribute):
      if(self.attributs[_attribute]==5):
         print("ERROR, cannot level-up maxed attribute")
      else:
         xpBefore = self.getSpentExp()
         self.attributs[_attribute] = self.attributs[_attribute] + 1
         print("\t Spent " + str(self.getSpentExp()-xpBefore).rjust(2,' ')+"xp [Attribute]\t\t"+ str(_attribute)+" \t("+ str(self.attributs[_attribute]-1) +" => "+str(self.attributs[_attribute])+")")


   def setCapacities(self, _dict):
      for key in _dict:
         value = _dict[key]
         self.capacités[key] = value
   def upgradeCapacity(self, _capacityName):
         if _capacityName in self.capacités:
            if(self.capacités[_capacityName]==5):
               print("ERROR, cannot level-up maxed capacity ("+_capacityName+")")
            else:
               xpBefore = self.getSpentExp()
               self.capacités[_capacityName] = self.capacités[_capacityName] + 1
               print("\t Spent " + str(self.getSpentExp()-xpBefore).rjust(2,' ')+"xp [Capacity]\t\t"+ str(_capacityName)+" \t("+ str(self.capacités[_capacityName]-1) +" => "+str(self.capacités[_capacityName])+")")
         else:
            xpBefore = self.getSpentExp()
            self.setCapacities({_capacityName:1})
            print("\t Spent " + str(self.getSpentExp()-xpBefore).rjust(2,' ')+"xp [Capacity]\t\t"+ str(_capacityName)+" \t(1)")

         
   def setHistorique(self, _dict):
      for key in _dict:
         value = _dict[key]
         self.historique[key] = value
   def upgradeHistorique(self, _historiqueName):
         if _historiqueName in self.historique:
            if(self.historique[_historiqueName]==5):
               print("ERROR, cannot level-up maxed historique ("+_historiqueName+")")
            else:
               xpBefore = self.getSpentExp()
               self.historique[_historiqueName] = self.historique[_historiqueName] + 1
               print("\t Spent " + str(self.getSpentExp()-xpBefore).rjust(2,' ')+"xp [Background]\t"+ str(_historiqueName)+" \t("+ str(self.historique[_historiqueName]-1) +" => "+str(self.historique[_historiqueName])+") Nouveau capital: "+self.ToExp())

         else:
            xpBefore = self.getSpentExp()
            self.setHistorique({_historiqueName:1})
            print("\t Spent " + str(self.getSpentExp()-xpBefore).rjust(2,' ')+"xp [Background]\t"+ str(_historiqueName)+" \t(1) Nouveau capital: "+self.ToExp())

   def setAtouts(self, _dict):
      for key in _dict:
         self.atouts[key] = _dict[key]
   def setHandicaps(self, _dict):
       for key in _dict:
         self.handicaps[key] = _dict[key]

   def displayHeader(self):
      #print("⎯"*66)
      print("⎯"*66)
      print("> ")
      print("> **"+self.name +"**")# ("+str(self.nature)+")" )
      print("> ")
      print("> "+self.faction +"(" +self.affiliation+")")
      print("> ")
      print("> *Concept:* "+self.concept)
      print("> *Physique:* "+self.physique)
      print("> *Attitude:* "+self.attitude)

   def display(self):
      #print("\tcontrolled by: "+self.player)
      self.displayAttributes()
      self.displayCapacités()
      self.displayBackground()
      self.displayAtoutsHandicaps()

   def displayAttributes(self):
      #print("Attributs:")
      #print(" ")
      print("> ⧍ Attributs ⧍")
      #for key in self.attributs:
      #   print("\t"+key+":"+str(self.attributs[key]))

      print("> \tForce:"+str(self.attributs[Attribut.Force])+"\t\tDextérité:"+str(self.attributs[Attribut.Dextérité])+"\tPerception:"+str(self.attributs[Attribut.Perception])+"\tCharisme:"+str(self.attributs[Attribut.Charisme]))
      print("> \tVolonté:"+str(self.attributs[Attribut.Volonté])+"\tLogique:"+str(self.attributs[Attribut.Logique])+"\tMémoire:"+str(self.attributs[Attribut.Mémoire])+"\t\tEmpathie:"+str(self.attributs[Attribut.Empathie]))

   def displayCapacités(self):
      #print(" ")
      print("> ⌘ Capacités ⌘")

      #for key in self.capacités:
      #   if(self.capacités[key]>0):
      #      print("\t"+key+":"+str(self.capacités[key]))

      # _sorted = sorted(self.capacités, key=self.capacités.get)
      # _sorted.reverse()
      # for key in _sorted:
      #    if(self.capacités[key]>0):
      #       print("\t"+key+":"+str(self.capacités[key]))

      lineBuffer = {5:[],4:[],3:[],2:[],1:[]}

      for key in self.capacités:
         if(self.capacités[key]>0):
            #lineBuffer[self.capacités[key]].append(key+":"+str(self.capacités[key]))
            lineBuffer[self.capacités[key]].append( key+"["+str(self.capacités[key])+"]" )

      if(len(lineBuffer[5])>0):print("> \t"+prettify(lineBuffer[5]))
      if(len(lineBuffer[4])>0):print("> \t"+prettify(lineBuffer[4]))
      if(len(lineBuffer[3])>0):print("> \t"+prettify(lineBuffer[3]))
      if(len(lineBuffer[2])>0):print("> \t"+prettify(lineBuffer[2]))
      if(len(lineBuffer[1])>0):print("> \t"+prettify(lineBuffer[1]))

      for key in self.spécialité:
         print("> \t(Spécialités)\t"+key+"["+str(self.capacités[key])+"]"+":"+str(self.spécialité[key]))



   def displayBackground(self):
      #print(" ")
      print("> 🗎 Historiques 🗎")
      lineBuffer = {5:[],4:[],3:[],2:[],1:[]}
      for key in self.historique:
         if(self.historique[key]>0):
            lineBuffer[self.historique[key]].append(key+":"+str(self.historique[key]))
      if(len(lineBuffer[5])>0):print("> \t"+prettify(lineBuffer[5]))
      if(len(lineBuffer[4])>0):print("> \t"+prettify(lineBuffer[4]))
      if(len(lineBuffer[3])>0):print("> \t"+prettify(lineBuffer[3]))
      if(len(lineBuffer[2])>0):print("> \t"+prettify(lineBuffer[2]))
      if(len(lineBuffer[1])>0):print("> \t"+prettify(lineBuffer[1]))

   def displayAtoutsHandicaps(self):
      #print(" ")
      print("> ⌛ Atouts&Handicaps ⌛")
      lineBuffer = "> \t"
      for key in self.atouts:
         lineBuffer += key+"["+prettify(self.atouts[key])+"], "
      lineBuffer += "\n> \t"
      for key in self.handicaps:
         lineBuffer += key+"["+prettify(self.handicaps[key])+"], "
      print(lineBuffer)


   def grantExp(self, value, _date):
      self.xp += value
      #print("\t Grant " + str(value).rjust(2,' ')+"xp (full pool = "+str(self.xp)+")") 
      print("["+_date+"] Tempus fugit ! \'"+self.name+"\' progresse de **"+str(value)+"**xp. (Nouveau capital: "+self.ToExp()+")")

   def ToExp(self):
      return str(self.xp-self.getSpentExp())+"/**"+str(self.xp)+"**"

   def printExp(self):
      print("> **XP:** "+self.ToExp())

class Mage(Character):
   def __init__(self, name, _faction, _affiliation, _player=None):

      super().__init__(name, _player)

      self.faction = _faction
      self.affiliation = _affiliation

      #self.name = name
      self.nature = Nature.Mage

      self.paradigme = ""
      self.foci = ""

      self.eveil = 1

      self.xp = 400


      #Spheres
      self.spheres = {}
      # self.capacités["Prime"] = 0
      # self.capacités["Forces"] = 0
      # self.capacités["Matière"] = 0
      # self.capacités["Temps"] = 0
      # self.capacités["Espace"] = 0
      # self.capacités["Vie"] = 0
      # self.capacités["Entropie"] = 0
      # self.capacités["Psyché"] = 0
      # self.capacités["Esprits"] = 0
      
      #self.spheres[Sphere.Prime] = 0
      #self.spheres[Sphere.Forces] = 3
      
      for s in Sphere:
         self.spheres[s] = 0

   def display(self):

      super(Mage,self).displayHeader()

      print("> ")
      print("> *Paradigme:* "+self.paradigme)
      print("> *Foci:* "+self.foci)
      print("> ")
      
      super(Mage,self).display()

      #print("\tForce:"+str(self.attributs[Attribut.Force])+"\tDextérité:"+str(self.attributs[Attribut.Dextérité])+"\tPerception:"+str(self.attributs[Attribut.Perception])+"\tCharisme:"+str(self.attributs[Attribut.Charisme]))
      #print("\tVolonté:"+str(self.attributs[Attribut.Volonté])+"\tLogique:"+str(self.attributs[Attribut.Logique])+"\tMémoire:"+str(self.attributs[Attribut.Mémoire])+"\tEmpathie:"+str(self.attributs[Attribut.Empathie]))

      #print(" ")
      print("> ◎ Sphères ◎")

      for key, value in self.spheres.items():
         if value == 5:
            print("> \t"+str(key)+":"+str(self.spheres[key]))
      for key, value in self.spheres.items():
         if value == 4:
            print("> \t"+str(key)+":"+str(self.spheres[key]))
      for key, value in self.spheres.items():
         if value == 3:
            print("> \t"+str(key)+":"+str(self.spheres[key]))
      for key, value in self.spheres.items():
         if value == 2:
            print("> \t"+str(key)+":"+str(self.spheres[key]))
      for key, value in self.spheres.items():
         if value == 1:
            print("> \t"+str(key)+":"+str(self.spheres[key]))
            



         #if(self.spheres[key]>0):
            #print(self.spheres[key])
            #print(str(self.spheres[key]))
            #print("\t"+str(key)+":"+str(self.spheres[key]))

      #print("> **XP:** "+str(self.xp-self.getSpentExp())+"**/"+str(self.xp)+"**")
      super(Mage,self).printExp()
      print("⎯"*66)


   def setSpheres(self, _dict):
      for key in _dict:
         value = _dict[key]
         self.spheres[key] = value

   def upgradeSphere(self, _sphereEnum):

      xpBefore = self.getSpentExp()

      if _sphereEnum in self.spheres:
         self.spheres[_sphereEnum] = self.spheres[_sphereEnum] + 1
         print("\t Spent " + str(self.getSpentExp()-xpBefore).rjust(2,' ')+"xp [Sphere]\t\t"+ str(_sphereEnum)+" \t("+ str(self.spheres[_sphereEnum]-1) +" => "+str(self.spheres[_sphereEnum])+")")
      else:
         self.spheres[_sphereEnum] = 1
         print("\t Spent " + str(self.getSpentExp()-xpBefore).rjust(2,' ')+"xp [Sphere]\t\t"+ str(_sphereEnum)+" \t(1)")



   def setEveil(self, value):
      self.eveil = value


   def getSpentExp(self):
      xp = 0

      # Attributs (x4):
      for key in self.attributs:
         for i in range(1,self.attributs[key]+1):
         #if self.attributs[key]>1: #first level is free
            if i>1:
               xp += i*4
               #print(xp)

      # Capacités (x3):
      for key in self.capacités:
         for i in range (1,self.capacités[key]+1):
            xp += i*3
            #print(xp)

      # Historiques (x3):
      for key in self.historique:
         for i in range(1,self.historique[key]+1):
            xp += i*3
            #print(xp)

      # Spheres (x8):
      for key in self.spheres:

         if self.spheres[key]==3:
            #Sphere Affinity
            for i in range(1,self.spheres[key]+1):
               xp += i*7
         else:
            for i in range(1,self.spheres[key]+1):
               xp += i*8

      #Eveil(Arété)
      for i in range(2,self.eveil+1): # the first point in Arete is free (we talk about mages...)
         xp += i*8

      return xp


#cop = Character("Cop01")
# cop.capacités["Conduite"] = 3
# cop.display()



# def populate():
#    pass



# # persoName = Mage("Prenom NOM", "Mage", "Tradition")
# # persoName.concept = ""

# # persoName.physique = ""
# # persoName.attitude = ""

# # persoName.paradigme = ""
# # persoName.foci = ""

# # persoName.setAttributes([1,2,4,2, 3,3,2,1])
# # persoName.setCapacities({"XX4XX":4})
# # persoName.setCapacities({"XX3XX":3,"XX3XX":3})
# # persoName.setCapacities({"XX2XX":2,"XX2XX":2,"XX2XX":2})
# # persoName.setCapacities({"XX1XX":1,"XX1XX":1,"XX1XX":1,"XX1XX":1})
# # persoName.setSpheres({Sphere.Esprits:3, Sphere.Entropie:2, Sphere.Espace:1})
# # persoName.setEveil(3)
# # persoName.setAtouts({"ATOUT":7})
# # persoName.setHandicaps({"HANDICAP":-7})
# # persoName.display()
# print("⎯"*20)

# print("="*40)
# # metFoe = Mage("MET")
# # metFoe.setAttributes([4,3,3,2, 2,2,1,1])
# # metFoe.setCapacities({ "A":4,"B":3,"C":3,"D":2,"E":2,"F":2,"G":1,"H":1,"I":1,"J":1})
# # metFoe.setSpheres({Sphere.Prime:3, Sphere.Psyché:2, Sphere.Entropie:1})
# # metFoe.setEveil(3)
# # metFoe.display()
# # print (metFoe.getSpentExp())
# #+ 80 pts d'XP !(399) C'est la seule fois où vous pourrez dépenser de l'historique sans justification de jeu (autre que votre BG)

# print("="*40)

# # KenHimiitsu = Mage("KenHimiitsu")
# # KenHimiitsu.setAttributes([4,2,3,2, 5,5,4,1])
# # KenHimiitsu.setCapacities({ "Technologie":5,"Médecine":4,"Science":4,"Recherche":4,"Commandement":4,"Bagarre":3,"Informatique":3,"Culture":2,"Intimidation":2,"Droit":1})
# # KenHimiitsu.setSpheres({Sphere.Vie:5, Sphere.Prime:4, Sphere.Matière:4, Sphere.Psyché:1})
# # KenHimiitsu.setEveil(5)
# # KenHimiitsu.display()
# # print (KenHimiitsu.getSpentExp())

# print("⎯"*20)

# theodora = Mage("Théodora El-Yueadu", "Mage", "Euthanatos")
# theodora.concept = "Gourou Fight Club"
# theodora.paradigme = "Femme ex de confusion musulmane qui en 'rencontrer' Lucifer. Il lui a fait comprendre que ce n'etait pas l'archange Gabriel mais lui qui avait guidé les musulmans."
# theodora.foci = "Séduction, ArtMartial, Rize de rue/SabotageUrbain, Méditation, DOmination sociale, Prière. Je suis l'étincelle du chaos, je montre l'exemple en démontrant les conséquences qui peuvent suivre les simples graines que je sème. Mon art martial me permet de mettre mon corps et mon moi-symbole comme exemple à suivre."
# theodora.physique = "..."
# theodora.attitude = "..."
# theodora.setAttributes([3,3,2,4, 2,1,1,2])
# theodora.setCapacities({"Manipulation":4})
# theodora.setCapacities({"Arts Martiaux":3,"Subterfuge":3})
# theodora.setCapacities({"Armes à feu":2,"Recherche":2,"Érudition":2})
# theodora.setCapacities({"Ésotérisme":1,"Informatique":1,"Intimidation":1,"Méditation":1})
# theodora.spécialité["Manipulation"] = "Politique"
# theodora.spécialité["Arts Martiaux"] = "Externes"
# theodora.setSpheres({Sphere.Entropie:3, Sphere.Psyché:2, Sphere.Prime:1})
# theodora.setEveil(3)
# theodora.xp = 500 #antago bonus
# theodora.display()

# print("⎯"*20)
# # print("First Level Up !")
# theodora.upgradeSphere(Sphere.Vie)
# theodora.upgradeAttribute(Attribut.Charisme)
# theodora.upgradeAttribute(Attribut.Volonté)
# theodora.upgradeAttribute(Attribut.Mémoire)
# theodora.upgradeAttribute(Attribut.Empathie)
# theodora.upgradeCapacity("Arts Martiaux")
# theodora.upgradeCapacity("Esotérisme")
# theodora.upgradeCapacity("Méditation")

# theodora.upgradeHistorique("Influence(Spirituel)")
# theodora.upgradeHistorique("Influence(Spirituel)")
# # theodora.upgradeHistorique("Influence(Spirituel)")

# theodora.upgradeHistorique("Influence(Politique)")
# theodora.upgradeHistorique("Influence(Politique)")
# theodora.upgradeHistorique("Influence(Politique)")
# # theodora.upgradeHistorique("Influence(Politique)")

# theodora.upgradeHistorique("Influence(Médias)")
# theodora.upgradeHistorique("Influence(Médias)")
# # theodora.upgradeHistorique("Influence(Médias)")

# theodora.upgradeHistorique("Ressources")
# theodora.upgradeHistorique("Ressources")
# theodora.upgradeHistorique("Ressources")
# theodora.upgradeHistorique("Ressources")
# theodora.upgradeHistorique("Ressources")

# theodora.upgradeHistorique("Secte")
# theodora.upgradeHistorique("Secte")
# theodora.upgradeHistorique("Secte")

# theodora.display()
# theodora.grantExp(3)
# theodora.display()
# print("⎯"*20)


# Zhen = Mage("Zhen", "Mage", "Akashite")
# Zhen.concept = "Artiste Martial de l'harmonie,Ange gardien"
# Zhen.paradigme = "Le matériel est une illusion. La volonté peut défaire ces illusions et les remodeler à sa convenance. Je peux transcender ces limites factices.L'univers est un tout.Je suis un membre d'un tout, d'une circulation d'énergie en harmonie"
# Zhen.foci = "Chants tibétains, Do, Tai-Chi, Bâton de combat, Prières, Médidation, Cuisine"
# Zhen.physique = "Zehn est un homme d'une trentaine d'années athlétique. Il s'habille dans un style urbain discret et porte une chevalière en argent à l'annulaire droit."
# Zhen.attitude = "C'est un mec fiable et ça se sent. Zehn est sociable même si il est parfois brut dans ces propos. Il ne supporte pas l'inégalité et n'hésitera pas à intervenir pour protéger les plus faibles"

# Zhen.setAttributes([4,3,2,1, 3,2,2,1])
# Zhen.setCapacities({ "Do":4,"Athlétisme":3,"Méditation":3,"Érudition":2,"Ésotérisme":2,"Cuisine":2,"Conduite":1,"Intimidation":1,"Vigilance":1,"Furtivité":1})
# Zhen.setSpheres({Sphere.Forces:3, Sphere.Matière:2, Sphere.Prime:1})
# Zhen.setEveil(3)
# Zhen.setAtouts({"Insensible à la douleur":5, "Force intérieure":2 })
# Zhen.setHandicaps({"Sauveur":-3, "Sensibilité à l'alcool":-2,"Problèmes familiaux":-1})
# Zhen.display()
# print("⎯"*20)

# #print("First Level Up !")
# Zhen.upgradeSphere(Sphere.Prime)
# Zhen.upgradeAttribute(Attribut.Charisme)
# Zhen.upgradeAttribute(Attribut.Empathie)
# Zhen.upgradeCapacity("Do")
# Zhen.upgradeHistorique("Influence(Réseaux Sociaux)")
# Zhen.upgradeHistorique("Culte")
# Zhen.upgradeHistorique("Node")
# Zhen.upgradeHistorique("Node")
# Zhen.upgradeHistorique("Node")
# Zhen.upgradeHistorique("Statut")
# Zhen.upgradeHistorique("Statut")

# Zhen.display()
# print("⎯"*20)

# Zhen.grantExp(6)
# Zhen.display()
# print("⎯"*20)



# print("⎯"*20)

# ccc = Mage("Christian Rosenkreutz", "Mage", "Ordre d'Hermes")
# ccc.concept = "Quintescence de sa faction, il incarne un hubrys froid et dur de l'élitisme. D'apparence aristocratique et poli à l'outrance, rigide et exhaustif, presque méprisant avec une pédagogie cassante, mais efficace, Christian est d'attitude un noble, mais de coeur un chercheur de vérité, curieux et ouvert d'esprit, avec une certaine poésie, mais dont la voracité intellectuelle est troublante."
# #ccc.paradigme = "Le monde est né du Logos, de l'or parfait, il s'est brisé, détioré, mélangé à la matière et à l'esprit. Oui, bien des choses sont arrivées depuis la Création Eternelle, mais Christian sait que les avatar sont les graines éveillés du Premier des Êtres. Par là, chaque mage peut exercer sa vérité en se basant sur sa croyance et sa connaissance. Il faut affûter son esprit par milles usage, entretenir un corps sain et nourrir son âme pour créer sa Vérité et devenir à son tour, ce que certaines nomment "Dieu." Ce n'est là qu'un concentré de surface des pensées de ce mage tragique et détaché des choses, sauf pour les menus plaisir de la vie."
# ccc.foci = "alchimie, géométrie sacrée, symboles, gestes, incantations, outils de rituels, numérologie, sang, vrais noms, démonologie, domination sociale"
# ccc.physique = "Des cheveux d'or, des yeux bleus affutés, un sourire de politesse aux lèvres, Christian incarne un autre temps. Son port altier le met toujours en valeur, que cela soit dans un tenue armani sur-mesure ou dans une chemise détendue. Pour autant, cette attitude parfaite, selon les canons de la belle société, pourrait en pertuber plus d'un en-dehors de son milieu."
# ccc.attitude = ""

# ccc.setAttributes([1,2,2,4, 2,3,3,1])
# ccc.setCapacities({ "Esotérisme":4,"Médecine":3,"Occultisme":3,"Langue":2,"Etiquette":2,"Erudtion":2,"Commandement":1,"Subterfuge":1,"Vigilance":1,"Technologie":1})
# ccc.setSpheres({Sphere.Prime:3, Sphere.Esprits:2, Sphere.Psyché:1})
# ccc.setEveil(3)
# ccc.setAtouts({"Affinité Céleste":3, "Chef Naturel":2, "Port Altier":1, "Calcul Mental":1 })
# ccc.setHandicaps({"Froid":-2,"Langue du barde":-1, "Marque du diable":-1, "Conspirateur":-1, "Diablotin":-1, "Apprenti":-1})

# ccc.display()
# print("⎯"*20)

# #ccc.upgradeAttribute(Attribut.Force)
# #ccc.upgradeAttribute(Attribut.Empathie)
# ccc.upgradeCapacity("Informatique")
# ccc.upgradeCapacity("Commandement")
# #ccc.upgradeCapacity("Informatique")

# ccc.upgradeHistorique("Prodige")
# ccc.upgradeHistorique("Prodige")
# ccc.upgradeHistorique("Prodige")
# ccc.upgradeHistorique("Prodige")
# ccc.upgradeHistorique("Prodige")

# ccc.upgradeHistorique("Ressources")
# ccc.upgradeHistorique("Ressources")
# ccc.upgradeHistorique("Ressources")

# ccc.upgradeHistorique("Statut")
# ccc.upgradeHistorique("Statut")
# #ccc.upgradeHistorique("Fausse identité")
# #ccc.upgradeHistorique("Statut")

# ccc.display()
# print("⎯"*20)
# ccc.grantExp(6)
# ccc.upgradeHistorique("Node")
# ccc.display()





# print("⎯"*20)

# suiko = Mage("Suiko KINKO", "Mage", "Verbena")
# suiko.concept = "Tatouese/Caligraphe fanatique"
# suiko.paradigme = "Les dieux existent et leurs energie se canalyse dans leur sang et modele le monde depuis la nuit des temps. En insulfant de l'intention et de la croyance dans le sang, il est possible de diriger cette energie pour modeler la realite. La force mentale se transmet dans le sang, c'est un peu le liquide de l'ame."
# suiko.foci = "SK pense etre descendante d'un dieu et son pouvoir est dans ses veines. Elle peut utiliser son sang pour ecrire et en y mettant croyance et intention elle peut changer la realite. Elle dilue son sang dans l'encre en faisant une ceremonie pour rendre ses capacites a durer limite, mais en l'utilisant dans un tatoo ou en utilisant sont sang directement, elle ancre cette energie dans le corp de l'objet ou la personne"
# suiko.physique = "Elle a la trentaine, percings un peu partout, on peut voire ses bras et orbites tatoue avec une encre, ainsi que son front. Son style est un melange de streetwear et de Kimono. Elle a un constant sourire qui semble plus inquietant que sympatique."
# suiko.attitude = "Elle sait qu'elle est superieur et tant qu'on lui montre le respect qu'elle merite elle sera sympatique surtout si c'est pour faire affaire. Pour les gens de sa famille, sont attitude est plus maternel et protectrice"
# suiko.setAttributes([1,4,3,2, 2,2,1,3])
# suiko.setCapacities({ "Commandement":4})
# suiko.setCapacities({"Subterfuge":3,"Médecine":3})
# suiko.setCapacities({"Exp.Rue":2,"Séduction":2,"Manipulation":2})
# suiko.setCapacities({"Art":1,"Langues":1,"Ésotérisme":1,"Méditation":1})
# suiko.setSpheres({Sphere.Vie:3, Sphere.Matière:2, Sphere.Psyché:1})
# suiko.setEveil(3)
# suiko.setAtouts({"Assurance":2, "Don artistique":1, "Prestige":2 })
# suiko.setHandicaps({"Délit de sale gueule":-2,"Marquant":-3})
# #suiko.display()
# print("⎯"*20)

# suiko.upgradeHistorique("Alliés(Mon Gang)")
# suiko.upgradeHistorique("Alliés(Mon Gang)")
# suiko.upgradeHistorique("Alliés(Mon Gang)")
# suiko.upgradeHistorique("Alliés(Mon Gang)")
# suiko.upgradeHistorique("Contacts(Gangs)")
# suiko.upgradeHistorique("Contacts(Gangs)")
# suiko.upgradeHistorique("Contacts(Gangs)")
# suiko.upgradeHistorique("Ressources")
# suiko.upgradeHistorique("Ressources")
# suiko.upgradeHistorique("Ressources")
# suiko.upgradeHistorique("Ressources")
# suiko.display()
# print("⎯"*20)






# print("⎯"*20)

# mamu = Mage("Kiōzan Mamu", "Mage", "Wu-Lung")
# mamu.concept = "Ex-sumo devenu yakuza faisant des combats clandestins"
# mamu.physique = "Il a gardé son physique massif de sumo mais s'est rasé le crâne depuis qu'il est arrivé aux USA. Il aime exhiber fièrement ses tatouages quand il en a l'occasion et ne retire jamais l'énorme chaîne en or qu'il porte autour du cou."
# mamu.attitude = "Il n'a peur de (presque) personne, son gabarit impressionnant aidant ; il est très fidèles aux personnes envers qui il a confiance ; généralement calme et assez stoïque, il est capable de partir dans des accès de colère et de violence qu'il a du mal à contrôler."

# mamu.paradigme = "Depuis qu'il a vu ce qu'il craint être l'Enfer, sa plus grande terreur est que ça puisse devenir la réalité. C'est pour ça que, malgré l'agréable sentiment de puissance que lui procure l'utilisation de sa magie, il s'efforce de s'en servir avec parcimonie, de peur de convoquer des forces qu'il ne maîtriserait pas"
# mamu.foci = "Par les extrémités de son corps (mains, tête, ou pieds), Mamu est capable d'augmenter la température jusqu'à enflammer ou faire bouillir les choses. Il considère sa grosse chaîne en or comme un régulateur de ce pouvoir, bien que ce soit un verrou psychologique qu'autre chose, Mamu est persuadé qu'il serait incapable de retirer sa magie s'il ne la portait pas. Il semble qu'il soit aussi capable d'influencer sur d'autres éléments ou encore sur la gravité, mais dans une bien moindre mesure."

# mamu.setAttributes([4,2,3,2, 1,1,2,3])
# mamu.setCapacities({ "Bagarre":4})
# mamu.setCapacities({"Arts Martiaux":3,"Vigiliance":3})
# mamu.setCapacities({"Exp.Rue":2,"Armes à feu":2,"Intimidation":2})
# mamu.setCapacities({"Instinct":1,"Etiquette":1,"Mêlée":1,"Survie":1})
# mamu.setSpheres({Sphere.Forces:3, Sphere.Espace:2, Sphere.Entropie:1})
# mamu.setEveil(3)
# mamu.setAtouts({"Taille gigantesque":4, "Estomac de fer":1, "Physique impressionnant":2 })
# mamu.setHandicaps({"Flash-back":-3,"SSPT":-2, "Colérique":-2})

# mamu.display()
# print("⎯"*20)


# mamu.upgradeAttribute(Attribut.Force)
# mamu.upgradeCapacity("Arts Martiaux")
# mamu.upgradeCapacity("Exp.Rue")
# mamu.upgradeCapacity("Intimidation")
# #mamu.upgradeCapacity("Intimidation")
# #mamu.upgradeCapacity("Artisanat (forge)")
# #mamu.upgradeCapacity("Étiquette")
# #mamu.upgradeCapacity("Méditation")

# mamu.upgradeHistorique("Contacts(Combats clandestins)")
# mamu.upgradeHistorique("Contacts(Combats clandestins)")

# mamu.upgradeHistorique("Influence[Economie](Industrie)")
# mamu.upgradeHistorique("Influence[Economie](Industrie)")
# mamu.upgradeHistorique("Influence[Economie](Industrie)")

# mamu.upgradeHistorique("Prodige")

# mamu.display()
# print("⎯"*20)

# #Force 5*4=20
# #Arts martiaux 4*3=12
# #Expérience de la rue 3*3=9
# #Intimidation 33+43=21
# #Artisanat (forge) 1*3=3
# #Étiquette 1*3=3
# #Méditation 1*3=3
# #Historiques 3*3=9
# #Contacts dans le milieu des combats clandestins =3
# #Influence dans l'industrie métallurgique =3 (parmi les "clients" sur qui il exerce une pression pour le clan, Mamu s'est particulièrement investi dans les fonderies, forges et autres activités liées au travail des métaux)
# #Prodige =3





# washi = Mage("Washi", "Mage", "Orphelin")
# washi.concept = "Jeune orpheline assassin par origami"
# washi.physique = "Japonaise de 1m60, plutôt athlétique au teint pâle. Ses cheveux bleu corbeaux sont long et vont jusqu’au genoux quand elle les détaches. Elle porte toujours des parures dans ses cheveux faites de fleurs en papiers.Des percings aux oreilles et un petit dans le nez.On voit sur des parties dénudés dès tatouages à l’encre rouge."
# washi.attitude = "taciturne, froide, calme"

# washi.paradigme = "Le monde est kamis. Je leur parle et les honore et ils me prêtent leur force pour accomplir mes desseins."
# washi.foci = "Par des prières et des pliages précis, je sais doter mes oeuvres de propriétés extraordinaires comme des fleurs qui endorment, une lame de papier tranchante."

# washi.setAttributes([1,3,3,2, 4,2,2,1])
# washi.setCapacities({ "Art(Origami)":4})
# washi.setCapacities({"Arts Martiaux":3,"Esotérisme":3})
# washi.setCapacities({"Exp.Rue":2,"Occultisme":2,"Vigiliance":2})
# washi.setCapacities({"Instinct":1,"Athlétisme":1,"Intimidation":1,"Survie":1})
# washi.setSpheres({Sphere.Vie:3, Sphere.Matière:2, Sphere.Espace:1})
# washi.setEveil(3)
# washi.setAtouts({"Neuf vies":6, "Concentration":1 })
# washi.setHandicaps({"Marquée":-5,"Froid":-2})

# washi.display()
# print("⎯"*20)

# washi.upgradeSphere(Sphere.Espace)
# washi.upgradeHistorique("Fausse identité")
# washi.upgradeHistorique("Fausse identité")
# washi.upgradeHistorique("Fausse identité")
# washi.upgradeHistorique("Rang")
# washi.upgradeHistorique("Rang")
# washi.upgradeHistorique("Familier")
# washi.upgradeHistorique("Familier")
# washi.upgradeHistorique("Familier")
# washi.display()








# print("⎯"*20)

# sybille = Mage("Sybille Andernikos", "Mage", "Euthanatos: Chakravanti")
# sybille.concept = "Prêtre du destin (Parque)"

# sybille.physique = " Bientôt la trentaine, Sibylle est une personne au physique androgyne qui pourrait sembler tout à fait invisible dans le monde l’entreprise. Son costume trois pièces implacablement repassé n’est perturbé que par la présence deux éléments : une broche en forme de caducée qu’elle semble toucher à chaque déplacement et le tintement des galets des galets qu’elle transporte dans les poches de son costume."
# sybille.attitude = "Sibylle est de prima bord un personnage plutôt froid et dont il se dégage une étrange attitude corporatiste de par son apparence physique, son regard inquisiteurs semblent ne pas vous voir mais regarder à travers-vous pour observer quelque chose d’imperceptible, ce qui peut pour un premier contact mettre les gens mal à l’aise. Cependant après quelques échanges tentés d’un léger accent grecque, cette façade laisse place à une personne polie à l’écoute des autres et prête à leur prêter main forte s’ils ne font pas preuve d’hubris mal placé."

# sybille.paradigme = "Ordre divin chaos terrestre/des dieux et des monstres. De Chaos vient la création et de ses entrailles jaillirent les premiers titans qui façonnèrent la terre avant de trahir leur père, perpétuant le chaos, puis leurs fils trahirent les titans, plongeant de nouveau le monde dans le chaos. Mais il est un ordre caché dans ce spectacle chaotique, l’ordre du destin, nul ne peut y échapper, ni homme, ni dieu. Tous se voient offert leur lot avant que les Moires ne frappent pour vous faire rejoindre le cycle. Le seul espoir des hommes est d’être exceptionnels, de dépasser leurs potentiels sans sombrer dans l’hubris, ils pourront alors accéder aux champs Élysées et quitter le grand cycle. Pour les esclaves de l’hubris, leur destin est d’être broyé par la roue du destin et d’être renvoyé en Hadès pour réintégrer le cycle une fois qu’ils seront purifiés. Il faut donc pousser l’humanité à se surpasser et ne pas se piéger elle-même dans la stagnation."
# sybille.foci = "Instruments: Bénédictions et malédictions, potions et décoctions, alignement céleste, nourriture et boissons, jeux, rites de groupes, herbes et plantes, offrandes et sacrifices, prières et invocations, symboles, baguettes et bâtons."
# sybille.foci += "Bénédiction et malédictions: Les Moires dictent le début et la fin de votre vie, mais le reste de votre vie est dicté par les bénédictions et les malédictions des dieux sur ta maison. Comprends les mots secrets et leur art pour manipuler les fils du destin avant qu’ils ne soient coupés."
# sybille.foci += "Potions et décoctions: Transformer une chose en une autre est un secret qui a été transmis des dieux aux hommes. Transformer le doux raison en une boisson enivrante capable de briser votre perceptions et vos inhibitions n’est qu’un exemple parmi tant d’autre. L’art d’Hécate est à manier avec précautions car les arts magiques peuvent être aussi être une source de mort."
# sybille.foci += "Alignement céleste: Le katasterismoi s’étend dans le ciel nocturne comme un héritage des dieux et de leurs accomplissements. Le passé, présent et futur est caché dans le ciel et l’ont peut en tirer du pouvoir."
# sybille.foci += "Nourriture et boisson: Les hommes et les dieux ont besoin de substance pour survivre. Donnes leur de la nourriture pour montrer ta dévotion, mange et partage la nourriture avec tes convives pour être unifiés sous l’œil des dieux. A moins de rendre hommage aux khthonios, laisse la nourriture et la boisson pour eux et eux seuls."
# sybille.foci += "Jeux: Les dieux ont donner vie et pouvoirs aux hommes. Les jeux nous permettent d’honorer ces dons en montrant notre force, notre détermination et notre intelligence attirent l’œil des dieux."
# sybille.foci += "Rites de groupes: Vénérer les dieux est une activité sociale où tous prennent part pour montrer aux dieux qu’ils ne sont pas oubliés. Ce sont nos liens qui montrent notre foi envers eux."
# sybille.foci += "Herbes et plantes: la flore a toujours eut une place particulière dans l’histoire humaine, comme source de vie, de merveille et de mort. De nombreuses plantes sont le produit des dieux par jalousie, colère ou par tragédie."
# sybille.foci += "Offrandes et sacrifices: Donnes aux dieux et les dieux t’entendrons, donnes leurs le produit de la terre et les animaux pour alimenter ton appel aux immortels."
# sybille.foci += "Prières et invocations: honore les dieux de tes mots et prières, chante leurs noms pour les atteindre en Hadès ou sur Olympes, mais pèses tes mots car les immortels sont capricieux."
# sybille.foci += "Symboles: Ils ont un sens pour les dieux et nous rappellent leurs présences et leurs pouvoirs dans le monde des hommes. La chouette symbole d’Athéna nous rappelle sa sagesse, la flamme de Prométhée nous rappel le pouvoir de la création. Nous utilisons ces symboles comme une inspiration de pouvoir."
# sybille.foci += "Baguettes et bâtons: les baguettes et bâtons ont de tout temps symbolisé la puissance du magicien, c’est la baguette de Circé qui a transformé les compagnons d’Ulysse en animaux, c’est le caducée d’Hermès qui focalise son pouvoir de guérison. Ces outils sont une part indéniable du pouvoir du mage."

# sybille.setAttributes([1,2,4,2, 3,3,2,1])
# sybille.setCapacities({"Occultisme":4})
# sybille.setCapacities({"Ésotérisme":3,"Investigation":3})
# sybille.setCapacities({"Recherche":2,"Instinct":2,"Armes à feu":2})
# sybille.setCapacities({"Droit":1,"Vigiliance":1,"Haut-Rituel":1,"Langues":1})
# sybille.setSpheres({Sphere.Esprits:3, Sphere.Entropie:2, Sphere.Espace:1})
# sybille.setEveil(3)
# sybille.setAtouts({"Messager respecté":3, "Concentration":1, "Medium":2 }) #Medium:2, Affinité céleste, Sagesse du juge, Mentor prestigieux, Messager respecté.
# sybille.setHandicaps({"Tics":-1,"Curiosité":-2,"Echos":-1, "Regression":-2})
# sybille.display()
# print("⎯"*20)

# sybille.upgradeCapacity("Etiquette")
# sybille.upgradeCapacity("Athlétisme")
# sybille.upgradeCapacity("Haut-Rituel")

# sybille.upgradeHistorique("Ressources")
# sybille.upgradeHistorique("Ressources")
# sybille.upgradeHistorique("Ressources")

# sybille.upgradeHistorique("Rang")
# #sybille.upgradeHistorique("Rang")

# sybille.upgradeHistorique("Influence(Politique)")#Juridique
# sybille.upgradeHistorique("Influence(Politique)")#Législatif

# sybille.upgradeHistorique("Culte") #Paganisme, grec. Action culturelle, mais avec vénération religieuse. Tissu social.
# sybille.upgradeHistorique("Culte")

# sybille.upgradeHistorique("Node")
# sybille.upgradeHistorique("Node")

# sybille.upgradeHistorique("Allié")
# sybille.upgradeHistorique("Allié")
# sybille.upgradeHistorique("Allié")

# sybille.upgradeHistorique("Mentor")

# sybille.display()
# print("⎯"*20)





# salome = Mage("Salomé Morin", "Mage", "Culte de l'extase")
# salome.concept = "Reine de la nuit et derviche de l'extase"

# salome.physique = "Femme approchant de la trentaine au physique athlétique, Salomé est une personne à l'allure envoutante mise en valeur par un corps couvert de tatouages formant de complexes motifs géométriques semblant se mouvoir au rythme de ses gestes."
# salome.attitude = "A première vue Salomé peut sembler désinvolte, provocatrice. Et elle l’est sans le moindre doute face à la banalité du quotidien. Amicale, séductrice et chaleureuse, elle ne porte aucun jugement sur les individus, veillant elle-même à mener une vie débridée comme bon lui semble. Mais derrière ce masque de surface se dissimule une rigueur et une intransigeance à son égard et à l'égard de ceux qu’elle estime. Les apparats n’ont aucune importance de la même manière que les paroles, seuls les actes semblent avoir de la valeur à ses yeux pour ceux qui apprennent."
# salome.paradigme = "En tant qu’extatique, Salomé s’inscrit ne serait-ce qu’en partie dans le paradigme de son culte. Mais en opposition avec la tradition du culte, elle trouve l’extase avant tout à travers la sexualité, la souffrance, la saturation des sens et l’épuisement physique. Elle obtient la  véritable jouissance à travers ces état, par cette jouissance atteint ce qu’elle considère comme une véritable extase et, par cette extase manifeste pleinement son égo. Et par son égo elle permet à sa réalité de s’imposer à celle du monde."
# salome.foci = "Les foci principaux de Salomé sont les pratiques sexuelles extrêmes (sadomasochisme, bondage, shibari), la consommation de drogues couplée à l’écoute de musique (à des volumes assourdissant), la fête débridée sans aucune retenue, la danse jusqu’à épuisement mais aussi la méditation et la pratique du yoga. Les pratiques traditionnelles du culte de l’extase sont quant à elles secondaires et ne servent qu’aux actes de magye mineures ou utilitaires"

# salome.setAttributes([1,3,2,3, 4,1,2,2])
# salome.setCapacities({"performer extreme (sexe)":4})
# salome.setCapacities({"Art":3,"Athlétisme":3})
# salome.setCapacities({"Séduction":2,"Méditation":2,"Ésotérisme":2})
# salome.setCapacities({"Exp.Rue":1,"Instinct":1,"Vigilance":1,"Édudition":1})
# salome.setSpheres({Sphere.Temps:3, Sphere.Vie:2, Sphere.Psyché:1})
# salome.setEveil(3)
# salome.setAtouts({"Souplesse du serpent":1, "Tolérance à l'alcool/drogues":2, "Traits enchanteurs":2, "Initié d'une sous-culture":2})
# salome.setHandicaps({"Apprenti":-1, "Ennemi":-1, "Curiosité":-2, "Pratiques sexuelles extrêmes":-3})
# salome.display()
# print("⎯"*20)
# salome.upgradeAttribute(Attribut.Force)
# salome.upgradeAttribute(Attribut.Logique)

# salome.upgradeCapacity("Langues")
# salome.upgradeCapacity("Occultisme")

# salome.upgradeSphere(Sphere.Prime)

# salome.upgradeHistorique("Renommée")
# salome.upgradeHistorique("Node")
# salome.upgradeHistorique("Culte")
# salome.upgradeHistorique("Culte")
# salome.upgradeHistorique("Ressources")
# salome.upgradeHistorique("Ressources")
# salome.upgradeHistorique("Ressources")
# salome.upgradeHistorique("Rang")
# salome.upgradeHistorique("Rang")
# salome.upgradeHistorique("Rang")


# salome.display()
# print("⎯"*20)







# john = Mage("John", "Mage", "Culte de l'extase")
# john.concept = "Meta Psyché Evangeliste"

# john.physique = "Femme approchant de la trentaine au physique athlétique, Salomé est une personne à l'allure envoutante mise en valeur par un corps couvert de tatouages formant de complexes motifs géométriques semblant se mouvoir au rythme de ses gestes."
# john.attitude = "A première vue Salomé peut sembler désinvolte, provocatrice. Et elle l’est sans le moindre doute face à la banalité du quotidien. Amicale, séductrice et chaleureuse, elle ne porte aucun jugement sur les individus, veillant elle-même à mener une vie débridée comme bon lui semble. Mais derrière ce masque de surface se dissimule une rigueur et une intransigeance à son égard et à l'égard de ceux qu’elle estime. Les apparats n’ont aucune importance de la même manière que les paroles, seuls les actes semblent avoir de la valeur à ses yeux pour ceux qui apprennent."

# john.paradigme = "En tant qu’extatique, Salomé s’inscrit ne serait-ce qu’en partie dans le paradigme de son culte. Mais en opposition avec la tradition du culte, elle trouve l’extase avant tout à travers la sexualité, la souffrance, la saturation des sens et l’épuisement physique. Elle obtient la  véritable jouissance à travers ces état, par cette jouissance atteint ce qu’elle considère comme une véritable extase et, par cette extase manifeste pleinement son égo. Et par son égo elle permet à sa réalité de s’imposer à celle du monde."
# john.foci = "Les foci principaux de Salomé sont les pratiques sexuelles extrêmes (sadomasochisme, bondage, shibari), la consommation de drogues couplée à l’écoute de musique (à des volumes assourdissant), la fête débridée sans aucune retenue, la danse jusqu’à épuisement mais aussi la méditation et la pratique du yoga. Les pratiques traditionnelles du culte de l’extase sont quant à elles secondaires et ne servent qu’aux actes de magye mineures ou utilitaires"

# john.setAttributes([1,2,2,3, 3,1,2,4])
# john.setCapacities({"Expression":4})
# john.setCapacities({"Manipulation":3,"Séduction":3})
# john.setCapacities({"Art()":2,"Etiquette":2,"Langues":2})
# john.setCapacities({"Esotérisme":1,"Occultisme":1,"Technologie":1,"Commandement":1})
# john.setSpheres({Sphere.Psyché:3, Sphere.Espace:2, Sphere.Prime:1})
# john.setEveil(3)
# #john.setAtouts({"Souplesse du serpent":1, "Tolérance à l'alcool/drogues":2, "Traits enchanteurs":2, "Initié d'une sous-culture":2})
# #john.setHandicaps({"Apprenti":-1, "Ennemi":-1, "Curiosité":-2, "Pratiques sexuelles extrêmes":-3})
# john.display()

# print("⎯"*20)
# # salome.upgradeAttribute(Attribut.Force)
# # salome.upgradeAttribute(Attribut.Logique)

# # salome.upgradeCapacity("Langues")
# # salome.upgradeCapacity("Occultisme")

# # salome.upgradeSphere(Sphere.Prime)

# # salome.upgradeHistorique("Renommée")
# # salome.upgradeHistorique("Node")
# # salome.upgradeHistorique("Culte")
# # salome.upgradeHistorique("Culte")
# # salome.upgradeHistorique("Ressources")
# # salome.upgradeHistorique("Ressources")
# # salome.upgradeHistorique("Ressources")
# # salome.upgradeHistorique("Rang")
# # salome.upgradeHistorique("Rang")
# # salome.upgradeHistorique("Rang")


# # salome.display()
# # print("⎯"*20)


