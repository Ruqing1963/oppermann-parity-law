# Oppermann's Parity Law

**Titan Project — Paper X**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview

When $p = 2n-1$ is prime and $n$ is even ($p \equiv 3 \pmod{4}$), the right half of the Legendre interval $[(n-1)^2, n^2]$ has **exactly zero** quadratic residue skewness modulo $p$. The global asymmetry $N^- - N^+ = 1$ (proved in [Paper IX](https://zenodo.org/records/18706876)) is carried entirely by the left half.

**Proof mechanism:** The negation involution $x \mapsto p - x$ swaps QR $\leftrightarrow$ NR when $(-1/p) = -1$, and the right half's residue set is closed under this involution, forcing perfect pairing.

Verified computationally for all 87 qualifying even $n \leq 500$.

## Repository Structure

```
├── paper/
│   ├── Oppermann_Parity.tex       # LaTeX source
│   └── Oppermann_Parity.pdf       # Compiled PDF (6 pages)
├── scripts/
│   └── oppermann_spin_scanner.py  # Half-interval skewness scanner
├── LICENSE
└── README.md
```

## Quick Start

```bash
pip install sympy
python scripts/oppermann_spin_scanner.py
```

## Companion Papers (Titan Project)

| # | Title | Link |
|---|-------|------|
| I | Conductor Incompressibility for Frey Curves | [Zenodo:18682375](https://zenodo.org/records/18682375) |
| III | Weil Restriction Rigidity via Genus 2 Jacobians | [Zenodo:18683194](https://zenodo.org/records/18683194) |
| IV | Landau's Fourth Problem: Conductor Rigidity and Sato–Tate | [Zenodo:18683712](https://zenodo.org/records/18683712) |
| V | The 2-2 Coincidence: Primes in Arithmetic Progressions | [Zenodo:18684151](https://zenodo.org/records/18684151) |
| VI | Genesis of Prime Constellations: GSp(8) | [Zenodo:18684352](https://zenodo.org/records/18684352) |
| VII | Conductor Rigidity and the Static Conduit in GSp(4) | [Zenodo:18684892](https://zenodo.org/records/18684892) |
| VIII | Legendre's Conjecture in Function Fields | [Zenodo:18705744](https://zenodo.org/records/18705744) |
| IX | Quadratic Residue Asymmetry in Legendre Intervals | [Zenodo:18706876](https://zenodo.org/records/18706876) |
| **X** | **Oppermann's Parity Law (this repo)** | Zenodo (forthcoming) |

## Citation

```bibtex
@article{chen2026oppermann,
  author  = {Ruqing Chen},
  title   = {Oppermann's Parity Law: Quadratic Residue Symmetry Breaking in Half-Intervals via the Negation Involution},
  year    = {2026},
  note    = {Titan Project Paper X}
}
```

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
