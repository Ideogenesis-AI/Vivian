<h1 align="center">
  <img src="docs/images/vivian.png" alt="Vivian Tensor Network Algorithms" width="280">
</h1>

<p align="center">
  <a href="https://pypi.org/project/vivian-net/"><img src="https://img.shields.io/pypi/v/vivian-net?color=red" alt="PyPI Version"></a>
  <a href="https://github.com/Ideogenesis-AI/Vivian/blob/stable/LICENSE"><img src="https://img.shields.io/github/license/Ideogenesis-AI/Vivian?color=orange" alt="License"></a>
  <a href="https://ideogenesis-ai.github.io/Vivian"><img src="https://img.shields.io/badge/docs-github.io-c9a400" alt="Documentation"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/pypi/pyversions/vivian-net?color=228b22" alt="Python Version"></a>
  <a href="https://pytorch.org/"><img src="https://img.shields.io/badge/PyTorch-2.5+-blue?logo=pytorch&logoColor=white" alt="PyTorch"></a>
  <a href="https://github.com/Ideogenesis-AI/Nicole"><img src="https://img.shields.io/badge/built%20on-Nicole-blueviolet" alt="Built on Nicole"></a>
  <a href="https://pypi.org/project/vivian-net/"><img src="https://img.shields.io/pypi/status/vivian-net?color=4b0082" alt="Status"></a>
</p>

Vivian is an open-source project for 2D tensor network algorithms, with an emphasis on infinite projected entangled-pair states (iPEPS). It is built on the [Nicole](https://github.com/Ideogenesis-AI/Nicole) symmetry-aware tensor library and its [Yuzuha](https://github.com/Ideogenesis-AI/Yuzuha) Clebsch-Gordan backend, inheriting full support for Abelian and non-Abelian (currently SU(2) only) symmetries.

Vivian is the two-dimensional counterpart of [Alice](https://github.com/Ideogenesis-AI/Alice), which covers 1D and quasi-1D algorithms. The two projects share the same design philosophy: a physicist-friendly API — TOML-driven model definitions, concise Python entry points — over a well-tested, performant backend designed with HPC in mind, so that cutting-edge tensor network calculations stay accessible without giving up mathematical rigor.

> **Status: early development.** This repository currently contains the project skeleton only. The APIs described below are planned rather than implemented, and everything is subject to change before the first release.


## Algorithms

### Planned

- **CTMRG** (Corner Transfer Matrix Renormalization Group): contraction of the infinite 2D network to obtain the fixed-point environment used for all expectation values
- **Simple Update**: imaginary-time evolution of an iPEPS with a local (bond-wise) approximation of the environment, cheap and robust for locating the right variational region
- **Full Update**: imaginary-time evolution with the full CTMRG environment, giving substantially better accuracy at higher cost
- **Variational Optimization**: direct energy minimization of the iPEPS tensors by gradient descent, with gradients obtained through automatic differentiation of the CTMRG contraction
- **Finite-Temperature iPEPS**: thermal density matrix evolution in 2D for thermodynamic observables


## Key Features

### Planned

- **Symmetry-Aware iPEPS/iPEPO**: block-sparse projected entangled-pair states and operators supporting any symmetry group or product group that Nicole supports, leveraging its exact block-sparse engine
- **Flexible Unit Cells and Lattices**: square, honeycomb, triangular, and kagome lattices with arbitrary unit cell sizes, plus custom lattice extensions via user-defined functions
- **AutoPEPO Construction**: TOML-configured Hamiltonian builder with built-in model presets and full support for custom models via user-defined model functions
- **Systematic Logging**: comprehensive iteration-by-iteration diagnostics via Python's `logging` module
- **PyTorch Backend**: all dense block operations run on PyTorch via Nicole, with optional GPU (CUDA/MPS), Ascend NPU acceleration, and on-demand autograd support


## Installation

Vivian is not yet published to PyPI. For now, install from source in editable mode:

```bash
git clone https://github.com/Ideogenesis-AI/Vivian.git
cd Vivian
uv venv --python 3.11
uv pip install -e ".[test,lint,docs]"
```

See the documentation for the full development workflow.


## Contributing

Vivian is structured around a shared core — the iPEPS, iPEPO, and environment infrastructure — on top of which each algorithm is developed and maintained as an independent unit. This means that individual algorithms can be contributed, extended, or maintained by different people, and each contributor's work is attributed accordingly. Because the project is at an early stage, there is ample room to take ownership of an entire algorithm.

**Ways to contribute:**
- Implement or co-develop one of the planned algorithms (see [Algorithms](#algorithms))
- Report issues and request features via [GitHub Issues](https://github.com/Ideogenesis-AI/Vivian/issues)
- Submit pull requests with bug fixes or enhancements
- Share benchmarks, use cases, or constructive feedback

**Development guidelines:**
- Ensure contributions include appropriate tests
- Follow the existing code style (enforced by `ruff`)
- Add type hints for all public function signatures
- Update documentation for user-facing changes

**Authors and Maintainers:**

Vivian is created by [Changkai Zhang](https://chx-zh.cc) as part of the Ideogenesis-AI effort in studying quantum many-body systems. The core infrastructure is maintained by the original author; individual algorithms have their respective maintenance teams. For questions about contributing or collaboration opportunities, feel free to open an issue on GitHub or contact the responsible team directly.


## License

Vivian is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. This means you are free to use, modify, and distribute this software under the terms of the GPL-3.0 license. We encourage you to share any improvements you make back to the community, helping Vivian grow and benefit all users. See the [LICENSE](LICENSE) file for the full license text. For more information about GPL-3.0, visit https://www.gnu.org/licenses/gpl-3.0.html
