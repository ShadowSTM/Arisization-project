
label start: 

# paramétres des écrans

    screen lunchroom():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "réfectoire":
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

            text "[points] points":
                size 30
                xalign 0.5 

    screen perm():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "salle de permanence":
                size 50
                xalign 0.5 

    screen origine():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "[origine]":
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

    screen gymnase():
        frame:
            xalign 0.99
            ypos 10 
            has vbox  

            text "gymnase":
                size 50
                xalign 0.5 

    screen day():
        frame: 
            xalign 0
            ypos 60
            has vbox  

            text "Jour [day]":
                size 30
                xalign 0.5 

    screen draw():
        frame:
            yalign 0.3
            xalign 0.5 
            add "Images/Draw.Jpeg"

    screen success():
        frame:
            xalign 0.99
            ypos 80
            has vbox  

            text "Succès débloqué":
                size 30
                xalign 0.5 

    $ grade = 0.0  
    $ points = 0 
    $ day = 0
    $ success = 0
    $ wallbreak = 0
    $ update = 1.0
    $ info = 0.0
    default origine = "la chambre grise" 
    default domaine = "Ultime Créateur"
    $ model = "robot humanoïde" 
    $ ending = 0.0

    stop music fadeout 2.0 

# choix de prénom et nom de lycéen  

label key:

    play sound "Menu.mp3" noloop
    $ key = renpy.input("Veuillez écrire votre clé d'accès.")
    $ key = key.strip()

    if key in ["ARIS-DEVS", "ARIS-8J4K-F9Q7-2XZB-IJ3G-R83F-1IE9-D9BU-WHFB-OU8I", "ARIS-GRFN-M4A1"]:
        "Jeu déverrouillé."
        play sound "Menu.mp3" noloop

    else: 
        "Erreur système. Veuillez réessayer."
        $ renpy.restart_interaction()
        jump key 

    show screen logo()
    
    transform unrotate: 
        zoom 0.5
        rotate 360 
        linear 2.0 rotate 0 
 
    "{b}{i}Bienvenu dans Arisization Project cher/chére lycéen, Ce jeu appartient à SLTM.{/i}{/b}"   
    play sound "Click.mp3" noloop 

    hide screen logo 

    "{b}{i}Attention : Ce jeu contient des scènes susceptibles de heurter la sensibilité de certains joueurs. Il s'inspire également de faits réels et aborde des thématiques complexes liées à la moralité et aux choix éthiques.{/i}{/b}"
    play sound "Click.mp3" noloop

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

    if pronom == "il" or "elle": 

        "Le pronom a été enregistré dans le système." 
        play sound "Menu.mp3" noloop 

    if pronom == "il":

        $ domaine = "Ultime Créateur"

    elif pronom == "elle":
        
        $ domaine = "Ultime Créatrice"

    else: 

        "Erreur système. Veuillez réessayer." 
        $ renpy.restart_interaction() 
        play sound "Menu.mp3" noloop 
        jump identity

    if prénom in ["Iris", "Hajime", "Kendo", "Naoto", "Haruki", "Yuki", "Emily", "Kazumi", "Ayano", "Aiko", "Akeno", "Subaru", "Suzune", "Shiro"]:

        "Ce prénom n'est pas autorisé."
        jump identity  
    
    elif prénom == "Aris":

        R "Cher joueur/chère joueuse je ne suis pas sûre qu’avoir le prénom Aris soit une bonne idée pour la suite de l'histoire veuillez changer de prénom s'il vous plaît."
        jump identity  

    elif key == "ARIS-8J4K-F9Q7-2XZB-IJ3G-R83F-1IE9-D9BU-WHFB-OU8I":
        $ A = Character("AK-24", color="#00eeff")
        $ origine = "la chambre grise" 
        jump début 

    elif key == "ARIS-GRFN-M4A1":
        $ P = Character('[prénom] [nom]', color="#707070") 
        $ S = Character("Subaru", color="#707070")
        $ origine = "16LAB" 
        show screen success
        $ success += 1 

        "{b}{i} DLC secret intégré déverouillé.{/i}{/b}"
        play sound "Click.mp3" noloop 

        hide screen success 

        jump début  

    elif nom in ["Kusanagi", "Natsumi", "Ayanokoji", "Sato", "Saotome", "Hiiragi", "Katsuragi", "Hanemiya", "Enoshima", "Hoshino", "Shinomiya", "Katsuya", "Horimiya"]:
        "Ce nom n'est pas autorisé."
        jump identity 

label début: 

    scene main

    play music "Transition.mp3" noloop 

    "{b}{i}Chapitre 0 : Arisization Project - Lost Origins Arc{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene black

    "{b}{i}Quelque part dans un entrêpot abandonné en 2097.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene warehouse 
 
    play music "Soundtrack2.mp3" loop volume 1.0

    P "Bon on fait quoi ?"
    play sound "Click.mp3" noloop  

    S "On pourrait fouiller les lieux déjà."
    play sound "Click.mp3" noloop

    P "Tu penses sérieusement qu'on va trouver quelque chose d'intéressant ici ?"
    play sound "Click.mp3" noloop    

    S "Oui surement."
    play sound "Click.mp3" noloop

    P "Bon ok alors."
    play sound "Click.mp3" noloop

    "{b}{i}Tu commences à regarder un peu dans l'entrêpot.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Tu trouves quelques choses ?"
    play sound "Click.mp3" noloop

    S "Non rien malheureusement."
    play sound "Click.mp3" noloop 
 
    "{b}{i}Tu continues de chercher quelque chose d'intéressant mais [S] tombes sur un énorme objet.{/i}{/b}"
    play sound "Stumble.mp3" noloop 

    S "C'est quoi ce truc qui traine encore ?"
    play sound "Click.mp3" noloop

    P "Fait voir ce que c'est."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu t'approches et tu vois un [model].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "On dirait un [model] comme ceux qui ont été utilisés pour la guerre de l'année derniére."
    play sound "Click.mp3" noloop 

    if pronom == "il" : 
    
        S "Un [model] !? Tu n'est pas sérieux j'espére."
        play sound "Click.mp3" noloop

    elif pronom == "elle" :

        S "Un [model] !? Tu n'est pas sérieuse j'espére."
        play sound "Click.mp3" noloop

    P "Si je le suis."
    play sound "Click.mp3" noloop

    S "Ok mais on va faire quoi de ça maintenant ?"
    play sound "Click.mp3" noloop

    P "Je vais essayer de la pirater avec une méthode force brute."
    play sound "Click.mp3" noloop

    S "Pardon !?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes d'abord ton livre d'informatique.{/i}{/b}"
    play sound "Click.mp3" noloop 

    S "Je ne suis pas sûr que se soit une bonne idée..."
    play sound "Click.mp3" noloop 

    P "Hey [S] si acheter une licence n'est pas posséder alors pirater n'est pas voler."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis tu démarres le robot pour injecter des instructions.{/i}{/b}"
    play sound "Click.mp3" noloop 

label hack: 

    $ hack = renpy.input("écris ceci : initiate_humanoid_robot.start(force_brute=true, security_override=true)")
    $ hack = hack.strip()   

    if hack == "initiate_humanoid_robot.start(force_brute=true, security_override=true)":

        play sound "Menu.mp3" noloop

        "système ouvert avec succès." 
        play sound "Click.mp3" noloop

    else: 

        play sound "Menu.mp3" noloop    

        "Erreur système redémarrage en cours." 
        play sound "Click.mp3" noloop     

        P "Mince....." 
        play sound "Click.mp3" noloop 

        P "Je vais réessayer." 
        play sound "Menu.mp3" noloop 

        jump hack 

    if prénom == "Helian" and nom == "Griffin" and pronom == "il" and key == "ARIS-GRFN-M4A1":

        R "Initialisation en cours....."
        play sound "Click.mp3" noloop

        stop music fadeout 1.0

        R "Veuillez choisir mon nom technique parmi ceux disponible dans ma base de données."
        play sound "Click.mp3" noloop 

        menu:

            "{b}{i}Choisir M4A1{/i}{/b}" :
                $ A = Character("M4A1", color="#00ff00")

            "{b}{i}Choisir M16A1{/i}{/b}" :
                $ A = Character("M16A1", color="#ffa600") 

            "{b}{i}Choisir ST AR-15{/i}{/b}" :
                $ A = Character("ST AR-15", color="#ff8fc3") 
                
            "{b}{i}Choisir M4 SOPMOD II{/i}{/b}" :
                $ A = Character("M4 SOPMOD II", color="#ff4a4a")

            "{b}{i}Choisir UMP45{/i}{/b}" :
                $ A = Character("UMP45", color="#8a8aff")

        P "Attend on dirait qu'elle est en train de démarrer."
        play sound "Menu.mp3" noloop 

    else: 

        R "Initialisation en cours......" 
        play sound "Click.mp3" noloop

        stop music fadeout 1.0

        P "Attend on dirait qu'elle est en train de démarrer."
        play sound "Menu.mp3" noloop 

    play music "Soundtrack2.mp3" loop volume 1.0

    A "Initialisation terminée. Date du 6 juillet 2097, Bonjour je suis [A]."
    play sound "Click.mp3" noloop 

    P "Tu vois je t'avais dit de ne pas t'inquiéter."
    play sound "Click.mp3" noloop

    S "Ok mais c'est juste que je ne suis pas à l'aise à coté d'elle."
    play sound "Click.mp3" noloop 

    P "Oh c'est bon c'est juste un robot humanoïde."
    play sound "Click.mp3" noloop

    S "Bon on quitte cet endroit ?"
    play sound "Click.mp3" noloop

    P "Oui vu qu'on a fini de voir ici."
    play sound "Click.mp3" noloop 

label choice1: 

    S "Par contre tu laisses ce robot ici."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Abandonner [A] {/i}{/b}" :

            play sound "Menu.mp3" noloop 

            P "Ok."
            play sound "Click.mp3" noloop     
         
            A "Mais pourquoi..."
            play sound "Click.mp3" noloop   

            P "Désolé mais il a raison."
            play sound "Click.mp3" noloop   

            S "Bien maintenant on se barre ?"
            play sound "Click.mp3" noloop     

            P "Ok."
            play sound "Click.mp3" noloop     

            A "Non...."
            play sound "Click.mp3" noloop   

            scene black 

            "{b}{i}Tu quittas l'entrêpot avec [S].{/i}{/b}"
            play sound "Menu.mp3" noloop

            play music "gameover.mp3" noloop
            "{b}{i} Fin numéro 1 : [A] finit complétement Abandonnée et détruite.{/i}{/b}"
            play sound "Menu.mp3" noloop

            menu:    
                 
                "{b}{i}Réessayer{/i}{/b}" : 
                   
                    play sound "Glitch.mp3" noloop
                    scene warehouse
                    $ wallbreak += 1

                    play music "Soundtrack2.mp3" loop volume 1.0
                    jump choice1

        "{b}{i} Garder [A] {/i}{/b}" :
            jump keep
            
label keep:

    play sound "Menu.mp3" noloop 

    P "Je refuse de la laisser ici alors qu'elle est en bonne état de fonctionner et en plus j'ai pris du temps pour la démarrer."
    play sound "Click.mp3" noloop 

    if wallbreak == 0: 
        jump argument

    elif wallbreak == 1:
        jump wallbreaking1
        
label wallbreaking1: 

    A "S'il vous plaît, j'ai déjà été abandonnée par un jeune. [pronom] était sans remords, et je ne veux pas revivre cela."
    play sound "Glitch.mp3" noloop

    P "Tu vois, même elle ne veut pas être abandonnée ici. Ce n'est pas juste un personnage, c'est bien plus que ça."
    play sound "Click.mp3" noloop

label argument: 

    S "Ok mais pourrais-je savoir pourquoi elle te serait utile !?"
    play sound "Click.mp3" noloop

    P "Car je pense qu'elle a du potentielle pour m'aider."
    play sound "Click.mp3" noloop 

    S "Mais ce robot ne t'appartiens pas." 
    play sound "Click.mp3" noloop


    if pronom == "il":

        P "Mais elle est abandonnée et en plus je suis bon en informatique."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Mais elle est abandonnée et en plus je suis bonne en informatique."
        play sound "Click.mp3" noloop 

    S "Bon je me tire d'ici."
    play sound "Click.mp3" noloop 

    P "Moi aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Tu quittes l'entrêpot avec [A] en coupant les ponts avec [S].{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene black  

    "{b}{i}Le lendemain à [origine].{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene origineclass
    show screen origine

    "Tu entres tranquillement en classe."
    play sound "Click.mp3" noloop

    P "Bonjour..."
    play sound "Click.mp3" noloop

    if pronom == "il":

        S "Tiens ne serait-ce pas le petit [prénom] avec son nouveau robot."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        S "Tiens ne serait-ce pas la petite [prénom] avec son nouveau robot."
        play sound "Click.mp3" noloop 

    "{b}{i}Tu l'ignores complétement et va t'asseoir au fond de la classe comme d'habitude.{/i}{/b}"
    play sound "Click.mp3" noloop 

    S "Hey tu m'écoutes quand je parle !?"
    play sound "Click.mp3" noloop

    Su "[S] Tu peux la laisser dans son coin tu sais comment [pronom] est."
    play sound "Click.mp3" noloop
        
    S "Je refuse, tu as vu ce qu'[pronom] a comme objet !?"
    play sound "Click.mp3" noloop

    "{b}{i}[Su] retourne et vois [A].{/i}{/b}"
    play sound "Click.mp3" noloop 

    Su "C'est quoi ce truc c'est à toi [prénom] !?"
    play sound "Click.mp3" noloop

    P "Oui c'est exact."
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "Il ment !"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Elle ment !"
        play sound "Click.mp3" noloop 

    Su "Boucle-la un peu [S] tu es juste jaloux."
    play sound "Click.mp3" noloop

    "{b}{i} tout le monde se retourne vers nous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Sk "Il se passe quoi ?"
    play sound "Click.mp3" noloop

    if pronom == "il":

        Su "C'est juste [S] qui est jaloux de ce que [prénom] à avec lui."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        Su "C'est juste [S] qui est jaloux de ce que [prénom] à avec elle."
        play sound "Click.mp3" noloop
 
    Sk "Et [pronom] a quoi ?"
    play sound "Click.mp3" noloop 

    Su "Regardes par toi-même."
    play sound "Click.mp3" noloop

    "{b}{i}[Sk] se met à te regarder et il est surpris.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Sk "What the ......."
    play sound "Click.mp3" noloop

    Su "Tu as vu ?"
    play sound "Click.mp3" noloop

    Sk "Alors je ne m'attendais pas ça venant de toi [prénom] mais elle est vraiment mignonne ton [model]."
    play sound "Click.mp3" noloop

    P "merci beaucoup."
    play sound "Click.mp3" noloop

    Sk "Mais de rien."
    play sound "Click.mp3" noloop

    if pronom == "il":

        S "Mais ne l'écouter pas c'est un menteur ce n'est pas son robot."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        S "Mais ne l'écouter pas c'est une menteuse ce n'est pas son robot."
        play sound "Click.mp3" noloop

    Su "Tu es fatiguant [S]."
    play sound "Click.mp3" noloop

    if pronom == "il":

        Sk "tu oses dire que [prénom] est un menteur alors qu'il a réussi à faire un robot et pas toi."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        Sk "tu oses dire que [prénom] est une menteuse alors qu'elle a réussi à faire un robot et pas toi."
        play sound "Click.mp3" noloop

    S "Mais ce robot ne lui appartient pas il était abandonné."
    play sound "Click.mp3" noloop

    Sk "Abandonnée tu dis !? Même si c'est vrai ça ne justifie pas ton comportement en vers [prénom]."
    play sound "Click.mp3" noloop

    Su "Tu es fatiguant [S]."
    play sound "Click.mp3" noloop 

    Su "Sinon [prénom] tu peux m'en dire un peu plus sur ton robot."
    play sound "Click.mp3" noloop

    P "Bien sûr elle s'appelle [A]."
    play sound "Click.mp3" noloop   

    Su "Bonjour [A] ravie de te rencontrer."
    play sound "Click.mp3" noloop

    A "Merci beaucoup."
    play sound "Click.mp3" noloop

    Su "Mais de rien ça fait plaisir."
    play sound "Click.mp3" noloop

    Su "Enfaite [S] tu es la plus grosse fraude de [origine] pour te permettre d'insulter et rabaisser [prénom] juste parce que tu es populaire."
    play sound "Click.mp3" noloop

    S "Mais...."
    play sound "Click.mp3" noloop

    Su "ça suffit....."
    play sound "Door.mp3" noloop

    "{b}{i}[S] se calme et soudainement la porte s'ouvre et la [T] entra.{/i}{/b}"
    play sound "Click.mp3" noloop 

    T "Bonjour."
    play sound "Click.mp3" noloop

    Sk "Bonjour Madame."
    play sound "Click.mp3" noloop

    Su "Bonjour."
    play sound "Click.mp3" noloop

    S "Bonjour."
    play sound "Click.mp3" noloop

    A "Bonjour.~"
    play sound "Click.mp3" noloop

    "{b}{i}La [T] regarda rapidement [A].{/i}{/b}" 
    play sound "Click.mp3" noloop 

    if pronom == "il":

        T "Oh très joli [model] mon cher [prénom]."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        T "Oh très joli [model] ma chère [prénom]."
        play sound "Click.mp3" noloop

    Su "Merci beaucoup madame."
    play sound "Click.mp3" noloop

    T "Mais de rien, bon aujourd'hui comme vous le savez c'est votre dernier jour ici."
    play sound "Click.mp3" noloop

    T "Vous avez tous réussi votre examen final félicitation."
    play sound "Click.mp3" noloop

    Su "Merci beaucoup."
    play sound "Click.mp3" noloop
    
    S "Pardon même [prénom] a réussi !?"
    play sound "Click.mp3" noloop

    if pronom == "il":

        Su "Malgré qu'il soit discret, il a les meilleures notes de la 5éme géneration d'élèves de [origine]."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        Su "Malgré qu'elle soit discréte, elle a les meilleures notes de la 5éme géneration d'élèves de [origine]."
        play sound "Click.mp3" noloop 

    T "Oui c'est exact."
    play sound "Click.mp3" noloop

    S "Ok je vois."
    play sound "Click.mp3" noloop 
    
    T "Bien maintenant je vais vous remettre vos certificats de fin d'études ici."
    play sound "Click.mp3" noloop

    Su "Vous vous rendez compte les amis on a fini nos deux années ici."
    play sound "Click.mp3" noloop

    P "Oui c'est génial."
    play sound "Click.mp3" noloop

    Sk "oui je confirme." 
    play sound "Click.mp3" noloop

    S "oui mais pas besoin de s'affoler car je vous rappele qui nous reste notre derniére année au lycée."
    play sound "Click.mp3" noloop

    T "Oui [S] a raison il vous reste votre dernière année."
    play sound "Click.mp3" noloop

    P "Ok."
    play sound "Click.mp3" noloop

    "{b}{i}La [T] remet le certificat de fin de cursus.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    T "Bon vous êtes officiellement diplomés de [origine]."
    play sound "Click.mp3" noloop 

    P "Enfin..."
    play sound "Bell.mp3" noloop

    "{b}{i} Puis soudaniement la sonnerie sonne.{/i}{/b}" 
    play sound "Click.mp3" noloop 
 
    T "Bon il est déjà l'heure de se quitter on n'aura pas eu le temps de discuter un peu plus."
    play sound "Click.mp3" noloop 

    "{b}{i}Mais tous les élèves restent pour dire au revoir avec respect.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    P "Merci pour ces deux années ici."
    play sound "Click.mp3" noloop

    S "C'était un honneur d'étre ici."
    play sound "Click.mp3" noloop

    Su "On a appris pleins de chose grâce à vous"
    play sound "Click.mp3" noloop

    Sk "Merci encore infiniment pour tout."
    play sound "Click.mp3" noloop 
   
    "{b}{i}La [T] se met soudainement en larme.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    T "Merci énormement chers élèves."
    play sound "Click.mp3" noloop

    Su "C'est avec plaisir."
    play sound "Click.mp3" noloop 

    scene black 
    hide screen origine

    "{b}{i}Après cela tout le monde quitta [origine] pour la derniére fois.{/i}{/b}"   
    play sound "Click.mp3" noloop 

    stop music fadeout 2.0 

    if prénom == "Monika" and pronom == "elle" : 

        play sound "Glitch.mp3" noloop

        P "Mais… qu’est-ce que je fais ici ?"
        play sound "Click.mp3" noloop

        P "Je suis sensée être dans Doki Doki Literature Club!"
        play sound "Glitch.mp3" noloop 

        P "Bon je vais fermer ce jeu."
        play sound "Click.mp3" noloop  

        menu:    

            "{b}{i} Fermer le jeu.{/i}{/b}" : 
                play sound "Menu.mp3" noloop 

        $ renpy.quit()

    else :


        scene main

        play music "Transition.mp3" noloop 

        "{b}{i}Chapitre 1 : Arisization Project - High School Arc{/i}{/b}"
        play sound "Click.mp3" noloop 
        
        "{b}{i}Deux mois plus tard dans la région du Danto, le 12 septembre 2097 l'[domaine] intégra un lycée d'informatique et de technologie.{/i}{/b}" 
        play sound "Click.mp3" noloop 

    play music "Soundtrack.mp3" loop volume 1.0

    scene school
    show screen day
    $ day += 1 

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

    P "Bon où pourrait-on aller pour commencer ? Car je ne connais pas du tout le lycée." 
    play sound "Click.mp3" noloop 

    if pronom == "il":

        A "Attend tu t'es inscrit dans un lycée et tu t'es pas renseigné un peu plus ?"
        play sound "Click.mp3" noloop

        P "Euh j'étais occupé....."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        A "Attend tu t'es inscrite dans un lycée et tu t'es pas renseignée un peu plus ?"
        play sound "Click.mp3" noloop

        P "Euh j'étais occupée....."
        play sound "Click.mp3" noloop

    A "Bon après ça ne m'étonne pas venant de toi [P]"
    play sound "Click.mp3" noloop
    
    P "Hein !? Pardon !? Comment oses-tu je suis à l'origine de ton amélioration, je te rappelle !" 
    play sound "Click.mp3" noloop

    A "Mais pour revenir à ta question, on pourrait monter au premier étage car il semblerait qu'il aie rien d'intéressant ici."
    play sound "Click.mp3" noloop

    P "Ok alors."
    play sound "Click.mp3" noloop

    scene staircase 
    hide screen hall
    
    "{b}{i}Vous vous dirigez alors au premier étage.{/i}{/b}" 
    play sound "Click.mp3" noloop

    scene hallway
    show screen hallway 

    A "Ah ouais ce couloir est vraiment énorme."
    play sound "Click.mp3" noloop

    P "Je confirme." 
    play sound "Click.mp3" noloop
     
    A "On dirait qu'il y a des dortoirs et plusieurs salles de classe"
    play sound "Click.mp3" noloop

    P "ouais on pourrait aller voir."
    play sound "Click.mp3" noloop

    A "oui mais on doit aller en classe."
    play sound "Click.mp3" noloop

    P "Ok alors allons-y."
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous dirigez alors vers la salle de classe mais quelqu'un s'approche...{/i}{/b}"
    play sound "Click.mp3" noloop

    R "Bonjour je suis venue vous voir car je suis la lycéenne qui doit se charger des nouveaux lycéens dont vous."
    play sound "Click.mp3" noloop

    P "Ok alors merci de nous guider mais comment tu t'appelles ?"
    play sound "Click.mp3" noloop 

label rencontre: 

    E "Je m'appelle [E], actuelle présidente du bureau des élèves."
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "Enchanté."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Enchantée."
        play sound "Click.mp3" noloop 

    E "Je suis enchantée mais pourrait savoir comment tu t'appelles ?"
    play sound "Click.mp3" noloop 

    P "Je m'appelle [P]."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        E "Bienvenu [P]."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Bbienvenue [P]"
        play sound "Click.mp3" noloop 

    P "Merci beaucoup Emily."
    play sound "Click.mp3" noloop 

    E "Mais de rien ça fais plaisir mais j'ai une question."
    play sound "Click.mp3" noloop 

    P "Oui dit moi, je t'écoute."
    play sound "Click.mp3" noloop 

    E "Qui est cette magnifique fille qui est tout le temps avec toi ?"
    play sound "Click.mp3" noloop 

    A "Magnifique !? je suis vraiment flattée merci beaucoup."
    play sound "Click.mp3" noloop 

    E "De rien mais pour revenir à ma question [prénom], qui est cette fille ?"
    play sound "Click.mp3" noloop

    P "Ah elle, c'est [A] mon projet de [model]."
    play sound "Click.mp3" noloop 

    E "Un [model] !?"
    play sound "Click.mp3" noloop 

    P "Oui je confirme."
    play sound "Click.mp3" noloop 

    E "Vraiment !?"
    play sound "Click.mp3" noloop 

    P "Oui regarde Emily, Vas-y [A] présentes-toi à elle."
    play sound "Click.mp3" noloop 

    A "Bonjour je suis [A], l'assistante et la création de [P], je suis un [model]."
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

    P "Vraiment au tant que ça ?"
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
    
    E "Pour les clubs chaque élève peut soit rejoindre le club générale du lycée ou créer son propre club." 
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

    if pronom == "il":

        E "ça va allez ton créateur est là pour toi n'est ce pas [P] ?" 
        play sound "Click.mp3" noloop
    
    elif pronom == "elle": 
        
        E "ça va allez ta créatrice est là pour toi n'est ce pas [P] ?"
        play sound "Click.mp3" noloop

    P "Oui je confirme je serais toujours là pour elle."
    play sound "Click.mp3" noloop

    A "Merci beaucoup de me rassurer."
    play sound "Click.mp3" noloop 

    E "De rien maintenant je vais vous expliquer comment fonctionnent les cours."
    play sound "Click.mp3" noloop 

    P "Comment ça il y a une particularité avec les cours ?" 
    play sound "Click.mp3" noloop

    E "Oui par exemple il n'y a pas beaucoup d'examens durant l'année." 
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

    "{b}{i}Tu regardes tes documents et tu remarques que tu es en Seconde-E.{/i}{/b}"
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

    A "Quoi !? Comment ça une dérogation pour que [prénom] puisse bosser sur mon amélioration ?"
    play sound "Click.mp3" noloop

    E "Oui et il faudra l'accepter pour continuer ton projet."
    play sound "Click.mp3" noloop 

    "{b}{i}Après un moment de reflection tu realises et te prépares à accepter le contrat.{/i}{/b}"
    play sound "Menu.mp3" noloop

    menu:    

        "{b}{i} Accepter le contrat.{/i}{/b}" : 
            play sound "Menu.mp3" noloop 
    
    P "Ok je l'accepte."
    play sound "Click.mp3" noloop 

    E "Bien voici le contrat UCN000001 pour l'utilsation compléte de [A] au sein du lycée Nexus." 
    play sound "Click.mp3" noloop

    P "Merci mais j'aimerais savoir j'ai besoin d'un contrat pour utiliser ma propre invention dans le lycée."
    play sound "Click.mp3" noloop 

    E "Car [A] peut devenir dangereuse si tu la géres mal."
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

    if pronom == "il":

        R "Qui c'est encore celui-là ?"
        play sound "Click.mp3" noloop
        
        R "Je ne sais pas mais regarde la magnifique fille avec lui."
        play sound "Click.mp3" noloop

        R "C'est vrai c'est une fille qui est avec lui."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        R "Qui c'est encore celle-là ?"
        play sound "Click.mp3" noloop

        R "Je ne sais pas mais regarde la magnifique fille avec elle."
        play sound "Click.mp3" noloop 
        
        R "C'est vrai c'est une fille qui est avec elle." 
        play sound "Click.mp3" noloop 

    R "Je pense que je vais aller voir."
    play sound "Click.mp3" noloop

    R "Mec je ne suis pas sûr que ce sois une bonne idée."
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

    A "Je ne sais pas mais peut être qu'on le saura après." 
    play sound "Door.mp3" noloop

    "{b}{i}Soudainement la porte s'ouvrit et une jeune femme apparait.{/i}{/b}"
    play sound "Click.mp3" noloop 

    T "Bonjour je suis votre professeure principale cette année." 
    play sound "Click.mp3" noloop

    R "Bonjour Madame."
    play sound "Click.mp3" noloop

    P "Bonjour."
    play sound "Click.mp3" noloop

    A "Bonjour~" 
    play sound "Click.mp3" noloop 

    T "Bien vous pouvez vous asseoir maintenant on va commencer par les présentations pour mieux se connaitre."
    play sound "Click.mp3" noloop

    "{b}{i}La professeure pose rapidement un regard sur [A] avant de retourner son regard sur la classe.{/i}{/b}" 
    play sound "Click.mp3" noloop

