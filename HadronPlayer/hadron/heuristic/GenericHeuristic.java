package hadron.heuristic;

import hadron.board.Board;

import java.util.Random;

public class GenericHeuristic implements Heuristic {
	private static final long serialVersionUID = 5783084660998719046L;
	private boolean isRandom=false;
	Random r= new Random();
	/**
	 * Costruttore euristica
	 * @param i
	 */
	public GenericHeuristic( int i ) {
		isRandom=true;
	}

	public GenericHeuristic() {

	}


	@Override
	public double evaluate(Board b, int col) {
		// Se la hadron.board da una vittoria vuol dire che il giocatore attuale è rimasto senza mosse
		// col è il vincitore
		if(b.isFinal())
			return -1000000D;
		if(isRandom) {
			return r.nextDouble()*10000-5000;
		}
		return  0;
	}

	
	@Override
	public int hashCode() {
		return this.toString().hashCode();
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) return true;
		if (obj == null) return false;
		if (!(obj instanceof GenericHeuristic) ) return false;
		GenericHeuristic other = (GenericHeuristic) obj;
		return other.toString().equals(this.toString());
	}

}
