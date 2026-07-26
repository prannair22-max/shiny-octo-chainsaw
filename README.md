

🚀 Quick Start
1. Prerequisites
Ensure you have GDAL dependencies installed on your system. Using Conda or a virtual environment is recommended.

2. Installation
Clone the repository and set up a virtual environment:

Bash
git clone [https://github.com/your-username/burnaby-parks-gis.git](https://github.com/your-username/burnaby-parks-gis.git)
cd burnaby-parks-gis

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
Note for GDAL/Fiona users on Windows/Mac: If you encounter issues installing geopandas via pip, install using conda:

Bash
conda env create -f environment.yml
conda activate burnaby-gis
3. Usage
Run Full Analysis Pipeline
Execute the automated script to fetch data, compute metrics, and generate maps:

Bash
python scripts/run_analysis.py --neighborhood Metrotown --buffer 800 --output-map output_metrotown.html
Python API Example
Python
from src.data_loader import load_burnaby_parks
from src.geo_processing import calculate_park_access_buffer
from src.visualization import create_interactive_park_map

# Load Burnaby Parks GeoDataFrame
gdf_parks = load_burnaby_parks(epsg=26910)

# Calculate 10-minute (800m) walkability buffers
gdf_buffers = calculate_park_access_buffer(gdf_parks, distance_meters=800)

# Build interactive Folium map
park_map = create_interactive_park_map(gdf_parks, gdf_buffers)
park_map.save("data/outputs/burnaby_parks_walkability.html")
print("Map successfully generated!")
📊 Example Outputs
Interactive Web Maps: Standalone HTML files containing layer toggles for:

Dog Off-Leash Areas

Playgrounds & Spray Pads

Trail Difficulty Levels

15-Minute Walk Isochrones

Neighborhood Summary Tables:

Neighborhood	Total Parks	Total Area (ha)	Park Area per Capita (m²)	Walkability Index
Metrotown	14	48.2	8.6	High
Brentwood	11	32.5	7.2	Moderate
Deer Lake	4	204.1	54.3	High
SFU / UniverCity	6	320.0	68.1	High
📜 License
Distributed under the MIT License. See LICENSE for more information.

🤝 Contributing & Acknowledgments
Data provided by the City of Burnaby Open Data Portal and Metro Vancouver Open Data.

Built with standard open-source geospatial Python tools (geopandas, folium, shapely).

Contributions, issue reports, and pull requests are welcome!
"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content)

print("File generated successfully: README.md")


```text?code_stdout&code_event_index=1
File generated successfully: README.md

Your README.md file has been generated.
MD icon
README
 MD 
Open

Overview of What's Included:
Project Structure & Tech Stack: Clearly details key Python GIS libraries (geopandas, folium, shapely, pyproj, osmnx) and standard directory organization.

Open Data Sources: References City of Burnaby Open Data, Metro Vancouver Open Data, and OpenStreetMap integration.

Features & Capabilities: Highlights spatial reprojection (EPSG:26910 / NAD83 UTM Zone 10N), walkability/buffer analysis (400m/800m network buffers), amenity spatial joins, and interactive HTML map generation.

Setup & Usage: Step-by-step instructions for environment creation (venv/conda), dependency installation, command-line usage, and a Python code example.




Gemini is AI and can make mistakes.

# Burnaby Parks GIS & Spatial Analytics Tool 🌲🗺️

A Python-based geospatial analysis and visualization tool that leverages **City of Burnaby Open Data**, **Metro Vancouver Open Data**, and **OpenStreetMap (OSM)** to analyze park access, amenities, green canopy coverage, and trail networks across Burnaby, British Columbia, Canada.

---

## 📌 Features

- **Open Data Pipeline**: Automated fetching and ingestion of vector datasets (GeoJSON, Shapefile, KML) from the City of Burnaby Open Data Portal.
- **Spatial Projections & Calculations**: Precise metric area and boundary calculations reprojected to **NAD83 / UTM Zone 10N (EPSG:26910)**.
- **Accessibility & Walkability Analysis**: Computes 5-minute (400m) and 10-minute (800m) network walkability buffers around park access points.
- **Amenity & Trail Mapping**: Spatial joins and indexing (`rtree`, `shapely`) to map playgrounds, sports fields, washrooms, picnic areas, and trail networks within park boundaries.
- **Interactive Map Generation**: Generates standalone, mobile-responsive interactive Leaflet maps (`folium`) with custom layer controls, cluster markers, and choropleth visualizations.
- **Summary & Statistical Reporting**: Generates automated neighborhood-level park metric reports in CSV, GeoJSON, and PDF/HTML formats.

---

## 🛠️ Tech Stack & GIS Libraries

| Category | Technology / Library | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core processing engine |
| **Core GIS** | `geopandas`, `shapely` | Vector data manipulation, spatial joins, geometries |
| **Projections** | `pyproj` | Coordinate reference system (CRS) transformations |
| **I/O & Formats** | `fiona`, `pyogrio` | Reading/writing spatial data formats (GeoPackage, GeoJSON, SHP) |
| **Spatial Network** | `osmnx`, `networkx` | OpenStreetMap street and pedestrian network analysis |
| **Visualization** | `folium`, `matplotlib`, `contextily` | Interactive Web maps and static publication-ready figures |
| **Data Processing**| `pandas`, `numpy` | Tabular aggregation and data transformation |

---

## 🌐 Data Sources

This project uses public datasets provided under open government licenses:

1. **City of Burnaby Open Data Portal**:
   - Park Boundaries (`burnaby_parks.geojson`)
   - Park Amenities & Facilities (`burnaby_park_amenities.geojson`)
   - Trail Networks (`burnaby_trails.geojson`)
   - Neighborhood Planning Areas (`burnaby_neighborhoods.geojson`)
2. **Metro Vancouver Open Data**:
   - Regional Parks & Protected Areas (e.g., Central Park, Burnaby Mountain Regional Park, Deer Lake Park)
3. **OpenStreetMap**:
   - Pedestrian walkways, crosswalks, and transit connections extracted via `osmnx`.

---

## 📂 Project Structure

```text
burnaby-parks-gis/
├── data/
│   ├── raw/                  # Downloaded raw datasets (GeoJSON, SHP)
│   ├── processed/            # Cleaned, reprojected GeoPackages
│   └── outputs/              # Exported maps, CSV reports, and charts
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_spatial_analysis.ipynb
│   └── 03_walkability_mapping.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py        # API & Open Data fetchers
│   ├── geo_processing.py     # Buffer, CRS transform, spatial join logic
│   ├── analytics.py          # Acreage, density, and walkability metrics
│   └── visualization.py      # Folium map builder & Matplotlib styling
├── scripts/
│   └── run_analysis.py       # Main CLI executable
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have GDAL dependencies installed on your system. Using **Conda** or a **virtual environment** is recommended.

### 2. Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/your-username/burnaby-parks-gis.git
cd burnaby-parks-gis

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

*Note for GDAL/Fiona users on Windows/Mac:* If you encounter issues installing `geopandas` via `pip`, install using `conda`:
```bash
conda env create -f environment.yml
conda activate burnaby-gis
```

### 3. Usage

#### Run Full Analysis Pipeline
Execute the automated script to fetch data, compute metrics, and generate maps:

```bash
python scripts/run_analysis.py --neighborhood Metrotown --buffer 800 --output-map output_metrotown.html
```

#### Python API Example

```python
from src.data_loader import load_burnaby_parks
from src.geo_processing import calculate_park_access_buffer
from src.visualization import create_interactive_park_map

# Load Burnaby Parks GeoDataFrame
gdf_parks = load_burnaby_parks(epsg=26910)

# Calculate 10-minute (800m) walkability buffers
gdf_buffers = calculate_park_access_buffer(gdf_parks, distance_meters=800)

# Build interactive Folium map
park_map = create_interactive_park_map(gdf_parks, gdf_buffers)
park_map.save("data/outputs/burnaby_parks_walkability.html")
print("Map successfully generated!")
```

---

## 📊 Example Outputs

- **Interactive Web Maps**: Standalone HTML files containing layer toggles for:
  - Dog Off-Leash Areas
  - Playgrounds & Spray Pads
  - Trail Difficulty Levels
  - 15-Minute Walk Isochrones
- **Neighborhood Summary Tables**:
  | Neighborhood | Total Parks | Total Area (ha) | Park Area per Capita (m²) | Walkability Index |
  | :--- | :--- | :--- | :--- | :--- |
  | **Metrotown** | 14 | 48.2 | 8.6 | High |
  | **Brentwood** | 11 | 32.5 | 7.2 | Moderate |
  | **Deer Lake** | 4 | 204.1 | 54.3 | High |
  | **SFU / UniverCity**| 6 | 320.0 | 68.1 | High |

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 🤝 Contributing & Acknowledgments

- Data provided by the **City of Burnaby Open Data Portal** and **Metro Vancouver Open Data**.
- Built with standard open-source geospatial Python tools (`geopandas`, `folium`, `shapely`).
- Contributions, issue reports, and pull requests are welcome!
README.md
Displaying README.md.
