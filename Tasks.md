# Lead Eagle - Tasks

## Week 1 (18-11-26)

Basic proof of concept.

- [x] Image import 
- [x] Image segmentation
- [ ] Measurements
- [x] Data export

## Week 2 (until 18-12-04)

- [ ] Extend number of extracted features
  - Use OpenCV shape features
- [ ] ~~Fix export format~~
- [ ] Learn Vue.js

## Week 3 (18-12-10)

Create a basic web application.

- [x] Fix export format (i.e. [t], [f])

## Week 4 (18-12-17)
- [ ] UI: Browse & Create datasets
- [ ] UI: Upload Files
  - https://serversideup.net/uploading-files-vuejs-axios/
- [ ] Backend: Index files
- [ ] DB-Model: Dataset (<u>ID</u>, name, path), File (<u>Dataset ID, subpath</u>, modification time, size)
  - http://flask-sqlalchemy.pocoo.org/2.3/models/
- [ ] UI: Browse files
- [ ] API:
  - `/datasets/<id>/files/<path>`
  - `/projects/<id>`

## Week 5
Process datasets in projects.

- [ ] UI: Browse & Create projects
- [ ] UI: Browse & Create processing nodes
  - [ ] DB-Model: Node (<u>ID</u>, name, class), Edge (<u>from ID, from slot, to ID, to slot</u>)
  - [ ] Dataset Source
    - Read file index of dataset
    - Parse file names
  - Extract object ID (default: filename)
  - [Extract parent object ID (for later stitching)]
    - [Use index file to provide metadata]
  - [ ] Processing Node
    - Do everything (segmentation, object extraction, ...) in one step and write results to the database
  - [ ] Export Sink
    - [ ] Generate EcoTaxa Export

## Week 6

Split processing into individual steps.