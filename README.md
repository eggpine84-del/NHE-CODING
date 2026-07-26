# sso-engine (v2.0)

**Generalized NHE S_s[N]_O: Polymorphic Direct-to-Silicon Logic Simulator**

An implementation of the breakthrough Silicon-Native 3-State Ternary Logic Architecture. It bypasses conventional CPU decoder tree latencies by mapping logical instructions to physical coordinates in exactly 1-Clock cycle.

## License
- **CC BY-NC-ND 4.0** (Attribution-NonCommercial-NoDerivs)
- **Original Authority:** eggpine84@gmail.com / Logic_Architect_eggpine84

## Key Features
1. **Decoding-Free 1-Clock Mapping**: Compute orthogonal coordinates using:
   `Addr = S * (N_s * N_O) + s * N_O + O`
2. **Energy Discharge Model**: Zero Memory Leak. Once discharged, the pipeline resets.
3. **Hardware-Level IRQ Exception**: Gracefully handoff 'Unknown' state to prevent core hardware crashes.

## Quick Start
```python
from sso_engine import NHEv2Core, ReflexKernel

# Initialize a custom NHE substrate (e.g., N_S=10, N_s=15, N_O=20)
core = NHEv2Core(N_S=10, N_s=15, N_O=20)
addr = core.get_physical_address(M_d=1, S=1, s=5, O=9)
print(f"Direct Physical Line: {addr}")