---
title: FAQ
description: Frequently Asked Questions
permalink: /faq/
toc: true
---

{:id="bboxes"}
## How to describe bounding boxes of detected objects?

In the [observations](/data/#observations) table there are four terms used to describe bounding boxes: [`bboxX`](/data/#observations.bboxX), [`bboxY`](/data/#observations.bboxY), [`bboxWidth`](/data/#observations.bboxWidth), and [`bboxHeight`](/data/#observations.bboxHeight). The values for all these fields are numbers between 0 and 1, relative to the image size.

The `bboxX` and `bboxY` fields represent the coordinates of the top-left corner of the bounding box. `bboxX` is measured from the left edge of the image, while `bboxY` is measured from the top edge. `bboxWidth` represents the width of the bounding box, measured from its left edge to its right edge. Similarly, `bboxHeight` represents the height of the bounding box, measured from its top edge to its bottom edge.

{:id="multiple-events"}
## How to describe multiple events related to a single resource?

Multiple records in the observations table can reference the same media. See [this GitHub issue](https://github.com/tdwg/camtrap-dp/issues/39).

{:id="multi-camera"}
## How to handle multi-camera deployments?

See [this GitHub issue](https://github.com/tdwg/camtrap-dp/issues/328).

{:id="non-animal"}
## Can I describe plant or fungus observations using Camtrap DP?

Currently, possible values for the [`observationType`](/data/#observations.observationType) field in the observations table are: `animal`, `human`, `vehicle`, `blank`, `unknown` and `unclassified`. This definition does not allow for observations of plants or fungi. 

If you have a use case for describing non-animal observations using Camtrap DP, please let us know in [this GitHub issue](https://github.com/tdwg/camtrap-dp/issues/346).

{:id="measurements"}
## How to include measurements in a data package?

There are two ways to include additional information (values not covered by the standard fields) in a Camtrap DP:

### Using tags

Deployment and observation tables include [`deploymentTags`](/data/#deployments.deploymentTags) and [`observationTags`](/data/#observations.observationTags) fields. You can use these fields to store additional information as key:value pairs, separated by a pipe character (`|`). For example, this is how temperature and snow cover information could be represented in the deployment table:

deploymentID | deploymentTags
--- | ---
dep1 | temperature:20 &#x7c; snow_cover:false
dep2 | temperature:-5 &#x7c; snow_cover:true

There are some drawbacks to using this method. Storing additional information in the media table is not possible, since it does not contain a tags field. Additionally, data represented this way is difficult to parse.

### Using a custom table

You can add a custom table to the data package to store additional information. This requires providing a schema for the additional table. The schema must include a foreign key to the referenced table ([`deploymentID`](/data/#deployments.deploymentID), [`observationID`](/data/#observations.observationID), or [`mediaID`](/data/#media.mediaID)) and the additional fields. Here is an example schema for the deployment measurement table:

```json
{
    "name": "deployment-measurements",
    "title": "Deployment measurements",
    "description": "Table with weather measurements for deployments. Associated with deployments (`deploymentID`).",
    "fields": [
        {
            "name": "deploymentID",
            "description": "Identifier of the deployment. Foreign key to `deployments.deploymentID`.",
            "skos:broadMatch": "http://rs.tdwg.org/dwc/terms/parentEventID",
            "type": "string",
            "constraints": {
                "required": true
            },
            "example": "dep1"
        },
        {
            "name": "temperature",
            "description": "Temperature (in Celsius) at the time of the observation.)",
            "type": "number",
            "constraints": {
                "required": false,
                "minimum": -50,
                "maximum": 100
            },
            "example": 19.5
        },
        {
            "name": "snowCover",
            "description": "Snow cover present at the time of the observation.",
            "type": "boolean",
            "constraints": {
                "required": false
            },
            "example": true
        }
    ],
    "foreignKeys": [
        {
            "fields": "deploymentID",
            "reference": {
                "resource": "deployments",
                "fields": "deploymentID"
            }
        }
    ]
}
```

You need to add this table to the `datapackage.json` file in the [`resources`](/metadata/#resources) field.

This is an example table following the schema above:

deploymentID | temperature | snowCover
--- | --- | ---
dep1 | 20 | false
dep2 | -5 | true

We recommend this approach for storing additional information. It allows for easier parsing and merging of tables and is more flexible than using tags.

For more details, see [this GitHub issue](https://github.com/tdwg/camtrap-dp/issues/358).

{:id="merge"}
## How to merge data packages describing different projects?

By design, a single Camtrap DP data package describes a single project. However, there are some use cases (for example, a meta-analysis) where merging multiple data packages could be beneficial.

We provide an [R package](https://inbo.github.io/camtrapdp/) to read and manipulate Camtrap DP. The R package includes the [merge function](https://inbo.github.io/camtrapdp/reference/merge_camtrapdp.html) that lets you combine two data packages into a single valid Camtrap DP.

Consult the merge function documentation to understand exactly how specific fields are merged to avoid information loss. Please note that when merging data packages x and y, the [`project$samplingDesign`](/metadata/#project.samplingDesign) field in the resulting package will be set to the value of `project$samplingDesign` from data package x. Therefore, we recommend merging data packages only for projects that use the same sampling design.

{:id="parquet"}
## Can I use Parquet format instead of CSV for very large tables (>1M rows)?

[Apache Parquet](https://parquet.apache.org/) is an open source data file format, designed for efficient data storage and retrieval. `"mediatype": "application/vnd.apache.parquet"` is a [registered media type](https://www.iana.org/assignments/media-types/application/vnd.apache.parquet).

Frictionless framework can be used to read and write Parquet files after installing an [extension](https://framework.frictionlessdata.io/docs/formats/parquet.html). 
As of Camtrap DP [1.0.2](https://github.com/tdwg/camtrap-dp/releases/tag/1.0.2), the standard supports using Parquet files for storing data. This is an example of the `resources` section of the package metadata, adapted for using Parquet format files:

```
    "resources": [
        {
            "name": "deployments",
            "type": "table",
            "profile": "tabular-data-resource",
            "path": "deployments.parquet",
            "format": "parquet",
            "mediatype": "application/vnd.apache.parquet",
            "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/1.0.1/deployments-table-schema.json"
        },
        {
            "name": "media",
            "type": "table",
            "profile": "tabular-data-resource",
            "path": "media.parquet",
            "format": "parquet",
            "mediatype": "application/vnd.apache.parquet",
            "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/1.0.1/media-table-schema.json"
        },
        {
            "name": "observations",
            "type": "table",
            "profile": "tabular-data-resource",
            "path": "observations.parquet",
            "format": "parquet",
            "mediatype": "application/vnd.apache.parquet",
            "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/1.0.1/observations-table-schema.json"
        }
    ],
```

{:id="ask"}
## Have a question?

Don't see your question answered here?

[Ask it in our discussion forum](https://github.com/tdwg/camtrap-dp/discussions){:.btn .btn-primary}