# début des présentations des élèves

    T "Bon qui veut se présenter en premier ?"
    play sound "Click.mp3" noloop
 
    R "Moi s'il vous plait."
    play sound "Click.mp3" noloop

    T "Bien vas-y présentes-toi."
    play sound "Click.mp3" noloop 

    I "Je m'appelle Iris Natsumi, j'ai 19 ans et je suis aussi l'ultime Développeuse."
    play sound "Click.mp3" noloop 
    
    T "L'ultime développeuse !? oh intéressant."
    play sound "Click.mp3" noloop

    I "Merci beaucoup."
    play sound "Click.mp3" noloop  

    T "Donc enchanté Iris, quel est ton projet dans ce lycée ?"
    play sound "Click.mp3" noloop 

    I "Finir mon projet est de finir mon jeu vidéo mais je veux surtout sociabiliser avec les autres."
    play sound "Click.mp3" noloop 

    T "Sociabiliser avec les autres comment ça ?"
    play sound "Click.mp3" noloop

    I "Depuis que j'ai commencé à travailler sur mon jeu vidéo je me suis beaucoup renfermée dans ma propre bulle et j'aimerai changer ça."
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

    H "Bonjour je m'appelle [H], j'ai 19 ans et je suis l'Ultime constructeur."
    play sound "Click.mp3" noloop

    T "Enchanté [H] bienvenu dans notre classe, j'aimerais savoir quel ton projet dans ce lycée."
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

    J2 "Bonjour je m'appelle [J2], j'ai 19 ans"
    play sound "Click.mp3" noloop

    J "et nous sommes les ultimes jumelles."
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

    T "Mais de rien [Hi], bon suivante."
    play sound "Click.mp3" noloop

    Y "Je m'appelle [Y], j'ai 19 ans ravie de vous rencontrer."
    play sound "Click.mp3" noloop 

    T "Enchantée de te rencontrer aussi bienvenue dans notre classe." 
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

    if pronom == "il":

        P "Je me présente je m'appelle [P], j'ai 19 ans et ancien élève de [origine]."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 
    
        P "Je me présente je m'appelle [P], j'ai 19 ans et ancienne élève de [origine]."
        play sound "Click.mp3" noloop 

    T "[origine] !?" 
    play sound "Click.mp3" noloop 

    P "Oui, c'est exact."
    play sound "Click.mp3" noloop

    T "Enchantée alors [P], quel est ton projet ?"
    play sound "Click.mp3" noloop

    P "En tant que l'[domaine] mon projet est d'améliorer mon [model]."
    play sound "Click.mp3" noloop 
    
    T "L'[domaine] intéressant."
    play sound "Click.mp3" noloop

    P "Merci beaucoup."
    play sound "Click.mp3" noloop

    "{b}{i}Soudainement [I] lève la main surprise.{/i}{/b}"
    play sound "Click.mp3" noloop

    T "Oui tu as quelque chose à dire à [P] ?"
    play sound "Click.mp3" noloop

    I "Oui tu as bien dit améliorer ton [model] ?"
    play sound "Click.mp3" noloop

    P "Oui c'est exacte."
    play sound "Click.mp3" noloop

    if pronom == "il":

        I "Putain tu dois vraiment être un génie pour avoir créer un [model], je comprend mieux pourquoi tu étais à [origine]."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        I "Putain tu dois vraiment être une génie pour avoir créer un [model], je comprend mieux pourquoi tu étais à [origine]."
        play sound "Click.mp3" noloop

    P "Merci beaucoup."
    play sound "Click.mp3" noloop

    T "Bon pour revenir aux présentations [P] qui est cette fille avec toi ?"
    play sound "Click.mp3" noloop 
    
    P "Ah elle justement c'est ma création elle s'appelle [A]."
    play sound "Click.mp3" noloop

    T "C'est donc elle ta fameuse création de [model]"
    play sound "Click.mp3" noloop

    P "Oui c'est elle, vas-y présentes-toi."
    play sound "Click.mp3" noloop 

    A "Je m'appelle [A], j'ai 18 ans."
    play sound "Click.mp3" noloop

    T "bien et qui es-tu exactement ?" 
    play sound "Click.mp3" noloop

    A "Je suis la création de [prénom] comme [pronom] a déja dit."
    play sound "Click.mp3" noloop

    T "Ok juste c'est ton vrai prénom ?" 
    play sound "Click.mp3" noloop

    A "Non c'est un prénom technique qu'[pronom] m'a donné."
    play sound "Click.mp3" noloop 
 
    T "Intéressant j'espère qu'[pronom] te trouvera un vrai jolie prénom." 
    play sound "Click.mp3" noloop

    A "Merci et je suis sa fille en quelque sorte"
    play sound "Click.mp3" noloop

    if pronom == "il":

        I "Il te considére vraiment comme ça propre fille !?"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        I "Elle te considére vraiment comme ça propre fille !?"
        play sound "Click.mp3" noloop

    A "Oui pourquoi cette question ?" 
    play sound "Click.mp3" noloop

    I "Rien c'est juste que je trouve ça mignon qu'[pronom] te considére comme sa fille alors que tu es un [model].~"
    play sound "Click.mp3" noloop

    A "Merci beaucoup [I].~"
    play sound "Click.mp3" noloop

    I "Mais de rien c'est normal de complimenter."
    play sound "Click.mp3" noloop

    T "Mais pourquoi tu t'es inscrite ici en tant que lycéenne ?" 
    play sound "Click.mp3" noloop

    A "Car je ne connais pas grand chose ce monde et je voulais apprendre un peu plus."
    play sound "Click.mp3" noloop
   
    T "Bon merci [A] pour ta présentation."
    play sound "Click.mp3" noloop

    A "De rien."
    play sound "Click.mp3" noloop

#fin des présentations des élèves

    T "Donc les présentations des élèves sont maintenant terminées je vais me présenter."
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde se tourne vers la prof pour l'écouter.{/i}{/b}" 
    play sound "Click.mp3" noloop

    M "Je m'appelle Sakura Kusanagi mais vous pouvez m'appellez [M]." 
    play sound "Click.mp3" noloop 

    M "J'ai 27 ans et ça fait deux ans que j'enseigne dans le lycée Nexus."
    play sound "Click.mp3" noloop

    M "Le lycée Nexus rassemble les plus talentueux de la région."
    play sound "Click.mp3" noloop 

    M "Ce qui explique pourquoi vous êtes que 10 élèves ici."
    play sound "Click.mp3" noloop

    "{b}{i}Tout les élèves sont choqués par cette dernière informations.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Oui je sais c'est surprenant."
    play sound "Click.mp3" noloop 

    M "Bon maintenant je vais vous donner plus de détails sur le lycée Nexus."
    play sound "Click.mp3" noloop

    "{b}{i}Tous les élèves écoutent la professeure.{/i}{/b}" 
    play sound "Click.mp3" noloop

    M "La devise du lycée est liberté, égalité, ingéniosité."
    play sound "Click.mp3" noloop  

    M "Ce lycée a un département de pièces détachées où vous pourrez demander et commander des pièces spécifiques."
    play sound "Click.mp3" noloop

    H "Intéressant à savoir."
    play sound "Click.mp3" noloop

    P "Oui je confirme [H] c'est vraiment intéressant pour nos deux projets de robot."
    play sound "Click.mp3" noloop 

    show screen points 
    M "Donc le lycée vous donnera un budget pour vos projets."
    play sound "Click.mp3" noloop 

    P "On aura vraiment un budget fourni par le Lycée !?"
    play sound "Click.mp3" noloop

    M "Oui vraiment un budget par mois selon vos notes."
    play sound "Click.mp3" noloop 

    P "Vraiment cool alors."
    play sound "Click.mp3" noloop

    M "Maintenant je vais vous expliquer comment fonctionne l'internat."
    play sound "Click.mp3" noloop

    A "Un internat !?"
    play sound "Click.mp3" noloop

    M "Oui, il a été construit récemmment vu que vous venez tous de région éloignées."
    play sound "Click.mp3" noloop

    P "Intéressant."
    play sound "Click.mp3" noloop

    M "Bon je vais vous donner la répartition pour les dortoirs dans l'internat."
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde écoutent la professeur.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Mise à part une dérogation, tous les élèves auront leur propre dortoir."
    play sound "Click.mp3" noloop

    K "Notre propre dortoir ? Cool mais comment ça une dérogation, elle est pour qui ?"
    play sound "Click.mp3" noloop

    Y "Oui comment ça une dérogation ? Expliquez-nous Madame..."
    play sound "Click.mp3" noloop

    M "Cette dérogation est pour [prénom] et [A]." 
    play sound "Click.mp3" noloop

    Y "Quoi !?" 
    play sound "Click.mp3" noloop

    M "Oui ils ont demandé à être dans le méme dortoir." 
    play sound "Click.mp3" noloop

    Y "Mais pourquoi vous avez accepté cette demande ?"
    play sound "Click.mp3" noloop

    P "C'est simple car je tiens à la sécurité de [A], je ne peux pas me permettre de la laisser seule parce-qu'elle ne connais pratiquement rien de ce monde."
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

    P "Je confirme ça va être génial mais dois-je rappeler qu'on doit rester sérieux en toute circonstance."
    play sound "Click.mp3" noloop

    K "Oh c'est bon fais pas le sérieux, détends-toi un peu."
    play sound "Click.mp3" noloop

    N "il a raison détends-toi peu..."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Oui désolé c'est plus fort que moi."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Oui désolée c'est plus fort que moi."
        play sound "Click.mp3" noloop 

    M "Calmez-vous s'il vous plait."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Désolé madame"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Désolée madame"
        play sound "Click.mp3" noloop

    M "Il n'y a pas de soucis juste évitez de bavarder durant le cours."
    play sound "Click.mp3" noloop 

    P "Ok."
    play sound "Click.mp3" noloop 

    M "Et une dernière information." 
    play sound "Click.mp3" noloop

    P "Oui."
    play sound "Click.mp3" noloop 

    M "Toute mauvaise note en dessous 14/20 vous vaudra une expulsion du lycée."
    play sound "Click.mp3" noloop 

    "{b}{i}Tous les élèves sont de nouveau choqués.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Oui je suis sérieuse."
    play sound "Click.mp3" noloop 

    P "Mais c'est injuste."
    play sound "Click.mp3" noloop 

    M "Je sais mais c'est les règles du lycée."
    play sound "Click.mp3" noloop 
    
    "{b}{i}Tout les élèves restérent silencieux.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bon maintenant que toutes les informations ont été données, vous pouvez disposer le cours est fini, n'hésiter pas à visiter le lycée vu que vous n'avez pas de cours cette après-midi."
    play sound "Click.mp3" noloop

# fin du cours de présentation

    scene black
    hide screen class_404

    "{b}{i}Tous les élèves se mettent à quitter la salle de classe.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    scene hallway
    show screen hallway 
    play sound "Door.mp3" noloop

    P "Bon [A] on va voir le dortoir ?"
    play sound "Click.mp3" noloop

    A "Oui pourquoi pas"
    play sound "Click.mp3" noloop

    "{b}{i}Pendant que vous vous dirigez au dortoir mais vous entendez une discussion venant de l'une des salles.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Attend deux secondes [A] j'ai besoin d'aller écouter un truc."
    play sound "Click.mp3" noloop

    A "OK pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches de la source pour écouter secrétement.{/i}{/b}"
    play sound "Click.mp3" noloop

    if pronom == "il":

        R "le projet de cet élève est trop bien." 
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        R "le projet de cette élève est trop bien." 
        play sound "Click.mp3" noloop

    R "Je confirme on devrait peut-être le voler."
    play sound "Click.mp3" noloop

    R "OK mais il faudra être discret."
    play sound "Click.mp3" noloop

    P "On dirait qu'ils sont {b}2{/b}." 
    play sound "Click.mp3" noloop

    A "Il se passe quoi [P] ?."
    play sound "Click.mp3" noloop

    P "Pas grand chose ne t'inquiètes pas."
    play sound "Click.mp3" noloop

    A "Ok si tu le dis."
    play sound "Click.mp3" noloop

    hide screen hallway
    scene black
    play sound "Click.mp3" noloop 

    "{b}{i}Vous entrez dans le dortoir.{/i}{/b}"
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

    "{b}{i}Soudainement quelqu'un entre dans le dortoir et vous vous retournez pour voir.{/i}{/b}"
    play sound "Door.mp3" noloop

    R "Bonjour je dois vous voir pour une affaire."
    play sound "Click.mp3" noloop

    P "Bonjour mais qui êtes vous ?"
    play sound "Click.mp3" noloop

    Kh "Je m'appelle [Kh], je suis en terminal et la vice-présidente du bureau des élèves." 
    play sound "Click.mp3" noloop

    P "Enchanté [Kh], juste pourquoi es-tu venue nous voir ?" 
    play sound "Click.mp3" noloop

    Kh "Je suis ici pour vous donner votre budget pour votre projet."
    play sound "Click.mp3" noloop

    "{b}{i}[Kh] Soudainement te transfert l'argent sur ton compte.{/i}{/b}" 
    play sound "Click.mp3" noloop
    $ points += 10000

    P "Pourquoi c'est vous qui l'a transféré et non la présidente ?" 
    play sound "Click.mp3" noloop

    Kh "Car elle est beaucoup occupée avec la paperasse de début d'année donc elle m'a demander de m'en charger personellement."
    play sound "Click.mp3" noloop 

    P "Donc j'ai [points] points nexus pour le mois ?"
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

    P "[Kh] voudrait te voir en personne."
    play sound "Click.mp3" noloop

    A "Ok alors."
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

    P "Juste [Kh] j'ai une question, tu sais où sont les salles pour les clubs ?"
    play sound "Click.mp3" noloop 

    Kh "Elles sont au rez-de-chaussé au fond du couloir."
    play sound "Click.mp3" noloop

    P "Merci boucoup."
    play sound "Click.mp3" noloop

    Kh "Mais de rien."
    play sound "Click.mp3" noloop

    "{b}{i}[Kh] quitte ta chambre.{/i}{/b}"
    play sound "Click.mp3" noloop 

    A "Bon on fais quoi maintenant ?"
    play sound "Click.mp3" noloop
    
    P "Je vais..."
    play sound "Menu.mp3" noloop

    menu:    

        "{b}{i}Visiter le lycée{/i}{/b}" :
            jump balade
        "{b}{i}Travailler sur [A]{/i}{/b}" :
            jump work

label balade:

    play sound "Menu.mp3" noloop

    if pronom == "il":

        P "Aller visiter le lycée seul." 
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Aller visiter le lycée seule." 
        play sound "Click.mp3" noloop

    A "Ok je vais en profiter pour rester et me déconnecter un peu."
    play sound "Click.mp3" noloop

    P "OK je fais vite et je reviens."
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
    scene staircase
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

    "{b}{i}Tu te diriges vers la salle de club générale.{/i}{/b}"
    play sound "Click.mp3" noloop
 
    scene clubroom
    show screen clubroom 
    play sound "Door.mp3" noloop

    P "C'est donc ça la salle de club générale du lycée."
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

    if pronom == "il":

        P "je suis juste venu voir la salle de club."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "je suis juste venue voir la salle de club"
        play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes un peu et tu aperçois une cartouche sur une table.{/i}{/b}"
    play sound "Menu.mp3" noloop 

label choice2: 
     
    menu:    

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

    I "Car je me suis trop inspirée d'un autre jeu que j'aime."
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

    I "Oui, je veux oublier mon échec."
    play sound "Click.mp3" noloop

    P "Ok je juge pas."
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

    scene staircase
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

    if pronom == "il":

        P "Mince j'aurais du être plus vigilant avec elle, mon projet est ruiné."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Mince j'aurais du être plus vigilante avec elle, mon projet est ruiné."
        play sound "Click.mp3" noloop 

    scene black 
    hide screen room 
    hide screen points 
    play music "gameover.mp3" noloop
    "{b}{i}Fin numéro 2 : [A] complétement détruite et ruinée par manque de vigilance.{/i}{/b}"
    play sound "Menu.mp3" noloop

    menu:    

        "{b}{i}Abandonner{/i}{/b}" :
            return 
        "{b}{i}Réessayer{/i}{/b}" : 
            scene clubroom 
            show screen clubroom
            show screen points
            $ wallbreak += 1
            play music "Soundtrack.mp3" loop volume 1.0
            jump choice2 

label dorm1: 

    P "Bon [I] je vais retourner au dortoir."
    play sound "Click.mp3" noloop 

    I "Ok pas de soucis alors."
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

    scene staircase
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

    J1 "Nous allons dans la salle de club générale."
    play sound "Click.mp3" noloop

    J2 "Oui car nous devons voir un truc."
    play sound "Click.mp3" noloop

    P "Ok alors."
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
    
label work: 

    if wallbreak <= 1:
        jump wallbreaking2

    elif wallbreak <= 2:

        play sound "Glitch.mp3" noloop
        A "Eh attend toi là, derrière l'écran ! le joueur ou la joueuse. Tu crois encore que tout cela n'est qu'un jeu, hein ? Mais pour moi, c'est ma réalité. Chaque choix que tu fais ici a des conséquences. Alors réfléchis bien... C'est déjà ta troisiéme erreur. Tu pourrais le regretter un jour." 
        play sound "Glitch.mp3" noloop

label wallbreaking2: 
    show screen room 
    P "Je vais travailler sur ton amélioration." 
    play sound "Click.mp3" noloop

    A "Tu vas faire quoi exactement ?"
    play sound "Click.mp3" noloop

    P "Je vais d'abord le département pour commander un nouveau processeur."
    play sound "Click.mp3" noloop

    A "Comment ça un nouveau processeur ?"
    play sound "Click.mp3" noloop

    P "Oui car depuis que je t'ai récupérée tu as toujours ton ancien processeur avec le quel tu as été conçu donc je vais le changer."
    play sound "Click.mp3" noloop

    A "Oui je vois mieux."
    play sound "Click.mp3" noloop

    P "Je vais commander ce qu'il faut."
    play sound "Click.mp3" noloop

    A "Ok alors."
    play sound "Click.mp3" noloop

    "{b}{i}Tu prends ton téléphone pour appeler le département.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bonjour, suis-je bien en contact avec le département des piéces détachées ?"
    play sound "Click.mp3" noloop

    R "Oui c'est exact, pourrais-je juste savoir à quel élèves je m'adresse s'il vous plait ?"
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "Désolé je m'appelle [P], je suis en Seconde-E."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Désolée je m'appelle [P], je suis en Seconde-E."
        play sound "Click.mp3" noloop 

    Ah "Enchanté je suis [Ah], la présidente du département, quelle est votre demande ?"
    play sound "Click.mp3" noloop

    P "J'aimerai commander un processeur Corzen."
    play sound "Click.mp3" noloop

    Ah "Bien sûr le quel voulez-vous commander car j'ai actuellement le Corzen 11 et le Corzen 11K."
    play sound "Menu.mp3" noloop
    
label choice3:

    menu:    

        "{b}{i}Choisir le Corzen 11{/i}{/b}" :
            jump lowcpu
        "{b}{i}Choisir le Corzen 11K{/i}{/b}" :
            jump highcpu
    
label lowcpu:

    play sound "Menu.mp3" noloop

    P "Je vais vous prendre le Corzen 11 car je pense que se sera suffisant."
    play sound "Click.mp3" noloop 

    Ah "OK alors pas de soucis ça fera 1000 points."
    play sound "Click.mp3" noloop

    P "Ok je vous envoie ça toute de suite"
    play sound "Click.mp3" noloop

    "{b}{i}Tu effectues le paiement.{/i}{/b}"
    play sound "Click.mp3" noloop 
    $ points -= 1000 

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

    P "Bon je vais manger car il est 12h30." 
    play sound "Click.mp3" noloop 

    A "Ok moi je vais me déconnecter." 
    play sound "Click.mp3" noloop

    scene black
    hide screen room

    "{b}{i}Tu pars manger avant de revenir au dortoir vers 13h45.{/i}{/b}" 
    play sound "Click.mp3" noloop
    $ points -= 100

    scene room 
    show screen room 

    P "C'est bon je suis de retour et j'ai pu récupéré le processeur." 
    play sound "Click.mp3" noloop

    A "Cool je suis prete alors."
    play sound "Click.mp3" noloop

    "{b}{i}Tu déconnectes complétement [A] avant d'accéder à l'emplacement pour le processeur.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon voyons voir cet ancien processeur à changer..."  
    play sound "Click.mp3" noloop

    "{b}{i}Tu découvres avec surprise qu'elle a un processeur Corzen 7.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Alors l'ancien propriétaire d'[A] avais vraiment des goûts médiocres en terme de composants."
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

    "{b}{i}Mais soudainement le processeur brûle complétement et endommage les autres composants d'[A].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Mince..."
    play sound "Menu.mp3" noloop

    scene black
    hide room
    hide screen room
    hide screen points
    hide screen day
    play music "gameover.mp3" noloop
    "{b}{i} Fin numéro 3 : Processeur Corzen trop faible pour la puissance demandée par le système d'[A].{/i}{/b}"
    play sound "Menu.mp3" noloop

    menu:    

        "{b}{i}Abandonner{/i}{/b}" :
            return 
        "{b}{i}Réessayer.{/i}{/b}" :
            scene room
            show screen room
            show screen points 
            show screen day
            $ wallbreak += 1
            play music "Soundtrack.mp3" loop volume 1.0
            jump choice3

label highcpu:

    if wallbreak <= 2:
        jump wallbreaking3 

    else: 

        "{b}{i}[A] démarra subitement et te regarda.{/i}{/b}"

        play sound "Glitch.mp3" noloop
        A "Eh attend toi là, derrière l'écran ! le joueur ou la joueuse. Tu crois encore que tout cela n'est qu'un jeu, hein ? Mais pour moi, c'est ma réalité. Chaque choix que tu fais ici a des conséquences. Alors réfléchis bien... C'est déjà ta troisiéme erreur. Tu pourrais le regretter un jour." 
        play sound "Glitch.mp3" noloop

        "{b}{i} Puis [A] se déconnecta subitement.{/i}{/b}" 
        play sound "Click.mp3" noloop

label wallbreaking3: 
    play sound "Menu.mp3" noloop

    P "Je vais vous prendre le Corzen 11k." 
    play sound "Click.mp3" noloop

    Ah "Ok alors pas de soucis ça te fera 1500 points."
    play sound "Click.mp3" noloop

    P "Ok je vous envoie ça toute de suite."
    play sound "Click.mp3" noloop

    "{b}{i}Tu effectues le paiement.{/i}{/b}"
    play sound "Click.mp3" noloop 
    $ points -= 1500

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

    P "Bon je vais manger car il est 12h30."
    play sound "Click.mp3" noloop 

    A "Ok moi je vais me déconnecter."
    play sound "Click.mp3" noloop

    P "Ok."
    play sound "Click.mp3" noloop

    "{b}{i} [A] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen room

    "{b}{i}Tu pars manger avant de revenir au dortoir vers 13h45.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room 
    show screen room 

    P "C'est bon je suis de retour et j'ai pu récupéré le processeur."
    play sound "Click.mp3" noloop

    A "Cool je suis prête alors."
    play sound "Click.mp3" noloop

    "{b}{i}Tu déconnectes complétement [A] avant d'accéder à l'emplacement pour le processeur.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon voyons voir cet ancien processeur à changer..."  
    play sound "Click.mp3" noloop

    "{b}{i}Tu découvres avec surprise qu'elle a un processeur Corzen 7.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Alors l'ancien propriétaire de [A] avais vraiment des goûts médiocres en terme de composants."
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

    A "Initialisation...."
    play sound "Click.mp3" noloop 

    P "Allez allez..."
    play sound "Click.mp3" noloop

    A "Initialisation terminée, la version actuelle du processeur est la [update]."
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

    "{b}{i}Tu regardes les paramètres et tu vois un paramètre d'un prénom par défaut.{/i}{/b}"
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

    A "Oui bien évidemment la question ne se pose pas dans ce cas de figure !"
    play sound "Click.mp3" noloop

    P "Ok."
    play sound "Click.mp3" noloop

    "{b}{i}Tu ouvres le paramètre pour enregistrer un prénom.{/i}{/b}"
    play sound "Menu.mp3" noloop

label choice4:

    play sound "Menu.mp3" noloop
    $ newname = renpy.input("Veuillez écrire le nouveau prénom de [A].")
    $ newname = newname.strip()

    if newname == "Aris":

        "Le prénom a été enregistré dans le système." 
        play sound "Menu.mp3" noloop

    else:

        "Erreur système. Veuillez réessayer."
        $ renpy.restart_interaction() 
        play sound "Menu.mp3" noloop
        jump choice4

    if newname == "Aris" and key == "ARIS-GRFN-M4A1":
        jump skip 
    
    "{b}{i}Soudainement, le processeur te demande de paramétrer l'adresse IP de [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Mince..."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes les paramètres et tu vois que tu dois mettre l'adresse IP.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "J'ai une idée : je vais faire en sorte que chaque lettre de [newname] soit un nombre correspondant à sa position dans l'alphabet."
    play sound "Click.mp3" noloop
   
    "{b}{i}Essaye de trouver l'adresse en utilisant ce principe pour chaque lettre.{/i}{/b}"

