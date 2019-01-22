# Lead Eagle - Tasks

## Week 1 (18-11-26)

Basic proof of concept.

- [x] Image import 
- [x] Image segmentation
- [x] Measurements
- [x] Data export

## Week 2 (until 18-12-04)

- [x] Extend number of extracted features
  - Use OpenCV shape features
- [ ] ~~Fix export format~~
- [x] Learn Vue.js

## Week 3 (18-12-10)

Create a basic web application.

- [x] Fix export format (i.e. [t], [f])

## Week 4 (18-12-17)
- [x] UI: Browse & Create datasets
- [x] UI: Upload Files
  - https://serversideup.net/uploading-files-vuejs-axios/
- [x] Backend: Index files
- [x] DB-Model: Dataset (<u>ID</u>, name, path), File (<u>Dataset ID, subpath</u>, modification time, size)
  - http://flask-sqlalchemy.pocoo.org/2.3/models/
- [ ] UI: Browse files
- [ ] API:
  - `/api/datasets/<id>/files/<path>`
  - `/api/projects/<id>`

## Week 5 (19-01-07)
Fixes.

- [ ] Fix and cleanup Upload: Do not compress
- [ ] Fix EcoTaxa zip (only one ecotaxa_* file)
- [x] Apply Martin's remarks
- [X] Refactor `/api` into its own Blueprint to keep the main application file clean
- [ ] UI: Browse & Create projects
- [X] Create sensible visual structure: Headline for navigation
- [ ] Remove absolute references to `http://localhost:5000`
- [ ] Implement Auth analogously to MorphoCluster
    - + Command for creating users

## Week 6 (19-01-14)

- [x] Pfade anpassen (Konfigurierbares Datenverzeichnis)

## Week 7 (19-01-21)

- [ ] Make download work
- [ ] Include contour images in ecotaxa export
- [ ] Draw contours only for one object in single-object image ("Vignette")
- [ ] Intra-Node computation with `graph.Sequential` (see `experiments.graph`)
- [ ] Tests

## Week 8

Implement processing nodes.

- [ ] UI: Browse & Create processing nodes
  - [ ] Api:
    - `/projects/<id>/nodes/<id>`
  - [ ] DB-Model: Node (<u>ID</u>, name, class), Edge (<u>from ID, from slot, to ID, to slot</u>)
  - [ ] Node 1: Dataset Source
    - Read file index of dataset
    - Parse file names
    - Extract object ID (default: filename)
    - [Extract parent object ID (for later stitching)]
    - [Use index file to provide metadata]
  - [ ] Node 2: Processing
    - Do everything (segmentation, object extraction, ...) in one step and write results to the database
  - [ ] Node 3: Export Sink
    - [ ] Generate EcoTaxa Export
