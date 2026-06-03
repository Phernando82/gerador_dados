# Brazilian Test Data Generator

Synthetic data pipeline · Python · pandas · geopy · shapely · NumPy

---

## Overview

Modular CLI application that generates realistic, structurally valid synthetic Brazilian personal records — name, email, CPF, city, state, phone, and ZIP code — on demand. Each data type is produced by a dedicated module with domain-specific generation logic: mathematical CPF validation, geospatial coordinate validation against a Brazil polygon, reverse geocoding via Nominatim, and state-aware DDD phone generation. Output can be saved to a timestamped `.txt` file. Demonstrates a multi-module data pipeline with geospatial processing, algorithmic validation, and structured file output — patterns applicable to IoT device registry seeding, test environment provisioning, and synthetic dataset generation for industrial system integration testing.

---

## Technical Highlights

**Algorithmic CPF generation and validation**
CPF numbers are generated using the official Brazilian Tax Authority check-digit algorithm: two verification digits are computed from weighted sums modulo 11, with palindrome rejection to exclude structurally invalid sequences. The same modular arithmetic validation pattern is used in industrial protocols for frame integrity checks (CRC, LRC in Modbus) and serial number validation in asset management systems.

**Geospatial coordinate validation via Shapely polygon**
Random latitude/longitude pairs are generated within Brazil's bounding box, then validated against a `shapely.Polygon` approximation of the Brazilian border. Only coordinates that fall within the polygon proceed to geocoding — rejecting ocean and neighboring-country hits before consuming API quota. Equivalent to geofencing logic in industrial IoT: filtering telemetry from GPS-equipped assets to include only readings within a defined operational zone.

**Reverse geocoding via geopy Nominatim**
Validated coordinates are resolved to city, state, and ZIP code through Nominatim's reverse geocoding API, returning real administrative data for geographically plausible addresses. The same reverse geocoding pipeline is used in industrial fleet management and field service systems to resolve GPS coordinates from mobile assets into human-readable location identifiers.

**State-aware DDD phone generation**
Phone numbers are generated following the Brazilian ANATEL numbering standard, with the area code (DDD) selected according to the state resolved from geocoding — ensuring internal consistency between location and contact data. Mirrors state-machine-driven data generation in industrial test fixtures that enforce logical consistency between interdependent parameters.

**Modular architecture with shared data objects**
Each domain (name, CPF, address, phone) is implemented as an independent module exposing a single generation function that returns a typed object. The `generator.py` orchestrator composes modules on demand based on user selection, with no tight coupling between domains. Equivalent to a plug-in sensor driver architecture where each device type is an independent module registered with a central data collection coordinator.

**Timestamped structured file output**
Records are written to a fixed-width formatted `.txt` file with generation timestamp per record (`%Y-%m-%d %H:%M`), providing a human-readable audit log. Mirrors the structured log format used in industrial data historians and SCADA event logs where each record carries a precise acquisition timestamp.

**NumPy-based coordinate batch generation**
`gera_lat_lon.py` uses `np.random.uniform` with configurable bounds to produce coordinate arrays as NumPy tuples, enabling batch generation independent of the main pipeline. Demonstrates NumPy as a numerical utility layer — directly applicable to synthetic sensor data generation for testing IoT ingestion pipelines.

---

## Stack

Python 3.x · pandas · geopy (Nominatim) · shapely · NumPy · random · datetime · csv

---

## Installation

```bash
git clone https://github.com/YOUR_USER/brazilian-test-data-generator
cd brazilian-test-data-generator
pip install -r requirements.txt
```

Place `nomes.csv` (name dataset) in the project root, then:

```bash
python generator.py
```

---

## Module Overview

| Module | Responsibility |
|---|---|
| `cpf.py` | CPF generation + validation (check-digit algorithm) |
| `endereco.py` | Coordinate generation → polygon validation → reverse geocoding |
| `nome.py` | Random name from CSV + unique email generation |
| `telefone.py` | Phone generation with state-matched DDD |
| `gera_lat_lon.py` | NumPy-based coordinate array generation |
| `cabecalho.py` | CLI menu rendering |
| `generator.py` | Orchestrator — composes modules per user selection |

---

## Generation Pipeline

```
User selects options (1–7)
        │
        ▼
gera_nome_email()          gera_endereco()
  │                          │
  ├── sample nomes.csv        ├── random lat/lon (uniform)
  ├── build unique email      ├── shapely polygon check (Brazil border)
  └── return nome_email obj   ├── Nominatim reverse geocode
                              └── return endereco_completo obj
        │                          │
        └──────────┬───────────────┘
                   ▼
          assemble dados dict
                   │
                   ▼
          print to console
                   │
                   ▼
          save to dados_gerados.txt?
          ├── yes → fixed-width format + timestamp per record
          └── no  → discard
```

---

## Relevance to Industry 4.0

The synthetic data generation pipeline demonstrates patterns directly applicable to industrial system development and testing:

- **Algorithmic check-digit validation** → CRC/LRC integrity checks in Modbus frames, serial number validation in asset registries, barcode check-digit verification in warehouse management systems
- **Geospatial polygon filtering** → geofencing in industrial IoT: filtering GPS telemetry from mobile assets (forklifts, field technicians, delivery vehicles) to include only readings within defined operational zones
- **Reverse geocoding pipeline** → location resolution in field service management and industrial fleet systems that convert GPS coordinates from equipment into site identifiers for work order assignment
- **Modular driver architecture** → plug-in sensor driver pattern where each device type is an independent, swappable module registered with a central data collection coordinator
- **Synthetic test data generation** → seeding test environments for industrial MES, ERP, and SCADA systems during development and integration testing, where using real production data is prohibited by compliance requirements
- **Timestamped structured output** → audit log format for industrial event records: each entry carries a precise timestamp, enabling traceability and replay of data generation sessions

---

## License

MIT · No real personal data is used or stored. All generated records are synthetic and structurally valid only.
