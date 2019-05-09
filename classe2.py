#!/Python
# -*-coding:Utf-8-*
import pygame;
from pygame.locals import *;
from constantes2 import *;

class Niveau:

    """classe qui va permettre de generer un niveau en fonction du choix de l'utilisateur
    le niveau est accessible via un fichier qui sera chargé dans une liste a deux dimensions
    on pourra ainsi utiliser cette liste pour generer le niveau avec le bon affichage"""

    def __init__(self, fichier):

        self.fichier = fichier;
        #on cree une structure qui permettra de contenir le contenu du fichier
        self.structure_fichier = 0;


    def generer(self):

        #on ouvre le fichier qui contient les donnes=es qui nous interesse

        with open(self.fichier, "r") as fichier:

            #on cree une premiere structure qui va servir de liste tampon

            structure_niveau = [];

            #on lit ensuite ligne par ligne le fichier

            for ligne in fichier:

                ligne_fichier = [];

                #on lit ensuite chacun des caracteres qui sont presents dans la ligne seulement si ils sont
                #differents d'un saut de ligne

                for sprite in ligne:

                    if sprite != '\n':

                        ligne_fichier.append(sprite);

                #comme on vient de lire une ligne, on va la stocker directement dans la structure principale

                structure_niveau.append(ligne_fichier);

            #une fois que l'on a tout lu, on peut stocker la liste dans celle de notre objet Niveau

            self.structure_fichier = structure_niveau;

    def afficher(self, fenetre):

        """fonction qui va permettre l'affichage du niveau, une fois que la structure principale de notre objet 
        a ete entierment rempli par les differentes ligne de notre fichier"""

        #on va d'abords definir des variable qui prennent en compte les differents objets a afficher

        mur = pygame.image.load(image_mur).convert();   
        depart = pygame.image.load(image_depart).convert_alpha();
        mur2 = pygame.image.load("mur_image2.png").convert_alpha();
        #on va maintenant proceder a l'affichage du niveau
        num_ligne = 0;
        arbre = pygame.image.load("arbre.png").convert_alpha();

        for ligne in self.structure_fichier:

            #chaque ligne correspond a l'abscisee de la fenetre, cad x

            num_colonne = 0;

            for sprite in ligne:

                #on passe maintenant a l'ordonne
     
                #on cree des variables de coordonnes qui vont nous permettre d'afficher les sprites au bon endroit
                x = num_colonne * taille_sprite;
                y = num_ligne * taille_sprite;

                #on tes maintenant les differentes valeurs des sprites pour afficher en fonction

                if sprite == 'm':

                    fenetre.blit(mur,(x,y));

                elif sprite == 'd':

                    fenetre.blit(depart,(x,y));

                elif sprite == 'n':

                    fenetre.blit(mur2,(x,y));

                elif sprite == 'o':

                    fenetre.blit(arbre,(x,y));
                #on incremente ensuite l'ordonne puis l'abscisse comme dans un repere

                num_colonne += 1;

            num_ligne += 1;

class Missile:

    def __init__(self,image,niveau,perso,direction):

        self.image = pygame.image.load(boule).convert_alpha();
        self.case_x = perso.case_x;
        self.case_y = perso.case_y;
        self.x = perso.x - 6.5;
        self.y = perso.y;
        self.direction = direction;
        self.niveau = niveau;
        self.ok = 1;
        self.perso = perso;
    def update(self):

        verif = 1;
        if self.direction == self.perso.bas:
            if (self.y % 30 == 0):
                self.case_y += 1;#augmentation du nombre de case

            if self.case_y < (nombre_sprite):

                if self.niveau.structure_fichier[self.case_y][self.case_x] != 'm' and \
                self.niveau.structure_fichier[self.case_y][self.case_x] != 'n' \
                and self.niveau.structure_fichier[self.case_y][self.case_x] != 'o':
                    self.y += (taille_sprite / 1);
                else:
                    self.ok = 0;

        elif self.direction == self.perso.haut:
            if (self.y % 30 == 0):
                self.case_y -= 1;

            if self.case_y >= 0:

                if self.niveau.structure_fichier[self.case_y][self.case_x] != 'm'\
                 and self.niveau.structure_fichier[self.case_y][self.case_x] !='n' \
                 and self.niveau.structure_fichier[self.case_y][self.case_x] != 'o':

                    self.y -= (taille_sprite / 1);
                else:
                    self.ok = 0;
        elif self.direction == self.perso.droite:
            if (self.x % 30 == 0):
                self.case_x += 1;
            if self.case_x < (nombre_sprite):

                if self.niveau.structure_fichier[self.case_y][self.case_x] != 'm' \
                and self.niveau.structure_fichier[self.case_y][self.case_x] !='n' \
                and self.niveau.structure_fichier[self.case_y][self.case_x] != 'o':
                    self.x += (taille_sprite / 1);
                else:
                    self.ok = 0;

        elif self.direction == self.perso.gauche:
            
            if (self.x % 30 == 0):
                self.case_x -= 1;
            if self.case_x >= 0:

                if self.niveau.structure_fichier[self.case_y][self.case_x] != 'm'\
                 and self.niveau.structure_fichier[self.case_y][self.case_x] !='n' \
                 and self.niveau.structure_fichier[self.case_y][self.case_x] != 'o':

                    self.x -= (taille_sprite/ 1);
                else:
                    self.ok = 0;

