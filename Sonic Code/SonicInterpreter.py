#sys et os pour interaction système, 

import sys
import os
import random
import json
import time
from typing import Dict, List, Tuple, Any, Optional
from antlr4 import *
from antlr4.tree.Tree import TerminalNode

# Import des classes générées par ANTLR
from SonicRPGLexer import SonicRPGLexer
from SonicRPGParser import SonicRPGParser
from SonicRPGVisitor import SonicRPGVisitor

#classe des données de jeu (objet, map, inventaire santé..)
class GameState:
    """Classe pour gérer l'état du jeu Sonic RPG"""
    
    def __init__(self):
        # Position de Sonic sur la grille (10x10)
        self.x = 0
        self.y = 0
        self.max_x = 9
        self.max_y = 9
        
        # Statistiques du joueur
        self.rings = 0
        self.speed_tokens = 0
        self.speed_multiplier = 1
        self.health = 100
        
        # État du jeu
        self.boss_unlocked = False
        self.boss_defeated = False
        self.game_over = False
        self.rings_needed_for_boss = 5  
        
        # Inventaire et objets
        self.inventory = []
        self.checkpoints = [(0, 0)]  # Checkpoint initial
        
        # Map du monde (objets sur la grille)
        self.world_map = self._generate_world()
        
        # Variables utilisateur
        self.variables = {}
        
        # Événements spéciaux
        self.events_triggered = set()
    
    def _generate_world(self) -> Dict[Tuple[int, int], List[str]]:
        """Génère une map du monde avec des objets dispersés"""
        world = {}
        
        # Placement des rings (plus nombreux pour faciliter le jeu)
        ring_positions = [
            (1, 1), (3, 2), (5, 1), (7, 3), (2, 8), (4, 6), 
            (6, 1), (7, 8), (2, 3), (8, 2)
        ]
        for pos in ring_positions:
            if pos not in world:
                world[pos] = []
            world[pos].append('RING')

        # Placement des speed tokens
        token_positions = [(2, 4), (6, 8),]
        for pos in token_positions:
            if pos not in world:
                world[pos] = []
            world[pos].append('SPEED_TOKEN')

        
        # Placement des checkpoints
        checkpoint_positions = [(0, 5), (5, 0), ]
        for pos in checkpoint_positions:
            if pos not in world:
                world[pos] = []
            world[pos].append('CHECKPOINT')
        
        # Zone du boss au centre
        world[(5, 5)] = world.get((5, 5), []) + ['BOSS_AREA']
        # Objets spéciaux
        for pos in [(0, 9), (5, 6), (2, 3), (8, 2)]:
        # Coffres spéciaux avec peluches
            world[(0, 9)] = ['TRESOR', 'PLUSH_TAILS']
            world[(5, 6)] = ['TRESOR', 'PLUSH_KNUCKLES']
            world[(2, 3)] = ['TRESOR', 'PLUSH_AMY']
            world[(8, 2)] = ['TRESOR', 'PLUSH_SHADOW']
        chili_dog_positions = [(7, 2), (1, 7), (9, 1)]
        for pos in chili_dog_positions:
            if pos not in world:
                world[pos] = []
            world[pos].append('CHILI_DOG')


        return world
    

    def get_current_position_objects(self) -> List[str]:
        objects = self.world_map.get((self.x, self.y), [])
        if objects:
            # Special message for BOSS_AREA at (5,5)
            if (self.x, self.y) == (5, 5) and 'BOSS_AREA' in objects:
                print(" ❗ Sonic est face à Eggman : BOSS_AREA \n Essayez de taper : FIGHT BOSS;")
            # Show collect hints for other objects, but never for BOSS_AREA or PLUSH_
            visible = [o for o in objects if not o.startswith('PLUSH_') and o != 'BOSS_AREA']
            if visible:
                print("Sonic remarque quelque chose ici :", ', '.join(visible))
                print("Essayez de taper : COLLECT " + " / ".join(o.upper() for o in visible) + ";")
        return objects

    
    def remove_object_at_position(self, obj_type: str):
        """Retire un objet de la position actuelle"""
        if (self.x, self.y) in self.world_map:
            if obj_type in self.world_map[(self.x, self.y)]:
                self.world_map[(self.x, self.y)].remove(obj_type)
    
    def check_boss_unlock(self):
        """Vérifie si Eggman est déjà présent"""
        if self.rings >= self.rings_needed_for_boss and not self.boss_unlocked:
            self.boss_unlocked = True
            print(f"ENFIN PRÊT POUR TE BATTRE !! T'AS COLLECTE {self.rings} RINGS (minimum: {self.rings_needed_for_boss})")
            print("Si tu veux trouver Eggman sans l'aide d'un GPS de Tails, je te conseille d'aller au milieu de la map...")
    
    def display_status(self):
        """Affiche l'état actuel du jeu"""
        print(f"\n{'='*40}")
        print(f"🦔 SONIC - STATUT")
        print(f"{'='*40}")
        print(f"Position: ({self.x}, {self.y})")
        print(f"Rings: {self.rings}/{self.rings_needed_for_boss}")
        print(f"⚡ Speed Tokens: {self.speed_tokens}")
        print(f" ❗ Multiplicateur vitesse: x{self.speed_multiplier}")
        print(f"PV, il n'y a pas de chili dogs dans le coin pour oublier la douleur...: {self.health}/100")
        print(f"Eggman trouvé :{' Oui' if self.boss_unlocked else 'Pas encore..'}")
        print(f"Eggman battu   : {' Oui' if self.boss_defeated else 'Pas encore..'}")
        
        objects = self.get_current_position_objects()
        print(f"Objets ici: {', '.join(objects) if objects else 'Aucun'}")
        
        if self.inventory:
            print(f"Inventaire: {', '.join(self.inventory)}")

        print(f"Checkpoints: {len(self.checkpoints)} activés")
        print(f"{'='*40}\n")
    
    def display_map(self):
        print(f"\n{'='*50}")
        print(f"MAP DE GREEN HILL")
        print(f"{'='*50}")
        print("   ", end="")
        for x in range(10):
            print(f" {x} ", end="")
        print()
        
        for y in reversed(range(10)):
            print(f" {y} ", end="")
            for x in range(10):
                if self.x == x and self.y == y:
                    print("🦔 ", end=" ") 
                elif (x, y) in self.world_map and self.world_map[(x, y)]:
                    obj = self.world_map[(x, y)][0]
                    if obj == 'RING':
                        print("💍", end=" ")
                    elif obj == 'SPEED_TOKEN':
                        print("⚡", end=" ")
                    elif obj == 'CHECKPOINT':
                        print("🏁", end=" ")
                    elif obj == 'BOSS_AREA':
                        print("👹", end=" ")
                    elif obj == 'TRESOR':
                        print("🎁", end=" ")
                    elif obj == 'CHILI_DOG':
                        print("🌭", end=" ")
                    else:
                        print("⬜", end=" ")

                else:
                    print("⬜", end=" ")
            print()
        
        print(f"🦔 = Sonic  💍 = Ring  ⚡ = Speed Token  🏁 = Checkpoint")
        print(f"👹 = Eggman  🎁 = Trésor    🌭= Chili Dog")
        print(f"{'='*50}\n")