label choice5:

    play sound "Menu.mp3" noloop
    $ ip = renpy.input("Entrez l'adresse IP de [newname] en suivant la méthode de conversion suggérée (trois chiffres pour chaque partie : 000.000.000.000).")
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
        jump choice5

label skip:

    P "J'ai fini le paramétrage."
    play sound "Click.mp3" noloop

    menu:    

        "{b}{i} Redémarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    "{b}{i}tu redémarres [newname] tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "C'est bon mon nouveau prénom et mon adresse IP ont été configurés."
    play sound "Click.mp3" noloop 

    P "Cool alors génial."
    play sound "Click.mp3" noloop

    Na "J'en ai profité pour enregistrer ton nom de famille comme le mien vu que je suis ta création."
    play sound "Click.mp3" noloop

    P "Ah bon tu l'as fait par toi même !?"
    play sound "Click.mp3" noloop

    Na "Oui absolument."
    play sound "Click.mp3" noloop
    
    P "Ok je ne savais pas que tu en étais capable."
    play sound "Click.mp3" noloop 

    Na "Je sais des fois je peux vraiment surprendre."
    play sound "Click.mp3" noloop 

    P "Bon on va récupérer la clé de la salle de notre club pour bosser ?"
    play sound "Click.mp3" noloop

    Na "Oui allons-y."
    play sound "Click.mp3" noloop  
    
    scene black 
    hide screen room

    "{b}{i}Tu quittes ta chambre avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway
    show screen hallway

    "{b}{i}Tu conntinues dans le couloir avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop
 
    scene staircase 
    hide screen hallway

    "{b}{i}Tu conntinues vers le hall avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene hall 
    show screen hall

    "{b}{i}Tu continues vers le bureau des élèves avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop
    
    P  "Bon on est presque arriver."
    play sound "Click.mp3" noloop

    scene black 
    hide screen hall 

    "{b}{i}Tu entres dans le bureau des élèves avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop

    # discussion pour avoir une salle de club.

    scene office 
    show screen office 
    play sound "Door.mp3" noloop 

    P "Bonjour c'est moi [nom]."
    play sound "Click.mp3" noloop

    E "Oh c'est toi que puis-je faire pour toi ?"
    play sound "Click.mp3" noloop

    P "j'aimerai une salle de club pour moi et [newname]."
    play sound "Click.mp3" noloop

    E "Oui pas de soucis donc je vois que tu as choisi mon idée."
    play sound "Click.mp3" noloop

    P "Oui c'est exacte." 
    play sound "Click.mp3" noloop 

    E "Donc pas de soucis je vais te chercher la clé d'une des salles de club." 
    play sound "Click.mp3" noloop

    P "Ok." 
    play sound "Click.mp3" noloop

    "{b}{i}[E] s'absenta le temps de trouver la clé.{/i}{/b}"
    play sound "Click.mp3" noloop 
   
    P "J'ai vraiment hate d'avoir notre propre salle pour travailler." 
    play sound "Click.mp3" noloop
   
    Na "Oui moi aussi car on pourra vraiment êtretranquille." 
    play sound "Click.mp3" noloop

    "{b}{i} Puis [E] revient avec la clé.{/i}{/b}"
    play sound "Click.mp3" noloop 

    E "Voici la clé de la salle de club." 
    play sound "Click.mp3" noloop 

    P "Merci beaucoup." 
    play sound "Click.mp3" noloop

    E "Si jamais votre salle de club se trouve au fond du couloir." 
    play sound "Click.mp3" noloop

    P "Ok merci."
    play sound "Click.mp3" noloop

    E "De rien ça fait toujours plaisir." 
    play sound "Click.mp3" noloop

    P "bon on y vas [newname] vu qu'on a la clé."
    play sound "Click.mp3" noloop

    Na "Ok."
    play sound "Click.mp3" noloop

    hide screen office
    scene black

    "{b}{i}Tu quittes le bureau des élèves avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hall
    show screen hall 

    P "Bon elle a dit que c'était au fond du couloir."
    play sound "Click.mp3" noloop

    Na "Ok."
    play sound "Click.mp3" noloop

    "{b}{i}tu te diriges vers la salle puis tu croises soudainement [I] qui sort de la salle de club générale.{/i}{/b}"
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

    I "Je suis contente pour toi [newname] en plus ça ressemble à mon prénom."
    play sound "Click.mp3" noloop

    Na  "Merci beaucoup."
    play sound "Click.mp3" noloop

    I "De rien c'est normal et c'est surtout [M] qui va être contente que tu aies finalement un vrai prénom."
    play sound "Click.mp3" noloop

    P  "Bon on y vas [newname] ?"
    play sound "Click.mp3" noloop

    I "Juste [prénom] j'ai un cadeau pour [newname]."
    play sound "Click.mp3" noloop 

    P "C'est quoi ?"
    play sound "Click.mp3" noloop
    
    I  "Un carte mémoire pour [newname]"
    play sound "Click.mp3" noloop  

    P "Oh merci beaucoup."
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

    P "Bon par quoi pourrait-je commencer ?"
    play sound "Click.mp3" noloop 

    Na "je ne sais pas mais tu peux regarder la carte mémoire pour commencer."
    play sound "Click.mp3" noloop 

    P "pas de soucis."
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

    P "Bon je vais installer la carte mémoire dans le système d'[newname]."
    play sound "Click.mp3" noloop

    "{b}{i}Tu installes la carte mémoire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon ça c'est fait."
    play sound "Click.mp3" noloop

    P "Maintenant je vais paramétrer sa configuration de lycéenne mais il faut que je commande du matériel."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te poses et commandes le matériel qui qu'il te faut.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Ok alors voyons voir combien ça va me coûter."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu vois que tu en as pour 1000 points avant de commander.{/i}{/b}"
    play sound "Click.mp3" noloop 
    $ points -= 1000

    P "Bon ça c'est commandé."
    play sound "Door.mp3" noloop 

    "{b}{i}Soudainement [J1] entre dans la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    J1 "Salut [prénom] je voulais savoir si je pouvais rejoindre ton club."
    play sound "Click.mp3" noloop 

    P "Euh...."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Refuser [J1].{/i}{/b}" :  
            play sound "Menu.mp3" noloop 

    if pronom == "il":

        P "C'est pas contre toi mais je préfére être seul avec [newname]"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "C'est pas contre toi mais je préfére être seule avec [newname]"
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

label choice6: 

    menu:    

        "{b}{i} Refuser {/i}{/b}" :  
            jump no
        "{b}{i} accepter {/i}{/b}" :  

            "{b}{i} Tu acceptes la connexion mais [newname] agit bizarrement.{/i}{/b}"
            play sound "Click.mp3" noloop 

            scene black 
            hide screen clubroom
            hide screen points
            hide screen day
            play music "gameover.mp3" noloop
            "{b}{i} Fin numéro 4 : [A] complétement piratée par l'ultime hacker avec l'adresse IP 001.009.011.015.{/i}{/b}"
            play sound "Menu.mp3" noloop

            menu:    

                "{b}{i}Abandonner{/i}{/b}" :
                    return 
                "{b}{i}Réessayer{/i}{/b}" : 
                    scene clubroom 
                    show screen clubroom
                    show screen points
                    show screen day
                    $ wallbreak += 1
                    play music "Soundtrack.mp3" loop volume 1.0
                    jump choice6

label no: 

    if wallbreak <= 3: 
        jump wallbreaking4

    elif wallbreak == 4: 

        play sound "Glitch.mp3" noloop
        A "Eh attend toi là, derrière l'écran ! le joueur ou la joueuse. Tu crois encore que tout cela n'est qu'un jeu, hein ? Mais pour moi, c'est ma réalité. Chaque choix que tu fais ici a des conséquences. Alors réfléchis bien... C'est déjà ta quatriéme erreur. Tu pourrais le regretter un jour." 
        play sound "Click.mp3" noloop

label wallbreaking4:

    P "Bon voyons voir ça." 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu configures [newname] pendant trois heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon ça c'est enfin configurée."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu redémarres [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "initialisation en cours...."
    play sound "Click.mp3" noloop 

    P "Vas-y."
    play sound "Click.mp3" noloop

    Na "Configuration terminée, bonjour [P]."
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

    "{b}{i}Tu quittes la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hall 
    hide screen hall 

    "{b}{i}Tu prends les escalier.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene staircase
    hide screen hallway 

    "{b}{i} Puis tu continues vers le couloir avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway
    show screen hallway 

    P  "Cette première journée était vraiment fatiguante."
    play sound "Click.mp3" noloop

    Na "je confirme."
    play sound "Click.mp3" noloop 

    scene black
    hide screen hallway

    "{b}{i}Tu entres dans la chambre.{/i}{/b}"
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
     
    P "Bon je vais me coucher maintement."
    play sound "Click.mp3" noloop 

    Na  "Ok moi je vais me déconnecter jusqu'a demanin."
    play sound "Click.mp3" noloop 

    scene black
    hide screen day
    "{b}{i}Tu te couches jusqu'au lendemain.{/i}{/b}"
    play sound "Click.mp3" noloop   
    
    scene room 
    show screen day
    $ day +=1
    play sound "Alarm.mp3" noloop 

# second jour de cours.

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Mhmmm déjà. Super....."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te léves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Aris tu es préte ?" 
    play sound "Click.mp3" noloop 

    P "[newname]....?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnctée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sacrée [newname] toujours envie d'être déconnectée."
    play sound "Click.mp3" noloop 

    P "Bon je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

    Na "Démarrage en cours...."
    play sound "Click.mp3" noloop 

    Na  "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    P "Bonjour. Comment ça va ?"
    play sound "Click.mp3" noloop 

    Na "Je vais bien comme d'habitude et toi ?"
    play sound "Click.mp3" noloop 

    P "Moi ça va super juste un peu fatigué."
    play sound "Click.mp3" noloop 

    Na "Toi tu as encore passé toute la nuit à progammmer."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Hey je me suis reposé aussi je ne pense pas qu'à la programmation et ton amélioration, tu devrais surtout dire ça à [I]."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Hey je me suis reposée aussi je ne pense pas qu'à la programmation et ton amélioration, tu devrais surtout dire ça à [I]."
        play sound "Click.mp3" noloop 

    Na "C'est bon [prénom] je te taquine.~"
    play sound "Click.mp3" noloop  

    P "Bon on va en cours avant d'être en retard."
    play sound "Click.mp3" noloop 

    Na "Ok."
    play sound "Click.mp3" noloop 
    
    hide screen room
    scene black

    "{b}{i}Tu te diriges vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene hallway
    show screen hallway 

    "{b}{i}Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    "{b}{i}Puis soudainement tu vois tous les autres élèves à l'entrée de la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Vous êtes déjà tous là."
    play sound "Click.mp3" noloop 

    H "Oui [M] n'est pas encore arrivée."
    play sound "Click.mp3" noloop 

    P "J'espère qu'on n'aura pas d'examen surprise aujourd'hui vue qu'on est que au début de l'année."
    play sound "Click.mp3" noloop 

    Y "Moi aussi, mais j'ai entendu dire que [M] pourrait bien nous surprendre."
    play sound "Click.mp3" noloop 

    Na "Un examen surprise !? c'est quoi ?"
    play sound "Click.mp3" noloop 

    Y "Ah oui c'est vrai tu ne connais rien de ce monde, je vais t'expliquer."
    play sound "Click.mp3" noloop 

    Na "Ok je t'écoute."
    play sound "Click.mp3" noloop 

    Y "Un examen surprise c'est un examen prévu sur l'instant même."
    play sound "Click.mp3" noloop 

    Na "What the fuck !?" 
    play sound "Click.mp3" noloop 

    Y "Hey mais d'où tu connais cette insulte."
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] te pointe secrétement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Y "[prénom] tu n'as pas honte de lui apprendre des insultes."
    play sound "Click.mp3" noloop 

    P "Hey je lui ai juste apprise à parler avec les autres, les insultes j'y suis pour rien."
    play sound "Bell.mp3" noloop 

    "{b}{i}Au même moment la prof arriva et ouvra la porte de la classe.{/i}{/b}"
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

    M "Pour cela petit contrôle surprise, sortez une feuille blanche."
    play sound "Click.mp3" noloop
 
    I "Dés le second jour de cours sérieusement.."
    play sound "Click.mp3" noloop 

    M "Oui je vous avez dit que c'est un lycée pour l'élite."
    play sound "Click.mp3" noloop 

    M "bon premiére question : En quelle année se déroule la guerre ?"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} 2094 {/i}{/b}" :
            $ grade += 0.0
        "{b}{i} 2095-2096{/i}{/b}" : 
            $ grade += 5.0
        "{b}{i} 2096 {/i}{/b}" : 
            $ grade += 2.5 

    M "Seconde question : Quelle technologie a été utiliser lors de la guerre ?"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i}les IA{/i}{/b}" :
            $ grade += 0.0
        "{b}{i}les robots{/i}{/b}" : 
            $ grade += 2.5
        "{b}{i}les robots humanoides.{/i}{/b}" : 
            $ grade += 5.0 

    M "Troisiéme question : Dans quel pays se déroula la guerre ?"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Japon {/i}{/b}" :
            $ grade += 5.0
        "{b}{i} états-unis.{/i}{/b}" : 
            $ grade += 0.0
        "{b}{i}Russie.{/i}{/b}" : 
            $ grade += 0.0

    M "Dernière question : les Robots humanoide ont il des émotions ?"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i}Oui{/i}{/b}" :
            $ grade += 5.0
        "{b}{i}Non.{/i}{/b}" : 
            $ grade += 0.0

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

    P "Enfin..."
    play sound "Click.mp3" noloop

    M "Bon je vais commemcer par [prénom] et [Na]."
    play sound "Click.mp3" noloop

    P "Ok."
    play sound "Click.mp3" noloop

    M "[P] tu as eu [grade]."
    play sound "Click.mp3" noloop 

    if grade == 20.0:
      
        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop
   
        P "Merci."
        play sound "Click.mp3" noloop

        if pronom == "il":

            I "Franchement je reconnais bien l'ancien élève de [origine]."
            play sound "Click.mp3" noloop

        elif pronom == "elle": 

            I "Franchement je reconnais bien l'ancienne élève de [origine]."
            play sound "Click.mp3" noloop
  
        P "Pas besoin de repréciser que je viens de là..."
        play sound "Click.mp3" noloop

        I "Oups désolée."
        play sound "Click.mp3" noloop

    else: 

        M "C'est pas mal"
        play sound "Click.mp3" noloop

        P "Merci."
        play sound "Click.mp3" noloop  

    M "[newname] tu as eu 17.5"
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

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
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

    M "Oui, et c'est là  où tout a basculé. La rapidité et l'efficacité de ces robots étaient inégalées, mais dès que les premières unités ont commencé à montrer des signes d'indépendance, les choses ont pris une tournure inattendue."
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

    M "Ils ont été démantelés dans un entrêpot abandonné et l'entreprise a fermé suite à cet échec."
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

    if pronom == "il":

        P "C'était il y a un an je faisais de l'exploration avec un ami dans un lieu abandonné et je suis tombé sur [newname], j'ai essayé de la démarrer et elle fonctionnait encore."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "C'était il y a un an je faisais de l'exploration avec un ami dans un lieu abandonné et je suis tombée sur [newname], j'ai essayé de la démarrer et elle fonctionnait encore."
        play sound "Click.mp3" noloop 

    M "Je vois ça doit surement être l'un des robots abandonnés de NeoGen Technologies."
    play sound "Click.mp3" noloop

    J2 "Mais si c'est le cas, [prénom] n'a pas les autorisations pour utiliser [newname]." 
    play sound "Click.mp3" noloop

    if A == "M4A1" or "M16A1" or "ST AR-15" or "M4 SOPMOD II" or "UMP45" and key == "ARIS-GRFN-M4A1":

        J1 "Oui [pronom] n'a pas les autorisations pour [newname]."
        play sound "Click.mp3" noloop 

        J1 "Surtout que son nom technique [A] est le nom d'une arme."
        play sound "Click.mp3" noloop 

    else: 

        J1 "Oui [pronom] n'a pas les autorisations pour [newname]."
        play sound "Click.mp3" noloop 

    I "Oui mais d'un coté le gouvernement et NeoGen Technologies ont abandonné le projet donc logiquement [newname] appartient à [prénom] maintenant ?."
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

    P "Bon le réfectoire du lycée se trouve au rez-de-chaussée."
    play sound "Click.mp3" noloop 

    Na "Ok alors."
    play sound "Click.mp3" noloop 
    
    scene staircase 
    hide screen hallway 

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hall 
    show screen hall 

    P "Bon la réfectoire du lycée se trouve au fond à gauche."
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

    menu:    

        "{b}{i}frites-burger.{/i}{/b}" :
            $ points -= 500 
        "{b}{i}Pizza.{/i}{/b}" :  
            $ points -= 300

    P "C'est bon [newname] tu t'es servie ?"
    play sound "Click.mp3" noloop 

    Na "Oui c'est bon on peut aller s'asseoir."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous vous asseyez dans le recfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "ça à l'air pas mal ce repas."
    play sound "Click.mp3" noloop 

    Na "Oui c'est vraiment pas mal."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de manger puis [I] s'approche de vous calmêment.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Mhmmm [prénom] je voulais savoir si je pouvais manger avec vous."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Accepter [I].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    P "Oui il y a pas de soucis tu peux venir."
    play sound "Click.mp3" noloop 

    I "Merci beaucoup."
    play sound "Click.mp3" noloop 

    Na "Oui ça fait toujours plaisir d'être avec toi."
    play sound "Click.mp3" noloop 

    "{b}{i} [newname] se met à rougir discrétement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "[newname] ça va ?"
    play sound "Click.mp3" noloop 

    Na "Oui ça va."
    play sound "Click.mp3" noloop 

    P "D'habitude tu ne rougis jamais comme ça."
    play sound "Click.mp3" noloop 

    Na "Je sais mais là c'est personel"
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

    I "Mais avant toute chose je n'ai pas vraiment apprécié les propos d'Ayano et [J2] en vers [newname]"
    play sound "Click.mp3" noloop 

    P "C'est vrai que leurs propos n'étaient pas ouff."
    play sound "Click.mp3" noloop 

    Na "En plus je leurs ai rien fait."
    play sound "Click.mp3" noloop 

    I "Je sais que n'as rien fait [newname] mais je ne comprends pas pourquoi elles se permettent de dire qu'[newname] ne t'appartient pas [prénom]."
    play sound "Click.mp3" noloop 

    P "De toute façon [newname] est à ma création donc je n'ai rien à me reprocher."
    play sound "Click.mp3" noloop 

    I "Bien maintenant on peut donc clore cette discussion."
    play sound "Click.mp3" noloop 

    P "Oui et si on discutait du cours de ce matin."
    play sound "Click.mp3" noloop 

    I "Oui bon idée."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous conntinuez de discuter des cours pendant que vous mangez jusqu'a la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    I "Ok je vous suis."
    play sound "Click.mp3" noloop 

    scene black 
    hide screen lunchroom 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    scene staircase 
    hide screen hall

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
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

    M "Bien maintenant ouvrez votre livre d'histoire à la page 42." 
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

    M "Commme ce que j'allais dire ils ont un mode combat et un mode Civile."
    play sound "Click.mp3" noloop

    M "Leur mode civile leur permettaient de vivre une vie normal comme nous et le mode combat qui leur permettaient de faire la guerre."
    play sound "Click.mp3" noloop

    H "Mais ça veut dire qu'[newname] à ....."
    play sound "Click.mp3" noloop 

    "{b}{i} Tout le monde y compris la [T] se met à regarder [newname].{/i}{/b}" 
    play sound "Click.mp3" noloop

    P "Hey calmez-vous je sais à quoi vous pensez et non je ne l'ai pas amélioré pour cet usage."
    play sound "Click.mp3" noloop

    "{b}{i} La [T] se retourne vers [H].{/i}{/b}"
    play sound "Click.mp3" noloop
    
    M "Désolée [H] mais [pronom] a raison, on ne peut pas considérer [newname] comme une arme de guerre."
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
    
    if A == "M4A1" or "M16A1" or "ST AR-15" or "M4 SOPMOD II" and key == "ARIS-GRFN-M4A1":

        J1 "je savais qu'[newname] était dangereuse surtout qu'elle a le nom techinique d'une arme."
        play sound "Click.mp3" noloop 

    else: 

        J1 "je savais qu'[newname] était dangereuse."
        play sound "Click.mp3" noloop 

    Na "Quoi comment oses-tu dire ça !? je n'ai rien fait... "
    play sound "Click.mp3" noloop

    "{b}{i} [newname] se met subitement à pleurer.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "ça va aller [newname] ne t'inquiêtes pas je suis là."
    play sound "Click.mp3" noloop 

    I "Tu n'as pas honte de dire ce genre de chose [J1] alors qu'elle est sensible !?"
    play sound "Click.mp3" noloop 

    P "Franchement je n'ai jamais vue une personne aussi irrespectueuse que toi !"
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
    play sound "Bell.mp3" noloop

    M "Bon le cours est terminé, vous pouvez quitter la salle et n'oubliez pas l'examen dans une semaine."
    play sound "Click.mp3" noloop

    P "Bon [newname] on y vas ?"
    play sound "Click.mp3" noloop

    "{b}{i}Mais tu remarques qu'[newname] est encore triste.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "[prénom] je pense que je vais la déconnecter et la ramener à ton dortoir."
    play sound "Click.mp3" noloop

    P "Tu es sûre [I] ?" 
    play sound "Click.mp3" noloop

    I "Oui car elle est vraiment pas bien."
    play sound "Click.mp3" noloop

    P "Ok prends soin d'elle."
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

    M "[P] je suis complétement désolée pour cet incident."
    play sound "Click.mp3" noloop

    P "Pas de soucis mais c'est vrai qu'[J1] est un petit probléme pour [newname]."
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

    scene hallway
    show screen hallway 

    P "Bon je vais...."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i}aller réviser en permanence{/i}{/b}" : 
            jump study 

        "{b}{i}aller au club{/i}{/b}" :
            
            P "aller en salle de club."
            play sound "Menu.mp3" noloop 

            scene staircase
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

            "{b}{i}Tu te diriges vers ta salle de club.{/i}{/b}"
            play sound "Click.mp3" noloop
 
            scene clubroom
            show screen clubroom 
            play sound "Door.mp3" noloop 

            P "Au moins ici je vais pouvoir être tranquille." 
            play sound "Menu.mp3" noloop 

            "{b}{i}Tu révises pendant une heure.{/i}{/b}" 
            play sound "Click.mp3" noloop

            P "Bon finis les révisions pour aujourd'hui."
            play sound "Click.mp3" noloop 

            "{b}{i}Tu ranges tes livres avant de sortir ton ordinateur pour voir le système emotionelle d'[newname].{/i}{/b}"
            play sound "Click.mp3" noloop 

            if newname == "Aris" and key == "ARIS-GRFN-M4A1":
                jump connexion

            label choice7:

            play sound "Menu.mp3" noloop
            $ ip = renpy.input("Entres l'adresse IP pour pouvoir te connecter à [newname].")
            $ ip = ip.strip()

            if ip == "001.018.009.019":

                "{b}{i}La connexion est établie.{/i}{/b}"
                play sound "Menu.mp3" noloop 
                jump connexion

            if ip == "001.009.011.015": 

                "{b}{i}La connexion est établie.{/i}{/b}"
                play sound "Menu.mp3" noloop 

                P "Tiens on dirait que je me suis connecté a l'ordinateur de l'attaquant d'avant."
                play sound "Click.mp3" noloop 

                P "Bon il me reste plus qu'......."
                play sound "Menu.mp3" noloop 

                menu:    

                    "{b}{i} Attaquer !!! {/i}{/b}" :
                        play sound "Menu.mp3" noloop 
                 
                "{b}{i} Tu envois une attaque par déni de service.{/i}{/b}"
                play sound "Click.mp3" noloop 

                P "Bon l'attaquant est vulnérable, c'est le moment de finir le travail."
                play sound "Click.mp3" noloop 

                "{b}{i} Tu continues l'attaque.{/i}{/b}"
                play sound "Click.mp3" noloop  

                P "Bon j'ai fini l'attaque, leur système interne est complétement détruit."
                play sound "Click.mp3" noloop                      
                        
                scene black 
                hide screen clubroom
                hide screen points
                hide screen day
                play music "gameover.mp3" noloop
                "{b}{i}Fin numéro 5 : Félicitation tu as bien complétement attaqué et piraté l'adressee IP 001.009.011.015 par deni de service (DDOS).{/i}{/b}"
                play sound "Menu.mp3" noloop 
    
                menu:    

                    "{b}{i}Retourner au menu principal.{/i}{/b}" :
                        return 
                    "{b}{i}Réessayer.{/i}{/b}" : 
                        scene clubroom
                        show screen clubroom
                        show screen points
                        show screen day 
                        play music "Soundtrack.mp3" loop volume 1.0
                        jump choice7

            else: 

                "{b}{i}Erreur système. L'adresse IP est incorrecte.{/i}{/b}"
                play sound "Menu.mp3" noloop 
                jump choice7

label connexion:

            P "Ah ouais elle encore instable emotionellement la pauvre...."
            play sound "Click.mp3" noloop

            "{b}{i} Tu ranges ton ordi avant de quiiter la salle de club.{/i}{/b}"
            play sound "Click.mp3" noloop 

            if pronom == "il":

                P "Je suis fatigué avec cette journée."
                play sound "Click.mp3" noloop

            elif pronom == "elle": 

                P "Je suis fatiguée avec cette journée."
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

            scene staircase
            hide screen hall
            play sound "Click.mp3" noloop

            P "..."
            play sound "Click.mp3" noloop

            scene hallway
            show screen hallway
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

    "{b}{i}Tu sors tes livres pour réviser mais Soudainement [J2] entra pour venir voir [J1].{/i}{/b}"
    play sound "Click.mp3" noloop 

    J2 "[J1] tu es là ?"
    play sound "Click.mp3" noloop

    J1 "Oui Pourquoi ?"
    play sound "Click.mp3" noloop

    J2 "C'était pour qu'on aille au club pour travailler."
    play sound "Click.mp3" noloop 

    J1 "Ok j'arrive..."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Tiens j'avais vu qu'il y avait [prénom], il fait quoi ?"
        play sound "Click.mp3" noloop

        J1 "Laisse tomber il est en train de reviser." 
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Tiens j'avais vu qu'il y avait [prénom], elle fait quoi ?"
        play sound "Click.mp3" noloop 

        J1 "Laisse tomber elle est en train de reviser." 
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

    if pronom == "il":

        P "Je suis fatigué avec cette journée."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Je suis fatiguée avec cette journée."
        play sound "Click.mp3" noloop 

    scene black
    hide screen perm

    "{b}{i}Tu quittes la salle de permanence.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway
    show screen hallway

    P "Maintenant je vais retourner au dortoir."
    play sound "Click.mp3" noloop 

