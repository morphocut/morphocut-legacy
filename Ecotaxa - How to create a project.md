# EcoTaxa: How to create a project

To create your first project, you must contact the application manager: [Marc Picheral (marc.picheral@obs-vlfr.fr)](mailto:marc.picheral@obs-vlfr.fr).

Then you will be allowed to create new projects.

# How to prepare data

  In a folder place: 

- image files

  ​       Colour and 8-bits greyscale images are supported, in `jpg`, `png`,`gif` (possibly animated) formats.     

- a `tsv`  (TAB separated file) which can be .txt or .tsv extension. File name must start with ecotaxa (ecotaxa*.txt or ecotaxa*.tsv)

  ​       It contains the metadata for each image. This file can be created in a spreadsheet application (see formats and examples below).                Line 1 contains column headers         Line 2 contains data format codes; [f] for floats, [t] for text         Line 3...n contain data for each image            

   The metadata and data for each image is organised in various levels  (image, object, process, sample, etc.). All column names must be  prefixed with the level name (`img_***`, `object_***`,  etc.). Some common fields, used to filter data, must be named and  sometimes formatted in a certain way (required format in blue), which is  documented below. But, overall, the only two mandatory fields are `img_file_name` and `object_id` (in red).    

- IMAGE

- - `img_file_name` [t]: name of the image file in the folder (including extension)
  - `img_rank` [f] : rank of image to be displayed, in case of existence of multiples (<10) images for one object. Starts at 1.

- OBJECT: one object to be classified, usually one organism. One object can be represented by several images. In this `tsv` file, there is one line per image which means the object data gets repeated on several lines.

- - `object_id` [t] : unique object name (will be displayed in Ecotaxa object page)
  - `object_link` [f] : URL of an associated website
  - `object_lat` [f] : latitude, decimal degrees
  - `object_lon` [f] : longitude, decimal degrees
  - `object_date` [f] : ISO8601 YYYYMMJJ UTC
  - `object_time` [f] : ISO8601 HHMMSS UTC
  - `object_depth_min` [f] : minimum depth of object, meters
  - `object_depth_max` [f] : maximum depth of object, meters

- ​     And, for already classified objects     

- - `object_annotation_date` [t] : ISO8601 YYYYMMJJ UTC
  - `object_annotation_time` [t] : ISO8601 YYYYMMJJ UTC
  - `object_annotation_category` [t] : class of the object
  - `object_annotation_person_name` [t] : name of the person who identified the object
  - `object_annotation_person_email` [t] : email of the person who identified the object
  - `object_annotation_status` [t] : predicted, dubious, or validated

- ​     And additional object-related fields     

- - `object_***` [f] or [t] : other fields relative to the object

- ACQUISITION: metadata relative to the image acquisition

- - `acq_id` [t] : unique identifier
  - `acq_instrument` [t] : name of the instrument (UVP, ZOOSCAN, FLOWCAM, etc.)
  - `acq_***` [f] or [t] : other fields relative to the acquisition

- PROCESS: metadata relative to the processing of the raw images

- - `process_id` [t] : unique identifier
  - `process_***` [f] or [t] : other fields relative to the process

- SAMPLE: a collection event

- - `sample_id` [t] : unique identifier
  - `sample_***` [f] or [t] : other fields relative to the sample



You can download example tsv files 

- [Minimal example](http://ecotaxa.obs-vlfr.fr/static/examples/ecotaxa_table_minimum.tsv), for fully manual entry
- [Full featured example, with unknown](http://ecotaxa.obs-vlfr.fr/static/examples/ecotaxa_table_without_classification.tsv) objects only
- [Full featured example, with already classified](http://ecotaxa.obs-vlfr.fr/static/examples/ecotaxa_table_with_classification.tsv) objects



Several such importation folders can be placed alongside each other  in a main folder. Pointing at that main folder will import all  subfolders recursively. EcoTaxa will read all `tsv` files and then import the images they point to. When "Skip `tsv` that have already been imported" is ticked, the names of `tsv`  files are recorded and those already imported are not re-imported. For  ongoing projects, this allows to simply put new data alongside the old  import folders and have EcoTaxa only import the new ones.

  So overall, the hierarchy can look like 

-  import_folder

- -  my_data_1

  - -  img_1.jpg
    -  img_2.jpg
    -  img_3.jpg
    -  table.tsv

  -  my_data_2

  - -  description.tsv
    -  DCN001.jpg
    -  IMG234.png
    -  anim.gif