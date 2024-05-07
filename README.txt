Summary:
This is a game where the user can play chess. To an extent. You play as a white pawn, and must capture enemy pawns without getting stuck. Do this and complete the objective to progress. Upon completing your first objective, you will be upgraded to queen. Queens have more moves than pawns. Upon completing your second objective, you will be able to return through the portals back home via a new button on your screen.

Instructions/Rules:
1) Pawns can only move forwards, but can attack diagonally forwards.
2) If you pawn is on the second row, it has the ability to move forwards twice in one turn, as per the rules of chess.
3) We have not coded En Passant, mainly because the black pawns do not actually move.
4) A "show path" button has been implemented if you are ever worried about being unable to find the path to the portal. This function is also called on map generation to make sure the pawn starts from a solvable position.
5) Queens can move in all 8 directions (forwards, backwards, left, right, and along all four diagonals) and can move an infinite distance.
6) To choose the length of the queens movement, select the distance along green number pad buttons. It will turn orange to show the distance has been saved. This number rewrites all direction buttons, and will move your queen in that direction, provided there are no obsicals in the way. It is also the number that indicates how many worlds back in time you travel. 
7) You may land on a pawn to capture it in any direction.
8) To travel through a portal, land on anywhere along the 8th row as either piece. This will bring you to a new room with new enemies to kill. 

The data types we have implemented are Array, Stack, and Queue:
  The Array was utilized to hold the data for all enemy positions. When you generate a new room, a new enemy array is generated. And then added to a stack, which brings us to our second data type.
  This can be justified because we need to be able to access any element in the array at any given time, and because we already know the index based on the user's piece location, there is no need for a queue for order 1 retrieval.
  The Stack was utilized to hold the data for all enemy Arrays of previous rooms. Because the portals themselves and the background do not need to change, this information was not stored in the stack. The stack is popped every time you travel back a room, but pushed every time you enter a portal. So popping will lose your current room permanantly.
  This can be justified because a stack is necessary for the storage of data which needs to be retrieved in a First-in-last-out basis. The rooms must be retrieved on this basis, so a Stack is necessary.
  The Queue was used to store the image objects of our portals. This was used to store the portal images at any given room. This queue is rewritten for each room upon entering, either forwards or backwards.
  This can be justified (sort of) because the Queue which stores the portals gives us an opportunity to potentially add features in the future which may utilize the Queue data type. Admittedly, it isn't really needed now, but it could be in the future.

  
