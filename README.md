# KO-Profile
A Python script to aggregate CSVs containing your KO data for Super Smash Bros. Melee/Ultimate. Requires Matplot, Pandas, and Numpy.

## Setup - Example CSV

Trash,Opponent,Move(How),Kill%(When),Where,W/L

Banjo,Red(PT),Usmash,100,?,W

,,Fair,133,L,W

,,Utilt,145,?,W

,Claw(Inkling),Utilt,111,?,W

,,Usmash,127,?,W

,,Usmash,104,?,W

,,Usmash,117,?,W

,,SideB,72,L,W

,,Utilt,136,L,W\n


1st row: The player's tag, and field names.
2nd row+: The player's character(s), their opponent, the move they KO'd with, the % before the KO move, where the opponent was K.O'd on the stage (L - Ledgetrap/Corner Pressure; E - Edgeguard/2-frame, ? - Elsewhere), and win/loss ratio.

You may include all of your characters, but this might skew the results depending on how early each of your characters K.O.

## Why are these statistics useful?

I take my main points from Shimi's page here https://shimigames.com/how-when-where-smash-pros-kill/ because they're smart and know how to parse statistics to create tangible and applicable theories in-game.

* Understanding when and where you score KOs with your character is a good metric for understanding how well you understand them. If you find your character killing at extremely high %s, that is usually an indicator that you, the player, are struggling to kill because you could be practicing and implementing your character's kill setups more. Say if you play R.O.B. - you have all these wonderful tools at your disposal, and a bevvy of TODs - if you find yourself killing with ROB at 150, 170, even 200%, is that a R.O.B. problem, or a *you* problem?
* The goal of aggregating your K.O. data is to create theories about your character's neutral, advantage, and disadvantage, that will help you lower the average KO %. The less you are in the 125-150 and 150+ categories, the better. The 'theory' comes from your understanding of the game right now, and can be pretty much anything, but usually, it's a good idea to base theories on the scientific model. As you continue to play and get better, you should see your average KO % decrease.
* For top players, over half to two thirds of all K.Os are scored through edgeguards or ledgetrapping/corner pressure, and so pushing your opponent into these situations is something to focus on. These situations limit the opponent's stage control and put you in advantage. Maintain stage control, increase your chance of killing, and of killing **earlier**
* Each character's data will vary depending on your strengths, and it's important to ask better players where those strengths lie. As an example, Pac-Man will score a lot of K.Os with Bell->Fsmash at centrestage or through ledgetrapping, but you might not see him K.O. as much through edgeguard attempts.
