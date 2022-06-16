// https://www.acmicpc.net/problem/9935
// 문자열, 스택
import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    String str = sc.nextLine();
	    String bomb = sc.nextLine();
	    int bLen = bomb.length();
	    char[] stack = new char[str.length()];
	    int sp = 0;
	    
	    for (int si=0; si < str.length(); ++si) {
            stack[sp++] = str.charAt(si);
            int j = sp - 1, k = bLen - 1;
	        if (stack[j] == bomb.charAt(k)) { // 폭탄의 끝 문자 발견
	            if (sp-bLen >= 0) { // stack에 bomb 길이 이상의 요소가 있으면
    	            for (; k>=0; --j, --k) { // 폭탄인지 확인
    	                if (stack[j] != bomb.charAt(k)) {
    	                    break;
    	                }
    	            }
    	            if (!(k>=0)) { // 폭탄 발견
    	                sp -= bLen; // 폭파
    	            }
	            }
	        }
	    }
	    
        if (sp == 0) {
            System.out.print("FRULA");
        } else {
            System.out.print(String.valueOf(stack, 0, sp));
        }
	}
}