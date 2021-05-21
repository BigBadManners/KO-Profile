# KO-Profile
A Python script to aggregate CSVs containing your KO data for Super Smash Bros. Melee/Ultimate.

## Setup

As an example:

Trash,Opponent,Move(How),Kill%(When),Where,W/L
Banjo,Red(PT),Usmash,100,?,W
,,Fair,133,L,W
,,Utilt,145,?,W
,Claw(Inkling),Utilt,111,?,W
,,Usmash,127,?,W
,,Usmash,104,?,W
,,Usmash,117,?,W
,,SideB,72,L,W
,,Utilt,136,L,W

1st row: The player's tag, and field names.
2nd row+: The player's character(s), their opponent, the move they KO'd with, the % before the KO move, where the opponent was K.O'd on the stage (L - Ledgetrap/Corner Pressure; E - Edgeguard/2-frame, ? - Elsewhere), and win/loss ratio.
