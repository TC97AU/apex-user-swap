# apex-user-swap
A python script for swapping .cfg files between two users playing Apex Legends on the same computer.

# Modifications required:
Lines 7, 8, 10, & 11, require modifying per system.
- Change "YOUR_USER" to your system's username.
- Change "YOUR_PLAYER_1" to whatever name you'd like player 1 to have.
- Change "YOUR_PLAYER_2" to whatever name you'd like player 2 to have.

Place profile.cfg and settings.cfg files into cfg_store for both users with the format:
- profile_john.cfg
- settings_john.cfg
- profile_claire.cfg
- settings_claire.cfg.
Make sure the names you use are the same as the names you assigned in swap.py to player1 & player2.

current.txt should start with the same name as player1.
