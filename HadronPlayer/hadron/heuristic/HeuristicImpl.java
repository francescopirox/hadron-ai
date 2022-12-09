package hadron.heuristic;

import hadron.board.Board;

public class HeuristicImpl implements Heuristic {
    double[] pesi = {-66 , -100 , -200 , -50};

    public HeuristicImpl( double[] pesi ) {
        this.pesi = pesi;
    }

    public HeuristicImpl() { }

    @Override
    public double evaluate( Board b , int col ) {
        if( b.isFinal() )
            return -10000D;

        int co,cb,cs,css ;
        co=cb=cs=css=0;

        for (int i = 1; i < 8; i++)
            for (int j = 0; j < 9; j++) {
                if( b.getCol(i , j) != -1 ) {
                    co += 1;
                } else {
                    if( cellaBloccata(b , i , j) )
                        cb += 1;
                    if( cellaSafe(b , col ,i , j) )
                        cs += 1;
                    if( cellaStrictSafe(b , i , j) )
                        css += 1;
                }
            }

        int dispari = -1;
        if( css + cs % 2 == 1 && cb > 40 ) {
            dispari = 4;
        }
        System.err.println("Co: "+co+" -  Cb"+cb);
        return pesi[0] * co + pesi[1] * cb + pesi[2] * dispari * css + pesi[3] * cs;
    }

    private static boolean cellaStrictSafe( Board b , int i , int j ) {
        int ret = 0;
        for (int k = i - 1; k < i + 2 ; k += 2) {
            if(k > -1 && k < 9)
                ret += b.getPawn(k , j);
        }
        for (int h = j - 1; h < j + 2 ; h += 2) {
            if(h > -1 && h < 9)
                ret += b.getPawn(i , h);
        }
        return ret == 0;
    }

    private static boolean cellaSafe( Board b , int col , int i , int j ) {
        int ret = 0;
        for (int k = i - 1; k < i + 2 && k > -1 && k < 9; k += 2)
            for (int h = j - 1; h < j + 2 && j > -1 && j < 9; h += 2) {

                if(k > -1 && k < 9 && h > -1 && h < 9 && b.getCol(k , h) != col )
                    return false;
            }
        return true;

    }

    private static boolean cellaBloccata( Board b , int i , int j ) {

        int ret = 0;
        for (int k = i - 1; k < i + 2 ; k += 2) {
            if(k > -1 && k < 9)
                ret += b.getPawn(k , j);
        }
        for (int h = j - 1; h < j + 2; h += 2) {
            if(h > -1 && h < 9)
                ret += b.getPawn(i , h);
        }

        return ret == 0;
    }

}