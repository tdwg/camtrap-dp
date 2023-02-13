---
title: Camtrap DP
background: /assets/home.jpg
permalink: /
description: Data exchange format for camera trap data
---

**Camera Trap Data Package** (or **Camtrap DP** for short) is a community developed data exchange format for camera trap data.

{:.alert .alert-warning}
Camtrap DP is [under development](https://github.com/tdwg/camtrap-dp/milestone/1) and not yet ready for production use.

## Usage

A Camtrap DP is a [Frictionless Data Package](https://specs.frictionlessdata.io/data-package/) that consists of:

File | Description
--- | ---
`datapackage.json`{:.d-inline-block style="width:150px;"} | [Metadata](https://tdwg.github.io/camtrap-dp/metadata/) regarding the data package and camera trap project.
`deployments.csv` | Table with camera trap [deployments](https://tdwg.github.io/camtrap-dp/data/#deployments).
`media.csv` | Table with [media](https://tdwg.github.io/camtrap-dp/data/#media) files captured by the camera traps.
`media-observations.csv` | Table with [observations](https://tdwg.github.io/camtrap-dp/data/#media-observations) that are classified at media level.
`event-observations.csv` | Table with [observations](https://tdwg.github.io/camtrap-dp/data/#event-observations) that are classified at event level.

## Example

[Example dataset](https://github.com/tdwg/camtrap-dp/tree/main/example) following Camtrap DP specifications.

## Validation

To allow validation, the `datapackage.json` of your dataset should reference the used version of Camtrap DP, both in `profile` and the resources' `schema`:

```json
{
   "name": "...",
   "profile": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/camtrap-dp-profile.json",
   "resources": [
      {
         "name": "deployments",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/deployments-table-schema.json"
      },
      {
         "name": "media",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/media-table-schema.json"
      },
      {
         "name": "media-observations",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/media-observations-table-schema.json"
      },
      {
         "name": "event-observations",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/<version>/event-observations-table-schema.json"
      }
   ]
}
```

You can validate your dataset against the specifications of Camtrap DP (and Frictionless Data Package) with:

```shell
pip install frictionless
frictionless validate path/to/your/datapackage.json
```

## Implementations

- [camtraptor](https://inbo.github.io/camtraptor): R package to read, explore and visualize Camtrap DP.
- [Agouti](https://agouti.eu): Data management platform, uses Camtrap DP as export format.
- [TRAPPER](https://os-conservation.org/projects/trapper): Data management platform, uses Camtrap DP as export format.

## Contribute

Questions? Suggestions? Contribute to the development of Camtrap DP by watching the [repository](https://github.com/tdwg/camtrap-dp) and participating in [issue discussions](https://github.com/tdwg/camtrap-dp/issues).

## Recommended citation

> Camtrap DP Development Team (2022) Camera Trap Data Package (Camtrap DP). <https://tdwg.github.io/camtrap-dp>

Camtrap DP is managed by the [Machine Observations Interest Group](https://www.tdwg.org/community/mobs/) of Biodiversity Information Standards (TDWG). It was originally developed by the [Open Science Conservation Fund](https://os-conservation.org/), the [Mammal Research Institute Polish Academy of Sciences (MRI PAS)](https://ibs.bialowieza.pl/en/) and the [Research Institute for Nature and Forest (INBO)](https://inbo.be/en).

Camtrap DP is endorsed the camera trap data management systems [Agouti](https://www.agouti.eu/), [eMammal](https://emammal.si.edu/), [TRAPPER](https://doi.org/10.1111/2041-210X.12571), [Wildlife Insights](https://www.wildlifeinsights.org/) and already available as an export format in some of these.
