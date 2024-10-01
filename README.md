# Summary:
This is a game where the user can play chess. To an extent. You play as a white pawn, and must capture enemy pawns without getting stuck. Do this and complete the objective to progress. Upon completing your first objective, you will be upgraded to queen. Queens have more moves than pawns. Upon completing your second objective, you will be able to return through the portals back home via a new button on your screen.

# Instructions/Rules:
1) Pawns can only move forwards, but can attack diagonally forwards.
2) If your pawn is on the second row, it has the ability to move forwards twice in one turn, as per the rules of chess.
3) We have not coded En Passant, mainly because the black pawns do not actually move.
4) A "show path" button has been implemented if you are ever worried about being unable to find the path to the portal. This function is also called on map generation to make sure the pawn starts from a solvable position.
5) Queens can move in all 8 directions (forwards, backwards, left, right, and along all four diagonals) and can move an infinite distance.
6) To choose the length of the queen's movement, select the distance along green number pad buttons. It will turn orange to show the distance has been saved. This number rewrites all direction buttons and will move your queen in that direction, provided there are no obstacles in the way. It is also the number that indicates how many worlds back in time you travel.
7) You may land on a pawn to capture it in any direction.
8) To travel through a portal, land anywhere along the 8th row as either piece. This will bring you to a new room with new enemies to kill.

# Data Structures:

The data types we have implemented are **Array**, **Stack**, and **Queue**:

- **Array:** Utilized to hold the data for all enemy positions. When you generate a new room, a new enemy array is generated and then added to a stack, which brings us to our second data type.
  - This is justified because we need to access any element in the array at any given time, and because we already know the index based on the user's piece location, there is no need for a queue for O(1) retrieval.
  
- **Stack:** Utilized to hold the data for all enemy arrays of previous rooms. The portals themselves and the background do not need to change, so this information is not stored in the stack. The stack is popped every time you travel back a room, but pushed every time you enter a portal. Popping will permanently lose your current room.
  - This is justified because a stack is necessary for the storage of data that needs to be retrieved in a First-in-Last-out (FILO) basis. The rooms must be retrieved on this basis, so a stack is necessary.
  
- **Queue:** Used to store the image objects of our portals. This queue is rewritten for each room upon entering, either forwards or backwards.
  - This is justified (sort of) because the queue storing the portals gives us an opportunity to potentially add features in the future that may utilize the queue data type. Admittedly, it isn't really needed now, but it could be in the future.
