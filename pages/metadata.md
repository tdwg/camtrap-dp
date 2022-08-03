---
layout: profile
title: Metadata
description: 
permalink: /metadata/
---

Metadata in Camtrap DP are defined in a `datapackage.json` file. It follows the [Data Package](https://specs.frictionlessdata.io/data-package/#specification) specifications and includes default **Data Package properties** and specific **Camtrap DP properties**. The latter are presented below in human-readable form. Properties indicated with `*` are required (i.e. cannot be empty).

For a full example, see [this `datapackage.json`](https://raw.githubusercontent.com/tdwg/dwc-for-biologging/403f57db105982dc05b70f3cf66fd2b5591798db/derived/camtrap-dp/data/raw/datapackage.json).

## Data Package properties

- [`name`](https://specs.frictionlessdata.io/data-package/#name)
- [`id`](https://specs.frictionlessdata.io/data-package/#id)
- [`profile`](#profile)*
- [`created`](https://specs.frictionlessdata.io/data-package/#created)*
- [`licenses`](#licenses)
- [`sources`](https://specs.frictionlessdata.io/data-package/#sources)
- [`contributors`](https://specs.frictionlessdata.io/data-package/#contributors)*
- [`resources`](#resources)*: the data files, see [Data](../data/).

## Camtrap DP properties

- [`organizations`](#organizations)
- [`rightsHolder`](#rightsHolder)
- [`bibliographicCitation`](#bibliographicCitation)
- [`project`](#project)*
- [`spatial`](#spatial)*
- [`temporal`](#temporal)*
- [`taxonomic`](#taxonomic)*
- [`platform`](#platform)

---
