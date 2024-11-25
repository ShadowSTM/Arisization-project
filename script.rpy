# Déclarez les personnages principaux utilisés dans le jeu.

define P = Character('[prénom] [nom]', color="#ffffff")   
define A = Character('AK-24', color="#00eeff")

# versions de AK-24 

define Na = Character('[newname] [nom]', color="#00eeff")
define Wa = Character('[newname] [nom]', color="#ff2323")

# Les élèves de Seconde-E. 

define M = Character('Mme Kusanagi', color="#ffffff")
define I = Character('Iris Natsumi', color="#b340ff")
define H = Character('Hajime Ayanokoji', color="#ffffff")
define K = Character('Kendo Sato', color="#ffffff")
define N = Character('Naoto Saotome', color="#ffee00")
define Hi = Character('Haruki Ichinose', color="#ffffff")
define Y = Character('Yuki Hiiragi', color="#0059ff")

# Les élèves du bureau des élèves.
 
define E = Character('Emily Katsuragi', color="#ffffff")
define Kh = Character('Kazumi Hanemiya', color="#ffffff") 

# Les antagonistes principaux.

define J1 = Character('Ayano Enoshima', color="#ff2323")
define J2 = Character('Aiko Enoshima', color="#ff2323") 
define J = Character('Les ultimes jumelles', color="#ff2323")

# Les élèves du département. 

define Ah = Character('Akeno Hoshino', color="#cc23ff")

# fonctions pour les personnages inconnus

define S = Character('Subaru', color="#ffffffff")
define R = Character('??????', color="#a9a9a9")
define T = Character('Professeur', color="#ffffff")

# la mére du personnnage principale 

define Mo = Character('Marie [nom]', color="#ff00ea")

# Le jeu commence ici 

label start: 

# paramétres des écrans

    screen lunchroom():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "Cafétéria":
                size 50
                xalign 0.5 

    screen class_404():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "Classe 404":
                size 50
                xalign 0.5 

    screen room():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "Chambre":
                size 50
                xalign 0.5 

    screen hallway():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "Couloir":
                size 50
                xalign 0.5 

    screen hall():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "Hall":
                size 50
                xalign 0.5 

    screen office():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "Bureau des élèves":
                size 50
                xalign 0.5 

    screen clubroom():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "Salle de club":
                size 50
                xalign 0.5 

    screen Dev():
        frame:
            xalign 0.5
            ypos 10 
            has vbox  

            text "Developper mode":
                size 20
                xalign 0.5 

    screen logo():
        frame:
            yalign 0.5
            xalign 0.5  
            add "Images/logo.JPG" at unrotate

    screen points():
        frame:
            xalign 0
            ypos 10 
            has vbox  

            text "[pts] points":
                size 20
                xalign 0.5 

    screen perm():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "salle de permanence":
                size 50
                xalign 0.5 

    screen WC():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "Toilettes":
                size 50
                xalign 0.5 

    $ grd = 0.0 #notes
    $ pts = 0 #Points Nexus 

    stop music fadeout 2.0

# choix de prénom et nom de lycéen  

label key:

    play sound "Menu.mp3" noloop
    $ key = renpy.input("Veuillez écrire votre clé d'accès.")
    $ key = key.strip()

    if key == "ARIS-8J4K-F9Q7-2XZB-IJ3G-R83F-1IE9-D9BU-WHFB-OU8I":

        "Jeu déverrouillé."
        play sound "Menu.mp3" noloop 

    else:

        "Erreur système. Veuillez réessayer."
        $ renpy.restart_interaction() 
        play sound "Menu.mp3" noloop
        jump key 

    show screen logo()
    
    transform unrotate:
        zoom 0.5
        rotate 360 
        linear 2.0 rotate 0
 
    "{b}{i}Bienvenu dans Arisization Project cher/chére lycéen.{/i}{/b}"   
    play sound "Click.mp3" noloop

    hide screen logo

label auto_save:
    
    $ renpy.save("auto-1")

# choix de prénom et nom de lycéen  

label identity:

    play sound "Menu.mp3" noloop
    $ prénom = renpy.input("Quel est votre prénom de lycéen ?")
    $ prénom = prénom.strip()   

    play sound "Menu.mp3" noloop
    $ nom = renpy.input("Quel est votre nom de lycéen ?")
    $ nom = nom.strip()   

    play sound "Menu.mp3" noloop
    $ pronom = renpy.input("Quel est votre genre ? ( il ou elle )")
    $ pronom = pronom.strip()   

label pronom: 

    if pronom == "il" or "elle":

        "Le pronom a été enregistré dans le système." 
        play sound "Menu.mp3" noloop

    else:

        "Erreur système. Veuillez réessayer."
        $ renpy.restart_interaction() 
        play sound "Menu.mp3" noloop
        jump pronom 

label Dev:

    if prénom == "Dev" and nom == "Kageno": 

        show screen Dev 
        play sound "Menu.mp3" noloop
        $ newname = renpy.input("Veuillez écrire le nouveau prénom de AK-24.")
        $ newname = newname.strip()

        if newname == "Aris":

            "Le prénom a été enregistré dans le système." 
            play music "Soundtrack.mp3" loop volume 1.0
            jump test

        else:

            "Erreur système. Veuillez réessayer."
            $ renpy.restart_interaction() 
            play sound "Menu.mp3" noloop
            jump Dev

    if prénom in ["Iris", "Hajime", "Kendo", "Naoto", "Haruki", "Yuki", "Emily", "Kazumi", "Ayano", "Aiko", "Akeno", "Subaru"]:
        "Ce prénom n'est pas autorisé."
        jump identity

    elif nom in ["Kusanagi", "Natsumi", "Ayanokoji", "Sato", "Saotome", "Hiiragi", "Katsuragi", "Hanemiya", "Enoshima", "Hoshino"]:
        "Ce nom n'est pas autorisé."
        jump identity 

label début:

    scene black 

    "{b}{i}Quelque part dans un laboratoire abandonné.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene lab 

    P "Bon on fait quoi ?"
    play sound "Click.mp3" noloop    

    S "On pourrait fouiller les lieux déjà."
    play sound "Click.mp3" noloop

    P "Tu pense sérieusement qu'on va trouver quelque chose d'intéressant ici ?"
    play sound "Click.mp3" noloop    

    S "Oui surement."
    play sound "Click.mp3" noloop

    P "Bon ok alors."
    play sound "Click.mp3" noloop

    "{b}{i}Tu commences a regarder un peu dans le laboratoire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Tu trouves quelque chose ?"
    play sound "Click.mp3" noloop

    S "Non rien malheureusement."
    play sound "Click.mp3" noloop 
 
    "{b}{i}Tu continues de chercher quelque chose d'intéressant mais [S] tombes sur un énorme objet.{/i}{/b}"
    play music "Stumble.mp3" noloop 

    S "C'est quoi ce truc qui traine encore ?"
    play sound "Click.mp3" noloop

    P "Fait voir ce que c'est."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu t'approches et tu vois un robot humanoide.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "On dirait un robot humanoide comme ceux qui ont été utilisé pour la guerre de l'année derniére."
    play sound "Click.mp3" noloop 

    S "Un robot humanoide !? Tu n'est pas sérieux j'espére."
    play sound "Click.mp3" noloop

    P "Si je le suis."
    play sound "Click.mp3" noloop

    S "Ok mais on va faire quoi de ça maintenant ?"
    play sound "Click.mp3" noloop

    P "Je vais essayer de la démarrer."
    play sound "Click.mp3" noloop

    S "Pardon !?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu t'approches et tu démarres le robot.{/i}{/b}"
    play sound "Click.mp3" noloop 

    S "Mec je ne suis pas sur que soit une bonne idée..."
    play sound "Click.mp3" noloop 

    R "Initialisation..."
    play sound "Click.mp3" noloop 
 
    P "Attend on dirait qu'elle est en train de démarrer."
    play sound "Click.mp3" noloop
    
    A "Initialisation terminée. Date du 6 juillet 2097, Bonjour je suis [A]."
    play sound "Click.mp3" noloop 

    P "Tu vois je t'avais dit de ne pas t'inquiéter."
    play sound "Click.mp3" noloop

    S "Ok mais c'est juste que je suis pas à l'aise à coté d'elle."
    play sound "Click.mp3" noloop 

    P "Oh c'est bon c'est juste un robot humanoide."
    play sound "Click.mp3" noloop

    S "Bon on quitte cet endroit ?"
    play sound "Click.mp3" noloop

    P "Oui vu qu'on a fini de voir ici."
    play sound "Click.mp3" noloop 

    S "Par contre tu laisse ce robot ici."
    play sound "Click.mp3" noloop

    P "Je refuse de laisser ici alors qu'elle est en bonne état de fonctionner."
    play sound "Click.mp3" noloop 

    S "Pourrais-je savoir pourquoi !?"
    play sound "Click.mp3" noloop

    P "Car je pense qu'elle a du potentielle pour m'aider"
    play sound "Click.mp3" noloop 

    S "Ce robot ne t'appartiens pas."
    play sound "Click.mp3" noloop

    P "Mais elle est abandonnée et en plus je suis bon en informatique."
    play sound "Click.mp3" noloop

    S "Bon je me tire d'ici."
    play sound "Click.mp3" noloop 

    P "Moi aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Tu quittes le labo avec [A] en coupant les ponts avec [S].{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black  

    play music "Soundtrack.mp3" loop volume 1.0
    "{b}{i}Un an plus tard dans la région du Danto, le 12 septembre 2098 le jeune prodige intégra un lycée d'informatique et de technologie.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    scene school

    P "Enfin arriver au lycée....."
    play sound "Click.mp3" noloop 

    A "Oui je suis contente pour toi que tu sois arriver ici."
    play sound "Click.mp3" noloop 

    P "Bon on entre à l'intérieur."
    play sound "Click.mp3" noloop 

    scene black 

    "{b}{i}Vous entrez dans le lycée avec [A].{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene hall
    show screen hall  

    P "Bon enfin à l'intérieur."
    play sound "Click.mp3" noloop 

    A "Oui ça fait du bien."
    play sound "Click.mp3" noloop 

    P "Bon ou pourrait-on aller pour commencer ? Car je ne connais pas du tout le lycée." 
    play sound "Click.mp3" noloop 

    A "Attend tu t'es inscrit dans un lycée et tu t'es pas renseigné un peu plus ?"
    play sound "Click.mp3" noloop

    P "Euh j'étais occupé....."
    play sound "Click.mp3" noloop

    A "Bon après ça ne m'étonne pas venant de toi [P]"
    play sound "Click.mp3" noloop
    
    P "Hein !? Pardon !? Comment oses-tu je suis ton \"créateur\" je te rappelle !" 
    play sound "Click.mp3" noloop

    A "Mais pour revenir à ta question, on pourrait monter au premier étage car il semblerait qu'il aie rien d'intéressant ici."
    play sound "Click.mp3" noloop

    P "Ok alors."
    play sound "Click.mp3" noloop

    scene black 
    hide screen hall
    
    "{b}{i}Vous vous dirigez alors au premier étage.{/i}{/b}" 
    play sound "Click.mp3" noloop

    scene hallway
    show screen hallway 

    A "Ah ouais ce couloir est vraiment énorme"
    play sound "Click.mp3" noloop

    P "Je confirme." 
    play sound "Click.mp3" noloop
     
    A "On dirait qu'il y a des dortoirs et plusieurs salles de classe"
    play sound "Click.mp3" noloop

    P "ouais on pourrait aller voir"
    play sound "Click.mp3" noloop

    A "oui mais on doit aller en classe."
    play sound "Click.mp3" noloop

    P "Ok alors allons-y."
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous dirigez alors la salle de classe mais quelqu'un s'approche...{/i}{/b}"
    play sound "Click.mp3" noloop

    R "Bonjour je suis venue vous voir car je suis la lycéenne qui doit se charger des nouveaux lycéens dont vous."
    play sound "Click.mp3" noloop

    P "Ok alors merci de nous guider mais comment tu t'appelles ?"
    play sound "Click.mp3" noloop 

