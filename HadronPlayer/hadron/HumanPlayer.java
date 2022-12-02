package hadron;

import hadron.board.Board;
import hadron.board.ByteBoard;
import hadron.research.GameController;
import hadron.research.HumanGameController;

public class HumanPlayer {

    private GameController game;

    public HumanPlayer(){}


    public void start(String ip, int port) {
        Board board = new ByteBoard();
        game = new HumanGameController( board, (byte)0, 930);
        new Communication(ip,port,game);
    }

    public static void main(String[] args) {
        HumanPlayer p1 = new HumanPlayer();
        p1.start(args[0], Integer.parseInt(args[1]));
    }

    public GameController getGame() {
        return this.game;
    }
}
