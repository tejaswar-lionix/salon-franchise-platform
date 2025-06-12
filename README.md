# Multi-Tenant Salon/Spa/Fitness Studio Franchise Management Platform

Handles scheduling across many locations with staff certifications/specialties, inventory per location, franchise royalties, loyalty across franchise.

## Architecture
- **Backend:** Django 4.2 + DRF + Celery, PostgreSQL (sqlite fallback)
- **Frontend:** React 18 + Vite
- **15 Apps:** locations, staff, scheduling, inventory, franchise, loyalty, customers, services, pos, reports, api, frontend, analytics, integrations, compliance

## Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build
```bash
make build
docker build -t salon-franchise .
npm run build
```

## Run
```bash
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
npm run dev
docker-compose up
```

## Tests
```bash
pytest -q
```

## Features
- **Scheduling:** `staff certs/specialties` e.g., `color specialist` can do `color` but `junior` cannot, double-booking check
- **Inventory:** `retail per location` `stock 20, par 30 → order 10`
- **Franchise:** `royalty 6% of gross`, `FDD`, territory `5-mile radius`
- **Loyalty:** `points 1 per $1`, tiers `silver/gold/platinum`, works across all locations

## License
Proprietary
