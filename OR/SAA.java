package sa;

/**
 * 實現模擬退火演算法
 * @author zzy
 *Email:zhaozhiyong1989@126.com
 */
public class SATest {
    public static final int T = 100;// 初始化溫度
    public static final double Tmin = 1e-8;// 溫度的下界
    public static final int k = 100;// 迭代的次數
    public static final double delta = 0.98;// 溫度的下降率

    public static double getX() {
        return Math.random() * 100;
    }

    /**
     * 求得函式的值
     * 
     * @param x目標函式中的一個引數
     * @param y目標函式中的另一個引數
     * @return函式值
     */
    public static double getFuncResult(double x, double y) {
        double result = 6 * Math.pow(x, 7) + 8 * Math.pow(x, 6) + 7
                * Math.pow(x, 3) + 5 * Math.pow(x, 2) - x * y;

        return result;
    }

    /**
     * 模擬退火演算法的過程
     * @param y目標函式中的一個引數
     * @return最優解
     */
    public static double getSA(double y) {
        double result = Double.MAX_VALUE;// 初始化最終的結果
        double t = T;
        double x[] = new double[k];
        // 初始化初始解
        for (int i = 0; i < k; i++) {
            x[i] = getX();
        }
        // 迭代的過程
        while (t > Tmin) {
            for (int i = 0; i < k; i++) {
                // 計算此時的函式結果
                double funTmp = getFuncResult(x[i], y);
                // 在鄰域內產生新的解
                double x_new = x[i] + (Math.random() * 2 - 1) * t;
                // 判斷新的x不能超出界
                if (x_new >= 0 && x_new <= 100) {
                    double funTmp_new = getFuncResult(x_new, y);
                    if (funTmp_new - funTmp < 0) {
                        // 替換
                        x[i] = x_new;
                    } else {
                        // 以概率替換
                        double p = 1 / (1 + Math
                                .exp(-(funTmp_new - funTmp) / T));
                        if (Math.random() < p) {
                            x[i] = x_new;
                        }
                    }
                }
            }
            t = t * delta;
        }
        for (int i = 0; i < k; i++) {
            result = Math.min(result, getFuncResult(x[i], y));
        }
        return result;
    }

    public static void main(String args[]) {
        // 設定y的值
        int y = 0;
        System.out.println("最優解為：" + getSA(y));
    }

}

