#!/usr/bin/env python3
"""
oppermann_spin_scanner.py
=========================
Scan Legendre intervals for local quadratic residue skewness
in the left and right halves, verifying the Oppermann Parity Law.

For each n with p = 2n-1 prime, computes:
  Left half  L_n = {(n-1)^2+1, ..., n(n-1)}
  Right half R_n = {n(n-1)+1, ..., n^2-1}
  Skewness   = #(NR) - #(QR) in each half

Titan Project -- Paper X, February 2026
Author: Ruqing Chen, GUT Geoservice Inc.
"""

import sympy


def scan_oppermann_halves(limit_n):
    print("=" * 70)
    print("Oppermann Parity Law: Local Spin Skewness Scanner")
    print("=" * 70)

    print(f"{'n (p)':<12} | {'[Left] Skew (NR-QR)':<22} | "
          f"{'[Right] Skew (NR-QR)':<22} | {'Anchor(0)'}")
    print("-" * 75)

    for n in range(2, limit_n + 1):
        p = 2 * n - 1
        if sympy.isprime(p):
            # Left half: (n-1)^2 < x <= n(n-1)
            left_start = (n - 1) ** 2 + 1
            left_end = n ** 2 - n

            # Right half: n(n-1) < x < n^2
            right_start = n ** 2 - n + 1
            right_end = n ** 2 - 1

            L_pos, L_neg, L_zero = 0, 0, 0
            R_pos, R_neg, R_zero = 0, 0, 0

            # Scan left half
            for x in range(left_start, left_end + 1):
                spin = sympy.jacobi_symbol(x, p)
                if spin == 1: L_pos += 1
                elif spin == -1: L_neg += 1
                else: L_zero += 1

            # Scan right half
            for x in range(right_start, right_end + 1):
                spin = sympy.jacobi_symbol(x, p)
                if spin == 1: R_pos += 1
                elif spin == -1: R_neg += 1
                else: R_zero += 1

            # Skewness = #NR - #QR
            L_skew = L_neg - L_pos
            R_skew = R_neg - R_pos

            # Determine which half contains the anchor (multiple of p)
            zero_loc = "Left" if L_zero == 1 else "Right"

            L_str = f"{L_skew:>2} (QR:{L_pos:<2} NR:{L_neg:<2})"
            R_str = f"{R_skew:>2} (QR:{R_pos:<2} NR:{R_neg:<2})"

            print(f"n={n:<2} (p={p:<3}) |  {L_str:<20}  |  "
                  f"{R_str:<20}  |  {zero_loc}")


if __name__ == '__main__':
    scan_oppermann_halves(30)
