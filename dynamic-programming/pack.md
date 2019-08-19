用一个二维数组 m\[\]\[\]来记录在某个背包容量下，某个物品数下所对应的最大包内价值，我们可以想象这样一种递推关系：当背包容量为$j$，物品数为1时，此时所能装下的最大价值的物品就是装此物品的包内总价值和不装（放不下）此物品的包内总价值的最大值（似乎显而易见，而此算法的核心思想就在于此）, 此最大值即为m\[1\]\[$j$\] ；将物品数增加1，变为2个物品,第二个物品的重量为 w [2],价值为v [2]，而此时所能装下的最大价值的物品就是装此物品的包内总价值和不装此物品的包内总价值的最大值(不用对比两句话了，核心思想是不变的)，对应的递推公式就是**m[ 2 ][ j ] = max( m[ 1 ] [ j - w[ 2 ] ] + v [ 2 ] ,m[ 1 ][ j ] )**。max函数中的左项为当物品数为1，背包容量为 j 减去第二个物品重量时所能装下的最大价值，然后再加上第二个物品的价值，即先默认肯定装第二个物品。相似的max函数中的右项为当不装第二件商品，背包容量为j，物品数为1时所能装下的最大价值。

```java
import java.util.Scanner;

public class Package01
{
    int n; // 表示物品的数量
    int m; // 表示背包的最大重量
    int[] w; // 表示每一个物品的重量
    int[] v; // 表示每一个物品的价值
    int[][] f; // 用来表示状态转移方程

    public void sovle()
    {
        // 初始化各初始条件
        init();
        // 首先构造第一行上
        int i = 0, j = 0;
        for (j = 1; j <= m; j++)
        {
            if (j < w[i])
            {
                f[i][j] = 0;
            }
            else
            {
                f[i][j] = v[i];
            }
        }
        // 然后对剩下的n-1个物品填充
        for (i = 1; i < n; i++)
        {
            for (j = 1; j <= m; j++)
            {
                if (j < w[i])
                {
                    f[i][j] = f[i - 1][j];
                }
                else
                {
                    f[i][j] = Math.max(f[i - 1][j - w[i]] + v[i], f[i - 1][j]);
                }
            }
        }
        // 输出打印地推二维表
        for (i = 0; i < n; i++)
        {
            for (j = 1; j <= m; j++)
            {
                System.out.print(f[i][j] + "\t");
            }
            System.out.println();
        }
    }

    public void init()
    {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();// 初始化物品的数量
        m = sc.nextInt();// 初始化背包的最大重量
        w = new int[n];
        v = new int[n];
        f = new int[n][m + 1]; // 初始化状态转移方程
        // 初始化每个物品重量
        for (int i = 0; i < n; i++)
        {
            w[i] = sc.nextInt();
        }
        // 初始化每个物品的价值
        for (int i = 0; i < n; i++)
        {
            v[i] = sc.nextInt();
        }
        sc.close();
    }
    public static void main(String[] args)
    {
        new Package01().sovle();
    }
}
```

