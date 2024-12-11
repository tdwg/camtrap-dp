---
title: FAQ
description: Frequently Asked Questions
permalink: /faq/
toc: true
---

{:id="bboxes"}
## How to describe bounding boxes?

In camtrap-dp there are 4 terms used to describe bounding boxes: `bboxX`, `bboxY`, `bboxWidth` and `bboxHeight`. The values for all those fields are numbers between 0 and 1, relative to the image size.

The `bboxX` and `bboxY` fields are the coordinates of the top-left corner of the bounding box. `bboxX` is measured from the left side of the image and `bboxY` is measured from the top of the image. `bboxWidth` is measured from the left side of the bounding box to the right side of the bounding box. `bboxHeight` is measured from the top of the bounding box to the bottom of the bounding box.

{:id="multiple-events"}
## How to describe multiple events related to a single resource?

Multiple records in the observations table can reference the same media. See the [github issue](https://github.com/tdwg/camtrap-dp/issues/39).

{:id="multi-camera"}
## How to handle multi-camera deployments?

See the [github issue](https://github.com/tdwg/camtrap-dp/issues/328).

{:id="non-animal"}
## Can I describe plant or fungus observations using camtrap-dp?

Currently, possible values for the `observationType` field in the observations table are: `animal`, `human`, `vehicle`, `blank`, `unknown` and `unclassified`. This definition does not allow for observations of plants or fungi. 

If you have a use case for describing non-animal observations using camtrap-dp, please let us know in [this github issue](https://github.com/tdwg/camtrap-dp/issues/346).

{:id="measurements"}
## How to include measurements in a data package?

There are two ways to include additional information (values not covered by the standard fields) in a camtrap-dp data package:
- Using tags

Deployment and observation tables include `deploymentTags` and `observationTags` fields. These fields can be used to store additional information as pipe-delimited key:value pairs. For example, this is how temperature and snow cover information could be represented in the deployment table:

deploymentID | deploymentTags
--- | ---
dep1 | temperature:20 &#x7c; snow_cover:false
dep2 | temperature:-5 &#x7c; snow_cover:true

There are some drawbacks to using this method. Storing additional information in the media table is not possible, since it does not contain a tags field. Additionally, data represented this way is difficult to parse.

- Using a custom table

A custom table can be added to the data package to store additional information. This requires providing a schema for the additional table. This schema has to contain the foreign key to the referenced table (`deploymentID`, `observationID` or `mediaID`) and the additional fields. This in an example schema for the deployment measurement table:
```JSON
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

The schema has to be added to the `datapackage.json` file in the `resources` field.

This is an example table following the above schema:

deploymentID | temperature | snowCover
--- | --- | ---
dep1 | 20 | false
dep2 | -5 | true

We recommend this approach for storing additional information. It allows for easy parsing and merging of tables and is more flexible than using tags.

For more details, see [this github issue](https://github.com/tdwg/camtrap-dp/issues/358).


{:id="merge"}
## How to merge data packages describing different projects?

By design, a single camtrap-dp data package describes a single project. However, there are some use cases (for example a meta analysis), where merging multiple data packages could be helpful.

We provide an [R package](https://inbo.github.io/camtrapdp/) to read and manipulate camtrap-dp data packages. The R package contains the [merge function](https://inbo.github.io/camtrapdp/reference/merge_camtrapdp.html) that can be used to merge two data packages into one. The resulting data package is in valid camtrap-dp format and can be published.

Read the merge function documentation on how particular fields are merged in order to avoid loss of information. Please note that when merging x and y data packages, the `project$samplingDesign` field in the resulting package will be set to the value of `project$samplingDesign` from data package x. Because of that, we recommend only merging data packages for projects using the same sampling design.

