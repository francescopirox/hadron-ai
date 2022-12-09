package hadron.heuristic;

import hadron.board.Board;

public class HeuristicImpl implements Heuristic {
    double[] pesi = {66 , -2 , -200 , 200,-50};

    public HeuristicImpl( double[] pesi ) {
        this.pesi = pesi;
    }

    public HeuristicImpl() { }

    @Override
    public double evaluate( Board b , int col ) {
        if( b.isFinal() )
            return -10000D;

        int co,cb,cs,css,csa,cass ;
        co=cb=cs=css=csa=cass=0;
        int i,j;

        for ( i = 0; i < 9; i++)
            for ( j = 0; j < 9; j++) {
                if( b.getCol(i , j) != -1 ) {
                    co += 1;
                }
                else if( cellaBloccata(b , i , j) )
                        cb += 1;
                else if( cellaSafe(b , col,i , j) )
                        cs += 1;
                else if( cellaSafe(b , 1-col,i , j) )
                        csa += 1;
                else if( cellaStrictSafe(b , i , j) )
                        css += 1;
                else if (cellaAngularStrictSafe(b,i,j))
                        cass+=1;
            }
        int dispari = 1;
        int consuma = 1;
        if( css + cass+ cs % 2 == 1) {
            dispari = 4;
            consuma = 2;
        }
        if( css+cs+cass % 2 == 0 && cb+co > 65 ) {
            if( css % 2 ==0 )
                dispari = -10;
            else
                consuma = -20;
        }

        System.out.println("co: "+co+" cb: "+cb+" cs: "+cs+" csa: "+csa+" css: "+css+" cass: "+cass);

        return pesi[0] * (9 * 9 - co-cb-css-cs-csa-cass) + pesi[1] * (cb+co) + pesi[2] * dispari * (css + cass)+pesi[3]*csa +pesi[4] * cs * consuma;

    }

    private boolean cellaAngularStrictSafe( Board b , int i , int j ) {
        if(i!=0 || i!=8 || j!=0 || j!=8)
            return false;

        // CASO VERTICE LARGO
        if(i==0 && j==0 && b.getCol(0,1)==-1 && b.getCol(1,0)==-1 && b.getCol(2,0)!=-1 && b.getCol(1,1)!=-1 && b.getCol(0,2)!=-1)
            return true;
        if(i==8 && j==8 && b.getCol(8,7)==-1 && b.getCol(7,8)==-1 && b.getCol(6,8)!=-1 && b.getCol(7,7)!=-1 && b.getCol(8,6)!=-1)
            return true;
        if(i==8 && j==0 && b.getCol(8,1)==-1 && b.getCol(7,0)==-1 && b.getCol(6,0)!=-1 && b.getCol(7,1)!=-1 && b.getCol(8,2)!=-1)
            return true;
        if(i==0 && j==8 && b.getCol(1,8)==-1 && b.getCol(0,7)==-1 && b.getCol(0,6)!=-1 && b.getCol(1,7)!=-1 && b.getCol(2,8)!=-1)
            return true;
        return false;


    }

    private static boolean cellaStrictSafe( Board b , int i , int j ) {
        int ret = 0;
        int val=0;
        for (int k = i - 1; k < i + 2 ; k += 2) {
            if(k > -1 && k < 9)
                val=b.getPawn(k , j);
                if(val==0)
                    return false;
                ret+=val;




        }
        for (int h = j - 1; h < j + 2 ; h += 2) {
            if(h > -1 && h < 9)
                val= b.getPawn(i , h);
                if(val==0)
                    return false;
                ret+=val;

        }
        return ret == 0 ;
    }

    private static boolean cellaSafe( Board b , int col , int i , int j ) {
        for (int k = i - 1; k < i + 2 ; k += 2)
            for (int h = j - 1; h < j + 2 ; h += 2) {

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

        return ret != 0;
    }

}