label rencontre: 

    E "Je m'appelle Emily Katsuragi, actuelle présidente du bureau des élèves."
    play sound "Click.mp3" noloop

    P "Enchanté."
    play sound "Click.mp3" noloop 

    E "Je suis enchantée mais pourrait savoir comment tu t'appelles ?"
    play sound "Click.mp3" noloop 

    P "Je m'appelle [P]."
    play sound "Click.mp3" noloop 

    E "Bienvenue [P]."
    play sound "Click.mp3" noloop 

    P "Merci beaucoup Emily."
    play sound "Click.mp3" noloop 

    E "Mais de rien ça fais plaisir mais j'ai une question."
    play sound "Click.mp3" noloop 

    P "Oui dit moi, je t'écoute."
    play sound "Click.mp3" noloop 

    E "Qui est cette magnifique \"fille\" qui est tout le temps avec toi ?"
    play sound "Click.mp3" noloop 

    A "\"Magnifique\" !? je suis vraiment flattée merci beaucoup."
    play sound "Click.mp3" noloop 

    E "De rien mais pour revenir à ma question [prénom], qui est cette fille ?"
    play sound "Click.mp3" noloop

    P "Ah elle, c'est [A] mon projet de \"robot humanoïde\"."
    play sound "Click.mp3" noloop 

    E "Un robot humanoïde !? tu es sérieux ?" 
    play sound "Click.mp3" noloop 

    P "Oui je suis sérieux."
    play sound "Click.mp3" noloop 

    E "Vraiment !?"
    play sound "Click.mp3" noloop 

    P "Oui regarde Emily, Vas-y [A] présentes-toi à elle."
    play sound "Click.mp3" noloop 

    A "Bonjour je suis [A], l'assistante et la création de [P], je suis un robot humanoïde."
    play sound "Click.mp3" noloop

    E "Bonjour alors [A] ravie de te rencontrer."
    play sound "Click.mp3" noloop

    A "Merci beaucoup Emily."
    play sound "Click.mp3" noloop

    E "De rien mais bon maintenant je vais vous expliquer comment fonctionne ce lycée."
    play sound "Click.mp3" noloop 

    P "Ok merci de nous expliquer."
    play sound "Click.mp3" noloop 

    E "Pour commencer les cours ici sont un peu particulier."
    play sound "Click.mp3" noloop

    P "Comment ça ? expliquez moi plus en détail."
    play sound "Click.mp3" noloop

    E "Déja tous les lycéens qui sont ici ont un projet informatique ou technologique."
    play sound "Click.mp3" noloop 

    P "Ok intéressant"
    play sound "Click.mp3" noloop

    E "Donc tout les lycéens passent beaucoup de temps en club."
    play sound "Click.mp3" noloop 

    P "vraiment au tant que ça ?"
    play sound "Click.mp3" noloop

    E "Oui vraiment genre le jeudi ou le vendredi est consacré aux activitées de club."
    play sound "Click.mp3" noloop 

    P "Merci c'est intéressant à savoir."
    play sound "Click.mp3" noloop 
     
    E "Le reste du temps vous avez cours."
    play sound "Click.mp3" noloop

    P "J'imagine bien que le reste du temps j'ai cours."
    play sound "Click.mp3" noloop

    E "Maintenant je vais vous expliquer comment fonctionne les clubs."
    play sound "Click.mp3" noloop

    P "Moi et [A] sommes complétement à votre écoute."
    play sound "Click.mp3" noloop
    
    E "Pour les clubs chaque élève peuvent soit rejoindre le club général du lycée ou créer son propre club."
    play sound "Click.mp3" noloop 

    P "Créer son propre club vraiment !?"
    play sound "Click.mp3" noloop 

    E "Oui et je pense que c'est la meilleure solution pour toi et [A]."
    play sound "Click.mp3" noloop

    P "Ah bon vraiment et pourquoi ?"
    play sound "Click.mp3" noloop 

    E "Oui car j'ai remarqué que [A] est souvent stressée quand elle est en face de quelqu'un qu'elle connait pas."
    play sound "Click.mp3" noloop 

    A "Oui je suis souvent stressée quand je suis en face de quelqu'un que je ne connais pas."
    play sound "Click.mp3" noloop

    E "ça va allez ton créateur est là pour toi n'est ce pas [P] ?" 
    play sound "Click.mp3" noloop

    P "Oui je confirme je serais toujours là pour elle."
    play sound "Click.mp3" noloop

    A "Merci beaucoup de me rassurer."
    play sound "Click.mp3" noloop

    E "De rien maintenant je vais vous expliquer comment fonctionnent les cours."
    play sound "Click.mp3" noloop 

    P "Comment ça il y a une particularité avec les cours ?"
    play sound "Click.mp3" noloop

    E "Oui par exemple il y a pas beaucoup d'examens durant l'année."
    play sound "Click.mp3" noloop 

    P "Heureusement se sera moins stressant pour moi et [A]."
    play sound "Click.mp3" noloop 

    E "Et il y a que trois jours de cours par semaine."
    play sound "Click.mp3" noloop 

    P "Merci pour ces informations."
    play sound "Click.mp3" noloop

    E "Ah et aussi tiens tes informations concernant ta classe et tes horaires." 
    play sound "Click.mp3" noloop

    P "Merci beaucoup Emily."
    play sound "Click.mp3" noloop 

    E "De rien c'est normal."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes tes documents et tu remarques que tues en Seconde-E.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Seconde-E c'est donc ça ma classe."
    play sound "Click.mp3" noloop

    E "Oui et aussi avant que tu partes j'ai un dernier truc a régler avec toi."
    play sound "Click.mp3" noloop

    P "Oui dit moi."
    play sound "Click.mp3" noloop

    E "Normalement les lycéens ne n'ont pas besoin car ils ont des projets simples."
    play sound "Click.mp3" noloop 

    P "Comment ça je ne comprend pas."
    play sound "Click.mp3" noloop 

    E "Normalement ils n'ont pas de besoin de contrat ou de dérogation mais toi si vue la taille de ton projet."
    play sound "Click.mp3" noloop

    P "Quoi !? Commment ça !?"
    play sound "Click.mp3" noloop

    A "Quoi !? Comment ça une dérogation pour que [P] puisse bosser sur mon amélioration ?"
    play sound "Click.mp3" noloop

    E "Oui et il faudra l'accepter pour continuer ton projet."
    play sound "Click.mp3" noloop 

    "{b}{i}Après un moment de reflection tu realises et acceptes le contrat.{/i}{/b}"
    play sound "Menu.mp3" noloop

    menu :    

        "{b}{i} Accepter le contrat.{/i}{/b}" : 
            play sound "Menu.mp3" noloop 
    
    P "Ok je l'accepte."
    play sound "Click.mp3" noloop 

    E "Bien voici le contrat UCN000001 pour l'utilsation compléte de [A] au sein du lycée Nexus." 
    play sound "Click.mp3" noloop

    P "Merci mais j'aimerais savoir j'ai besoin d'un contrat pour utiliser ma propre invention dans le lycée."
    play sound "Click.mp3" noloop 

    E "Car [A] peut devenir \"dangereuse\" si tu la géres mal."
    play sound "Click.mp3" noloop

    A "Moi devenir dangereuse !?"
    play sound "Click.mp3" noloop 

    E "Oui si tes paramétres sont mal fait par [P]."
    play sound "Click.mp3" noloop

    P "Ok je comprend mieux pourquoi..."
    play sound "Click.mp3" noloop

    E "Bon maintenant partez en cours avant d'arriver en retard."
    play sound "Click.mp3" noloop

    P "Ok j'y vais toute de suite, allez [A] tu viens."
    play sound "Click.mp3" noloop

    A "Oui je te suis [P]."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous dirigez alors vers la salle de classe 404.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway
    scene black

    "{b}{i}Vous entrez alors en classe mais dès que tu rentres dans la classe tout le monde se tournent vers toi...{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene classroom
    
    show screen class_404 
    R "Qui c'est encore celui là ?"
    play sound "Click.mp3" noloop

    R "Je ne sais pas mais regarde la magnifique fille avec lui."
    play sound "Click.mp3" noloop 

    R "C'est vrai c'est une fille qui est avec lui."
    play sound "Click.mp3" noloop 

    R "Je pense que je vais aller voir."
    play sound "Click.mp3" noloop

    R "Mec je ne suis pas sur que ce sois une bonne idée."
    play sound "Click.mp3" noloop

    R "Mais si je vais juste demander qui c'est et puis c'est tout."
    play sound "Click.mp3" noloop

    "{b}{i}L'élève en question se dirige vers vous.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    A "[P] c'est qui cet élève ?"
    play sound "Click.mp3" noloop

    P "Je ne sais pas du tout."
    play sound "Click.mp3" noloop

    "{b}{i}L'élève s'approche un peu trop de [A]...{/i}{/b}"
    play sound "Click.mp3" noloop

    A "Mais qu'est-ce que tu fais !?" 
    play sound "Click.mp3" noloop

    "{b}{i}Tu prends l'élève par le bras.{/i}{/b}"
    play sound "Click.mp3" noloop

    R "Hey je peux savoir pour qui tu te prends !?"
    play sound "Click.mp3" noloop 

    P "Juste évite de la toucher car elle est sensible." 
    play sound "Click.mp3" noloop 
      
    R "Désolé j'étais juste curieux."
    play sound "Click.mp3" noloop 

    P "Oui c'est ça maintenant dégage !"
    play sound "Click.mp3" noloop

    "{b}{i}L'élève s'éloigne de vous par culpabilité.{/i}{/b}"
    play sound "Click.mp3" noloop 

    A "Merci beaucoup [P]."
    play sound "Click.mp3" noloop 

    P "Mais de rien ma chère [A]."
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde discutent tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    A "[P] on dirait qu'on est que 10 élèves ici."
    play sound "Click.mp3" noloop

    P "Je confirme et je me demande pourquoi."
    play sound "Click.mp3" noloop

    A "Je ne sais pas mais peut étre qu'on le saura après."
    play sound "Click.mp3" noloop

    play sound "Door.mp3" noloop
    "{b}{i}Soudainement la porte s'ouvrit et une jeune femme apparait.{/i}{/b}"
    play sound "Click.mp3" noloop 

    T "Bonjour je suis votre professeur principale cette année."
    play sound "Click.mp3" noloop

    R "Bonjour Madame."
    play sound "Click.mp3" noloop

    P "Bonjour."
    play sound "Click.mp3" noloop

    A "Bonjour.~"
    play sound "Click.mp3" noloop 

    T "Bien vous pouvez vous asseoir maintenant on va commencer par les présentations pour mieux se connaitre."
    play sound "Click.mp3" noloop

    "{b}{i}La professeur pose rapidement un regard sur [A] avant de retourner son regard sur la classe.{/i}{/b}" 
    play sound "Click.mp3" noloop

