package GUI;

import java.awt.*;

/**
 * @author Shrujan Cheruku
 */


public class ChessBoardDisplay {

    //Using unicode characters for the chess pieces
    //Idea to do this is from http://stackoverflow.com/questions/7665120/displaying-chess-pieces-with-unicode-in-eclipse-using-java
    private static final char BLACK_PAWN = '\u265F';
    private static final char BLACK_ROOK = '\u265C';
    private static final char BLACK_KNIGHT = '\u265E';
    private static final char BLACK_BISHOP = '\u265D';
    private static final char BLACK_QUEEN = '\u265B';
    private static final char BLACK_KING = '\u265A';
    private static final char WHITE_PAWN = '\u2659';
    private static final char WHITE_ROOK = '\u2656';
    private static final char WHITE_KNIGHT = '\u2658';
    private static final char WHITE_BISHOP = '\u2657';
    private static final char WHITE_QUEEN = '\u2655';
    private static final char WHITE_KING = '\u2654';

    /**
     *Main function to display the board
     *Initializes the values and tiles
     *@param: none
     *@return: none
     **/
    public static void main(String[] args) {
        GUI gui = new GUI();
        //setup board as an array of tiles
        Tile[] board = new Tile[64];

        //iterate over the tiles, alternating the colors and adding pieces in their starting positions
        for (int row = 0; row <= 7; row++) {
            for (int column = 0; column <= 7; column++) {

                if ((column + row) % 2 == 0) {
                    board[row] = new Tile("", Color.WHITE);
                } else {
                    board[row] = new Tile("", Color.LIGHT_GRAY);
                }

                gui.mainframe.add(board[row].lbl);
                if (row == 6) {
                    board[row].lbl.setText("" + WHITE_PAWN);
                } else if (row == 1) {
                    board[row].lbl.setText("" + BLACK_PAWN);
                } else if (row == 7) {
                    switch (column) {
                        case 0:
                        case 7:
                            board[row].lbl.setText("" + WHITE_ROOK);
                            break;

                        case 1:
                        case 6:
                            board[row].lbl.setText("" + WHITE_KNIGHT);
                            break;

                        case 2:
                        case 5:
                            board[row].lbl.setText("" + WHITE_BISHOP);
                            break;

                        case 3:
                            board[row].lbl.setText("" + WHITE_QUEEN);
                            break;

                        case 4:
                            board[row].lbl.setText("" + WHITE_KING);
                            break;
                    }

                } else if (row == 0) {
                    switch (column) {
                        case 0:
                        case 7:
                            board[row].lbl.setText("" + BLACK_ROOK);
                            break;

                        case 1:
                        case 6:
                            board[row].lbl.setText("" + BLACK_KNIGHT);
                            break;

                        case 2:
                        case 5:
                            board[row].lbl.setText("" + BLACK_BISHOP);
                            break;

                        case 3:
                            board[row].lbl.setText("" + BLACK_QUEEN);
                            break;

                        case 4:
                            board[row].lbl.setText("" + BLACK_KING);
                            break;
                    }
                }
            }
        }
        gui.mainframe.setVisible(true);
    }
}
