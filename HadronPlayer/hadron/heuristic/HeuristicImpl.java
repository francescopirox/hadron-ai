package hadron.heuristic;

import hadron.board.Board;

public class HeuristicImpl implements Heuristic {
    double[] pesi = {10 , -10 , -1000 , 500,-500};

    public HeuristicImpl( double[] pesi ) {
        this.pesi = pesi;
    }

    public HeuristicImpl() { }

    @Override
    public double evaluate( Board b , int col ) {

        int co,cb,cs,css,csa;
        co=cb=cs=css=csa=0;
        int i,j;


        for ( i = 0; i < 9; i++)
            for ( j = 0; j < 9; j++) {
                if (b.getCol(i, j) != -1) {
                    co += 1;
                } else if (cellaBloccata(b, i, j))
                    cb += 1;

                else if (cellaStrictSafe(b, i, j))
                    css += 1;
                else if (cellaSafe(b, 1 - col, i, j))
                    cs += 1;
                else if (cellaSafe(b, col, i, j))
                    csa += 1;
                else if ((i==0  || i==8) ^ (j==0 || j==8) && cellaBorderSafe(b, i, j, 1 - col))
                    cs += 1;
                else if ((i==0  || i==8) ^ (j==0 || j==8) && cellaBorderSafe(b, i, j, col))
                    csa += 1;
                else if ((i==0 || i==8) &&( j==0 || j==8) && cellaAngularStrictSafe(b, i, j))
                    css += 1;
            }
        int fattoreSS = 1;
        int fattoreS  = 1;
        int fattoreSA = 1;
        int fattoreCB = 1;

        if(co<5)
            fattoreCB=2;

        if( css + cs % 2 == 0 && csa==0 && (81 - co-cb-css-cs-csa)==0 ) {
            fattoreSS = 8;
            fattoreS = 6;
            if( (csa+css+cs)==0 && cb+co==81 )
                return -10000D;
        }
        if( css+cs % 2 == 1 && cb+co+csa+css+cs > 75 ) {
            if( cs % 2 == 1 )
                fattoreS = -2;
            else
               fattoreSS = -1;
        }

        return pesi[0] * (81 - co-cb-css-cs-csa) + pesi[1] * fattoreCB *(cb+co) + pesi[2] * fattoreSS * css+ pesi[3]*csa*fattoreSA +pesi[4] * cs * fattoreS;

    }

    private boolean cellaBorderSafe( Board b , int i , int j, int col ) {

        if(i == 0 && j!=0 && b.getCol(i+1 , j-1)!= col)
            return false;
        if(i==8 && j!=0 && b.getCol(i-1 , j-1)!= col)
            return false;
        if(i==0 && j !=8  && b.getCol(i+1 , j+1)!= col)
            return false;
        if(i==8 && j !=8  && b.getCol(i-1 , j+1)!= col)
            return false;
        if(i != 0 && j==0 && b.getCol(i-1 , j+1)!= col)
            return false;
        if(i!=8 && j==0 && b.getCol(i+1 , j+1)!= col)
            return false;
        if(i!=0 && j ==8  && b.getCol(i-1 , j-1)!= col)
            return false;
        if(i!=8 && j ==8  && b.getCol(i-1 , j-1)!= col)
            return false;
        return true;
    }

    private boolean cellaAngularStrictSafe( Board b , int i , int j ) {
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
        if(i !=0) {
            val = b.getPawn(i - 1 , j);
            if( val == 0 )
                return false;
        ret+=val;
        }
        if(i !=8){
            val = b.getPawn(i+1 , j);
            if( val == 0 )
                return false;
            ret+=val;
         }
        if(j !=0){
            val = b.getPawn(i , j-1);
            if( val == 0 )
                return false;
            ret+=val;
        }
        if(j !=8){
            val = b.getPawn(i, j+1);
            if( val == 0 )
                return false;
            ret+=val;
        }
        return ret == 0 ;
    }

    private static boolean cellaSafe( Board b , int col , int i , int j ) {
        if(i !=0 && j!=0 && b.getCol(i-1 , j-1)!= col)
             return false;
        else if(i !=8 && j!=0 && b.getCol(i+1 , j-1)!= col)
            return false;
        else if(i!=0 && j !=8  && b.getCol(i-1 , j+1)!= col)
           return false;
        else if(i!=8 && j !=8  && b.getCol(i+1 , j+1)!= col)
            return false;
        return true;
    }

    private static boolean cellaBloccata( Board b , int i , int j ) {

        int ret = 0;
       if(i !=0)
            ret += b.getPawn(i-1 , j);
        if(i !=8)
            ret += b.getPawn(i+1 , j);
        if(j !=0)
            ret += b.getPawn(i , j-1);
        if(j !=8)
            ret += b.getPawn(i, j+1);

        return ret != 0;
    }

}