#!/Python
# -*-coding:Utf-8-*
import pygame
from pygame.locals import *
from constantes2 import *;
from classe2 import *;
import time;

pygame.init();#on initialise la fenetre
fenetre = pygame.display.set_mode((taille_fenetre_largeur,taille_fenetre_longueur));#on parametre les dimensions de la fenetre
nom_perso1 = str();
nom_perso2 = str();
compteur = 0;
font = pygame.font.Font(None, 30);
pygame.display.set_caption("DragonBall 2d");#pour le titre de la fenetre
text_compteur = font.render(" " + str(compteur), 1,(0,0,0));
count_piece = 0;
count_choice = 0;
continuer = 1;
continuer_accueil = 0;
continuer_jeu = 0;
choix = 0;
contniuer_pause = 0;
end = 1;
continuer_aide = 0;
deplacement = 0;
missile_ok = 0;
missile2_ok = 0;
end = 0;
continuer_selction = 0;
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

	missile2_ok = 0;

	nom_perso1 = "";

	nom_perso2 = "";

	count_choice = 0;

	missile_ok = 0;
	while continuer_accueil:

		pygame.time.Clock().tick(50);

		for event in pygame.event.get():

			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):

				continuer_accueil = 0;
				continuer_jeu = 0;
				continuer = 0;

			if event.type == KEYDOWN:
				if event.key == K_F4:

					continuer_accueil = 0;
					choix = 'n10';
				elif event.key == K_F1:

					continuer_accueil = 0;
					choix = 'n1bis';

				elif event.key == K_F2:
					continuer_accueil = 0;
					choix = 'n2bis';

				elif event.key == K_F3:
					continuer_accueil = 0;
					choix = 'n3bis';
			elif event.type == MOUSEBUTTONDOWN:

				if (event.pos[0] > 0 and event.pos[1] < 40) and (\
					event.pos[1] > 0 and event.pos[1] < 50):
					continuer_accueil = 0;
					continuer_aide = 1;
					continuer_jeu = 0;

	while continuer_aide:

		pygame.time.Clock().tick(50);

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

		continuer_selction = 1;

		fond = pygame.image.load("dbz_fond.jpg").convert();

		fenetre.blit(fond,(0,0));

		niveau = Niveau(choix);
			#on genere le niveau
		niveau.generer();
		while continuer_selction:

			pygame.time.Clock().tick(50);


			scrrec = fenetre.get_rect();
			fond = pygame.transform.scale(fond,(scrrec.right, scrrec.bottom));
			fenetre.blit(fond,(0,0));
			afficher_selection(fenetre);
			
			for event in pygame.event.get():

				if event.type == QUIT:
					continuer_selction = 0;
					continuer = 0;
					continuer_jeu = 0;
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						continuer_selction = 0;
						continuer_jeu = 0;
						"""premier choix"""
					elif event.key == K_F1 and count_choice == 0:
						perso1 = Perso("s_haut.png", "s_bas.png", "s_droite.png", "s_gauche.png", niveau,0,0,0);
						count_choice += 1;
						nom_perso1 = "Sangoku";
					elif event.key == K_F2 and count_choice == 0:
						perso1 = Perso("v_bas.png","v_haut.png","v_droite.png","v_gauche.png",niveau,0,0,0);
						count_choice += 1;
						nom_perso1 = "Vegeta";
					elif event.key == K_F3 and count_choice == 0:
						perso1 = Perso("boo_bas.png", "boo_haut.png", "boo_droite.png", "boo_gauche.png",niveau,0,0,0);
						count_choice += 1;
						nom_perso1 = "Boo";
					elif event.key == K_F4 and count_choice == 0:
						perso1 = Perso("broly_bas.png","broly_haut.png","broly_droite.png","broly_gauche.png",niveau,0,0,0);
						count_choice += 1;
						nom_perso1 = "Broly";
					elif event.key == K_F5 and count_choice == 0:
						count_choice += 1;
						perso1 = Perso("cell_bas.png","cell_haut.png","cell_droite.png","cell_gauche.png",niveau,0,0,0);
						nom_perso1 = "Cell";
					elif event.key == K_F6 and count_choice == 0:
						count_choice += 1;
						perso1 = Perso("freezer_bas.png","freezer_haut.png","freezer_droite.png","freezer_gauche.png",niveau,0,0,0);
						nom_perso1 = "Freezer forme finale";
					elif event.key == K_F7 and count_choice == 0:
						count_choice += 1;
						perso1 = Perso("g_bas.png","g_haut.png","g_droite.png","g_gauche.png",niveau,0,0,0);
						nom_perso1 = "Freese";
					elif event.key == K_F8 and count_choice == 0:
						count_choice += 1;
						perso1 = Perso("s2_bas.png","s2_haut.png","s2_droite.png","s2_gauche.png",niveau,0,0,0);
						nom_perso1 = "Sangoku SS4";
					elif event.key ==K_F9 and count_choice == 0:
						count_choice += 1;
						perso1 = Perso("f_bas.png","f_haut.png","f_gauche.png","f_droite.png",niveau,0,0,0);
						nom_perso1 = "Freezer éeme forme";
						"""deuxieme choix"""
					elif event.key == K_F1 and count_choice == 1:
						perso2 = Perso("s_haut.png","s_bas.png","s_droite.png","s_gauche.png",niveau,14*taille_sprite,0,14);
						count_choice += 1;
						nom_perso2 = "Sangoku";
					elif event.key == K_F2 and count_choice == 1:
						perso2 = Perso("v_bas.png","v_haut.png","v_droite.png","v_gauche.png",niveau,14*taille_sprite,0,14);
						count_choice += 1;
						nom_perso2 = "Vegeta"
					elif event.key == K_F3 and count_choice == 1:
						perso2 = Perso("boo_bas.png", "boo_haut.png", "boo_droite.png", "boo_gauche.png", niveau,14*taille_sprite,0,14);
						count_choice += 1;
						nom_perso2 = "Boo";
					elif event.key == K_F4 and count_choice == 1:
						perso2 = Perso("broly_bas.png","broly_haut.png","broly_droite.png","broly_gauche.png",niveau,14*taille_sprite,0,14);
						count_choice += 1;
						nom_perso2 = "Broly";
					elif event.key == K_F5 and count_choice == 1:
						count_choice += 1;
						perso2 = Perso("cell_bas.png","cell_haut.png","cell_droite.png","cell_gauche.png",niveau,14*taille_sprite,0,14);
						nom_perso2 = "Cell";
					elif event.key == K_F6 and count_choice == 1:
						count_choice += 1;
						perso2 = Perso("freezer_bas.png","freezer_haut.png","freezer_droite.png","freezer_gauche.png",niveau,14*taille_sprite,0,14);
						nom_perso2 = "Freezer forme finale";
					elif event.key == K_F7 and count_choice == 1:
						count_choice += 1;
						perso2 = Perso("g_bas.png","g_haut.png","g_droite.png","g_gauche.png",niveau,14*taille_sprite,0,14);
						nom_perso2 = "Freese";
					elif event.key == K_F8 and count_choice == 1:
						count_choice += 1;
						perso2 = Perso("s2_bas.png","s2_haut.png","s2_droite.png","s2_gauche.png",niveau,14*taille_sprite,0,14);
						nom_perso2 = "Sangoku SS4";
					elif event.key ==K_F9 and count_choice == 1:
						count_choice += 1;
						perso2 = Perso("f_bas.png","f_haut.png","f_gauche.png","f_droite.png",niveau,14*taille_sprite,0,14);
						nom_perso2 = "Freezer éeme forme";
					elif count_choice == 2:
						continuer_selction = 0;

			pygame.display.flip();
		
		#on peut maintenant passer a la boucle de jeu
	while continuer_jeu:


		fond = pygame.image.load(image_fond).convert();
		
		delta = pygame.time.Clock().tick(30) / 1000.0;
		#on affiche le niveau a l'ecran
		niveau.afficher(fenetre);
		for event in pygame.event.get():	

			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):

				continuer_jeu = 0;

			elif event.type == KEYDOWN:

				"""deplacement de mario"""
				if event.key == K_RIGHT:

					perso1.deplacer('droite');


				elif event.key == K_UP:

					perso1.deplacer('haut');

				elif event.key == K_LEFT:

					perso1.deplacer('gauche');

				elif event.key == K_DOWN:

					perso1.deplacer('bas');

				"""deplacement de luigi"""

				if event.key == K_z:
					
					perso2.deplacer('haut');

				elif event.key == K_s:

					perso2.deplacer('bas');

				elif event.key == K_d:

					perso2.deplacer('droite');

				elif event.key == K_q:

					perso2.deplacer('gauche');

				elif event.key == K_KP0:
					missile = Missile(boule,niveau,perso1,perso1.direction);
					missile_ok = 1;

				elif event.key == K_a:

					missile2 = Missile(boule,niveau,perso2,perso2.direction);
					missile2_ok = 1;

				elif event.key == K_SPACE:
					continuer_pause = 1;
					while continuer_pause:
						for event in pygame.event.get():

							if event.type == KEYDOWN and event.key == K_SPACE:
								continuer_pause = 0;
						afficher_pause(fenetre);
						pygame.display.flip();
		#on rafraichit l'image a chaque tour de boucle
		fenetre.blit(fond, (0,0));
		niveau.afficher(fenetre);
		if missile_ok and missile2_ok and missile.ok and missile2.ok:
			missile.update();
			missile2.update();
			fenetre.blit(missile2.image,(missile2.x,missile2.y));
			fenetre.blit(missile.image,(missile.x,missile.y));
			pygame.display.flip();
			fenetre.blit(perso1.direction, (perso1.x,perso1.y));
			fenetre.blit(perso2.direction, (perso2.x,perso2.y));
		if missile_ok and missile.ok:
			missile.update();
			fenetre.blit(missile.image,(missile.x,missile.y));
			fenetre.blit(perso1.direction, (perso1.x,perso1.y));
			fenetre.blit(perso2.direction, (perso2.x,perso2.y));
		elif missile2_ok and missile2.ok:
			missile2.update();
			fenetre.blit(missile2.image,(missile2.x,missile2.y));
			fenetre.blit(perso1.direction, (perso1.x,perso1.y));
			fenetre.blit(perso2.direction, (perso2.x,perso2.y));
		
		fenetre.blit(perso1.direction, (perso1.x,perso1.y));
		fenetre.blit(perso2.direction, (perso2.x,perso2.y));
		pygame.display.flip();
		if (missile_ok and (missile.case_x == perso2.case_x) and (missile.case_y == perso2.case_y)):
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
				texte_victoire = font4.render("{} a gagne !!" .format(nom_perso1), 1,(255,255,255));
				texte_quitter = font4.render("Press ESCAPE to quit...", 1,(255,255,255));
				fenetre.blit(texte_victoire,(40,200));
				fenetre.blit(texte_quitter, (40,220));
				pygame.display.flip();

		elif (missile2_ok and (missile2.case_x == perso1.case_x) and (missile2.case_y == perso1.case_y)):

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
				texte_victoire = font4.render("{} a gagne !!" .format(nom_perso2), 1,(255,255,255));
				texte_quitter = font4.render("Press ESCAPE to quit...", 1,(255,255,255));
				fenetre.blit(texte_victoire,(40,200));
				fenetre.blit(texte_quitter, (40,220));
				pygame.display.flip();
