#!/Python
# -*-coding:Utf-8-*
import pygame
from pygame.locals import *
from constantes import *;
from classes import *;
import time;

pygame.init();#on initialise la fenetre
fenetre = pygame.display.set_mode((taille_fenetre_largeur,taille_fenetre_longueur));#on parametre les dimensions de la fenetre

compteur = 0;
font = pygame.font.Font(None, 30);
pygame.display.set_caption("Mario Labirynthe");#pour le titre de la fenetre
text_compteur = font.render(" " + str(compteur), 1,(0,0,0));
count_piece = 0;

continuer = 1;
continuer_accueil = 0;
continuer_jeu = 0;
choix = 0;
princesse = 0;
end = 1;
continuer_aide = 0;
deplacement = 0;
missile_ok = 0;
font3 = pygame.font.Font(None, 25);
font4 = pygame.font.Font(None, 23);
while continuer:

	#on charge le bg de la fenetre d'accueil
	afficher_menu(fenetre);
	pygame.display.flip();

	continuer_accueil = 1;#on met en route les boucles a chaque fois

	continuer_jeu = 1;

	continuer_aide = 0;

	choix = 0;

	deplacement = 0;

	princesse = 0;

	compteur = 0;

	count_piece = 0;

	liste_missile = [];

	while continuer_accueil:

		pygame.time.Clock().tick(30);

		for event in pygame.event.get():

			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):

				continuer_accueil = 0;
				continuer_jeu = 0;
				continuer = 0;

			if event.type == KEYDOWN:

				if event.key == K_F1:
					#on arrete la boucle d'accueil car on va passer dans celle de jeu

					continuer_accueil = 0;
					choix = 'n1'#nom du fichier
					princesse = 1;

				elif event.key == K_F2:

					continuer_accueil = 0;
					choix = 'n2';
					princesse = 1;

				elif event.key == K_F3:

					continuer_accueil = 0;
					choix = 'n3';
					princesse = 1;

				elif event.key == K_F4:

					continuer_accueil = 0;
					choix = 'n5';
					princesse = 2;

				elif event.key == K_F5:

					continuer_accueil = 0;
					choix = 'n6';
					princesse = 2;

				elif event.key == K_F6:

					continuer_accueil = 0;
					choix = 'n7';
					princesse = 2;

				elif event.key == K_F7:

					continuer_accueil = 0;
					choix = 'n4';
					princesse = 0;

			elif event.type == MOUSEBUTTONDOWN:

				if (event.pos[0] > 0 and event.pos[1] < 40) and (\
					event.pos[1] > 0 and event.pos[1] < 50):
					continuer_accueil = 0;
					continuer_aide = 1;
					continuer_jeu = 0;


	while continuer_aide:

		pygame.time.Clock().tick(30);

		for event in pygame.event.get():

			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):

				continuer_aide = 0;

				continuer_accueil = 1;

				continuer_jeu = 0;

			elif event.type == MOUSEBUTTONDOWN:

				if (event.pos[0] > 0 and event.pos[1] < 40) and (\
				event.pos[1] > 0 and event.pos[1] < 50):
					continuer_accueil = 1;
					continuer_aide = 0;
					continuer_jeu = 0;

		afficher_aide(fenetre);
		pygame.display.flip();

	if choix != 0:

		fond = pygame.image.load(image_fond).convert();

		fenetre.blit(fond,(0,0));

		niveau = Niveau(choix);
		#on genere le niveau
		niveau.generer();
		#on affiche le niveau a l'ecran
		niveau.afficher(fenetre);

		mario = Perso("mario_bas.png", "mario_haut.png", "mario_droite.png", "mario_gauche.png", niveau, 0, 0);


		#on peut maintenant passer a la boucle de jeu
	while continuer_jeu:

		pygame.time.Clock().tick(30);
		
		for event in pygame.event.get():

			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):

				continuer_jeu = 0;

			elif event.type == KEYDOWN:

				if event.key == K_RIGHT:

					mario.deplacer('droite');

					deplacement += 1;

				elif event.key == K_UP:

					mario.deplacer('haut');

					deplacement += 1;

				elif event.key == K_LEFT:

					mario.deplacer('gauche');

					deplacement += 1;

				elif event.key == K_DOWN:

					deplacement += 1;

					mario.deplacer('bas');

				elif event.key == K_a:
					missile = Missile(boule,niveau,mario,mario.direction);
					missile_ok = 1;

				elif event.key == K_l:

					mario.changeToLuigi();
					fenetre.blit(mario.direction, (mario.x,mario.y));

				elif event.key == K_m:

					mario.changeToMario();
					fenetre.blit(mario.direction,(mario.x,mario.y));

		#on rafraichit l'image a chaque tour de boucle
		fenetre.blit(fond, (0,0));
		niveau.afficher(fenetre);
		if missile_ok and missile.ok:

			missile.update();
			fenetre.blit(missile.image,(missile.x,missile.y));

		fenetre.blit(mario.direction, (mario.x,mario.y));
		pygame.display.flip();
		if mario.niveau.structure_fichier[mario.case_y][mario.case_x] == 'p':
			count_piece += 1;
			niveau.structure_fichier[mario.case_y][mario.case_x] = '0';

		if mario.niveau.structure_fichier[mario.case_y][mario.case_x] == 't':

			end = 1;

			while end:	

				for event in pygame.event.get():

					if event.type == KEYDOWN and event.key == K_ESCAPE:
						continuer_jeu = 0;
						end = 0;

				pygame.time.Clock().tick(30);
				fenetre.blit(fond,(0,0));
				niveau.afficher(fenetre);
				texte_victoire = font3.render("Vous avez sauvez Princesse Peach en " + str(deplacement) + " coups!!", 1,(255,255,255));
				texte_victoire2 = font3.render("Vous avez recuperer " + str(count_piece) + " pieces!!!", 1,(255,255,255));
				texte_quitter = font3.render("Press ESCAPE to quit...", 1,(255,255,255));
				fenetre.blit(texte_victoire,(40,200));
				fenetre.blit(texte_victoire2,(40,225));
				fenetre.blit(texte_quitter, (40,250));
				pygame.display.flip();


		elif mario.niveau.structure_fichier[mario.case_y][mario.case_x] == 's':
			
			end = 1;

			while end:	
				
				for event in pygame.event.get():

					if event.type == KEYDOWN and event.key == K_ESCAPE:
						continuer_jeu = 0;
						end = 0;

				pygame.time.Clock().tick(30);
				fenetre.blit(fond,(0,0));
				niveau.afficher(fenetre);
				texte_victoire = font3.render("Vous avez sauvez Princesse Daisy en " + str(deplacement) + " coups!!", 1,(255,255,255));
				texte_victoire2 = font3.render("Vous avez recuperer " + str(count_piece) + " pieces!!!", 1,(255,255,255));
				texte_quitter = font3.render("Press ESCAPE to quit...", 1,(255,255,255));
				fenetre.blit(texte_victoire,(40,200));
				fenetre.blit(texte_victoire2,(40,225));
				fenetre.blit(texte_quitter, (40,250));
				pygame.display.flip();
		elif mario.niveau.structure_fichier[mario.case_y][mario.case_x] == 'c' and compteur == 0:
			compteur += 1;
			print(compteur);
		elif mario.niveau.structure_fichier[mario.case_y][mario.case_x] == 'e' and compteur == 1:
			compteur += 1;
			print(compteur)
		elif compteur == 2:
			end = 1;
			while end:

				for event in pygame.event.get():

					if event.type == KEYDOWN and event.key == K_ESCAPE:
						continuer_jeu = 0;
						end = 0;
						compteur = 0;

				pygame.time.Clock().tick(30);
				fenetre.blit(fond,(0,0));
				niveau.afficher(fenetre);
				texte_victoire2 = font4.render("Vous avez recuperer " + str(count_piece) + " pieces!!!", 1,(255,255,255));
				texte_victoire = font4.render("Vous avez sauvez Princesse Peach et Daisy en " + str(deplacement) + " coups!!", 1,(255,255,255));
				texte_quitter = font4.render("Press ESCAPE to quit...", 1,(255,255,255));
				fenetre.blit(texte_victoire,(0,200));
				fenetre.blit(texte_victoire2,(0,225));
				fenetre.blit(texte_quitter, (40,250));
				pygame.display.flip();