# classe principale qui interprète et exécute chaque commande du joueur.
class SonicCommandExecutor(SonicRPGVisitor):
    """Visitor personnalisé pour exécuter les commandes du jeu Sonic RPG"""

    def __init__(self, game):
        self.game = game
        self.game_state = game.game_state
        self.variables = self.game_state.variables

    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)

    def visitMoveStatement(self, ctx):
        direction = ctx.direction().getText().upper()
        steps = 1
        
        steps = self.game_state.speed_multiplier  # par défaut
        if ctx.NUMBER():
            steps = int(ctx.NUMBER().getText()) * self.game_state.speed_multiplier


        print(f" MOVE {direction} ({steps} step(s))")

        moves_made = 0
        for _ in range(steps):
            old_x, old_y = self.game_state.x, self.game_state.y

            if direction in ['DOWN', 'SOUTH']:
                if self.game_state.y > 0:
                    self.game_state.y -= 1
                    moves_made += 1
            elif direction in ['UP', 'NORTH']:
                if self.game_state.y < self.game_state.max_y:
                    self.game_state.y += 1
                    moves_made += 1
            elif direction in ['LEFT', 'WEST']:
                if self.game_state.x > 0:
                    self.game_state.x -= 1
                    moves_made += 1
            elif direction in ['RIGHT', 'EAST']:
                if self.game_state.x < self.game_state.max_x:
                    self.game_state.x += 1
                    moves_made += 1
            else:
                print(f" La terre est ronde, mais ta map est plate ! tu ne peux pas la dépasser.({direction})")
                break

        if moves_made > 0:
            print(f" Sonic s'est déplacé de {moves_made} case(s) vers {direction}")
            print(f" Nouvelle position: ({self.game_state.x}, {self.game_state.y})")


    def visitWaitStatement(self, ctx):
        if ctx.NUMBER():
            duration = int(ctx.NUMBER().getText())
        else:
            duration = 1

        print(f"💤 Sonic fait la sieste pendant {duration} seconde(s)...")
        for i in range(duration):
            time.sleep(1)
            if self.game_state.health < 100:
                self.game_state.health = min(100, self.game_state.health + 5)
                print(f" +5 PV → {self.game_state.health}/100")
            else:
                print("❗ PV déjà au max !")
                break

    def visitCollectStatement(self, ctx):
        target = ctx.collectTarget().getText().upper()
        # objects_here = self.game_state.get_current_position_objects()
        objects_here = self.game_state.world_map.get((self.game_state.x, self.game_state.y), [])

        if target in ['RING', 'RINGS']:
            if 'RING' in objects_here:
                self.game_state.remove_object_at_position('RING')
                self.game_state.rings += 1
                print(f"💍 Ring collecté! Total: {self.game_state.rings}")
                print(f"✅ COLLECT {target}")
                self.game_state.check_boss_unlock()
            else:
                print("❌ Aucun ring à collecter ici!")

        elif target == 'SPEED_TOKEN':
            if 'SPEED_TOKEN' in objects_here:
                self.game_state.remove_object_at_position('SPEED_TOKEN')
                self.game_state.inventory.append('SPEED_TOKEN')
                self.game_state.speed_tokens += 1
                print("⚡ SPEED_TOKEN rammassé, tu peux le trouver dans ton inventaire !")
            else:
                print(" Aucun SPEED_TOKEN ici.")

        elif target == 'CHILI_DOG':
            if 'CHILI_DOG' in objects_here:
                self.game_state.remove_object_at_position('CHILI_DOG')
                self.game_state.inventory.append('CHILI_DOG')
                print("🌭 CHILI_DOG dévoré ! Tu sens que l'énergie revient...")
            else:
                print(" Aucun CHILI_DOG ici.")

        elif target == 'TRESOR':
            plushes = [o for o in objects_here if o.startswith('PLUSH_')]
            if 'TRESOR' in objects_here and plushes:
                plush = plushes[0]
                self.game_state.remove_object_at_position('TRESOR')
                self.game_state.remove_object_at_position(plush)
                self.game_state.inventory.append(plush)
                print(f"🎁 Trésor ouvert! Tu obtiens la peluche de {plush.replace('PLUSH_', '')}!")
            else:
                print(" Ne sois pas trop gourmand, tu as déjà eu cette surprise")

 
    def visitUseStatement(self, ctx):
        item = ctx.useTarget().getText().upper()

        if item == 'SPEED':
            if 'OFF' in ctx.getText().upper():
                self.game_state.speed_multiplier = 1
                print("❗Mode vitesse désactivé. Retour à la vitesse normale.")
            elif 'SPEED_TOKEN' in self.game_state.inventory:
                self.game_state.inventory.remove('SPEED_TOKEN')
                self.game_state.speed_multiplier += 1
                print(f"⚡ Token de vitesse utilisé! Multiplicateur: {self.game_state.speed_multiplier}")
            else:
                print(" Tu n'as pas de token de vitesse ")

        elif item in ['TOKEN', 'SPEED_TOKEN']:
            if 'SPEED_TOKEN' in self.game_state.inventory:
                self.game_state.inventory.remove('SPEED_TOKEN')
                self.game_state.speed_multiplier += 1
                print(f"⚡ Token de vitesse utilisé! Multiplicateur: {self.game_state.speed_multiplier}")
            else:
                print("Tu n'a pas de token de vitesse")

        elif item == 'CHECKPOINT':
            self.game_state.checkpoints.append((self.game_state.x, self.game_state.y))
            print(f"📍 Checkpoint sauvegardé à ({self.game_state.x}, {self.game_state.y})")

        else:
                print(f"❌ Objet inconnu: {item}")


    def visitFightStatement(self, ctx):
        if not self.game_state.boss_unlocked:
            print("Tu n'as pas assez de ring pour battre Eggman!")
            print(f"Ramasse {self.game_state.rings_needed_for_boss - self.game_state.rings} rings supplémentaires")
            return
        # Avoid printing BOSS_AREA hint here
        if 'BOSS_AREA' not in self.game_state.world_map.get((self.game_state.x, self.game_state.y), []):
            print(" Tu n'es pas dans la zone d'Eggman ! Va au centre de la map (5,5)")
            return
        print(" ❗ COMBAT COTNRE EGGMAN ! ⚔️")
        time.sleep(1)
        sonic_power = (self.game_state.rings * 2) + (self.game_state.speed_multiplier * 15) + (self.game_state.health // 2)
        boss_power = random.randint(60, 100)
        print(f"Puissance de Sonic: {sonic_power}, Eggman: {boss_power}")
        time.sleep(2)
        if sonic_power >= boss_power:
            print("VICTOIRE ! Sonic a vaincu le boss!")
            self.game_state.boss_defeated = True
            self.game_state.game_over = True
        else:
            damage = random.randint(20, 40)
            self.game_state.health = max(0, self.game_state.health - damage)
            print(f"DÉFAITE ! Sonic perd {damage} PV. Santé: {self.game_state.health}/100")
            if self.game_state.health <= 0:
                print(" Sonic est K.O. Game Over...💀")
                self.game_state.game_over = True

    def visitSayStatement(self, ctx):
        msg = ctx.STRING().getText()[1:-1]
        print(f"Sonic: {msg}")

    def visitStatusStatement(self, ctx):
        self.game_state.display_status()

    def visitMapStatement(self, ctx):
        self.game_state.display_map()

    def visitHelpStatement(self, ctx):
        print("\n❗ COMMANDES DISPONIBLES:")
        print("  MOVE <direction> [steps];")
        print("  COLLECT <item>;\n  USE <item>;\n  FIGHT BOSS;\n  SAY \"message\";\n  IF (...) { ... } [ELSE { ... }] ENDIF;\n  LOOP [N] { ... } ENDLOOP;\n  EXIT;\n  STATUS;\n  MAP;\n  HELP;")

    def visitExitStatement(self, ctx):
        print(" Merci d'avoir joué ! À bientôt!")
        self.game.running = False

    def visitExpressionStatement(self, ctx):
        expr = ctx.expression()
        if expr.getChildCount() == 3 and expr.getChild(1).getText() in ['=', '==']:
            var_name = expr.getChild(0).getText()
            value = self.visit(expr.getChild(2))
            self.variables[var_name] = value
            print(f"Variable '{var_name}' mise à jour: {value}")
        else:
            self.visit(expr)

    def visitIfStatement(self, ctx):
        cond = self.visit(ctx.condition())
        if cond:
            for stmt in ctx.statement():
                self.visit(stmt)
        elif ctx.ELSE():
            for stmt in ctx.statement()[len(ctx.statement())//2:]:
                self.visit(stmt)

    def visitLoopStatement(self, ctx):
        count = 1
        if ctx.NUMBER():
            count = int(ctx.NUMBER().getText())
        for _ in range(count):
            for stmt in ctx.statement():
                self.visit(stmt)
#VISIT QUI SERVENT SURTOUT SEULEMENT SI JOUEUR VEUT TESTER LES EXPRESSIONS HABITUEL (reprise des séries vu en classe comme pour calculette)
    def visitCondition(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            op = ctx.compareOp().getText()
            return {
                '>': left > right,
                '<': left < right,
                '>=': left >= right,
                '<=': left <= right,
                '==': left == right,
                '=': left == right,
                '!=': left != right,
                '<>': left != right,
            }.get(op, False)
        else:
            return bool(self.visit(ctx.expression(0)))

    def visitExpression(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            op = ctx.getChild(1).getText()
            return {
                '+': left + right,
                '-': left - right,
                '*': left * right,
                '/': left // right if right != 0 else 0
            }.get(op, 0)
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.atom())
        elif ctx.getChildCount() == 2:
            return self.visit(ctx.expression(0))
        elif ctx.getChildCount() == 0:
            return 0

    def visitAtom(self, ctx):
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        elif ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            return self.variables.get(name, 0)
        elif ctx.gameProperty():
            prop = ctx.gameProperty().getText().lower()
            if prop == 'rings':
                return self.game_state.rings
            elif prop == 'speed':
                return self.game_state.speed_multiplier
            elif prop == 'x':
                return self.game_state.x
            elif prop == 'y':
                return self.game_state.y
            elif prop == 'boss_unlocked':
                return self.game_state.boss_unlocked
            elif prop == 'game_over':
                return self.game_state.game_over
            else:
                return 0


class SonicRPGGame: 
    def __init__(self):
        self.game_state = GameState()
        self.running = True
        self.command_executor = SonicCommandExecutor(self)
    
    def start_game(self):
        """Démarre le jeu interactif"""
        self._display_welcome()
        
        while self.running and not self.game_state.game_over:
            try:
                # Afficher le prompt
                command = input(f"🦔 [{self.game_state.x},{self.game_state.y}] Sonic> ").strip()
                
                if not command:
                    continue
                
                # Parser et exécuter la commande via ANTLR
                if not command.endswith(';'):
                    command += ';'
                self._execute_command(command)

                
                # Vérifier les événements spéciaux
                self._check_special_events()
                
            except KeyboardInterrupt:
                print("\n\n Merci d'avoir sauvé Green Hill 💚")
                break
            except EOFError:
                print("\n\nMerci d'avoir sauvé Green Hill 💚")
                break
            except Exception as e:
                print(f" Erreur: {e}")
        
        if self.game_state.boss_defeated:
            self._display_victory()
        
        print("Fin de l'aventure!")
    
    def _display_welcome(self):
        """Affiche le message de bienvenue"""
        print("🌟" + "="*60 + "🌟")
        print("🦔" + " "*20 + "SONIC RPG ADVENTURE" + " "*20 + "🦔")
        print("🌟" + "="*60 + "🌟")
        print()
        print("📜 HISTOIRE:")
        print("   Sonic doit collecter des rings dans Green Hill pour sauver la nature")
        print("   pour vaincre EGGMAN")
        print()
        print("OBJECTIF:")
        print("💡 TAPEZ 'HELP' pour voir toutes les commandes disponibles")
        print("💡 TAPEZ 'MAP' pour voir la carte du monde")
        print("💡 TAPEZ 'STATUS' pour voir votre état actuel")
        print()
        
        # Afficher le statut initial
        self.game_state.display_status()
    
    def _display_victory(self):
        """Affiche le message de victoire"""
        print("\n🎉" + "="*50 + "🎉")
        print("🏆" + " "*15 + "FÉLICITATIONS!" + " "*15 + "🏆")
        print("🎉" + "="*50 + "🎉")
        print()
        print("🦔 Sonic a vaincu le boss et sauvé le MONDE (Amy)")
        print(f"💍 Rings collectés: {self.game_state.rings}")
        print("Vous méritez un chili dog en guise de récompense")
        print()
    
    def _execute_command(self, command: str):
        """Parse et exécute une commande utilisateur via ANTLR"""
        try:
            # Créer le flux d'entrée ANTLR
            input_stream = InputStream(command)
            
            # Créer le lexer
            lexer = SonicRPGLexer(input_stream)
            
            # Créer le flux de tokens
            stream = CommonTokenStream(lexer)
            
            # Créer le parser
            parser = SonicRPGParser(stream)
            
            # Parser le programme (point d'entrée de la grammaire)
            tree = parser.program()
            
            # Exécuter via le visitor
            self.command_executor.visit(tree)
            
        except Exception as e:
            print(f"Commande non reconnue ou erreur de syntaxe: {e}")
            print("💡 Tapez 'HELP' pour voir les commandes disponibles")
    
    def _check_special_events(self):
        """Vérifie les événements spéciaux"""
        # Événement de collecte automatique de checkpoint
        objects = self.game_state.get_current_position_objects()
        if 'CHECKPOINT' in objects and (self.game_state.x, self.game_state.y) not in self.game_state.checkpoints:
            self.game_state.checkpoints.append((self.game_state.x, self.game_state.y))
            print(" Checkpoint automatiquement sauvegardé!")
        
        # Vérification de la santé critique
        if self.game_state.health <= 20 and 'low_health_warning' not in self.game_state.events_triggered:
            print("⚠️ Attention! Votre santé est critique! Utilisez WAIT pour récupérer.")
            self.game_state.events_triggered.add('low_health_warning')


if __name__ == "__main__":
    game = SonicRPGGame()
    game.start_game()