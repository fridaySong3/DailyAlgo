// https://www.acmicpc.net/problem/2293
// DP
import java.util.Scanner;

public class Main
{   
    public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int n = sc.nextInt();
	    int k = sc.nextInt();
        int[] DP = new int[k+1]; // DP[c]: 지금까지의 코인을 사용해서 가치 c를 만드는 경우의 수.
        DP[0] = 1; // 가치 0을 만드는 방법은 아무 동전도 사용하지 않으면 됨. 즉 경우의 수 1.
        
        // DP
        for (int r = 1; r<=n; ++r) {
            int new_coin = sc.nextInt();
            for (int c=new_coin; c<=k; ++c) {
                // 이전 코인들과 new_coin을 사용해서 가치 c를 만드는 경우의 수 
                //  = 이전 코인들을 사용해서 가치 c를 만드는 경우의 수 (new_coin 0번 사용) 
                //   + 이전 코인과 new_coin을 사용해서 가치 c-new_coin을 만드는 경우의 수 (new_coin 1~최대(c/new_coin)번 사용)
                DP[c] = DP[c] + DP[c-new_coin]; 
            }
        }
        
        System.out.println( DP[k] );
	}
}