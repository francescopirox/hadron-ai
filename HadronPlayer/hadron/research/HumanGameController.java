package hadron.research;

import hadron.board.Board;

import java.util.Scanner;

public class HumanGameController  implements GameController{
    private Board board;
    private byte col;

    public HumanGameController(Board board, byte col, int i) {
        this.board=board;
        this.col=col;
    }

    @Override
    public Node nextMove(Board board) {
        int iRiga=0;
        int iColonna=0;

        System.out.println("Inserisci una mossa:");
        Scanner scanner=new Scanner(System.in);
        iRiga= new Integer(scanner.nextLine());
        iColonna = new Integer(scanner.nextLine());
        return new Node(board, iRiga ,iColonna, this.col);
    }

    @Override
    public void updateGame(String move) {

    }

    @Override
    public int setCol(String colore) {
        return 0;
    }

    public Board getBoard() { return this.board; }

    public int getCol() { return this.col; }

}

