# Lead Eagle

Generic image processing pipeline.

> Here we propose the **self-learning Helmholtz Imaging Pipeline** (sHIP) for **collaborative online  processing** of biological, medical, oceanographic and remote sensing imagery. Image processing often consists of **three basic processing steps: 1) segmentation** of one or several regions of interest (ROI) from the remaining image, **2) quantification** of certain characteristics such as the size, shape, color or texture of a given ROI and **3) classification** of a given ROI.

## Inspiration

- http://scantailor.org/
- http://brain-maps.org/index.php?action=viewslides&datid=89&start=41

## File formats

- (DICOM Supplement 145: Whole Slide Microscopic Image IOD and SOP Classes)[ftp://medical.nema.org/medical/dicom/final/sup145_ft.pdf]
- HDF5
  - Large arrays
  - Chunked, compressed storage
  - Easy interfacing: https://www.h5py.org/
  - Discussion:
    - https://cyrille.rossant.net/moving-away-hdf5/
    - https://cyrille.rossant.net/should-you-use-hdf5/
    - http://blog.khinsen.net/posts/2016/01/07/on-hdf5-and-the-future-of-data-management/
- NetCDF4
  - Built upon HDF5
- [TileDB](https://docs.tiledb.io/en/latest/index.html)
  - Speed
  - Compression
  - "immutable, append-only fragments" -> secure
  - concurrent reads and writes
  - Discussion: https://github.com/pangeo-data/pangeo/issues/120

## Tiling of large images

- Software
  - https://leafletjs.com/
  - https://www.npmjs.com/package/vue2-leaflet
  - https://stackoverflow.com/questions/17187161/bounding-view-of-a-leaflet-image-map-to-a-landscape-viewport
  - https://iime.github.io/virtualmicroscope/
  - https://stackoverflow.com/a/31529463/1116842
  - https://stackoverflow.com/a/17199400/1116842

- Tile size: 256 / 512px?

| Zoom | Number of tiles |                          |
| ---- | --------------- | ------------------------ |
| 0    | 1               | Whole image in one tile. |
| 1    | 4               |                          |
| 2    | 8               |                          |



## Backend

- Flask
- PostgreSQL / PostGIS
- SQLAlchemy Core + ORM
- [GeoAlchemy](https://geoalchemy-2.readthedocs.io/en/latest/index.html) (extension to [SQLAlchemy](http://sqlalchemy.org) for working with spatial databases)
- Pandas
- [RQ](http://python-rq.org/) / [Flask-RQ2](https://flask-rq2.readthedocs.io/en/latest/)
- [Redis](https://redis.io/)

## Frontend

- Vue
- [Leaflet](https://leafletjs.com/)
- [vue2-leaflet](https://www.npmjs.com/package/vue2-leaflet)
- Image enhancement: http://camanjs.com/
- https://github.com/Norkart/Leaflet-MiniMap

**Attention:** Make sure to include Leaflet css.

## Modules

- **Data import:** Read and index input files (Image location $\mapsto$ Image collection)
  - Tokenize filenames
    - regex
    - https://pypi.org/project/parse/
  - Later include HTTP/FTP-Upload
  - Read EXIF info
  - HTTP directory upload
    - https://stackoverflow.com/a/5849341/1116842
    - https://serversideup.net/uploading-files-vuejs-axios/
    - https://serversideup.net/drag-and-drop-file-uploads-with-vuejs-and-axios/
    - https://github.com/rowanwins/vue-dropzone
- **Restrict working area**
  - User draws bounding box for the area that should be handled
- **Lighting / shading / vignetting correction **(Image collection (N) $\mapsto$ Image collection (N))
  - Obtain correction image with gaussian filter: Leong et al. 2003. Correction of uneven illumination (vignetting) in digital microscopy images 
  - Maybe improve with local background extraction and impainting of foreground objects:
    - [Local Otsu](http://scikit-image.org/docs/dev/auto_examples/xx_applications/plot_rank_filters.html#image-threshold)
    - [Inpainting](https://docs.opencv.org/3.4/df/d3d/tutorial_py_inpainting.html)
- **Frame stitching:** Stitch images to make a whole
  - https://docs.opencv.org/trunk/d8/d19/tutorial_stitcher.html: Does not directly work; not enough features?
  - https://github.com/opencv/opencv/blob/master/samples/cpp/stitching_detailed.cpp
  - https://www.pyimagesearch.com/2016/01/11/opencv-panorama-stitching/
  - [Log-polar Transform](https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#logpolar)? 
  - Black box optimization?
- **Segmentation:** Extract individual segments (Image collection (N) $\mapsto$ Mask collection (M))
  - Thresholding (various techniques: Otsu, Quantiles, ...)
  - Deep learning
  - Object size threshold
  - Use uploaded segmentations
- **Edit Segmentation** (Mask collection (M) | Image collection (N) $\mapsto$ Mask collection (M))
  - Merge segments
  - Split segments
  - Manually draw segments
  - http://leaflet.github.io/Leaflet.draw/docs/leaflet-draw-latest.html#leaflet-1-0-examples
- **Measurement:** Measurement of object/shape features (Mask collection (M) $\mapsto$ Mask collection (M))
  - [Contours in OpenCV](https://docs.opencv.org/3.1.0/d3/d05/tutorial_py_table_of_contents_contours.html)
  - [skimage.measure.regionprops](http://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.regionprops)
  - Which one is better?
  - [Implementation by Jean-Olivier Irisson](https://github.com/jiho/apeep/blob/master/segment.py)
  - [skimage.morphology.skeletonize](http://scikit-image.org/docs/dev/auto_examples/edges/plot_skeleton.html)
- **Classification**
  - Manually
  - Automatically
    - Random Forest
    - Deep learning
- **Data export**
  - CSV and image files
  - Export measurements in `object_*` columns
  - Option: Augment Object of Interest?

## Data

### ImageBlob

- ImageBlobID
- Path
- Metadata
- Axes order (x, y, z, channels, time, ...)
- Axes resolution / meaning
- File type

### Object

- ObjectID
- ImageBlobID
- Bounding Box (PostGIS)
- Metadata
- Mask (1bit PNG)

### Task

One of the modules (import/export/calculations/...)

- TaskID
- Parameters
- Type

## Long-running jobs

Everything that takes more than 0.5s-1s.

- Use [Flask-RQ2](https://flask-rq2.readthedocs.io/en/latest/) to enqueue background jobs.

- API:

  - `POST /api/jobs/`: Create a job
    Response:  `202 Accepted, Location: /api/jobs/<jobid>`
  - ...

- Resources:

  - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs
  - https://farazdagi.com/2014/rest-and-long-running-jobs/
  - https://flask-marshmallow.readthedocs.io/en/latest/

## Misc

- Splitting metadata field: https://stackoverflow.com/questions/38231591/splitting-dictionary-list-inside-a-pandas-column-into-separate-columns
- Cache file handles for image blobs: https://cachetools.readthedocs.io/en/latest/#extending-cache-classes
  - Might be an improvement when tiles have to be rendered

## Paths (=Blueprints)

- `/blobs/<imgblobid>`: Raw blob (might be large)
- `/blobs/<imgblobid>/tiles/<z>/<x>/<y>`: Tiles of a large image
- `/masks/<objid>.png?color=<color>`: Mask for a specific object (for overlay)

## Manual Segmentation

- Annotations:
  - **Skeleton:** Connect inner parts of an object (certainly foreground).
  - **Outline:** Draw the object boundaries (certainly background).
  - **Point:** Designate an object.
- Application cases:
  - **Connect oversegmented parts of an object:** Draw skeleton lines connecting the individual segments.
  - **Split touching objects:** Place markers on the respective object centers. The segment pixels will be assigned to object with the nearest annotation.
  - **Separate overlapping objects:** After placing markers, draw skeleton lines of each object. The segment pixels will be assigned to object with the nearest annotation. Refine with object outlines.

## Environment

- Python 3.7

## Module-UI-interaction

A processing node provides a data structure that completely describes the required configuration settings.

- https://www.npmjs.com/package/vue-form-generator

## API

- REST
- No framework (Flask-RESTful, Flask-Restless, ...) because too inflexible.
- http://www.bradcypert.com/writing-a-restful-api-in-flask-sqlalchemy/

## Database

- SQLAlchemy ORM
- http://flask-sqlalchemy.pocoo.org/2.3/models/

## Computation Graph

- Model
  - NodeClass (<u>class_name</u>, FQN)
  - NodeInstance (<u>ID</u>, name, class, config)
    - config: JSON object of configuration values
  - Slots (<u>node_id</u>, <u>name</u>, [dtype])
  - Edge (<u>from ID, from slot, to ID, to slot</u>)
  - Object (project_id, parent_id)
  - Facet (<u>node id, object id, slot id</u>, meta)
    - FK: node id, object id, slot id
    - meta: metadata
  - ImageData (url, data)
    - FK: facet_id / node id, object id, slot id
    - URL: URL to image file on disk
    - data: Byte string of image data (e.g. PNG) (Optional)
    - Bounding Box: Bounding box in the on disk file to select a subarea

## Intra-node computation

- One node may consist of multiple chained operations.

- The Elements of the chain pass data in dicts

- Implemented with generators

  ```python
  seq = Sequential([DataLoader(path, ...), Processor(params...), Export(path)])
  seq.process()
  ```

- Data loader class: ~ import_data

  - Reads files, loads images

  - Outputs single image as object

    ```
    {
        object_id: ...
        [create: True,]
        facets: {
        	# For DataLoader
            input_data: {
                meta: {filename: ...},
                image: <np.array of shape = [h,w,c]>,
                [create: True,]
            },
            # For Processor
            raw_img: {
                meta: {region props...},
                image: <np.array of shape = [h,w,c]>
            },
            contour_img: {
                meta: {},
                image: <np.array of shape = [h,w,c]>
            },
           	# Nothing for export
        }
    }
    ```

- Vignetting correction: `__init__(self, input_facet: str, output_facet: str, [params...])`

- Image Segmentation class: ~ process_single_image
  `__init__(self, input_facet: str, output_facet: str, min_object_area=None, padding=None, ...)`

  - Iterates over values of data generator
  - Outputs single ROI as object

- Ecotaxa export class: ~ export_data

  `__init__(self, input_facet: str, output_facet: str, output_path, ...)`

  - Iterates over values of segmentation
  - Writes ZIP

- Database Persistence class

  - Reads objects dict
  - Creates object (if necessary, `create: True`)
  - Creates corresponding facets (if necessary, `create: True`)
  - Creates image files, stores `image_url`

  ```{
  {
     	object_id: ...
      create: true,
      facets: {
      	# For DataLoader
          input_data: {
              meta: {filename: ...},
              image: <np.array of shape = [h,w,c]>,
              create: true,
              image_url: ..., # When file is available on disk
          },
      }
  }`
  ```

### Full Pipeline

```python
Pipeline([
    DataLoader(import_path, output_facette="raw"),
    VignetteCorrector(input_facette="raw", output_facette="color"),
    RGB2Gray(input_facette="color", output_facette="gray"),
    ThresholdOtsu(input_facette="gray", output_facette="mask"),
    ExtractRegions(
    	mask_facette="mask",
    	image_facettes=["color", "gray"],
    	output_facet="features",
    	padding=10),
    FadeBackground(input_facette="gray", output_facette="gray_faded", alpha=0.5, color=1.0),
    DrawContours(input_facette="color", output_facette="color_countours"),
    Exporter(
    	"/path/to/archive.zip",
    	prop_facettes=["features"],
    	img_facettes=["gray_faded", "color", "color_contours"])
])
```



## Database persistence of objects

- After Data loader

- After Processing

- ```
  DatasetReader: 
  Converts files to objects
  
  for i in index:
  yield
  {
     	object_id: ...
      create: true,
      facets: {
          raw_image: {
              meta: {None},
              image: Image(files[i]),
              create: true,
          },
      }
  }
  
  When processing:
  
  for r in regions:
  yield
  {
     	object_id: parent_id + idx
      create: true,
      parent_id: parent_id,
      parent_bbox: ...
      facets: {
          mask: {
              image: Image,
          },
      }
  }
  
  
  Image class:
  	Image(filename, bbox=None)
  	get() -> np.ndarray
  ```

  

## Classification

- > Rainer: some objects are vignetted several times, 
  > because there is a big one that contains several small ones.

  Is this really the case? Then: https://docs.opencv.org/3.4/d9/d8b/tutorial_py_contours_hierarchy.html

  > Fred: Only the large one should be kept, although some smaller ones could be 
  > extracted as well. This is typical from a fecal aggregate for instance 
  > (a lager phytoplankton aggregates containing small fecal pellets and/or 
  > fragments a larger fecal pellets). This as such constitutes a category. 
  > I would keep them as it is. However, if it is possible to get info on 
  > what sort of FP are included in them, it's obviously relevant 
  > information.

-	Categories:

  -	Phytoplankton aggregates
  -	Fecal aggregates

  -	single cells (if any...)

  -	Cylindrical FP

  -	Ovoid FP

  -	unclear (we could put in this category what we are unsure off for now, 
    and decide later together)

## Authorization

- First step: Projects are owned by user. Only user may see data
- Later: Allow shared access to projects

## Data Storage

- Data is owned by project
- Storage location: `<root>/<user_id>/<project_id>/<node_id>/`
- Not in `static`!