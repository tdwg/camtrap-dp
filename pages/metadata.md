---
layout: profile
title: Metadata
description: 
permalink: /metadata/
---

Metadata in Camtrap DP are expressed in a `datapackage.json` file. It follows the [Data Package](https://specs.frictionlessdata.io/data-package/#specification) specifications and includes generic **Data Package properties** and specific **Camtrap DP properties**. Properties indicated with `*` are required (i.e. cannot be empty).

For a full example, see [this `datapackage.json`](https://raw.githubusercontent.com/tdwg/dwc-for-biologging/403f57db105982dc05b70f3cf66fd2b5591798db/derived/camtrap-dp/data/raw/datapackage.json).
Property | From | Comment
--- | --- | ---
[`resources`](https://specs.frictionlessdata.io/data-package/#resources)* | Data Package | Additional requirements [below](#resources).
[`profile`](https://specs.frictionlessdata.io/data-package/#profile)* | Data Package | Additional requirements [below](#profile).
[`name`](https://specs.frictionlessdata.io/data-package/#name) | Data Package
[`id`](https://specs.frictionlessdata.io/data-package/#id) | Data Package
[`created`](https://specs.frictionlessdata.io/data-package/#created)* | Data Package | Required in Camtrap DP.
[`title`](https://specs.frictionlessdata.io/data-package/#title) | Data Package
[`contributors`](https://specs.frictionlessdata.io/data-package/#contributors)* | Data Package | Required in Camtrap DP.
[`organizations`](#organizations) | Camtrap DP
[`description`](https://specs.frictionlessdata.io/data-package/#description) | Data Package
[`version`](https://specs.frictionlessdata.io/data-package/#version) | Data Package
[`keywords`](https://specs.frictionlessdata.io/data-package/#keywords) | Data Package
[`image`](https://specs.frictionlessdata.io/data-package/#image) | Data Package
[`homepage`](https://specs.frictionlessdata.io/data-package/#homepage) | Data Package
[`sources`](https://specs.frictionlessdata.io/data-package/#sources) | Data Package
[`licenses`](https://specs.frictionlessdata.io/data-package/#licenses) | Data Package | Additional requirements [below](#licenses).
[`rightsHolder`](#rightsholder) | Camtrap DP
[`bibliographicCitation`](#bibliographiccitation) | Camtrap DP
[`project`](#project)* | Camtrap DP
[`spatial`](#spatial)* | Camtrap DP
[`temporal`](#temporal)* | Camtrap DP
[`taxonomic`](#taxonomic)* | Camtrap DP
[`references`](#references) | Camtrap DP
[`platform`](#platform) | Camtrap DP

---
