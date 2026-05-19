# file: ch_22_01_collision_simulation.py
"""Mini simulation of collision handling in hash tables.

The program compares three probing strategies in open addressing:
1) Linear probing
2) Quadratic probing
3) CPython-inspired perturbation probing

The simulation starts from original keys and computes hash(key) in code.
It therefore shows explicitly how key types and __hash__ affect
the probe sequence.

The script runs multiple scenarios:
- int keys (built-in int.__hash__)
- DemoKey keys (custom __hash__)

For each strategy and scenario it prints:
- key -> hash(key)
- probe path for each insertion
- number of probes, total probes, and average

The goal is pedagogical: make collisions, probing, and differences between
concrete strategies visible, and compare how different key types (with the same start index)
affect the probe sequence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterator, Sequence

# dataclass is a shorthand for classes that primarily hold data.
# It automatically generates __init__, __repr__, and other methods from fields.
# This keeps the code readable and avoids boilerplate when extra logic is minimal.
@dataclass
class InsertTrace:
    key_name: str
    hash_value: int
    probe_path: list[int]
    probes_used: int


@dataclass(frozen=True)
class DemoKey:
    """Key type used to demonstrate controlled __hash__."""

    _name: str
    _forced_hash: int

    def __hash__(self) -> int:
        return self._forced_hash

    def __repr__(self) -> str:
        return self._name


@dataclass
class SimulationResult:
    strategy_name: str
    traces: list[InsertTrace]
    failed_insertions: list[str]

    @property
    def total_probes(self) -> int:
        return sum(t.probes_used for t in self.traces)

    @property
    def average_probes(self) -> float:
        return self.total_probes / len(self.traces)


def linear_indices(hash_value: int, table_size: int):
    start = hash_value % table_size
    step = 0
    while True:
        yield (start + step) % table_size
        step += 1


def quadratic_indices(hash_value: int, table_size: int):
    start = hash_value % table_size
    step = 0
    while True:
        # Uses k + k^2 to reduce clustering compared to pure linear probing.
        yield (start + step + step * step) % table_size
        step += 1


def perturb_indices(hash_value: int, table_size: int, perturb_shift: int = 5):
    if table_size & (table_size - 1) != 0:
        raise ValueError("table_size must be a power of two for this demo")

    mask = table_size - 1
    j = hash_value
    perturb = hash_value

    while True:
        yield j & mask
        j = (5 * j) + 1 + perturb
        perturb >>= perturb_shift


def insert_with_generator(
    slot_list: list[int | None], key: Hashable, hash_value: int, index_generator: Iterator[int]
) -> InsertTrace:
    max_probes = len(slot_list)
    probe_path: list[int] = []
    for probe_count, idx in enumerate(index_generator, start=1):
        probe_path.append(idx)
        if slot_list[idx] is None:
            slot_list[idx] = hash_value
            return InsertTrace(
                key_name=repr(key),
                hash_value=hash_value,
                probe_path=probe_path,
                probes_used=probe_count,
            )
        if probe_count >= max_probes:
            break

    raise RuntimeError(
        f"Could not place h={hash_value} after {max_probes} probes. "
        f"Probe path: {probe_path}"
    )


def run_simulation(
    strategy_name: str, keys: Sequence[Hashable], table_size: int
) -> SimulationResult:
    slots: list[int | None] = [None] * table_size
    traces: list[InsertTrace] = []
    failed_insertions: list[str] = []

    for key in keys:
        h = hash(key)
        if strategy_name == "linear":
            gen = linear_indices(h, table_size)
        elif strategy_name == "quadratic":
            gen = quadratic_indices(h, table_size)
        elif strategy_name == "perturb":
            gen = perturb_indices(h, table_size)
        else:
            raise ValueError(f"Unknown strategy: {strategy_name}")

        try:
            traces.append(insert_with_generator(slots, key, h, gen))
        except RuntimeError as exc:
            failed_insertions.append(str(exc))

    return SimulationResult(
        strategy_name=strategy_name,
        traces=traces,
        failed_insertions=failed_insertions,
    )


def print_result(result: SimulationResult):
    print(f"\n=== {result.strategy_name.upper()} ===")
    print("key             hash  probes  probe-path")
    print("-" * 72)
    for t in result.traces:
        path = " -> ".join(str(i) for i in t.probe_path)
        print(f"{t.key_name:<15} {t.hash_value:<5} {t.probes_used:<7} {path}")
    print("-" * 72)
    print(f"Total probes:    {result.total_probes}")
    if result.traces:
        print(f"Average probes:  {result.average_probes:.2f}")
    else:
        print("Average probes:  n/a")

    if result.failed_insertions:
        print("Failed/aborted insertions:")
        for failure in result.failed_insertions:
            print(f"  - {failure}")


def find_string_keys_with_same_start_index(
    count: int, table_size: int, target_index: int, prefix: str = "s"
) -> list[str]:
    """Find str keys where hash(key) % table_size yields the same start index."""
    keys: list[str] = []
    candidate = 0
    max_candidates = 200_000

    while len(keys) < count and candidate < max_candidates:
        key = f"{prefix}_{candidate}"
        if hash(key) % table_size == target_index:
            keys.append(key)
        candidate += 1

    if len(keys) < count:
        raise RuntimeError(
            f"Found only {len(keys)} str keys for index {target_index}. "
            f"Tried {max_candidates} candidates."
        )

    return keys


def main():
    # Scenario A: built-in int.__hash__ (for int, hash is typically the value itself).
    # All keys below share the same low 4 bits (= 3), so they collide on start index
    # when table_size=16. The higher bits are different.
    int_keys = [0x13, 0x53, 0x93, 0xD3, 0x113, 0x153]

    # Scenario B: custom type with controlled __hash__.
    # Shows explicitly that hash comes from the type instance's __hash__.
    demo_keys = [
        DemoKey("K1", 0x13),
        DemoKey("K2", 0x53),
        DemoKey("K3", 0x93),
        DemoKey("K4", 0xD3),
        DemoKey("K5", 0x113),
        DemoKey("K6", 0x153),
    ]

    # Scenario C: real str keys with str.__hash__.
    # Keys are found dynamically so they collide on the same start index.
    str_keys = find_string_keys_with_same_start_index(
        count=6,
        table_size=16,
        target_index=3,
        prefix="key",
    )

    table_size = 16

    print("Mini simulation: collisions in a hash table")
    print(f"Table size: {table_size}")
    print("(intentionally chosen to produce the same start index)")

    scenarios: list[tuple[str, Sequence[Hashable]]] = [
        ("A: int keys (int.__hash__)", int_keys),
        ("B: DemoKey keys (custom __hash__)", demo_keys),
        ("C: str keys (str.__hash__)", str_keys),
    ]

    for scenario_name, keys in scenarios:
        print(f"\n### Scenario {scenario_name}")
        print("Original key -> hash(key):")
        for key in keys:
            print(f"  {repr(key):<15} -> {hash(key)}")

        if "str keys" in scenario_name:
            print("Note: hash values for str can vary between different runs.")

        for strategy in ("linear", "quadratic", "perturb"):
            result = run_simulation(strategy, keys, table_size)
            print_result(result)

    print("\nShort interpretation:")
    print("- Linear probing tends toward primary clustering (long neighbor chains).")
    print("- Quadratic often spreads probes better than linear.")
    print("- Perturbation mixes in more hash bits over time and")
    print("  often separates colliding keys more quickly.")


if __name__ == "__main__":
    main()
