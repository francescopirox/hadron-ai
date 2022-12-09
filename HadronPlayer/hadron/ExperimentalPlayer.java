package hadron;

import hadron.board.Board;
import hadron.board.ByteBoard;
import hadron.heuristic.Heuristic;
import hadron.heuristic.HeuristicImpl;
import hadron.research.GameController;
import hadron.research.GameControllerImpl;
import hadron.research.NegaSort;
import hadron.research.Research;

public class ExperimentalPlayer {
    private Heuristic heuristic;
    private GameController game;

    public ExperimentalPlayer( Heuristic h) {
        this.heuristic = h;
    }


    public void start(String ip, int port) {
        Board board = new ByteBoard();
        Research algorithm = new NegaSort();
        game = new GameControllerImpl(algorithm, heuristic, board, (byte)0, 930);
        new Communication(ip,port,game);
    }

    public static void main(String[] args) {
        double[] pesi= new double[]{Integer.parseInt(args[2]), Integer.parseInt(args[3]), Integer.parseInt(args[4]), Integer.parseInt(args[5]),Integer.parseInt(args[6])};
        Heuristic h = new HeuristicImpl(pesi);
        Player p1 = new Player(h);
        p1.start(args[0], Integer.parseInt(args[1]));


    }

    public GameController getGame() {
        return this.game;
    }


}