class Perso:

    """classe permettant de creer mario
    il faudra dans son constructeur son image de face, de dos, droite et gauche
    ainsi que le niveau dans lequel il va se situer"""

    def __init__(self,bas,haut,droite,gauche,niveau,x,y,xx):

        #initialisation des differentes faces du personnage
        self.bas = pygame.image.load(bas).convert_alpha();
        self.haut = pygame.image.load(haut).convert_alpha();
        self.gauche = pygame.image.load(gauche).convert_alpha();
        self.droite = pygame.image.load(droite).convert_alpha();

        self.niveau = niveau;

        #on initialise les coordonnees du personnages ainsi que les coordonnees
        #qui permettront de gerer les collisions

        self.x = x;
        self.y = y;
        self.case_x = xx;
        self.case_y = 0;

        #direction par defaut : bas

        self.direction = self.bas;

    def deplacer(self,direction):

        if direction == 'droite':

            if self.case_x < (nombre_sprite - 1):

                if self.niveau.structure_fichier[self.case_y][self.case_x+1] != 'm' and \
                self.niveau.structure_fichier[self.case_y][self.case_x+1] != 'n' \
                and self.niveau.structure_fichier[self.case_y][self.case_x+1] != 'o':

                    self.case_x += 1;
                    self.x = (self.case_x * taille_sprite) + 6.5;

            self.direction = self.droite;

        if direction == 'gauche':

            if self.case_x > 0:

                if self.niveau.structure_fichier[self.case_y][self.case_x-1]!='m' and \
                self.niveau.structure_fichier[self.case_y][self.case_x-1] != 'n' \
                and self.niveau.structure_fichier[self.case_y][self.case_x-1] != 'o':

                    self.case_x -= 1;
                    self.x = (self.case_x * taille_sprite) + 6.5;
            self.direction = self.gauche;


        if direction == 'haut':

            if self.case_y > 0:

                if self.niveau.structure_fichier[self.case_y-1][self.case_x] != 'm' and \
                self.niveau.structure_fichier[self.case_y-1][self.case_x] != 'n' and \
                self.niveau.structure_fichier[self.case_y-1][self.case_x] != 'o':


                    self.case_y -= 1;
                    self.y = (self.case_y * taille_sprite);
            self.direction = self.haut;


        if direction == 'bas':

            if self.case_y < (nombre_sprite - 1):

                if self.niveau.structure_fichier[self.case_y+1][self.case_x] != 'm' and \
                self.niveau.structure_fichier[self.case_y+1][self.case_x] != 'n' and \
                self.niveau.structure_fichier[self.case_y+1][self.case_x] != 'o':

                    self.case_y += 1;

                    self.y = self.case_y * taille_sprite;

            self.direction = self.bas;

def afficher_aide(fenetre):

    scrrec = fenetre.get_rect();
    font2 = pygame.font.Font(None, 20);
    font3 = pygame.font.Font(None, 25);
    font4 = pygame.font.Font(None, 15);
    
    accueil = pygame.image.load(image_accueil).convert();

    accueil = pygame.transform.scale(accueil, (scrrec.right, scrrec.bottom))
    texte_aide = font2.render("Bienvenue dans mon jeu intitule DragonbBall 2d",1,(255,255,255));
    texte_aide2 = font2.render("Le but du jeu est simple : il faut eliminer le joueur adverse",1,(255,255,255));
    texte_aide3 = font2.render("Les commandes pour y parvenir sont les suivantes : ",1,(255,255,255));
    texte_aide4 = font2.render("Fleche directionnelle droite ou D pour aller a droite",1,(255,255,255));
    texte_aide5 = font2.render("Fleche directionnelle gauche ou Q pour aller a gauche",1,(255,255,255));
    texte_aide6 = font2.render("Fleche directionnelle haut ou Z pour aller en haut",1,(255,255,255));
    texte_aide7 = font2.render("Fleche directionnelle bas ou S pour aller en bas",1,(255,255,255));
    texte_aide10 = font2.render("Touche A ou 0 pour lancer des boules de feu (1 seule a chaque fois",1,(255,255,255));
    texte_aide11 = font2.render("Touche Espace pour mettre le jeu en pause",1,(255,255,255));
    texte_chance = font2.render("Que le meilleur gagne !", 1,(255,255,255));
    arriere = pygame.image.load(retour_arriere).convert_alpha();

    fenetre.blit(accueil, (0,0));
    fenetre.blit(arriere, (0,0));

    fenetre.blit(texte_aide,(0,50));

    fenetre.blit(texte_aide2,(0,70));

    fenetre.blit(texte_aide3,(0,90));

    fenetre.blit(texte_aide4,(25,110));

    fenetre.blit(texte_aide5,(25, 130));

    fenetre.blit(texte_aide6,(25,150));

    fenetre.blit(texte_aide7,(25,170));

    fenetre.blit(texte_aide10, (25,190));

    fenetre.blit(texte_aide11, (25,210));

    fenetre.blit(texte_chance, (0,230));