# début des présentations des élèves

    T "Bon qui veut se présenter en premier ?"
    play sound "Click.mp3" noloop
 
    R "Moi s'il vous plait."
    play sound "Click.mp3" noloop

    T "Bien vas-y présentes-toi."
    play sound "Click.mp3" noloop

    I "Je m'appelle Iris Natsumi, j'ai 19 ans et je suis aussi \"l'ultime Développeuse\"."
    play sound "Click.mp3" noloop 
    
    T "L'ultime développeuse !? oh intéressant."
    play sound "Click.mp3" noloop

    I "Merci beaucoup."
    play sound "Click.mp3" noloop  

    T "Donc enchanté Iris, quel est ton projet dans ce lycée ?"
    play sound "Click.mp3" noloop 

    I "Finir mon projet de jeu vidéo mais je veux surtout sociabiliser avec les autres."
    play sound "Click.mp3" noloop 

    T "Sociabiliser avec les autres comment ça ?"
    play sound "Click.mp3" noloop

    I "Depuis que j'ai commencé à travailler sur mon jeu vidéo je me suis beaucoup renfermé dans ma propre bulle et j'aimerais changer ça."
    play sound "Click.mp3" noloop 

    T "Intéressant c'est bien que tu veuilles changer."
    play sound "Click.mp3" noloop

    I "Merci beaucoup."
    play sound "Click.mp3" noloop 
    
    T "De rien maintenant toi juste dérrière Iris."
    play sound "Click.mp3" noloop 

    R "Euh moi...."
    play sound "Click.mp3" noloop

    T "Oui toi qui d'autre."
    play sound "Click.mp3" noloop

    H "Bonjour je m'appelle [H], j'ai 19 ans."
    play sound "Click.mp3" noloop

    T "Enchanté [H] bienvenue dans notre classe, j'aimerais savoir quel ton projet dans ce lycée."
    play sound "Click.mp3" noloop

    H "Mon projet est de construire un robot." 
    play sound "Click.mp3" noloop 

    T "Intéressant comme projet."
    play sound "Click.mp3" noloop

    H "Merci beaucoup."
    play sound "Click.mp3" noloop

    T "De rien maintenant suivant s'il vous plait."
    play sound "Click.mp3" noloop 

    R "Nous s'il vous plait."
    play sound "Click.mp3" noloop 

    T "Bien présentez vous dans ce cas."
    play sound "Click.mp3" noloop

    J1 "Bonjour je m'appelle [J1], j'ai 19 ans et voici ma soeur jumelle."
    play sound "Click.mp3" noloop

    J2 "Bonjour je m'appelle [J2], j'ai 19 ans."
    play sound "Click.mp3" noloop

    J "Et nous sommes les \"ultimes jumelles\"."
    play sound "Click.mp3" noloop

    T "Bien enchanté de vous rencontrer."
    play sound "Click.mp3" noloop

    J2 "Merci beaucoup madame."
    play sound "Click.mp3" noloop
    
    T "De rien maintenant à toi là-bas."
    play sound "Click.mp3" noloop

    R "Moi, bien si vous me le permettez."
    play sound "Click.mp3" noloop

    T "Oui vas-y présentes-toi."
    play sound "Click.mp3" noloop

    K "Je m'appelle [K], j'ai 19 ans"
    play sound "Click.mp3" noloop

    T "Bien enchantée de te rencontrer bon suivant maintenant."
    play sound "Click.mp3" noloop 

    N "Je m'appelle [N], j'ai 19 ans."
    play sound "Click.mp3" noloop

    T "Enchantée aussi de te rencontrer [N]."
    play sound "Click.mp3" noloop

    N "Merci beaucoup Madame."
    play sound "Click.mp3" noloop 

    T "De rien maintenant suivant."
    play sound "Click.mp3" noloop 

    Hi "Bonjour je m'appelle [Hi]."
    play sound "Click.mp3" noloop

    T "Ravie de te rencontrer [Hi], bienvenue dans notre classe."
    play sound "Click.mp3" noloop

    Hi "Merci beaucoup Madame."
    play sound "Click.mp3" noloop

    T "Mais de rien [Hi], bon suivant."
    play sound "Click.mp3" noloop

    Y "Je m'appelle [Y], j'ai 19 ans ravie de vous rencontrer."
    play sound "Click.mp3" noloop 

    T "Enchantée de te rencontrer aussi bienvune dans notre classe."
    play sound "Click.mp3" noloop

    Y "Merci beaucoup Madame."
    play sound "Click.mp3" noloop 

# Présentation du personnage principal et AK-24

    T "De rien maintenant vous deux au fond pour finir les présentations."
    play sound "Click.mp3" noloop

    P "Nous, Bien alors si vous le permettez."
    play sound "Click.mp3" noloop

    T "Allez-y donc."
    play sound "Click.mp3" noloop

    P "Je me présente je m'appelle [P], j'ai 19 ans et ancien élève de la chambre blanche."
    play sound "Click.mp3" noloop 

    T "enchanté alors [P], quel est ton projet ?"
    play sound "Click.mp3" noloop

    P "En tant que \"L'ultime Créateur\" mon projet est d'améliorer mon robot humanoïde."
    play sound "Click.mp3" noloop
    
    T "L'ultime créateur intéressant."
    play sound "Click.mp3" noloop

    P "Merci beaucoup."
    play sound "Click.mp3" noloop

    "{b}{i}Soudainement [I] lève la main surprise.{/i}{/b}"
    play sound "Click.mp3" noloop

    T "Oui tu as quelque chose à dire à [P] ?"
    play sound "Click.mp3" noloop

    I "Oui tu as bien dit améliorer ton robot humanoïde ?"
    play sound "Click.mp3" noloop

    P "Oui c'est exacte."
    play sound "Click.mp3" noloop

    I "Putain tu dois vraiment étre un génie pour avoir créer un robot humanoïde je comprend pourquoi tu étais à la chambre blanche."
    play sound "Click.mp3" noloop

    P "Merci beaucoup."
    play sound "Click.mp3" noloop

    T "Bon pour revenir aux présentations [P] qui est cette fille avec toi ?"
    play sound "Click.mp3" noloop 
    
    P "Ah elle justement c'est ma création elle s'appelle [A]."
    play sound "Click.mp3" noloop

    T "C'est donc elle ta fameuse création de robot humanoïde"
    play sound "Click.mp3" noloop

    P "Oui c'est elle, vas-y présentes-toi."
    play sound "Click.mp3" noloop 

    A "Je m'appelle [A], j'ai 18 ans."
    play sound "Click.mp3" noloop

    T "bien et qui es-tu exactement ?" 
    play sound "Click.mp3" noloop

    A "Je suis la création de [P] comme [pronom] a déja dit."
    play sound "Click.mp3" noloop

    T "Ok juste c'est ton vrai prénom ?" 
    play sound "Click.mp3" noloop

    A "Non c'est un prénom \"technique\" que [P] m'a donné."
    play sound "Click.mp3" noloop 
 
    T "Intéressant j'espère qu'[pronom] te trouvera un vrai jolie prénom." 
    play sound "Click.mp3" noloop

    A "Merci et je suis sa fille en quelque sorte"
    play sound "Click.mp3" noloop

    I "[pronom] te considére vraiment comme ça propre fille !?"
    play sound "Click.mp3" noloop

    A "Oui pourquoi cette question ?" 
    play sound "Click.mp3" noloop

    I "Rien c'est juste que je trouve ça mignon qu'[pronom] te considére comme sa fille alors que tu es un robot humanoïde.~"
    play sound "Click.mp3" noloop

    A "Merci beaucoup [I].~"
    play sound "Click.mp3" noloop

    I "Mais de rien c'est normal de complimenter."
    play sound "Click.mp3" noloop

    T "Mais pourquoi tu t'es inscrit ici en tant que lycéenne ?"
    play sound "Click.mp3" noloop

    A "Car je connais pas grand chose ce monde."
    play sound "Click.mp3" noloop
   
    T "Bon merci [A] pour ta présentation."
    play sound "Click.mp3" noloop

    A "De rien."
    play sound "Click.mp3" noloop

#fin des présentations des élèves

    T "Donc les présentations des élèves sont maintenant terminées je vais me présenter."
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde se tournent vers la prof pour l'écouter.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Je m'appelle Sakura Kusanagi mais vous pouvez m'appellez [M]." 
    play sound "Click.mp3" noloop 

    M "J'ai 27 ans et ça fait deux ans que j'enseigne dans le lycée Nexus."
    play sound "Click.mp3" noloop

    M "Le lycée Nexus rassemble les plus talentueux de la région."
    play sound "Click.mp3" noloop 

    M "Ce qui explique pourquoi vous étes que 10 élèves ici."
    play sound "Click.mp3" noloop

    "{b}{i}Tout les élèves sont choqués par cette dernière informations.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Oui je sais c'est surprenant."
    play sound "Click.mp3" noloop 

    M "Bon maintenant je vais vous donner plus de détails sur le lycée Nexus."
    play sound "Click.mp3" noloop

    "{b}{i}Tout les élèves écoutent la professeur.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Ce lycée a un département de pièces détachées ou vous pourrez demander et commander des pièces spécifiques."
    play sound "Click.mp3" noloop

    H "Intéressant à savoir."
    play sound "Click.mp3" noloop

    P "Oui je confirme [H] c'est vraiment intéressant pour nos deux projts de robot."
    play sound "Click.mp3" noloop 

    show screen points 
    M "Donc le lycée vous donnera un budget pour vos projets."
    play sound "Click.mp3" noloop 

    P "On aura vraiment un budget fourni par le Lycée !?"
    play sound "Click.mp3" noloop

    M "Oui vraiment un budget par mois selon vos notes"
    play sound "Click.mp3" noloop 

    P "Vraiment cool alors."
    play sound "Click.mp3" noloop

    M "Maintwnant je vais vous expliquer comment fonctionne l'internat."
    play sound "Click.mp3" noloop

    A "Un internat !?"
    play sound "Click.mp3" noloop

    M "Oui il a été construit récemmment vu que vous venez tous de région éloignée."
    play sound "Click.mp3" noloop

    P "Intéressant."
    play sound "Click.mp3" noloop

    M "Bon je vais vous donner la répartition pour les dortoirs dans l'internat."
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde écoutent la professeur.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Mise à part une dérogation, tout les élèves auront leur propre dortoir."
    play sound "Click.mp3" noloop

    K "Notre propre dortoir ? Cool mais comment ça une dérogation, elle est pour qui ?"
    play sound "Click.mp3" noloop

    Y "Oui Comment ça une dérogation ? Expliquez-nous Madame..."
    play sound "Click.mp3" noloop

    M "Cette Dérogation est pour [P] et [A]."
    play sound "Click.mp3" noloop

    Y "Quoi !?" 
    play sound "Click.mp3" noloop

    M "Oui ils ont demandé à étre dans le méme dortoir."
    play sound "Click.mp3" noloop

    Y "Mais pourquoi vous avez accepté cette demande ?"
    play sound "Click.mp3" noloop

    P "C'est simple car je tiens à la securité de [A], je ne peux pas me permettre de la laisser seule parce-qu'elle ne connais pratiquement rien de ce monde."
    play sound "Click.mp3" noloop

    Y "Ah je comprends mieux pourquoi cette demande."
    play sound "Click.mp3" noloop

    M "Voici la répartition des dortoirs pour vous."
    play sound "Click.mp3" noloop

    M "Le premier étage est pour les lycéennes et le second pour les lycéens."
    play sound "Click.mp3" noloop

    K "Vous entendez les gars un étage de dortoir pour nous seuls."
    play sound "Click.mp3" noloop

    N "Je confirme ça va le feu cette année."
    play sound "Click.mp3" noloop

    P "Je confirme ça va étre génial mais dois-je rappeler qu'on doit rester sérieux en toute circonstance."
    play sound "Click.mp3" noloop

    K "Oh c'est bon fais pas le sérieux, détends-toi un peu."
    play sound "Click.mp3" noloop

    N "il a raison détend-toi peu..."
    play sound "Click.mp3" noloop 

    P "Oui désolé c'est plus fort que moi."
    play sound "Click.mp3" noloop 

    M "calmez-vous s'il vous plait."
    play sound "Click.mp3" noloop 

    P "désolé madame."
    play sound "Click.mp3" noloop 

    M "Il y a pas de soucis juste évitez de bavarder durant le cours."
    play sound "Click.mp3" noloop 

    P "Ok."
    play sound "Click.mp3" noloop 

    M "Bon maintenant que toutes les informations ont été données, vous pouvez disposer le cours est fini, n'hésiter pas à visiter le lycée vu que vous n'avez pas de cours cette après-midi."
    play sound "Click.mp3" noloop

