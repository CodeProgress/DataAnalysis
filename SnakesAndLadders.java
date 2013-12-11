import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;


public class SnakesAndLadders {
	
	public int boardSize;
	public int startPosition;
	public int dieSize;
	public HashMap<Integer, Integer> magicSq;
	
	public SnakesAndLadders(){
		boardSize = 100;
		startPosition = 0;
		dieSize = 6;
		buildMagigSq();
	}
	
	public SnakesAndLadders(int boardSize, int startPosition, int dieSize){
		this.boardSize = boardSize;
		this.startPosition = startPosition;
		this.dieSize = dieSize;
		this.buildMagigSq();
	}
	
	public void buildMagigSq(){
		magicSq = new HashMap<Integer, Integer>();
		for (int i = 0; i < boardSize + dieSize; i++){
			magicSq.put(i, i);
		}
		//snakes
		magicSq.put(16, 6);
		magicSq.put(47, 26);
		magicSq.put(49, 11);
		magicSq.put(56, 53);
		magicSq.put(62, 19);
		magicSq.put(64, 60);
		magicSq.put(87, 24);
		magicSq.put(93, 73);
		magicSq.put(95, 75);
		magicSq.put(98, 78);
		
		//ladders
		magicSq.put(1, 38);
		magicSq.put(4, 14);
		magicSq.put(9, 31);
		magicSq.put(21, 42);
		magicSq.put(28, 84);
		magicSq.put(36, 44);
		magicSq.put(51, 67);
		magicSq.put(71, 91);
		magicSq.put(80, 100);
	}
	
	
	public int climbOrSlide(int curPos){
		return magicSq.get(curPos);
	}
	
	public ArrayList<Integer> playGame(){
		int curPos = startPosition;
		
		ArrayList<Integer> positions = new ArrayList<Integer>();
		
		while (curPos < boardSize){
			Random rand = new Random();
			int roll = rand.nextInt(5) + 1 ;
			curPos += roll;
			curPos = climbOrSlide(curPos);
			positions.add(curPos);
		}
		
		return positions;
	}
	
	public void printGameStats(int numGames){
		int longest    = Integer.MIN_VALUE;
		int shortest   = Integer.MAX_VALUE;
		double totalMoves = 0.0;
		for (int i = 0; i < numGames; i++){
			int gameLen = playGame().size();
			
			totalMoves += gameLen;
			
			if (gameLen > longest){
				longest = gameLen;
			}
			
			if (gameLen < shortest){
				shortest = gameLen;
			}	
		}
		
		System.out.println("Longest Game: " + "\t" + longest);
		System.out.println("Shortest Game: " + "\t" + shortest);
		System.out.println("Average Game: " + "\t" + totalMoves/numGames);
		
		System.out.println();
	}
		
	
	public static void main(String[] args) {
		SnakesAndLadders sal = new SnakesAndLadders();
		
		int numGames = 100000;
		sal.printGameStats(numGames);
		
	}

}
