import sympy

def scan_oppermann_halves(limit_n):
    print("="*70)
    print("🎯 [标靶一] 奥珀曼猜想：局部自旋偏度 (Local Spin Skewness) 扫描")
    print("="*70)
    
    print(f"{'n (p)':<12} | {'[左半区] 偏度 (负-正)':<22} | {'[右半区] 偏度 (负-正)':<22} | {'锚点(0)位置'}")
    print("-" * 75)
    
    for n in range(2, limit_n + 1):
        p = 2*n - 1
        if sympy.isprime(p):
            # 左半区: (n-1)^2 < x <= n(n-1)
            left_start = (n-1)**2 + 1
            left_end = n**2 - n
            
            # 右半区: n(n-1) < x < n^2
            right_start = n**2 - n + 1
            right_end = n**2 - 1
            
            L_pos, L_neg, L_zero = 0, 0, 0
            R_pos, R_neg, R_zero = 0, 0, 0
            
            # 扫描左半区
            for x in range(left_start, left_end + 1):
                spin = sympy.jacobi_symbol(x, p)
                if spin == 1: L_pos += 1
                elif spin == -1: L_neg += 1
                else: L_zero += 1
                    
            # 扫描右半区
            for x in range(right_start, right_end + 1):
                spin = sympy.jacobi_symbol(x, p)
                if spin == 1: R_pos += 1
                elif spin == -1: R_neg += 1
                else: R_zero += 1
                
            # 计算偏度 (Skewness = 负自旋 - 正自旋)
            L_skew = L_neg - L_pos
            R_skew = R_neg - R_pos
            
            # 确定自旋为 0 的锚点在哪一半
            zero_loc = "左半区 🟢" if L_zero == 1 else "右半区 🔵"
            
            # 格式化输出 (为了视觉对齐，加上正负号)
            L_skew_str = f"{L_skew:>2} (正:{L_pos:<2} 负:{L_neg:<2})"
            R_skew_str = f"{R_skew:>2} (正:{R_pos:<2} 负:{R_neg:<2})"
            
            print(f"n={n:<2} (p={p:<2})  |  {L_skew_str:<20}  |  {R_skew_str:<20}  |  {zero_loc}")

if __name__ == '__main__':
    # 我们先扫描到 n=30，观察自旋偏度的演化规律
    scan_oppermann_halves(30)