def afficher_menu(fenetre):

    aide = pygame.image.load(image_aide).convert_alpha();
    scrrec = fenetre.get_rect();
    font = pygame.font.Font(None, 30);
    text4 = font.render("F4 Baraquements", 1, (0,0,0));
    text1 = font.render("F1 Map Ouverte", 1,(0,0,0))
    text2 = font.render("F2 Zone de Combat",1,(0,0,0));
    accueil = pygame.image.load(image_accueil).convert();
    text3 = font.render("F3 VS",1,(0,0,0));
    accueil = pygame.transform.scale(accueil, (scrrec.right, scrrec.bottom))

    fenetre.blit(accueil, (0,0));

    fenetre.blit(aide,(0,0));
    fenetre.blit(text2, ((taille_fenetre_longueur/2) - 100, (taille_fenetre_largeur/2)));
    fenetre.blit(text1, ((taille_fenetre_longueur/2) - 100, (taille_fenetre_largeur/2) - 20));
    fenetre.blit(text3, ((taille_fenetre_longueur/2) -100, (taille_fenetre_largeur/2) + 20));
    fenetre.blit(text4, ((taille_fenetre_longueur/2)- 100, (taille_fenetre_largeur/2) + 40));

def afficher_selection(fenetre):

    font = pygame.font.Font(None,30);

    text1 = font.render("F1 Sangoku", 1,(255,255,255));
    text2 = font.render("F2 Vegeta", 1,(255,255,255));
    text3 = font.render("F3 Boo", 1,(255,255,255));
    text4 = font.render("F4 Broly", 1,(255,255,255));
    text5 = font.render("F5 Cell", 1,(255,255,255));
    text6 = font.render("F6 Freezer (forme final)", 1,(255,255,255));
    text7 = font.render("F7 Jeese",1,(255,255,255));
    text8 = font.render("F8 Sangoku SS4",1,(255,255,255));
    text9 = font.render("F9 Freezer (2eme forme)",1,(255,255,255));
    fenetre.blit(text1, ((taille_fenetre_longueur/2) - 100, (taille_fenetre_largeur/2) -25));
    fenetre.blit(text2, ((taille_fenetre_longueur/2) - 100, (taille_fenetre_largeur/2)));
    fenetre.blit(text3, ((taille_fenetre_longueur/2) - 100, (taille_fenetre_largeur/2) +25));
    fenetre.blit(text4, ((taille_fenetre_longueur/2) - 100, (taille_fenetre_largeur/2) +50));
    fenetre.blit(text5, ((taille_fenetre_longueur/2) -100, (taille_fenetre_largeur/2) + 75));
    fenetre.blit(text6, ((taille_fenetre_longueur/2) - 100, (taille_fenetre_largeur/2) + 100));
    fenetre.blit(text7, ((taille_fenetre_longueur/2) - 100, (taille_fenetre_largeur/2) + 125));
    fenetre.blit(text8, ((taille_fenetre_longueur/2) -100, (taille_fenetre_largeur/2) + 150));
    fenetre.blit(text9, ((taille_fenetre_longueur/2) - 100, (taille_fenetre_largeur/2) + 175));

def afficher_pause(fenetre):
    scrrec = fenetre.get_rect();
    font = pygame.font.Font(None,30);
    text = font.render("PAUSE",1,(255,255,255));

    fond = pygame.image.load(image_accueil).convert();

    fond = pygame.transform.scale(fond, (scrrec.right, scrrec.bottom))
    fenetre.blit(fond,(0,0));
    fenetre.blit(text, ((taille_fenetre_longueur/2) - 50, (taille_fenetre_largeur / 2)));