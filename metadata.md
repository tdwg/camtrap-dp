---
layout: metadata
title: Metadata
description: 
permalink: /metadata/
---

Metadata are defined in a `datapackage.json` file. It follows the [Tabular Data Package specs](https://specs.frictionlessdata.io/tabular-data-package/#specification) and includes default Data Package properties and specific Camtrap DP properties (defined below). For a full example, see this [datapackage.json](https://github.com/tdwg/dwc-for-biologging/blob/master/derived/camtrap-dp/data/raw/datapackage.json).

## Data Package properties

- [`name`](https://specs.frictionlessdata.io/data-package/#name)
- [`id`](https://specs.frictionlessdata.io/data-package/#id)
- [`created`](https://specs.frictionlessdata.io/data-package/#created)
- [`profile`](https://specs.frictionlessdata.io/data-package/#profile): `tabular-data-package`
- [`sources`](https://specs.frictionlessdata.io/data-package/#sources)
- [`contributors`](https://specs.frictionlessdata.io/data-package/#contributors)
- [`resources`](https://specs.frictionlessdata.io/data-package/#required-properties): three [Tabular Data Resources](https://specs.frictionlessdata.io/tabular-data-resource/), see [Tables](../tables/).

## Camtrap DP properties

- [`multimedia_access`](#multimedia_access)
- [`organizations`](#organizations)
- [`project`](#project)
- [`spatial`](#spatial): from Dublin Core
- [`temporal`](#temporal): from Dublin Core
- [`taxonomic`](#taxonomic)
- [`taxon_id_reference`](#taxon_id_reference)
- [`_platform_title`](#_platform_title)
- [`_platform_path`](#_platform_path)
- [`_platform_package_id`](#_platform_package_id)

---
