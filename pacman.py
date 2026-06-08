# 4you-pacman.py


import os
import time
import sys

# Das Spielfeld (Matrix)
# # = Wand, . = Punkt, P = Pac-Man, G = Geist
spielfeld = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "P", ".", ".", ".", "#", ".", ".", ".", ".", ".", "#"],
    ["#", ".", "#", "#", ".", "#", ".", "#", "#", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "G", "#"],
    ["#", "#", "#", ".", "#", "#", "#", ".", "#", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

# Start-Positionen extrahieren
p_zeile, p_spalte = 1, 1
g_zeile, g_spalte = 3, 10
score = 0

def spielfeld_zeichnen():
    # Löscht die Terminal-Ausgabe, damit es flüssig animiert wirkt
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"🏆 SCORE: {score} Punkte | Steuerung: w (hoch), s (runter), a (links), d (rechts) + Enter\n")
    
    for zeile in spielfeld:
        print(" ".join(zeile))
    print("\nDrücke 'q' und Enter zum Beenden.")

# Spiel-Loop
while True:
    spielfeld_zeichnen()
    
    # Benutzereingabe abfangen
    zug = input("➡️ Wohin bewegen? (w/a/s/d): ").lower()
    
    if zug == 'q':
        print("Spiel beendet. Bis zum nächsten Mal! 👋")
        break
        
    # Zielkoordinaten berechnen
    neue_p_zeile, neue_p_spalte = p_zeile, p_spalte
    
    if zug == 'w': neue_p_zeile -= 1   # hoch
    elif zug == 's': neue_p_zeile += 1 # runter
    elif zug == 'a': neue_p_spalte -= 1 # links
    elif zug == 'd': neue_p_spalte += 1 # rechts
    else: continue # Ungültige Taste -> Loop von vorn
    
    # Kollisionsabfrage: Ist da eine Wand (#)?
    if spielfeld[neue_p_zeile][neue_p_spalte] != "#":
        # Wenn da ein Punkt ist, Score erhöhen
        if spielfeld[neue_p_zeile][neue_p_spalte] == ".":
            score += 10
            
        # Alte Position leeren
        spielfeld[p_zeile][p_spalte] = " "
        
        # Neue Position setzen
        p_zeile, p_spalte = neue_p_zeile, neue_p_spalte
        
        # Prüfen, ob wir in den Geist gelaufen sind
        if p_zeile == g_zeile and p_spalte == g_spalte:
            spielfeld_zeichnen()
            print("👾 OH NEIN! Der Geist hat dich geschnappt! GAME OVER 💀")
            break
            
        spielfeld[p_zeile][p_spalte] = "P"

    # Eine ganz einfache KI für den Geist (G): Er bewegt sich langsam auf Pac-Man zu
    spielfeld[g_zeile][g_spalte] = "." # Alte Geist-Position temporär mit Punkt füllen
    if g_zeile < p_zeile and spielfeld[g_zeile+1][g_spalte] != "#": g_zeile += 1
    elif g_zeile > p_zeile and spielfeld[g_zeile-1][g_spalte] != "#": g_zeile -= 1
    elif g_spalte < p_spalte and spielfeld[g_zeile][g_spalte+1] != "#": g_spalte += 1
    elif g_spalte > p_spalte and spielfeld[g_zeile][g_spalte-1] != "#": g_spalte -= 1
    
    # Hat der Geist Pac-Man erwischt?
    if g_zeile == p_zeile and g_spalte == p_spalte:
        spielfeld_zeichnen()
        print("👾 Der Geist war schneller! GAME OVER 💀")
        break
        
    spielfeld[g_zeile][g_spalte] = "G"
