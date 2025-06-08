# Planet Hunter

🪐 A Python-based space probe for your Kubernetes cluster that hunts NASA's Exoplanet Archive for potential Earth-like worlds.

---

## 🚀 Overview
Planet Hunter queries NASA's exoplanet database using their TAP API, applies configurable filters to identify Earth-like candidates, and prints matches to the terminal. It’s designed to be containerized and deployed to a Raspberry Pi cluster running K3s.

## 🧪 Features
- Queries NASA's Exoplanet Archive using ADQL
- Full dataset scan of confirmed exoplanets
- Filters for Earth-like planets based on modular criteria
- Modular, configurable filters (radius, orbital period, equilibrium temp, star temp, radius)
- Partial match logic to broaden discovery scope
- Built-in retry + timeout logic for robust requests
- Docker + Kubernetes ready
- Logs discovered candidates into timestamped files
- Can be run as a Kubernetes Job or CronJob
- Fully containerized via Docker

## 🧰 Requirements
- Python 3.7+
- `requests` library
- Optional: Docker, K3s, kubectl, Helm

---

## 🔧 Usage
### Run locally
```bash
pip install requests
python planet_hunter.py
```

---

## 🐳 Container Build
```bash
docker build -t youruser/planet-hunter:latest .
docker push youruser/planet-hunter:latest
```

### 🐳 Run Container Locally (optional)
```bash
sudo docker run --rm ashwreaper/planet-hunter:latest
```

## ☁️ Kubernetes Deployment
#### As a Job
```bash
kubectl apply -f k8s_job.yaml
```

#### As a CronJob (Midnight UTC)
```bash
kubectl apply -f k8s_cronjob.yaml
```

This will write logs to:
```
/var/log/planet-hunter/earth_candidates_<timestamp>.log
```
on the master node.

## Environment Variables
- `REQUIRE_ALL_CRITERIA`: Set to `true` to require all match criteria, `false` to match on any (default: `false`)

---

## 📂 Project Structure
```
planet-hunter/
├── planet_hunter.py         # Main logic
├── planet_filters.py        # Modular filtering logic
├── Dockerfile               # Container definition
├── k8s_job.yaml      # K8s manifest
├── k8s_cronjob.yaml      # K8s manifest
└── README.md
```

---

## 🧙 Author
Built by space-coding pirates on a mission to map the cosmos — byte by byte 🌌💾