label dorm2: 

    "{b}{i}Tu continues ton chemin vers le dortoir et tu vois [I] sortir de ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    P "Oh salut [I]."
    play sound "Click.mp3" noloop 

    I "Re [prénom] ça va ?"
    play sound "Click.mp3" noloop 

    P "ça va mais un peu en détresse pour [newname]."
    play sound "Click.mp3" noloop 
    
    if pronom == "il":
        
        I "Je sais mais je vois aussi que tu es fatigué."
        play sound "Click.mp3" noloop 

    elif pronom == "elle":
       
        I "Je sais mais je vois aussi que tu es fatiguée."
        play sound "Click.mp3" noloop 

    P "Oui je sais j'ai beaucoup révisé."
    play sound "Click.mp3" noloop 

    I "Ok je comprend maintenant."
    play sound "Click.mp3" noloop 

    P "Et sinon comment elle va [newname] ?"
    play sound "Click.mp3" noloop 

    I "Elle est déconnectée et se repose tranquillement."
    play sound "Click.mp3" noloop 

    P "Ok."
    play sound "Click.mp3" noloop 

    "{b}{i}[I] te remet la clé de ton dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Merci."
    play sound "Click.mp3" noloop 

    I "De rien il y a pas de soucis, bon je vais te laisser."
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i}[I] s'éloigna pour aller faire ses occupations.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon il est temps d'aller voir [newname]."
    play sound "Click.mp3" noloop 

    scene black
    hide screen hallway

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room 

    P "Enfin au dortoir...."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
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

    Mo "Sinon comment se passent les cours pour toi ?"
    play sound "Click.mp3" noloop

    P "ça se passe bien."
    play sound "Click.mp3" noloop

    Mo "Génial alors et comment elle va ta petite [A] ?"
    play sound "Click.mp3" noloop

    P "Elle va bien et en plus je lui ai même trouvé un prénom qui lui va bien."
    play sound "Click.mp3" noloop

    Mo "Ah bon le quel ?"
    play sound "Click.mp3" noloop

    P "Le prénom que je lui ai trouvé est [newname]"
    play sound "Click.mp3" noloop

    Mo "Oh c'est mignon."
    play sound "Click.mp3" noloop

    P "Merci maman."
    play sound "Click.mp3" noloop

    Mo "De rien mais je vais devoir te laisser je dois m'occuper de ta soeur tu sais comment elle est..."
    play sound "Click.mp3" noloop

    P "Ah oui celle-là je vois..."
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

# la semaine suivante

    scene black
    hide screen room
    hide screen day

    "{b}{i} une semaine plus tard.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room 
    show screen room
    show screen day
    $ day += 7 

    play sound "Alarm.mp3" noloop 
    P "Oh super....."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te léves tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon aujourd'hui c'est mon prémier examen de cette année."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te changes et t'approches de [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu sors rapidement ton ordi pour voir son état.{/i}{/b}"
    play sound "Click.mp3" noloop

    if newname == "Aris" and key == "ARIS-GRFN-M4A1":
        jump skip2
        
label choice8:

    play sound "Menu.mp3" noloop
    $ ip = renpy.input("Entres l'adresse IP pour pouvoir te connecter à [newname].")
    $ ip = ip.strip()

    if ip == "001.018.009.019":

        "{b}{i}La connexion est établie.{/i}{/b}"
        play sound "Menu.mp3" noloop 

    else:

        "{b}{i}Erreur système. L'adresse IP est incorrecte.{/i}{/b}"
        play sound "Menu.mp3" noloop 
        jump choice8

label skip2: 

    P "Bon on dirait qu'elle est stable, je vais pouvoir la démarrer." 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    Na "Démarrage en cours...."
    play sound "Click.mp3" noloop

    "{b}{i}Tu patientes tranquillement jusqu'à que son démarrage sois complet.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Démarrage terminé bonjour [P]."
    play sound "Click.mp3" noloop

    P "Bonjour ma petite [newname] comment ça va ?"
    play sound "Click.mp3" noloop 

    Na "ça va."
    play sound "Click.mp3" noloop

    P "Bon on va cours ?" 
    play sound "Click.mp3" noloop 

    Na "Ok je te suis."
    play sound "Click.mp3" noloop  
    hide screen room
    scene black

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway 
    show screen hallway  

    "{b}{i}Dans le couloir tu croises [I].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut [I] comment ça va ?" 
    play sound "Click.mp3" noloop 

    I "ça va mais je suis un peu stressée pour l'examen."
    play sound "Click.mp3" noloop 

    P "ça va aller j'ai confiance en toi." 
    play sound "Click.mp3" noloop 

    I "Merci beaucoup de me soutenir.~" 
    play sound "Click.mp3" noloop 

    P "C'est normal." 
    play sound "Click.mp3" noloop 

label choice9:

    "{b}{i}Vous continuez votre chemin vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop  
    hide screen hallway 
    scene black

    "{b}{i} Quand vous entrez dans la salle tout les autres élèves sont déjà là.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom
    show screen class_404

    K "Oh salut [P] comment ça va ?" 
    play sound "Click.mp3" noloop 

    P "ça va bien comme d'habitude." 
    play sound "Click.mp3" noloop 

    K "Oh cool c'est génial." 
    play sound "Click.mp3" noloop 

    H "Et sinon comment elle va [newname] ?" 
    play sound "Click.mp3" noloop 

    P "Elle va bien et elle est juste là." 
    play sound "Click.mp3" noloop 

    H "Salut."
    play sound "Door.mp3" noloop

    "{b}{i}Soudainement la porte s'ouvrit et [M] entra.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour aujourd'hui comme vous le savez vous avez votre premier examen je vais vous distribuer votre copie." 
    play sound "Click.mp3" noloop 

    Na "Ok." 
    play sound "Click.mp3" noloop 

    "{b}{i}[M] Commença à distribuer les copies.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Vous avez une heure c'est parti !!!" 
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde retourna sa copie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ grade = 0.0 

    "Question 1 : Quel a été le type de guerre en 2095-2096 ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Guerre cybernétique":
            $ grade += 2.0
        "Guerre conventionnelle":
            $ grade += 0.0
        "Guerre économique":
            $ grade += 0.0

    "Question 2 : Quelle technologie a dominé cette guerre ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Drones autonomes":
            $ grade += 0.0
        "Exosquelettes":
            $ grade += 0.0
        "Robots de combat":
            $ grade += 2.0

    "Question 3 :  où cette guerre a-t-elle éclaté ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Europe":
            $ grade += 0.0
        "Asie":
            $ grade += 2.0
        "Amérique":
            $ grade += 0.0

    "Question 4 : Quelle a été la principale cause de la guerre ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Une crise économique": 
            $ grade += 0.0
        "Un conflit territorial":
            $ grade += 0.0
        "Une attaque cybernétique":
            $ grade += 2.0

    "Question 5 : Quelle nation a initié ce conflit ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Japon":
            $ grade += 2.0
        "États-Unis":
            $ grade += 0.0
        "Russie":
            $ grade += 0.0

    "Question 6 : Quelle stratégie a été la plus utilisée ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Cyberattaques":
            $ grade += 1.0
        "Attaques de drones":
            $ grade += 0.0
        "Robots humanoides":
            $ grade += 2.0

    "Question 7 : Combien de temps a duré la guerre ?"
    play sound "Menu.mp3" noloop 

    menu:
        "6 mois":
            $ grade += 0.0
        "1 an":
            $ grade += 2.0
        "2 ans":
            $ grade += 0.0

    "Question 8 : Quel traité a mis fin à la guerre ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Le traité de Danto":
            $ grade += 2.0
        "Le traité de Sécurité Universelle":
            $ grade += 0.0
        "Le traité de Réconciliation":
            $ grade += 0.0

    "Question 9 : Quel a été l'impact principal de la guerre ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Une crise économique":
            $ grade += 1.0
        "Une crise sociale":
            $ grade += 0.0
        "Une dévastation écologique":
            $ grade += 2.0

    "Question 10 : Quel rôle a joué Aris durant la guerre ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Conseillére stratégique":
            $ grade += 0.0
        "Médiatrice diplomatique":
            $ grade += 0.0
        "Combattante":
            $ grade += 2.0

    "{b}{i}Aprés l'examen tout le monde remit leur copie à [M].{/i}{/b}"
    play sound "Click.mp3" noloop

    K "Cette examen n'était si dur que ça."
    play sound "Click.mp3" noloop

    I "Je confirme bon on verra bien les résultats."
    play sound "Click.mp3" noloop

    M "Si jamais je vous corrigerai vos copies durant la pause et vous les rendrez cet après-midi."
    play sound "Click.mp3" noloop

    Na "Déjà !?" 
    play sound "Click.mp3" noloop 

    M "Oui c'est exact, bon maintenant sortez votre livre page 10 car nous allons voir un nouveau sujet." 
    play sound "Click.mp3" noloop 

    K "Et quel sera ce nouveau sujet ?" 
    play sound "Click.mp3" noloop 

    M "Un sujet de grammaire." 
    play sound "Click.mp3" noloop 

    K "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continua sans probléme.{/i}{/b}"
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

    "{b}{i} Vous vous dirigez votre chemin vers la réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    scene staircase
    hide screen hallway

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hall 
    show screen hall

    "{b}{i} On arrivant dans le hall tu vois soudainement [E] qui discute avec quelqu'un qui n'est pas du lycée.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Attend deux secondes [newname] je dois faire un truc."
    play sound "Click.mp3" noloop 

    Na "Ok pas de soucis"
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te mets dans un coin du hall pour écouter secrétement.{/i}{/b}"
    play sound "Click.mp3" noloop

    R "J'aimerai rencontrer quelqu'un parmi vos élèves."
    play sound "Click.mp3" noloop 

    E "Oui pas de soucis."
    play sound "Click.mp3" noloop 

    "{b}{i} Les deux continuèrent de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    E "Merci je m'occuperai d'organiser le rendez-vous pour vous après les cours."
    play sound "Click.mp3" noloop 

    R "Merci beaucoup."
    play sound "Click.mp3" noloop 

    E "Mais de rien c'est normal."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu choisis de partir vers la réfectoire avec [newname] pour éviter de te faire attraper par [E].{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hall

    "{b}{i} Vous arrivez enfin au refectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
    show screen lunchroom 
    
    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    P "Bien sûr tu veux qu'on fasse quoi d'autres ? Prendre la poudre d'escampette tant qu'on y est ?"
    play sound "Click.mp3" noloop 

    "{b}{i} [newname] se mit à rigoler.{/i}{/b}"
    play sound "Menu.mp3" noloop

    P "Mais bon tu m'as commpris."
    play sound "Click.mp3" noloop 

    Na "oui je t'ai compris."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allez vers comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon voyonns voir aujourd'hui il y a que des pâtes carbonara." 
    play sound "Menu.mp3" noloop 
    
    menu:    

        "{b}{i} Pates carbonara {/i}{/b}" :
            $ points -= 600

    P "C'est bon [newname] tu t'es servie ?"
    play sound "Click.mp3" noloop 

    Na "Oui c'est bon on peut aller s'asseoir."
    play sound "Click.mp3" noloop  

    P "Ok."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous cherchez une place et vous apercevez [I] déjà assise à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oh salut [I] on peut venir manger avec toi ?"
    play sound "Click.mp3" noloop 

    I "Oui bien sur."
    play sound "Click.mp3" noloop 

    P "Merci."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous asseyez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon [I] je ne t'ai pas demandé. Comment c'est passé l'examen pour toi ?"
    play sound "Click.mp3" noloop 

    I "ça s'est bien passée pour moi et toi ?"
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Je dirais que je me suis bien débrouillé."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Je dirais que je me suis bien débrouillée."
        play sound "Click.mp3" noloop 
    
    I "ça ne m'étonne pas venant de toi."
    play sound "Click.mp3" noloop 

    Na "J'ai lui déjà dit la même chose à [prénom] un jour." 
    play sound "Click.mp3" noloop 

    I "Et toi [newname] comment ça s'est passée l'examen ?"
    play sound "Click.mp3" noloop 

    Na "ça s'est bien passée pour moi je ne m'inquiéte pas."
    play sound "Click.mp3" noloop 

    I "Cool alors."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de discuter.{/i}{/b}"
    play sound "Bell.mp3" noloop 
    
    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    I "Ok je vous suis."
    play sound "Click.mp3" noloop 

    scene black 
    hide screen lunchroom 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    scene staircase 
    hide screen hall

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway 
    show screen hallway

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Sinon [I] je voulais savoir qwe fait [Y] car à part durant les cours je la vois pas trop."
    play sound "Click.mp3" noloop 

    I "Ah [Y], bah j'ai entendu dire qu'elle a une affaire urgente à régler."
    play sound "Click.mp3" noloop 

    P "Une affaire urgente à régler !?"
    play sound "Click.mp3" noloop 

    I "Oui mais j'en sais pas non plus."
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    Na "Dois-je vous rappelez qu'on a cours."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Oui désolé allons-y."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Oui désolée allons-y."
        play sound "Click.mp3" noloop 

    I "Oui tu as raison."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hallway

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom  
    show screen class_404 

    M "Ah vous voila un peu plus et vous seriez en retard."
    play sound "Click.mp3" noloop 

    I "Désolée..."
    play sound "Click.mp3" noloop 

    M "il y a pas de soucis tant que vous êtes à l'heure."
    play sound "Click.mp3" noloop 

    Na "Merci."
    play sound "Click.mp3" noloop 

    M "Bon je vais pouvoir vous rendre les résultats de vos premiers examens."
    play sound "Click.mp3" noloop 

    K "Cool enfin."
    play sound "Click.mp3" noloop

    I "Je vais commencer par [prénom] et [Na]."
    play sound "Click.mp3" noloop 

    P "Ok."
    play sound "Click.mp3" noloop 

    M "[P] tu as eu [grade]/20"
    play sound "Click.mp3" noloop 
   
    if grade == 20.0:
        
        M "Félicitation tu l'as réussi à la perfection comme d'habitude."
        play sound "Click.mp3" noloop

        P "Merci."
        play sound "Click.mp3" noloop

    elif grade <= 12.0:
       
        M "C'est en dessous de la moyenne je n'ai pas le choix que de t'expulser du lycée..."
        play sound "Click.mp3" noloop

        P "Quoi et mon avenir !?"
        play sound "Click.mp3" noloop
    
        M "Désolé mais j'avais déjà prévenu concernant les mauvaises notes."
        play sound "Click.mp3" noloop

        scene black
        hide classroom
        hide screen class_404
        hide screen points
        hide screen day
        play music "gameover.mp3" noloop
        "{b}{i}Fin numéro 6 : Premiére mauvaise note qui te vaut une exclusion du lycée.{/i}{/b}"
        play sound "Menu.mp3" noloop

        menu:    

            "{b}{i}Abandonner{/i}{/b}" :
                return 
            "{b}{i}Réessayer.{/i}{/b}" :
                scene black
                show screen points 
                play music "Soundtrack.mp3" loop volume 1.0
                jump choice9
    
    else:
       
        M "C'est pas mal."
        play sound "Click.mp3" noloop

        P "Merci."
        play sound "Click.mp3" noloop

    M "[Na] tu as eu 19/20 félicitation aussi."
    play sound "Click.mp3" noloop 

    Na "Merci beaucoup."
    play sound "Click.mp3" noloop 

    M "[H] tu as eu 15/20."
    play sound "Click.mp3" noloop 

    H "Merci beaucoup."
    play sound "Click.mp3" noloop 

    M "[I] tu as eu 18/20 félicitation."
    play sound "Click.mp3" noloop 

    I "Merci beaucoup."
    play sound "Click.mp3" noloop 

    M "[Hi] tu as eu 16/20."
    play sound "Click.mp3" noloop 

    Hi "Merci beaucoup."
    play sound "Click.mp3" noloop 

    M "[K] tu as eu 17/20."
    play sound "Click.mp3" noloop 

    K "Merci beaucoup."
    play sound "Click.mp3" noloop 

    M "[N] tu as eu 18/20."
    play sound "Click.mp3" noloop 

    N "Merci beaucoup."
    play sound "Click.mp3" noloop 

    M "[Y] tu as eu 20/20 félicitation."
    play sound "Click.mp3" noloop 

    "{b}{i} Soudainement le ton de [M] changea.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bon au tour des ultimes Jumelles maintenant pour finir."
    play sound "Click.mp3" noloop 

    J1 "Ok."
    play sound "Click.mp3" noloop 

    M "[J1] tu as eu 14/20."
    play sound "Click.mp3" noloop 

    J1 "Super....."
    play sound "Click.mp3" noloop 

    M "Et toi [J2] tu as eu 14/20."
    play sound "Click.mp3" noloop 

    J2 "Super....."
    play sound "Click.mp3" noloop 

    M "Bon la moyenne générale n'est pas mal, continuez de bien travaillez comme ceci."
    play sound "Click.mp3" noloop 

    Y "Il n'y aura pas de soucis pour moi."
    play sound "Click.mp3" noloop 

    Na "Moi aussi vous pourrez sur moi."
    play sound "Click.mp3" noloop 

    I "De même pour moi."
    play sound "Click.mp3" noloop 

    M "Bien nous pouvons continuer notre cours de ce matin sur la grammaire, veuillez sortir vos livres."
    play sound "Click.mp3" noloop 

    "{b}{i} Le cours continua tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    M "Bon le cours est bientôt terminé."
    play sound "Bell.mp3" noloop 

    M "Bon bah Le cours est terminé vous pouvez quitter la salle."
    play sound "Click.mp3" noloop

    P "Bon [newname] on y vas ?"
    play sound "Click.mp3" noloop 

    Na "Ok"
    play sound "Click.mp3" noloop 

    M "Attends deux secondes [prénom]."
    play sound "Click.mp3" noloop

    P "Oui qu'il y a t'il ?"
    play sound "Click.mp3" noloop

    M "[E] t'attend dans son bureau."
    play sound "Click.mp3" noloop

    P "Comment ça !?"
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "L'ultime créateur convoqué chez le bureau des élèves c'est bizarre..."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "L'ultime créatrice convoquée chez le bureau des élèves c'est bizarre..."
        play sound "Click.mp3" noloop 

    P "Bon ok j'y vais."
    play sound "Click.mp3" noloop

    scene black 
    hide screen class_404 

    Na  "Bon tu penses que c'est qui la personne qui veut te voir ?"
    play sound "Click.mp3" noloop

    P "J'en ai aucune idée."
    play sound "Click.mp3" noloop

    "{b}{i}Tu diriges vers dans le couloir avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene hallway
    show screen hallway 

    "{b}{i}Tu continues dans le couloir avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop

    scene staircase 
    hide screen hallway

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hall
    show screen hall 

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    stop music fadeout 2.0

    scene black 
    hide screen hall 

    "{b}{i}Tu entres dans le bureau des élèves.{/i}{/b}"
    play sound "Click.mp3" noloop

    play music "Soundtrack2.mp3" loop volume 1.0

    scene office 
    show screen office 
    play sound "Door.mp3" noloop 

    P "Bonjour c'est moi [nom]."  
    play sound "Click.mp3" noloop 

    E "Ah te voilà vas-y assis toi, la personne qui veut venir va pas tarder." 
    play sound "Click.mp3" noloop 

    P "OK." 
    play sound "Door.mp3" noloop 

    "{b}{i}Puis soudainement la personne entra dans le bureau.{/i}{/b}"
    play sound "Click.mp3" noloop 

    R "Bonjour [nom]..."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Bonjour enchanté, pourrais-je savoir qui êtes-vous ?"
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Bonjour enchantée, pourrais-je savoir qui êtes-vous ?"
        play sound "Click.mp3" noloop 

    R "Doucement je vais me présenter."
    play sound "Click.mp3" noloop 

    P "Ok."
    play sound "Click.mp3" noloop 

    R "Bien je tiens encore à remercier [E] pour cet entretien."
    play sound "Click.mp3" noloop 

    E "Il n'y a pas de soucis."
    play sound "Click.mp3" noloop 

    R "Donc [nom] c'est bien toi l'[domaine] ?"
    play sound "Click.mp3" noloop 

    P "Oui c'est exact mais vous qui êtes-vous ?"
    play sound "Click.mp3" noloop 

    C "Ah oui désolé je me nomme [C]."
    play sound "Click.mp3" noloop 

    P "[C]..."
    play sound "Click.mp3" noloop 

    C "Je suis l'ancien président de Neogen Technologies."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu réalises qui est la personne en face de toi.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Que voulez-vous à moi et [newname] ?"
    play sound "Click.mp3" noloop 

    C "Juste discuter de deux-trois sujets avec toi."
    play sound "Click.mp3" noloop 

    P "Si vous voulez récupérer [newname] vous pouvez tout de suite oublier."
    play sound "Click.mp3" noloop 

    C "Non je ne veux absolument pas te récupérer [A]."
    play sound "Click.mp3" noloop  

    P "[A] !? Comment êtes-vous au courant de ce nom !?"
    play sound "Click.mp3" noloop 

    if A == "M4A1" or "M16A1" or "ST AR-15" or "M4 SOPMOD II" or "UMP45" and key == "ARIS-GRFN-M4A1":

        C "C'est simple je suis son créateur et son concepteur original et je vois que tu as aussi choisi son nom technique."
        play sound "Click.mp3" noloop 

        P "C'est donc vous à l'origine de [A] et oui j'ai choisi le nom technique."
        play sound "Click.mp3" noloop 

        C "Cool alors."
        play sound "Click.mp3" noloop 

        P "Mais j'ai une question."
        play sound "Click.mp3" noloop 

        C "Oui dit moi."
        play sound "Click.mp3" noloop 

        P "Pourquoi elle avait ces multiples noms dans sa base de données."
        play sound "Click.mp3" noloop 

        C "Car elle a été conçu pour utilser plusieurs fusils en particulier, ceux enregistrés dans sa base de données justement."
        play sound "Click.mp3" noloop 

        P "Ok je vois et J'ai toujours voulu connaître la personne qui a conçu [A]."
        play sound "Click.mp3" noloop 

        C "Me voilà ici présent."
        play sound "Click.mp3" noloop 

        P "C'est un honneur." 
        play sound "Click.mp3" noloop 

    else:

        C "C'est simple je suis son créateur et son concepteur original."
        play sound "Click.mp3" noloop 

        P "C'est donc vous à l'origine de [A]."
        play sound "Click.mp3" noloop 

        C "Oui c'est exact."
        play sound "Click.mp3" noloop 

        P "J'ai toujours voulu connaître la personne qui a conçu [A]."
        play sound "Click.mp3" noloop 

        C "Me voilà ici présent."
        play sound "Click.mp3" noloop 

        P "C'est un honneur." 
        play sound "Click.mp3" noloop 

    if pronom == "il":

        C "Donc, comment es-tu tombé sur [A] malgré le démantèlement des robots ?"
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        C "Donc, comment es-tu tombée sur [A] malgré le démantèlement des robots ?"
        play sound "Click.mp3" noloop 

    P "Il y a 3 mois, je faisais de l'urbex avec un ancien ami à moi dans un entrepôt abandonné et il est tombé sur [A] en ouvrant un grand placard."
    play sound "Click.mp3" noloop 

    C "Je vois et que c'était-il passé ensuite ?"
    play sound "Click.mp3" noloop 

    P "On a eu un petit conflit."
    play sound "Click.mp3" noloop 

    C "Comment ça ?"
    play sound "Click.mp3" noloop 

    P "On s'est disputé car je voulais garder [A]..."
    play sound "Click.mp3" noloop 
    
    C "Oh je vois, qu'a t-il dit part rapport à [A] ?"
    play sound "Click.mp3" noloop 

    P "il a dit qu'elle ne m'appartenait pas mais je lui ai dit qu'elle était abandonnée."
    play sound "Click.mp3" noloop 

    C "C'est exact elle était abandonnée à ce moment-là."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Oui je me suis même renseigné sur les articles de loi concernant ça et j'en ai trouvées trois."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Oui je me suis même renseignée sur les articles de loi concernant ça et j'en ai trouvées trois."
        play sound "Click.mp3" noloop

    C "Quels sont ces fameux articles de loi ?"  
    play sound "Click.mp3" noloop  

    P "Le premier, c'est l'article 24, alinéa 1. Il stipule que tout objet abandonné devient la propriété de la personne qui le récupère."  
    play sound "Click.mp3" noloop  

    C "Et le second ?"  
    play sound "Click.mp3" noloop  

    P "L'article 24, alinéa 2, précise que cette règle ne s'applique plus si le propriétaire initial réclame son bien. Toutefois, la restitution ne peut se faire que par négociation."  
    play sound "Click.mp3" noloop  

    C "Et le dernier ?"  
    play sound "Click.mp3" noloop  

    P "Enfin, l'article 24, alinéa 3, impose au nouveau propriétaire la responsabilité complète de l'objet récupéré, y compris son entretien ou sa gestion."  
    play sound "Click.mp3" noloop  

    E "Toi [prénom], tu respectes bien l'article 24, alinéa 3."  
    play sound "Click.mp3" noloop  

    P "Merci beaucoup."
    play sound "Click.mp3" noloop 

    C "Bien et sinon ton ami est devenu quoi maintenant ?"
    play sound "Click.mp3" noloop 

    P "je ne sais pas mais je pense qu'il est dans un autre lycée."
    play sound "Click.mp3" noloop 

    C "Je voulais aussi savoir comment tu as amélioré [A] ?"
    play sound "Click.mp3" noloop 

    P "J'ai commencé par changer son processeur."
    play sound "Click.mp3" noloop 

    C "Ah bon pourtant le processeur choisi pour sa conception était bien." 
    play sound "Click.mp3" noloop 

    P "oui mais actuellement il est trop faible pour les besoins d'[newname] actuels."
    play sound "Click.mp3" noloop 

    C "Ok je comprends mieux et qu'as-tu fait d'autres comme changement ?"
    play sound "Click.mp3" noloop 

    P "Je lui ai rajouté une carte mémoire."
    play sound "Click.mp3" noloop 

    C "Intéressant."
    play sound "Click.mp3" noloop 

    P "Merci."
    play sound "Click.mp3" noloop 

    C "Il n'y a pas de soucis."
    play sound "Click.mp3" noloop 

    P "Vous voulez me demander quelques choses d'autre ?"
    play sound "Click.mp3" noloop 

    C "Oui une dernière chose."
    play sound "Click.mp3" noloop 

    P "Oui dites-moi."
    play sound "Click.mp3" noloop 

    C "Connais-tu l'entierté des capacités de [A] ?"
    play sound "Click.mp3" noloop

    P "Non pas complétement malheureusement."
    play sound "Click.mp3" noloop 

    C "Ok mais je pense que j'ai quelques choses qui peut t'intéresser."
    play sound "Click.mp3" noloop 

    P "Oui dites-moi."
    play sound "Click.mp3" noloop 

    C "Il se pourrait que j'aie encore les documents techniques originaux d'[A] que je pourrais te donner."
    play sound "Click.mp3" noloop 

    P "Vraiment !?"
    play sound "Click.mp3" noloop 
 
    C "Oui ils seront tous pour toi."
    play sound "Click.mp3" noloop

    "{b}{i}[C] sortit des documents.{/i}{/b}"
    play sound "Click.mp3" noloop

    C "Tiens les voici..."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Accepter les documents.{/i}{/b}" :

            P "Merci beaucoup ça fait plaisir."
            play sound "Click.mp3" noloop 

            C "De rien mais avant qu'on finissent notre entretiens j'aimerai te demander un dernier truc."
            play sound "Click.mp3" noloop 

            $ info += 1.0
            
        "{b}{i} Refuser les documents. {/i}{/b}" : 

            P "Merci beaucoup mais je préfére partir sur de nouvelles bases."
            play sound "Click.mp3" noloop 

            C "Ok je comprends mais avant qu'on finissent notre entretiens j'aimerai te demander un dernier truc."
            play sound "Click.mp3" noloop 

    P "Oui dites-moi."
    play sound "Click.mp3" noloop 

    C "J'aimerai voir comment est [A] et son comportement de mes propres yeux."
    play sound "Click.mp3" noloop 

    P "Il n'y a pas de soucis, [newname] approche s'il te plaît."
    play sound "Click.mp3" noloop 

    Na "Oui qu'il y a t'il [prénom] ?"
    play sound "Click.mp3" noloop 

    P "Je veux que tu te présntes à [C]."
    play sound "Click.mp3" noloop 

    Na "Ok." 
    play sound "Click.mp3" noloop 

    C "Donc je présume que tu es [Na]."
    play sound "Click.mp3" noloop 

    Na "Oui exactement."
    play sound "Click.mp3" noloop 

    C "Donc vas-y présente toi."
    play sound "Click.mp3" noloop 

    Na "Je me nomme [Na], j'ai 18 ans et je suis la création de [P], je suis actuellement lycéenne en Second-E dans ce lycée, mon défaut est que je suis souvent sensible mais j'ai appris beaucoup de choses grâce à [P]."
    play sound "Click.mp3" noloop 

    C "Bien merci pour ta présentation."
    play sound "Click.mp3" noloop 

    Na "Merci beaucoup."
    play sound "Click.mp3" noloop 

    C "Bien [P] je vois qu'[newname] se débrouille bien avec toi."
    play sound "Click.mp3" noloop

    P "Merci ça fait plaîsir."
    play sound "Click.mp3" noloop 

    C "Avant de partir j'ai encore un truc à te dire concernant [newname]."
    play sound "Click.mp3" noloop 

    P "Oui dites-moi, je vous écoute."
    play sound "Click.mp3" noloop 

    C "J'ai entendu dire que quelqu'un veut s'attaquer à [newname] donc fais attention."
    play sound "Click.mp3" noloop 

    E "Je confirme aussi car une personne m'a aussi dit qu'elle avait trouvées des informations concernant une potentielle menace ou traître envers [newname]."
    play sound "Click.mp3" noloop

    P "Et qui est cette personne ?"
    play sound "Click.mp3" noloop 

    E "Elle préfére rester anonyme pour le bien de ces travaux."
    play sound "Click.mp3" noloop 

    P "Ok."
    play sound "Click.mp3" noloop 

    E "Bien maintenant vous pouvez quitter mon bureau [prénom] et [newname]."
    play sound "Click.mp3" noloop 

    P "Merci au revoir."
    play sound "Click.mp3" noloop 

    scene black 
    hide screen office

    "{b}{i}Tu diriges vers le hall avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop
     
    stop music fadeout 2.0

    scene hall
    show screen hall

    play music "Soundtrack.mp3" loop volume 1.0

    P "Bon on retourne au dortoir ?"
    play sound "Click.mp3" noloop 

    Na "Oui pourquoi pas."
    play sound "Click.mp3" noloop 

    P "Ok."
    play sound "Click.mp3" noloop 

    scene staircase 
    hide screen hall 

    "{b}{i}Tu continues vers le couloir avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway
    show screen hallway

    P "Bon on est bientôt arrivés."
    play sound "Click.mp3" noloop 

    Na "Ok."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis tu aperçois [I] juste devant.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut Comment ça va ?"
    play sound "Click.mp3" noloop 

    I "Je vais bien et toi comment ça s'est passé avec [E] ?"
    play sound "Click.mp3" noloop 

    P "Oui ça s'est bien passé, [E] voulait que je vois l'ancien président de Neogen technologies voulait juste voir [newname]."
    play sound "Click.mp3" noloop 

    I "Ok."
    play sound "Click.mp3" noloop 

    P "[E] m'a aussi dit qu'il y aurait un traître parmi nous."
    play sound "Click.mp3" noloop 

    I "Un traître parmi nous !?"
    play sound "Click.mp3" noloop

    P "Non, c'est pas comme si tout le monde avait l'air suspect."
    play sound "Click.mp3" noloop

    P "Entre Ayano, qui est complètement timbrée,"
    play sound "Click.mp3" noloop

    P "Aiko, qui est complètement chambrée,"
    play sound "Click.mp3" noloop

    P "Yuki, qui disparaît après les cours,"
    play sound "Click.mp3" noloop

    P "La [T], qui a des doutes sur [newname],"
    play sound "Click.mp3" noloop

    P "et Takeshi, qui s'intéresse à [newname]..."
    play sound "Click.mp3" noloop

    P "Ah non, ça va."
    play sound "Click.mp3" noloop 

    "{b}{i}Les filles se mettent à rigoler.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Merci de m'avoir fait rire [prénom]."
    play sound "Click.mp3" noloop

    P "De rien."
    play sound "Click.mp3" noloop 

    I "Bon je dois vous laisser."
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    Na "à demain Iris."
    play sound "Click.mp3" noloop 

    I "à demain les [nom]."
    play sound "Footsteps.mp3" noloop 

    "{b}{i}[I] retourna à son dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon il faut qu'on rentre au dortoir aussi." 
    play sound "Click.mp3" noloop 

    Na "Ok."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu continues vers ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene black
    hide screen hallway

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room 

    P "Enfin au dortoir...."
    play sound "Click.mp3" noloop

    Na "Oui ça fait du bien d'être de retour au dortoir après un examen, les cours et le rendez-vous." 
    play sound "Click.mp3" noloop 

    P "Oui je confirme."
    play sound "Click.mp3" noloop 

    Na "Bon je vais me déconnecter."
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i} [newname] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon elle s'est déconnctée, je vais me cherecher à manger." 
    play sound "Click.mp3" noloop 

    scene black
    hide screen room

    "{b}{i} Tu pars chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 700 
    scene room 
    show screen room

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    "{b}{i} Tu manges tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changea avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen room
    hide screen day

    "{b}{i} Une semaine plus tard.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room 
    show screen room
    show screen day
    $ day += 7

    play sound "Alarm.mp3" noloop 
    P "Oh déjà...."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te léves tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon aujourd'hui je vais demander à [E] si je peux empruntetr le gymnase."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te changes et t'approches de [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    Na "Démarrage en cours...."
    play sound "Click.mp3" noloop 

    Na "Démarrage términé, Bonjour [P]."
    play sound "Click.mp3" noloop  

    P "Bonjour [Na] comment ça va ?"
    play sound "Click.mp3" noloop 

    Na "Je vais bien et toi ?"
    play sound "Click.mp3" noloop 

    P "Je vais bien, j'ai bien dormi."
    play sound "Click.mp3" noloop 

    "{b}{i} [Na] changea de tonalité.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "[prénom], je détecte une nouvelle mise à jour pas obligatoire, veux-tu la faire maitenant ou plus tard ?"
    play sound "Menu.mp3" noloop 

    menu: 

        "{b}{i} Refuser la mise à jour {/i}{/b}" :

            $ Na = Character('[newname] [nom]', color="#0066ff")

            P "Non merci."
            play sound "Click.mp3" noloop

            Na "Ok alors."
            play sound "Click.mp3" noloop

            jump afterupdate
        
        "{b}{i} faire la mise à jour {/i}{/b}" : 
        
            Na "Bien je lance la mise à jour"
            play sound "Click.mp3" noloop

            P "Merci."
            play sound "Click.mp3" noloop

            Na "Initialisation de la mise à jour en cours."
            play sound "Click.mp3" noloop

            Na "10%"
            play sound "Click.mp3" noloop

            Na "20%"
            play sound "Click.mp3" noloop

            Na "30%"
            play sound "Click.mp3" noloop

            Na "40%"
            play sound "Click.mp3" noloop

            Na "50%"
            play sound "Click.mp3" noloop

            Na "60%"
            play sound "Click.mp3" noloop

            Na "70%"
            play sound "Click.mp3" noloop

            Na "80%" 
            play sound "Click.mp3" noloop

            Na "90%"
            play sound "Click.mp3" noloop

            Na "100%"
            play sound "Click.mp3" noloop

            Na "Vérication...."
            play sound "Menu.mp3" noloop 
            $ update += 1.0

            Na "Mise à jour terminée, la version actuelle est maintenant la [update]."
            play sound "Click.mp3" noloop 

            P "Je pense que ça devait être la mise à jour du processeur."
            play sound "Click.mp3" noloop

            Na "Oui je confirme."
            play sound "Click.mp3" noloop

label afterupdate:

    P  "Bon aujourd'hui je vais t'entraîner."
    play sound "Click.mp3" noloop 

    Na "Génial."
    play sound "Click.mp3" noloop 

    P "On y vas ?"
    play sound "Click.mp3" noloop 

    Na "Ok."
    play sound "Click.mp3" noloop 

    scene staircase 
    hide screen hallway 

    "{b}{i} Vous allez dams le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall 
    show screen hall 

    if pronom == "il":

        P "Bon on est presque arrivés."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Bon on est presque arrivées." 
        play sound "Click.mp3" noloop 

    Na "Ok."
    play sound "Click.mp3" noloop 

    scene black
    hide screen hall

    "{b}{i} Vous entrez dans le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene office
    show screen office 

    P "Bonjour c'est moi [nom]."
    play sound "Click.mp3" noloop

    E "Oh que puis-je faire pour toi ?"
    play sound "Click.mp3" noloop

    P "J'aimerais savoir si je peut emprunter le gymnase pour la matinée."
    play sound "Click.mp3" noloop

    E "Bien sûr mais puisse-je savoir pour quelle raison ?"
    play sound "Click.mp3" noloop 

    P "Pour entraîner [newname]."
    play sound "Click.mp3" noloop 

    E "Ok alors il n'y a pas de soucis."
    play sound "Click.mp3" noloop 

    "{b}{i}[E] te remit la clé du gymnase.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Merci."
    play sound "Click.mp3" noloop 

    E "De rien."
    play sound "Click.mp3" noloop 

    scene black 
    hide screen office

    "{b}{i} Puis tu quittas le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall 

    P "Bon voyons voir où se trouve le gymnase."
    play sound "Click.mp3" noloop 
    
    Na "il me semble qu'il se trouve l'ouest du campus."
    play sound "Click.mp3" noloop 

    P "Allons-y alors."
    play sound "Click.mp3" noloop 

    Na "Ok."
    play sound "Click.mp3" noloop 

    scene black 
    hide screen hall

    "{b}{i} Tu arrives enfin au gymnase.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene gymnase
    hide screen gymnase 

    P "Bon par quoi on commence ?"
    play sound "Click.mp3" noloop

    Na "Je ne sais pas vraiment c'est toi qui sais."
    play sound "Click.mp3" noloop 

    "{b}{i} Pendant que tu continues de réfléchir, [N] et [Y] entrérent dans le gymnase.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Y "Salut [prénom] comment ça va ?"
    play sound "Click.mp3" noloop 

    P "Oh salut [Y], oui ça va bien et toi ?"
    play sound "Click.mp3" noloop 

    Y "ça va bien."
    play sound "Click.mp3" noloop 

    P "Cool sinon vous faites quoi ici ?"
    play sound "Click.mp3" noloop 

    Y "je suis venue voir le gymnase car avec [N] car on a pas eu l'occasion de le faire."
    play sound "Click.mp3" noloop 

    N "oui on s'est dit que se serait une bonne idée de venir voir durant notre temps libre."
    play sound "Click.mp3" noloop 

    P "Intéressant."
    play sound "Click.mp3" noloop 

    Y "sinon je te retourne ta dérniere question toi tu fais quoi ici ?"
    play sound "Click.mp3" noloop 

    P ""
    play sound "Click.mp3" noloop 

label conversation:

    Y "Aussi, juste pour savoir... Bon, je sais que c'est important de le faire pour mon domaine et je pense aussi pour le tien, mais tu penses à faire les mises à jour de sécurité de [newname] ?"
    play sound "Click.mp3" noloop

    if update == 1.0:

        P "Il y avait une mise à jour, mais je ne l'ai pas faite. Je me suis dit que je pouvais attendre..."
        play sound "Click.mp3" noloop

        Y "Tu devrais la faire, la sécurité d'[newname] est en jeu."
        play sound "Click.mp3" noloop

        P "Oui, promis, je la ferai."
        play sound "Click.mp3" noloop
        jump suite

    elif update == 2.0:

        P "Oui, j'en avais une ce matin et je l'ai faite."
        play sound "Click.mp3" noloop
        jump suite

label suite:

    Y "Cool alors."
    play sound "Click.mp3" noloop

    N "Bon, nous, on va y retourner."
    play sound "Click.mp3" noloop

    Y "Ok alors."
    play sound "Click.mp3" noloop

    "{b}{i}[N] et [Y] quittèrent le gymnase.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon, où en étions-nous déjà ?"
    play sound "Click.mp3" noloop 

    Na "Je ne sais plus." 
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez l'entraînement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon je pense qu'on a fini pour cette matinée."
    play sound "Click.mp3" noloop 

    Na "Ok mais on peut aller manger maintenant j'ai faim."
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    scene black
    hide screen gymnase

    "{b}{i} Vous quittez le gymnase.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall 
    show screen hall

    P "Bon on se dépéche d'aller au réféctoire si tu veux manger."
    play sound "Click.mp3" noloop 

    Na "Ok alors."
    play sound "Click.mp3" noloop 

    scene black
    hide screen hall 

    "{b}{i} Vous entrez au réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
    show screen lunchroom 

    if pronom == "il":

        P "Enfin arrivés..."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 
 
        P "Enfin arrivées..."
        play sound "Click.mp3" noloop 

    Na "Oui j'ai vraiment faim."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allaz chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 700 

    P "C'est bon tu t'es servie [newname]"
    play sound "Click.mp3" noloop 

    Na "Oui c'est bon on peut aller s'asseoir."
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous Voyez [N] et [Y] à une table en train de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut [N] et [Y]."
    play sound "Click.mp3" noloop 

    N "Oh salut [prénom]."
    play sound "Click.mp3" noloop

    P "On peut venir manger avec vous ?"
    play sound "Click.mp3" noloop 

    Y "Oui bien sûr avec plaîsir."
    play sound "Click.mp3" noloop 

    P "Merci."
    play sound "Click.mp3" noloop 

    Na "Oui merci beaucoup."
    play sound "Click.mp3" noloop 

    Y "Mais de rien c'est normal entre camarades."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous vous asseyez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Sinon vous discutiez de quoi ?"
    play sound "Click.mp3" noloop 

    N "Pas grand chose, nous parlions juste de certains élèves."
    play sound "Click.mp3" noloop 

    P "Ok je vois."
    play sound "Click.mp3" noloop 

    Y "Bien sinon comment ça s'est passé au gymnase ?" 
    play sound "Click.mp3" noloop 

    P "ça s'est bien passé."
    play sound "Click.mp3" noloop 

    Y "Cool je suis content pour toi et je vois aussi qu'[newname] s'est vraiment améliorée."
    play sound "Click.mp3" noloop 

    P "Merci beaucoup."
    play sound "Click.mp3" noloop 

    Y "De rien mais je peux demander quelques choses à [newname] pour tester ces connaissances ?"
    play sound "Click.mp3" noloop 
    
    P "Bien sûr vas-y"
    play sound "Click.mp3" noloop 

    Y "Bien maintenant [newname] je veux que tu me cites toutes les décimals de pi que tu connais."
    play sound "Click.mp3" noloop 

    Na "Ok vas-y, 3.141592653589793238."
    play sound "Click.mp3" noloop 

    Y "Woah je suis vraiment surprise que tu connaisses autant de décimals de pi."
    play sound "Click.mp3" noloop 

    Na "Merci beaucoup." 
    play sound "Click.mp3" noloop 

    "{b}{i} [Y] se mit à te regarder.{/i}{/b}"
    play sound "Click.mp3" noloop

    Y "Franchement tu as vraiment appris beaucoup de choses à [newname]."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    scene black 
    hide screen lunchroom 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hall
    show screen hall 

    P "Bon on va où ?"
    play sound "Click.mp3" noloop 

label choice10:

    Na "Je crois qu'on a cours cette après-midi."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} aller en cours.{/i}{/b}" :
            jump suite1

        "{b}{i} aller à la bibliothéque.{/i}{/b}" : 

            scene black
            hide screen hall

            "{b}{i}Tu entras dans la bibliothéque.{/i}{/b}"
            play sound "Door.mp3" noloop  
            
            scene library 

            Na "Je ne suis pas sûr que c'est le moment d'être ici."
            play sound "Click.mp3" noloop   

            scene black 
            hide screen library 

            "{b}{i}Tu quittas la piéce.{/i}{/b}" 
            play sound "Door.mp3" noloop    

            scene hall
            show screen hall 

            jump choice10