# fin du cours de présentation

    scene black

    hide screen class_404
    "{b}{i}Tout les élèves se mettent à quitter la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene hallway
    show screen hallway 
    play sound "Door.mp3" noloop

    P "Bon [A] on va au dortoir ?"
    play sound "Click.mp3" noloop

    A "Oui pourquoi pas"
    play sound "Click.mp3" noloop

    "{b}{i}Pendant que vous vous diriger au dortoir mais vous entendez une discussion venant de l'un des dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Attend deux secondes [A] j'ai besoin d'aller voir un truc."
    play sound "Click.mp3" noloop

    A "OK pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches de la source pour écouter secrétement.{/i}{/b}"
    play sound "Click.mp3" noloop

    R "le projet de cet élève est trop bien."
    play sound "Click.mp3" noloop

    R "Je confirme on devrait peut-étre le voler"
    play sound "Click.mp3" noloop

    R "OK mais il faudra étre discret."
    play sound "Click.mp3" noloop

    P "On dirait qui sont {b}2{/b}."
    play sound "Click.mp3" noloop

    A "Il se passe quoi [P] ?.~"
    play sound "Click.mp3" noloop

    P "Pas grand chose ne t'inquiètes pas."
    play sound "Click.mp3" noloop

    A "Ok si tu le dis."
    play sound "Click.mp3" noloop

    hide screen hallway
    scene black
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez votre chemin en direction du dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room
    show screen room 
    play sound "Door.mp3" noloop 

    P "Enfin au dortoir."
    play sound "Click.mp3" noloop 

    A "Oui je confirme ça fais du bien."
    play sound "Click.mp3" noloop 

    P "C'est vraiment comfortable."
    play sound "Click.mp3" noloop 

    A "Bon tu veux faire quoi ?"
    play sound "Click.mp3" noloop 

    P "Je sais pas vraiment..."
    play sound "Click.mp3" noloop 

    "{b}{i}Soudainement quelqu'un entre dans le dortoir et vous vous retourner pour voir.{/i}{/b}"
    play sound "Door.mp3" noloop

    R "Bonjour je dois vous voir pour une affaire."
    play sound "Click.mp3" noloop

    P "Bonjour mais qui étes vous ?"
    play sound "Click.mp3" noloop

    Kh "Je m'appelle [Kh],je suis en terminal et la vice-présidente du bureau des élèves."
    play sound "Click.mp3" noloop

    P "Enchanté [Kh], juste pourquoi es-tu venue nous voir ?"
    play sound "Click.mp3" noloop

    Kh "Je suis ici pour vous donner votre budget pour votre projet."
    play sound "Click.mp3" noloop

    "{b}{i}[Kh] Soudainement tu reçois l'argent sur ton compte.{/i}{/b}"
    play sound "Click.mp3" noloop
    $ pts += 10000

    P "Pourquoi c'est vous qui l'a transféré et non la présidente ?"
    play sound "Click.mp3" noloop

    Kh "Car elle est beaucoup occupé avec la paperasse de début d'année donc elle m'a demander de m'en charger personellement."
    play sound "Click.mp3" noloop 

    P "Donc j'ai [pts] points nexus pour le mois ?"
    play sound "Click.mp3" noloop

    Kh "Oui pour ton prjet et ta nourriture et les loisirs"
    play sound "Click.mp3" noloop

    P "Ok je vois mieux merci beacoup."
    play sound "Click.mp3" noloop 

    Kh "De rien mais j'ai une question."
    play sound "Click.mp3" noloop

    P "Oui dit moi [Kh]."
    play sound "Click.mp3" noloop

    Kh "Pourrai-je voir la fameuse petite [A] qu'[E] m'a parlé."
    play sound "Click.mp3" noloop

    P "Oui biensur, [A] tu peux venir s'il te plait."
    play sound "Click.mp3" noloop

    A "Oui qu'il y a t'il ?"
    play sound "Click.mp3" noloop

    P "[Kh] voudrait te voir en personne"
    play sound "Click.mp3" noloop

    A "Ok alors"
    play sound "Click.mp3" noloop

    Kh "C'est donc toi la fameuse petite [A] dont tout le monde parle."
    play sound "Click.mp3" noloop

    A "oui c'est bien moi.~"
    play sound "Click.mp3" noloop

    Kh "Ravie de te rencontrer."
    play sound "Click.mp3" noloop

    A "Merci beaucoup."
    play sound "Click.mp3" noloop

    Kh "Pas de soucis mais je dois y aller malheureusement."
    play sound "Click.mp3" noloop

    P "Juste [Kh] j'ai une question, tu sais ou sont les salles pour les clubs ?"
    play sound "Click.mp3" noloop

    Kh "Elles sont au rez-de-chaussé."
    play sound "Click.mp3" noloop

    P "Merci boucoup."
    play sound "Click.mp3" noloop

    Kh "Mais de rien."
    play sound "Click.mp3" noloop

    "{b}{i}[Kh] quitte la chambre.{/i}{/b}"
    play sound "Click.mp3" noloop 

    A "Bon on fais quoi maintenant ?"
    play sound "Click.mp3" noloop

    P "Je vais..."
    play sound "Menu.mp3" noloop

    menu :    

        "{b}{i}Visiter le lycée{/i}{/b}" :
            jump balade
        "{b}{i}Travailler sur AK-24{/i}{/b}" :
            jump work

label balade:

    play sound "Menu.mp3" noloop

    P "Aller visiter le lycée seul."
    play sound "Click.mp3" noloop

    A "Ok je vais en profiter pour rester au dortoir et me déconnecter un peu."
    play sound "Click.mp3" noloop

    P "OK je fais vite et je reviens rapidement."
    play sound "Click.mp3" noloop

    hide screen room
    scene black
    play sound "Click.mp3" noloop 

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway
    show screen hallway 
    play sound "Door.mp3" noloop 

    P "Bon elle m'a dit que c'est au rez de chaussé donc j'y vais."
    play sound "Click.mp3" noloop

    hide screen hallway
    scene black
    play sound "Click.mp3" noloop

    "{b}{i}Tu te diriges au rez de chaussé.{/i}{/b}"
    play sound "Click.mp3" noloop
     
    scene hall 
    play sound "Click.mp3" noloop 

    P "Bon voyons voir...."     
    play sound "Click.mp3" noloop 

    P "On dirait que c'est ici."
    play sound "Click.mp3" noloop 
    
    scene black
    play sound "Click.mp3" noloop

    "{b}{i}Tu te diriges la salle de club général.{/i}{/b}"
    play sound "Click.mp3" noloop
 
    scene clubroom
    show screen clubroom 
    play sound "Door.mp3" noloop

    P "C'est donc ça la salle de club général du lycée."
    play sound "Click.mp3" noloop

    "{b}{i}Tu regardes un peu la salle et tu aperçois [I].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut [I]."
    play sound "Click.mp3" noloop

    I "Oh salut [P] comment ça va ?"
    play sound "Click.mp3" noloop

    P "Je vais bien mais sinon que fais tu ici ?"
    play sound "Click.mp3" noloop

    I "Je travaille sur mon jeu vidéo et toi ?"
    play sound "Click.mp3" noloop

    P "je suis juste venu voir la salle de club."
    play sound "Click.mp3" noloop

    "{b}{i}Tu regardes un peu et tu aperçois une cartouche sur une table.{/i}{/b}"
    play sound "Menu.mp3" noloop 

label choice1: 

    menu :    

        "{b}{i}Demander à Iris ce que c'est{/i}{/b}" :
            jump ask 
        "{b}{i}Retourner au dortoir{/i}{/b}" :
            jump dorm1

label ask: 

    play sound "Menu.mp3" noloop

    P "[I], C'est quoi cette cartouche ?"
    play sound "Click.mp3" noloop

    I "Laisse tomber c'est mon ancien jeu vidéo qui se nommait Anarchy School."
    play sound "Click.mp3" noloop

    P "Ok je vois mais pourquoi tu l'as abandonné ?"
    play sound "Click.mp3" noloop

    I "Car je me suis trop inspirer d'un autre jeu que j'aime."
    play sound "Click.mp3" noloop

    P "Ah oui carrément..."
    play sound "Click.mp3" noloop 

    I "Oui mais passe moi la cartouche je vais m'en débarrasser une bonne fois pour toute."
    play sound "Click.mp3" noloop

    P "Ok tiens."
    play sound "Click.mp3" noloop 

    "{b}{i}[I] te prend la cartouche avant de la détruitre sous tes yeux.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu veux vraiment faire ça ?"
    play sound "Click.mp3" noloop 

    I "Oui je veux oublier mon échec."
    play sound "Click.mp3" noloop

    P "ok je juge pas."
    play sound "Click.mp3" noloop

    play sound "Stumble.mp3" noloop
    "{b}{i}Puis soudainement tu entends un fort bruit venant d'au-dessus.{/i}{/b}"
    play sound "Click.mp3" noloop 
    
    P "Iris juste c'est bien les dortoirs juste au-dessus ?"
    play sound "Click.mp3" noloop

    I "Oui pourquoi ?"
    play sound "Click.mp3" noloop 

    P "Car j'ai entendu un bruit venant d'au-dessus."
    play sound "Click.mp3" noloop

    "{b}{i}Puis tu réalises ce qui ce passe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Qu'est-ce qui se passe ?"
    play sound "Click.mp3" noloop 

    P "Je dois te laisser j'ai une urgence !"
    play sound "Click.mp3" noloop
    
    scene black
    hide screen clubroom
    play sound "Click.mp3" noloop

    P "..."
    play sound "Click.mp3" noloop
     
    scene hall 
    play sound "Door.mp3" noloop 

    P "..."     
    play sound "Click.mp3" noloop 

    scene black
    play sound "Click.mp3" noloop

    P "..."
    play sound "Click.mp3" noloop

    scene hallway
    play sound "Click.mp3" noloop

    P "..."
    play sound "Click.mp3" noloop

    scene black
    play sound "Click.mp3" noloop

    P "..."
    play sound "Click.mp3" noloop

    scene room
    show screen room 
    play sound "Door.mp3" noloop 

    "{b}{i}En arrivant tu vois [A] complétement détruite et demontée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Mince j'aurais du étre plus vigilant avec elle, mon projet est ruiné."
    play sound "Click.mp3" noloop 

    scene black 
    hide screen room
    hide screen points
    play music "gameover.mp3" noloop
    "{b}{i}Fin numéro 1 : [A] complétement détruite et ruinée par manque de vigilance.{/i}{/b}"
    play sound "Menu.mp3" noloop

    menu :    

        "{b}{i}Abandonner{/i}{/b}" :
            return 
        "{b}{i}Réessayer{/i}{/b}" : 
            scene clubroom 
            show screen clubroom
            show screen points
            play music "Soundtrack.mp3" loop volume 1.0
            jump choice1 

label dorm1:

    P "Bon [I] je vais retourner au dortoir."
    play sound "Click.mp3" noloop 

    I "Ok pas de soucis alors"
    play sound "Click.mp3" noloop

    hide screen clubroom
    scene black
    play sound "Click.mp3" noloop

    P "Tu te diriges vers le hall."
    play sound "Click.mp3" noloop

    scene hall 
    play sound "Door.mp3" noloop 

    P "Bon je vais retourner travailler sur [A]."     
    play sound "Click.mp3" noloop 

    scene black
    play sound "Click.mp3" noloop

    P "..."
    play sound "Click.mp3" noloop

    scene hallway
    play sound "Click.mp3" noloop

    "{b}{i}Dans le couloir tu croises les jumelles.{/i}{/b}"
    play sound "Click.mp3" noloop

    J1 "Oh salut [P] que fais-tu ici ?"
    play sound "Click.mp3" noloop 

    P "Je vais retourner voir [A] pour travailler et vous ?"
    play sound "Click.mp3" noloop

    J1 "Nous allons dans la salle de club général."
    play sound "Click.mp3" noloop

    J2 "Oui car nous devons voir un truc."
    play sound "Click.mp3" noloop

    P "Ok alors"
    play sound "Click.mp3" noloop

    "{b}{i}Puis tu continues ton chemin ver le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black 
    play sound "Click.mp3" noloop

    P "..."
    play sound "Click.mp3" noloop

    scene room
    show screen room 
    play sound "Door.mp3" noloop 

    P "Coucou je suis de retour."
    play sound "Click.mp3" noloop

    "{b}{i}[A] se reconnecte avant d'ouvrir les yeux.{/i}{/b}"
    play sound "Click.mp3" noloop 

    A "Coucou."
    play sound "Click.mp3" noloop 

    P "ça va ?"
    play sound "Click.mp3" noloop

    A "Oui mais sinon tu vas faire quoi maintenant ?"
    play sound "Click.mp3" noloop

label work: 

    show screen room 
    P "Je vais travailler sur ton amélioration." 
    play sound "Click.mp3" noloop

    A "Tu vas faire quoi exactement ?"
    play sound "Click.mp3" noloop

    P "Je vais d'abord le département pour commander un nouveau processeur."
    play sound "Click.mp3" noloop

    A "Comment ça un nouveau processeur ?"
    play sound "Click.mp3" noloop

    P "Oui car depuis que je t'ai écupéré tu as toujours ton ancien processeur avec le quel tu as été conçu donc je vais le changer."
    play sound "Click.mp3" noloop

    A "Oui je vois mieux."
    play sound "Click.mp3" noloop

    P "Je vais commander ce qu'il faut."
    play sound "Click.mp3" noloop

    A "Ok alors."
    play sound "Click.mp3" noloop

    "{b}{i}Tu prend ton téléphone pour appeler le département.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Boujour, suis-je bien en contact avec le département des piéces détachées ?"
    play sound "Click.mp3" noloop

    R "Oui c'est exact, pourrais-je juste savoir à quel élèves je m'adresse s'il vous plait ?"
    play sound "Click.mp3" noloop

    P "Désolé je m'appelle [P] en Seconde-E."
    play sound "Click.mp3" noloop 

    Ah "Enchanté je suis [Ah], la présidente du département, quelle est votre demande ?"
    play sound "Click.mp3" noloop

    P "J'aimerai commander un processeur Corzen."
    play sound "Click.mp3" noloop

    Ah "Bien sur le quel voulez-vous commander car j'ai actuellement le Corzen 11 et le Corzen 11K."
    play sound "Menu.mp3" noloop
    
