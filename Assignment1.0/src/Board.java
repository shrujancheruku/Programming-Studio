import java.awt.*;

/**
 * @author Shrujan Cheruku
 *         A board class. This controls the gameplay.
 */

class Board {
    //board dimensions that the entire game uses
    //TODO add user input to change these values
    static final int height = 7;
    static final int width = 7;
    //the game board itself is an array of Pieces
    private Piece[][] gameBoard;

   /*
   *Constructor for the Board class.
   *Initializes the gameBoard array and calls setupPieces()
   *@param: none
   *@return: none
   */
    Board() {
        //initializing the game board
        gameBoard = new Piece[height+1][width+1];
        setupPieces();
    }

   /*
   *Sets up the gameBoard array with the right pieces and positions
   *Fills the gaps with blank spaces
   *@param: none
   *@return: none
   */
    void setupPieces(){
        //adding the row of white pawns on the second bottommost row
        for(int whitePawns = 0; whitePawns <= width; whitePawns++){
            gameBoard[whitePawns][1] = new Pawn(true, new Point(whitePawns, 1));
        }

        //adding the row of black pawns on the second topmost row
        for(int blackPawns = 0; blackPawns <= width; blackPawns++){
            gameBoard[blackPawns][height - 1] = new Pawn(true, new Point(blackPawns, height - 1));
        }

        //adding the white pieces on the bottommost row
        gameBoard[0][0] = new Rook(true, new Point(0, 0));
        gameBoard[1][0] = new Knight(true, new Point(1, 0));
        gameBoard[2][0] = new Bishop(true, new Point(2, 0));
        gameBoard[3][0] = new Queen(true, new Point(3, 0));
        gameBoard[4][0] = new King(true, new Point(4, 0));
        gameBoard[5][0] = new Bishop(true, new Point(5, 0));
        gameBoard[6][0] = new Knight(true, new Point(6, 0));
        gameBoard[7][0] = new Rook(true, new Point(7, 0));

        //adding the black pieces on the topmost row
        gameBoard[0][height] = new Rook(false, new Point(0, height));
        gameBoard[1][height] = new Knight(false, new Point(1, height));
        gameBoard[2][height] = new Bishop(false, new Point(2, height));
        gameBoard[3][height] = new Queen(false, new Point(3, height));
        gameBoard[4][height] = new King(false, new Point(4, height));
        gameBoard[5][height] = new Bishop(false, new Point(5, height));
        gameBoard[6][height] = new Knight(false, new Point(6, height));
        gameBoard[7][height] = new Rook(false, new Point(7, height));

        //iterate over the entire board
        for(int i = 0; i < width; i++){
            for (int j = 0; j < height; j++){
                //ignore a spot if there is already a piece there
                if(gameBoard[i][j] instanceof Piece) {
                    continue;
                }
                //fill in the blank spaces with Blank objects
                gameBoard[i][j] = new Blank(new Point(i , j));
            }
        }
    }

   /*
   *This function takes in the starting and ending points to move a piece
   *Checks to see whether that move is possible
   *@param: the two Points, startPosition and movePosition
   *@return: true if the move happens, false if it's not possible
   */
   boolean movePiece(Point startPosition, Point movePosition) {
       //TODO add logic for checking if the legal move is blocked by any piece

       if (gameBoard[movePosition.x][movePosition.y] instanceof Blank) {
           if (gameBoard[startPosition.x][startPosition.y].move(movePosition)) {

               gameBoard[movePosition.x][movePosition.y] = gameBoard[startPosition.x][startPosition.y];
               gameBoard[startPosition.x][startPosition.y] = new Blank(startPosition);

               return true;
           }
       } else if (gameBoard[movePosition.x][movePosition.y].getIsWhite() != gameBoard[startPosition.x][startPosition.y].getIsWhite()) {
           if (gameBoard[startPosition.x][startPosition.y].move(movePosition)) {

               gameBoard[movePosition.x][movePosition.y] = gameBoard[startPosition.x][startPosition.y];
               gameBoard[startPosition.x][startPosition.y] = new Blank(startPosition);

               return true;
           }
       }

       return false;
   }

   /*
   *Helper function to add the x and y coordinates of two Points
   *@param: the two Points to be added, a and b
   *@return: the summation of a and b
   */
    static Point addPoints(Point a, Point b) {
        return new Point((int)(a.getX() + b.getX()), (int)(a.getY() + b.getY()));
    }
}