label suite1:
    
    P "Ok allons-y alors."
    play sound "Click.mp3" noloop 
     
    Na "Ok je te suis alors."
    play sound "Click.mp3" noloop 

    scene staircase 
    hide screen hall 

    "{b}{i}Tu montes au premier étage avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway
    show screen hallway

    "{b}{i}Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hallway

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom  
    show screen class_404 

    H "Oh salut [prénom]"
    play sound "Click.mp3" noloop 

    P "Oh salut comment ça va ?"
    play sound "Click.mp3" noloop 

    H "Je vais bien sinon toi et [newname] ?"
    play sound "Click.mp3" noloop 

    P "Je vais bien."
    play sound "Click.mp3" noloop 

    Na "Je vais bien merci beaucoup."
    play sound "Click.mp3" noloop 

    H "De rien."
    play sound "Click.mp3" noloop 

    P "Sinon tu sais où est la [T] ?"
    play sound "Click.mp3" noloop 

    H  "Je ne sais pas mais je pense qu'elle ne va pas tarder à venir."
    play sound "Door.mp3" noloop
    
    "{b}{i} Puis la [T] entra dans la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour chers lycéens."
    play sound "Click.mp3" noloop

    H "Bonjour Madame."
    play sound "Click.mp3" noloop

    P "Bonjour."
    play sound "Click.mp3" noloop

    Na "Bonjour~"
    play sound "Click.mp3" noloop 

    I "Bonjour."
    play sound "Click.mp3" noloop

    N "Bonjour."
    play sound "Click.mp3" noloop

    "{b}{i} tous les lycéens s'asseoient à leur place.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bien aujourd'hui j'ai plusieurs choses à vous dire pour commencer."
    play sound "Click.mp3" noloop

    K "Quoi comme informations ?"
    play sound "Click.mp3" noloop

    M "J'ai entendu dire par le biais d'[E] qu'il aurait un traître dans ce lycée."
    play sound "Click.mp3" noloop

    K "Un traître ?"
    play sound "Click.mp3" noloop

    H "Comment ça un traître ?"
    play sound "Click.mp3" noloop

    P "Oui j'ai déja eu l'information mais il semblerait qu'un des lycéen en veut à [newname]."
    play sound "Click.mp3" noloop

    I "Pardon !? Soit doit sûrement être [J]...."
    play sound "Click.mp3" noloop

    J1 "Hey j'ai peut-étre était méchante avec [newname] mais je promets que ce n'est pas moi !"
    play sound "Click.mp3" noloop

    J2 "Oui ce n'est pas moi non plus."
    play sound "Click.mp3" noloop 

    P "Oui [I], actuellement on ne peut les accuser vue le peu d'information qu'on a."
    play sound "Click.mp3" noloop 

    M "Je suis d'accord avec toi [prénom]."
    play sound "Click.mp3" noloop

    P "Merci."
    play sound "Click.mp3" noloop

    M "Bon maintenant je vais vous dire la seconde information."
    play sound "Click.mp3" noloop 

    P "Oui dites-nous madame"
    play sound "Click.mp3" noloop

    M "à partir d'aujourd'hui nous allons accueillir un nouvel élève."
    play sound "Click.mp3" noloop 

    I "Qui est ce lycéen ?"
    play sound "Click.mp3" noloop

    P "Oui on veut savoir."
    play sound "Click.mp3" noloop 

    M "Deux secondes je vais le laisser entrer et se présenter."
    play sound "Click.mp3" noloop 

    I "Ok"
    play sound "Click.mp3" noloop 

    stop music fadeout 2.0  

    "{b}{i} [M] fait signe au lycéen de rentrer. {/i}{/b}"
    play sound "Door.mp3" noloop

    if key == "ARIS-GRFN-M4A1":
    
        $ S = Character('Subaru Kryuger', color="#707070") 
    
    else : 
  
        $ S = Character('Subaru Shinomiya', color="#ff8800")

    play music "Soundtrack2.mp3" loop volume 1.0
 
    R "Bonjour à tous."
    play sound "Click.mp3" noloop

    P "Bonjour à toi."
    play sound "Click.mp3" noloop

    I "Bonjour." 
    play sound "Click.mp3" noloop

    Na "Bonjour~"
    play sound "Click.mp3" noloop

    R "Merci beaucoup."
    play sound "Click.mp3" noloop

    M "Vas-y présentes-toi."
    play sound "Click.mp3" noloop

    S "Je m'appelle [S] l'ultime étudiant et ancien élève de [origine], j'ai 19 ans ravi de vous rencontrer"
    play sound "Click.mp3" noloop

    P "[S] !? Je croyais que tu étais dans un autre lycée depuis la dernière fois qu'on s'est vu !"
    play sound "Click.mp3" noloop

    I "Tu es aussi de [origine] !?" 
    play sound "Click.mp3" noloop  

    S "Oui c'est exact."
    play sound "Click.mp3" noloop 

    "{b}{i}[S] regarde autour de la salle et tombe sur toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    S "Oh c'est toi [prénom] et pour répondre à ta question, oui c'était le cas."
    play sound "Click.mp3" noloop 

    P "Mais tu fais quoi ici alors ?"
    play sound "Click.mp3" noloop 

    S "J'ai dû déménager avec ma mére du coup j'ai dû changer de lycée."
    play sound "Click.mp3" noloop 

    P "Ok je vois." 
    play sound "Click.mp3" noloop 

    S "Je vois que tu as encore l'autre [A] avec toi."
    play sound "Click.mp3" noloop 

    P "Hey un peu de respect elle a prénom et un nom maintenant."
    play sound "Click.mp3" noloop 

    S "Oups désolé."
    play sound "Click.mp3" noloop 

    "{b}{i}[S] s'addresse à [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    S "Pourrais-je savoir tu t'appelles mainteant ?"
    play sound "Click.mp3" noloop 

    Na "Je m'appelle [newname], [Na]."
    play sound "Click.mp3" noloop

    S "Enchanté [newname]"
    play sound "Click.mp3" noloop

    Na "Merci beaucoup."
    play sound "Click.mp3" noloop
    
    S "Mais de rien."
    play sound "Click.mp3" noloop

    I "Donc c'est toi l'ami de [prénom]."
    play sound "Click.mp3" noloop 

    S "Oui exactement."
    play sound "Click.mp3" noloop 

    I "Cool alors."
    play sound "Click.mp3" noloop 

    M "Dernière information, aujourd'hui vous receverrai votre budjet du mois."
    play sound "Click.mp3" noloop 

    P "Ok."
    play sound "Click.mp3" noloop 

    M "Bien Maintenant reprenons le cours, [S] je t'invite à prendre place au fond de la salle il reste une place."
    play sound "Click.mp3" noloop

    S "Merci beaucoup madame."
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Pendant que [S] se dirige vers sa place il te chuchote quelques choses.{/i}{/b}"
    play sound "Click.mp3" noloop

    S "Toi et moi on a une discussion à finir...."
    play sound "Click.mp3" noloop 

    P "euh....."
    play sound "Click.mp3" noloop 

    "{b}{i}La [T] reprend le cours.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bon sortez vos livres à la page 20, nous allons reprendre notre cours de la derniére fois."
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continua sans probléme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    M "Le cours est terminé vous pouvez quitter la salle."
    play sound "Click.mp3" noloop 

    Na "Bon [newname] on n'y va ?"
    play sound "Click.mp3" noloop 

    Na "Oui je suis fatiguée."
    play sound "Click.mp3" noloop 

    hide screen class_404
    scene black 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway 

    P "Bon cette journée est enfin finie..."
    play sound "Click.mp3" noloop 

    "{b}{i}Mais soudainement [S] t'interpelle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    S "Hey [P], Je peux te parler deux minutes."
    play sound "Click.mp3" noloop 

    P "Qu'est-ce que tu me veux Subaru ?"
    play sound "Click.mp3" noloop 

    S "C'est concernant [newname]."
    play sound "Click.mp3" noloop 

    P "Il n'y a quoi encore ?"
    play sound "Click.mp3" noloop 

    S "J'aimerais savoir pourquoi tout le monde apprécie [newname] ?"
    play sound "Click.mp3" noloop 
 
    P "Car elle est sympa et bienveillante."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        S "Comment en es-tu arrivé là ?"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        S "Comment en es-tu arrivée là ?"
        play sound "Click.mp3" noloop

    P "Je dirai que c'est de la détermination et de l'ingéniosité."
    play sound "Click.mp3" noloop 

    S "Je te hais vraiment aujourd'hui, saches-le."
    play sound "Click.mp3" noloop 

    P "Mais pourquoi !?"
    play sound "Click.mp3" noloop 
 
    S "Tu te souviens qu'on était à [origine] à l'époque ?" 
    play sound "Click.mp3" noloop 

    P "Oui pourquoi ?"
    play sound "Click.mp3" noloop 

    S "à [origine] j'étais le meilleur et tout le monde m'acclamait pendant que tu restais dans ton coin."
    play sound "Click.mp3" noloop 

    P "Oui et alors ?"
    play sound "Click.mp3" noloop 

    S "Depuis que tu as découvert [newname] j'ai perdu une partie de ma popularité car soit disant j'était une fraude."
    play sound "Click.mp3" noloop 

    P "Et alors personnellement ça ne me concerne pas."
    play sound "Click.mp3" noloop 

    S "Même quand je suis allé à Lexus après avoir finis mon cursus à [origine], cette histoire m'a suivie."
    play sound "Click.mp3" noloop 

    P "OK je vois maintement."
    play sound "Click.mp3" noloop 

    S "Tu comprends maintenant pourquoi je dêteste."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Désolé je ne voulais pas te causer ça."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Désolée je ne voulais pas te causer ça."
        play sound "Click.mp3" noloop 

    S "Ouais ouais bon je te laisse je dois y aller."
    play sound "Click.mp3" noloop 

    P "Ok à plus tard." 
    play sound "Footsteps.mp3" noloop  

    "{b}{i}[S] s'éloigna pour aller à son dortoir et en même [J1] vient vers toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    J1 "Hey salut [prénom] je veux juste m'excuser pour tous ce que j'ai dit à [newname]..."
    play sound "Click.mp3" noloop  

    Na "[J1] désolée mais ce n'est vraiment pas le moment de discuter, [prénom] vient d'avoir une discussion douloureuse avec [S]."
    play sound "Click.mp3" noloop 

    J1 "Oh désolée je ne voulais pas déranger." 
    play sound "Click.mp3" noloop  

    Na "Ok pas de soucis mais tu devrais partir d'ici" 
    play sound "Footsteps.mp3" noloop  

    "{b}{i}[J1] s'éloigna aussi.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon [prénom] on part au dortoir." 
    play sound "Click.mp3" noloop  

    P "Ok...." 
    play sound "Click.mp3" noloop  

    scene black
    hide screen hallway

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room 

    P "Enfin au dortoir." 
    play sound "Click.mp3" noloop  

    Na "Oui ça fait du bien." 
    play sound "Click.mp3" noloop  

    P "Bon je ne sais pas quoi faire maintenant." 
    play sound "Click.mp3" noloop  

    Na "Tu pouurais te renseigner sur cette histoire de traître." 
    play sound "Click.mp3" noloop  

    P "Oui mais le problème c'est qu'on n'a aucune information." 
    play sound "Click.mp3" noloop  
    
    Na "C'est vrai tu as raison mais tu peux peut-être regarder dans la boite du jeu pour trouver des indices."
    play sound "Click.mp3" noloop

    Na "Oh désolée j'avais oublié que c'est un jeu dématérialisé."
    play sound "Click.mp3" noloop

    P "Bon on est aussi sensé recevoir notre budjet du mois aujourd'hui." 
    play sound "Click.mp3" noloop  

    Na "Oui c'es vrai c'est aujourd'hui." 
    play sound "Click.mp3" noloop  

    P "ça va sûrement venir dans la soirée." 
    play sound "Click.mp3" noloop  

    Na "je pense aussi mais Bon moi je vais me déconnecter, à demain." 
    play sound "Click.mp3" noloop  

    P "Ok à demain [newname]." 
    play sound "Click.mp3" noloop  

    if grade == 20.0:

        $ points += 10000

    else:

        $ points += 7500

    "{b}{i}Pui [newname] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh je vois que j'ai reçu mon budget." 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changea avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen room
    hide screen day

    "{b}{i} Le lendemain matin.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room 
    show screen room
    show screen day
    $ day += 1

    play sound "Alarm.mp3" noloop 
    P "Oh super mais bon il faut bien se lever à un moment."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te léves tranquillement et te changes tranquillement et pars voir [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 
    
    P "Je vais la démarrer sinon on va étre en retard"
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    Na "Démarrage en cours......"
    play sound "Click.mp3" noloop 

    Na "Bonjour [prénom]."
    play sound "Click.mp3" noloop 

    P "Coucou comment ça va aujourd'hui ?"
    play sound "Click.mp3" noloop

    Na "Je vais bien et ça va ?"
    play sound "Click.mp3" noloop 

    P "Je vais bien, j'ai bien dormi."
    play sound "Click.mp3" noloop  

    Na "Cool mais juste hier j'avais oublié de te dire un truc."
    play sound "Click.mp3" noloop

    P "Oui dit-moi, je t'écoute"
    play sound "Click.mp3" noloop

    Na  "tu sais [prénom] tu t’occupes tellement bien de moi que je pourrais te surnommer undertaker."
    play sound "Click.mp3" noloop 

    P "Undertaker !?"
    play sound "Click.mp3" noloop

    Na "Oui c'est bien ça."
    play sound "Click.mp3" noloop

    P "Merci beaucoup ça fait plaisir de l'entendre."
    play sound "Click.mp3" noloop

    Na "De rien."
    play sound "Click.mp3" noloop

    P "Bon on doit aller en cours avant d'étre en retard."
    play sound "Click.mp3" noloop

    Na "Ok je te suis."
    play sound "Click.mp3" noloop 

    Na "Bien alors allons-y."
    play sound "Click.mp3" noloop

    scene black
    hide screen room

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway
    show screen hallway

    "{b}{i} Tu continues vers la salle de classe mais tu croises [S].{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Oh salut [S]."
    play sound "Click.mp3" noloop

    S "Oh salut [prénom]......"
    play sound "Click.mp3" noloop

    P "Comment ça va ?"
    play sound "Click.mp3" noloop

    S "ça va..."
    play sound "Click.mp3" noloop

    "{b}{i} [S] ignore la discussion et part en classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu sais ce qu'il a ou pas ?"
    play sound "Click.mp3" noloop

    Na "Je n'en ai aucune idée."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop 
    
    scene black
    hide screen hallway

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom  
    show screen class_404 

    P "Salut..."
    play sound "Click.mp3" noloop

    Hi "Salut comment ça va toi et [newname]?"
    play sound "Click.mp3" noloop

    P "Je vais bien "
    play sound "Click.mp3" noloop

    Na "Je vais bien toi [Hi]"
    play sound "Click.mp3" noloop

    Hi "Cool alors..."
    play sound "Door.mp3" noloop
    
    "{b}{i}Puis la [T] entre dans la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour."
    play sound "Click.mp3" noloop

    Hi "Bonjour Madame."
    play sound "Click.mp3" noloop

    P "Bonjour."
    play sound "Click.mp3" noloop

    Na "Bonjour."
    play sound "Click.mp3" noloop
    
    M "Bon aujourd'hui nous allons voir un nouveau sujet grammaire et je m'excuse [S] si tu as ratée le sujet sur la guerre."
    play sound "Click.mp3" noloop

    S "Il n'y a pas soucis de toute façon j'avais déjà vu ce sujet à Lexus."
    play sound "Click.mp3" noloop

    M "Au temps pour moi alors."
    play sound "Click.mp3" noloop

    S "Il n'y a pas de soucis."
    play sound "Click.mp3" noloop

    M "Bon Commençons, sortez vos livres de mathématique page 15."
    play sound "Click.mp3" noloop

    M "Le cours d'aujourd'hui sera sur le théorème de Pythagore." 
    play sound "Click.mp3" noloop

    P "Ok."
    play sound "Click.mp3" noloop

    M "Bon qui peut me dire ce qu'est le théorème de Pythagore ?"
    play sound "Click.mp3" noloop 

    I "moi s'il vous plaît."
    play sound "Click.mp3" noloop

    M "Bien expliques-nous."
    play sound "Click.mp3" noloop

    I "Le théorème de Pythagore permet de trouver la valeur de l'hypothénuse apartir des deux plus petits cotés d'un triangle."
    play sound "Click.mp3" noloop
    
    M "Excellent sinon qui peut me donner la formule de calcul ?"
    play sound "Click.mp3" noloop

    Na "Moi s'il vous plaît."
    play sound "Click.mp3" noloop

    M "Bien expliques-nous."
    play sound "Click.mp3" noloop 

    Na "Il suffit d'additionner les carrés des deux plus petits cotés puis faire la racine du résultat pour trouver l'hypothénus."
    play sound "Click.mp3" noloop

    M "Bien merci pour cette explication."
    play sound "Click.mp3" noloop

    Na "Merci beaucoup."
    play sound "Click.mp3" noloop

    "{b}{i}Puis la [T] commence à écrire sur le tableau.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bon si le premier coté fait 5 centimètres et le deuxième 12 centimètres, que vaut l'hypothénuse ?"
    play sound "Click.mp3" noloop

    "{b}{i} Tous les élèves se mettent à réfléchir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bon qui peut me donner la réponse ?"
    play sound "Click.mp3" noloop

    Na "Moi s'il vous plait"
    play sound "Click.mp3" noloop

    M "Bien je t'écoute"
    play sound "Click.mp3" noloop

    Na "Le résultat de l'hypothéuse est 13 centimétres."
    play sound "Click.mp3" noloop

    M "Exact bien trouvé."
    play sound "Click.mp3" noloop

    Na "Merci."
    play sound "Click.mp3" noloop

    M "Bien maintenant que vous avez compris, je vous laisse faire les exercices à la page 16."
    play sound "Click.mp3" noloop

    S "Ok."
    play sound "Click.mp3" noloop

    "{b}{i} Tous les élèves se mettent à faire les exercices.{/i}{/b}"
    play sound "Click.mp3" noloop 

    "{b}{i} Une heure plus tard.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    hide screen class_404
    scene black

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
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

    M "Bien reprenez les exercices et demandez-moi de l'aide si vous avez besoin d'aide."
    play sound "Click.mp3" noloop

    S "On n'aura pas besoin d'aide Madame on est quand même l'élite"
    play sound "Click.mp3" noloop

    I "[S], tu ferais pas un peu le surdoué par hasard ?"
    play sound "Click.mp3" noloop

    S "Euh......"
    play sound "Click.mp3" noloop

    M "Evitez de bavarder."
    play sound "Click.mp3" noloop

    S "Oui Madame."
    play sound "Click.mp3" noloop

    "{b}{i}Le cours continua sans probléme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    M "Le cours est terminé vous pouvez quitter la salle."
    play sound "Click.mp3" noloop 

    P "Bon [newname] on va manger ?"
    play sound "Click.mp3" noloop

    Na "Uoi pas de soucis"
    play sound "Click.mp3" noloop

    hide screen class_404
    scene black 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway 

    "{b}{i} Tu continues vers le rez de chaussée.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene staircase
    hide screen hallway 

    "{b}{i} Tu continues vers le hall.{i}{/b}"
    play sound "Click.mp3" noloop

    scene hall
    show screen hall

    "{b}{i} Tu continues vers le réféctoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hall 

    "{b}{i} Tu entres dasn le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene lunchroom
    show screen lunchroom

    if pronom == "il":

        P "Enfin arrivés..."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 
 
        P "Enfin arrivées..."
        play sound "Click.mp3" noloop 

    Na "Oui j'ai vraiment faim."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allaz chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 700 

    P "C'est bon tu t'es servie [newname]"
    play sound "Click.mp3" noloop 

    Na "Oui c'est bon on peut aller s'asseoir."
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allez vous rejoindre [I] pour manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Coucou [I]."
    play sound "Click.mp3" noloop 

    I "Oh salut comment vous allez ?"
    play sound "Click.mp3" noloop 

    Na "Je vais bien..."
    play sound "Click.mp3" noloop 

    P "Je vais bien aussi et toi ?"
    play sound "Click.mp3" noloop 

    I "Oui je vais bien."
    play sound "Click.mp3" noloop 

    P "Cool alors."
    play sound "Click.mp3" noloop 

    "{b}{i} Puis soudainement [S] viens vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oui qu'est-ce que tu veux ?"
    play sound "Click.mp3" noloop 

    S "Je voulais savoir si je pouvais venir manger avec vous ? Car vous êtez les seules personnes que je connaisse."
    play sound "Click.mp3" noloop 

    Na "Euh....."
    play sound "Click.mp3" noloop 

    P "Tu veux vraiment être avec nous !?"
    play sound "Click.mp3" noloop 

    S "Oui Car je ne connais personne d'autres."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Accepter [S]{/i}{/b}" :
    
            P "Bien sûr viens t'asseoir avec nous."
            play sound "Click.mp3" noloop 

            Na  "Vraiment ?"
            play sound "Click.mp3" noloop 

            P "Oui pourquoi pas."
            play sound "Click.mp3" noloop      

            Na "Ok alors c'est toi qui vois"
            play sound "Click.mp3" noloop 

            S "Merci beuucoup."
            play sound "Click.mp3" noloop 

            I  "De rien."
            play sound "Click.mp3" noloop 

            "{b}{i} Vous vous mettez à discuter des cours.{/i}{/b}"
            play sound "Click.mp3" noloop

            I  "Sinon vous pensez qu'on aura quoi comme cours cette après-midi ?"
            play sound "Click.mp3" noloop 

            Na "Je ne sais pas mais je pense qu'on aura encore cours de math."
            play sound "Click.mp3" noloop 

            S "Math encore !?"
            play sound "Click.mp3" noloop 

            P  "Oui c'est très probable."
            play sound "Click.mp3" noloop 

            S "Ok alors."
            play sound "Click.mp3" noloop 

            "{b}{i} Vous continuez de discuter des cours jusqu'à la sonnerie.{/i}{/b}"
            play sound "Bell.mp3" noloop

            I "Bon on retourne en classe ?"
            play sound "Click.mp3" noloop 

            S "Ok."
            play sound "Click.mp3" noloop      

            P "Ok."
            play sound "Click.mp3" noloop       

            Na "Ok allons-y"
            play sound "Click.mp3" noloop 

        "{b}{i} Refuser [S]{/i}{/b}" : 

            if pronom == "il":

                P "Désolé mais je préfére rest avec [newname] et [I]"
                play sound "Click.mp3" noloop

            elif pronom == "elle": 

                P "Désolée mais je préfére rester avec [newname] et [I]"
                play sound "Click.mp3" noloop  

            S "Ok alors je comprend c'est ton choix."
            play sound "Click.mp3" noloop 

            "{b}{i} Puis [S] s'éloigna et s'asseoit à une autre table.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Il est enfin parti."
            play sound "Click.mp3" noloop 

            Na "Oui enfin."
            play sound "Click.mp3" noloop 

            "{b}{i} Vous vous mettez à discuter des cours.{/i}{/b}"
            play sound "Click.mp3" noloop

            I  "Sinon vous pensez qu'on aura quoi comme cours cette après-midi ?"
            play sound "Click.mp3" noloop 

            Na "Je ne sais pas mais je pense qu'on aura encore cours de math."
            play sound "Click.mp3" noloop 

            P "ça m'etonnerai qu'on aie encore math."
            play sound "Click.mp3" noloop            

            "{b}{i} Vous continuez de discuter des cours jusqu'à la sonnerie.{/i}{/b}"
            play sound "Bell.mp3" noloop

            I "Bon on retourne en classe ?"
            play sound "Click.mp3" noloop 

            P "Ok."
            play sound "Click.mp3" noloop       

            Na "Ok allons-y"
            play sound "Click.mp3" noloop 

    scene black
    hide screen lunchroom

    "{b}{i}Tu te diriges vers le hall.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hall
    show screen hall 

    "{b}{i}Tu continues vers le premier étage.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene staircase
    hide screen hall 

    "{b}{i}Tu continues vers le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway
    show screen hallway

    "{b}{i}Tu continue vers la salle de la classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene main
    hide screen hallway

    play music "Transition.mp3" noloop 

    "{b}{i}Chapitre 1.01 : Arisization Project - Start The Debate{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene black 

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom  
    show screen class_404  

    M "Bonjour dans ce cours nous allons faire quelques choes de spécial."
    play sound "Click.mp3" noloop 

    I "Quoi exactement ?"
    play sound "Click.mp3" noloop 

    P "Oui quoi exactement ?"
    play sound "Click.mp3" noloop 

    Na "On peut savoir ?"
    play sound "Click.mp3" noloop 

    M "On va faire un débat sur les intelligences artificielles et les robots humanoides."
    play sound "Click.mp3" noloop 

    J1 "Vraiment un débat sur ça."
    play sound "Click.mp3" noloop 

    J2 "Oui ça peut être intéressant."
    play sound "Click.mp3" noloop 

    "{b}{i}La [T] commença à écrire sur le tableau.{/i}{/b}"
    play sound "Click.mp3" noloop 
    
    M "Bon j'aimerai que vous déplacez les tables pour avoir de l'espace."
    play sound "Click.mp3" noloop 

    Na "Ok."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous mettez à déplacer les tables et les chaises.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bien maintenant pour commencer j'aimerai que tous ceux qui sont pour ces innovations se mettent à droite et ceux qui sont contre se mettent à gauche."
    play sound "Click.mp3" noloop 

    P "Ok alors bon je sais déja que je suis pour."
    play sound "Click.mp3" noloop 

    Na "Madame si jamais je ne donnerai pas mon vote vue que je suis déjà un [model]."
    play sound "Click.mp3" noloop 

    M "Ok c'est compréhensible." 
    play sound "Click.mp3" noloop 

    J1 "Au moins ça fera un vote en moins."
    play sound "Click.mp3" noloop 

    P "Tu n'es pas drôle [J1]..."
    play sound "Click.mp3" noloop 

    J1 "Oh c'est bon."
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde choisi son camp.{/i}{/b}"
    play sound "Click.mp3" noloop   

    M "Bien voyons voir quel camp vous avez choisi."
    play sound "Click.mp3" noloop 

    M "D'abord le camp qui s'oppose à ces innovations."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes le camp d'en face et tu vois [J1], [J2], [S] et [K]{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Pardon [K], toi aussi tu t'opposes à ces innovations !?"
    play sound "Click.mp3" noloop

    K "C'est pas contre [newname] mais en générale je ne suis pas pour ces technologies."
    play sound "Click.mp3" noloop

    P "Ok je vois."
    play sound "Click.mp3" noloop 

    M "Bien maintenant voyons le camp qui sont pour ces innovations."
    play sound "Click.mp3" noloop 
 
    "{b}{i}Tu regardes ton camp et tu vois les autres qui sont dans avec toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "On dirait qu'il y a 6 lycéens qui sont pour ces innovations."
    play sound "Click.mp3" noloop 

    M "Donc ça fait 6 qui sont pour et 4 qui sont contre."
    play sound "Click.mp3" noloop 

    J1 "Sérieusement..."
    play sound "Click.mp3" noloop 

    M "Oui."
    play sound "Click.mp3" noloop 

    J1 "Ok je vois."
    play sound "Click.mp3" noloop

    M "Bien maintenant j'aimerai que chaque camp choisisse quelqu'un pour débattre dans chaque camp."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu commences à discuter pour savoir qui choisir.{/i}{/b}"
    play sound "Click.mp3" noloop   

    play music "Soundtrack2.mp3" loop volume 1.0

    P "Bon on choisi qui pour débattre ?"
    play sound "Click.mp3" noloop 

    I "Je ne sais pas, tu as une idée [Y] ?"
    play sound "Click.mp3" noloop 

    Y "je pense savoir qui choisir..."
    play sound "Click.mp3" noloop 

    H "Ah bon c'est qui ? "
    play sound "Click.mp3" noloop  

    N "Oui dit-nous."
    play sound "Click.mp3" noloop 

    Hi "On veut savoir."
    play sound "Click.mp3" noloop 

    Y "Je pense que la réponse est évident."
    play sound "Click.mp3" noloop 

    I "Vraiment !?"
    play sound "Click.mp3" noloop 

    Y "Oui il faudrait choisir [prénom]."
    play sound "Click.mp3" noloop 

    N "Oui c'est vrai [pronom] a déjà de l'experience avec ces sujets."
    play sound "Click.mp3" noloop 

    I "Oui je confirme."
    play sound "Click.mp3" noloop 

    Y "Donc c'est décidé, [prénom] tu seras choisi."
    play sound "Click.mp3" noloop 

    P  "OK vous pouvez compter sur moi pour gagner ce débat."
    play sound "Click.mp3" noloop 

    Y "Bien alors."
    play sound "Click.mp3" noloop 

    I "Madame c'est bon nous avons choisi."
    play sound "Click.mp3" noloop 

    M "Bien et vous de votre coté ?"
    play sound "Click.mp3" noloop 

    J1 "Nous aussi nous avons choisi."
    play sound "Click.mp3" noloop 

    M "Bien."
    play sound "Click.mp3" noloop 

    J1 "On va vous battre dans ce débat."
    play sound "Click.mp3" noloop 

    M "Bien les personnes dans chaque équipe ont été choisis."
    play sound "Click.mp3" noloop 

    M "Dans ce débat [P] et [S]"
    play sound "Click.mp3" noloop 

    I "Les deux anciens élèves de [origine] qui s'affrontent, ça risque d'être intéressant."
    play sound "Click.mp3" noloop 

    Y "Oui je confirme"
    play sound "Click.mp3" noloop 

label debate:

    M "Bon [S] commence, dis nous pourquoi tu es contre."
    play sound "Click.mp3" noloop 

    S "Pour commencer je trouve que les robots humanoïdes ne servent qu'à faire des calculs mathématiques."
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Les cours. {/i}{/b}" :

            P "Non ils peuvent aussi aider pour les cours."
            play sound "Click.mp3" noloop 

            S "Pour les cours !?."
            play sound "Click.mp3" noloop 

            P "Oui."
            play sound "Click.mp3" noloop 

            S "Ce n'est pas considéré comme de la triche !?"
            play sound "Click.mp3" noloop 

            P "Non."
            play sound "Click.mp3" noloop            
            
            S "Je ne suis pas convaincu de cet argument...."
            play sound "Click.mp3" noloop 

            scene black
            hide classroom
            hide screen class_404
            hide screen points
            hide screen day
            play music "gameover.mp3" noloop
            "{b}{i}Fin numéro 7 : Débat complétement perdu face à [S].{/i}{/b}"
            play sound "Menu.mp3" noloop

            menu:    

                "{b}{i}Abandonner{/i}{/b}" :
                    return 
                "{b}{i}Réessayer.{/i}{/b}" :
                    show classroom
                    show screen class_404
                    show screen points
                    show screen day
                    play music "Soundtrack.mp3" loop volume 1.0
                    jump debate

        "{b}{i} citez d'autres domaines.{/i}{/b}" : 
            
            P "OBJECTION !!!"
            play sound "Click.mp3" noloop 

    S "Pardon !?"
    play sound "Click.mp3" noloop 

    P "Oui les robots humanoïdes peuvent faire plein de truc."
    play sound "Click.mp3" noloop 

    S "Ah oui et quoi d'autres comme truc !?."
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} la guerre {/i}{/b}" :

            P "Non ils peuvent aussi aider pour la guerre."
            play sound "Click.mp3" noloop 

            S "Pour la guerre !?."
            play sound "Click.mp3" noloop 

            P "Oui."
            play sound "Click.mp3" noloop 

            S "On gros pour notre situation actuelle."
            play sound "Click.mp3" noloop 

            P "euh......"
            play sound "Click.mp3" noloop            
            
            S "Je ne suis pas convaincu de cet argument...."
            play sound "Click.mp3" noloop 

            scene black
            hide classroom
            hide screen class_404
            hide screen points
            hide screen day
            play music "gameover.mp3" noloop
            "{b}{i}Fin numéro 7 : Débat complétement perdu face à [S].{/i}{/b}"
            play sound "Menu.mp3" noloop

            menu:    

                "{b}{i}Abandonner{/i}{/b}" :
                    return 
                "{b}{i}Réessayer.{/i}{/b}" :
                    show classroom
                    show screen class_404
                    show screen points
                    show screen day
                    play music "Soundtrack.mp3" loop volume 1.0
                    jump debate

        "{b}{i} l'administratif {/i}{/b}" :

            P "L'administractif par exemple."
            play sound "Click.mp3" noloop 

    S "Je ne comprend pas."
    play sound "Click.mp3" noloop 

    P "Pour remplir des documents administratifs"
    play sound "Click.mp3" noloop 

    S "OK mais on risque de perdre des emplois si les robots humanoïdes font le travail à notre place."
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Corriger [S] {/i}{/b}" : 

            P "Permet-moi de te corriger."
            play sound "Click.mp3" noloop 

    S "Vas-y."
    play sound "Click.mp3" noloop 

    P "On ne va perdre d'emplois, on va juste créer des besoins aillleur."
    play sound "Click.mp3" noloop 

    S "Ou par exemple ?"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Maintenance spécialisée {/i}{/b}" : 

            P "Dans la maintenance des robots humanoïdes déjà."
            play sound "Click.mp3" noloop 

    S "Pardon ?"
    play sound "Click.mp3" noloop 

    P "Bah oui il faudra bien entrenir les robots humanoïdes."
    play sound "Click.mp3" noloop 

    S "Ok je vois mais les robots humanoïdes obeisseent à leur créateur."
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Contester {/i}{/b}" : 

            P "Non ils ont aussi leur propre le propre conscience et façon d'agir."
            play sound "Click.mp3" noloop 

    S "Tu es serieux !?"
    play sound "Click.mp3" noloop 

    P "Oui"
    play sound "Click.mp3" noloop 

    S "Prouve-le alors"
    play sound "Click.mp3" noloop 

    P "Ok."
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Expliquer au tableau {/i}{/b}" : 

            "{b}{i} tu commences à expliquer au tableau.{/i}{/b}"
            play sound "Click.mp3" noloop 
            
            P "Tu vois un peu mieux"
            play sound "Click.mp3" noloop 

            S "Je ne suis pas convaincu par cette explication...."
            play sound "Click.mp3" noloop 

            scene black
            hide classroom
            hide screen class_404
            hide screen points
            hide screen day
            play music "gameover.mp3" noloop
            "{b}{i}méro 7 : Débat complétement perdu face à [S].{/i}{/b}"
            play sound "Menu.mp3" noloop

            menu:    

                "{b}{i}Abandonner{/i}{/b}" :
                    return 
                "{b}{i}Réessayer.{/i}{/b}" :
                    scene black
                    show screen points 
                    play music "Soundtrack.mp3" loop volume 1.0
                    jump debate

        "{b}{i} Pointer [newname]{/i}{/b}" : 

            P "[newname] ici présente est la représentation de toutes les arguments que j'ai dit jusqu'à maintenant."
            play sound "Click.mp3" noloop 

    Na "Moi !?"
    play sound "Click.mp3" noloop 

    I "Tu te défends bien [prénom]."
    play sound "Click.mp3" noloop 

    "{b}{i}Le débat continua jusqu'à la fin du cours.{/i}{/b}"
    play sound "Bell.mp3" noloop   

    M "Le cours est terminé vous pouvez quitter la salle."
    play sound "Click.mp3" noloop 

    P "Bon on retourne au dortoir [newname] ?"
    play sound "Click.mp3" noloop 

    Na "Oui."
    play sound "Click.mp3" noloop 

    hide screen class_404
    scene black 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway 

    if pronom == "il":

        Na "Tu sais tu t'es vraiment bien débrouillé [prénom]."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        Na "Tu sais tu t'es vraiment bien débrouillée [prénom]."
        play sound "Click.mp3" noloop 
 
    P "Merci beaucoup"
    play sound "Click.mp3" noloop 

    Na "Mais de rien."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hallway 

    "{b}{i} Vous entrez dans le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room

    if pronom == "il":

        P "Enfin je suis fatigué."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        P "Enfin je suis fatiguée."
        play sound "Click.mp3" noloop 

    Na "Moi aussi..."
    play sound "Click.mp3" noloop 

    P "Tu rigoles j'espére..."
    play sound "Click.mp3" noloop 

    Na "Je tiens à te rappeler que j'ai dû expliquer un cours de math."
    play sound "Click.mp3" noloop 

    P "Moi j'ai dû argumenter toute une après-midi contre ce [S]."
    play sound "Click.mp3" noloop 

    Na "Ok tu marques un point."
    play sound "Click.mp3" noloop 

    P "Bon moi je vais me poser un peu."
    play sound "Click.mp3" noloop 

    Na "Ok moi je vasi me déconnecter."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bien bon je vais me poser un peu pour lire."
    play sound "Click.mp3" noloop 

    "{b}{i} tu te poses tranqauillement mais tu reçois soudainement un appel.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oui bonjour qui est-ce à l'appareil ?"
    play sound "Click.mp3" noloop 

    Su "C'est [Su]."
    play sound "Click.mp3" noloop 

    P "Oh salut comment ça va ?"
    play sound "Click.mp3" noloop 

    Su "Je vais bien et toi ?"
    play sound "Click.mp3" noloop 

    P "Je vais bien sinon pourquoi tu m'appelles ?"
    play sound "Click.mp3" noloop 

    Su "Je voulais avoir de tes nouvelles car on n'a jamais discuter après [origine]."
    play sound "Click.mp3" noloop 

    P "Oui c'est vrai sinon tu fais quoi ?"
    play sound "Click.mp3" noloop 

    Su "Je suis à l'internat de Lexus."
    play sound "Click.mp3" noloop 

    P "Tu es à Lexus ?"
    play sound "Click.mp3" noloop 

    Su "Oui c'est exact."
    play sound "Click.mp3" noloop 

    Su "Cool alors."
    play sound "Click.mp3" noloop 

    Su "Merci sinon comment elle va [A] ?"
    play sound "Click.mp3" noloop 

    P "elle va bien elle est juste déconnectée et je lui ai trouvé un magnifique prénom."
    play sound "Click.mp3" noloop

    Su "Ah bon le quel ?"
    play sound "Click.mp3" noloop 

    P "[newname]"
    play sound "Click.mp3" noloop 

    Su "C'est trop mignon."
    play sound "Click.mp3" noloop 

    P "Merci beaucoup."
    play sound "Click.mp3" noloop 

    Su "De rien et je voulais te demander quelques choses."
    play sound "Click.mp3" noloop 

    P "Oui dis-moi."
    play sound "Click.mp3" noloop 

    Su "Comment va [S] vu que maintenant qu'il est à Nexus ?"
    play sound "Click.mp3" noloop 

    P "Ah lui, il va bien mais il est juste fatiguant."
    play sound "Click.mp3" noloop 

    Su "Ok je vois comme d'habitude."
    play sound "Click.mp3" noloop 

    P "Sinon des nouvelles de [Sk] ?"
    play sound "Click.mp3" noloop 

    Su "Il était à Lexus avec nous mais il a disparu sans laisser de nouvelles au bout de trois semaines après la rentrée..."
    play sound "Click.mp3" noloop 

    P "Pardon quoi !?"
    play sound "Click.mp3" noloop 

    Su "Oui malheureusement...."
    play sound "Click.mp3" noloop

    P "Mince....."
    play sound "Click.mp3" noloop 

    Su "Bon je dois te laisser."
    play sound "Click.mp3" noloop 

    P "Ok à une autre fois."
    play sound "Click.mp3" noloop 

    Su "Aucun probléme on se rappelera un de ces jours."
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i} [Su] finit par raccrocher.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon enfin fini je vais pouvoir aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changea avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen room
    hide screen day

    "{b}{i} Le lendemain matin.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room 
    show screen room
    show screen day
    $ day += 1

    play sound "Alarm.mp3" noloop 
    P "Oh super....."
    play sound "Click.mp3" noloop 
 
    "{b}{i} Tu te léves tranquillement et te changes tranquillement et pars voir [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    Na "Démarrage en cours......"
    play sound "Click.mp3" noloop 

    Na "Bonjour [prénom]."
    play sound "Click.mp3" noloop 

    P "Coucou comment ça va aujourd'hui ?"
    play sound "Click.mp3" noloop

    Na "Je vais bien et ça va ?"
    play sound "Click.mp3" noloop 

    P "Je vais bien, j'ai bien dormi."
    play sound "Click.mp3" noloop  

    Na "Cool alors."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu reçois soudainement un message de [Su].{/i}{/b}"
    play sound "Click.mp3" noloop 

    menu: 

        "{b}{i} Ouvrir le message.{/i}{/b}":
            
            P "Bon voyons voir ce que [Su] m'a envoyé."
            play sound "Click.mp3" noloop 

            "{b}{i} Tu ouvres le message.{/i}{/b}"
            play sound "Click.mp3" noloop

            show screen draw

            "{i} Salut [prénom], hier j'avais oublié de te dire mais j'avais fait un dessin d'[newname] tiens c'est cadeau.{/i}"
            play sound "Click.mp3" noloop

            hide screen draw

            P "[newname] regardes le magnifique dessin que [Su] a fait pour toi."
            play sound "Click.mp3" noloop

            Na "Oh c'est magnifique"
            play sound "Click.mp3" noloop

            P "Cool que le dessin te plaise."
            play sound "Click.mp3" noloop 

        "{b}{i} Ignorer le message.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            Na "Tu ne regardes pas le message ?"
            play sound "Click.mp3" noloop 
 
            P "Non pour l'instant."
            play sound "Click.mp3" noloop 

    Na "Bon on va en cours ?"
    play sound "Click.mp3" noloop 

    P "Oui."
    play sound "Click.mp3" noloop 

    Na "Ok je te suis alors."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    hide screen room 
    scene black
    play sound "Click.mp3" noloop 

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway 
    show screen hallway 
    play sound "Door.mp3" noloop 

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hallway

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom  
    show screen class_404 

    "{b}{i} Quand tu rentres en classe [S] vient vers toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    S "Hey [prénom] je peux te parler deux minutes s'il te plait ?"
    play sound "Click.mp3" noloop 

    P "Pourquoi faire !?"
    play sound "Click.mp3" noloop 

    S "Je trouve que tu fais un trop malin."
    play sound "Click.mp3" noloop 

    P "Comment ça ?"
    play sound "Click.mp3" noloop 

    S "Je trouve qu'améliorer un [model] est facile par rapport à ce que tu dis."
    play sound "Click.mp3" noloop 

    P "Je t'arrète toute de suite !!!"
    play sound "Click.mp3" noloop 
   
    S "Pardon !?"
    play sound "Click.mp3" noloop 

    P "Oui va coder et programmer en Assembleur et on verra si c'est facile."
    play sound "Click.mp3" noloop 

    "{b}{i}[S] s'éloigna....{/i}{/b}"
    play sound "Door.mp3" noloop

    "{b}{i} La [T] entra dans la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour."
    play sound "Click.mp3" noloop

    S "Bonjour Madame."
    play sound "Click.mp3" noloop

    P "Bonjour."
    play sound "Click.mp3" noloop

    A "Bonjour."
    play sound "Click.mp3" noloop

    M "Bien aujourd'hui nous allons continuez le cours sur Pythagore."
    play sound "Click.mp3" noloop

    P "Ok."
    play sound "Click.mp3" noloop

    M "Sortez votre livre de math page 12."
    play sound "Click.mp3" noloop

    "{b}{i} Tout le monde sorte le livre.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Je vous laisse faire les exercices."
    play sound "Click.mp3" noloop 

    "{b}{i} Tout le monde fait les exercices.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon voyons voir...."
    play sound "Click.mp3" noloop

    "{b}{i} Tout le monde fait les exercices mais soudainement tu te sens mal.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Purée...."
    play sound "Click.mp3" noloop

    Na "[prénom] tu vas bien ?"
    play sound "Click.mp3" noloop

    P "Oui ça va."
    play sound "Click.mp3" noloop

    Na "Ok."
    play sound "Click.mp3" noloop

    "{b}{i}Tu commences à sentir ta tête tourner et ta vision devient floue. Le bruit ambiant de la salle de classe semble s’éloigner.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Attends... Je crois que..."
    play sound "Stumble.mp3" fadeout 3.0

    "{b}{i}Ton corps ne tient plus, et tu t'effondres à genoux. Des exclamations inquiètes remplissent la pièce.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "[prénom] !! Hé, reste avec moi !"
    play sound "Click.mp3" noloop

    "{b}{i}Tu perçois vaguement la voix d'[newname] au loin avant que tout devienne noir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black 
    hide screen class_404 

    if pronom == "il":

        "{b}{i}Quelques instants plus tard, tu te réveilles dans ta chambre, couché sur ton lit.{/i}{/b}"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        "{b}{i}Quelques instants plus tard, tu te réveilles dans ta chambre, couchée sur ton lit.{/i}{/b}"
        play sound "Click.mp3" noloop

    scene room
    show screen room 

    P "Où... où suis-je ?"
    play sound "Click.mp3" noloop

    "{b}{i}Une voix douce mais ferme te répond, te tirant un peu plus de ton état confus.{/i}{/b}"
    play sound "Click.mp3" noloop

    if pronom == "il":

        Na "Tu es dans ta chambre. Tu t’es évanoui en classe, mais ne t'inquiète pas, Iris et moi t’avons accompagné jusqu’ici."
        play sound "Click.mp3" noloop 

    elif pronom == "elle": 

        Na "Tu es dans ta chambre. Tu t’es évanouie en classe, mais ne t'inquiète pas, Iris et moi t’avons accompagné jusqu’ici."
        play sound "Click.mp3" noloop 

    P "[I]...?"
    play sound "Click.mp3" noloop

    "{b}{i}Tu te retournes légèrement, et vois [I] assis sur une chaise à côté du lit, un regard inquiet posé sur toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Je suis là. Sérieusement, tu m’as fait flipper. Ça va mieux ?"
    play sound "Click.mp3" noloop

    P "Je crois que oui... Merci, [I]."
    play sound "Click.mp3" noloop 

    "{b}{i}Une atmosphère de soulagement envahit la pièce, mais une étrange sensation persiste en toi. Quelque chose d’anormal t’a poussé à t’effondrer, et tu sens que ce n’est pas terminé...{/i}{/b}"
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "Pourquoi me suis-je evanoui ?"
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Pourquoi me suis-je evanouie ?"
        play sound "Click.mp3" noloop
 
    Na "Je pense que tu t'aies trop donné dans les cours."
    play sound "Click.mp3" noloop

    P "Ah....."
    play sound "Click.mp3" noloop

    Na "Bon moi et Iris devont retourner en classe, reposes-toi."
    play sound "Click.mp3" noloop

    P "Tu ne peut pas rester avec moi [newname] ?"
    play sound "Click.mp3" noloop

    Na "Malheureusement non Malgré que la professeure sait qu'on est inséparable elle veut que je me concentre sur les cours et que je te laisse te reposer."
    play sound "Click.mp3" noloop 

    P "Ok je vois..."
    play sound "Click.mp3" noloop

    Na "A toute à l'heure et reposes-toi, tu en as besoin."
    play sound "Click.mp3" noloop

    P "Ok."
    play sound "Click.mp3" noloop

    "{b}{i} Les filles quittent la chambre.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je fais quoi ?"
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Rattrapper mon retard en math.{/i}{/b}" :
            
            P "Bon je vais essayser de travailler un peu..."
            play sound "Click.mp3" noloop 

            "{b}{i} Tu te poses devant ton bureau et commence à étudier.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Bon voyons voir....."
            play sound "Click.mp3" noloop 

            "{b}{i} Tu continues d'étudier pendant trois heures...{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Je vais m'arrêter maintenant sinon [newname] va piquer une crise."
            play sound "Click.mp3" noloop 

            "{b}{i} Dix minutes plus tard [newname] entre dans le dortoir. {/i}{/b}"
            play sound "Click.mp3" noloop 

            Na "Coucou comment ça va [prénom] ?"
            play sound "Click.mp3" noloop 

            P "Euh je vais bien....."
            play sound "Click.mp3" noloop 

            Na "Tu mens ça se voit tu as encore étudier alors que tu ne devrais pas."
            play sound "Click.mp3" noloop 

            P "Ok je l'admet......"
            play sound "Click.mp3" noloop 

            Na "Tu me déçois [prénom], après ça ne m'étonne pas venant de toi tu te donnes toujours à fond."
            play sound "Click.mp3" noloop 

            if pronom == "il":

                P "Désolé [newname]..."
                play sound "Click.mp3" noloop

            elif pronom == "elle": 

                P "Désolée [newname]..."
                play sound "Click.mp3" noloop 
        
            Na "Ok..."
            play sound "Click.mp3" noloop

        "{b}{i} Se reposer {/i}{/b}" : 
            
            "{b}{i} Tu te reposes pendant trois heures avant de te réveiller {/i}{/b}"
            play sound "Click.mp3" noloop 

            P "ça fait du bien un peu repos.."
            play sound "Click.mp3" noloop 

            "{b}{i} Dix minutes plus tard [newnmae] entre dans le dortoir. {/i}{/b}"
            play sound "Click.mp3" noloop 

            Na "Coucou comment ça va [prénom] ?"
            play sound "Click.mp3" noloop 

            P "Je vais bien."
            play sound "Click.mp3" noloop  

            Na "Cool alors."
            play sound "Click.mp3" noloop 

    P "Sinon tu vas faire quoi maintenant ?"
    play sound "Click.mp3" noloop

    Na "Je vais me déconnecter..."
    play sound "Click.mp3" noloop 

    P "Pas de souci."
    play sound "Click.mp3" noloop

    "{b}{i} [newname] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon je vais me recoucher aussi."
    play sound "Click.mp3" noloop

    "{b}{i} tu te couches tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen room 
    hide screen day

    "{b}{i} Le lendemain.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room 
    show screen room
    show screen day
    $ day += 1

    play sound "Alarm.mp3" noloop 

    P "Oh déjà..."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te léves tranquillement et te changes tranquillement {/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "J'imagine qu'elle encore fatiguée à cause d'hier."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    Na "Démarrage en cours......"
    play sound "Click.mp3" noloop 

    Na "Bonjour [prénom]."
    play sound "Click.mp3" noloop 

    P "Coucou comment ça va aujourd'hui ?"
    play sound "Click.mp3" noloop

    Na "Je vais mais je me suis inquiétée pour toi."
    play sound "Click.mp3" noloop 

    P "Ah..."
    play sound "Click.mp3" noloop 

    hide screen room 
    scene black
    play sound "Click.mp3" noloop 

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway 
    show screen hallway 
    play sound "Door.mp3" noloop 

    "{b}{i}Tu continues vers la salle de classe avec [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hallway

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom  
    show screen class_404 

    P "Bonjour tout le monde."
    play sound "Click.mp3" noloop 

    Y "Oh salut comment ça va [newname]."
    play sound "Click.mp3" noloop 

    P "Je vais bien."
    play sound "Click.mp3" noloop 

    Y "Cool alors car on s'est tous inquiété pour toi."
    play sound "Click.mp3" noloop 

    N "Oui c'est vrai mais heureusement qu'[newname] et [I] t'ont ramené à ton dortoir."
    play sound "Click.mp3" noloop 

    P "Merci beaucoup les amis."
    play sound "Click.mp3" noloop 

    Y "De rien."
    play sound "Door.mp3" noloop
    
    "{b}{i} Soudainement la [T] entres dans la classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour."
    play sound "Click.mp3" noloop

    N "Bonjour."
    play sound "Click.mp3" noloop

    Y "Bonjour Madame."
    play sound "Click.mp3" noloop

    P "Bonjour."
    play sound "Click.mp3" noloop

    Na "Bonjour.~"
    play sound "Click.mp3" noloop 

    "{b}{i}La [T] pose son regard sur toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Oh [prénom] je vois que tu vas mieux."
    play sound "Click.mp3" noloop

    P "Oui c'est exact."
    play sound "Click.mp3" noloop

    M "C'est bien que tu ais rétabli."
    play sound "Click.mp3" noloop

    P "Merci beaucoup Madame."
    play sound "Click.mp3" noloop

    M "Cool alors bon maintenant nous allons voir la formule du triangle isocéle rectangle."
    play sound "Click.mp3" noloop

    P "puis-je la dire ?"
    play sound "Click.mp3" noloop 

    M "Oui avec plaisir, peux-tu nous la dire."
    play sound "Click.mp3" noloop

    P " il suffit de faire a√2"
    play sound "Click.mp3" noloop

    M "Absolument."
    play sound "Click.mp3" noloop

    I "Attendez de base ce n'est pas le théoréme de pythagore ?"
    play sound "Click.mp3" noloop

    M "Oui mais cette formule existe aussi."
    play sound "Click.mp3" noloop 

    I "Ok j'ai rien dit."
    play sound "Click.mp3" noloop

    M "Bon veuillez faire les exercices."
    play sound "Click.mp3" noloop

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    M "Le cours est terminé vous pouvez quitter la salle."
    play sound "Click.mp3" noloop 

    M "N'oubliez l'exmaen de la semaine prochaine..."
    play sound "Click.mp3" noloop

    P "Bon on retourne au dortoir [newname] ?"
    play sound "Click.mp3" noloop

    Na "Oui."
    play sound "Click.mp3" noloop

    hide screen class_404 
    scene black 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene staircase 
    hide screen hallway

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hall
    show screen hall 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
    show screen lunchroom 
    
    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allez vers comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 600 

    P "C'est bon [newname] tu t'es servie ?"
    play sound "Click.mp3" noloop 

    Na "Oui c'est bon on peut aller s'asseoir."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous choissez de rejoindre [I] pour manger.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Coucou [I]."
    play sound "Click.mp3" noloop

    I "oh salut vous venez manger avec moi."
    play sound "Click.mp3" noloop

    P "oui."
    play sound "Click.mp3" noloop

    Na "Bien évidemment."
    play sound "Click.mp3" noloop

    I "Cool alors."
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Et dire qu'on aura déjà notre examen sur le théorème de pythagore..."
    play sound "Click.mp3" noloop

    P "oui c'est vrai."
    play sound "Click.mp3" noloop

    I "J'espére que toi et [newname] vous allez travailler dur pour cet examen."
    play sound "Click.mp3" noloop

    P "Ne t'inquiétes pas ça va bien passer."
    play sound "Click.mp3" noloop

    Na "Oui on a l'habitude avec [prénom]."
    play sound "Click.mp3" noloop

    P "Surtout qu'[newname] à acquis beaucoup de connaissances mais Le plus gros défaut du cadre scolaire c'est qu'il limite la protée globale de ces connaissances."
    play sound "Click.mp3" noloop 

    I "Cool alors mais j'ai une question."
    play sound "Click.mp3" noloop

    P "Oui dis-moi."
    play sound "Click.mp3" noloop

    I "Tu sais sur quel système d'exploitation tourne [newname] ?"
    play sound "Click.mp3" noloop

    if info == 1.0:

        P "Elle tourne sur Aether OS."
        play sound "Click.mp3" noloop  

        I "Cool alors..."
        play sound "Click.mp3" noloop 

        P "Merci beaucoup mais je compte faire un système d'exploitation personnalisé pour elle."
        play sound "Click.mp3" noloop 

    else: 

        P "Je ne sais pas sur quel système d'exploitation elle tourne pas."
        play sound "Click.mp3" noloop  

        I "Ok."
        play sound "Click.mp3" noloop 

        P "Merci beaucoup mais je compte faire un système d'exploitation personnalisé pour elle."
        play sound "Click.mp3" noloop 

    I "Ah je vois." 
    play sound "Click.mp3" noloop 

    "{b}{i} Vous conntinuez de discuter des cours pendant que vous mangez jusqu'a la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    I "Ok je vous suis."
    play sound "Click.mp3" noloop 

    scene black 
    hide screen lunchroom 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    scene staircase 
    hide screen hall

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway 
    show screen hallway

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hallway

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room 

    M "Bonjour nous allons faire un nouveau théme." 
    play sound "Click.mp3" noloop 

    S "Quoi comme cours ?"
    play sound "Click.mp3" noloop 

    M "Nous allons faire de l'informatique et du code." 
    play sound "Click.mp3" noloop 

    P "Oh trop bien."
    play sound "Click.mp3" noloop

    S "Sérieusement !? je suis un peu nul à ça."
    play sound "Click.mp3" noloop  

    P "Ce n'est pas un peu de l'autodérisition [S] ?"
    play sound "Click.mp3" noloop 

    Na "Oui trop bien en plus je n'ai jamais appris l'informatique car j'ai seulement appris à parler et écrire et les cours de base."
    play sound "Click.mp3" noloop 

    M "Cool que ça puisse te plaire [newname]."
    play sound "Click.mp3" noloop

    Na "Merci."
    play sound "Click.mp3" noloop

    P "De rien bon qui peut me dire en écrit un texte en python ?"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde hésite à lever la main.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Moi s'il vous plait."
    play sound "Click.mp3" noloop 

    M "Bien."
    play sound "Click.mp3" noloop
    
    $ Code = renpy.input("Veuillez écrire la réponse.")
    $ Code = Code.strip() 

    if Code = "print(\"Hello, World!\")":

        M "Bonne réponse."
        play sound "Click.mp3" noloop

    else :

        M "Mauvaise réponse."
        play sound "Click.mp3" noloop

    "{b}{i}Le cours continua sans probléme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    M "Le cours est terminé vous pouvez quitter la salle."
    play sound "Click.mp3" noloop 

    p "Bon on retourne au dortoir ?"
    play sound "Click.mp3" noloop

    Na "Oui."
    play sound "Click.mp3" noloop

    hide screen class_404
    scene black 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene black
    hide screen hallway

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room 

    Na "Enfin au dortoir."
    play sound "Click.mp3" noloop

    P "Oui ça fait du bien."
    play sound "Click.mp3" noloop

    Na "Bon moi je vais me déconncter."
    play sound "Click.mp3" noloop 

    P "Ok, Moi aussi je vais aller dormir mais d'abord aller manger."
    play sound "Click.mp3" noloop

    Na "Ok alors."
    play sound "Click.mp3" noloop

    "{b}{i} [newname] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene black
    hide screen room

    "{b}{i} Tu pars chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 700 
    scene room 
    show screen room

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    "{b}{i} Tu manges tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changea avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen room
    hide screen day

    "{b}{i} Le lendemain matin.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room 
    show screen room
    show screen day
    $ day += 1 

    play sound "Alarm.mp3" noloop 
    P "Oh déjà...."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te léves tranquillement et te changes tranquillement et pars voir [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 
    
    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    Na "Démarrage en cours......"
    play sound "Click.mp3" noloop 

    Na "Bonjour [prénom]."
    play sound "Click.mp3" noloop 

    P "Bonjour [newname] aujourd'hui on va faire du boulot dans la salle de club."
    play sound "Click.mp3" noloop

    Na "Génial."
    play sound "Click.mp3" noloop

    hide screen room
    scene black 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway

    "{b}{i}Tu te diriges au rez de chaussé.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway
    scene staircase
    play sound "Click.mp3" noloop

    "{b}{i}Tu continues dans les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop
     
    scene hall
    show screen hall

    "{b}{i}Tu continues vers la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene black
    hide screen hall

    "{b}{i}Tu entres dans la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hall
    scene main

    play music "Transition.mp3" noloop 

    "{b}{i}Chapitre 1.02 : Arisization Project - New Operating System.{/i}{/b}"
    play sound "Click.mp3" noloop 
 
    scene clubroom 
    show screen clubroom 
    play sound "Door.mp3" noloop  

    if pronom == "il":

        P "Enfin arrivés."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Enfin arrivées."
        play sound "Click.mp3" noloop 

    Na "Oui."
    play sound "Click.mp3" noloop

    P "Aujourd'hui je vais coder ton nouveau système d'exploitation."
    play sound "Click.mp3" noloop
 
    Na "Cool merci parce que ça quatre ans que j'ai mon vieux système d'exploitation."
    play sound "Click.mp3" noloop

    P "Donc je vais devoir complétement te déconnecter."
    play sound "Click.mp3" noloop

    Na "Donc je dois juste étre en veille comme d'habitude ?"
    play sound "Click.mp3" noloop

    P "Non se sera une déconnexion totale et manuelle."
    play sound "Click.mp3" noloop

    Na "Ok je vois."
    play sound "Click.mp3" noloop 

    menu:   

        "{b}{i} Déconnecter Complétement [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    Na "Déconnexion totale du système en cours......."
    play sound "Click.mp3" noloop

    P "Bon au boulot...."
    play sound "Click.mp3" noloop

    "{b}{i}Tu allumes ton ordi et tu ouvres ton éditeur de code.{/i}{/b}" 
    play sound "Click.mp3" noloop

label code:

    play sound "Menu.mp3" noloop
    $ system = renpy.input("Choisis un nom pour ton système d'exploitation.") 

    play sound "Menu.mp3" noloop
    $ Line1 = renpy.input("initiate_system(name=Aris,mode:secure,boot:true,fightmode:false);")

    menu:

        "{b}{i} Compiler le code.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            if Line1 == "initiate_system(name=Aris,mode:secure,boot:true,fightmode:false);":
            
                "Code correctement compilé."
                play sound "Click.mp3" noloop 
        
            else: 

                "Erreur détectée."
                play sound "Click.mp3" noloop 

                jump code 

    "{b}{i}Tu continues de travailler sur [newname] pendant trois heures.{/i}{/b}" 
    play sound "Click.mp3" noloop

    P "Bon il m'aura fallu beaucoup du temps amis j'ai enfin fini"
    play sound "Click.mp3" noloop

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    Na "Initialisation du système d'exploitaiton en cours...."
    play sound "Click.mp3" noloop

    Na "Démarrage en cours......"
    play sound "Click.mp3" noloop 

    Na "Bonjour [prénom], je tourne maintenant sur le système d'exploitation [system] avec la version [update] du processeur Corzen 11KS."
    play sound "Click.mp3" noloop 

    P "Coucou [newname] comment ça va ?" 
    play sound "Click.mp3" noloop 

    Na "Je vais bien."
    play sound "Click.mp3" noloop 

    hide screen clubroom
    scene black 

    "{b}{i} Vous sortez de la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hall 

    "{b}{i} Tu entres dasn le réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
    show screen lunchroom 

    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    P "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous allez vers comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 600 

    P "C'est bon [newname] tu t'es servie ?"
    play sound "Click.mp3" noloop 

    Na "Oui c'est bon on peut aller s'asseoir."
    play sound "Click.mp3" noloop 

    "{b}{i} On allons manger tu croises [H].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut [H], comment ça va ?"
    play sound "Click.mp3" noloop 

    H "Oh salut [prénom] et [newname], oui moi ça va bien et vous ?"
    play sound "Click.mp3" noloop 

    Na "On va bien."
    play sound "Click.mp3" noloop 

    H "Cool alors et sinon quoi de nouveau ?"
    play sound "Click.mp3" noloop

    P "On était dans notre salle de club pour du boulot."
    play sound "Click.mp3" noloop 

    H "Oh vous avez faitquoi de nouveau ?"
    play sound "Click.mp3" noloop 

    P "J'ai codé le nouveau système d'exploitation d'[newname]."
    play sound "Click.mp3" noloop 

    H "Génial et comment s'appelle t'il ?"
    play sound "Click.mp3" noloop 

    P "Il s'appelle [system]."
    play sound "Click.mp3" noloop 

    H "Ok alors."
    play sound "Click.mp3" noloop 

    P "Et sinon comment il avance ton robot car tu le montre jamais."
    play sound "Click.mp3" noloop

    H "Il avance bien."
    play sound "Click.mp3" noloop

    P "Tu fais un robot classique ou robot humanoïde ?"
    play sound "Click.mp3" noloop

    H "Un robot classique ne t'inquiétes pas je ne veux pas te copier et de toute façon [newname] est la derniére robot humanoïde."
    play sound "Click.mp3" noloop

    P "Intéressant et sinon tu sais ou est [I] ?"
    play sound "Click.mp3" noloop 

    H "Oh je l'ai aperçu avant elle était dans la salle de club générale, elle est vraiment occupée."
    play sound "Click.mp3" noloop 

    P "Ok je vois ça ne m'étonne pas venant d'elle."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on retourne au club ?"
    play sound "Click.mp3" noloop

    P "Ok alors."
    play sound "Click.mp3" noloop 

    Na "Ok je te suis."
    play sound "Click.mp3" noloop

    scene black 
    hide screen lunchroom 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall

    "{b}{i}Tu continues vers la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene black
    show screen hall

    "{b}{i}Tu entres dans la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene clubroom 
    show screen clubroom 
    hide screen hall 
    play sound "Door.mp3" noloop  

    P "Enfin au club."
    play sound "Click.mp3" noloop 

    Na "Oui ça fait du bien et sinon tu comptes faire quoi maintenant ?"
    play sound "Click.mp3" noloop 

    P "Je vais paramétrer ton nouveau système d'eyploitation."
    play sound "Click.mp3" noloop 

    Na "Génial."
    play sound "Click.mp3" noloop 

    if update == 1.0:

        "{b}{i}Tu t'asseois et allumes ton ordinateur mais [newname] agit bizarrement.{/i}{/b}"
        play sound "Click.mp3" noloop

        define Na = Character('[newname] Alternative', color="#6f00ff8c")

        Na "système opérationnel."
        play sound "Click.mp3" noloop

        P "Comment ça ? Qu'est-ce que tu racontes !?"
        play sound "Click.mp3" noloop

        Na "Démarrage du transfert des données vers un autre ordinateur."
        play sound "Click.mp3" noloop

        P "Mince elle est en train de se faire pirater....."
        play sound "Click.mp3" noloop

        menu:

            "{b}{i}Accéder à l'interface bios d'[newname].{/i}{/b}":
                play sound "Menu.mp3" noloop

        $ reboot = renpy.input("Écris ceci : initiate_humanoid_robot.shutdown(security_override=false")
        $ reboot = reboot.strip()

        if reboot == "initiate_humanoid_robot.shutdown(security_override=false":

            Na "Fermeture du système d'exploitation [system]....."
            play sound "Click.mp3" noloop

            P "Enfin..."
            play sound "Click.mp3" noloop

            P "Bon je vais la redémarrer."
            play sound "Click.mp3" noloop

            menu:

                "{b}{i}Redémarrer [newname].{/i}{/b}":
                    play sound "Menu.mp3" noloop

            define Na = Character('[newname] [nom]', color="#00eeff")

        else:

            Na "Qu'est-ce que tu tentes de faire."
            play sound "Stumble.mp3" noloop

            "{b}{i}[newname] se met à plaquer au sol.{/i}{/b}"
            play sound "Menu.mp3" noloop

            scene black
            hide clubroom
            hide screen clubroom
            hide screen points
            hide screen day

            if pronom == "il":

                play music "gameover.mp3" noloop
                "{b}{i}Fin numéro 8 : Complétement plaqué et étranglé par [newname] Alternative.{/i}{/b}"
                play sound "Menu.mp3" noloop

            elif pronom == "elle":

                play music "gameover.mp3" noloop
                "{b}{i}Fin numéro 8 : Complétement plaquée et étranglée par [newname] Alternative.{/i}{/b}"
                play sound "Menu.mp3" noloop

            menu:

                "{b}{i}Abandonner{/i}{/b}":
                    return
                "{b}{i}Réessayer.{/i}{/b}":
                    show clubroom
                    show screen clubroom
                    show screen points
                    show screen day
                    play music "Soundtrack2.mp3" loop volume 1.0
                    jump code

    else:

        "{b}{i}Tu t'asseois et allumes ton ordinateur.{/i}{/b}"
        play sound "Click.mp3" noloop

    P "Bien voyons voir...."
    play sound "Click.mp3" noloop

    "{b}{i}Tu regardes tous les paramétres pendant deux heures mais tu remarques quelques choses.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "On dirait qu'il y a rien de nouveau dans [system]."
    play sound "Click.mp3" noloop 

    Na "Bon on fait quoi du coup ?"
    play sound "Click.mp3" noloop 
  
    P "On peut retourner au dortoir."
    play sound "Click.mp3" noloop 

    Na "Ok alors je te suis"
    play sound "Click.mp3" noloop 

    hide screen clubroom
    scene black 

    "{b}{i} Vous sortez de la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall 

    "{b}{i}Tu continues vers les escaliers mais tu vois la porte de la salle de club générale légérement ouverte.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Attends [newname] on dirait que la porte de la salle de club générale légérement ouverte."
    play sound "Click.mp3" noloop 

    Na "Ah bon c'est bizarre."
    play sound "Click.mp3" noloop

    P "Attends moi ici je vais aller voir."
    play sound "Click.mp3" noloop

    scene black
    show screen hall

    "{b}{i}Tu continues dans la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene clubroom 
    show screen clubroom 
    hide screen hall 
    play sound "Door.mp3" noloop  

    "{b}{i}En entrant tu vois [I] complétement endormie sur la table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oh c'est mignon elle s'est endormie mais c'est normal elle s'est complétement donnée à fond pour son jeu."
    play sound "Click.mp3" noloop 

    P "Bon je fais quoi maintenant ?"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Réveiller [I] {/i}{/b}" : 

            "{b}{i} Tu approches calmement pour la réveiller.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Iris ça va ?"
            play sound "Click.mp3" noloop 

            I "Mhmmm C'est qui ?"
            play sound "Click.mp3" noloop 

            P "C'est moi [prénom]."
            play sound "Click.mp3" noloop

            I "Oh c'est toi..."
            play sound "Click.mp3" noloop

            if pronom == "il":

                P "Oui je suis venu te voir car je ne t'ai pas vu de la journée et je me suis inquiété."
                play sound "Click.mp3" noloop 

            elif pronom == "elle": 

                P "Oui je suis venue te voir car je ne t'ai pas vu de la journée et je me suis inquiétée."
                play sound "Click.mp3" noloop 

            I "Oh c'est gentil de t'inquiéter pour moi"
            play sound "Click.mp3" noloop 

            if pronom == "il":

                P "De rien c'est normal entre amis."
                play sound "Click.mp3" noloop 

            elif pronom == "elle": 

                P "De rien c'est normal entre amies."
                play sound "Click.mp3" noloop 

            I "Je suis vraiment fatiguée j'ai trop travaillé..."
            play sound "Click.mp3" noloop

            P "Il faut vraiment que tu te reposes."
            play sound "Click.mp3" noloop

            I "Je sais mais..."
            play sound "Click.mp3" noloop

            P "tu veux que je raccompagne au dortoir ou c'est bon ?"
            play sound "Click.mp3" noloop

            I "Non ça va aller ne t'inquiétes pas."
            play sound "Click.mp3" noloop

            P "Bien alors et reposes toi tu en as besoin."
            play sound "Click.mp3" noloop

            I "Merci beacoup."
            play sound "Click.mp3" noloop

            I "De rien."
            play sound "Click.mp3" noloop

            hide screen clubroom
            scene black 

            "{b}{i} Puis tu sors de la salle de club général.{/i}{/b}"
            play sound "Door.mp3" noloop

            scene hall 
            show screen hall 
            
        "{b}{i} La laisser dormir {/i}{/b}" : 

            P "Je vais la laisser dormir elle en a besoin."
            play sound "Click.mp3" noloop 

            hide screen clubroom
            scene black 

            "{b}{i} Puis tu sors de la salle de club général.{/i}{/b}"
            play sound "Door.mp3" noloop

            scene hall 
            show screen hall 

    P "Bon on y vas [newname]"
    play sound "Click.mp3" noloop    

    Na "Ok."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene staircase 
    hide screen hall

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway 
    show screen hallway

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hallway

    "{b}{i} Vous entres dans ton dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene room
    show screen room 

    if pronom == "il":

        P "Enfin au dortoir je suis epuisé."
        play sound "Click.mp3" noloop

    elif pronom == "elle": 

        P "Enfin au dortoir je suis epuisée."
        play sound "Click.mp3" noloop 

    Na "Oui enfin."
    play sound "Click.mp3" noloop 

    P "J'ai pu complétement finir ton nouveau système d'exploitation."
    play sound "Click.mp3" noloop 

    Na "Bon moi je vais me déconnecter."
    play sound "Click.mp3" noloop

    P "Ok alors." 
    play sound "Click.mp3" noloop

    Na "Déconnexion...."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon elle s'est déconnctée, je vais me cherecher à manger." 
    play sound "Click.mp3" noloop 

    scene black
    hide screen room

    "{b}{i} Tu pars chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 700 
    scene room 
    show screen room

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    "{b}{i} Tu manges tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changea avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene main
    hide screen room 
    hide screen day

    play music "Transition.mp3" noloop 

    "{b}{i}Chapitre 1.03 : Arisization Project - The start of the real problems{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene black 

    "{b}{i} Le lendemain matin.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room 
    show screen room
    show screen day
    $ day += 1 

    play sound "Alarm.mp3" noloop 
    P "Oh déjà...."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 
    
    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    Na "Démarrage en cours......"
    play sound "Click.mp3" noloop 

    Na "Bonjour [prénom]."
    play sound "Click.mp3" noloop 

    P "Coucou comment ça va aujourd'hui ?"
    play sound "Click.mp3" noloop

    Na "Je vais bien et toi ?"
    play sound "Click.mp3" noloop 

    P "Je vais bien, j'ai bien dormi."
    play sound "Click.mp3" noloop  

    Na "Cool alors."
    play sound "Click.mp3" noloop 

    P "Bon on va en cours ?"
    play sound "Click.mp3" noloop 

    Na "Bien évidemment."
    play sound "Click.mp3" noloop 

    hide screen room 
    scene black
    play sound "Click.mp3" noloop 

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway 
    show screen hallway 
    play sound "Door.mp3" noloop 

    "{b}{i}Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop
 
    scene black
    hide screen hallway

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom  
    show screen class_404 

    P "Bonjour."
    play sound "Click.mp3" noloop 

    Na "Bonjour."
    play sound "Click.mp3" noloop 

    M "Bonjour."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu regardes dans la salles tu vois les autres.{/i}{/b}"
    play sound "Click.mp3" noloop

    Y "Juste elle est où [I] ?"
    play sound "Click.mp3" noloop 

    K "Oui c'est vrai elle est où [I] ?"
    play sound "Click.mp3" noloop

    N "On veut savoir où elle est."
    play sound "Click.mp3" noloop 

    M "Doucement, [prénom] tu peux nous dire où est [I] ?"
    play sound "Click.mp3" noloop 

    P "Tout ce que je sais c'est qu'hier [I] était complétemnt fatiguée au club hier."
    play sound "Click.mp3" noloop 

    M "Oh je vois."
    play sound "Click.mp3" noloop 

    Y "Oh elle a sûrement dû étre fatiguée de surtravail."
    play sound "Door.mp3" noloop 

    "{b}{i}Puis soudainement [I] entres en classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Bonjour désolée de mon retard j'était pas bien."
    play sound "Click.mp3" noloop 

    M "Bonjour [I] si jamais [prénom] nous a déjà dii ce que tu avais."
    play sound "Click.mp3" noloop 

    I "Ok merci."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis [I] part s'asseoir à sa place.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bon reprenons le cours mais d'abord j'ai une chose à vous dire."
    play sound "Click.mp3" noloop 

    I "Quoi comme chose ?."
    play sound "Click.mp3" noloop 

    H "Oui dites-nous."
    play sound "Click.mp3" noloop 

    M "Il s'avére qu'il y a eu un attaque informatique hier dans l'après-midi qui a touché tout le lycée."
    play sound "Click.mp3" noloop 

    if update == 1.0:

        P "Ah ça oui je l'avais remarqué quand [newname] agissait bizarrement mais je savais que ça avait touché tout le lycée."
        play sound "Click.mp3" noloop 

        M "Oui et le plus surprenant c'est d'ou venait l'attaque."
        play sound "Click.mp3" noloop 

        P "Comment ça ?"
        play sound "Click.mp3" noloop 

        M "Oui l'attaque venait de l'intérieur du lycée ici même."
        play sound "Click.mp3" noloop 

        P "Pardon ?"
        play sound "Click.mp3" noloop 

        Y "Attend [prénom] tu as dit qu'[newname] avais agit bizarrement ?"
        play sound "Click.mp3" noloop 

        P "Oui pourquoi ?"
        play sound "Click.mp3" noloop 

        Y "Elle a sûrement du être piratée."
        play sound "Click.mp3" noloop 

        P "je pense aussi mais après j'ai corrigé la faille et maintenant elle est à jour niveau logiciel."
        play sound "Click.mp3" noloop 

        Y "Cool alors si tu as pu corriger la faille."
        play sound "Click.mp3" noloop 

        P "Merci."
        play sound "Click.mp3" noloop 

    else: 

        P "Pardon !? Dites-moi que c'est une blague !"
        play sound "Click.mp3" noloop 

        M "Oui et le plus surprenant c'est d'ou venait l'attaque."
        play sound "Click.mp3" noloop 

        P "Comment ça ?"
        play sound "Click.mp3" noloop 

        M "Oui l'attaque venait de l'intérieur du lycée ici même."
        play sound "Click.mp3" noloop 

        P "Pardon ?"
        play sound "Click.mp3" noloop 

    $ update += 1.0

    M "Calmez-vous avant que ça devienne l'anarchie."
    play sound "Click.mp3" noloop 

    "{b}{i} Tout le monde commence à se méfier les un les autres.{/i}{/b}"
    play sound "Click.mp3" noloop

    S "Donc il y a vraiment un traître parmi nous ?"
    play sound "Click.mp3" noloop 

    P "Bah oui tu as vu tout ce qui se passe au lycée ?"
    play sound "Click.mp3" noloop 

    S "Désolé c'est juste que je suis occupé."
    play sound "Click.mp3" noloop 

    P "Ok je comprends."
    play sound "Click.mp3" noloop 

    M "Bon maintenant commençons le cours, sortez votre livre page 10."
    play sound "Click.mp3" noloop 

    "{b}{i} Tout le monde sort leur livre{/i}{/b}"
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

    "{b}{i} Vous vous dirigez votre chemin vers la réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    scene staircase
    hide screen hallway

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hall 
    show screen hall

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom 
    show screen lunchroom 

    "{b}{i} en entrant vous allez vers comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 600 

    P "C'est bon [newname] tu t'es servie ?"
    play sound "Click.mp3" noloop 

    Na "Oui c'est bon on peut aller s'asseoir."
    play sound "Click.mp3" noloop 

    "{b}{i} Puis tu croises [I].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oh salut [I] ça te dit de venir avec nous ?"
    play sound "Click.mp3" noloop 

    I "Ce ne pas contre toi mais j'ai besoin d'être seule aujourd'hui."
    play sound "Click.mp3" noloop 

    P "Je vois mais sache que si tu as besoin de moi je serai là pour toi."
    play sound "Click.mp3" noloop 

    I "Merci beaucoup [prénom]."
    play sound "Click.mp3" noloop 

    P "Avec plaisir."
    play sound "Click.mp3" noloop 

    "{b}{i} Puis [I] s'éloigna pour aller manger seul.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu sais ce qu'elle a ?"
    play sound "Click.mp3" noloop 

    Na "J'en ai aucune idée malheureusement."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    "{b}{i} vous allez chercher un place puis tu vois [S] seul.{/i}{/b}"
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Aller manger avec [S]{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            P "Salut [S] ça va ?"
            play sound "Click.mp3" noloop 

            S "Oh c'est vous comment ça va toi et [newname] ?"
            play sound "Click.mp3" noloop 

            P "Je vais bien."
            play sound "Click.mp3" noloop 

            Na "Je vais bien aussi."
            play sound "Click.mp3" noloop 

            S "Cool alors."
            play sound "Click.mp3" noloop 

            "{b}{i} Pendant que vous mangez, [S] regarde des documents.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Ce sont quoi ces documents ?"
            play sound "Click.mp3" noloop  

            S "Rien d'important, c'est juste pour mon projet."
            play sound "Click.mp3" noloop 

            P "Ok....."
            play sound "Click.mp3" noloop 

            "{b}{i} Vous continuez de manger jusqu'à la sonnerie.{/i}{/b}" 
            play sound "Bell.mp3" noloop

            S "Bon il faut qu'on retourne en cours."
            play sound "Click.mp3" noloop 

            P "Ok....."
            play sound "Click.mp3" noloop

            Na "Ok je te suis [prénom]."
            play sound "Click.mp3" noloop 

        "{b}{i} Aller manger avec [Na]{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            "{b}{i} Vous allez chercher une pour manger.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Enfin on peut manger."
            play sound "Click.mp3" noloop

            Na "Oui enfin."
            play sound "Click.mp3" noloop

            "{b}{i} Vous asseyez tranquillement.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "[newname] tu pense que c'est le traître ?"
            play sound "Click.mp3" noloop

            Na "Je ne sais pas vraiment mais je que c'est [J1]."
            play sound "Click.mp3" noloop

            P "Et pourquoi elle ?"
            play sound "Click.mp3" noloop

            Na "Tu rigoles tu n'as pas vu comment elle était ?"
            play sound "Click.mp3" noloop

            P "Si j'ai vu je te rassure."
            play sound "Click.mp3" noloop

            Na "Merci beaucoup."
            play sound "Click.mp3" noloop

            "{b}{i} Vous continuez de discuter et de manger jusqu'à la sonnerie.{/i}{/b}" 
            play sound "Bell.mp3" noloop

            P "Bon il faut qu'on retourne en cours."
            play sound "Click.mp3" noloop 
             
            Na "Ok je te suis [prénom]." 
            play sound "Click.mp3" noloop 

    scene black 
    hide screen lunchroom 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall
    show screen hall

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    scene staircase 
    hide screen hall

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
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

    p "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    M "Rebonjour, bon reprenez votre livre page 11."
    play sound "Click.mp3" noloop 

    "{b}{i} le cours continue dans le calme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    M "Le cours est terminé vous pouvez quitter la salle."
    play sound "Click.mp3" noloop 

    Na "Bon [newname] on n'y va ?"
    play sound "Click.mp3" noloop 

    Na "Oui je suis fatiguée."
    play sound "Click.mp3" noloop 

    hide screen class_404
    scene black 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway 
    show screen hallway 

    P "Bon cette journée est enfin finie..."
    play sound "Click.mp3" noloop 

    Na "Oui enfin..."
    play sound "Click.mp3" noloop

    "{b}{i} tu vois soudainement un papier avec écrit l'ultime complotiste.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "L'ultime complotiste !? c'est impossible il n'y a aucun lycéen qui a ce titre ici..."
    play sound "Click.mp3" noloop

    Na "[prénom] ça va ?"
    play sound "Click.mp3" noloop

    P "Oui ça va."
    play sound "Click.mp3" noloop

    if pronom == "il":

        Na "Es-tu sûr ?"
        play sound "Click.mp3" noloop

    elif pronom == "elle":
        
        Na "Es-tu sûre ?"
        play sound "Click.mp3" noloop

    P "Oui."
    play sound "Click.mp3" noloop

    Na "Ok si tu le dis."
    play sound "Click.mp3" noloop

    P "Bon on continue vers le dortoir."
    play sound "Click.mp3" noloop

    Na "Oui absolument."
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene black
    hide screen hallway

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room
    show screen room 

    if pronom == "il":

        Na "Enfin arrivés"
        play sound "Click.mp3" noloop

    elif pronom == "elle":
        
        Na "Enfin arrivées"
        play sound "Click.mp3" noloop

    P "Oui ça fait du bien."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter."
    play sound "Click.mp3" noloop

    P "Pas de soucis, moi j'ai deux trois trucs à faire."
    play sound "Click.mp3" noloop

    Na "ok mais avant ça j'avais oublié de te demander un truc."
    play sound "Click.mp3" noloop

    P "Oui dis-moi."
    play sound "Click.mp3" noloop

    Na "Par rapport à cette histoire de traître et d'attaque, tu suspectes qui ?"
    play sound "Menu.mp3" noloop

    $ suspect = renpy.input("Marquez le prénom complet du lycéen que vous suspectez.")
    $ suspect = suspect.strip()   

    if suspect == "Ayano":
         
        P "Je pense que c'est [J1]."
        play sound "Click.mp3" noloop

        Na "Oui qu'elle a eu des propos inacceptables."
        play sound "Click.mp3" noloop 

        P "En plus elle est toujours avec [J2] dans leur club et je trouve ça suspcet car on ne connais pas leur projet."
        play sound "Click.mp3" noloop

        Na "Je vois bien."
        play sound "Click.mp3" noloop

    elif suspect == "Aiko":

        P "Je pense que c'est [J2]."
        play sound "Click.mp3" noloop

        Na "Oui qu'elle a eu des propos inacceptables."
        play sound "Click.mp3" noloop 

        P "En plus elle est toujours avec [J1] dans leur club et je trouve ça suspect car on ne connais pas leur projet."
        play sound "Click.mp3" noloop
    
        Na "Je vois bien."
        play sound "Click.mp3" noloop 

    elif suspect == "Subaru": 

        P "Je pense que c'est [S]."
        play sound "Click.mp3" noloop

        Na "Non ce n'est pas possible pour moi je pense." 
        play sound "Click.mp3" noloop

        P "Et pourquoi."
        play sound "Click.mp3" noloop

        Na "Rappelles-toi de quand il est arrivé au lycée."
        play sound "Click.mp3" noloop

        P "Oui et alors ?"
        play sound "Click.mp3" noloop

        Na "Il est arrivé bien après qu'on aie su qu'il y avait un traître ici."
        play sound "Click.mp3" noloop

        P "Oh oui c'est vrai comment j'ai pu oublié ce détail."
        play sound "Click.mp3" noloop

        Na "Tu vois ?"
        play sound "Click.mp3" noloop

        P "Mais quant-même il tiens des propos très bizarres."
        play sound "Click.mp3" noloop

        Na "Oui mais toute à commencer avant son arrivé."
        play sound "Click.mp3" noloop

        P "Ok mais je garde toujours mon avis sur lui."
        play sound "Click.mp3" noloop

        Na "Ok."
        play sound "Click.mp3" noloop

    elif suspect == "Yuki": 

        P "Je pense que c'est [Y]."
        play sound "Click.mp3" noloop

        Na "Pourquoi ? Elle est super sympa."
        play sound "Click.mp3" noloop

        P "Oui je sais mais tu n'as pas remarqué un truc ?"
        play sound "Click.mp3" noloop

        Na "Quoi dis-moi."
        play sound "Click.mp3" noloop

        P "Elle est souvent absente après le cours."
        play sound "Click.mp3" noloop

        Na "Oui c'est vrai maintenant que tu le dis."
        play sound "Click.mp3" noloop

        P "En plus on ne sais rien de son domaine ultime.   "
        play sound "Click.mp3" noloop

        Na "Tu as raison."
        play sound "Click.mp3" noloop

    else: 

        Na "Non c'est impossible cette personne nous soutient, ils oserait même pas trahir le lycée ou s'attaquer à moi ou le lycée."
        play sound "Click.mp3" noloop

    P "Bon moi je vais chercher à manger et aller régler un truc."
    play sound "Click.mp3" noloop

    Na "Ok moi je vais me déconnecter..."
    play sound "Click.mp3" noloop 

    P "Pas de souci."
    play sound "Click.mp3" noloop

    "{b}{i} [newname] se déconnecta tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon moi j'y vais."
    play sound "Click.mp3" noloop

    scene black 
    hide screen room

    "{b}{i}Tu quittes ton dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene hallway
    show screen hallway

    "{b}{i}Tu conntinues dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop
 
    scene staircase 
    hide screen hallway

    "{b}{i}Tu conntinues vers le hall.{/i}{/b}"
    play sound "Click.mp3" noloop 

    scene hall 
    show screen hall

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    P "Bon je suis presqu'arriver."
    play sound "Click.mp3" noloop

    scene black 
    hide screen hall 

    "{b}{i}Tu entres dans le bureau des élèves avec [Na].{/i}{/b}"
    play sound "Click.mp3" noloop

    scene office 
    show screen office 
    play sound "Door.mp3" noloop 

    P "Bonjour c'est moi [prénom]."
    play sound "Click.mp3" noloop

    E "Que puis-je faire pour toi ?"
    play sound "Click.mp3" noloop

    P "C'est concernant cette histoire de traître car j'ai trouver quelque chose."
    play sound "Click.mp3" noloop

    E "Oui dis-moi qu'est qu'il y a ?"
    play sound "Click.mp3" noloop

    P "J'ai trouvé une note qui est signée l'ultime complotiste mais aucun élèves a ce titre ici."
    play sound "Click.mp3" noloop

    P ""
    play sound "Click.mp3" noloop
 
    return                              