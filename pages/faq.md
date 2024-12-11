---
title: FAQ
description: Frequently Asked Questions
permalink: /faq/
toc: true
---

{:id="x"}
## How do I do x

Text

field 1 | field 2
--- | ---
x | 1
y | 2

```SQL
SELECT * FROM table
```

{:id="y"}
## How do I do y

...

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

todo

{:id="merge"}
## How to merge data packages describing different projects?

By design, a single camtrap-dp data package describes a single project. However, there are some use cases (for example a meta analysis), where merging multiple data packages could be helpful.

We provide an [R package](https://inbo.github.io/camtrapdp/) to read and manipulate camtrap-dp data packages. The R package contains the [merge function](https://inbo.github.io/camtrapdp/reference/merge_camtrapdp.html) that can be used to merge two data packages into one. The resulting data package is in valid camtrap-dp format and can be published.

Read the merge function documentation on how particular fields are merged in order to avoid loss of information. Please note that when merging x and y data packages, the `project$samplingDesign` field in the resulting package will be set to the value of `project$samplingDesign` from data package x. Because of that, we recommend only merging data packages for projects using the same sampling design.