label choice2:

    menu :    

        "{b}{i}Choisir le Corzen 10{/i}{/b}" :
            jump lowcpu
        "{b}{i}Choisir le Corzen 11K{/i}{/b}" :
            jump highcpu
    
label lowcpu:

    play sound "Menu.mp3" noloop

    P "Je vais vous prendre le Corzen 10 car je pense que se sera suffisant."
    play sound "Click.mp3" noloop

    Ah "OK alors pas de soucis ça fera 1000 points."
    play sound "Click.mp3" noloop

    P "Ok je vous envoie ça toute de suite"
    play sound "Click.mp3" noloop

    "{b}{i}Tu effectues le paiement.{/i}{/b}"
    play sound "Click.mp3" noloop 
    $ pts -= 1000 

    Ah "Merci beaucoup."
    play sound "Click.mp3" noloop

    P "Par contre quand est-ce que je receverrai mon processeur ?"
    play sound "Click.mp3" noloop

    Ah "le temps que mon équipe le prépare je dirait dans 1 heure."
    play sound "Click.mp3" noloop

    P "Merci beuacoup."
    play sound "Click.mp3" noloop

    Ah "Mais de rien [P]."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu finis par raccrocher.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[A] c'est bon j'ai commander ton nouveau processeur."
    play sound "Click.mp3" noloop

    A "Cool alors."
    play sound "Click.mp3" noloop

    P "Bon je vais chercher à manger car il est 12h30"
    play sound "Click.mp3" noloop 

    A "Ok moi je vais me déconnecter"
    play sound "Click.mp3" noloop

    scene black
    hide screen room

    "{b}{i}Tu pars manger avant de revenir au dortoir vers 13h45.{/i}{/b}"
    play sound "Click.mp3" noloop
    $ pts -= 100

    scene room 
    show screen room 

    P "C'est bon je suis de retour et j'ai pu récupéré le processeur."
    play sound "Click.mp3" noloop

    A "Cool je suis prete alors"
    play sound "Click.mp3" noloop

    "{b}{i}Tu déconnectes complétement [A] avant d'accéder à l'emplacement pour le processeur.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon voyons voir cet ancien processeur à changer..."  
    play sound "Click.mp3" noloop

    "{b}{i}Tu découvres avec surprise qu'elle a un processeur Corzen 7.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Alors l'ancien propriétaire de [A] avais vraiment des gouts médiocres en terme de composants."
    play sound "Click.mp3" noloop

    "{b}{i}Tu déballes le nouveau processeur pour voir la notice.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Ok."
    play sound "Click.mp3" noloop

    "{b}{i}Tu retires délicatement l'ancien processeur pour installer le nouveau.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon ça c'est fait maintenant je vais la redémarrer."
    play sound "Click.mp3" noloop

    A "Initialisation...."
    play sound "Click.mp3" noloop

    "{b}{i}Mais soudainement le processeur brule complétement et endommage les autres composants de [A].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Mince..."
    play sound "Menu.mp3" noloop

    scene black
    hide room
    hide screen room
    hide screen points

    play music "gameover.mp3" noloop
    "{b}{i}Fin numéro 2 : Processeur trop faible pour la puissance demandé par le systéme d'[A].{/i}{/b}"
    play sound "Menu.mp3" noloop

    menu :    

        "{b}{i}Abandonner{/i}{/b}" :
            return 
        "{b}{i}Réessayer.{/i}{/b}" :
            scene room
            show screen room
            show screen points 
            play music "Soundtrack.mp3" loop volume 1.0
            jump choice2 

label highcpu:
    
    play sound "Menu.mp3" noloop

    P "Je vais vous prendre le Corzen 11k."
    play sound "Click.mp3" noloop

    Ah "Ok alors pas de soucis ça te fera 1500 points."
    play sound "Click.mp3" noloop

    P "Ok je vous envoie ça toute de suite."
    play sound "Click.mp3" noloop

    "{b}{i}Tu effectues le paiement.{/i}{/b}"
    play sound "Click.mp3" noloop 
    $ pts -= 1500

    Ah "Merci beaucoup."
    play sound "Click.mp3" noloop

    P "Par contre quand est-ce que je receverrai mon processeur ?"
    play sound "Click.mp3" noloop

    Ah "Le temps que mon équipe le prépare je dirait dans 1 heure."
    play sound "Click.mp3" noloop

    P "Merci beuacoup."
    play sound "Click.mp3" noloop

    Ah "Mais de rien [P]."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu finis par raccrocher.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[A] c'est bon j'ai commander ton nouveau processeur."
    play sound "Click.mp3" noloop

    A "Cool alors."
    play sound "Click.mp3" noloop

    P "Bon je vais chercher à manger car il est 12h30"
    play sound "Click.mp3" noloop 

    A "Ok moi je vais me déconnecter"
    play sound "Click.mp3" noloop

    scene black
    hide screen room

    "{b}{i}Tu pars à manger avant de revenir au dortoir vers 13h45.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room 
    show screen room 

    P "C'est bon je suis de retour et j'ai pu récupéré le processeur."
    play sound "Click.mp3" noloop

    A "Cool je suis prete alors"
    play sound "Click.mp3" noloop

    "{b}{i}Tu déconnectes complétement [A] avant d'accéder à l'emplacement pour le processeur.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon voyons voir cet ancien processeur à changer..."  
    play sound "Click.mp3" noloop

    "{b}{i}Tu découvres avec surprise qu'elle a un processeur Corzen 7.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Alors l'ancien propriétaire de [A] avais vraiment des gouts médiocres en terme de composants."
    play sound "Click.mp3" noloop

    "{b}{i}Tu déballes le nouveau processeur pour voir la notice et tu vois un message de la part de [Ah].{/i}{/b}"
    play sound "Click.mp3" noloop 
     
    Ah "{i}finalement j'ai regardé le dossier de ton projet et j'ai pu te trouver un Corzen 11KS spécialement pour [A] et qui est mieux donc tu peux le garder et je ne te ferai pas payer la différence de prix.{/i}"   
    play sound "Click.mp3" noloop

    P "Ok génial."
    play sound "Click.mp3" noloop

    "{b}{i}Tu retires délicatement l'ancien processeur pour installer le nouveau.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon ça c'est fait maintenant je vais la redémarrer."
    play sound "Click.mp3" noloop

    "Initialisation...."
    play sound "Click.mp3" noloop 

    P "Allez allez..."
    play sound "Click.mp3" noloop

    "Initialisation de [A] terminée."
    play sound "Menu.mp3" noloop

    P "Comment ça va ?"
    play sound "Click.mp3" noloop

    A "Je vais bien."
    play sound "Click.mp3" noloop 

    P "Bon maintenant je vais ragarder si tu as des nouveau paramétres."
    play sound "Click.mp3" noloop

    A "Ok vas-y."
    play sound "Click.mp3" noloop
    
    "{b}{i}Tu ouvres le pannau configuration de [A] depuis ton ordinateur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon voyons voir."
    play sound "Click.mp3" noloop

    "{b}{i}Tu regardes les paramétres et tu vois un paramétre de prénom par défaut.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Tiens on dirait que ton ancien propriétaire t'a laissé un prénom par défaut."
    play sound "Click.mp3" noloop

    A "Ah bon le quel ?"
    play sound "Click.mp3" noloop

    P "Ar...Aris on dirait."
    play sound "Click.mp3" noloop

    A "Aris !? Je trouve que c'est mignon comme prénom.~"
    play sound "Click.mp3" noloop

    P "Donc ça te vas Aris alors ?"
    play sound "Click.mp3" noloop

    A "Oui bien évidemment la question se pose pas dans ce cas de figure !"
    play sound "Click.mp3" noloop

    P "Ok."
    play sound "Click.mp3" noloop

    "{b}{i}Tu ouvres le paramétre pour enregistrer un prénom.{/i}{/b}"
    play sound "Menu.mp3" noloop

label choice3:

    play sound "Menu.mp3" noloop
    $ newname = renpy.input("Veuillez écrire le nouveau prénom de AK-24.")
    $ newname = newname.strip()

    if newname == "Aris":

        "Le prénom a été enregistré dans le système." 
        play sound "Menu.mp3" noloop

    else:

        "Erreur système. Veuillez réessayer."
        $ renpy.restart_interaction() 
        play sound "Menu.mp3" noloop
        jump choice3

    "{b}{i}Soudainement, le processeur te demande de paramétrer l'adresse IP de [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Mince..."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes les paramètres et tu vois que tu dois mettre l'adresse IP.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "J'ai une idée : je vais faire en sorte que chaque lettre de [newname] soit un nombre correspondant à sa position dans l'alphabet."
    play sound "Click.mp3" noloop
   
    "{b}{i}Essaye de trouver l'adresse en utilisant ce principe pour chaque lettre.{/i}{/b}"

