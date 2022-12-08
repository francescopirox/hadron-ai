package hadron.heuristic;

import hadron.board.Board;

public class HeuristicImpl implements Heuristic {
    double[] pesi = {+10 , -10 , -2000 , -500};

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
        int i,j;

        for ( i = 1; i < 8; i++){
            if( b.getCol(i , 0) != -1 )
                co += 1;
            if( b.getCol(0 , i) != -1 )
                co += 1;
            if( b.getCol(i , 8) != -1 )
                co += 1;
            if( b.getCol(8 , i) != -1 )
                co += 1;
        }

        if( b.getCol(0 , 0) != -1 )
            co += 1;
        if( b.getCol(0 , 8) != -1 )
            co += 1;
        if( b.getCol(8 , 8) != -1 )
            co += 1;
        if( b.getCol(8 , 0) != -1 )
            co += 1;

        for ( i = 1; i < 8; i++)
            for ( j = 1; j < 8; j++) {
                if( b.getCol(i , j) != -1 ) {
                    co += 1;
                } else {
                    if( cellaBloccata(b , i , j) )
                        cb += 1;
                    else
                        if( cellaSafe(b , col,i , j) )
                            cs += 1;
                        else
                            if( cellaStrictSafe(b , i , j) )
                                css += 1;
                    }
            }

        int dispari = 1;
        int consuma = 1;
        if( css + cs % 2 == 1) {
            dispari = 4;
            consuma = 2;
        }
        if( css+cs % 2 == 0 && cb+co > 70 ) {
            if( css % 2 ==0 )
                dispari = -10;
            else
                consuma = -20;
        }

        return pesi[0] * (9 * 9 - co-cb-css-cs) + pesi[1] * (cb+co) + pesi[2] * dispari * css + pesi[3] * cs * consuma;
    }

    private static boolean cellaStrictSafe( Board b , int i , int j ) {
        int ret = 0;
        for (int k = i - 1; k < i + 2 && k > -1 && k < 9; k += 2) {
            ret += b.getPawn(k , j);
        }
        for (int h = j - 1; h < j + 2 && j > -1 && j < 9; h += 2) {
            ret += b.getPawn(i , h);
        }
        return ret == 0;
    }

    private static boolean cellaSafe( Board b , int col , int i , int j ) {
        int ret = 0;
        for (int k = i - 1; k < i + 2 && k > -1 && k < 9; k += 2)
            for (int h = j - 1; h < j + 2 && j > -1 && j < 9; h += 2) {
                if( b.getCol(k , h) != col )
                    return false;
            }
        return true;

    }

    private static boolean cellaBloccata( Board b , int i , int j ) {

        int ret = 0;

        for (int k = i - 1; k < i + 2 && k > -1 && k < 9; k += 2) {
            ret += b.getPawn(k , j);
        }
        for (int h = j - 1; h < j + 2 && j > -1 && j < 9; h += 2) {
            ret += b.getPawn(i , h);
        }

        return ret != 0;
    }

}