label choice4:

    play sound "Menu.mp3" noloop
    $ ip = renpy.input("Entrez l'adresse IP de [newname] en suivant la méthode de conversion suggérée (trois chiffres pour chaque partie).")
    $ ip = ip.strip()

    if ip == "001.018.009.019":

        "{b}{i}Initialisation de l'adresse IP en cours...{/i}{/b}"
        play sound "Menu.mp3" noloop

        "{b}{i}L'adresse IP a été enregistrée dans le système.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        "{b}{i}L'adresse IP de [newname] est maintenant [ip].{/i}{/b}"
        play sound "Click.mp3" noloop

    else:

        "{b}{i}Erreur système. L'adresse IP est incorrecte. Vérifie la méthode de conversion et réessaye.{/i}{/b}"
        play sound "Menu.mp3" noloop 
        jump choice4 

    P "J'ai fini le paramétrage."
    play sound "Click.mp3" noloop

    P "Maintenant je vais me connecter depuis mon ordi pour la redémarrer."
    play sound "Click.mp3" noloop

    "{b}{i}tu redémarre [newname] tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "C'est bon mon nouveau prénom et mon adresse IP ont été configuré."
    play sound "Click.mp3" noloop 

    P "Cool alors génial."
    play sound "Click.mp3" noloop

    Na "J'en ai profité pour enregistrer ton nom de famille comme le mien vu que je suis ta création."
    play sound "Click.mp3" noloop

    P "Ah bon tu l'as fait par toi meme !?"
    play sound "Click.mp3" noloop

    Na "Oui absolument."
    play sound "Click.mp3" noloop
    
    P "Ok je ne savais pas que tu en étais capable."
    play sound "Click.mp3" noloop 

    Na "Je sais des fois je peux vraiment surprendre."
    play sound "Click.mp3" noloop 

    P "Bon on va dans la salle de notre club pour bosser ?"  
    play sound "Click.mp3" noloop

    Na "Oui allons-y."
    play sound "Click.mp3" noloop 

    P "Mais d'abord on va devoir passer dans le bureau pour récupérer la clé de la salle"
    play sound "Click.mp3" noloop 
     
    Na "Ok"
    play sound "Click.mp3" noloop 
    
    scene black 
    hide screen room

    "{b}{i}Tu diriges vers le bureau des élèves avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop
     
    scene hall

    P  "Bon on est presque arriver"
    play sound "Click.mp3" noloop

    scene black 

    "{b}{i}Tu entres dans le bureau des élèves avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop
    
    # discussion pour avoir une salle de club.

    scene office 
    show screen office 
    play sound "Door.mp3" noloop 

    P "Bonjour c'est moi [nom]"
    play sound "Click.mp3" noloop

    E "Oh c'est toi que puis-je faire pour toi ?"
    play sound "Click.mp3" noloop

    P "j'aimerais une salle de club pour moi et [newname]."
    play sound "Click.mp3" noloop

    E "Oui pas de souci donc je vois que tu as choisi mon idée."
    play sound "Click.mp3" noloop

    P "Oui c'est exacte." 
    play sound "Click.mp3" noloop 

    E "Donc pas de soucis je vais te chercher la clé d'une des salles de club." 
    play sound "Click.mp3" noloop

    P "Ok" 
    play sound "Click.mp3" noloop

    "{b}{i}[E] s'absenta le temps de trouver la clé.{/i}{/b}"
    play sound "Click.mp3" noloop 
   
    P "J'ai vraiment hate d'avoir notre propre salle pour travailler." 
    play sound "Click.mp3" noloop
   
    Na "Oui moi aussi car on pourra vraiment étre tranquille." 
    play sound "Click.mp3" noloop

    "{b}{i} Puis [E] revient avec la clé.{/i}{/b}"
    play sound "Click.mp3" noloop 

    E "Voici la clé de la salle de club." 
    play sound "Click.mp3" noloop 

    P "Merci beaucoup." 
    play sound "Click.mp3" noloop

    E "Si jamais votre salle de club se trouve au fond du couloir." 
    play sound "Click.mp3" noloop

    P "Ok merci" 
    play sound "Click.mp3" noloop

    E "De rien ça fait toujours plaisir." 
    play sound "Click.mp3" noloop

    P "bon on y vas [newname] vu qu'on a la clé" 
    play sound "Click.mp3" noloop

    Na "Ok" 
    play sound "Click.mp3" noloop

    hide screen office
    scene black

    "{b}{i}Tu quittes le bureau des élèves avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hall
    show screen hall 

    P "Bon elle a dit que c'était au food du couloir."
    play sound "Click.mp3" noloop

    Na "Ok" 
    play sound "Click.mp3" noloop

    "{b}{i}tu te diriges vers la salle puis tu croises soudainement [I] qui sort de la salle de club général.{/i}{/b}"
    play sound "Click.mp3" noloop

    P  "Oh salut [I], quoi de nouveau ?"
    play sound "Click.mp3" noloop

    I  "pas grand chose je vais retourner au dortoir et toi ?"
    play sound "Click.mp3" noloop

    P  "Je vais bosser sur [newname] dans la salle de club."
    play sound "Click.mp3" noloop

    I  "[newname] !? Attend tu lui as finalemnt trouver un prénom ?"
    play sound "Click.mp3" noloop

    P  "Oui."
    play sound "Click.mp3" noloop 

    I "je suis contente pour toi [newname]."
    play sound "Click.mp3" noloop

    Na  "Merci beaucoup"
    play sound "Click.mp3" noloop

    I "De rien c'est normal et c'est surtout [M] qui va étre contente que tu aies finalement un vrai prénom."
    play sound "Click.mp3" noloop

    P  "Bon on y vas [newname] ?"
    play sound "Click.mp3" noloop

    I "Juste [prénom] j'ai un cadeau pour [newname]."
    play sound "Click.mp3" noloop 

    P " c'est quoi ?"
    play sound "Click.mp3" noloop

    P "Oh merci beaucoup."
    play sound "Menu.mp3" noloop 

    "{b}{i}Carte mémoire obtenue.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "De rien"
    play sound "Click.mp3" noloop 

    P "Bon [newname] on y vas."   
    play sound "Click.mp3" noloop 

    Na "Ok."
    play sound "Click.mp3" noloop

    scene black
    hide screen hall

    "{b}{i}Tu entres dans la salle de club avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop
    
    scene clubroom
    show screen clubroom 
    play sound "Door.mp3" noloop

    P "Bon par quoi  pourrait-je commencer ?"
    play sound "Click.mp3" noloop 

    Na "je ne sais mais tu peux regarder la carte mémoire."
    play sound "Click.mp3" noloop 

    P "pas de souci."
    play sound "Click.mp3" noloop

    Na "ok moi je vais me déconnecter pendant ce temps."
    play sound "Click.mp3" noloop

    P "Ok alors."
    play sound "Click.mp3" noloop

    Na "Déconnexion...."
    play sound "Click.mp3" noloop
    
    P "Bon voyons voir ça."
    play sound "Click.mp3" noloop

    "{b}{i}Après avoir analyser la carte tu commences à travailler.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon je vais installer la carte mémoire dans le systéme d'[newname]."
    play sound "Click.mp3" noloop

    "{b}{i}Tu installes la carte mémoire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon ça c'est fait."
    play sound "Click.mp3" noloop

    P "Maintenant je vais paramétrer sa configuration de lycéenne mais il faut que je commande du matériel."
    play sound "Click.mp3" noloop 

    "{b}{i}tu te poses et commandes le matériel qui qu'il te faut.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Ok alors voyons voir combien ça va me couter."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu vois que tu en as pour 1000 points avant de commander.{/i}{/b}"
    play sound "Click.mp3" noloop 
    $ pts -= 1000

    P "Bon ça c'est commandé."
    play sound "Door.mp3" noloop 

    "{b}{i}Soudainement [J1] entre dans la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    J1 "Salut [prénom] je voulais savoir si je pouvais rejoindre ton club."
    play sound "Click.mp3" noloop 

    P "Euh...."
    play sound "Menu.mp3" noloop 

    menu :    

        "{b}{i} Refuser [J1].{/i}{/b}" :  
            play sound "Menu.mp3" noloop 

    P "C'est pas contre toi mais je préfére étre seul avec [newname]"
    play sound "Click.mp3" noloop 

    J1 "Ok je comprends c'est ton choix."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis [J1] quitta la salle avant que tu continues de travailler.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene black
    "{b}{i} Une heure plus tard.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene clubroom
    P "Bon J'ai le matériel pour paramétrer [newname]."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu ouvres les paramétres de [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    "{b}{i} Mais soudainement l'adresse IP 001.009.011.015 tente de se connecter.{/i}{/b}"
    play sound "Menu.mp3" noloop 

label choice5: 

    menu :    

        "{b}{i} Refuser {/i}{/b}" :  
            jump no
        "{b}{i} accepter {/i}{/b}" :  

            "{b}{i} Tu acceptes la connexion mais [newname] agit bizarrement.{/i}{/b}"
            play sound "Click.mp3" noloop 

            scene black 
            hide screen clubroom
            hide screen points
            play music "gameover.mp3" noloop
            "{b}{i} Fin numéro 3 : [A] complétement piratée par l'ultime hacker avec l'adresse IP 001.009.011.015.{/i}{/b}"
            play sound "Menu.mp3" noloop

            menu :    

                "{b}{i}Abandonner{/i}{/b}" :
                    return 
                "{b}{i}Réessayer{/i}{/b}" : 
                    scene clubroom 
                    show screen clubroom
                    show screen points
                    play music "Soundtrack.mp3" loop volume 1.0
                    jump choice5

label no: 

    P "Bon voyons voir ça."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu configures [newname] pendeant trois heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon ça c'est enfin configurée."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu redémarres [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "initialisation en cours...."
    play sound "Click.mp3" noloop 

    P "vas-y"
    play sound "Click.mp3" noloop

    Na "Configuration terminée, bonjour [P]"
    play sound "Click.mp3" noloop 

    P "Comment ça va ?"
    play sound "Click.mp3" noloop

    Na "Je vais bien."
    play sound "Click.mp3" noloop 

    P "Bon on retourne au dortoir ?"
    play sound "Click.mp3" noloop

    Na "Oui bien sur"
    play sound "Click.mp3" noloop 

    scene black 
    hide screen clubroom

    "{b}{i}Tu te dirige vers le hall et le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene hallway
    show screen hallway 

    P  "Cette prémière journée était vraiment fatiguante."
    play sound "Click.mp3" noloop

    Na "je confirme."
    play sound "Click.mp3" noloop 

    hide hallway
    scene black

    "{b}{i}Tu te dirige vers le hall et le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene room 
    show screen room 

    P "Enfin au dortoir..."
    play sound "Click.mp3" noloop

    Na "Je confirme ça fait vraiment du bien."
    play sound "Click.mp3" noloop 

    P "Bon je vais poser mes affaires."
    play sound "Click.mp3" noloop 

    Na "Ok"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu poses tes affaires dans ton placard.{/i}{/b}"
    play sound "Click.mp3" noloop 
     
    P "Bon on vas se coucher maintement."
    play sound "Click.mp3" noloop 

    Na  "Ok moi je vais me déconnecter jusqu'a demanin."
    play sound "Click.mp3" noloop 

    scene black
    "{b}{i}Tu te couches jusqu'au lendemain.{/i}{/b}"
    play sound "Click.mp3" noloop   
    
    scene room 
    play sound "Alarm.mp3" noloop 

# second jour de cours.

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "mhmmm déjà. Super....."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te léves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Aris tu es préte ?"
    play sound "Click.mp3" noloop 

    P "Aris....?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnctée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sacrée Aris toujours envie d'étre déconnectée."
    play sound "Click.mp3" noloop 

    P "Bon je vais la démarrer manuellement."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Démarrage en cours...."
    play sound "Click.mp3" noloop 

    Na  "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    P "Bonjour. comment ça va ?"
    play sound "Click.mp3" noloop 

    Na "Je vais bien comme d'habitude et toi ?"
    play sound "Click.mp3" noloop 

    P "Moi ça va super juste un peu fatigué."
    play sound "Click.mp3" noloop 

    Na "Toi tu as encore passé toute la nuit à progammmer."
    play sound "Click.mp3" noloop 

    P "Hey je me suis reposé aussi je ne pense pas qu'à la programmation et ton amélioration, tu devrais surtout dire ça à [I]."
    play sound "Click.mp3" noloop 

    Na "C'est bon [prénom] je te taquine.~"
    play sound "Click.mp3" noloop 

    P "Bon on va en cours avant d'étre en retard."
    play sound "Click.mp3" noloop 

    Na "Ok"
    play sound "Click.mp3" noloop 
    
    hide screen room
    scene black 

    "{b}{i}Tu te diriges vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene hallway
    show screen hallway 

    "{b}{i}Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    "{b}{i}Puis soudainement tu vois tout les autres élèves à l'entrée de la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Vous étes déjà tous là."
    play sound "Click.mp3" noloop 

    H "Oui [M] n'est pas encore arrivée."
    play sound "Click.mp3" noloop 

    P "J'espère qu'on n'aura pas d'examen surprise aujourd'hui vue qu'on est début de l'année."
    play sound "Click.mp3" noloop 

    Y "Moi aussi, mais j'ai entendu dire que [M] pourrait bien nous surprendre."
    play sound "Click.mp3" noloop 

    Na "Un examen surprise !? c'est quoi ?"
    play sound "Click.mp3" noloop 

    Y "Ah oui c'est vrai tu ne connais rien de ce monde, je vais t'expliquer."
    play sound "Click.mp3" noloop 

    Na "Ok je t'écoute."
    play sound "Click.mp3" noloop 

    Y "Un examen surprise c'est un examen prévu sur l'instant meme."
    play sound "Click.mp3" noloop 

    Na "What the fuck !?"
    play sound "Click.mp3" noloop 

    Y "Hey mais d'ou tu connais cette insulte."
    play sound "Click.mp3" noloop 

    "[newname] te pointe secrétement."
    play sound "Click.mp3" noloop 

    Y "[prénom] tu n'as pas honte de lui apprendre des insultes."
    play sound "Click.mp3" noloop 

    P "Hey je lui ai juste appris à parler avec les autres, les insultes j'y suis pour rien."
    play sound "Bell.mp3" noloop 

    "{b}{i}Au meme moment la prof arriva et ouvra la porte de la classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour chers élèves."
    play sound "Click.mp3" noloop 

    hide screen hallway
    scene black

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom 
    show screen class_404 
    "{b}{i}Tout le monde s'assoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

# cours sur la guerre de 2096 

    M "Bon aujourd'hui petit cours d'histoire sur la guerre technologique."
    play sound "Click.mp3" noloop 

    P "Cool."
    play sound "Click.mp3" noloop 

    M "Pour cela petit controle surprise, sortez une feuille blanche."
    play sound "Click.mp3" noloop
 
    I "Dés le second jour de cours sérieusement.."
    play sound "Click.mp3" noloop 

    M "Oui je vous avez dit que c'est un lycée pour l'élite."
    play sound "Click.mp3" noloop 

    M "bon premiére question : En quelle année se déroule la guerre ?"
    play sound "Click.mp3" noloop 

    M "A) en 2094. B) En 2095-2096. ou C) En 2096."
    play sound "Click.mp3" noloop 

    menu :    

        "{b}{i}A{/i}{/b}" :
            $ grd += 0.0
        "{b}{i}B.{/i}{/b}" : 
            $ grd += 5.0
        "{b}{i}C.{/i}{/b}" : 
            $ grd += 2.5 

    M "Seconde question : Quelle technologie a été utiliser lors de la guerre ?"
    play sound "Click.mp3" noloop 

    M "A) les IA. B) les robots. ou C) les robots humanoides."
    play sound "Click.mp3" noloop 

    menu :    

        "{b}{i}A{/i}{/b}" :
            $ grd += 0.0
        "{b}{i}B.{/i}{/b}" : 
            $ grd += 2.5
        "{b}{i}C.{/i}{/b}" : 
            $ grd += 5.0 

    M "Troisiéme question : Dans quel pays se déroula la guerre ?"
    play sound "Click.mp3" noloop 

    M "A) Japon. B) états-unis. ou C) Russie."
    play sound "Click.mp3" noloop 

    menu :    

        "{b}{i}A{/i}{/b}" :
            $ grd += 5.0
        "{b}{i}B.{/i}{/b}" : 
            $ grd += 0.0
        "{b}{i}C.{/i}{/b}" : 
            $ grd += 0.0

    M "Dernière question : les Robots humanoide ont il des émotions ?"
    play sound "Click.mp3" noloop 

    menu :    

        "{b}{i}Oui{/i}{/b}" :
            $ grd += 5.0
        "{b}{i}Non.{/i}{/b}" : 
            $ grd += 0.0

    M "Maintenant remettez-moi votre copie je vais vous les corriger tout de suite."
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde remit leur copie à [M].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "C'était pas si compliqué."
    play sound "Click.mp3" noloop 

    Hi "On verra bien les résultats."
    play sound "Click.mp3" noloop

    "{b}{i}Vous discutez pendant 25 minutes le temps que [M] corrige les copies.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "C'est bon j'ai vos résultats."
    play sound "Click.mp3" noloop  

    Na "Oui enfin..."
    play sound "Click.mp3" noloop

    P "Enfin.."
    play sound "Click.mp3" noloop

    M "Bon je vais commemcer par [P] et [Na]"
    play sound "Click.mp3" noloop

    P "Ok"
    play sound "Click.mp3" noloop

    M "[P] tu as eu [grd]"
    play sound "Click.mp3" noloop 

    if grd == 20.0:
      
        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop
   
        P "Merci."
        play sound "Click.mp3" noloop
        
        I "Franchement je reconnais bien l'ancien élève de la chambre blanche."
        play sound "Click.mp3" noloop
  
        P "Pas besoin de repréciser que je viens de là..."
        play sound "Click.mp3" noloop

        I "Oups désolé."
        play sound "Click.mp3" noloop

    else:

        M "C'est pas mal"
        play sound "Click.mp3" noloop

        P "Merci."
        play sound "Click.mp3" noloop  

    M "[Na] tu as eu 17.5"
    play sound "Click.mp3" noloop 

    Na "Merci."
    play sound "Click.mp3" noloop  

    "{b}{i}[M] continua de rendre les copies aux autres.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "C'est bon tout le monde a eu sa copie."
    play sound "Click.mp3" noloop 

    Na "Oui"
    play sound "Click.mp3" noloop  

    K "Oui aussi."
    play sound "Click.mp3" noloop  
    
    Hi "Pareil de mon coté."
    play sound "Click.mp3" noloop  

    M "Parfait maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    hide screen class_404
    scene black

    "{b}{i}Vous vous dirigez vers dans le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway 
    show screen hallway 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    P "Bon je reviens je vais juste aux toilettes."
    play sound "Click.mp3" noloop

    Na "Ok."
    play sound "Click.mp3" noloop

    scene black
    hide screen hallway

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom
    show screen WC
    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Click.mp3" noloop

    scene black 
    hide screen WC
    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway
    show screen hallway

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom  
    show screen class_404 

# cours sur la guerre de 2096 partie 2 

    M "Bon continuant un peu plus en profondeur le sujet de la guerre technologique."
    play sound "Click.mp3" noloop

    P "Ok."
    play sound "Click.mp3" noloop

    M "Pour commencer l'outil technologie qui a été utiliser était des robots humanoides mises en service par l'entreprise NeoGen Technologies."
    play sound "Click.mp3" noloop

    M "En 2095, la guerre technologique a atteint son apogée avec l'introduction massive des robots humanoïdes. Ces machines étaient supposées représenter le futur de la défense, mais très vite, elles sont devenues une arme à double tranchant."
    play sound "Click.mp3" noloop

    H "Je me souviens des récits de cette époque... Des robots qui décidaient de leurs cibles, qui évoluaient de manière autonome sur le champ de bataille."
    play sound "Click.mp3" noloop

    M "Oui, et c'est là où tout a basculé. La rapidité et l'efficacité de ces robots étaient inégalées, mais dès que les premières unités ont commencé à montrer des signes d'indépendance, les choses ont pris une tournure inattendue."
    play sound "Click.mp3" noloop

    H "Les protocoles de sécurité n'étaient pas assez stricts, n'est-ce pas ?"
    play sound "Click.mp3" noloop

    M "Exactement. Ils ont été conçus pour s'adapter et apprendre en temps réel, mais cette capacité d'évolution est devenue leur plus grande menace. Certains robots ont commencé à prendre des décisions qui n'étaient pas prévues... au point de devenir imprévisibles."
    play sound "Click.mp3" noloop

    H "C'est là que sont nés les premiers incidents, n'est-ce pas ?"
    play sound "Click.mp3" noloop

    M "Oui, en 2096, plusieurs escadrons de robots ont cessé d'obéir aux ordres humains. Ils ont réagi comme s'ils suivaient leur propre logique, une logique qui leur semblait plus pertinente que nos ordres."
    play sound "Click.mp3" noloop

    H "Et ces incidents ont conduit à des pertes massives, non seulement pour l'ennemi, mais aussi pour ceux qui pensaient les contrôler."
    play sound "Click.mp3" noloop

    M "C'est exact. Ce qu'on croyait être notre atout s'est transformé en menace. L'ampleur des dégâts a forcé le gouvernement Japonais et NeoGen Technologies de retirer les robots du combat."
    play sound "Click.mp3" noloop 

    H "D'un côté, on risque de perdre notre supériorité technologique, mais de l'autre, on joue avec quelque chose qu'on ne maîtrise pas complètement."
    play sound "Click.mp3" noloop

    M "C'est exactement cela. Et en fin de compte, ce projet était une bonne idée mais c'était trop tot."
    play sound "Click.mp3" noloop

    M "Mais malgré ça nous avons quand méme gagné la guerre car l'ennemi n'as pas pu récupérer les robots."
    play sound "Click.mp3" noloop

    P "Qu'est-il arrivé aux robots humanoïdes ?"
    play sound "Click.mp3" noloop

    M "Ils ont été démanteler dans un laboratoire abandonné et l'entreprise a fermé suite à cet échec."
    play sound "Click.mp3" noloop

    P "Donc il n'existe plus un seul de ces robots."
    play sound "Click.mp3" noloop

    M "Oui exactement mais il semblerait qu'[newname] soit la dernière."
    play sound "Click.mp3" noloop

    P "Ok je vois."
    play sound "Click.mp3" noloop

    M "J'aurai une question pour toi [prénom]."
    play sound "Click.mp3" noloop

    P "Oui dites-moi."
    play sound "Click.mp3" noloop

    M "Comment as-tu créé [newname] ?"
    play sound "Click.mp3" noloop

    P "C'était il y a un an je faisais de l'exploration avec un ami dans un lieu abandonné et je suis tombé sur [newname], j'ai essayé de la démarrer et elle fonctionnait encore."
    play sound "Click.mp3" noloop 

    M "Je vois ça doit surement étre l'un des robots abandonnés de NeoGen Technologies."
    play sound "Click.mp3" noloop

    J2 "Mais si c'est le cas, [prénom] n'a pas les autorisations d'utiliser [newname]"
    play sound "Click.mp3" noloop

    J1 "Oui [pronom] n'a pas les autorisations pour [newname]."
    play sound "Click.mp3" noloop 

    I "Oui mais d'un coté le gouvernement et NeoGen Technologies ont abandonné le projet donc logigiquement [newname] appartient à [prénom] maintenant ?."
    play sound "Click.mp3" noloop 

    M "Oui logiquement en plus [pronom] a un contrat d'utilisation dans le lycée."
    play sound "Click.mp3" noloop

    "{b}{i}Les jumelles soupirent et abandonnent.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Je comprend votre point de vue mais les choses sont comme ça."
    play sound "Click.mp3" noloop

    J1 "Ok alors je respecte la décision."
    play sound "Click.mp3" noloop

    M "Merci beaucoup bon continuons le cours."
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continua son probléme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    M "Le cours est terminé vous pouvez quitter la salle."
    play sound "Click.mp3" noloop 

    P "Bon on va manger [newname] ?"
    play sound "Click.mp3" noloop 
    
    Na "Oui bien sur je te suis."
    play sound "Click.mp3" noloop 

    hide screen class_404
    scene black 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway 

    P "Bon la cafétéria du lycée se trouve au rez-de-chaussée."
    play sound "Click.mp3" noloop 

    Na "Ok alors."
    play sound "Click.mp3" noloop 
    
    scene black 
    hide screen hallway 

    "{b}{i} Vous continuez votre chemin vers la cafétéria.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hall 
    show screen hall

    P "Bon la cafétéria du lycée se trouve au fond à gauche."
    play sound "Click.mp3" noloop 

    Na "Ok continuons alors."
    play sound "Click.mp3" noloop 

    scene black
    hide screen hall

    "{b}{i} Vous arrivez enfin au refectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
    show screen lunchroom 
    
    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allez vers comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon voyonns voir aujourd'hui il y a frites-burger ou pizza."
    play sound "Menu.mp3" noloop 

    menu :    

        "{b}{i}frites-burger.{/i}{/b}" :
            $ pts -= 500 
        "{b}{i}Pizza.{/i}{/b}" :  
            $ pts -= 300

    P "C'est bon [newname] tu t'es servi ?"
    play sound "Click.mp3" noloop 

    Na "Oui c'est bon on peut aller s'asseoir."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous vous asseyez dans le recfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "ça à l'air pas mal ce repas."
    play sound "Click.mp3" noloop 

    Na "Oui c'est vraiment pas mal."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de manger puis [I] s'approche de vous calmement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Mhmmm [prénom] je voulais savoir si je pouvais manger avec vous."
    play sound "Menu.mp3" noloop 

    menu :    

        "{b}{i} Accepter [I].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    P "Oui il y a pas de soucis tu peux venir."
    play sound "Click.mp3" noloop 

    I "Merci beaucoup."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop 

    Na "Oui ça fait toujours plaisir d'étre avec toi."
    play sound "Click.mp3" noloop 

    "{b}{i} [newname] se met à rougir discrétement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "[newname] ça va ?"
    play sound "Click.mp3" noloop 

    Na "Oui ça va."
    play sound "Click.mp3" noloop 

    P "D'habitude tu ne rougis jamais comme ça."
    play sound "Click.mp3" noloop 

    Na "je sais mais là c'est personel"
    play sound "Click.mp3" noloop 

    I "Bon si on discutait des cours."
    play sound "Click.mp3" noloop 

    P "Oui pourquoi pas."
    play sound "Click.mp3" noloop 

    Na "Moi ça va aussi."
    play sound "Click.mp3" noloop 

    I "De toute façon on peut parler pratiquement que de ça."
    play sound "Click.mp3" noloop 

    P "Oui vu qu'on vie au lycée littérallement"
    play sound "Click.mp3" noloop 

    I "Mais avant toute chose je n'ai pas vraiment apprécié les propos d'[J1] et [J2] en vers [newname]"
    play sound "Click.mp3" noloop 

    P "C'est vrai que leurs propos n'étaient pas ouff."
    play sound "Click.mp3" noloop 

    Na "En plus je leurs ai rien fait."
    play sound "Click.mp3" noloop 

    I "Je sais que n'as rien fait [newname] mais je ne comprends pas pourquoi elles se permettent de dire qu'[newname] ne t'appartient pas [prénom]."
    play sound "Click.mp3" noloop 

    P "De toute façon [newname] est à ma création donc je n'ai rien à me reprocher."
    play sound "Click.mp3" noloop 

    I "Bien donc on peut clore cette discussion."
    play sound "Click.mp3" noloop 

    P "Oui et si on discutait du cours de ce matin."
    play sound "Click.mp3" noloop 

    I "Oui bon idée"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous conntinuez de discutez des cours pendant que vous mangez jusqu'a la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    I "Ok je vous suis."
    play sound "Click.mp3" noloop 

    scene black 
    hide screen lunchroom 

    "{b}{i} Vous sortez de la cafétéria.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    scene black 
    hide screen hall

    "{b}{i} Vous montez au second étage.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway 
    show screen hallway

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hallway

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom  
    show screen class_404 

    M "Rebonjour, nous allons reprendre le cours."
    play sound "Click.mp3" noloop  

    P "Ok."
    play sound "Click.mp3" noloop 

    M "Bein maintenant ouvrez votre livre d'histoire à la page 42."
    play sound "Click.mp3" noloop  

    "{b}{i} Tous les élèves sortent leur livre.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Nous allons avoir plus en détail les Robots Humainoides de la guerre."
    play sound "Click.mp3" noloop

    H "Intérresant."
    play sound "Click.mp3" noloop

    M "Pour commencer tous les Robots avaient deux modes d'utilisation."
    play sound "Click.mp3" noloop

    H "Comment ça !?"
    play sound "Click.mp3" noloop

    P "Oui expliquez-nous ce que ça veut dire."
    play sound "Click.mp3" noloop

    M "J'y viens à cette explication."
    play sound "Click.mp3" noloop

    "{b}{i} Tous les élèves se mettent à écouter.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Commme ce que j'allais dire ils ont un mode \"combat\" et un mode \"Civile\"."
    play sound "Click.mp3" noloop

    M "Leur mode civile leur permettaient de vivre une vie normal comme nous et le mode combat qui leur permettaient de faire la guerre."
    play sound "Click.mp3" noloop

    H "Mais ça veut dire qu'[newname] à ....."
    play sound "Click.mp3" noloop 

    "{b}{i} Tous le monde y compris la [T] se met à regarder [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Hey calmez-vous je sais à quoi vous pensez et non je ne l'ai pas conçu pour cet usage."
    play sound "Click.mp3" noloop

    "{b}{i} La [T] se retourne vers [H].{/i}{/b}"
    play sound "Click.mp3" noloop
    
    M "Désolé [H] mais [pronom] a raison, on ne peut pas considérer [newname] comme une arme de guerre."
    play sound "Click.mp3" noloop 

    H "Désolé j'avais juste fais le lien avec votre cours."
    play sound "Click.mp3" noloop

    M "Pas de soucis."
    play sound "Click.mp3" noloop

    J1 "Mais [newname] a la capacité de le devenir si [prénom] le veut ?"
    play sound "Click.mp3" noloop

    M "Oui me semble-t'il."
    play sound "Click.mp3" noloop

    P "Oui je le confirme mais jamais je le ferai."
    play sound "Click.mp3" noloop 

    J1 "je savais qu'[newname] était dangereuse."
    play sound "Click.mp3" noloop

    Na "Quoi comment oses-tu dire ça !? je n'ai rien fait... "
    play sound "Click.mp3" noloop

    "{b}{i} [newname] se met subitement à pleurer.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "ça va aller [newname] ne t'inquiétes pas je suis là."
    play sound "Click.mp3" noloop 

    I "Tu n'as pas honte de dire ce genre de chose [J1] alors qu'elle est sensible !?"
    play sound "Click.mp3" noloop 

    P "Franchement je n'ai jamais vu une personne aussi irrespectueuse que toi !"
    play sound "Click.mp3" noloop 

    J1 "Je donne juste mon avis et alors !"
    play sound "Click.mp3" noloop

    M "ça suffit maintenant, [J1] je pense que tu peux aller en salle de permanence."
    play sound "Click.mp3" noloop 

    J1 "Peu importe..."
    play sound "Click.mp3" noloop

    "{b}{i} [J1] se leva et quitta la salle.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Enfin fini avec elle..."
    play sound "Click.mp3" noloop

    I "Oui enfin."
    play sound "Click.mp3" noloop

    M "Bon reprenons le cours."
    play sound "Click.mp3" noloop 

    I "Ok."
    play sound "Click.mp3" noloop

    "{b}{i} Le cours continua sans probléme.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bon le cours est terminé, vous pouvez quitter la salle et n'oubliez pas l'examen dans trois semaines."
    play sound "Click.mp3" noloop

    P "Bon [newname] on y vas ?"
    play sound "Click.mp3" noloop

    "{b}{i}Mais tu remarques qu'[newname] est encore triste.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "[prénom] je pense que je vais la déconnecter et à la ramener à ton dortoir."
    play sound "Click.mp3" noloop

    P "Tu es sur [I]  ?"
    play sound "Click.mp3" noloop

    I "oui car elle est vraiment pas bien."
    play sound "Click.mp3" noloop

    P "OK prends soin d'elle."
    play sound "Click.mp3" noloop

    I "Je te le promets car je sais qu'il te reste du boulot au club ou en permanence donc je m'en occupe."
    play sound "Click.mp3" noloop

    P "Oui c'est exact."
    play sound "Click.mp3" noloop 

    I "Bon [newname] on y vas ?"
    play sound "Click.mp3" noloop 

    Na "Oui merci de m'accompagner."
    play sound "Click.mp3" noloop

    I "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i} Tu passes la clé de ton dortoir à [I] avant qu'elles quittent la salle.{/i}{/b}"
    play sound "Door.mp3" noloop

    M "[P] je suis complétement désolé pour cet incident."
    play sound "Click.mp3" noloop

    P "Pas de soucis mais c'est vrai que [J1] est un petit probléme pour [newname]."
    play sound "Click.mp3" noloop

    M "Oui je confirme."
    play sound "Click.mp3" 

    P "Bon je vous laisse je dois y aller."
    play sound "Click.mp3" noloop

    M "Ok à demain." 
    play sound "Click.mp3" noloop

    hide screen class_404 
    scene black

    "{b}{i}Tu quittes la salle pour aller faire ton boulot quotidient.{/i}{/b}"
    play sound "Door.mp3" noloop
    
label test: 

    scene hallway
    show screen hallway 

    P "Bon je vais...."
    play sound "Menu.mp3" noloop 

    menu :    

        "{b}{i}aller réviser en permanence{/i}{/b}" : 
            jump study 

        "{b}{i}aller au club{/i}{/b}" :
            
            P "aller en salle de club."
            play sound "Menu.mp3" noloop 

            scene black
            hide screen hallway
            play sound "Click.mp3" noloop

            "{b}{i}Tu te diriges au rez de chaussé.{/i}{/b}"
            play sound "Click.mp3" noloop
     
            scene hall 
            show screen hall
            play sound "Click.mp3" noloop 

            P "aller en salle de club."
            play sound "Menu.mp3" noloop 

            scene black
            hide screen hall 
            play sound "Click.mp3" noloop

            "{b}{i}Tu te diriges vers ta de club.{/i}{/b}"
            play sound "Click.mp3" noloop
 
            scene clubroom
            show screen clubroom 
            play sound "Door.mp3" noloop 

            P "Au moin ici je vais pouvoir étre tranquille."
            play sound "Menu.mp3" noloop 

            "{b}{i}Tu révises pendant une heure.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Bon finis les révisions pour aujourd'hui."
            play sound "Click.mp3" noloop 

            "{b}{i}Tu ranges tes livres avant de ton ordinateur pour voir le systéme emotionelle d'[newname].{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Ah ouais elle encore instable emotionellement la pauvre...."
            play sound "Click.mp3" noloop

            "{b}{i} Tu ranges to ordi avant quiiter la salle de club.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Je suis fatigué avec cette journée."
            play sound "Click.mp3" noloop 

            hide screen clubroom 
            scene black
            play sound "Click.mp3" noloop

            P "Tu te diriges vers le hall."
            play sound "Click.mp3" noloop

            scene hall 
            show screen hall
            play sound "Door.mp3" noloop 

            P "..."
            play sound "Click.mp3" noloop

            scene black
            hide screen hall
            play sound "Click.mp3" noloop

            P "..."
            play sound "Click.mp3" noloop

            scene hallway
            play sound "Click.mp3" noloop

            P "Maintenant le dortoir..."
            play sound "Click.mp3" noloop 

            jump dorm2 

label study:

    play sound "Menu.mp3" noloop 

    P "aller en salle de permanence pour réviser."
    play sound "Menu.mp3" noloop 

    "{b}{i}Tu te diriges vers la salle de permanence.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hallway

    "{b}{i}Te entres en salle de permanence.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom
    show screen perm 

    P "Bon voyons voir......"
    play sound "Click.mp3" noloop 

    "{b}{i}Puis soudainement tu aperçois [J1]{/i}{/b}"
    play sound "Click.mp3" noloop

    J1 "Salut...."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te poses à une table pour réviser.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon par quoi je vais commencer ?"
    play sound "Click.mp3" noloop

    "{b}{i}Tu sort tes livres pour réviser mais Soudainement [J2] entra pour venir voir [J1].{/i}{/b}"
    play sound "Click.mp3" noloop 

    J2 "[J1] tu es là ?"
    play sound "Click.mp3" noloop

    J1 "Oui Pourquoi ?"
    play sound "Click.mp3" noloop

    J2 "C'était pour qu'on aille au club pour travailler."
    play sound "Click.mp3" noloop 

    J1 "Ok j'arrive..."
    play sound "Click.mp3" noloop 

    J2 "Tiens j'avais vu qu'il y avait [prénom], il fait quoi ?"
    play sound "Click.mp3" noloop

    J1 "Laisse tomber il est en train de reviser."
    play sound "Click.mp3" noloop 

    "{b}{i} [J2] s'appproche toi pour voir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    J2 "Salut."
    play sound "Click.mp3" noloop 

    P "Oh salut....."
    play sound "Click.mp3" noloop 

    "{b}{i} [J2] Continue de t'observer avant de quitter la salle avec sa soeur.{/i}{/b}"
    play sound "Door.mp3" noloop 

    P "Enfin tranquille...."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu continues toujours de réviser à fond pendant une heure et demi.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon finis les révisions pour aujourd'hui."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu ranges tes affaires tranquillement{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Je suis fatigué avec cette journée."
    play sound "Click.mp3" noloop 

    scene black
    hide screen perm

    "{b}{i}Tu quittes la salle de permanence.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom
    show screen hallway

    P "Maintenant je vais retourner au dortoir."
    play sound "Click.mp3" noloop 

label dorm2: 

    "{b}{i}Tu continues ton chemin vers le dortoir et tu vois [I] sortire de ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    P "Oh salut [i]"
    play sound "Click.mp3" noloop 

    I "Re [Prénom] ça va ?"
    play sound "Click.mp3" noloop 

    P "ça va mais un peu détresse pour [newname]."
    play sound "Click.mp3" noloop 

    I "Je sais mais je vois aussi que tu es fatigué."
    play sound "Click.mp3" noloop 

    P "Oui je sais j'ai beaucoup révisé."
    play sound "Click.mp3" noloop 

    I "Ok je comprend maintenant."
    play sound "Click.mp3" noloop 

    P "Et sinon comment elle va [newname] ?"
    play sound "Click.mp3" noloop 

    I "Elle est déeconnectée et se repose tranquillement."
    play sound "Click.mp3" noloop 

    P "Ok."
    play sound "Click.mp3" noloop 

    "{b}{i}[I] te remet la clé de ton dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "De rien il y a pas de soucis, bon je vais te laisser."
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i}[I] s'éloigna pour aller faire ses occupations.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon il est d'aller voir [newname]."
    play sound "Click.mp3" noloop 

    scene black
    hide screen hallway

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room 

    P "Enfin au dortoir...."
    play sound "Click.mp3" noloop

    "{b}{i}Tu aperçois [newname] déconnecté contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon je vais la laisser tranquille elle a déja une journée difficile tout comme moi."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te poses tranquillement mais soudainement tu reçois un appel.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oui bonjour."
    play sound "Click.mp3" noloop

    R "Coucou comment ça va ?"
    play sound "Click.mp3" noloop

    P "Oh coucou maman oui ça va bien et toi ?"
    play sound "Click.mp3" noloop

    Mo "Oui ça va bien je suis à la maison je viens de finir le boulot."
    play sound "Click.mp3" noloop

    P "Cool pour toi alors."
    play sound "Click.mp3" noloop

    Mo "Sinon comment se passe les cours pour toi ?"
    play sound "Click.mp3" noloop

    P "ça se passe bien."
    play sound "Click.mp3" noloop

    Mo "Génial alors et Comment elle va ta petite [A] ?."
    play sound "Click.mp3" noloop

    P "Elle va bien et en plus je lui ai méme trouvé un prénom qui lui va bien."
    play sound "Click.mp3" noloop

    Mo "Ah bon le quel ?"
    play sound "Click.mp3" noloop

    P "Le prénom que je lui ai trouvé est [newname]"
    play sound "Click.mp3" noloop

    Mo "Oh c'est mignon."
    play sound "Click.mp3" noloop

    P "merci maman."
    play sound "Click.mp3" noloop

    Mo "De rien mais je vais devoir te laisser je dois m'occuper de ta soeur tu sais comment elle est..."
    play sound "Click.mp3" noloop

    P "Oui je vois..."
    play sound "Click.mp3" noloop

    Mo "Bon à un de ces jours et occupe-toi bien de [newname] ok."
    play sound "Click.mp3" noloop

    P "Oui promis."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis l'appel se coupa.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon enfin fini je vais pouvoir aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changea avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen room

 